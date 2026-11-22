"""Unauthenticated public IHES catalogue queries through its observed search form."""
import concurrent.futures, datetime, hashlib, html, json, re, time
import urllib.parse, urllib.request
from pathlib import Path

queries = ['affine analog', 'proper base change', 'changement de base']

def fetch(query):
    url = 'https://archives.ihes.fr/search?' + urllib.parse.urlencode({
        'query': query, 'query_type': 'exact_match'})
    start = time.perf_counter()
    out = {'query': query, 'url': url}
    try:
        with urllib.request.urlopen(url, timeout=35) as response:
            body = response.read()
            out.update(status=response.status, final_url=response.url,
                       bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
        source = body.decode('utf-8', 'replace')
        source = re.sub(r'<(?:script|style)\b[^>]*>[\s\S]*?</(?:script|style)>', '', source)
        plain = html.unescape(re.sub(r'<[^>]+>', ' ', source))
        out['text'] = re.sub(r'\s+', ' ', plain).strip()
        out['links'] = [{'href': html.unescape(u), 'label': re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', t))).strip()}
                        for u,t in re.findall(r'<a\b[^>]*href=[\"\']([^\"\']+)[\"\'][^>]*>([\s\S]*?)</a>', source)]
    except Exception as exc:
        out['error'] = f'{type(exc).__name__}: {exc}'
    out['elapsed_seconds'] = time.perf_counter() - start
    return out

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    records = list(pool.map(fetch, queries))
output = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'form_observed_on': 'https://archives.ihes.fr/items/browse?sort_field=Dublin+Core%2CCreator&tags=GABBER',
          'records': records}
path = Path(__file__).resolve().parents[1] / 'logs/B_IHES_original_title_search.json'
path.write_text(json.dumps(output, ensure_ascii=False, indent=2))
for record in records:
    print(json.dumps({key:record[key] for key in ['query','status','text','error'] if key in record}, ensure_ascii=False))
