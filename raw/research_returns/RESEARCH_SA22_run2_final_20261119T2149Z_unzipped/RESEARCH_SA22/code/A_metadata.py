#!/usr/bin/env python3
"""Root-owned statement/event metadata; theorem text is read from its source."""
from pathlib import Path
import csv,re,json
root=Path(__file__).resolve().parents[1]
data={
'A:shadowdef':('67/062-064','Pointed-disc parametrizations differ by a rotation; shadow is independent of that ambiguity.'),
'A:tensor':('67/074-078','Rotation covariance checked explicitly; tensor and dual pairing conventions separated.'),
'A:koebe':('67/061-070','Opened Siu Koebe proof; normalized omitted value gives radius at most4.'),
'A:04':('67/074-082','Complete labelled stable(0,4) target with tensor17; each radius at most4, product at most16.'),
'A:alltypes':('67/074-082','Genus0 Koebe, genus1 area, genus>=2 Schwarz-Pick; finite automorphism ambiguity and (0,3),(1,1) retained.'),
'A:arbitrarycuts':('67/074-075','Explicit analytic nonisometric welding t↦−t−epsilon sin(t); geodesic cuts repair torsor compatibility.'),
'A:fullcaps':('67/074-082','Fully faithful and essentially surjective retained-cap groupoid equivalence; Fermi metric proves geodesic gluing.'),
'A:plumbing':('67/074-082','Opened Hubbard–Koch Theorems9.11/10.1; local analytic chart is not a global inverse to forgotten caps.'),
'A:graph-radius-domain':('67/074-082','SPD weighted radius Jacobian, support inequality, properness, and all normalization strata. Independent agent algebra_c audit passed.'),
'A:graph-pi-one':('67/074-082','Fixed normalization fibre Z^E; identity phase map; convex logarithmic radius deformation. Orbifold and fully marked lift conventions explicit.'),
'A:04-exact-image':('67/074-082','Full corrected fixed normalization fibre0<|q|<16; strict monotonicity and JS endpoint4.'),
'A:bordered-radius-algorithm':('67/074-082','Includes external flags, then tests equality of the actual retained external discs. Does not replace that compatibility by radius alone.'),
'A:cap-plumbing-equation':('67/074-082','Normalized cap coordinates give exact moving-coordinate equation Z+Z−=q. Algebra_c independent audit passed.'),
'A:plumbing-sources':('67/074-082','Opened Kra Thms1–3, Wolpert Expansion4.2/Example4.3, Obitsu–Wolpert Thms4/6; each comparison and limitation derived.'),
'A:EarleMarden-local':('67/074-082','Opened full Hubbard–Koch Appendix supplies the requested primary local-comparison proof; the unopened2012 chapter is a bibliographic limitation, not a missing derivation. Independent comparison audit passed.'),
'A:hinich-explicit':('67/074-082','Complete rational Hinich specialization, correct-side caps, cancelling residues and explicit cross-ratio function with simple critical point99/101. Ten original plus eleven independent exact checks; second proof audit by algebra_c.'),
'A:grafting':('67/061-070,016-021','Opened Mondello Theorem5.4; analytic fixed-positive-length stratum and continuous cusp-face extension are distinguished.'),
'A:cuspnorm':('67/061-070,016-021','Opened Wolpert cusp normalization and Penner decorations; exact h=−2pi/log rho formula; no disjointness assertion for arbitrary decorations.'),
'A:collar':('67/021','Equidistant inward collar: maximum-principle comparison with exact boundary curvature. Arbitrary collars treated by separate nonmonotonicity theorem.'),
'A:welding':('67/054-061,071-073','Opened Hamilton proof and Younsi removability discussion; QS existence and removable-seam uniqueness separately verified.'),
'A:slit':('67/071-073','Opened Lind Lemma6; whole-bank QS includes endpoint distance comparability, necessary for slit extension.'),
'A:fold':('67/071-073','Single-bank t^2 is QS but full folded map has unbounded adjacent ratio; explicit complete counterexample.'),
'A:L5':('67/073-082','From074 onward smooth seams; no appeal to arbitrary rectifiable welding existence is needed.'),
'A:orange':('67/016-021','Hua-project extremal-length method credited; explicit annulus, exact inequality and corrected implicit length/radius parametrization.'),
'A:action':('67/016-021,061-070','Length multiplication in Mondello coordinates; zero-length faces, canonical cusp norm section and intrinsic marked/unmarked action.')
}
fields=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']
events=[];rows=[]
who='GPT-6 Astra (OpenAI), inherited reasoning effort, run /root, ChatGPT Pro mode'
for name in ['part_A1234.tex','A1_radius_domain.tex','A1_plumbing_comparison.tex']:
 text=(root/'sections'/name).read_text()
 for m in re.finditer(r'\\begin\{(theorem|proposition|lemma|corollary|definition|example|remark)\}(.*?)\\end\{\1\}',text,re.S):
  body=m.group(2); label=re.search(r'\\label\{([^}]+)\}',body).group(1)
  pages,note=data[label]
  explicit=re.search(r'\\status\{([^}]+)\}',body)
  heading=re.match(r'\s*\[([^\]]*)\]',body)
  low=(explicit.group(1) if explicit else heading.group(1) if heading else '').lower()
  status='Refuted' if 'refuted' in low else 'Known' if 'known' in low else 'Proved under stated hypotheses' if 'under stated' in low else 'Proved'
  clean=re.sub(r'^\s*\[.*?\]','',body,count=1,flags=re.S)
  clean=re.sub(r'\\(?:label|status)\{[^}]+\}','',clean)
  rows.append(dict(zip(fields,[label,' '.join(clean.split()),status,'sections/'+name+', label '+label,'',pages,note])))
  events.append({'statement_id':label,'date':'2026-11-19','who':who,'type':'used and rechecked in this run' if status=='Known' else 'targeted proof check','outcome':note+' Complete statement/proof in sections/'+name+'. This is not formal verification.'})
for sid,outcome in [
 ('SA22-6 67/054-061,071-073','R1 rechecked: QS circle welding, removable-seam uniqueness, whole-bank slit compatibility. Refined statements A:welding,A:slit,A:fold.'),
 ('SA22-7 67/074-082','R3 and L2 rechecked on original scans; unrestricted nonzero tensor target confirmed. Global surjectivity false, A:04; corrected graph-radius image and tangent/fundamental-group maps proved.'),
 ('R2 67/061-070','Bounded shadow obstruction rederived with exact norm conventions; later image and JS limit supply full corrected answer.'),
 ('R6 67/016-021','Orange-slice counterargument independently calculated, credited to Michel Hua\'s project; A:orange.'),
 ('L3 67/061-070','Cusp norm and decoration identification verified in Wolpert/Penner, with canonical section via normalized length1; A:cuspnorm.'),
 ('L4 67/061-070','Single-dominant-length limit is its one-pole JS disc; general relative growth gives multi-pole JS cells. Universal physical Koebe-slit wording is overbroad; pants explicit case proved.'),
 ('L5 67/073-082','Smooth seams suffice after073; A:L5.')
]:events.append({'statement_id':sid,'date':'2026-11-19','who':who,'type':'used and rechecked in this run','outcome':outcome})
events.append({'statement_id':'L2 67/074-082','date':'2026-11-19','who':who,'type':'refuted, with the refined statement\'s id','outcome':'False; corrected A:fullcaps,A:graph-radius-domain,A:graph-pi-one. Tensor17 on two labelled three-pointed spheres is outside the image.'})
for label in ['A:cap-plumbing-equation','A:hinich-explicit','A:graph-radius-domain','A:graph-pi-one']:
 events.append({'statement_id':label,'date':'2026-11-19','who':'GPT-6 Astra (OpenAI), inherited reasoning effort, run /root/algebra_c, ChatGPT Pro mode','type':'targeted proof check','outcome':'Independent second audit passed and communicated to root; no formal certification claim. The rational example also has attached exact-arithmetic checks.'})
# Preserve current unresolved-obligation metadata and all historical check events.
old_results=root/'A_results.csv'
if old_results.exists():
 active_obligations=set(re.findall(r'\\label\{(U:[^}]+)\}',(root/'sections/unresolved.tex').read_text()))
 rows.extend(r for r in csv.DictReader(old_results.open()) if r['id'] in active_obligations)
old_events=root/'A_CHECK_EVENTS.tsv'
if old_events.exists():
 previous=list(csv.DictReader(old_events.open(),delimiter='\t'))
 seen={tuple(r.items()) for r in previous}
 events=previous+[r for r in events if tuple(r.items()) not in seen]
with (root/'A_results.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
with (root/'A_CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)
print(json.dumps({'root_statements':len(rows),'root_events':len(events)}))
