export async function onRequest(context) {
  const { request, env } = context;
  const p = new URL(request.url).searchParams;
  const brand = p.get("brand"), sobun = p.get("sobun"), status = p.get("status"), q = p.get("q");
  const page = Math.max(1, parseInt(p.get("page")||"1",10));
  const size = Math.min(100, parseInt(p.get("size")||"24",10));
  const where=[], binds=[];
  if(brand){where.push("brand = ?");binds.push(brand);}
  if(sobun){where.push("sobun = ?");binds.push(sobun);}
  if(status){where.push("status = ?");binds.push(status);}
  if(q){where.push("(name LIKE ? OR model LIKE ?)");binds.push("%"+q+"%","%"+q+"%");}
  const clause = where.length ? "WHERE "+where.join(" AND ") : "";
  const sql = `SELECT id,sku,brand,sobun,model,name,features,supply_price,retail_price,image_url,product_url,status FROM products ${clause} ORDER BY brand,sobun,model LIMIT ? OFFSET ?`;
  binds.push(size,(page-1)*size);
  const { results } = await env.DB.prepare(sql).bind(...binds).all();
  return new Response(JSON.stringify({page,size,count:results.length,items:results}), {
    headers:{"content-type":"application/json; charset=utf-8","cache-control":"public, max-age=300"}
  });
}
