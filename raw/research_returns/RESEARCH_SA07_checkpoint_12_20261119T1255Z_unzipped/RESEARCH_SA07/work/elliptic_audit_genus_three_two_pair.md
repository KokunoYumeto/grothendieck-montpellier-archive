# Independent audit of F.3.28: genus-three two-pair tangencies

Auditor: OpenAI GPT-6 Astra, elliptic_splitting; effort inherited. Date: 19 November 2026. Verdict: **pass for the exact stated universal-image assertion**. The statement remains on the original six-dimensional homology, with tangencies imposed on four basis lines spanning two paired handles. It does not assert that a general detecting cover provides those four lines.

Files read in full: `work/LM6_A22_genus_three_two_pair.tex` and `work/check_genus_three_two_pair_partial.py`. The original F.3.24 geometric-image construction and F.3.25 torus projector were also re-read at their points of use. The proof uses these already established constructions as dependencies; it does not replace their actual maps with formal derivations on a quotient curve.

## 1. Exact geometric kernel

I visually re-read Nakamura's original 1996 printed p.117, using `work/sources_audit_next/Nakamura1996_images/page20.png`. Equation (4.7.1) is the equivariant exact sequence from the actual geometric image into the universal image and then to the arithmetic quotient. In the proof of Theorem (4.8) on the same page, the topological Johnson image is explicitly contained in the geometric image. Therefore the map q6 kills the actual degree-six Johnson image after the strict punctured-action identification proved in F.3.24.

Each displayed delta_uvw is in the degree-one Johnson image. That image, with its graded brackets, maps to the actual graded geometric image. Consequently the two literal right-nested brackets Z1 and Z2 in (PT.5) belong to J6 and to U_{3,6}; q6(Z1)=q6(Z2)=0. Repeated entries such as delta_adf cause no problem: the program uses the stated nested bracket, not a wedge of its six inputs. I checked that its bracket loop implements exactly right-nesting.

The canonical special degree-six representative is the same one used in F.3.24. No separate, arbitrary lift of Z1 or Z2 is introduced. This is the required map connecting the finite derivation vectors to the kernel of the actual arithmetic quotient.

## 2. Extension to all tensor invariants

The finite-dimensional rational Sp-module U_{3,6} is a submodule of h_{3,6}, as proved by the geometric conjugation and Zariski-density argument in F.3.24. Its target Q6 is Sp-trivial. Complete reducibility in characteristic zero gives an equivariant projection h_{3,6} to U_{3,6}; composing q6 with that projection extends q6 and retains its vanishing on every vector in J6. An equivariant projection from V tensor-power 8 to the image of h_{3,6} then extends it once more.

For full typing, this extension may be taken Q6-valued, or applied after every scalar linear functional on Q6. Thus the argument needs no unstated dimension-one assumption on Q6. The parent confirmed that the particular Q6 here is one-dimensional by the previously read Nakamura rank table, but the vector-valued formulation is valid independently of that specialization.

I independently read the local original Morita--Sakasai--Suzuki v2, printed pp.7--8. Page 7 defines the dual contraction alpha_C as the product of the k pairings times the sign of the matching. Proposition 2.1, p.8, explicitly states surjectivity for **every** g; only bijectivity requires g>=k. At 2k=8 and g=3 this supplies all invariant functionals, with possible relations among the 105 matchings. Independence of those 105 coordinates is not used. Passing from the source's signed convention to the program's unsigned matching convention is an invertible diagonal change of the 105 coordinates, so the same coefficient change acts on K(P0) and K(J6) and preserves the required inclusion.

The symplectic tensor map sends D to sum_i(a_i tensor D(b_i)-b_i tensor D(a_i)), exactly as used by `contractions` and `ES`. It is injective because its six first-slot coordinates recover all six values of D.

## 3. Completeness of the 31-dimensional partial-tangent calculation

The torus weight t^3 for a degree-six derivation makes the degree-eight specialness equation have paired multidegree (n1,n1,n2,n2,n3,n3), with n1+n2+n3=4. The fifteen blocks in the program exhaust those possibilities.

For a constrained generator x, writing D(x)=[A_x,x] requires the complete degree-six Lie space of multidegree ds-e_x-e_partner(x), exactly the basis selected in the program. This parametrization is injective: the centralizer of a free generator in the free Lie algebra has no nonzero homogeneous degree-six part. One elementary proof embeds into the free associative algebra, where a homogeneous element commuting with x is a multiple of x^6; the one-generator free Lie algebra has no degree-six element. For an unconstrained generator, every degree-seven Lie word of multidegree ds-e_partner(x) is included. The parameter columns therefore neither omit permitted values nor add a parameter kernel.

Standard Lyndon bracketing is implemented by taking the longest proper Lyndon suffix. Its leading associative word is the original Lyndon word with coefficient one and all remaining words larger. The coefficient restriction to the Lyndon row words is therefore injective on the relevant free-Lie multidegree. The modular matrix supplies a genuine rank lower bound for the full specialness map.

For every modular kernel basis vector the program finds a nonzero scalar modulo 101 and checks the resulting integer vector against the integer matrix. It then constructs the full derivation and independently verifies all associative coefficients of D(omega)=0. Since their free-coordinate reductions remain independent, the lifted integer vectors supply the matching rational upper bound. The resulting 31 derivations are therefore a basis over Q and, by scalar extension, over every Q_ell. No congruence-only equality is assumed.

The twenty degree-one deltas enumerate the complete basis of Lambda^3(V). Applying all their ES7 bracket equations produces the full 3920-by-31 integer matrix. Its modular rank is 15, and the sixteen independent lifted integer vectors are checked in the original integer matrix. This proves dim(P0)=16 over Q and Q_ell. The geometric-normalizer equation from F.3.24 places the actual U_{3,6} intersect P in this complete kernel.

## 4. Integer image certificate and arithmetic conclusion

The two geometric contraction vectors have the first nonzero two-row minor at rows 0 and 7. Its entries are [[-104,-288],[32,192]], with determinant -10752. These rows represent the two specified matchings. For each of the sixteen integer kernel basis vectors the program solves for the two coefficients by this minor and verifies the identity in all 105 coordinates after multiplication by the determinant. Therefore it proves the full rational inclusion K(P0) in span(K(Z1),K(Z2)), and hence in K(J6). The determinant's prime divisors do not restrict the conclusion over Q_ell: every nonzero rational number is invertible there, including at ell=2,3,7.

Every extended invariant functional is a linear combination of the contractions. Evaluating it on the displayed contraction identity gives the same linear combination of its values on Z1 and Z2, both zero. This proves q6(U_{3,6} intersect P)=0. The full diagonal torus preserves all four line tangencies and the unconstrained complement. The already established weight projector in F.3.25 preserves U_{3,6}, preserves this partial-tangent subspace, and leaves q6 unchanged while projecting to weight t^3. Thus the balanced calculation proves the full assertion (PT.1).

## 5. Independent program run

I ran `python work/check_genus_three_two_pair_partial.py` independently on 19 November 2026. It exited 0 and printed `ACTUAL_WALL_SECONDS 8.859784069`. Every block, all integer lift multipliers, the 3920-by-31 trace matrix, rank 15, kernel dimension 16, the two geometric brackets, the determinant -10752, and all sixteen coefficient triples agreed with the retained `work/check_genus_three_two_pair_partial.output.txt` (whose earlier wall time differs, as expected). The program's bounded modular products fit int16; exact matrix products are checked against explicit int64 bounds. The integer polynomial operations themselves use Python integers.

No gap was found in the stated partial-summand result. The one-pair discovery calculation is outside its proof and supplies no arithmetic vector. The result makes no assertion about arbitrary CM line configurations, all detecting covers, or the unresolved general LM6 subgroup problem.
