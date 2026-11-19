"""Retrieve named public primary papers for local formula inspection. No source text in final ZIP."""
import urllib.request,pathlib,sys
name,url=sys.argv[1:]
dest=pathlib.Path(__file__).parents[1]/'evidence'/name
try:
    with urllib.request.urlopen(url,timeout=30) as r:
        b=r.read();ctype=r.headers.get('Content-Type');final=r.geturl()
    dest.write_bytes(b)
    print(f'{url}\nFinal URL: {final}\nContent type: {ctype}\nBytes: {len(b)}\nSaved: {dest}')
except Exception as e:
    print(type(e).__name__+': '+str(e));sys.exit(1)
