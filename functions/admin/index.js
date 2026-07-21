// functions/admin/index.js
// 관리자 페이지 (/admin) — Basic Auth
//   · 상태별 개수 대시보드
//   · 브랜드/카테고리/상태/검색 필터
//   · 제품 표에서 공급가·소비자가·이미지URL·상태 인라인 수정 → /api/admin/products (PUT)
// 비밀번호는 코드에 박지 않고 Cloudflare 환경변수 ADMIN_PASSWORD 사용.

const REALM = 'rndsetup-admin';

export async function onRequest(context) {
  const { request, env } = context;

  const auth = request.headers.get('Authorization') || '';
  if (!checkAuth(auth, env)) {
    return new Response('인증이 필요합니다. (관리자)', {
      status: 401,
      headers: {
        'WWW-Authenticate': `Basic realm="${REALM}", charset="UTF-8"`,
        'content-type': 'text/plain; charset=utf-8',
      },
    });
  }

  // 인증 성공: API 호출에 재사용할 토큰을 페이지에 주입 (이미 인증된 세션에만 전달)
  const token = auth.slice(6); // "Basic " 이후의 base64
  return new Response(renderHTML(token), {
    headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store' },
  });
}

function checkAuth(auth, env) {
  const pw = env.ADMIN_PASSWORD || '';
  if (!pw) return false;
  if (!auth.startsWith('Basic ')) return false;
  let decoded = '';
  try { decoded = atob(auth.slice(6)); } catch { return false; }
  const i = decoded.indexOf(':');
  const pass = i >= 0 ? decoded.slice(i + 1) : decoded;
  return pass === pw;
}

function renderHTML(token) {
  return `<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>rndsetup 관리자</title>
<style>
  :root{ --green:#2f7d4f; --ink:#1a2430; --line:#e3e8ef; --muted:#5a6470; --bg:#f6f8fb; --navy:#1E3A5F; }
  *{ box-sizing:border-box; }
  body{ margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Malgun Gothic",sans-serif; color:var(--ink); background:var(--bg); }
  header{ background:var(--navy); color:#fff; padding:14px 22px; display:flex; align-items:center; justify-content:space-between; }
  header h1{ font-size:17px; margin:0; font-weight:700; letter-spacing:-.01em; }
  header .sub{ font-size:12px; color:#c7d3e2; }
  .wrap{ max-width:1400px; margin:0 auto; padding:20px 22px 60px; }

  .cards{ display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:12px; margin-bottom:20px; }
  .card{ background:#fff; border:1px solid var(--line); border-radius:12px; padding:16px 18px; cursor:pointer; transition:transform .1s,border-color .1s; }
  .card:hover{ transform:translateY(-2px); border-color:#c3ccd8; }
  .card.on{ border-color:var(--green); box-shadow:0 0 0 2px rgba(47,125,79,.15); }
  .card .n{ font-size:26px; font-weight:800; }
  .card .l{ font-size:13px; color:var(--muted); margin-top:2px; }
  .card.total .n{ color:var(--navy); }
  .card.ok .n{ color:var(--green); }
  .card.price .n{ color:#c47f16; }
  .card.img .n{ color:#b4453a; }

  .filters{ background:#fff; border:1px solid var(--line); border-radius:12px; padding:14px 16px; display:flex; flex-wrap:wrap; gap:10px; align-items:center; margin-bottom:16px; }
  .filters select,.filters input{ height:36px; border:1px solid var(--line); border-radius:8px; padding:0 10px; font-size:13.5px; color:var(--ink); background:#fff; }
  .filters input[type=text]{ min-width:200px; }
  .filters button{ height:36px; padding:0 16px; border-radius:8px; border:0; font-size:13.5px; font-weight:700; cursor:pointer; }
  .btn-go{ background:var(--green); color:#fff; }
  .btn-reset{ background:#eef1f5; color:var(--ink); }
  .filters .spacer{ flex:1; }
  .filters .hint{ font-size:12px; color:var(--muted); }

  .tablewrap{ background:#fff; border:1px solid var(--line); border-radius:12px; overflow:auto; }
  table{ border-collapse:collapse; width:100%; font-size:13px; }
  th,td{ padding:8px 10px; border-bottom:1px solid #eef1f5; text-align:left; vertical-align:middle; white-space:nowrap; }
  th{ background:#fafbfc; font-weight:700; color:var(--muted); position:sticky; top:0; z-index:1; font-size:12px; }
  tr.dirty td{ background:#fffbe9; }
  td .name{ white-space:normal; min-width:220px; max-width:320px; display:inline-block; line-height:1.35; }
  td.sku{ font-family:ui-monospace,monospace; font-size:12px; color:var(--muted); }
  .thumb{ width:44px; height:44px; object-fit:contain; border:1px solid var(--line); border-radius:6px; background:#fff; }
  .thumb.none{ display:flex; align-items:center; justify-content:center; font-size:10px; color:#b4453a; }
  input.p{ width:100px; height:32px; border:1px solid var(--line); border-radius:6px; padding:0 8px; font-size:13px; text-align:right; }
  input.url{ width:210px; height:32px; border:1px solid var(--line); border-radius:6px; padding:0 8px; font-size:12px; }
  select.st{ height:32px; border:1px solid var(--line); border-radius:6px; padding:0 6px; font-size:13px; }
  .save{ height:32px; padding:0 12px; border-radius:6px; border:0; background:var(--green); color:#fff; font-weight:700; font-size:12.5px; cursor:pointer; }
  .save:disabled{ opacity:.4; cursor:default; }

  .pager{ display:flex; justify-content:center; gap:6px; margin:18px 0 4px; flex-wrap:wrap; }
  .pager button{ min-width:34px; height:34px; padding:0 10px; border:1px solid var(--line); background:#fff; border-radius:8px; font-size:13px; font-weight:700; cursor:pointer; }
  .pager button.on{ background:var(--green); color:#fff; border-color:var(--green); }
  .pager button:disabled{ opacity:.4; cursor:default; }

  #toast{ position:fixed; left:50%; bottom:26px; transform:translateX(-50%); background:#1a2430; color:#fff; padding:10px 18px; border-radius:8px; font-size:13.5px; opacity:0; pointer-events:none; transition:opacity .2s; z-index:50; }
  #toast.on{ opacity:1; }
  #toast.err{ background:#b4453a; }
  .meta{ font-size:12.5px; color:var(--muted); margin:10px 2px; }
</style>
</head>
<body>
<header>
  <h1>rndsetup 제품 관리자</h1>
  <span class="sub">공급가 · 소비자가 · 이미지 · 상태 관리</span>
</header>
<div class="wrap">

  <div class="cards" id="cards"></div>

  <div class="filters">
    <select id="f-brand">
      <option value="">전체 브랜드</option>
      <option value="SH Scientific">SH Scientific</option>
      <option value="Leadfluid">Leadfluid</option>
      <option value="RUNZE">RUNZE</option>
      <option value="Alicat">Alicat</option>
    </select>
    <select id="f-status">
      <option value="">전체 상태</option>
      <option value="등록가능">등록가능</option>
      <option value="가격대기">가격대기</option>
      <option value="이미지대기">이미지대기</option>
    </select>
    <input type="text" id="f-sobun" placeholder="소분류(정확히 일치)">
    <input type="text" id="f-q" placeholder="상품명 / 모델 / SKU 검색">
    <button class="btn-go" id="btn-go">검색</button>
    <button class="btn-reset" id="btn-reset">초기화</button>
    <span class="spacer"></span>
    <span class="hint" id="count-hint"></span>
  </div>

  <div class="meta" id="meta"></div>

  <div class="tablewrap">
    <table>
      <thead>
        <tr>
          <th>ID</th><th>브랜드</th><th>소분류</th><th>모델</th><th>상품명</th>
          <th>이미지</th><th>이미지 URL</th><th>공급가</th><th>소비자가</th><th>상태</th><th></th>
        </tr>
      </thead>
      <tbody id="tbody"></tbody>
    </table>
  </div>

  <div class="pager" id="pager"></div>
</div>

<div id="toast"></div>

<script>
const AUTH = "Basic ${token}";
const SIZE = 50;
const state = { page:1, total:0 };

const el = (id)=>document.getElementById(id);
function esc(s){ return (s==null?'':String(s)).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }
function toast(msg, err){ const t=el('toast'); t.textContent=msg; t.className='on'+(err?' err':''); setTimeout(()=>t.className='',2200); }

async function api(path, opts){
  const o = Object.assign({ headers:{} }, opts||{});
  o.headers['Authorization'] = AUTH;
  if (o.body) o.headers['content-type'] = 'application/json';
  const r = await fetch(path, o);
  if (!r.ok){ let m=''; try{ m=(await r.json()).error||''; }catch{} throw new Error(m||('HTTP '+r.status)); }
  return r.json();
}

async function loadStats(){
  try{
    const s = await api('/api/admin/products?stats=1');
    const by = s.byStatus||{};
    const defs = [
      { k:'', l:'전체', n:s.total||0, cls:'total' },
      { k:'등록가능', l:'등록가능', n:by['등록가능']||0, cls:'ok' },
      { k:'가격대기', l:'가격대기', n:by['가격대기']||0, cls:'price' },
      { k:'이미지대기', l:'이미지대기', n:by['이미지대기']||0, cls:'img' },
    ];
    el('cards').innerHTML = defs.map(d=>
      '<div class="card '+d.cls+'" data-status="'+d.k+'"><div class="n">'+d.n.toLocaleString()+'</div><div class="l">'+d.l+'</div></div>'
    ).join('');
    document.querySelectorAll('.card').forEach(c=>c.addEventListener('click',()=>{
      el('f-status').value = c.dataset.status; state.page=1; load();
    }));
  }catch(e){ toast('통계 로드 실패: '+e.message, true); }
}

function markStatusCard(){
  const cur = el('f-status').value;
  document.querySelectorAll('.card').forEach(c=>c.classList.toggle('on', c.dataset.status===cur));
}

async function load(){
  markStatusCard();
  const p = new URLSearchParams();
  if (el('f-brand').value)  p.set('brand', el('f-brand').value);
  if (el('f-status').value) p.set('status', el('f-status').value);
  if (el('f-sobun').value.trim()) p.set('sobun', el('f-sobun').value.trim());
  if (el('f-q').value.trim())     p.set('q', el('f-q').value.trim());
  p.set('page', state.page); p.set('size', SIZE);

  el('tbody').innerHTML = '<tr><td colspan="11" style="padding:24px;text-align:center;color:#5a6470">불러오는 중…</td></tr>';
  try{
    const d = await api('/api/admin/products?'+p.toString());
    state.total = d.total;
    el('count-hint').textContent = '총 '+d.total.toLocaleString()+'건';
    el('meta').textContent = '페이지 '+d.page+' · '+d.count+'건 표시';
    renderRows(d.items);
    renderPager();
  }catch(e){
    el('tbody').innerHTML = '<tr><td colspan="11" style="padding:24px;text-align:center;color:#b4453a">로드 실패: '+esc(e.message)+'</td></tr>';
  }
}

function renderRows(items){
  if (!items.length){ el('tbody').innerHTML='<tr><td colspan="11" style="padding:24px;text-align:center;color:#5a6470">결과 없음</td></tr>'; return; }
  el('tbody').innerHTML = items.map(it=>{
    const img = it.image_url
      ? '<img class="thumb" src="'+esc(it.image_url)+'" onerror="this.style.display=\\'none\\'">'
      : '<div class="thumb none">없음</div>';
    const opt = ['등록가능','가격대기','이미지대기'].map(s=>'<option'+(it.status===s?' selected':'')+'>'+s+'</option>').join('');
    return '<tr data-id="'+esc(it.id)+'">'
      + '<td class="sku">'+esc(it.id)+'</td>'
      + '<td>'+esc(it.brand)+'</td>'
      + '<td>'+esc(it.sobun)+'</td>'
      + '<td>'+esc(it.model)+'</td>'
      + '<td><span class="name">'+esc(it.name)+'</span></td>'
      + '<td>'+img+'</td>'
      + '<td><input class="url" data-f="image_url" value="'+esc(it.image_url)+'" placeholder="https://…"></td>'
      + '<td><input class="p" data-f="supply_price" value="'+esc(it.supply_price)+'"></td>'
      + '<td><input class="p" data-f="retail_price" value="'+esc(it.retail_price)+'"></td>'
      + '<td><select class="st" data-f="status">'+opt+'</select></td>'
      + '<td><button class="save" disabled>저장</button></td>'
      + '</tr>';
  }).join('');

  el('tbody').querySelectorAll('tr[data-id]').forEach(tr=>{
    const btn = tr.querySelector('.save');
    tr.querySelectorAll('[data-f]').forEach(inp=>{
      inp.addEventListener('input', ()=>{ tr.classList.add('dirty'); btn.disabled=false; });
      inp.addEventListener('change', ()=>{ tr.classList.add('dirty'); btn.disabled=false; });
    });
    btn.addEventListener('click', ()=>saveRow(tr, btn));
  });
}

async function saveRow(tr, btn){
  const payload = { id: tr.dataset.id };
  tr.querySelectorAll('[data-f]').forEach(inp=>{ payload[inp.dataset.f] = inp.value; });
  btn.disabled = true; btn.textContent='저장중…';
  try{
    const r = await api('/api/admin/products', { method:'PUT', body: JSON.stringify(payload) });
    tr.classList.remove('dirty');
    btn.textContent='저장';
    // 썸네일 갱신
    const cell = tr.children[5];
    const url = payload.image_url;
    cell.innerHTML = url ? '<img class="thumb" src="'+esc(url)+'" onerror="this.style.display=\\'none\\'">' : '<div class="thumb none">없음</div>';
    toast('저장됨 · '+(r.item? r.item.model : tr.dataset.id));
    loadStats();
  }catch(e){
    btn.disabled=false; btn.textContent='저장';
    toast('저장 실패: '+e.message, true);
  }
}

function renderPager(){
  const pages = Math.max(1, Math.ceil(state.total/SIZE));
  const cur = state.page;
  if (pages<=1){ el('pager').innerHTML=''; return; }
  let start = Math.max(1, cur-4), end = Math.min(pages, start+9); start = Math.max(1, end-9);
  let h = '<button '+(cur<=1?'disabled':'')+' data-p="'+(cur-1)+'">‹</button>';
  if (start>1) h += '<button data-p="1">1</button><span style="align-self:center">…</span>';
  for (let i=start;i<=end;i++) h += '<button class="'+(i===cur?'on':'')+'" data-p="'+i+'">'+i+'</button>';
  if (end<pages) h += '<span style="align-self:center">…</span><button data-p="'+pages+'">'+pages+'</button>';
  h += '<button '+(cur>=pages?'disabled':'')+' data-p="'+(cur+1)+'">›</button>';
  el('pager').innerHTML = h;
  el('pager').querySelectorAll('button[data-p]').forEach(b=>b.addEventListener('click',()=>{
    state.page = parseInt(b.dataset.p,10); load(); window.scrollTo(0,0);
  }));
}

el('btn-go').addEventListener('click', ()=>{ state.page=1; load(); });
el('btn-reset').addEventListener('click', ()=>{
  el('f-brand').value=''; el('f-status').value=''; el('f-sobun').value=''; el('f-q').value='';
  state.page=1; load();
});
el('f-q').addEventListener('keydown', e=>{ if(e.key==='Enter'){ state.page=1; load(); } });
el('f-sobun').addEventListener('keydown', e=>{ if(e.key==='Enter'){ state.page=1; load(); } });

loadStats();
load();
</script>
</body>
</html>`;
}
