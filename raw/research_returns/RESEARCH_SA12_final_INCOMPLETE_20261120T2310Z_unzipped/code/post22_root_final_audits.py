"""Record actual exceptional-recognition and exact wild-image checks."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
root=Path(__file__).resolve().parents[1];now=datetime.now(timezone.utc).isoformat()
actor='GPT-6 Astra Pro; /root; SA12 run1; effort setting not independently exposed'
def save(name,path,sha,scope,checks,sources):
 assert hashlib.sha256((root/path).read_bytes()).hexdigest()==sha
 r={'utc':now,'actor':actor,'type':'targeted proof check','verdict':'PASS','path':path,'sha256':sha,
    'actual_read_scope':scope,'checks':checks,'source_scope':sources,
    'movement':'Recognition or auxiliary within the already tracked gates; no separate requested-status/main-gate movement.'}
 out=root/name;assert not out.exists();out.write_text(json.dumps(r,indent=2)+'\n');return name
out=[]
out.append(save('parts/B/post22_research/audit_exceptional_automorphism_crowns_root.json',
 'parts/B/post22_research/D_exceptional_automorphism_crowns_B.tex',
 '55325738912f6a9fe74ee3c047ed61ba2fe14424f9baa8fc944c329971058872',
 'Complete actual candidate; Steinberg1960§§2–7 retained full written proof audit with fresh§§2–4 reread. Original Yale notes: Section11 definitions, Theorem33 and Lemmas60–64, Theorem34 and entire written sketch/remark, Theorem36 and entire written sketch; missing OCR torus formula read on actual printed196 image. Theorem5 statement and written text proof read; no independent reproving of omitted Chevalley calculations.',
 ['Faithful inner-diagonal action follows from the two Bruhat normalizers and injective root parameters, without adjoint irreducibility.',
  'Every displayed Lie bracket has a surviving off-diagonal minus-one Cartan entry; a scalar Lie automorphism is therefore the identity.',
  'First seven coefficient fields and bounded graph indices match1960§3.2–3.6, including graph automorphisms whose square is a field operation.',
  'For Suzuki/Ree, finite-field root/weight-character extension and Lemma64 put the diagonal part inside the simple group. The first root coordinate excludes a nonidentity field operation from the inner subgroup.',
  'Dimensions≤248, coefficient fields≤q³ and an injective root coordinate of sizeq prove kappa184512 without an unstated order formula.',
  'Simplicity exclusions and ambient-field notation are separated; the three fixed derived exceptions use a faithful permutation action of Aut(S), with a permitted fixed constant enlargement.',
  'The normal-subgroup crown theorem is applied with b0=6; outer radial tameness remains essential.'],
 {'Yale_file':'parts/B/sources/SteinbergYale1968/YaleNotes.pdf',
  'actual_images':['qa/post22_Steinberg_root/physical_202.png','qa/post22_Steinberg_root/physical_203.png','qa/post22_Steinberg_root/physical_204.png'],
  'image_printed_pages':[195,196,197],
  'qualification':'Theorem34/36 are source proof sketches with expressly omitted calculations. They are used as known literature theorems with their exact locators, not claimed as new full derivations of all their dependencies.'}))
out.append(save('parts/C/post22_research/audit_wild_swap_exact_image_root.json',
 'parts/C/post22_research/D_wild_swap_exact_image.tex',
 '1d57d8d93dc20f567e90039445a0aba28aa04eaadd3317a62a0e160c96f4c085',
 'Complete actual candidate, complete existing formal-retraction proof, exact finite-cone (WI) proof passage, and the full tame-generator proof through its finite-quotient argument.',
 ['The upstairs regular resolution has one diagonal exceptional curve, negative normal degree and the actual first-projection retraction.',
  'Every punctured upstairs cover kills the fixed intersection P_K∩G_L; the bound2 concerns the full profinite image, not just separate finite quotient bounds.',
  'The fierce degree-two quotient is entirely wild inertia, proving the upper bound is attained.',
  'The upstairs full group equals its radial tame quotient;2g+1 generators upstairs plus one quotient lift give2g+2 downstairs.',
  'The normal closure of the wild image is not identified.'],
 {'fresh_existing_proofs':['parts/D/D_formal_retraction_root.tex','parts/D/D_finite_formal_cone_cover.tex: proposition D:finite-cone-wild-bound','parts/B/post20_research/D_radial_tame_cover_geometry_B.tex: proposition D:one-curve-radial-tame-generators'],
  'new_external_sources':False,'prior_primary_checks_reused':'Precise prior source audits of those proved inputs; fresh Keel/Stacks reads for the swap example recorded separately.'}))
# Check the typography-only final swap candidate by exact reversal.
p=root/'parts/C/post22_research/D_wild_one_curve_swap_obstruction.tex'
s=p.read_text();old=(root/'parts/C/post22_research/wild_swap_pre_alignment_audited.source.txt').read_text()
assert hashlib.sha256(p.read_bytes()).hexdigest()=='fa76dba77a27378c6acff80d808060285774605342d25bd8860a5f82d2378a18'
assert s.replace('\\begin{aligned}','\\begin{split}').replace('\\end{aligned}','\\end{split}')==old
r={'utc':now,'actor':actor,'type':'targeted proof check','verdict':'PASS',
 'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'scope':'Exact byte comparison to the full audited8b06b393 candidate: only the two split environments were changed to aligned, with all words and formulas unchanged.',
 'prior_full_audit':'parts/C/post22_research/audit_wild_swap_root.json'}
(root/'parts/C/post22_research/audit_wild_swap_root_final_precision.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({'utc':now,'audits':out,'swap_final_precision':'PASS'}))
