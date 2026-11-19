"""Serialize explicitly scoped checks, separate from reading a source assertion."""
from pathlib import Path
import csv,json,re
R=Path(__file__).resolve().parents[1]
rows=[]
def E(id,typ,outcome):rows.append({'statement_id':id,'date':'2026-11-19','who':'GPT-6 Astra Pro; effort not exposed; /root SA21','type':typ,'outcome':outcome})
checks={
 'Hua2026':'Opened versionv2 §§76–79; inspected exact manuscript/theorem hypotheses and restricted scope. Public I/II Lean definitions and named theorem statements inspected; no compiler run. See root_primary_checks.md and independent III/IV source checks.',
 'Schapira2023':'Definition10.1.1 and Proposition10.1.2, printedp176, read. The source states the theorem for k-module sheaves, sufficient here; retains closedness and Hausdorff paracompactness. The proof of case(iii) is referred to Godement, not independently reproved in this run.',
 'Gillam2011':'Read §2.1 prime systems, §2.2 set/topology of localization and §3.3 relative spectrum. Matched only the explicit relative-spectrum convention, not the full cutting topology.',
 'EGAI1960':'Original PDF successfully downloaded. Read0,2.1.1–2.1.6 pp21–22 and I,1.1.1–1.1.10 pp80–82; affine spectrum and generic-point background checked. Earlier subsidiary access failure is superseded only for these actual passages.',
 'Esquisse1984':'Primary §5 pushout and Isom discussion read; independently confirmed §5 printedpp29–30 for the Isom display, correcting old §6 reference. Proposed axioms/comparison remain programmatic.',
 'McCord1966':'Opened and compared Theorems1–3; conclusion is weak homotopy, with actual finite-space/complex data retained.',
 'BarmakMinian2008':'Opened Theorem3.10 and publication/arXiv history. Simple-homotopy comparison checked at statement/hypothesis level; no claimed complete independent proof of the paper.',
 'Clader2009':'Read Theorem1.1 and Lemma3.1 with the later erratum. Specific inverse system and quotient distinguished from arbitrary finite pro-spaces.',
 'Clader2016':'Successfully downloaded and read both pages after browser403 errors. The finite-coordinate open-star argument repairs continuity without changing the main conclusions. Exact fetch receipt retained.',
 'AFR2019':'Opened Theorem4.2.5 in author PDF, publisher dates and arXiv history. Retains conically smooth stratified-homotopy conventions; no homeomorphism theorem for a bare incidence poset inferred.',
 'Stacks09XV':'Opened Lemma5.23.12; used directed finite-sober inverse limits and spectrality with its precise hypotheses.',
 'Stacks08ZY':'Opened Lemma5.22.2 profinite equivalences; used compact Hausdorff zero-dimensional conclusion in conjunction with the separate spectral-limit argument.',
 'Stacks00ER':'Opened Lemma10.26.5 ring-spectrum criteria; Boolean ring application checked algebraically.',
 'Stacks04PN':'Opened idempotent/clopen correspondence in §10.21; kept ordinary global Spec distinct from relative sheaf Spec.',
 'Stone1934':'Primary article metadata successfully opened; PDF response was HTML protection, so full theorem text was not inspected. Used for historical bibliography only; exact Boolean calculations independently proved.',
 'Crainic2024':'Author quotient sections opened; used only as modern background. The precise saturated-closed embedding lemma has its own proof here.',
 'SiebenmannGuillouHahl1973':'Opened Numdam original bibliographic page and followed references; used as a historical comparison, not an exact proof of the manuscript tame assertion.',
 'CSGPublished':'Opened and searched the published-work inventory, including EGA,SGA,Esquisse; no source-specific classA resolution inferred from a broad title.',
 'CSGUnpublished':'Opened inventory; manuscript listed as unpublished. This does not prove absence of independent later development.',
 'MontpellierArchive':'Opened official catalogue and checked cotes/counts; actual attachment marker inventory separately computed.',
 'Malgoire2002':'Opened3October2002 official seminar description. It documents exposition of the programme, not an established theorem for the custom axioms.',
 'CruzMorales2021':'Opened arXiv metadata and paper; used for conceptual history, not a substitute mathematical settlement.'}
for k,v in checks.items():E(k,'used and rechecked in this run',v)
for k,v in {'Godement1958':'Exact historical attribution read in Schapira; original book not opened. Marked unverified and no unread theorem proof relied on.','Cohen1969':'Bibliographic lead confirmed by backward references; AMS access403. Marked unverified, exact theorem not used.'}.items():E(k,'carried as background without fault found',v)
proofs={
 'support':('independent re-proof','F1/F2 side containment proves support injectivity and local endpoint uniqueness; no divisibility premise.'),
 'infinite':('independent re-proof','Nested proper subsegments prove infinitude under divisibility; the nondivisible reduced-graph case is kept separate.'),
 'branches':('targeted proof check','The explicit common-initial-subsegment filtering condition supplies transitivity. No independent proof of the separate F5 equivalence is claimed.'),
 'orders':('independent re-proof','All interval-model F1–F5 and F3′ clauses verified analytically for a dense locally filtered poset. Converse is separately compared with Hua.'),
 'restriction':('independent re-proof','Dense diamond counterexample: every ambient axiom checked analytically; restricted F4 fails. Finite sample is only a support-obstruction check.'),
 'fork':('independent re-proof','Rational ordinal-sum fork verifies density, local filtering and connected incidence while failing a global upper bound and F6.'),
 'weakF6':('independent re-proof','Two-maxima dense order separates weak interior extension from strong support extension; does not refute the special equal-endpoint conclusion.'),
 'orientation':('targeted proof check','Proved the elementary transport-graph holonomy criterion; did not prove manuscript axioms imply trivial holonomy.'),
 'quotient-embedding':('independent re-proof','Closed saturated traces extend to closed saturated ambient sets; exact quotient-subspace embedding follows.'),
 'cones':('independent re-proof','Compact radial cofinality and finite simplicial-pair height-function cone proof checked. No arbitrary tame-space theorem asserted.'),
 'ficelle-connectivity':('independent re-proof','Both component implications with finite-component qualification, interior contraction and reduction checked.'),
 'disconnected':('computation or formal certificate','Exact two-interval cell-incidence quotient certificate plus analytical conic-neighborhood verification in root_proofs.md.'),
 'interval':('independent re-proof','Disconnected-end interval example checked and connected-end classification proved at its precise scope.'),
 'tripod':('computation or formal certificate','Tripod enlargement quotient components enumerated; conic regularity checked analytically.'),
 'polyhedra':('independent re-proof','Finite-polyhedron reduced existence and unordered-pair uniqueness iff arc proved; graph enumeration only corroborates the elementary finite subcase.'),
 'cone-cover':('independent re-proof','Literal omitted-cover counterexamples and neighborhood-cover repair checked, respecting empty-link convention.'),
 'cutting':('targeted proof check','Closed-piece reassociation and piece counts checked; arbitrary category/morphism and general interpolation obligations are explicitly not fully proved.'),
 'side-contraction':('computation or formal certificate','Connected finite tripod contraction refutes literal side-contained preservation, including all end/regularity hypotheses; independently reviewed by VIII–IX reader.'),
 'incompatible':('computation or formal certificate','Alternating rational two-point cuts of a circle checked; ordinary set disjointness does not imply geometric compatibility.'),
 'rives':('independent re-proof','Conic clopen algebra, zero iff open, disconnected-node and connected-link information-loss examples checked.'),
 'sheaves':('targeted proof check','Independent injection and explicit relative-Stone clopen reconstruction; paracompact surjectivity only compared with opened Schapira theorem.'),
 'Stone':('independent re-proof','Finite Boolean subalgebra bound and global inverse-limit spectrum proved; small free-algebra cases enumerated.'),
 'finite-topology':('independent re-proof','Deduction from opened finite-sober-limit spectrality: a Hausdorff limit has clopen compact basis and cannot be a connected nontrivial compact space.')}
for suffix,(t,o) in proofs.items():E('R-SA21-'+suffix,t,o+' See audit/root_proofs.md; code/root_checks.py identifies executed finite checks.')
for item,suffix in [(18,'support'),(22,'support'),(34,'fork'),(8,'weakF6'),(38,'quotient-embedding'),(48,'cone-cover'),(49,'side-contraction'),(56,'disconnected'),(57,'interval'),(58,'tripod'),(77,'polyhedra'),(78,'polyhedra'),(66,'sheaves'),(68,'rives'),(69,'rives'),(70,'rives'),(76,'Stone'),(82,'finite-topology'),(80,'incompatible')]:
 E('SA21-'+str(item),'targeted proof check','Mathematical content compared with the explicitly scoped argument R-SA21-'+suffix+'; source attribution remains the earlier run where stated. This event does not confer proof on other claims grouped in the same item.')
for claim,outcome in {
 'C-SA21-9-054':'Read P4 in the IX66–104 proof report. Checked both implications between full closure commutation and join preservation plus equality on singleton closures, including the empty join. This is a targeted review of the explicit proof, not a new source or formal certificate.',
 'C-SA21-9-060':'Read P9. Checked the atom/coatom classification argument and the implication that40 atoms versus16 coatoms rules out every order-reversing bijection. The234-map enumeration is the owner’s saved execution, not a rerun by root.',
 'C-SA21-9-066':'Read P10. Checked that any complement-preserving join map from the four-atom lattice into a nontrivial ortholattice reflects zero, so its transpose sends top to top; the trivial intermediate gives zero. This covers arbitrary intermediates and retains the comorphism/morphism convention.',
 'C-SA21-9-088':'Read final IX proof§3.1. Checked that complement preservation of both conjugates yields both order adjunctions and hence mutual inverses; the standing orthogonal conjugacy is essential.',
 'C-SA21-9-106':'Read final IX proof§5.1 and the seven-point support certificate explanation. Checked ordinary faithfulness, normalization and the nonBoolean virtual-support obstruction; no full-faithfulness premise is claimed.',
 'C-SA21-9-116':'Read final IX proof§5.2. Checked the three-stratum inverse-image example: top open preimage disappears while two proper faces survive. The separate partial-generator convention is not conflated with the full-figure pullback.',
 'C-SA21-9-123':'Read final IX proof§6. Checked deletion and the universal factorization in the exact pointed maquette category, including incidence across the deleted subset because zero is incident in both directions.'}.items():
 E(claim,'targeted proof check',outcome)
with (R/'parts/root/extra_check_events.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(rows)
print(json.dumps({'additional_scoped_events':len(rows)}))
