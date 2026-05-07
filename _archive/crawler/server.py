# -*- coding: utf-8 -*-
"""
셀렙 외부 제품 크롤러 — 미니 웹 서버 (Stage 2)

기능:
  - 워크스페이스(상위 폴더)의 HTML 정적 파일 서빙
  - GET  /api/data     : 현재 products_output.json 내용 반환
  - POST /api/refresh  : crawl.py 실행 후 결과 반환
실행:
  python server.py  (또는 run_server.bat 더블클릭)
접속:
  http://localhost:5000/tubing_curated_demo.html
"""
import os
import sys
import json
import subprocess
from datetime import datetime

try:
    from flask import Flask, send_from_directory, jsonify, request, Response
except ImportError:
    print("[!] Flask 미설치. install_requirements.bat을 먼저 실행하세요.")
    print("    또는: pip install flask")
    sys.exit(1)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE = os.path.dirname(SCRIPT_DIR)  # 리드플루이드 페이지/
JSON_PATH = os.path.join(SCRIPT_DIR, "products_output.json")
CRAWL_PY = os.path.join(SCRIPT_DIR, "crawl.py")
LOG_PATH = os.path.join(SCRIPT_DIR, "crawl_log.txt")

app = Flask(__name__, static_folder=WORKSPACE, static_url_path='')


@app.route('/')
def home():
    """루트 → 큐레이션 데모 페이지"""
    return send_from_directory(WORKSPACE, 'tubing_curated_demo.html')


@app.route('/api/data')
def api_data():
    """현재 products_output.json 반환"""
    if not os.path.exists(JSON_PATH):
        return jsonify({
            "error": "아직 크롤링 결과 파일이 없습니다.",
            "hint": "먼저 '지금 스크랩하기' 버튼을 누르거나 run_crawl.bat을 실행하세요."
        }), 404
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        body = f.read()
    return Response(body, mimetype='application/json; charset=utf-8')


@app.route('/api/refresh', methods=['POST'])
def api_refresh():
    """crawl.py 실행 → 결과 요약 반환"""
    started_at = datetime.now().isoformat()
    try:
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        result = subprocess.run(
            [sys.executable, CRAWL_PY],
            cwd=SCRIPT_DIR,
            capture_output=True,
            text=True,
            timeout=300,
            input="\n",  # crawl.py 끝의 input("Press Enter") 즉시 통과
            encoding='utf-8',
            errors='replace',
            env=env,
        )
        ok = (result.returncode == 0)
        log_tail = ""
        if os.path.exists(LOG_PATH):
            with open(LOG_PATH, 'r', encoding='utf-8') as f:
                log_tail = f.read()[-2000:]

        # JSON 갱신 시각도 같이 반환
        last_updated = None
        if os.path.exists(JSON_PATH):
            try:
                with open(JSON_PATH, 'r', encoding='utf-8') as f:
                    last_updated = json.load(f).get("last_updated")
            except Exception:
                pass

        return jsonify({
            "ok": ok,
            "started_at": started_at,
            "finished_at": datetime.now().isoformat(),
            "returncode": result.returncode,
            "last_updated": last_updated,
            "stdout_tail": (result.stdout or "")[-1500:],
            "stderr_tail": (result.stderr or "")[-500:],
            "log_tail": log_tail,
        })
    except subprocess.TimeoutExpired:
        return jsonify({
            "ok": False,
            "error": "크롤링이 5분 안에 끝나지 않았습니다 (타임아웃). URL 수가 많으면 자연스러운 일이니 잠시 기다린 뒤 다시 시도해 주세요."
        }), 504
    except Exception as e:
        return jsonify({
            "ok": False,
            "error": f"{type(e).__name__}: {e}"
        }), 500


@app.route('/api/log')
def api_log():
    """현재 크롤 로그 반환 (디버깅용)"""
    if not os.path.exists(LOG_PATH):
        return Response("(로그 파일 없음)", mimetype='text/plain; charset=utf-8')
    with open(LOG_PATH, 'r', encoding='utf-8') as f:
        return Response(f.read(), mimetype='text/plain; charset=utf-8')


if __name__ == '__main__':
    print("=" * 60)
    print("  셀렙 외부 제품 크롤러 — 미니 서버")
    print("=" * 60)
    print()
    print(f"  접속: http://localhost:5000")
    print(f"        http://localhost:5000/tubing_curated_demo.html")
    print()
    print(f"  종료: Ctrl + C")
    print()
    print(f"  워크스페이스: {WORKSPACE}")
    print()
    print("=" * 60)
    print()
    app.run(host='127.0.0.1', port=5000, debug=False)
