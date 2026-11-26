"""Fetch data.pequalnp.com paths (relative, e.g. data/map/overview.x.json) into OUTDIR keeping the path; <= 2 req/s.
usage: python -I -B fetch.py OUTDIR path [path ...]   (skips files already present)"""
import sys, os, time, urllib.request
out = sys.argv[1]
for p in sys.argv[2:]:
    dst = os.path.join(out, p.replace('/', os.sep))
    if os.path.exists(dst) and os.path.getsize(dst) > 0:
        print('have', p); continue
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    req = urllib.request.Request('https://data.pequalnp.com/' + p, headers={'User-Agent': 'joint-map-reader/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        open(dst, 'wb').write(data)
        print('got', p, len(data))
    except Exception as e:
        print('ERR', p, e)
    time.sleep(0.6)
