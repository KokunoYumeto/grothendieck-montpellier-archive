# Number-field plain integral Betti comparisons

Agent: GPT-6 Astra / `/root/period_generation`.
Date: 2026-11-19. Scratch research record; the parent controls checkpoints.

## 1. Completed numbered results

### E.2.2 — a CM elliptic curve over its ring class field

For an imaginary quadratic order O in K, an elliptic curve E with CM by O
over k=K(j(E)), together with one labelled nonreal endomorphism, distinguishes
all complex places of k through its integral H1 diagram. The proof is in
`output/RESEARCH_SA07/sections/E_numberfield.tex`.

All endomorphisms descend to k by their faithful differential character,
whose values lie in O⊂K. Representatives of complex places may be chosen to
agree on K. For a nonreal alpha∈O, the real operator T induced by alpha
recovers the complex structure by

    J=(T-Re(alpha)I)/Im(alpha).

A natural integral comparison therefore extends to a complex-linear map
carrying one period lattice onto the other. The quotient complex tori are
isomorphic, so their j-invariants coincide. Since K and j generate k, the
embeddings coincide. This uses integral invertibility, not merely rational
isogeny.

Explicit checked example: K=Q(sqrt(-5)),
j=632000+282880sqrt(5), k=Q(i,sqrt(5)), and

    y²=x³−3j/(j−1728)x−2j/(j−1728).

Campagna–Pengo §5, preprint p.11, gives the CM order and Hilbert class field.
The ideals O and (2,1+sqrt(-5)) give the two ideal classes; nonprincipality is
the impossible norm equation a²+5b²=2. The exact j formula and the polynomial
x²−1264000x−681472000 were checked by the attached script.

### E.2.3 — finite-extension descent and exact transporter

The full proof now appears in `sections/E_numberfield.tex`. Given k'/k,
the descent operation on a variety is composition of its structural map
X→Spec k'→Spec k. At v:k→C its complex fibre is the disjoint union over
extensions u:k'→C of v. The algebra A=h0(Spec k') acts by pullback and cup
product, and its primitive idempotent e_u selects that component.

A k'-correspondence is a cycle on the open and closed diagonal component
X×_{k'}Y of X_{[k]}×_kY_{[k]}; codimension is unchanged. Relative tensor
products are selected by the algebraic diagonal idempotent sum e_u⊗e_u.
A comparison over k must permute primitive idempotents, and the same
permutation selects the compatible pair of extensions on every object.
Thus a finite separating diagram over k' descends to a finite separating
diagram over k. Its finite labelled direct sum is one tensor generator.

In particular every subfield of an elliptic ring class field has a finite
separating test. The explicit real quadratic example Q(sqrt5) descends the
CM test over Q(i,sqrt5), with the degree-two Artin algebra and module action
included.

The same construction gives the bijection

    Isom^tensor(omega_v,Z,omega_w,Z)
      ≅ {g∈Aut^tensor(omega_Q,Z): g_A(e_v)=e_w}.

Forward: restrict a k-comparison to base-changed Q-objects; the diagonal
Spec k→Spec k×QSpec k gives ev_w g_A=ev_v. Reverse: restrict g on the
underlying Q-scheme of X to the v block. The two inverses are checked using
the diagonal component of X_{[Q]}×Qk and M⊗A, respectively. No algebraic-
closure extension choices occur.

Elliptic agent independently checked all these maps; root independently
checked the inverse constructions. Root also visually checked Deligne1979
original printed314 Example0.1.1 and316 (0.5.1), which use exactly the same
scheme restriction and direct sum over embeddings. Citation Deligne1979 is
included, while our integral reconstruction is proved directly.

Restriction of tensor automorphisms to finite étale Q-schemes gives a map
to Gamma_Q: deck-map naturality on each finite Galois extension forces a
left translation, compatible across extensions. Its image contains identity
and actual complex conjugation. The universal all-number-field place
injectivity assertion is equivalent to that image being exactly {1,c}.
The transporter and this equivalence are proved; the equality is unresolved.

The integral source is explicitly the smooth-projective integral algebraic-
correspondence/cohomology diagram (free parts, with grading), or an actual
integral realization extending it. A Q-linear category does not itself
supply a free-Z-valued additive fibre functor: the invertible morphism n
would have a noninvertible image. No such functor is silently introduced.

### E.2.4 — generalized-dihedral coverage and its exact limit

Let L/Q be finite Galois, K⊂L imaginary quadratic, B=Gal(L/K) abelian, and
actual complex conjugation c act on B by inversion. Since c²=1 and c∉B,
Gal(L/Q)=B⋊<c>. The transfer to B vanishes: Ver(b)=b(cbc^-1)=1 and
Ver(c)=c²=1. This is stronger than deriving only a 2-torsion condition from
the inversion action.

Choose integer f divisible by all ramified rational primes and with
conductor(L/K)|f O_K. Milne's Artin-map diagram identifies extension of
ideals with transfer. Hence every rational ideal prime to f has trivial
Artin image over K. If alpha≡a mod f O_K for rational integer a coprime to
f, choose gamma with a gamma≡1; then alpha gamma≡1, so the ray-principal
kernel gives Artin(alpha)=Artin(a)=1. Thus the exact surjection is

    Pic(Z+f O_K) = I_K(f)/P_{K,Z}(f) → Gal(L/K),
    [a] ↦ Artin_{L/K}(a O_K).

The class-field inclusion is L⊂H_f. The main CM theorem gives
H_f=K(j(E_f)); E.2.2 and E.2.3 yield the finite test for every subfield of L.

Every negative-discriminant cubic field is covered: its normal closure is
S3, its A3-fixed quadratic field is imaginary, and actual conjugation is a
reflection acting by inversion on C3.

The opposite scope statement is proved by an exact quotient: a totally
real Galois subfield T of H_f kills c in B_f⋊<c>, hence every image b has
b²=1 and the quotient is elementary abelian2. If a nonnormal totally real
field lies in H_f, so does its totally real normal closure, since H_f/Q is
Galois. Therefore a totally real field with nonabelian-dihedral normal
closure cannot lie in an elliptic ring class field. The explicit example
Q(theta), theta³−4theta+1=0, has irreducible polynomial, positive nonsquare
discriminant229, and three certified real roots. This excludes this
construction for that field; it proves no absence of other motivic tests.

## 2. Primary source access and exact locators

1. Cox, *Primes of the Form x²+ny²*, Wiley1989. Original scanned book
   downloaded with a browser User-Agent from
   https://www.math.utoronto.ca/~ila/Cox-Primes_of_the_form_x2%2Bny2.pdf .
   Local `work/sources_generation/cox_primes.pdf` has363 pages. PDFpage =
   printedpage+12. Visually read copyright1989/ISBN page; Proposition7.22
   pp145–146; Lemma9.3 pp180–181; Theorem9.18 and entire proof pp190–192;
   Theorem11.1 p220. Rendered selections in `tmp/manuscript_qa/cox_*` are
   transient QA images. The PDF is image-only; the empty text extraction
   is not evidence of a text reading. Web open failed because20MB exceeds
   its content limit; direct download and rendered scan reading succeeded.
   Search refs turn349571796search34 and turn537014290search7 corroborate
   the exact theorem and last proof page; no search snippet substitutes
   for the scan reading.

2. Milne, *Class Field Theory*, v4.03,2020,
   https://www.jmilne.org/math/CourseNotes/CFT.pdf . Opened web PDF,
   printedp162/PDFzero-index170, ChapterV §3 Proposition3.18 and surrounding
   diagram: ideal extension corresponds to transfer even with nonabelian
   outer Galois extension. References turn349571796view0,
   turn222091702view2, turn707150844view0. Direct urllib fetch returned406;
   web PDF access succeeded. No local Milne PDF is claimed.

3. Campagna–Pengo, arXiv2201.04046, §5 p11 immediately before(19), local
   `sources_generation/campagna_pengo2201.04046.pdf/.txt`. Exact source
   supports the CM numerical example. Entry GenCampagnaPengo2022.

4. Charles, *Conjugate varieties with distinct real cohomology algebras*,
   author journal proof2008, https://www.math.ens.psl.eu/~charles/crll5855.pdf,
   Theorem2 PDFp3. Its automorphism must fix one specified imaginary
   quadratic field and act nontrivially on the other. This does not supply
   a result for every prescribed pair; the exact restricted theorem is
   cited. Bibliography key Charles2009 identifies the consulted2008proof.

5. Deligne1979 original French PDF: parent inspected
   `work/source_records/Deligne1979_original.pdf`, printed314 Example0.1.1
   and316(0.5.1). Author URL
   https://publications.ias.edu/sites/default/files/33_Valeursde.pdf?download=1 .
   Parent supplied this independent source confirmation and bibliography.

6. Ayoub, *An anabelian presentation of the motivic Galois group in
   characteristic zero*, author PDF
   https://user.math.uzh.ch/ayoub/PDF-Files/Anabel.pdf . Local
   `sources_generation/ayoub_anabel2026.pdf/.txt`,257pages. Theorem2.2.3
   printed71 gives the nonconnective spectral motivic group as tensor
   autoequivalences of geometric constructible-sheaf presheaves, for a
   commutative ring spectrum Lambda. Theorem4.4.2 printed234 restricts to
   geometric local-system presheaves. Corollary4.4.15 pp248–249 gives the
   classical heart version; Corollary4.4.16 p249 treats torsion ordinary
   connected coefficients and the absolute Galois group. Construction1.4.8
   p37 supplies the Artin Hopf map. Exact source categories retained below.

## 3. Precise unresolved gates and approaches already tried

### 3.1 Arbitrary number fields

The exact remaining gate is E.2.3(d), the image of the integral tensor
automorphism group on Gamma_Q. The transporter reduces the prescribed
embedding problem to this image without assuming any Hodge filtration.
The CM descent results now prove more cases but do not prove the image
equality. The real cubic with discriminant229 was beyond the elliptic ring-class
construction, but E.2.5 below now supplies its explicit higher-dimensional
CM test. Every quadratic and cubic field is now covered. A smallest-degree
concrete remaining field is Q(alpha), alpha^4-alpha-1=0: its irreducible
quartic has discriminant -283, two real roots, and S4 normal closure. The
exact polynomial and resolvent checks are attached.

### 3.2 Ayoub/Legendre route

Ayoub constructs the stated equivalence for his full mixed/derived motivic
Betti group and relative geometric local-system presheaves. We have not
constructed a lift of an automorphism on the concrete pure integral
correspondence diagram into that full mixed/derived source. Faithful
flatness of a rational group quotient does not provide a Z-point lift.
Nor has an action on the relative Legendre local-system diagram been
constructed from the pure automorphism alone. These are actual missing
maps, not a categorical nonrelation claim.

At the group-theoretic end, the intended test uses Legendre's discrete
free monodromy subgroup generated by [[1,2],[0,1]] and [[1,0],[-2,1]].
One would need the integral action to normalize that discrete subgroup,
not just its finite completions; the subgroup is a congruence subgroup
(up to its central sign and the corresponding level-four condition), so
intersection with SL2(Z) can recover it from its closure. The next map
would compare the resulting automorphism of the discrete free group
with the Galois action on its profinite completion, then impose the three
puncture classes and use the faithful Galois action on dessins. None of
these latter statements has been promoted to a theorem of the present
integral pure diagram without the missing relative realization maps.

### 3.3 Other published conjugate-variety examples checked

Schreieder2014, *Multiplicative sub-Hodge structures of conjugate varieties*,
ForumMathSigma2 e1, author PDF
https://www.iag.uni-hannover.de/fileadmin/iag/homepages/schreieder/publications/Conjugate_Varieties_FOM_Sigma.pdf
has existence results (Th3p3, Th6p4, Th7p5), but the coefficient-field and
chosen-automorphism hypotheses do not give every prescribed embedding
pair. No enlargement of those hypotheses is asserted.

Shimada arXivmath/0611596, Example4.1 p13, gives the cubic
17t³−18t²−228t+536 and singular K3 transcendental lattices
[[10,4],[4,22]] versus diag(6,34) at its real and complex places. Its
discriminant is -51*(3792)², so its normal closure already lies in the
generalized-dihedral scope now proved. The K3 example is useful independent
evidence but is not needed for E.2.4 and has not been added as a new result.

### 3.4 Plain torsor-class surjectivity with existential RH comparison

The Hodge deformations in E.3.3–4 leave the plain integral fibre functor
isomorphism class unchanged, and therefore do not refute surjectivity onto
plain torsor classes. Allowing an existential comparison to de Rham may
admit such deformations by alpha'=alpha g^-1; this is already explicitly
recorded in the parent's section. A separate construction of a new plain
integral fibre-functor class, or a proof that every such class arises from
a place, is still required. No such construction is claimed here.

## 4. Computation and check records

`work/code_generation/verify_numberfield_descent.py` and its exact output
are copied to `output/RESEARCH_SA07/code/`. They verify the displayed CM
model, its class polynomial, and the real S3 cubic exclusion example.
`work/generation_check_events.tsv` contains canonical statement IDs and
the prompt's exact event type vocabulary. Independent checks are attributed
in the outcome text, not inflated into an independent re-proof event.


## 5. Further proved movement: E.2.5, all totally real fields

The paper now proves a finite real, hence integral, separating diagram for
every totally real number field F. For degree n>=3 take K=F(i) and choose
the CM type Phi with +i at the specified inclusion of F and -i at all other
real embeddings. Choose b in O_F with one positive and all other negative
conjugates. The analytic abelian variety is C^Phi/Phi(O_F[i]), with integral
Riemann form Q(x,y)=Tr_K/Q(i b x conjugate(y)). At each type embedding its
coefficient has positive imaginary part, so the Riemann positivity is
verified explicitly. Its Rosati involution restricts to complex conjugation
on K. Milne7.9 supplies an algebraic Qbar model and descent of all labelled
morphisms; a finite number field L contains the finite defining data.

On H1_R, labelled K-action gives one real two-plane for each real embedding
of F. Those planes are orthogonal because F is self-adjoint. On each, the
analytic complex structure is s_tau I_tau with s_tau=+1 or -1; polarization
positivity makes sign Q(x,I_tau x)=s_tau. A labelled real comparison commutes
with I_tau and has Q'(Tx,Ty)=lambda Q(x,y), using ONE Tate scalar common to
all factors. Hence s'_tau=sign(lambda)s_tau simultaneously. Thus the types
are equal or globally conjugate. This is a proved extraction map from plain
Betti algebraic data, not an added Hodge-filtration hypothesis.

The traces t_Phi(i)=(2-n)i and t_Phi(i a)=i(2a-Tr_F/Q(a)) generate F(i).
Consequently a comparison between L-embeddings forces equality/conjugacy
on F(i), hence equality on F. E.2.3 was expanded to record explicitly that
this restriction-of-place obstruction descends even when places of L above
one F-embedding are not separated. For real quadratic fields, pass to a
totally real cubic compositum of degree6 and descend its real test.

For the concrete cubic theta^3-4theta+1=0, theta is the largest root; take
R=Z[theta,i] and b=theta-1. The type signs in ascending-root order are
(-,-,+). In the basis1,theta,theta^2,i,i theta,i theta^2 the Riemann matrix
is [[0,2T],[-2T,0]], T=[[-3,8,-11],[8,-11,35],[-11,35,-52]]. Its determinant
is3664^2, and all Rosati identities are exact and program-checked. The type
traces are -i and2i theta. Projective algebraic equations of the Qbar model
have not been numerically computed; the finite algebraic model follows
from the opened CM descent theorem.

Independent elliptic-agent audit passed this sign calculation and exact
field recovery. Parent was notified before inclusion.

## 6. Next attempted gate after E.2.5

The field Q(alpha), alpha^4-alpha-1=0, has two real embeddings and one
complex place. Mod2 the polynomial is irreducible; its discriminant is
-283. The cubic resolvent x^3+4x-1 has no rational root, so its Galois action
on the three pair partitions is transitive. The nonsquare discriminant
then gives S4. This field is neither totally real nor a subfield of an
elliptic ring class field; S4 has no abelian subgroup of index<=2, whereas
every quotient of a generalized-dihedral group has one. The same polynomial
calculations are in verify_numberfield_descent.py. This scope observation
is not a nonexistence result for other separating diagrams.

The active next approach is an actual non-CM integral isogeny diagram, or
a proved bridge from its automorphism to relative geometric monodromy in
Ayoub's full category. No extra conclusion has yet been obtained.


### 6.1 Exact quartic tower, primary source checked at 06:08--06:10 UTC

Serre, *On a theorem of Jordan*, Bulletin AMS 40 (2003), 429--440,
Notes 5.4, printed438/PDFp10, was opened in the original author article:
https://www.math.mcgill.ca/goren/SeminarOnCohomology/Serre.pdf
(web references turn461627906view0, turn829087065view0). The source states:
for L the splitting field of x^4-x-1, Gal(L/Q)=S4, the fixed field
H=L^{V4} is the Hilbert class field of K=Q(sqrt(-283)), and h(K)=3.
It further records Tate's quadratic extension
Ltilde=L(sqrt(4-7alpha^2)), where alpha is any root, unramified over L;
L/K is unramified as well. The group Gal(Ltilde/Q) is GL2(F3), and
Gal(Ltilde/K)=SL2(F3). The stated maximal-unramified-extension result is
attributed there to Martinet; that latter proof has not been opened and is
not used here. Serre's formulas and source attribution are recorded only;
no motivic integral lift follows from these finite Galois groups alone.

The cubic-resolvent test in E.2.4 forces any global integral transporter
with Artin image sigma to restrict to 1 or the actual c on H. Thus its
image in S4 is in V4 union c V4, an order-eight subgroup. Choose c=(12),
so roots3,4 are real. The residual element (12)(34) exchanges those two
real roots. The reduction therefore does not already separate the quartic
places. This is a direct computation of the exact surviving subgroup,
not an assertion that a surviving element lifts to the full diagram.

### 6.2 A proved comparison for quadratic twists of the CM test curve

Let E/H be any elliptic curve, let d_1,...,d_r in H^*, and put
L'=H(sqrt(d_1),...,sqrt(d_r)). For sigma in Gal(L'/H), take the standard
quadratic-twist isomorphisms phi_d:E^d_{L'} -> E_{L'}. They satisfy
phi_d^sigma=[chi_d(sigma)] phi_d, where chi_d(sigma)=+1 or -1 and
chi_{dd'}=chi_d chi_{d'}. Fix an embedding u of L' and put u'=u sigma.
For H1, identify the two H-defined base curves E_u and E_{u'} literally;
take T_E=identity. Identify each twisted H-defined curve likewise and set
T_{E^d}=chi_d(sigma) identity. Then
(phi_d)_{u'} T_{E^d}=chi_d(sigma)(phi_d)_u chi_d(sigma)=(phi_d)_u=T_E(phi_d)_u.
Every T is integral and preserves its polarization because its scalar
squares to1. Labelled endomorphisms inherited from E commute with these
signs. On tensor products use tensor products of the signs; multiplicativity
of the characters verifies all twist-product identifications and evaluations.
This gives an explicit integral tensor comparison on the diagram generated
by E, these quadratic twists, their twisting isomorphisms, endomorphisms,
polarizations, tensor constructions and direct summands with labelled
projectors. After identifying each object through the phi_d, every such
labelled morphism has exactly the source/target character covariance that
this formula cancels. Thus these twists do not distinguish sigma.

This applies to the proposed V4 twist route using the H-defined CM curve.
It does not rule out larger diagrams involving other abelian varieties or
isogeny classes. No assertion of an integral comparison on the entire
motivic category is made.

### 6.3 Additional exact obstruction in the Ayoub/Legendre route

The monodromy map from the profinite fundamental group of the three-punctured
line to the congruence closure of its integral Legendre representation is a
quotient map. Recovering the discrete congruence subgroup as the intersection
of that closure with SL2(Z) does not provide an inverse of this quotient.
In particular, an action identified only on the Tate-module quotient is not
yet an action identified on all finite etale covers. Applying the faithful
Galois action on the full geometric fundamental group at that point would
require proving compatibility on the quotient kernel as well. The attempted
proof has not supplied this map. Ayoub's full mixed geometric-local-system
construction gives a different, larger action, but an integral lift of the
pure comparison to that construction remains to be built.


## 7. Proved global CM comparison and the residual quartic (06:17 UTC)

This result supplies a global integral map, not merely an adelic matrix.
Let Qcm be the compositum, inside the fixed Qbar in C, of all CM number
fields, and put Fcm=the compositum of K^ab for all such CM fields K.
Both fields are normal over Q; Qcm is contained in Fcm. Also Fcm/Qcm is
abelian, because each K^ab Qcm/Qcm is abelian and a compositum of abelian
Galois extensions is abelian.

**CM-1.** Every sigma in Gal(Qbar/Fcm) induces a canonical natural integral
Betti comparison between a CM abelian variety A/Qbar and its conjugate
sigma A, simultaneously for all such A, their products, duals, Tate objects,
Artin objects and algebraic correspondences on these products.

**Proof.** Choose a CM algebra E acting on A and its CM type Phi. Its reflex
field E* is a CM field, including when E is a CM algebra; this is Milne
CM2020 Proposition1.18, printed14. Hence sigma fixes E*ab. In Milne's main
CM theorem, Theorem9.10 printed78, take the finite idele s=1. The theorem
gives a unique E-linear quasi-isogeny alpha_A:A -> sigma A such that
  T_f(alpha_A) = sigma : V_f(A) -> V_f(sigma A).
Here the equality is the theorem's exact formula
alpha_A(N_Phi(s)x)=sigma x with N_Phi(1)=1. Since a Galois automorphism
carries integral Tate lattices bijectively to integral Tate lattices, this
quasi-isogeny and its inverse preserve every integral Tate lattice.

To upgrade the quasi-isogeny to an actual algebraic isomorphism, write
alpha_A=f/m with f:A -> sigma A an actual morphism and m a positive integer.
For every prime l dividing m, f(T_lA) is contained in m T_l(sigma A).
Reduction modulo l^{v_l(m)} says that f kills A[l^{v_l(m)}]. Thus f kills
A[m], so the quotient property of [m]:A -> A gives an actual morphism
alpha_0 with f=alpha_0 [m]. Equality in Hom(A,sigma A) tensor Q gives
alpha_0=alpha_A. Apply the same reasoning to alpha_A^{-1}. Therefore
alpha_A is an actual isomorphism of abelian varieties, and its Betti action
is an integral lattice isomorphism. This argument verifies the precise
passage from the adelic identity supplied by CM theory to the global map.

The map is independent of the chosen CM algebra: a homomorphism of abelian
varieties is determined by its action on one rational Tate module, so all
choices give the same alpha_A. For any homomorphism f:A -> B,
  (sigma f) alpha_A = alpha_B f,
because both maps have the same Tate-module action. The same uniqueness
shows alpha_{A x B}=alpha_A x alpha_B, and gives compatibility with duality.
The field Qab is contained in Fcm (adjoin an imaginary quadratic field K;
K Qab/K is abelian), so sigma fixes all roots of unity. Hence the Weil
pairings and the one Tate object are fixed; equivalently Remark9.11(c)
gives polarization multiplier chi_cyc(sigma)/N_{E*/Q}(1)=1. Every labelled
polarization is preserved.

For an algebraic correspondence Z between products of CM abelian varieties,
its etale cycle class is carried by sigma to the class of sigma Z. The
alpha maps have exactly this action on H1_et, hence on all its exterior
powers, Kunneth products and Tate twists. Therefore the induced maps on
Betti cohomology commute with the correspondence Z and its conjugate:
this can be checked after tensoring with Q_l, and the comparison map is
injective on rational cohomology. Integral cohomology of an abelian variety
is the exterior algebra of its integral H1 lattice and has no torsion;
all integral correspondence maps are therefore respected integrally. The
cohomological comparison is inverse pullback (alpha_A^{-1})^*; the
homological comparison is (alpha_A)_*. On finite etale schemes use the
permutation of geometric points induced by sigma. Kunneth then supplies
the product comparisons with Artin objects, and compatible projectors
restrict these comparisons to every included direct summand and assigned
intersection lattice. This proves the claimed global integral tensor
comparison on this concrete CM-abelian/Artin diagram. It makes no assertion
about an integral realization of an arbitrary Q-linear category.

**CM-2.** Let L/Q be the splitting field of x^4-x-1, K=Q(sqrt(-283)),
and H=L^{V4}. Then L intersect Fcm = H. Consequently, for the quartic
field k=Q(alpha) with alpha one of the real roots, its two distinct real
embeddings have isomorphic integral Betti functors on the entire diagram
in CM-1.

**Proof.** Complex conjugation c is central on Qcm. Indeed, on each CM
field E it is the unique nontrivial automorphism over the totally real
subfield, and for any embedding r:E -> C one has c r = r c_E. This proves
centrality on the compositum of all conjugates and hence on Qcm. The field
L intersect Qcm is Galois over Q, so it corresponds to a quotient of S4
in which the image of the actual c is central. Here c is a transposition.
The normal subgroup generated by commutators [g,c], g in S4, is A4: these
commutators are even, and suitable products of two distinct transpositions
give 3-cycles, whose conjugates generate A4. Thus the quotient has order
at most2. Since K is an imaginary quadratic field contained in L and Qcm,
  L intersect Qcm = K.
It follows that Gal(L Qcm/Qcm)=A4. As Fcm/Qcm is abelian, the intersection
(L Qcm) intersect Fcm corresponds to an abelian quotient of A4, and hence
is contained in (L Qcm)^{V4}=H Qcm. Intersecting back with L gives
L intersect Fcm contained in H. Conversely H is the Hilbert class field
of K (Serre, Notes5.4 p438), so H is contained in K^ab and Fcm. Equality
follows.

The restriction map Gal(Qbar/Fcm) -> Gal(L/H)=V4 is therefore surjective:
a chosen automorphism of L fixing H extends first to L Fcm by the identity
on Fcm, then to the algebraic closure. Label the roots so c=(12) and
roots3,4 are real. Choose sigma with restriction (12)(34). If alpha=root3,
then u:k -> C is its given inclusion and w=sigma|_k sends alpha to root4.
Both embeddings are real and distinct, hence give distinct complex places.
For every CM abelian variety over k, apply CM-1 after u and use
sigma(uA)=wA; all maps defined over k satisfy the naturality just proved.
This supplies a global integral tensor isomorphism of the two restricted
Betti functors. In fact the maps are algebraic isomorphisms on the CM
abelian generators and preserve their polarizations, so their induced
Hodge structures are respected as well.

The conclusion concerns the full stated CM-abelian/Artin diagram. The same
sigma has not been lifted to the Betti functor on all pure motives, and this
proof does not assert such a lift. It proves by explicit natural maps that
adding further CM isogenies, CM types, or CM twists cannot decide the
remaining quartic test for the full category.

**Source/check record.** MilneCM2020 PDF at
work/sources_generation/milne_cm2020.pdf, Proposition1.18 p14 and
Theorem9.10 with Remark9.11 p78 read locally, then reopened through the web
at turn492735190view0/1, 06:16UTC. The full proof of Theorem9.10 pp78--80
was read; it identifies the idelic class using ray class groups and the
closed norm-one torus quotient, so choosing s=1 uses the theorem exactly.
Elliptic-agent independent field/morphism audit passed at06:17UTC; its
independent check of the exact source normalization also passed. The result
was integrated as E.2.6 after the parent reserved that identifier.


## 8. Real-Frobenius scope correction, E.2.7

The parent correctly required that geometric real-Frobenius be distinguished from scalar extension to R. For the quartic, S=Spec k(sqrt(alpha)) has identity Frobenius on H0 at the positive real root and a transposition at the negative root, traces2 and0. The E.2.6 global plain/Hodge comparison therefore cannot intertwine these additional involutions. E.2.7 now proves separation of all real embeddings using r1-1 rational thresholds q_j between ordered real values of a primitive element theta and S_j=Spec k[t]/(t^2-(theta-q_j)). The trace test is exact and finite; it leaves the plain full-category gate unchanged.
