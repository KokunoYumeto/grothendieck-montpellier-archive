# Root audit after checkpoint 07

Date: 19 November 2026. Author: OpenAI GPT-6 Astra, inherited effort, root.
This record supplements the dated check events. No source consultation or
finite computation is itself counted as movement at the timed review.

## E.2.25: integral comparison on all simple factors of dimension at most two

We read AS-1 through AS-4 in `agent_surface_integral_tower.md` in full and
independently checked the following actual maps and hypotheses.

The field of definition is enlarged finitely to define the finite list of
models, endomorphisms, polarizations, conjugate isogenies and Hodge tensors.
The product monodromy equality is an equality in its labelled block
representation. Its non-CM factors have derived groups Sp4, Res(F/Q)SL2,
or SL1(B^op), with the quaternion algebra acting on the left and its
centralizer acting on the right. In the last case the right reduced norm
is the polarization multiplier; this equality follows over Q from its
verified matrix equality at one split completion and faithful scalar
extension. The common multiplier has connected simply connected kernel H.
The quotient of the cocharacter lattice by the coroot lattice is Z, and
the Hodge cocharacter maps to a generator under that same multiplier.
These are precisely the Hodge-maximality hypotheses of the cited adelic
theorem. A finite extension preserves open image because its compact
image has finite index in the preceding compact image.

We checked the conjugate-isogeny equation on the actual completed Betti
maps. The conjugation commutators lie in the image of Gamma_Qcm.
Independently supported elements in an open adelic product isolate each
swapped factor by one further commutator. In the fixed RM case a field
automorphism either exchanges split local factors or acts nontrivially on
the centroid of the local Lie algebra. With trivial field action, the
anti-complex-linear real planes force trace zero and exclude a scalar at
every completion. In the quaternionic case Skolem--Noether removes the
left inner automorphism, leaving right multiplication by an
anti-complex-linear, noncentral quaternion. This verifies the local
nontriviality before using the Lie algebra.

The explicit Cayley curves are defined also at quaternion division primes.
Conjugation by an open group spans the full simple Lie algebra from the
nonzero commutator derivative. Products of chosen curves have invertible
Jacobian; the displayed contraction proves an actual open image. At all
remaining primes, the finite normal-subgroup and lifting arguments give
the full integral factor. In the unramified RM case the lift uses every
residue coefficient and spans sl2(k_v) over F_l, so no one-dimensional
residue-field restriction has been inserted. Taking the closure of finite
supported products gives the claimed open restricted adelic product.
The closed derived subgroup maps into Gamma_Fcm and still has open image.

For rational approximation, E.2.11 supplies the rational tensor point T0
in the stated CM/Artin fibre. The difference T0^{-1}rho(sigma) centralizes
the same labelled endomorphisms and has multiplier one, hence belongs to
the displayed H(A_f). Each Q-simple factor of H has noncompact real
points, including SL1(B) for an indefinite quaternion algebra. D.4.1
therefore gives rational density in the required restricted adelic group.
The chosen rational point of an actual integral coset has integer entries
and integer inverse by Q intersect Zhat = Z. This proves an integral
isomorphism with the prescribed target, rather than only congruence
solvability at finitely many primes.

The finite-field cylinders freeze target models and all previous full
Tate matrices. Product openness leaves an open image on the next factor.
Nested compactness gives the required common automorphism, and the
exhaustion of finite Galois fields makes the selected branch unique.
Actual isogeny kernels determine the superlattices; faithful completion
then proves independence, tensor coherence and the labelled Artin
descent equations. The scope is all geometric simple factors of dimension
at most two, arbitrary CM factors and the stated whole diagram. Simple
non-CM factors of dimension at least three and the full pure category
remain separate unresolved extension requirements.

### Primary sources independently opened and read by root

* Lombardo, *On the l-adic Galois representations attached to nonsimple
  abelian varieties*, arXiv:1402.1478v4: Corollaries 4.4--4.5 and their
  proofs, printed p.12. These pages explicitly exclude type III simple
  surfaces and imaginary-quadratic endomorphism fields in the non-CM
  absolutely simple surface case. Web source `turn384372773view0`.
* Lombardo, *Explicit surjectivity ...*, arXiv:1411.1703v3:
  Theorems 1.3, 1.4, 1.7 and Corollary 1.5, pp.2--3;
  Lemma 2.4, p.6; Lemmas 5.3--5.6, pp.19--20. The geometric
  endomorphism and finite-extension qualifications, opposite-algebra
  action and cyclotomic determinant were checked directly.
  Web source `turn384372773view1`.
* Cadoret--Moonen, *Integral and adelic aspects of the Mumford--Tate
  conjecture*: Theorem A(ii), p.2; sections 1.1--1.2, p.3;
  sections 2.2--2.3, p.4. The homology convention is obtained by inverse
  dual from the source's H1 cohomology convention. The primitive
  multiplier cocharacter verifies its maximality criterion exactly.
  Web source `turn384372773view2`.
* Mayle--Wang, arXiv:2212.11472v5: Lemma 2.3(4), printed p.6,
  gives the finite symplectic normal-subgroup statement used here.
  No GRH-based numerical bound is used. Web source
  `turn384372773view3`.

We read the complete `work/code_generation/verify_surface_groups.py` and
independently ran it: exit 0, actual wall time 0.744691331 seconds.
Its exact symbolic certificates verify the Cayley alternating-form
identity, symplectic short and long root commutators, Lie-derived rank
10, scalar standard-action centralizer, RM determinant identity,
quaternion pure-element norm identity and real anti-Hodge plane matrix.
Openness, strong approximation and the countable construction have the
separate proofs checked above.

## H1: exact modular-foliation substitution

We read the complete work section 39 and independently opened Movasati's
2008 primary preprint (`turn589496958view0`), its Theorem 2, p.3,
and Corollary 2, p.14 (`turn178265020view0--1`). In the source family
the coordinate translation X=x+a carries X dX/Y to xi+a omega.
For a=h its period row is -c times the conjugate holomorphic row.
Every nonzero integral cycle has nonzero period on that row, so the
source's zero-period exclusion supplies no contradiction. The
one-algebraic-point-per-leaf theorem permits the single candidate point;
a second point on that same leaf has not been constructed.

For any algebraic a whose second-kind periods form a lattice, algebraic
raw Weierstrass invariants would give an algebraic elliptic curve with
holomorphic differential having exactly the same integral period module
as -xi-a omega. The opened Corollary 2 supplies an isomorphism pulling
back that holomorphic class to this class with nonzero xi coefficient.
The equality contradicts preservation of the holomorphic line. The
rescaling needed to obtain algebraic invariants is consequently
transcendental. This does not exclude algebraicity of the rescaling-
invariant j-value and does not change the nonzero algebraic-h gate.

We also opened the final 2022 *On elliptic modular foliations II*
(`turn589496958view1`), Theorem 1, p.105, and the original
Shiga--Suzuki--Wolfart 2009 paper (`turn589496958view2`). The former's
classification requires an algebraic leaf; the latter's relevant period
theorem requires an algebraic projective period. Neither needed input
has been supplied by the actual h-algebraicity equation. These exact
missing maps remain recorded in the work note.

## F.3.25: actual CM endomorphism action over Q

We read `LM6_A22_general_CM_Q_model.tex` in full. The action is the
actual conjugation of endomorphisms. With embeddings indexed by G/H,
the rational de Rham filtration gives sigma S = S n_sigma, including
the indicated right-action direction. The right stabilizer equals H:
a strictly larger stabilizer induces the type from a proper CM subfield,
and the displayed subfield-linear coordinate projector produces an
actual proper abelian subvariety after clearing lattice denominators.
Normality of the kernel of the actual endomorphism action then converts
left stabilization into right stabilization. The full index chain forces
H to be normal and, in the normal closure, trivial. The action is onto
Gal(E/Q) and its kernel is exactly Gamma_E.

At a completely split prime its actual Tate-module permutation is
V_phi -> V_{phi composed with a_sigma^{-1}}. Polarization pairs conjugate
eigenlines and provides the needed symplectic basis. At any other prime
all local field factors of the Galois field E have degree greater than
one. On its rank-one module no idempotent then has Q_l-rank one;
Faltings semisimplicity excludes a rational Galois line after every
finite extension defining the endomorphisms.

We also checked the universal torus projector in
`LM6_A22_CM_threefold_Q_orbits.tex`. It acts on the finite-dimensional
linear constraint space only after the six tangencies have been obtained
from actual normalizing lifts. That space and U6 are stable under the
full split diagonal torus. Lagrange interpolation at one torus element
separating the target weight projects to t^3, preserves the two
subspaces and preserves q6. F.3.24 therefore kills q6 on the full tangent
space. No arithmetic lift of this later linear projection is required.
The final integrated statement and its analytic-to-algebraic descent
reference are still to be checked before the canonical final proof event.

The final integrated F.3.25 text was then read in full. Root visually inspected the original Milne1986 printed pp146–147 and checked Corollary20.4(b) directly. The nonsplit-prime rank argument includes ramification, and the split-prime proof uses actual section lifts over Q, one common finite extension, and the same degree-six arithmetic class throughout. The finite-cover detector compares its character with the first Magnus weight in the original once-punctured curve, so its larger covering Jacobian is not substituted for the original homology. The final canonical F.3.25 proof audit passes.

Root additionally read the complete four-handle block program and reran it: exit0, actual wall1.597119087seconds, matrix5040-by960, rank958 modulo101, selected minor determinant1, two exact independent integer kernels with a determinant-minus-one independence minor, and zero S4 orbit sum for each. Witness SHA256127b51abbbdcbb44bae724088005a55ae58be45b692a260a3ec51333b9e197b9 was reproduced. The surrounding all-genus theorem still requires its full written projection and source-map audit.

## All-genus proof and source-map completion

The complete all-genus work proof was read and checked. The exact outside-handle contraction terms are p(delta A_i)+p(delta B_i); the other terms retain an outside letter and vanish after projection. The survivors are Lie polynomials of degree7, hence zero in cyclic coinvariants. Every support outside a fixed triple vanishes on that triple, so the six-dimensional genus3 certificate gives all pair coefficients zero and zero sums on each triple. On four handles, the S4 average of every multilinear degree3 conjugator is zero already by pairing the six permutations that reverse the inner Lie bracket. This supplies a direct written proof in addition to the exact word certificate. Complete reducibility extends the invariant functional without assigning arithmetic meaning outside U_g6. The subsequent diagonal-torus projector preserves the already established linear constraint space.

Root then visually re-read Nakamura1996 original printed pp115,116,117. The rank inequalities and table give r_g,n(6)=1; Lemma4.5 and (4.7.1)–(4.7.2) give the actual fibre map onto that quotient, and the paragraph preceding Lemma4.5 explicitly records finite-base-change invariance. Their scope is every hyperbolic(g,n) with n>=1. The degree-six multiplier is chi^3 and no simple-Jacobian endomorphism assumption enters these quotient statements. The additional End(J)=Z premise belongs to the later centralizer-finiteness conclusion. Thus the full source-map audit needed in F.3.26 passes.


## Further working-source audit before checkpoint08

Root visually read Vasil'ev1996 original Russian pages681–682 from the downloaded primary scan. The unnumbered theorem explicitly quantifies over any g+1 distinct rows jointly. For g=1 it controls both rows; the algebraic triangular basis change [[1,0],[a,1]] preserves its hypotheses and gives no isolated conclusion about the coefficient h. This confirms the application boundary in agent_elliptic.md §41. Root independently checked §40's third-kind residues, sigma quasi-period integral modulo pi*i*Z, real-component descent, and the exact isomorphism (x,y)↦(-x,iy). The nontorsion proof uses the actual good group orders5 and7 and primary-to-primary reduction injections. The coefficient-to-full-value-trace algebraicity bridge is not supplied. These checks concern ongoing work and do not add numbered production-paper results to checkpoint08.

Root opened Commelin2019 original final article, Theorem10.3 atp675 and Theorem10.5 atp676, including the finite-family and finitely-generated-field hypotheses and the hyperadjoint argument. Root opened Serre2013 Th1 and §3.1 atp544: the bounded Tate representations satisfy potential semistability and become an actually independent all-prime family after one finite field extension. Root opened Moonen–Zarhin1999 §2.3 and Proposition2.4 atp9, including the unitary signature(2,1), and §2.7 atp10. These Hodge-group identities are separately tracked from the arithmetic Mumford–Tate equality. Root read Lombardo1402.1478v4 Theorems2.12–2.18,p6, and opened Tankeev's original1988 English article, Theorem1 atp528, with prime dimension d≠7. The OCR drops the displayed theorem equality; the exact display and individual-case proof are still being checked before this source supports the new threefold proof. No original-source access is inferred from another author's citation.
