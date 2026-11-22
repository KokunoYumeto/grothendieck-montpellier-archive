from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,difflib
own=Path(__file__).resolve().parents[1];work=own.parents[1]
p=own/'B_first_wild_irreducible_image_candidate.tex';raw=p.read_bytes()
expected='89fe8a1c7e95c145738418c7f9d852a4cfb4a032506887d1a41266e72b697870'
assert hashlib.sha256(raw).hexdigest()==expected
root=json.loads((work/'outputs/root_B79_audit.json').read_text());oc=json.loads((own.parent/'obstructions_crystals/B79_independent_audit.json').read_text())
for a in (root,oc):assert a['candidate_sha256']==expected and 'PASS' in a['status']
pre=own/'notes/B_first_wild_irreducible_image.prepromotion.tex';assert not pre.exists();pre.write_bytes(raw)
s=re.sub(r'\\status\{Candidate[^}]*\}',lambda _:r'\status{Proved; complete independent root and companion proof and exact-code audits passed.}',raw.decode())
s=s.replace('% Isolated post-CP28 candidate. No exclusion of the larger wild images.','% Proved after full post-CP28 independent audits. Larger wild images remain open.')
needle='Stacks coefficient-ring proof supplies the fixed representatives.';assert s.count(needle)==1
s=s.replace(needle,needle+r'''
The full independent root and companion audits reread the actual
B55, B53 and B60 arguments, with the arbitrary-index leading
action rederived here. Their literal isolated reruns passed in
\(0.9384170099947369\) and \(1.0166636889916845\) seconds,
respectively, preserving the author output. No additional fresh
external-source read is claimed beyond the recorded Stacks
proof used for B78. Exact candidate and audit records are retained.''')
can=own/'B_first_wild_irreducible_image.tex';assert not can.exists();can.write_text(s)
labels=re.findall(r'\\label\{([^}]+)\}',s);assert len(labels)==4 and r'\status{Candidate' not in s
now=datetime.now(timezone.utc).isoformat();r={'status':'PROVED','promotion_utc':now,'canonical':str(can),'canonical_sha256':hashlib.sha256(can.read_bytes()).hexdigest(),'audited_candidate_sha256':expected,'preserved_candidate':str(pre),'labels':labels,'root_audit':'../../outputs/root_B79_audit.json','root_audit_utc':root['actual_utc'],'root_runtime_seconds':root['independent_runtime_seconds'],'companion_audit':'../obstructions_crystals/B79_independent_audit.json','companion_audit_utc':oc['actual_utc'],'companion_runtime_seconds':oc['runtime_seconds'],'author_runtime_seconds':0.9368512359942542,'scope':'At e=p(p-1), a different-character actual p^3 pair with irreducible residual inertia must have wild order p^r,4<=r<=8. No CM assumption and no larger-image/reducible-residual exclusion. First-wild full index remains2..3.','source_scope':'Full internal B55/B53/B60 dependencies and actual leading orientation rederived; no extra fresh external-source claim beyond Stacks032A already freshly read for B78.','checkpoint_scope':'Post-CP28 canonical for CP29; immutable CP28 unchanged.','executed_failures':[]}
(own/'outputs/B79_promotion.json').write_text(json.dumps(r,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in labels:f.write('\t'.join([now,label,'PROVED_FULL_AUDITS',r['scope'],'B_first_wild_irreducible_image.tex;outputs/B79_promotion.json','Full root+OC proof/code audits; exact candidate/output retained'])+'\n')
with (own/'STATUS_CURRENT.md').open('a') as f:f.write('\n## '+now+' — B79 promoted: minimal wild third-level image\n\n'+r['scope']+'\n')
hist=own/'notes/CP29_before_B79_wiring';assert not hist.exists();hist.mkdir()
p=work/'code/consolidate.py';before=p.read_bytes();t=before.decode();old="'B_wild_CM_layer.tex']:";new="'B_wild_CM_layer.tex',\n                    'B_first_wild_irreducible_image.tex']:";assert t.count(old)==1
out=t.replace(old,new);(hist/p.name).write_bytes(before);(hist/(p.name+'.diff')).write_text(''.join(difflib.unified_diff(t.splitlines(True),out.splitlines(True),fromfile='consolidate.before',tofile='consolidate.after')));p.write_text(out)
w={'status':'CONSOLIDATE_WIRED_NOT_BUILT','actual_utc':datetime.now(timezone.utc).isoformat(),'path':'code/consolidate.py','before_sha256':hashlib.sha256(before).hexdigest(),'after_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'prior_versions':str(hist),'prepare29':'Coordinate required entry with OC; not edited by this script.'}
(own/'outputs/B79_CP29_wiring.json').write_text(json.dumps(w,indent=2)+'\n')
print(json.dumps({'promotion':r,'wiring':w},indent=2))
