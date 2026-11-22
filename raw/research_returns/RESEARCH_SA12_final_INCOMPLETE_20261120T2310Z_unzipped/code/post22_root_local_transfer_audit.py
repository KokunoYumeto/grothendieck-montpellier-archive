"""Record the actual local-transfer check and the precise source-note update."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
path='parts/D/post22_research/D_local_projective_growth_all_dimensions.tex'
expected='85e25a3b11db1de40e932c0a3a0d8d520f1c676aac6a871ffa641fa79f64b2c8'
assert hashlib.sha256((root/path).read_bytes()).hexdigest()==expected
record={
 'utc':now,'actor':'GPT-6 Astra Pro; /root; SA12 run1; effort setting not independently exposed',
 'type':'targeted proof check','verdict':'PASS','path':path,'sha256':expected,
 'actual_read_scope':'Complete actual candidate file, its full earlier fixed-slice Brauer-zero transfer proof, and fresh complete written Stacks 0BGP and 0BIC statements and proofs. The established arbitrary-SNC count is a separately audited prerequisite; this record does not replace its four audits.',
 'fresh_primary_sources':[
  {'url':'https://stacks.math.columbia.edu/tag/0BGP','locator':'Theorem 54.14.5; complete written proof','web_ref':'turn577331681view0'},
  {'url':'https://stacks.math.columbia.edu/tag/0BIC','locator':'Lemma 54.15.6; complete written proof','web_ref':'turn577331681view1'}],
 'reused_previously_checked_sources':['Stacks 0ECR and 0DX9, exact fixed-slice connectedness and cohomological-dimension lemmas','SGA1 IX Theorem4.7 finite-proper descent','Lucchini--Marion--Tracey Proposition2.6(ii), equations(2.1)--(2.2), pp12--13'],
 'checks':[
  'Normal two-dimensional complete domain is regular off its closed point; finite normalization of blowups makes the resolution projective, and embedded point blowups give SNC over the same closed point.',
  'The fixed parameter slice detects all connected covers through the d-2<d-1 connectedness inequality; conjugacy restriction is therefore injective.',
  'Finite normalization gives fixed complete normal surface components and a finite double product; each equivariant descent isomorphism is determined by one fibre value per connected component, giving |PGL|^a.',
  'The nonnormal and nonreduced closure requires every irreducible component to have dimension at least two, first removes nilpotents, and then applies the same finite-proper descent to its finite normalization.',
  'A torsor on one connected component extends trivially over the others; this proves the displayed componentwise bound.',
  'Distinct simple kernels remain distinct under the chosen faithful projective embedding; the earlier generating-orbit argument applies with fixed exponent.'
 ],
 'scope_limits':'Complete equicharacteristic local rings with algebraically closed coefficient/residue field and all components of dimension at least two. No mixed characteristic, one-dimensional component, uniform hereditary constant, or full finite generation.',
 'movement':'Closure within the same arbitrary-SNC local projective reduction staged for review15; no additional independent movement.',
 'finite_certificate':'None: this is a general geometric transfer proof, not a finite example.'
}
out=root/'parts/D/post22_research/audit_local_projective_all_dimensions_root.json'
assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n')

note=json.loads((root/'parts/D/post22_research/bibliography_note_SNC_general_D.json').read_text())
bib=root/note['central_file'];old=bib.read_text()
pattern=r'(@article\{Lieblich2011ResidualD,[\s\S]*?\n  note = \{)([^\n]*)(\}\n\})'
matches=list(re.finditer(pattern,old));assert len(matches)==1
new=re.sub(pattern,lambda m:m[1]+note['note']+m[3],old,count=1)
bib.write_text(new)
change={'utc':now,'key':note['key'],'file':note['central_file'],
 'before_sha256':hashlib.sha256(old.encode()).hexdigest(),
 'after_sha256':hashlib.sha256(new.encode()).hexdigest(),
 'change':'Update the one existing Opened note to the precisely scoped collective actual source reads; do not change historical source manifests.'}
(root/'code/output/post22_Lieblich_bibliography_update.json').write_text(json.dumps(change,indent=2)+'\n')
print(json.dumps({'audit':str(out.relative_to(root)),'verdict':'PASS','bibliography_note_updated':note['key'],'utc':now}))
