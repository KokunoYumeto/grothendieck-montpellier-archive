from pathlib import Path
from datetime import datetime, timezone
import csv
R=Path(__file__).resolve().parent;OUT=R.parents[1]/'deliverables'
now=datetime.now(timezone.utc).isoformat();who='GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'
p=R/'findings.tex';s=p.read_text();assert '\\label{G-13}' not in s
s+='\n'+(R/'g13_fragment.tex').read_text()
s+='''
\\paragraph{Complexity lower-bound context.}
The multiplicity statements G-10--G-13 locate particular representation
sectors and degrees. They do not improve the established quadratic
lower bound $\\overline{\\operatorname{dc}}(\\operatorname{per}_m)
\\geq m^2/2$ of Landsberg, Manivel, and Ressayre (2013);
the inspected April 2010 author version states it as Theorem~1.0.1,
p.~1 (G-B16). No claim about the strongest currently proposed lower
bound is needed here. A noncontainment result by itself does not
specify the four-row or rectangular multiplicity differences proved
in the present restricted parameter ranges.
''';p.write_text(s)
with (R/'questions.tsv').open('a',newline='') as f:
 csv.writer(f,delimiter='\t',lineterminator='\n').writerow(['G-Q13','Prompt Q1/Q2; G13 weighted quotient filtration; Derksen2001 and Chardin1989','Can the first rectangular-gap degree be bounded without the factorial Veronese?','PROVED G-13: some d<=beta[(u+1)((n beta^2)^u−1)+1], with log bound O(n²logn), in all stated stable dimension-gap ranges; exact successful degree not specified.'])
rows=[
('R-17','targeted proof check','PASS full root reading: unique complementary matchings give signed equality of determinant/permanent base Jacobian images; exact determinant dimension including n=1,2,3; stable quotient dimension; numerical padded pairs and G12 exclusion force nonrectangular labels.'),
('R-18','targeted proof check','PASS full root reading: disjoint row pairs and both cofactor identities; both limiting normal families; exact A-coefficient ratios; four binary cubic normalization; root-of-unity mode determinant; Toeplitz Schur minor; two Vandermonde systems; simultaneous deformation and sqrt(3/2) padding range.'),
('R-18','computation or formal certificate','PASS independent root symbolic expansion of both cofactor identities, A_V/A numerator and cubic evaluation determinant; determinant independent of X. Script check_r18_cubics.py and result r18_cubic_check.json. Finite symbolic supplement, not a formal proof of all results.'),
('G-13','targeted proof check','PASS complete root reading of independently drafted proof: affine generator embedding; homogenized degree n beta; weighted-to-ordinary filtration inclusion; cumulative affine Hilbert equals projective Hilbert; algebraically independent generator subset; exact binomial ratio and strict threshold; rectangular invariant pieces; O(n²logn) logarithmic degree bound.'),
('I-22','targeted proof check','PASS full root reading: explicit zero prescribed scalar/nonzero full word-algebra example and nonzero radical word killed by every simple quotient; examples remain within source characteristic-zero assumptions; no disproof of headline existence claimed.'),
('I-23','targeted proof check','PASS full root reading: formal Plucker exchange equalities in every characteristic; connected exchange graph and integral additive weights; classification of binary additive functions; pairwise Hamming-distance sum; quantified all-seeds-coherent Hoza limitation.'),
('I-24','targeted proof check','PASS full root reading: nested projection factors give every interval exact generic/constant rank>=2; unit-rank truncated form; fresh-variable reset recursion and h_w=3*2^(w−2)−2; scalar monomial; final rank-one local test. Explicitly not a hitting-set lower bound.'),
('I-25','targeted proof check','PASS full root reading: constant cut normalization preserves decomposability; nested irreducible Grassmannian images; remove nongrowth positions through continuity on invertible open sets; hyperplane nonvanishing; rational endpoint-field reduction. Only existence of a low-support monomial is claimed.'),
('I-B08c','used and rechecked in this run','Root independently opened primary arXiv2602.13449 PDF and read Definition2.1 p4, repeated equivalence section3.1 p6, Lemma3.1 pp6–7 and its invalid radical inference. The I22 examples directly contradict those written claims.'),
('G-B16','used and rechecked in this run','Root inspected primary author April2010 LMR PDF Theorem1.0.1 p1 and definition of border determinantal complexity. Established quadratic lower bound is used only as prior-result context, not as a latest/best assertion.')]
with (R/'integration_03_check_events.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['statement_id','date','who','type','outcome'])
 for i,t,o in rows:w.writerow([i,now,who,t,o])
p=R/'sources.md';s=p.read_text();s+='''

## G-B16 — Existing quadratic border-complexity bound

Landsberg, J. M., Manivel, L., & Ressayre, N. (2013). Hypersurfaces with degenerate duals and the Geometric Complexity Theory Program. *Commentarii Mathematici Helvetici, 88*(2), 469–484. https://doi.org/10.4171/CMH/292

Primary author version inspected: https://math.univ-lyon1.fr/~ressayre/PDFs/lmr.pdf , dated April2010. Its exact locator is Theorem1.0.1, p.1, with the border-complexity definition immediately preceding it. The published bibliographic metadata was corroborated by the publisher record. This source supplies established prior-result context: the present linear-padding multiplicity constructions do not improve that quadratic lower bound. No latest/best lower-bound assertion or acceptance of unrelated newer preprints is made.
''';p.write_text(s)
p=R/'grothendieck.tex';s=p.read_text();marker='\\subsection{What the manuscript record does and does not establish}'
new=r'''
\paragraph{R-17. Identical tangent-image modules and distinct isotypic sectors.}
At the cyclic pencil, the determinant and permanent differential maps have the same image up to signs of their columns. Their rank equality, together with the group-scheme fiber bound, gives the exact determinant-image dimension. D-FGA and D-S3 transport this computation. The two finite padded pairs then compare Hilbert polynomials, while the cocharacter specialization of G-12 removes the determinant-character summands. Their remaining positive differences are necessarily nonrectangular Schur summands in D-S6.

\paragraph{R-18. Two compatible normal families on the same scheme curve.}
Both local permanent identities hold on the same one-parameter deformation. The character decomposition of the special-fiber quotient now has two independent sections per permitted mode. The four-column coefficient determinant is the Schur operation $s_{(4^b)}$, interpreted in D-S6; its root-of-unity specialization is checked by a Weyl alternant. D-FGA turns their joint nonzero minor into an open rank condition, giving the improved padding range. The simultaneous nature of the deformation is necessary: ranks obtained at unrelated pencils are not added.

\paragraph{G-13. A weighted filtration inside an ordinary projective embedding.}
Generators of the reductive invariant quotient have specified positive degrees. Its cumulative graded module embeds in the ordinary polynomial-degree filtration of their affine coordinate embedding. Homogenizing that embedding gives an integral projective closure, to which the D-FGA Hilbert and degree comparison applies. Algebraically independent homogeneous sections provide the lower filtered dimension. This reduces the finite first-gap bound without asserting equality of the two filtrations or generation by a small Veronese degree.

\paragraph{I-22. Ordered coefficient modules and the radical quotient.}
The actual ROABP coefficients occupy an ordered product subspace, which need not equal the associative algebra generated by all layer coefficients. Passing to the semisimple quotient loses radical-valued sections even when their specified boundary functional is nonzero. In D-FGA these are different linear maps and different kernels; in representation $K_0$ the composition factors alone do not recover the off-diagonal extension data. The explicit triangular examples show the missing information before any trace or purity estimate can be applied.

\paragraph{I-23. Cocharacters preserving a Pl\"ucker subscheme.}
The Grassmann cone is cut out by the Pl\"ucker ideal. A diagonal cocharacter preserves that subscheme precisely when its weights satisfy the proved exchange equalities, which identify the integral torus weights induced from the original rank-$w$ bundle, up to a common character. D-S3 supplies the cocharacter lattice and D-FGA the Grassmannian. The binary classification and code-distance sum then quantify the cost of imposing this exact subscheme-preservation condition on every Hoza seed.

\paragraph{I-24. Constant-rank maps with repeated loss of remembered directions.}
The nested projections and their univariate perturbations define maps of free modules over an affine parameter scheme. Every interval lies on its specified unit-minor rank chart, including over the finite Artin quotients used in I-21. Nevertheless the selected boundary section is one monomial of exponential support. D-FGA's rank stratification records this phenomenon exactly; the ranks alone do not bound the length of a coefficient-support filtration.

\paragraph{I-25. Nested projective images on a Grassmannian.}
Invertible factors act regularly on the Grassmannian of rank-$r$ quotients or subspaces. The irreducible prefix image closures are nested because the constant factor is the identity; every strict inclusion raises dimension. D-FGA's Grassmannian chart gives dimension $r(w-r)$, and its projective geometry identifies scalar vanishing with containment in a hyperplane. Removing equal-image steps therefore gives the stated support existence bound. The invertible-factor hypothesis is what allows this proof to omit the reset behavior in I-24.

'''
assert marker in s;s=s.replace(marker,new+marker);p.write_text(s)
for name in ['intro.tex','open_gates.tex']:
 p=R/name;s=p.read_text().replace('R-15--R-16','R-15--R-18').replace('below $\\sqrt5/2$','below $\\sqrt{3/2}$')
 if name=='intro.tex':s=s.replace('G-12 excludes that rectangular sector','G-13 bounds the first possible rectangular gap by a degree with logarithm $O(n^2\\log n)$. G-12 excludes that rectangular sector')
 p.write_text(s)
p=OUT/'IMPLICATIONS.md';s=p.read_text().replace('R15–R16','R15–R18').replace('1<n/m<sqrt(5)/2','1<n/m<sqrt(3/2)');s=s.replace('G12 excludes these rectangular gaps','G13 gives a much smaller finite first-gap bound, with logarithm O(n²logn), while G11 retains its separate every-degree progression. G12 excludes these rectangular gaps');p.write_text(s)
with (OUT/'LEDGER.md').open('a') as f:f.write('\n\n## '+now+' — further proof-checked movement\n\nR18 improves the unbounded genuine-padding ratio to every fixed value below sqrt(3/2), with explicit rectangular labels through G11. R17 gives exact determinant-image dimension and two concrete padded pairs where the forced four-row gaps must be nonrectangular. G13 reduces the first rectangular-gap degree bound to one whose logarithm is O(n²logn), using cumulative quotient filtrations instead of a factorial Veronese. I22–I25 precisely test the next growing-width repairs: false active-simple-block claims are refuted; every-seed Plücker-compatible code masks have quantified cost; preserved-rank words can require exponentially supported lowest components; invertible chunks nevertheless admit an intrinsic Grassmannian support bound. Root whole-proof checks and independent reviews are recorded. This is an ordinary progress entry, not the scheduled three-hour review.\n')
print(now)
