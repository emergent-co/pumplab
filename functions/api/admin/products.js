// functions/api/admin/products.js
// 관리자 전용 제품 API — Basic Auth 필요
//   GET  /api/admin/products?stats=1                     → 상태별 개수 대시보드
//   GET  /api/admin/products?brand=&sobun=&status=&q=&page=&size=  → 전체 컬럼 목록(모든 상태)
//   PUT  /api/admin/products   { id, supply_price?, retail_price?, image_url?, status? } → 수정

const REALM = 'rndsetup-admin';
const ALLOWED_STATUS = ['등록가능', '가격대기', '이미지대기'];

export async function onRequest(context) {
  const { request, env } = context;

  if (!checkAuth(request, env)) {
    return json({ error: 'unauthorized' }, 401, {
      'WWW-Authenticate': `Basic realm="${REALM}", charset="UTF-8"`,
    });
  }

  try {
    if (request.method === 'GET') return await handleGet(request, env);
    if (request.method === 'PUT') return await handlePut(request, env);
    return json({ error: 'method_not_allowed' }, 405);
  } catch (e) {
    return json({ error: 'server_error', message: String(e && e.message || e) }, 500);
  }
}

// ---- 인증 ----
function checkAuth(request, env) {
  const pw = env.ADMIN_PASSWORD || '';
  if (!pw) return false; // 환경변수 미설정 시 무조건 차단
  const auth = request.headers.get('Authorization') || '';
  if (!auth.startsWith('Basic ')) return false;
  let decoded = '';
  try { decoded = atob(auth.slice(6)); } catch { return false; }
  const i = decoded.indexOf(':');
  const pass = i >= 0 ? decoded.slice(i + 1) : decoded;
  return pass === pw;
}

// ---- GET ----
async function handleGet(request, env) {
  const p = new URL(request.url).searchParams;

  // 대시보드: 상태별 개수
  if (p.get('stats')) {
    const { results } = await env.DB
      .prepare('SELECT status, COUNT(*) AS c FROM products GROUP BY status')
      .all();
    const byStatus = {};
    let total = 0;
    for (const r of results) {
      byStatus[r.status || '(없음)'] = r.c;
      total += r.c;
    }
    return json({ total, byStatus });
  }

  // 목록 (모든 상태 포함, 관리자용 전체 컬럼)
  const brand = p.get('brand'), sobun = p.get('sobun'), status = p.get('status'), q = p.get('q');
  const page = Math.max(1, parseInt(p.get('page') || '1', 10));
  const size = Math.min(200, Math.max(1, parseInt(p.get('size') || '50', 10)));

  const where = [], binds = [];
  if (brand)  { where.push('brand = ?');  binds.push(brand); }
  if (sobun)  { where.push('sobun = ?');  binds.push(sobun); }
  if (status) { where.push('status = ?'); binds.push(status); }
  if (q)      { where.push('(name LIKE ? OR model LIKE ? OR sku LIKE ?)'); binds.push('%'+q+'%', '%'+q+'%', '%'+q+'%'); }
  const clause = where.length ? 'WHERE ' + where.join(' AND ') : '';

  // 총 개수
  const countRow = await env.DB
    .prepare(`SELECT COUNT(*) AS n FROM products ${clause}`)
    .bind(...binds).first();
  const total = countRow ? countRow.n : 0;

  const sql = `SELECT id, sku, brand, maker, origin, daebun, sobun, model,
                      opt_name, opt_value, name, features, unit,
                      supply_price, retail_price, image_url, product_url,
                      lead_time, cert, stock, status
               FROM products ${clause}
               ORDER BY brand, sobun, model
               LIMIT ? OFFSET ?`;
  const listBinds = binds.concat([size, (page - 1) * size]);
  const { results } = await env.DB.prepare(sql).bind(...listBinds).all();

  return json({ page, size, total, count: results.length, items: results });
}

// ---- PUT (수정) ----
async function handlePut(request, env) {
  let body;
  try { body = await request.json(); } catch { return json({ error: 'bad_json' }, 400); }
  if (!body || body.id == null || body.id === '') return json({ error: 'id_required' }, 400);

  const sets = [], binds = [];

  if ('supply_price' in body)  { sets.push('supply_price = ?');  binds.push(toPriceOrNull(body.supply_price)); }
  if ('retail_price' in body)  { sets.push('retail_price = ?');  binds.push(toPriceOrNull(body.retail_price)); }
  if ('image_url' in body)     { sets.push('image_url = ?');     binds.push(emptyToNull(body.image_url)); }
  if ('status' in body) {
    const s = String(body.status || '').trim();
    if (s && !ALLOWED_STATUS.includes(s)) {
      return json({ error: 'bad_status', allowed: ALLOWED_STATUS }, 400);
    }
    sets.push('status = ?'); binds.push(s || null);
  }

  if (!sets.length) return json({ error: 'no_fields' }, 400);

  binds.push(body.id);
  const info = await env.DB
    .prepare(`UPDATE products SET ${sets.join(', ')} WHERE id = ?`)
    .bind(...binds).run();

  const changes = info && info.meta ? info.meta.changes : undefined;
  if (changes === 0) return json({ error: 'not_found', id: body.id }, 404);

  // 갱신된 행 반환
  const row = await env.DB
    .prepare('SELECT id, sku, brand, sobun, model, name, supply_price, retail_price, image_url, status FROM products WHERE id = ?')
    .bind(body.id).first();

  return json({ ok: true, id: body.id, item: row });
}

// ---- helpers ----
function toPriceOrNull(v) {
  if (v === null || v === undefined || v === '') return null;
  const n = Number(String(v).replace(/[, ]/g, ''));
  return Number.isFinite(n) ? n : null;
}
function emptyToNull(v) {
  const s = (v == null) ? '' : String(v).trim();
  return s === '' ? null : s;
}
function json(obj, status = 200, extraHeaders = {}) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: {
      'content-type': 'application/json; charset=utf-8',
      'cache-control': 'no-store',
      ...extraHeaders,
    },
  });
}
