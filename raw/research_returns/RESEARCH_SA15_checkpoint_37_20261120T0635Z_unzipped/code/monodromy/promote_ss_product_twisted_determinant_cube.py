"""Parent-authorized one-axis product cross-pencil promotion after full audits."""
from pathlib import Path
from datetime import datetime,timezone
import difflib,hashlib,json,re

agent=Path(__file__).resolve().parents[1]
root=agent.parents[1]
candidate=agent/'post_CP34_product_twisted_determinant_cube_candidate.tex'
canonical=agent/'ss_product_twisted_determinant_cube.tex'
expected='0f67ca3f9ff32439e04dd2dfb319bb5e85ef21cb746eaf5fc7201b31b51f76b0'
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert digest(candidate)==expected and not canonical.exists()
audits=[root/'outputs/root_product_cross_cube_audit.json',
        root/'agents/obstructions_crystals/product_determinant_cube_independent_audit.json']
for p in audits:
    r=json.loads(p.read_text())
    assert r['candidate_sha256']==expected and 'PASS' in r['status']
before=candidate.read_text()
after,count=re.subn(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; independent audits passed.}',before)
assert count==3
after=after.replace('% Isolated after CP34; no canonical or shared build input is changed.',
                    '% Promoted after complete independent root and obstruction/crystal proof/code audits.')
needle='are retained unchanged in\n'
assert after.count(needle)==1
after=after.replace(needle,
    'are retained unchanged in\n',1)
end='\\path{agents/monodromy/notes/CP35_product_determinant_gcd_failure}.\n'
assert after.count(end)==1
after=after.replace(end,end+
    'The complete proof and unchanged exact program were independently\n'
    'audited by the root and obstruction/crystal reviewers on\n'
    '20 November 2026 at 04:36:55 and 04:36:33 UTC. Their retained\n'
    'isolated runs passed all 69 checks in\n'
    '\\(0.3022066289995564\\) and \\(0.29094762601016555\\) seconds;\n'
    'the author run took \\(0.2893797970027663\\) seconds. The exact\n'
    'candidate, transpose-convention correction and all prior executed\n'
    'bytes remain retained.\n')
history=agent/'notes/CP35_product_cube_promotion'
history.mkdir(parents=True,exist_ok=False)
(history/'candidate.tex').write_text(before)
(history/'promotion.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile=candidate.name,tofile=canonical.name)))

shared=root/'code/consolidate.py'
sb=shared.read_text()
anchor="    out.write('\\n'+product_cross.read_text()+'\\n')\n"
assert sb.count(anchor)==1 and canonical.name not in sb
addition=("   product_cross_cube=a/'monodromy/ss_product_twisted_determinant_cube.tex'\n"
          "   if product_cross_cube.exists() and '\\\\status{Candidate' not in product_cross_cube.read_text():\n"
          "    out.write('\\n'+product_cross_cube.read_text()+'\\n')\n")
sa=sb.replace(anchor,anchor+addition)
cfg=root/'notes/checkpoint35_promoted_inputs.json'
cb=cfg.read_text();entries=json.loads(cb)
cp=str(canonical.relative_to(root));assert cp not in entries
index=entries.index('agents/obstructions_crystals/A4_compatible_residual_modules.tex')+1
entries.insert(index,cp)
ca=json.dumps(entries,indent=2)+'\n'
assert 'B_both_large_tracefree_rows.tex' in sa and 'B_both_large_tracefree_rows.tex' in ca
for name,old,new in [('consolidate.py',sb,sa),('checkpoint35_promoted_inputs.json',cb,ca)]:
    (history/('prior_'+name)).write_text(old)
    (history/(name+'.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='prior/'+name,tofile=name)))
canonical.write_text(after);shared.write_text(sa);cfg.write_text(ca)
now=datetime.now(timezone.utc).isoformat()
labels=re.findall(r'\\label\{([^}]+)\}',before)
scope='Actual one-axis supersingular-product dual cross determinant is det(T)^3, with rank6 at every rank2 T and no rank8 point. No cycle or full-monodromy conclusion.'
record={'status':'PROMOTED','actual_utc':now,'candidate':str(candidate.relative_to(root)),
        'candidate_sha256':expected,'canonical':cp,'canonical_sha256':digest(canonical),
        'labels':labels,'audits':[str(p.relative_to(root)) for p in audits],
        'consolidate_sha256':digest(shared),'config_sha256':digest(cfg),
        'scope':scope,'new_computation_at_promotion':False}
(agent/'outputs/ss_product_twisted_determinant_cube_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
with (agent/'CHECK_EVENTS_post_CP16.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([label,now,'/root/monodromy','PROMOTED-ROOT-OC-FULL-PROOF-CODE-PASS',scope])+'\n')
assert digest(candidate)==expected
print(json.dumps(record,indent=2))
