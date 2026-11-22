"""Authorized four-label promotion, preserving exact audited source and shared priors."""
from pathlib import Path
from datetime import datetime, timezone
import ast, difflib, hashlib, json, re

root = Path(__file__).resolve().parents[3]
own = root/'agents/obstructions_crystals'
src = own/'post_CP33_general_odd_source_Cartier_candidate.tex'
dst = own/'A4_general_odd_source_Cartier.tex'
expected = 'dac82081dc46a2c1e80254831e301a0e52e64c9604af420289bae95dd3e21b83'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
audits = ['outputs/root_general_odd_source_Cartier_audit.json',
          'agents/monodromy/outputs/independent_general_odd_source_Cartier_audit.json']
assert sha(src) == expected and not dst.exists()
for path in audits:
    r = json.loads((root/path).read_text())
    assert 'PASS' in r['status'] and r['candidate_sha256'] == expected
before = src.read_text()
labels = re.findall(r'\\label\{([^}]+)\}', before)
assert len(labels) == 4
after = re.sub(r'\\status\{Candidate[^}]*\}', r'\\status{Proved; full independent proof audits passed.}', before)
after = re.sub(r'\A%[^\n]*', '% Promoted after complete root and monodromy proof audits; exact candidate retained.', after)
assert after.count('\\status{Proved') == 4
con = root/'code/consolidate.py'
old = con.read_text()
anchor = "   lang_deck_slice=a/'obstructions_crystals/A4_Lang_deck_slice_bound.tex'\n   if lang_deck_slice.exists() and '\\\\status{Candidate' not in lang_deck_slice.read_text():\n    out.write('\\n'+lang_deck_slice.read_text()+'\\n')\n"
assert old.count(anchor) == 1 and dst.name not in old
addition = "   general_odd_source=a/'obstructions_crystals/A4_general_odd_source_Cartier.tex'\n   if general_odd_source.exists() and '\\\\status{Candidate' not in general_odd_source.read_text():\n    out.write('\\n'+general_odd_source.read_text()+'\\n')\n"
new = old.replace(anchor, anchor+addition)
ast.parse(new)
cfg = root/'notes/checkpoint34_promoted_inputs.json'
cfgold = cfg.read_text()
inputs = json.loads(cfgold)
path = str(dst.relative_to(root))
assert isinstance(inputs,list) and path not in inputs
inputs.append(path)
cfgnew = json.dumps(inputs,indent=2)+'\n'
history = own/'notes/CP34_general_odd_source_promotion'
history.mkdir(exist_ok=False)
(history/'candidate.tex').write_bytes(src.read_bytes())
(history/'consolidate.before.py').write_bytes(con.read_bytes())
(history/'inputs.before.json').write_bytes(cfg.read_bytes())
for name,a,b in [('promotion.diff',before,after),('consolidate.diff',old,new),('inputs.diff',cfgold,cfgnew)]:
    (history/name).write_text(''.join(difflib.unified_diff(a.splitlines(True),b.splitlines(True),fromfile='before',tofile='after')))
with dst.open('x') as f:f.write(after)
con.write_text(new)
cfg.write_text(cfgnew)
assert sha(src) == expected
now = datetime.now(timezone.utc).isoformat()
record = {
    'status':'PROMOTED AFTER TWO COMPLETE INDEPENDENT PROOF AUDITS','actual_utc':now,
    'candidate':str(src.relative_to(root)),'candidate_sha256':expected,
    'canonical':path,'canonical_sha256':sha(dst),'labels':labels,'audits':audits,
    'scope':'Twisted multiplication and cross determinants, and their simultaneous actual wall witnesses, for arbitrary positive odd cubic pullback sources of degree a. A full source image condition yields K contained in the nontrivial outer deck part and quotient dimension >=9a-1. No new source full-image theorem, prime degree or K=0 conclusion is asserted.',
    'history':str(history.relative_to(root)),
    'changes':'Only short statuses and provenance comment changed. One optional include and one CP34 required canonical path added, preserving shared prior bytes/diffs.',
    'computation':'No numerical computation needed or claimed.'
}
rp = own/'general_odd_source_Cartier_promotion.json'
with rp.open('x') as f:json.dump(record,f,indent=2);f.write('\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'promotion_after_full_independent_audits',path,
                           record['scope'],'PROVED; stated conditional scope',str(rp.relative_to(root))])+'\n')
with (own/'D_results.md').open('a') as f:
    f.write('\n\n## Arbitrary odd cubic-pullback source — '+now+'\n\n')
    f.write('`A4_general_odd_source_Cartier.tex` proves the exact relative twisted blocks and simultaneous same-Fermat wall witnesses for M=eta*3Theta with arbitrary positive odd deg(eta)=a, without assuming the source is principally polarized. If that source has full geometric image, the outer odd-cover slice forces K into its nontrivial deck part and gives quotient dimension at least9a-1. The source full-image hypothesis remains explicit. The earlier narrower candidate is retained and not separately promoted.\n')
print(json.dumps({'status':record['status'],'actual_utc':now,'canonical':path,
                  'canonical_sha256':record['canonical_sha256'],'record':str(rp.relative_to(root))}))
