from pathlib import Path
import hashlib,json,sys
P=Path(__file__).resolve().parents[1]
path=P/'records/MATH_PROSE_PROOF_VISUAL_OBSERVATIONS.json'
identity=lambda r:(r['key'],r['mode'],r['page'])
manifest={identity(r):r for r in json.loads((P/'records/MATH_PROSE_PROOF_RENDER_MANIFEST.json').read_text())}
old={identity(r):r for r in json.loads(path.read_text())} if path.exists() else {}
for row in json.load(sys.stdin):
    m=dict(manifest[identity(row)])
    for kind in ['pdf','image']:
        assert hashlib.sha256((P/m[kind]).read_bytes()).hexdigest()==m[kind+'_sha256']
    m.update(row)
    m['viewed']=True
    old[identity(m)]=m
path.write_text(json.dumps(list(old.values()),indent=2)+'\n')
print(json.dumps({'actual_proof_views':len(old),'rendered_pages':len(manifest)}))
