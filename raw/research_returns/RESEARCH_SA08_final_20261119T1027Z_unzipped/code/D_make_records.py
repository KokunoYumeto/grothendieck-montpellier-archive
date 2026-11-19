"""Rebuild mergeable records for the D-agent proofs. Does not assert new checks."""
from pathlib import Path
import csv
root=Path('SA08_work')
rows=[
('D001','Exact coefficient extraction L left adjoint F left adjoint weight-zero evaluation over every k','Proved','notes/D_shadows_proof.md D.1','','23;27;265','Already present in supplied Pro notes N32; independently proved using p-local cofinal weights p^r-1.'),
('D002','General finite-tail graded Hom and all positive Ext vanish for every k,M,N and nonnegative shift i','Proved','notes/D_shadows_proof.md D.2','D001','27;265','Corrects prompt R4 status; nonnegative and integer-graded categories, not ungraded Ext.'),
('D003','Finite-tail derived unit is an isomorphism on D+','Proved','notes/D_shadows_proof.md D.3','D002','273','Images of injectives are injective; no unsupported derived composition.'),
('D004','Elementwise bounded-weight negligible modules are not Serre; bounded modules are not localizing','Refuted','notes/D_shadows_proof.md D.4','','244-273','Explicit S/I^2 extension over Fp; infinite algebraic counterexample.'),
('D005','Correct localizing shadow quotient has full faithful derived coefficient embedding and derived unit','Proved','notes/D_shadows_proof.md D.5','D001;D004','273','Uses localizing Serre closure of bounded weights; does not equate ambiguous manuscript categories.'),
('D006','Weighted PD cochains recover RΓ(X;Z) with product and H*(X;Z)','Proved','notes/D_shadows_proof.md D.6','D005;A001;A003','11-12;273','Canonical derived-sections comparison, whose cone has bounded-weight cohomology.'),
('D006E','Enhanced shadow localization recovers the full E-infinity cochain algebra for all k,X','Proved','sections/D_enhancement.tex theorem D006E; notes/D_shadows_enhancement.md','D001;D005;D006','11-12;273','Unbounded tensor ideal by generators; explicit E-infinity evaluation cone.'),
('D006M','Integral weighted PD cochains determine finite-type nilpotent weak homotopy types','Known with proved comparison','sections/D_enhancement.tex corollary D006M','D006E;Mandell2006Main','11-12','Object determination, not fullness on maps; no binomial bridge assumption.'),
('D007','All natural convolution PD structures have the explicit parameter space P(A) with U,A,S,I equations','Proved','notes/D_coalgebras_proof.md D.7','','324-335','Intrinsic equation presentation, no hidden flatness; stronger I+ kept distinct.'),
('D008','Flat coalgebras admit a unique full natural convolution PD law, satisfying strong iteration','Proved','notes/D_coalgebras_proof.md D.8','D007;Lundkvist2008Prop2.2','324;329-335','General flat comparison checked against opened primary paper.'),
('D009','Convolution PD existence fails for a finite nonflat coalgebra over Z/4','Refuted with corrected classification','notes/D_coalgebras_proof.md D.9','D007','324','Finite adaptation of supplied Pro N43; complete exhaustive certificate.'),
('D010','Two written product/iteration relations alone do not force uniqueness, even for A=F2','Refuted','notes/D_coalgebras_proof.md D.10','D008','324','Canonical family versus u_n=0 for n>=2; missing addition compatibility.'),
('D011','Primitive nonflat coalgebras admit natural PD laws; over k/2 two full laws can differ','Proved','notes/D_coalgebras_proof.md D.11','D007;D009;Stacks07HH','324','All-index proof plus exhaustive finite example; no priority claimed.'),
('D012','Typed divided copowers classify dual natural PD laws; Sym(M) has the partition formula for all M','Proved','notes/D_coalgebras_proof.md D.12','','324','No finite dual, flatness or projectivity hypothesis; DA,DS,DI explicit.'),
('D013','Breen A1,A2 hypotheses and sheaf categories are necessary to type the manuscript results','Known, used and rechecked','notes/D_Breen_comparison.md D.13','Breen1978Thm1.3','374-376','Opened pp45-49; big versus small site distinguished.'),
('D014','Tensor coefficient formula needs finiteness; all individual Steenrod operations are Frobenius-semilinear','Refuted with corrected statement','notes/D_Breen_comparison.md D.14','Breen1978Lemma4.1;Eq4.13','374','Infinite discrete counterexample and finite F2[t]/t2 CP2 algebra certificate.'),
('D015','Odd-primary K(O,n) theorem needs Q operations and boundary excess generators','Refuted with corrected theorem','notes/D_Breen_comparison.md D.15','D013;Breen1978Thms4.3-4.4','374','Witt polynomial cocycle gives explicit p3 n1 counterexample; polynomial certificate.'),
('D016','Derived Sym and restricted duality hold with correct variance; operation representability is homotopical','Known with corrected scope','notes/D_Breen_comparison.md D.16','D013;Breen1978Lemma2.11','374','Unrestricted infinite-coefficient marginal free-algebra claim refuted by infinite-rank alternating form.'),
('D017','Finite-field restriction detects total weight below p^h; per-variable cohomology notation needs definition','Proved corrected precise claim','notes/D_Breen_comparison.md D.17','D014;D015;Breen1978Remark4.5','374','Moore-matrix proof; no inference from cochain injection alone.'),
('D018','Ext_Fp^(2j)=k[F]/(F^(v_p(j)+1)); all odd Ext including Ext1 vanish','Refuted printed exponent; known correction','notes/D_Breen_comparison.md D.18','D013;Breen1978Thm1.3','375-376','Missing +1; Witt extension belongs to Ext_Z, not Ext_Fp; not a Yoneda algebra computation.'),
('D019','Positive Ext_Fp is F-torsion; perfect-site higher Ext vanishes with specified category and site','Known, used and rechecked','notes/D_Breen_comparison.md D.19','D018;Breen1978p41;Milne1976Lemma2.2','375','Attribution Breen; Milne printed witness/application. Full 1981 perfect-site chapter not opened.'),
('D020','Universal-coefficient spectral sequence and two lemmas hold with stable range and category corrections','Proved/Known under stated hypotheses','notes/D_Breen_comparison.md D.20','D014;D018','375-376','Unstabilized homology direct-sum assertion refuted by finite bar calculations.'),
('D021','Final Tor/Koszul E2 computation is valid; universal E2 collapse is false at odd primes','Known/refuted alternate readings','notes/D_Breen_comparison.md D.21','Breen1978Props5.1;5.3;7.9;7.10','376','Final glyph ambiguous; both mathematical readings settled; Yoneda product not inferred.'),
]
with (root/'logs/D_results.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages','notes']);w.writerows(rows)
events=[]
def ev(s,typ,out):events.append((s,'2026-11-19','GPT-6 Astra; ChatGPT Pro; SA08 D-agent',typ,out))
for row in rows:
    sid=row[0]
    typ='used and rechecked in this run' if sid in {'D013','D016','D018','D019','D021','D006M'} else 'independent re-proof'
    ev(sid,typ,row[2]+'; '+row[6])
for sid in ['D009','D010','D011','D014','D015','D020']:
    ev(sid,'computation or formal certificate','code/D_finite_pd_checks.py and logs/D_finite_pd_checks.json; all assertions passed; exact scope and counts in JSON; all-index claims proved separately.')
for sid,out in [
('S3-136-002-141-CE018','General graded Ext now proved by D001-D002; prompt status contradicted supplied Pro notes N32-N33.'),
('CE-F03','Flat convolution law and strong iteration rechecked using Gamma-to-symmetric-tensors isomorphism and all compatibilities; D008.'),
('CE-F04','Iterated divided powers checked; coefficient c_mn=(mn)!/(m!(n!)^m); D008 and D011.'),
('Pro-N43','Nonflat obstruction independently checked and made finite over Z/4; D009.'),
('R13','Flat statement independently reproved; nonflat obstruction strengthened by finite example, uniqueness distinguished; D007-D012.'),
('R14','374-376 comparison completed; printed valuation exponent and reading Ext1 category are corrected; D013-D021.'),
('L8','Extended algebra differs from ordinary Steenrod algebra, but unit common and P0 distinct; automorphism conclusions require B-agent proof; D014.'),
('B-01','Focused independent audit of arbitrary PD triples, derivative recursion, endpoint typing, mixed commutators and simplicial identities; notes/D_Baudit.md.'),
('B-03','Focused independent audit of binary derivations, convergence, Delta-weight inverse and finite exterior inverse; notes/D_Baudit.md.'),
('B-discontinuous-ultrafilter','Independent check of compact pointwise limit automorphism and infinite-order witnesses; notes/D_Baudit.md.'),
('A006','Independent check of derived-tail image formula, Kan lifting cokernel, triangle shifts and product identification; notes/D_main_review.md.'),
('A007','Independent check of completed bar construction and filtration-preserving comparison transfer; notes/D_main_review.md.'),
('A008','Associated-graded exactness plus complete filtration gives Ehat_i equivalent F^iS; notes/D_main_review.md.')]:
    ev(sid,'used and rechecked in this run',out)
ev('reading-136_282-376-lines394-395','refuted, with the refined statement D018','Witt extension is Ext_Z, not Ext_Fp; Ext_Fp^1=0 literally, not only modulo F-torsion.')
ev('scan376-Ext-even-formula','refuted, with the refined statement D018','Breen1978 Thm1.3 p47 and final deduction p116 visibly give v_p(i)+1; smallest i1 gives Ext2=k.')
ev('scan374-odd-prime-generator-list','refuted, with the refined statement D015','Explicit nonzero Witt class in H2(BGa,Ga) absent from P-only generator list.')
with (root/'logs/D_CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(events)
print({'statements':len(rows),'check_events':len(events)})
