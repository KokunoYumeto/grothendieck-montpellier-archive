"""Parent-authorized universal two-axis promotion after full proof/code audits."""
from pathlib import Path
from datetime import datetime,timezone
import difflib,hashlib,json,re

agent=Path(__file__).resolve().parents[1];root=agent.parents[1]
candidate=agent/'post_CP35_product_two_axis_squarefree_candidate.tex'
canonical=agent/'ss_product_two_axis_squarefree.tex'
expected='e5f2460eb4a5ed0e644963a1ebda95dc8c6eb6b02b535f68292e10bdfe479930'
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert digest(candidate)==expected and not canonical.exists()
audits=[root/'outputs/root_product_two_axis_audit.json',root/'agents/obstructions_crystals/product_two_axis_squarefree_independent_audit.json']
for p in audits:
    data=json.loads(p.read_text());assert data['candidate_sha256']==expected and 'PASS' in data['status']
before=candidate.read_text()
after,count=re.subn(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; independent audits passed.}',before)
assert count==4
after=after.replace('% Isolated CP35 candidate; no canonical or shared build input is changed.',
                    '% Promoted after full independent root and obstruction/crystal proof/code audits.')
needle='is used for the universal theorem.\n'
assert after.count(needle)==1
after=after.replace(needle,needle+
    'The complete proof, actual Cartier dependency and unchanged standalone\n'
    'checker were independently audited by the root and obstruction/crystal\n'
    'reviewers. Their full passes were recorded on 20 November 2026 at\n'
    '04:47:12 and 04:46:10 UTC; isolated runs took\n'
    '\\(0.037655560998246074\\) and \\(0.040847354001016356\\) seconds,\n'
    'respectively. The exact candidate, discovery calculations and author\n'
    'outputs are preserved.\n')
history=agent/'notes/CP35_product_two_axis_promotion';history.mkdir(parents=True,exist_ok=False)
(history/'candidate.tex').write_text(before)
(history/'promotion.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile=candidate.name,tofile=canonical.name)))
shared=root/'code/consolidate.py';sb=shared.read_text()
anchor="    out.write('\\n'+product_cross_cube.read_text()+'\\n')\n"
assert sb.count(anchor)==1 and canonical.name not in sb
addition=("   product_two_axis=a/'monodromy/ss_product_two_axis_squarefree.tex'\n"
          "   if product_two_axis.exists() and '\\\\status{Candidate' not in product_two_axis.read_text():\n"
          "    out.write('\\n'+product_two_axis.read_text()+'\\n')\n")
sa=sb.replace(anchor,anchor+addition)
cfg=root/'notes/checkpoint35_promoted_inputs.json';cb=cfg.read_text();entries=json.loads(cb)
cp=str(canonical.relative_to(root));assert cp not in entries
entries.insert(entries.index('agents/monodromy/ss_product_twisted_determinant_cube.tex')+1,cp)
ca=json.dumps(entries,indent=2)+'\n'
assert 'B_both_large_tracefree_rows.tex' in sa and 'B_both_large_tracefree_rows.tex' in ca
assert len(entries)>=6
for name,old,new in [('consolidate.py',sb,sa),('checkpoint35_promoted_inputs.json',cb,ca)]:
    (history/('prior_'+name)).write_text(old)
    (history/(name+'.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='prior/'+name,tofile=name)))
canonical.write_text(after);shared.write_text(sa);cfg.write_text(ca)
now=datetime.now(timezone.utc).isoformat();labels=re.findall(r'\\label\{([^}]+)\}',before)
scope='Every nontrivial two-axis supersingular-product dual cross determinant is geometrically squarefree with generic corank1; local deformation openness only, no cycle or global-image conclusion.'
record={'status':'PROMOTED','actual_utc':now,'candidate':str(candidate.relative_to(root)),
        'candidate_sha256':expected,'canonical':cp,'canonical_sha256':digest(canonical),
        'labels':labels,'audits':[str(p.relative_to(root)) for p in audits],
        'consolidate_sha256':digest(shared),'config_sha256':digest(cfg),'scope':scope,'new_computation_at_promotion':False}
(agent/'outputs/ss_product_two_axis_squarefree_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
with (agent/'CHECK_EVENTS_post_CP16.tsv').open('a') as f:
    for label in labels:f.write('\t'.join([label,now,'/root/monodromy','PROMOTED-ROOT-OC-FULL-PROOF-CODE-PASS',scope])+'\n')
assert digest(candidate)==expected
print(json.dumps(record,indent=2))
