"""Authorized three-label promotion after complete root and monodromy audits."""
from pathlib import Path
from datetime import datetime, timezone
import ast, difflib, hashlib, json, re

root = Path(__file__).resolve().parents[3]
own = root / 'agents/obstructions_crystals'
src = own / 'post_CP33_Lang_deck_slice_bound_candidate.tex'
dst = own / 'A4_Lang_deck_slice_bound.tex'
expected = '2b0420d99c26ab0947196c600fbc466f92a3f40c05db41e3d71e48be29b54355'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
audits = ['outputs/root_Lang_deck_slice_bound_audit.json',
          'agents/monodromy/outputs/independent_Lang_deck_slice_bound_audit.json']
assert sha(src) == expected and not dst.exists()
for name in audits:
    r = json.loads((root/name).read_text())
    assert 'PASS' in r['status'] and r['candidate_sha256'] == expected
before = src.read_text()
labels = re.findall(r'\\label\{((?:lem|prop|rem):[^}]+)\}', before)
assert len(labels) == 3
after = re.sub(r'\\status\{Candidate[^}]*\}', r'\\status{Proved; full independent proof audits passed.}', before)
after = re.sub(r'\A%[^\n]*', '% Promoted after complete independent root and monodromy audits; exact candidate retained.', after)
assert after.count('\\status{Proved') == 3
con = root/'code/consolidate.py'
old = con.read_text()
anchor = "   lang_main_orbit=a/'obstructions_crystals/A4_Lang_main_orbit.tex'\n   if lang_main_orbit.exists() and '\\\\status{Candidate' not in lang_main_orbit.read_text():\n    out.write('\\n'+lang_main_orbit.read_text()+'\\n')\n"
assert old.count(anchor) == 1 and dst.name not in old
addition = "   lang_deck_slice=a/'obstructions_crystals/A4_Lang_deck_slice_bound.tex'\n   if lang_deck_slice.exists() and '\\\\status{Candidate' not in lang_deck_slice.read_text():\n    out.write('\\n'+lang_deck_slice.read_text()+'\\n')\n"
new = old.replace(anchor, anchor+addition)
ast.parse(new)
cfg = root/'notes/checkpoint34_promoted_inputs.json'
cfgold = cfg.read_text()
inputs = json.loads(cfgold)
path = str(dst.relative_to(root))
assert isinstance(inputs,list) and path not in inputs
inputs.append(path)
cfgnew = json.dumps(inputs,indent=2)+'\n'
h = own/'notes/CP34_Lang_deck_slice_promotion'
h.mkdir(exist_ok=False)
(h/'candidate.tex').write_bytes(src.read_bytes())
(h/'consolidate.before.py').write_bytes(con.read_bytes())
(h/'inputs.before.json').write_bytes(cfg.read_bytes())
for name,a,b in [('promotion.diff',before,after),('consolidate.diff',old,new),('inputs.diff',cfgold,cfgnew)]:
    (h/name).write_text(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='before',tofile='after')))
with dst.open('x') as f:f.write(after)
con.write_text(new)
cfg.write_text(cfgnew)
assert sha(src) == expected
now = datetime.now(timezone.utc).isoformat()
rp = own/'Lang_deck_slice_bound_promotion.json'
record = {'status':'PROMOTED AFTER TWO COMPLETE INDEPENDENT PROOF AUDITS','actual_utc':now,
          'candidate':str(src.relative_to(root)),'candidate_sha256':expected,
          'canonical':path,'canonical_sha256':sha(dst),'labels':labels,'audits':audits,
          'scope':'K lies in the nontrivial deck part; quotient dimension at least8. Main-component degree bound only in the fixed principal-system specialization. No K=0 or cross-slice comparison.',
          'changes':'Only short statuses and provenance comment changed in the canonical proof. One optional include and one CP34 required input added. Exact candidates and all prior bytes/diffs retained.',
          'history':str(h.relative_to(root)),'computation':'No numerical computation needed or claimed.'}
with rp.open('x') as f:json.dump(record,f,indent=2);f.write('\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'promotion_after_full_independent_audits',path,record['scope'],
                           'PROVED; stated scope',str(rp.relative_to(root))])+'\n')
with (own/'D_results.md').open('a') as f:
    f.write('\n\n## Actual deck-slice quotient bound — '+now+'\n\n')
    f.write('`A4_Lang_deck_slice_bound.tex` proves K is contained in the nontrivial deck part on the actual cubic principal slice, so the radical-generated quotient has dimension at least8. The proof uses the F2 averaging projector, full projected degree-one image after dense-open restriction, and unique henselian lifts of regular wall Lang vectors. It does not specialize the full generic fibre across a rank drop or compare different deck slices. The source-scope correction and both complete audits are retained.\n')
print(json.dumps({'status':record['status'],'actual_utc':now,'canonical':path,
                  'canonical_sha256':record['canonical_sha256'],'record':str(rp.relative_to(root))}))
