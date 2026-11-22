"""Integrate individually audited post-checkpoint15 research; never archive."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,hashlib,re
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
paths=['parts/C/D_cover_uniform_canonical_defect.tex','parts/C/D_cover_uniform_different_refinement.tex','parts/B/post15_research/D_local_Eisenstein_atlas_B.tex','parts/C/D_RDP_full_sheaf_degree.tex','parts/B/post15_research/D_unpointed_Eisenstein_witness_B.tex','parts/B/post15_research/D_fixed_formal_curve_fibres_B.tex','parts/C/D_exceptional_canonical_energy.tex','parts/D/post15_research/D_elliptic_cone_order_obstruction.tex']
pattern=re.compile(r'\\begin\{(proposition|corollary|lemma|example)\}\[([^\]]+)\]\s*\\label\{([^}]+)\}')
rows=[]
for rel in paths:
 s=(root/rel).read_text()
 for m in pattern.finditer(s):
  assert m[2].startswith(('Proved:','Refuted:')),(rel,m[2])
  rows.append(dict(id=m[3],statement=m[2].split(':',1)[1].strip(),status=m[2].split(':',1)[0],where_proved=rel+': label '+m[3],depends_on='; '.join(sorted(set(re.findall(r'\\ref\{([^}]+)\}',s)))),manuscript_pages='29/061,066',notes='Auxiliary post-checkpoint15 result. Complete root/B/C/D actual-file audits; exact independent source scopes and finite-only computation scopes are recorded per event. No hereditary object atlas, factorial surface-cover count or general finite-generation conclusion. No movement after review09.'))
p=root/'parts/D/results_D.csv'
with p.open() as f:old=list(csv.DictReader(f))
known={r['id'] for r in old};new=[r for r in rows if r['id'] not in known]
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['id','statement','status','where_proved','depends_on','manuscript_pages','notes']);w.writeheader();w.writerows(old+new)
p=root/'parts/D/paper_D.tex';s=p.read_text()
for rel in paths:
 line='\\input{'+rel+'}'
 if line not in s:s+='\n'+line+'\n'
p.write_text(s)
p=root/'parts/D/CHECK_EVENTS_D.tsv'
with p.open() as f:events=list(csv.DictReader(f,delimiter='\t'))
with (root/'parts/C/CHECK_EVENTS_C_post15.tsv').open() as f:part_events=list(csv.DictReader(f,delimiter='\t'))
added={r['id'] for r in new}
c_labels={r['id'] for r in rows if r['where_proved'].startswith('parts/C/')}
for e in part_events:
 if e['statement_id'] not in added or e['statement_id'] not in c_labels:continue
 actor=e['auditor'].rsplit('; ',1)[1]
 events.append(dict(statement_id=e['statement_id'],date=now,who='GPT-6 Astra Pro; '+actor+'; SA12 run1; effort setting not independently exposed',type=e['check_type'],outcome=e['result']+' Actual source-read scope is retained verbatim from the C event record; event consolidation occurred after the immutable checkpoint15.'))
for label in ['D:local-Eisenstein-linear-atlas','D:local-branch-data-linear-complexity']:
 if label not in added:continue
 for actor in ['/root/part_b','/root','/root/part_c','/root/part_d']:
  scope='Section 2, equation (4.1), Proposition 4.4, Corollary 4.6 and Lemma 4.7' if actor in ['/root','/root/part_b'] else 'Section 4 definitions, Proposition 4.4, Corollary 4.6 and Lemma 4.7'
  events.append(dict(statement_id=label,date=now,who='GPT-6 Astra Pro; '+actor+'; SA12 run1; effort setting not independently exposed',type='complete actual-file proof and primary-source audit',outcome='PASS: coefficient chart, derivative weights, all-ring pointed formal-disc model, Newton correction, finite Isom witness and branch-list count fully checked. Yasuda (2025) '+scope+' used passages freshly read; root does not claim a fresh complete read of contextual Lemma 4.9--Corollary 4.12. Branch-fibre clarification applied before promotion. No global gluing bound or main-gate movement. Exact author manifest: parts/B/post15_research/integration_manifest_B_post15.json.'))
for label in ['D:unpointed-Eisenstein-witness','D:fixed-formal-curve-fibre-bound']:
 if label not in added:continue
 for actor in ['/root/part_b','/root','/root/part_c','/root/part_d']:
  if label=='D:unpointed-Eisenstein-witness':
   outcome='PASS: complete actual-file proof over arbitrary coefficient rings; nilpotent-coordinate inversion, beta-adic derivative and Newton calculation, continuity and converse chain rule verified. The already proved/source-audited pointed theorem is the only external dependency; the coordinate refinement is proved internally.'
  else:
   scope={'/root':'Fresh complete Stacks0BP2,0BNI15.92.18–19,0BQB,09ZT,0DZQ,0DZT109.15.1–2; complete SGA1 XIII2.12 pp392–394; all12 pages of de Jong–Katz including Proposition4.2 pp4–6.', '/root/part_b':'Fresh complete used Stacks0BP2,0BNI15.92.18–19,0BQB,09ZT,0DZQ,0DZT; SGA1 XIII2.12 pp392–394 characteristic-zero proof; de Jong–Katz Proposition4.2 pp4–6 complete written proof.', '/root/part_c':'Fresh complete Stacks0BP2,0BNI15.92.18–19,09ZT,0BQB; other dependencies checked within the proof, without claiming a fresh full source read.', '/root/part_d':'Fresh complete used Stacks gluing, nilpotent invariance, curve lifting and existence proofs; SGA1 exact earlier audit reused.'}[actor]
   outcome='PASS: complete corrected actual-file proof, including explicit degree n when B is empty; common local lifts, nilpotent finite-algebra patching, common global discriminant, generic normalization injectivity and permutation-defect count. '+scope+' Exact source scopes in B integration manifest. This is a fixed-formal-data fibre count only.'
  events.append(dict(statement_id=label,date=now,who='GPT-6 Astra Pro; '+actor+'; SA12 run1; effort setting not independently exposed',type='complete actual-file proof and stated source audit',outcome=outcome))
label='D:elliptic-cone-order-generators'
if label in added:
 for actor in ['/root/part_d','/root','/root/part_b','/root/part_c']:
  scope='Fresh full0EBJ,03RP,0E39 Lemma53.22.1 and0AYQ degree definition.' if actor in ['/root/part_d','/root'] else ('Fresh full0EBJ,03RP and0E39 source proofs; certificate source/output read without an independent rerun.' if actor=='/root/part_c' else 'Complete certificate source read; no independent fresh source opening or rerun claimed.')
  events.append(dict(statement_id=label,date=now,who='GPT-6 Astra Pro; '+actor+'; SA12 run1; effort setting not independently exposed',type='complete actual-file proof check and stated source audit',outcome='PASS: fixed normal elliptic cone, full graded Hom, completion, Frobenius periodicity, semisimple lower bound and refreshed sharp upper bound mu=3r. '+scope+' Refutes uniformity for arbitrary anchors, not existence of a better anchor or the quadratic projective count.'))
 for actor,seconds in [('/root/part_d',0.072169335),('/root',0.08516565100217122)]:
  events.append(dict(statement_id=label,date=now,who='GPT-6 Astra Pro; '+actor+'; SA12 run1; effort setting not independently exposed',type='computation or finite certificate',outcome='PASS:438486 exact Jacobian, index-set, semisimple dimension and Frobenius-congruence assertions for r=2,4,...,256. Calculation seconds='+str(seconds)+'. The geometry, torsion-bundle existence and sharp upper bound are proved separately, not computationally certified. Root run retained in code/output/elliptic_order_generators_root.* and parts/D/output/elliptic_order_generators_root.json.'))
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)
for source,dest in [('parts/C/references_C_post15.bib','parts/C/references_C.bib'),('parts/B/post15_research/references_Eisenstein_B.bib','parts/B/references_B.bib'),('parts/B/post15_research/references_formal_curve_B.bib','parts/B/references_B.bib'),('parts/D/post15_research/references_elliptic_order_D.bib','parts/D/references_D.bib')]:
 p=root/dest;s=p.read_text()
 for entry in re.split(r'(?m)(?=^@)',(root/source).read_text()):
  match=re.match(r'@\w+\{([^,]+),',entry)
  if match and '{'+match[1]+',' not in s:s+='\n'+entry.strip()+'\n'
 p.write_text(s)
p=root/'parts/D/unresolved_D.tex';s=p.read_text();marker='% Post-checkpoint15 canonical and weighted-genus bounds'
if marker not in s:
 s+='\n\n'+marker+r'''
\paragraph{Further auxiliary control, with the atlas still missing.}
Proposition~\ref{D:cover-uniform-canonical-defect} gives one fixed
base ideal annihilating the canonical defect and the resolution's first
cohomology for every finite punctured cover of a complete equicharacteristic
normal surface. Its geometric genus is linear in cover degree.
Corollary~\ref{D:cover-thickening-linear-cohomology} bounds the full
cohomology of each fixed pulled-back exceptional thickening linearly.
Proposition~\ref{D:cover-uniform-Noether-different} improves the
source-factorization ideal to its first power, including the stated
Artinian coefficient families. Lemma~\ref{D:exceptional-weighted-genus}
bounds the sum of squared arithmetic genera divided by negative
self-intersection. These conclusions do not control the number of global
cover objects, a hereditary atlas with the required degree bound, or the
remaining nonabelian crowns. They do not count as new formal-review movement.
'''
 p.write_text(s)
p=root/'code/assemble.py';s=p.read_text()
para='After checkpoint15, four further auxiliary units give a fixed first-power canonical-defect and source-factorization ideal on all finite punctured surface covers, a geometric-genus bound linear in cover degree, linear cohomology for fixed pulled-back exceptional thickenings, and a linear weighted-genus budget. The complete-local and relative Artinian scopes are explicit and independently checked. These results do not supply a hereditary object atlas, the needed factorial cover count or general finite generation; they are not movement after formal review09.'
if para not in s:s=s.replace("'','## Files and continuation','',",repr(para)+",\n'','## Files and continuation','',")
p.write_text(s)
marker='% Post-checkpoint15 local Eisenstein and RDP degree bounds'
p=root/'parts/D/unresolved_D.tex';s=p.read_text()
if marker not in s:
 s+='\n\n'+marker+r'''
\paragraph{Local object data and the remaining global comparison.}
Proposition~\ref{D:local-Eisenstein-linear-atlas} presents all separable
extensions of a Laurent series field with fixed degree and different
exponent using a linear number of coefficients. It includes an explicit
finite witness for pointed isomorphisms over arbitrary coefficient rings.
Corollary~\ref{D:local-branch-data-linear-complexity} controls the number
and degree of charts when total different is linear in cover degree.
Proposition~\ref{D:RDP-full-sheaf-degree} bounds the total degree of a
reflexive module's full pullback on an entire rational-double-point
block by its rank. Neither theorem bounds global cover objects or supplies
the compatibility with adjacent exceptional curves needed for a uniform
hereditary atlas. These are auxiliary results, not new formal-review movement.
'''
 p.write_text(s)
p=root/'code/assemble.py';s=p.read_text()
para='Three additional post-checkpoint15 auxiliary units give a linear-dimensional local Eisenstein chart with explicit pointed Isom witnesses over arbitrary coefficient rings, a controlled collection of local branch-data charts, and a rank-linear total full-sheaf degree bound on each entire rational-double-point block. Full root/B/C/D proof and primary-source audits passed. Global gluing degree and adjacent-core compatibility remain open; this work does not change a requested row or the strongest main gate.'
if para not in s:s=s.replace("'','## Files and continuation','',",repr(para)+",\n'','## Files and continuation','',")
p.write_text(s)
marker='% Post-checkpoint15 fixed-fibre, energy and anchored-order results'
p=root/'parts/D/unresolved_D.tex';s=p.read_text()
if marker not in s:
 s+='\n\n'+marker+r'''
\paragraph{The sharpened local and gluing statements.}
Corollary~\ref{D:unpointed-Eisenstein-witness} supplies the same finite
isomorphism witness for continuous unpointed formal-disc maps, including
nilpotent translations. Proposition~\ref{D:fixed-formal-curve-fibre-bound}
bounds each fixed-full-formal-data fibre on a genus-$h$ curve by
$(n!)^{2h}n^{2D}$. Its common-lift argument does not impose a high-degree
or Galois hypothesis. The missing step is an effective bound on the
additional locus of local data arising from the fixed surface problem;
fibre cardinality does not bound that locus.
Proposition~\ref{D:exceptional-canonical-energy} and
Corollary~\ref{D:punctured-cover-linear-energy} give a degree-linear
canonical-energy budget and control genus against effective intersection
numbers after elimination of rational blocks. They do not present the
cover objects. Example~\ref{D:elliptic-cone-order-generators} refutes
constant module-generator bounds for arbitrary Azumaya anchors on one
fixed punctured elliptic cone: the exact number is $3r$. A better anchor
is not excluded. None of these auxiliary conclusions closes a requested
row or proves the remaining nonabelian-crown bound.
'''
 p.write_text(s)
p=root/'code/assemble.py';s=p.read_text()
para='Five further audited auxiliary units complete unpointed formal-disc Isom witnesses, a fixed-formal-data curve fibre bound (n!)^(2h)n^(2D), and degree-linear canonical energy including effective genus costs after rational-block elimination. A fixed elliptic-cone example refutes constant generator bounds for arbitrary Azumaya anchors, with exact number3r; choosing a better anchor remains possible. Root actually ran its438486-assertion finite arithmetic certificate. Effective surface-extension loci, global factorial surface-cover counts and general nonabelian crowns remain open. These results are not movement after review09.'
if para not in s:s=s.replace("'','## Files and continuation','',",repr(para)+",\n'','## Files and continuation','',")
p.write_text(s)
r={'utc':now,'labels':[r['id'] for r in rows],'added_rows':len(new),'files':[{'path':p,'sha256':hashlib.sha256((root/p).read_bytes()).hexdigest()} for p in paths],'main_movement':False,'archive_created':False,'requested_open':['D.1','D.2(ii)','residual L8']}
(root/'code/output/integrate_post15.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
