# -*- coding: utf-8 -*-
"""
크롤러 — 외부 사이트 제품 정보 자동 수집
사용법: python crawl.py  (또는 run_crawl.bat 더블클릭)
입력: urls.txt (한 줄에 URL 하나)
출력:
  - products_output.csv   (부모 요약)
  - options_output.csv    (옵션 상세, 1부모=N행) ← Phase D
  - products_output.json  (HTML 자동 통합용, 옵션 포함)
  - external_cards.html   (HTML 카드 스니펫)
  - crawl_log.txt         (실행 로그)
"""
import os
import sys
import json
import time
import csv
import re
from copy import copy
from datetime import datetime
from urllib.parse import urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("[!] 의존성 미설치. install_requirements.bat을 먼저 실행하세요.")
    print("    또는 명령창에서: pip install requests beautifulsoup4 lxml")
    sys.exit(1)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
URLS_FILE = os.path.join(SCRIPT_DIR, "urls.txt")
CSV_OUT = os.path.join(SCRIPT_DIR, "products_output.csv")
OPTIONS_CSV_OUT = os.path.join(SCRIPT_DIR, "options_output.csv")
JSON_OUT = os.path.join(SCRIPT_DIR, "products_output.json")
HTML_OUT = os.path.join(SCRIPT_DIR, "external_cards.html")
LOG_FILE = os.path.join(SCRIPT_DIR, "crawl_log.txt")

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
TIMEOUT = 15

SITE_SELECTORS = {
    "shsigma.co.kr": {
        "name": ['h2#sit_title', 'meta[name="description"]', 'h1', '.product-name', '.item-name', '.goods-name'],
        "price": ['tr.tr_price strong', '.price', '.product-price', '.item-price', '.sale-price', '[class*="price"]'],
        "spec": ['meta[name="description"]', '.spec', '.product-spec', '.detail-info', '.product-info', '.summary'],
        "image": ['#sit_pvi_big img', 'meta[property="og:image"]', '.product-image img', '.item-image img', '.main-image img'],
        "site_label": "성호씨그마 (Sigma-Aldrich)"
    },
    "kolabshop.com": {
        "name": ['h1', '.product-name', '.item_name'],
        "price": ['.price', '.item_price', '.product-price'],
        "spec": ['.product-detail', '.item_detail'],
        "image": ['meta[property="og:image"]', '.product-image img'],
        "site_label": "코랩샵"
    },
    "allforlab.com": {
        "name": ['h1', '.product-name', '.goods_name'],
        "price": ['.price', '.goods_price'],
        "spec": ['.product_summary', '.goods_summary'],
        "image": ['meta[property="og:image"]', '.product-image img'],
        "site_label": "올포랩"
    },
    "_default": {
        "name": ['h1', 'meta[property="og:title"]', 'title'],
        "price": ['[class*="price"]', '[class*="Price"]'],
        "spec": ['meta[name="description"]', 'meta[property="og:description"]'],
        "image": ['meta[property="og:image"]'],
        "site_label": "외부 (확인 필요)"
    }
}

HIDDEN_SELECTORS = '.sound_only, .sr-only, .visually-hidden, [aria-hidden="true"]'


def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def detect_site(url):
    host = urlparse(url).netloc.replace("www.", "").lower()
    for key in SITE_SELECTORS:
        if key in host:
            return key
    return "_default"


def safe_select_text(soup, selectors):
    for sel in selectors:
        if sel.startswith("meta["):
            tag = soup.select_one(sel)
            if tag and tag.get("content"):
                return tag["content"].strip()
        else:
            tag = soup.select_one(sel)
            if tag:
                tag_copy = copy(tag)
                for hidden in tag_copy.select(HIDDEN_SELECTORS):
                    hidden.decompose()
                text = tag_copy.get_text(strip=True)
                if text:
                    return text
    return ""


def safe_select_image(soup, selectors, base_url):
    for sel in selectors:
        if sel.startswith("meta["):
            tag = soup.select_one(sel)
            if tag and tag.get("content"):
                return _resolve_url(tag["content"].strip(), base_url)
        else:
            tag = soup.select_one(sel)
            if tag:
                src = tag.get("src") or tag.get("data-src")
                if src:
                    return _resolve_url(src.strip(), base_url)
    return ""


def _resolve_url(url, base):
    if url.startswith("//"):
        return "https:" + url
    if url.startswith("/"):
        parsed = urlparse(base)
        return f"{parsed.scheme}://{parsed.netloc}{url}"
    if not url.startswith("http"):
        return base.rstrip("/") + "/" + url.lstrip("/")
    return url


def clean_price(text):
    if not text:
        return ""
    match = re.search(r'[\d,]+', text)
    return match.group(0) if match else text


def _format_price(num):
    try:
        return f"{int(num):,}"
    except (TypeError, ValueError):
        return str(num) if num else ""


def extract_options_shsigma(soup):
    options = []
    for inp in soup.select('tr.option_item input[name="it_value"]'):
        val = inp.get("value", "").strip()
        if not val:
            continue
        try:
            data = json.loads(val)
            options.append({
                "code": str(data.get("io_id", "")).strip(),
                "name": str(data.get("io_description", "")).strip(),
                "unit": str(data.get("io_unit", "")).strip(),
                "price": _format_price(data.get("io_price", "")),
                "price_dealer": _format_price(data.get("io_price_dealer", "")),
                "price_real": _format_price(data.get("io_price_real", "")),
                "stock": data.get("io_stock_qty", 0),
            })
        except (ValueError, TypeError):
            continue
    return options


def crawl_url(url):
    site_key = detect_site(url)
    config = SITE_SELECTORS[site_key]

    try:
        headers = {"User-Agent": USER_AGENT}
        resp = requests.get(url, headers=headers, timeout=TIMEOUT)
        resp.raise_for_status()
        if resp.encoding == "ISO-8859-1":
            resp.encoding = resp.apparent_encoding
        soup = BeautifulSoup(resp.text, "lxml")

        product = {
            "url": url,
            "site_key": site_key,
            "site_label": config["site_label"],
            "name": safe_select_text(soup, config["name"]),
            "price_raw": safe_select_text(soup, config["price"]),
            "spec": safe_select_text(soup, config["spec"]),
            "image_url": safe_select_image(soup, config["image"], url),
            "crawled_at": datetime.now().isoformat()
        }
        product["price"] = clean_price(product["price_raw"])

        options = []
        if site_key == "shsigma.co.kr":
            options = extract_options_shsigma(soup)
        product["options"] = options
        product["options_count"] = len(options)

        if options:
            try:
                nums = [int(o["price"].replace(",", "")) for o in options if o.get("price")]
                if nums:
                    product["price_min"] = _format_price(min(nums))
                    product["price_max"] = _format_price(max(nums))
                    if not product["price"]:
                        product["price"] = _format_price(nums[0])
                else:
                    product["price_min"] = product["price"]
                    product["price_max"] = product["price"]
            except (ValueError, AttributeError):
                product["price_min"] = product["price"]
                product["price_max"] = product["price"]
        else:
            product["price_min"] = product["price"]
            product["price_max"] = product["price"]

        if len(product["spec"]) > 300:
            product["spec"] = product["spec"][:300] + "..."

        if product["options_count"] > 1:
            price_log = f"{product['price_min']}~{product['price_max']} ({product['options_count']}종)"
        else:
            price_log = product["price"]
        log(f"OK [{site_key}] {product['name'][:40]}... / {price_log}")
        return product

    except requests.exceptions.RequestException as e:
        log(f"FAIL [{site_key}] {url} - {type(e).__name__}: {e}")
        return {"url": url, "site_key": site_key, "site_label": config["site_label"], "error": str(e), "crawled_at": datetime.now().isoformat()}
    except Exception as e:
        log(f"ERROR [{site_key}] {url} - {type(e).__name__}: {e}")
        return {"url": url, "error": str(e), "crawled_at": datetime.now().isoformat()}


def write_csv(products, path):
    fields = ["site_label", "name", "price", "price_min", "price_max", "options_count", "spec", "image_url", "url", "site_key", "crawled_at", "error"]
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for p in products:
            writer.writerow(p)


def write_options_csv(products, path):
    fields = ["parent_url", "site_label", "parent_name", "code", "option_name", "unit", "price", "price_dealer", "price_real", "stock"]
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for p in products:
            if "error" in p:
                continue
            base = {"parent_url": p.get("url", ""), "site_label": p.get("site_label", ""), "parent_name": p.get("name", "")}
            options = p.get("options") or []
            if options:
                for o in options:
                    row = dict(base)
                    row["code"] = o.get("code", "")
                    row["option_name"] = o.get("name", "")
                    row["unit"] = o.get("unit", "")
                    row["price"] = o.get("price", "")
                    row["price_dealer"] = o.get("price_dealer", "")
                    row["price_real"] = o.get("price_real", "")
                    row["stock"] = o.get("stock", "")
                    writer.writerow(row)
            else:
                writer.writerow(base)


def write_json(products, path):
    data = {
        "last_updated": datetime.now().isoformat(),
        "total": len(products),
        "succeeded": sum(1 for p in products if "error" not in p),
        "failed": sum(1 for p in products if "error" in p),
        "products": products
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def write_html_cards(products, path):
    cards = []
    for p in products:
        if "error" in p or not p.get("name"):
            continue
        if p.get("image_url"):
            img_html = f'<img src="{p["image_url"]}" alt="{p["name"]}" onerror="this.style.display=\'none\'">'
        else:
            img_html = '<span class="prod-img-fallback">📷</span>'
        if p.get("options_count", 0) > 1 and p.get("price_min") and p.get("price_max"):
            price = f'{p["price_min"]} ~ {p["price_max"]} 원'
        elif p.get("price"):
            price = f'{p["price"]} 원'
        else:
            price = "[참고]"
        spec = p.get("spec", "")[:120]
        name = p["name"][:80]
        card = f'''<a class="prod ext" href="{p['url']}" target="_blank" rel="noopener noreferrer">
  <div class="prod-img">{img_html}<span class="prod-tag ref">참고</span></div>
  <div class="prod-body">
    <div class="prod-name">{name}</div>
    <div class="prod-spec"><span class="label">스펙</span> <span class="val">{spec}</span></div>
    <div class="prod-foot">
      <div class="prod-seller">공급처<br><strong>{p['site_label']}</strong></div>
      <div class="prod-price ref">{price}</div>
    </div>
  </div>
</a>'''
        cards.append(card)
    html = f'''<!-- 자동 생성 — 마지막 업데이트: {datetime.now().strftime("%Y-%m-%d %H:%M")} -->
<!-- {len(cards)}개 외부 제품 카드 -->
<div class="ext-products-grid">
{chr(10).join(cards)}
</div>'''
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    print("=" * 60)
    print("  성호씨그마·코랩샵·올포랩 등 외부 제품 크롤러")
    print("=" * 60)
    print()

    if not os.path.exists(URLS_FILE):
        print(f"[!] {URLS_FILE} 파일이 없습니다.")
        print("    urls.txt 파일을 만들고 URL을 한 줄씩 입력해 주세요.")
        input("\nPress Enter to exit...")
        return

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(f"=== 크롤링 시작: {datetime.now().isoformat()} ===\n")

    urls = []
    with open(URLS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            urls.append(line)

    if not urls:
        log("urls.txt가 비어 있습니다. URL을 추가해 주세요.")
        input("\nPress Enter to exit...")
        return

    log(f"총 {len(urls)}개 URL 크롤링 시작")
    print()

    products = []
    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] {url[:70]}...")
        product = crawl_url(url)
        products.append(product)
        time.sleep(1)

    print()
    log(f"크롤링 완료: 성공 {sum(1 for p in products if 'error' not in p)}개 / 실패 {sum(1 for p in products if 'error' in p)}개")

    # Phase D+ (2026-05-01): 한 파일이 잠겨도 나머지는 저장되도록 개별 try/except
    write_steps = [
        ("products_output.csv",  write_csv,         CSV_OUT),
        ("options_output.csv",   write_options_csv, OPTIONS_CSV_OUT),
        ("products_output.json", write_json,        JSON_OUT),
        ("external_cards.html",  write_html_cards,  HTML_OUT),
    ]
    write_failures = []
    for name, fn, path in write_steps:
        try:
            fn(products, path)
        except PermissionError as e:
            msg = f"{name} 잠김 (Excel/메모장 열려있음). 닫고 다시 실행하세요. [{e}]"
            log("[!] " + msg)
            write_failures.append(name)
        except Exception as e:
            msg = f"{name} 저장 실패: {type(e).__name__}: {e}"
            log("[!] " + msg)
            write_failures.append(name)

    print()
    print("=" * 60)
    print("  완료. 결과 파일:")
    print(f"  - {os.path.basename(CSV_OUT)}      (부모 요약)")
    print(f"  - {os.path.basename(OPTIONS_CSV_OUT)}      (옵션 상세, 1부모=N행)")
    print(f"  - {os.path.basename(JSON_OUT)}     (HTML 자동 통합용)")
    print(f"  - {os.path.basename(HTML_OUT)}      (HTML 카드 스니펫)")
    print(f"  - {os.path.basename(LOG_FILE)}         (실행 로그)")
    print("=" * 60)
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
