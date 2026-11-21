from pathlib import Path
from datetime import datetime, timezone
import csv

root = Path(__file__).resolve().parent
p = root / 'grothendieck.tex'
s = p.read_text()
rect = r'''
\paragraph{R-13. A finite family of integral rank certificates and a torus quotient.}
For each stated size the Jacobian is a map of free modules on the affine pencil-parameter scheme. Its displayed minor defines a principal open rank locus over $\mathbb Z[1/101]$ and over $\mathbb Q$. The independent permanent identities check that these are the derivatives of the same morphism, rather than arbitrary matrices. For larger sizes the row-column torus acts in the fibers with the computed one-dimensional stabilizer. D-S3, VI$_B$~4.1 and the cited EGA dimension result, together with the elementary fiber-dimension calculation, give the upper bound. Highest-weight ideal restriction in D-FGA then yields the stated finite-range multiplicities. This extends the rank and Schur-functor dictionary of cote~133, scan~028; it does not turn a modular certificate into a characteristic-free semisimple decomposition.

\paragraph{R-14. The projective multiplication image and Hilbert growth.}
The map sending a line and a degree-$m$ form to their padded product is a morphism from $\mathbb P^3\times\mathbb P(\mathcal P_{m,4})$. Properness makes its image closed, and the unique linear factor of a general product makes the morphism generically injective. The resulting affine cone has dimension $c_m+3$. Its homogeneous ideal and Hilbert function are the D-FGA objects of EGA~II~2.4--2.5 and FGA Expos\'e~221, Theorems~3.1--3.2. The dimension comparison forces a larger Hilbert function in large degree, and D-S3 identifies the corresponding highest-weight multiplicities. The same proof therefore transports exactly; no effective degree threshold or new purity statement is inserted by this reformulation.

\paragraph{R-15. A normal direction to a family of pencil images.}
The cyclic pencil is a point of the affine parameter scheme, and $W_0$ is the image of its tangent map. Restriction to the explicitly defined lines $\Lambda_i\subset\mathbb P^3$ and the independent interval sections computes a lower bound for that image. The residue calculation proves that the section $T$ gives a nonzero class in the quotient by $W_0$. The two-chord family makes this class lie in the tangent image away from the special parameter, while an augmented determinant witnesses persistence of independence on a principal open. These are explicit maps of coefficient modules and open rank loci in D-FGA, defined over an integer coefficient ring after choosing the stated integral parameters. The generic characteristic-zero dimension and Hilbert argument then gives the four-row inequality for every equal size. D-S3 and D-S6 identify its weight and Schur class. Cote~133, scan~028 supplies the tensor-module setting; scan~019 explains why this is a multiplicity assertion rather than a numerical CUE dimension alone.

'''
if '\\paragraph{R-13.' not in s:
    s = s.replace('\\subsection{Isolation as a torus action and a problem of coefficient modules}', rect + '\\subsection{Isolation as a torus action and a problem of coefficient modules}')
iso = r'''
\paragraph{I-14. A Grassmannian open condition for several substitutions.}
The row plane of the coefficient matrix is a point of $\operatorname{Gr}(r,F^s)$. A fixed family of cocharacters gives the integral linear map $P_{\mathcal W}^{\mathsf T}$. The desired locus is the open set where its restriction to the tautological rank-$r$ bundle is injective. Its complementary equations are the displayed linear forms in Pl\"ucker coordinates. D-FGA, Expos\'e~221, Proposition~3.8 is the Grassmannian framework, and D-S3 identifies the cocharacters. The example proves that this open set depends on coordinate values and can be larger than the union of the individual basis-isolation loci.

\paragraph{I-15. A finite character-lattice obstruction.}
The bounded seed decoder produces a subspace of cocharacters of the split torus. Pigeonhole counting gives two distinct characters whose difference annihilates every cocharacter in that subspace. Their binomial is therefore a nonzero regular function in the kernel of every pullback. This is precisely the character/cocharacter pairing of D-S3, I~4.7.3, with the finite integer bounds retained. The extension to bounded-degree Boolean decoders is a dimension bound for their cocharacter span. It does not forbid more general maps whose spans are larger.

\paragraph{I-16. A finite coefficient-state scheme and base-field points.}
Over $\mathbb F_q$ the coefficient row space has $q^w$ rational points, and each letter acts on it by a linear morphism. The state automaton records these morphisms exactly. The separate evaluation lower bound counts the rational points avoiding products of prescribed coordinate divisors. Both constructions live in affine schemes over the finite field; D-S3 gives the coefficient representation, while D-FGA distinguishes the finite set of rational points from the whole scheme or its extension-field points. Purity does not change the explicit counting inequality.

\paragraph{I-17. A trivialization on an invertibility open set.}
The nonzero determinant polynomials define an open set on which the constant transition maps are bundle isomorphisms. The displayed gauge change trivializes those constant maps. The nested coefficient row subspaces can then grow at most $w-1$ times, and their chosen sections have the stated support. This is a concrete filtered-module argument in D-S3 and a rank-stratum argument in D-FGA. The known AGKS invertible-factor result is cited separately; the proof establishes the particular permutation-invariant sampler stated here.

\paragraph{I-18. A unit minor over a discrete valuation ring.}
Over $F[[\varepsilon]]$, a maximal minor defines an open rank locus precisely when it is a unit. A nonzero nonunit meets the generic fiber and misses the special fiber. The explicit matrix family separates these two cases, and the ideal of sampled scalar values shows why saturation in the fraction field does not recover an original evaluation. This is the elementary local-module form of the determinantal loci in D-FGA. The distinction from a flat Rees degeneration is essential: flatness of an ambient family does not imply surjectivity of this particular compressed module map.

\paragraph{I-19. Rank-factorization charts and the coefficient field.}
On the principal open where a chosen minor is invertible, a rank-$r$ bundle map factors through a rank-$r$ bundle. The adjugate formula clears its denominator and is an integral polynomial identity. Passing to the function field of the cut-variable scheme makes the intervening blocks disjoint; it does not remove the cut variables from the original base. Multilinearity proves coefficient-span preservation under independent local substitutions. D-FGA supplies these rank charts and D-S3 the tensor contractions. The unresolved descent from the cut-variable function field is explicitly retained.

\paragraph{I-20. Bounded losses in a sequence of coefficient subspaces.}
The product of a nonzero coefficient and the selected pivot minors defines a principal open on the cut-coordinate affine scheme. The finite grid meets this open by the degree bound. After specializing there, the coefficient subspaces have total dimension loss at most $\kappa$; hence their total growth is at most $w-1+\kappa$. This is an exact rank and filtration argument on the same D-FGA charts as I-19, followed by the D-S3 coordinate grading. It yields the stated sampler with its parameter dependence, without asserting that arbitrary singular sequences have bounded total loss.

'''
if '\\paragraph{I-14.' not in s:
    s = s.replace('\\subsection{Purity, arithmetic sampling, and the limits of numerical shadows}', iso + '\\subsection{Purity, arithmetic sampling, and the limits of numerical shadows}')
pur = r'''
\paragraph{P-09. Positive Hermitian forms on a Segre cone.}
The width-one coefficient tensors are decomposable sections, forming a Segre cone. Applying the upper sampled-energy bound to the conjugate evaluation tensor bounds each weighted evaluation norm, while applying the lower bound to the monomial sections bounds their total trace. This is the complete rank-one tensor proof of the cardinality inequality. D-S6 identifies tensor products and D-FGA the Segre coefficient scheme. The inequalities themselves use a complex Hermitian realization and are not inequalities in integral $K_0$.

\paragraph{P-10. Projective incidence and avoidance of a determinantal cone.}
The tensor-train class is the closed cone defined by the stated flattening minors. Its projectivization and evaluation hyperplane sections give a projective incidence correspondence. Proper projection makes the bad tuples a closed set; successive hyperplane sections show this set is proper at the stated cardinality. For unknown order one uses the finite union of the permuted cones. This is D-FGA's projective and determinantal geometry with D-S3's coefficient grading. Compactness of the complex unit sphere gives a positive Hermitian lower bound only after kernel avoidance is known. Neither the projective argument nor the $K_0$ class bounds the integer heights of an explicit good tuple.

\paragraph{P-11. Pullback along an explicit arithmetic parameterization.}
The presentation $\alpha_i=A_i(\theta)/b$ specifies a morphism from an affine parameter scheme to the variable space after inverting $b$. Pulling back a polynomial to $G_f(U,T)$ and using the stated degree grid gives the unconditional forward construction. Conversely Lagrange interpolation and a cyclotomic point give a finite \emph{\'etale} arithmetic realization after inverting the discriminant; minimal-polynomial degree prevents a nonzero rational pullback from vanishing there. D-FGA describes the morphism and its kernel, and D-ET places the finite cover. The proof does not require a Frobenius estimate: the missing hypothesis is the explicit common nonvanishing map itself, rather than a further trace bound.

'''
if '\\paragraph{P-09.' not in s:
    s = s.replace('\\paragraph{P-Z01 and P-Z02.', pur + '\\paragraph{P-Z01 and P-Z02.')
s = s.replace('R-07. Binary-form restriction and highest-weight sections.', 'R-07. Binary restriction and highest weights.')
p.write_text(s)

event = root / 'integration_01_check_events.tsv'
if not event.exists():
    now = datetime.now(timezone.utc).isoformat()
    with event.open('w', newline='') as f:
        out = csv.writer(f, delimiter='\t', lineterminator='\n')
        out.writerow(['statement_id','date','who','type','outcome'])
        who = 'GPT-6 Astra Pro; effort not exposed; agent=/root; run=CUE_GCT_20261121_R1'
        details = {
          **{f'R-{i:02}':'Complete written proof read, including source specialization, dimension and highest-weight transfer; finite certificates retain their separately recorded execution scope.' for i in range(10,16)},
          **{f'I-{i:02}':'Complete written proof read; coefficient-span, rank and sampling hypotheses checked; no formal certification.' for i in range(13,21)},
          **{f'P-{i:02}':'Complete written proof read during this run; recorded now. P10 finite-union unknown-order refinement also read in full.' for i in range(9,12)},
          'G-B06':'Corrected associated-sheaf locator to EGA II Proposition2.5.2 in manuscript and source register; independent review identified the setup/statement distinction.'
        }
        for sid, desc in details.items():
            out.writerow([sid,now,who,'targeted proof check' if not sid.startswith('G-B') else 'used and rechecked in this run','PASS: '+desc])

sp = root / 'sources.md'
src = sp.read_text()
for name in ['ARCHIVE_133_scan006.tex','ARCHIVE_133_scan008.tex','ARCHIVE_133_scan009.tex','ARCHIVE_133_scan019.tex','ARCHIVE_133_scan028.tex','SA17_STUDY_cote133_lambda.md']:
    if '`'+name+'`' not in src:
        src = src.replace(name, '`'+name+'`')
sp.write_text(src)
print('Integrated R13–15, I14–20, P09–11 dictionary entries and actual root proof-reading events.')
