# Dictionary of conventions

## Symmetric-group lattices

`Lat_A(G)` is the exact category of finite free A-modules with a G-action; all short exact sequences with three such terms are allowed. The sequence splits over A, not necessarily over A[G]. `R(A)` uses induction between symmetric groups for multiplication. `rho_n` is the degree-n trivial representation, and `rho_lambda` the corresponding Young permutation lattice. `Phi_A` sends complete symmetric generators to these classes. Characteristic zero means the unital map Z→A is injective. The zero ring is excluded.

The split Green ring uses direct-sum relations only. The split quadratic ring similarly uses orthogonal-sum relations only. Neither is the exact representation group or the metabolic Grothendieck–Witt quotient. Integer coefficients in these Grothendieck groups are never reduced modulo the coefficient-field characteristic.

## Finite-field isogeny classes

A model over F_(p^e) means an abelian variety whose base change to the algebraic closure is isogenous to the given variety. The model need not have the original Frobenius in the geometric center. The degree of a central division algebra is the square root of its dimension over its center. In the quadratic-center proposition, `d` is this degree, `t` the order of a prime ideal class, and `h_K` the full class number.

## Tori in apposition

Groups are connected simple adjoint groups over C. Apposition pairs are ordered. Classes of quadruples are taken under simultaneous inner conjugation. A regular semisimple group element has a torus as the identity component of its centralizer; the full centralizer can be disconnected. Naturality under isomorphisms is a condition on inner-conjugacy classes and equals outer invariance. It does not mean a quadruple fixed by every inner automorphism.

## Records

`NGQ-*` are provisional package locators, not permanent workbench tags. WB numbers and permanent statement tags are assigned only when filing in the central registry. No commit or deposited version is asserted. Independent re-proof means a statement-only reconstruction before access to the corresponding internal proof, and is distinct from a targeted proof check. All current independent checks use separate instances of the same GPT-6 Astra model; no human verification is claimed.

## New positive coefficient mechanism: rational nil ideals

For a scheme Spec(A) supported on a nil thickening Spec(A/I), a uniquely divisible ideal I permits division by each finite group order inside all representation-lifting defects. The explicit group-cohomology averaging in Theorem6.1 lifts both objects and exact relations, so every equivariant lattice K0, and hence the symmetric induction lambda construction, is unchanged. The ideal may be nil without being nilpotent. The square-zero ring Z_(p)⊕Qε is a positive noncoherent example. This concerns the coefficient-ring question explicitly present on cote133; it does not assert ordinary nil-invariance for arbitrary lattice categories.

## CM arithmetic of a central finite-field Frobenius

For a geometrically simple class with CM geometric center K, the Newton slopes first determine a fractional-valuation denominator a and integral ideal I. The ideal-class order t makes I^t principal; a residual totally positive unit has order s≤2 modulo unit norms. Exactly the multiples of ats are central-Frobenius model exponents. Thus the arithmetic obstruction separates into integral valuations, a class-group obstruction, and a norm obstruction. For commutative geometric endomorphisms centrality is automatic. This refines the finite-field isogeny question connected to cote15, without claiming that a realization-level motive comparison gives algebraic mixed cycles.

## Correspondences versus Frobenius realization

A homological target built from powers of one suitable abelian variety may have the same graded Frobenius realization as an ordinary K3 surface or cubic fourfold. The exact missing statement is surjectivity of specified mixed cycle maps. Theorem7 on mixed correspondences proves the equivalence using target Tate fullness, rational duality pairings, and prime-independent rational traces. It leaves those mixed cycles unconstructed for general varieties. Explicit Kummer and separated-cubic Chow retractions supply them for those families.

## Infinite torsion invisible on the generic fibre

Over Spec(Z_(2)[epsilon]/epsilon²), the exact equivariant K0 already has a split direct sum of infinitely many Z/2 classes for S2. The ideal epsilonA is torsion-free over Z but not uniquely divisible. Its canonical square-zero extension defines an odd boundary on Tate cohomology; primary lengths for the square of that boundary are additive modulo2. Companion matrices realize all simple finite-length F2[t,t^-1]-modules. The explicit relative resolution proves each displayed class has order2. These classes vanish after reduction to the DVR and after inverting2, so generic ranks, traces, and generic Picard groups do not see them. This supplies an additional exact K-theoretic obstruction to the coefficient-ring classification on cote133. It does not classify the whole kernel.

## Exact square-zero coefficient classification

For every scheme Spec(A) that is a square-zero extension of Spec(Z_(p)), the extension has a canonical coefficient section and is an idealization Z_(p)⊕M. Its symmetric-group induction ring is polynomial exactly when M is uniquely divisible, equivalently a Q-vector space. This is a necessary-and-sufficient coefficient criterion inside the local-ring problem on cote133. A torsion-free nondivisible direction is separated by a map M→Z_p; any torsion direction is separated by a map M→Q/Z_(p). The latter produces a split countable free subgroup of the degree-p reduction kernel, even when the ideal is divisible. Thus divisibility and unique divisibility have different K-theoretic consequences. The proof consists of the two canonical extension boundaries, their sign cancellation, and integer primary Euler characteristics.

## Singular arithmetic curves and normal surfaces

Every nonmaximal quadratic Z_2-order has an infinite split sum of Z/2 in its ordinary-character kernel; the maximal order, a DVR, is positive. The residual homology operators satisfy a two-by-two matrix-algebra relation, so half-length parity survives exact sequences. This classifies that family of singular arithmetic curves. Separately, two-dimensional normal local domains over every residue prime fail generation through a nontrivial generic eigenline of exact Picard order two. They can be complete, and dimension two is minimal for noetherian normal counterexamples. These results distinguish arithmetic singularities invisible to generic characters from generic line-bundle obstructions. They do not characterize every singular local base.

## Ramification and higher nilpotent thickness

Flat dual numbers over every characteristic-zero DVR of residue characteristic two still have infinite split two-torsion: an intermediate integral involution has length-one Tate groups even when O/2 has even length. Odd-degree F2 companion polynomials make the detector uniform over arbitrary residue fields. Every even truncation Z_(p)[e]/e^(2m) fails by finite free restriction to the dual-number subring epsilon=e^m; asymmetric matrix entries e and e^(2m−1) preserve one-dimensional Tate boundaries. Odd truncations remain an explicit gate.

## Uniform torsion and Adams operations

The flat dual thickening Spec(O[epsilon]/epsilon²) over O=Z_(p) or Z_p carries an infinite split elementary-two subgroup in degree p of exact equivariant K0. The coefficient prime p does not control this torsion order: an explicit admissible sequence proves order two for every p. More generally, the rank-p cyclic family over the n-th thickening has successive classes x_j=j*x_1 and n*x_1=0. Odd n remains a nonvanishing gate. Exterior powers kill the exhibited two-torsion under psi², whereas a group automorphism cannot do so. Thus the integral lambda operations contain information lost by ordinary characters; this is directly within cote133's lambda-ring and induction-ring question.

## Even ramification in the cubic examples

The dual numbers over the integer rings of Q_3(zeta_3) and Q_3(sqrt3) have a split countable degree-three two-torsion subgroup. A self-matrix-factorization produces an exact coefficient extension with one-dimensional Tate groups; scalar changes in unramified extensions separate normalizer-twisted eigenvalues. An independent proof instead uses a triangular constant rank-two cyclic lattice and its third character. These are negative square-zero thickenings of regular arithmetic curves, not counterexamples over the DVR itself.

## Odd-prime ramification criterion

For a complete arithmetic DVR O with finite residue field of odd characteristic p, an absolute ramification index e satisfying v2(e)<=v2(p−1) gives a negative flat square-zero thickening. A tame coefficient extension makes the cyclotomic distance e/gcd(e,p−1) odd. Tate primary composition length, rather than the underlying residue-field dimension, survives coefficient restriction and detects a split countable two-torsion subgroup. The cubic examples are special cases. The complementary even-distance range remains open; failure of this detector is not positivity.

## Arbitrary residue fields and finite coefficient algebras

The odd-prime ramification theorem now applies to every arithmetic DVR O with v2(v_O(p))<=v2(p-1), without completeness or finiteness/perfection of the residue field. A finite free cyclotomic coefficient algebra replaces an unavailable Hensel lift, and an endomorphism selects one residue factor. Composition length over O[U] detects an odd cyclotomic distance. This strictly removes the former incomplete/infinite-residue subcase from the cote133 coefficient problem. The complementary ramification range remains unresolved.

## Three-torsion on a cubic infinitesimal neighbourhood

Over Spec(O[e]/e³), for O=Z_(p) or Z_p, degree-p exact equivariant K0 has a split countably infinite direct sum of Z/3 killed by both reduction and generic specialization. The first coefficient boundary is a differential; its third-order curvature annihilates its homology. Nonzero curvature-primary pieces are acyclic, and the difference of the two boundary ranks is additive modulo3. A second proof constructs the same curvature from two canonical coefficient extensions. Explicit asymmetric cyclic deformations and an admissible exact relation prove exact order3. Thus higher infinitesimal neighbourhoods have torsion that is invisible to ordinary characters and is not governed by the residue prime. For C2 the smallest example also has x²=0 and psi³x=0!=x, despite3 being a coefficient unit. This resolves the cubic coefficient test within cote133 without a claim about every nilpotent thickness.

## Quadratic arithmetic curves at every prime

For every p, among Z_p-orders in quadratic fields, precisely the maximal orders satisfy polynomial induction generation. Every nonmaximal order has an infinite split two-torsion subgroup killed by normalization. At odd primes the homotopy for multiplication by p and two canonical coefficient boundaries force even primary lengths, including lengths of connecting images, so half-length parity is additive. The explicit cyclic family gives the nonzero classes. This extends the previous residue-two classification to all quadratic arithmetic orders in fields, while degree at least3 remains unresolved.

## Transfer to all thicknesses divisible by three

The finite free map O[epsilon]/epsilon³ -> O[e]/e^(3m), epsilon=e^m, transfers the cubic obstruction through an asymmetric cyclic lattice. Its reduced Tate groups are one-dimensional, and the exact identities (T−1)v0=epsilon²v1 and N(T)v1=epsilon v0 give cubic curvature1. Together with the even-thickness result this refutes generation for every length divisible by2 or3. The displayed class is killed by the length; its exact order at composite lengths is not determined here. The next coefficient test is length5.

## Localized quadratic orders without completeness

The odd-prime quadratic construction extends from Z_p to Z_(p). A monic lift of a finite-field irreducible gives a finite local DVR, and choosing alpha first makes kappa=d/(1−alpha^p) an explicitly verified unit with prescribed residual inverse. No Hensel root is needed. Every nonmaximal finite order in a quadratic number field is thereby a negative local coefficient ring. The maximal order can be semilocal at a split prime; the complete-base classification is not incorrectly extended to that semilocal ring.

## Every principal infinitesimal thickness

For O=Z_(p) or Z_p and every n>=2, the degree-p reduction kernel over Spec(O[e]/e^n) contains a split countably infinite direct sum of Z/n, invisible on the generic fibre. The cyclic deformation has exact order n. Curvature is canonical modulo maps through regular lattices; its nonzero primary components have an exact Tate complex, and their invariant lattice has an additive covolume modulo n. This closes the previously unresolved odd-thickness gate, including n=5. It does not classify arbitrary nilpotent extensions. The explicit C2 class has x²=0 and Adams value k*x for odd k, zero for even k.

## Even binomial arithmetic rings

At odd primes every O[t]/(t^(2m)-d), d in p²O, is negative. Restriction to the quadratic subring s=t^m detects independent parity coordinates. The explicit classes are killed by2m; if m is odd their multiples by m form a split countable two-torsion sum. Exact order2m is not claimed in general. The quartic domain t^4=27 at3 gives a concrete higher-degree order beyond the quadratic classification.

## Ramification and principal thickness

For any mixed-characteristic DVR with h=v(p), the curvature covolume has value h*r modulo n on the standard witness. Hence n not dividing h gives failure in degree p, and gcd(n,h)=1 gives split countable Z/n. Coarse prime-field primary components remove all residue-field restrictions; completion is used only to define detectors. This does not settle n dividing h, nor determine the exact class order when n and h have a common factor.

## Monogenic arithmetic orders with a nontrivial generic residue extension

For A=Z_p[t]/F, F monic and F modp=t^N, assume the generic quotient is a field of residue degree f>1. In the proved constant-term range (valuation at least2 for odd p, at least3 at2), degree-p generic specialization has a kernel mapping onto countable Z/f, and every Young class maps to zero. The generic field norm makes determinant valuations well-defined modulo f. Curvature-primary Tate acyclicity makes the invariant lattice exact, and the companion witness has invariant ideal(p,t), of colength equal to its coefficient-parameter degree. This gives singular arithmetic curves in odd degrees, including every scaled unramified cubic order. These are quotient invariants; exact torsion and a splitting are not asserted. Endpoint and noncomplete extensions are recorded as pending until their check events close.

## The boundary of the current ramified parity method

For O[epsilon]/epsilon² in odd residue characteristic, all current nonzero-primary composition-length parity detectors vanish when v2(v_O(p))>v2(p−1). A curvature-unit lattice becomes an exact one-periodic free O[C_p]-module; hypersurface periodicity and a commuting square root reduce it to a genuine symmetric matrix factorization. Its specialized homology parity factors through the G0 of a double-cover arithmetic surface; prime filtrations and point valuations force evenness. Separating only the separable part of residue factors preserves the required parity normalization for arbitrary residue fields. This eliminates a whole detector family, but gives neither polynomial generation nor a complete description of the reduction kernel.

## Congruent arithmetic bases and every deep monogenic thickening

NGQ-A133-038 identifies exact lattice K0 for a fixed finite group over two finite flat Z_p-algebras agreeing modulo p^r, when r exceeds twice the p-valuation of the group order. Geometrically, these finite arithmetic schemes have indistinguishable sufficiently thick closed fibres for this fixed-group invariant. The isomorphism-class correction is performed inside upper triangular matrix algebras, so it preserves all admissible exact relations. This is the bridge from Maranda-type rigidity to the coefficient question in cote133; it does not assert an equivalence on Hom modules or a fixed-modulus comparison in every symmetric degree.

NGQ-A133-039/040 transfer the exact order-n obstruction from Spec(Z_p[t]/t^n) to every monic equation congruent to t^n modulo p³; explicit binomial formulas also work over Z_(p). The generic representation group is torsion-free, so these transferred classes lie in the generic kernel. The finite flat arithmetic scheme can have a totally ramified field generic fibre: generic characters therefore do not account for all integral lattice classes. A split retraction, not merely a quotient, proves the countable direct summand.

The endpoint forms of NGQ-A133-032/035 include residue characteristic two and the localized integer base. The monogenic norm modulus is the residue degree and requires no additional constant-term hypothesis. NGQ-A133-036 now has a full independent arbitrary-rank proof: every current nonzero-primary parity detector vanishes in the complementary odd-ramification range, while the coefficient-generation problem itself remains open.

## Completion and cubic arithmetic fibres

NGQ-A133-041 compares integral lattice K0 over a finite flat arithmetic scheme over Spec Z_(p) with its p-adic completion. Completion is injective on the entire exact group and identifies the subgroup lost on inverting p. The proof algebraizes lattices after adding an explicit coefficient-free syzygy to make the generic group-algebra module regular; H1 descends exact relations and Weibel cofinality preserves them. Thus formal split torsion in the generic kernel gives actual split torsion over the localized integers. NGQ-A133-039 consequently includes every monic F≡t^n modulo p³ over both bases, beyond binomials. No equivalence of full morphism categories is asserted.

NGQ-A133-042 gives the depth-p² cubic obstruction by signed lengths of an acyclic coefficient-boundary complex. Odd-prime Bockstein/homotopy projection and characteristic-two Artin–Schreier primary decomposition both make the signed lengths additive modulo3 on every exact Tate cycle. An explicit split exact mesh gives exact order3. NGQ-A133-043 restricts a binomial arithmetic scheme of degree3m to its cubic subring: the witness decomposes into one cubic block and m−1 regular blocks. This narrows the remaining totally ramified monogenic gate to equations outside the established depth and exponent criteria. Full author and targeted checks are complete; the separate unhinted cubic nonvanishing reconstruction remains pending.

## All binomial arithmetic thickenings at depth p²

NGQ-A133-044 concerns the finite flat arithmetic scheme Spec(O[t]/(t^n-d)), d in p²O, at every exponent and every prime. Its exact lattice K0 has countably many split order-n classes invisible on the rational generic fiber and outside the symmetric-group Young span. The stable-module proof uses the mod-p truncated coefficient algebra and a mod-p² Bockstein to orient a stable length modulo n. The independently reconstructed geometric proof passes through the generic hypersurface of the complete intersection O[C_p] tensor O[t]/(t^n-d), takes a formal root section, and evaluates supported singularity classes by length modulo n. The supported invariant is constructed before taking K0, so it respects idempotent completion. An explicit coefficient-split mesh supplies the exact annihilator relation. This strengthens the even/cubic/deep-binomial findings without changing Grothendieck's cote133 question or attributing the later invariants to his manuscript.

## Every mixed-characteristic trait has a negative flat square-zero thickening

NGQ-A133-046 closes the complementary odd-ramification row. If Spec(O) is any characteristic-zero trait with odd residue characteristic p, its flat first-order thickening Spec(O[epsilon]/epsilon²) has an exact-order-two class of symmetric-group lattices invisible both on the reduced trait and on the generic thickening. A class-group-valued additive invariant detects it while annihilating every Young permutation lattice. The coefficient-free exact category remembers a nonprincipal divisor on the auxiliary normal surface y²=(1+x)^p−1; its divisor class survives although all previously used Tate length parities vanish in the complementary range. The explicit coefficient-split relation proves two-annihilation, rather than reading a torsion order off a quotient. The separate categorical proof specializes a supported formal disc to the singularity category of the same type of surface. With the residue-two theorem, failure holds over every mixed-characteristic DVR. This concerns Grothendieck's lattice-generation question on cote133 scans28–29, not a claim that his other representation constructions fail. A split two-torsion summand in the unrestricted odd-ramification case is not proved.

## Monic depth two and arbitrary-DVR truncations — 2026-11-23T21:57:00.545065+00:00

NGQ-A133-049 concerns finite flat local schemes Spec(O[t]/F) over Spec(O) whose equation reduces to a principal nilpotent thickening modulo p². Their degree-p lattice K0 contains a split countable direct sum of exact order-n generic classes, killed by passage to the characteristic-zero generic fibre and detected outside the induction span of trivial symmetric-group representations. The proof constructs natural stable coefficient operators on the full exact category, then formal deformations of companion matrices whose coefficient-split meshes prove n-annihilation. It answers a further family in cote133, scan29; no analogous claim is attributed to another cote.

NGQ-A133-047 removes the ramification restriction for truncation exponents prime to the residue characteristic. A normal surface divisor class of exact order n and a supported singularity functor detect the finite explicit lattice mesh. Finite flat restriction and extension detect the prime-to-p part of every exponent. No split summand is inferred for arbitrary DVRs. The remaining principal-truncation question is therefore limited to pure p-power exponents dividing the absolute ramification index, apart from already settled exponent two.

## One shallow coefficient at odd primes — 2026-11-23T21:59:15.517688+00:00

NGQ-A133-048 excludes the finite flat local orders defined by t^n+pb t^(n−1)+p²H. The whole degree-p lattice Grothendieck group maps to a countable sum of Z/n, killing the Young span and mapping the generic kernel onto it. A palindromic chain of coefficient lifts gives a stable Bockstein proof; an independent generic-hypersurface root correction gives a length-one detector. The cubic Z3[t]/(t³+3t²+9) is a proper index3 order in a totally ramified cubic field and gives an explicit shallow wild example. This narrows the cote133 coefficient-ring question to lower shallow coefficients and other unresolved rings; no split torsion is inferred here.

## Distinguished monic coefficient schemes and pure-power limitations — 2026-11-23T22:37:04.861955+00:00

NGQ-A133-051 classifies polynomial generation for Spec(O[t]/F) with O=Z_p or Z_(p) and F modp=t^n: it holds exactly for regular members. For singular members, the first valuation-one nonconstant coefficient determines N=min(n,pr), and the coefficient-free equivariant K0 has a whole-group retract onto countable Z/N outside the Young span, with section supported in the generic specialization kernel. This gives an obstruction over a finite flat singular scheme over the arithmetic base, not an ordinary-character obstruction. If the completed generic scheme is a single field point, valuation invariance forces N=n. The proof uses a finite-support generic-hypersurface category, regular root sections and supported length modulo N, with exact lattice meshes establishing actual annihilation. Its separate unexposed re-proof gives finite polynomial source formulas over both bases. NGQ-A133-050 is the r=n−1 case and NGQ-A133-049 is r=infinity. Cote133 is the direct archive connection; no motive or weight statement is inferred.

NGQ-A133-052 proves that a standard nilpotent lattice mesh vanishes in exact K0 for two ramified pure-power schemes. Finite normalizations furnish an exact module self-map with residue O; fully faithful stable-category reflection turns this into a lattice K0 relation. Replacing the unit gives a normal surface with torsion divisor class, but no full-category specialization has been established. These findings narrow which witnesses can work, not the class of positive coefficient rings.

## Every principal truncation over a mixed-characteristic DVR — 2026-11-23T22:43:08.289521+00:00

NGQ-A133-053 resolves the remaining pure-power generation family, and indeed every exponent divisible by p, through a different integral lattice. On the finite flat nilpotent scheme Spec(O[t]/t^n), write n=pr. A coefficient-free lattice obtained from a uniformizer ideal has curvature−1 and invariant ideal(pi,t^r); its primary equivariant K0 covolume is r modulo n. This value is nonzero independently of ramification. It vanishes on all induction monomials in trivial symmetric-group classes, but is attained by a class vanishing on both the reduced coefficient scheme and the generic fiber. Combined with047, every nontrivial principal truncation over every mixed-characteristic DVR is negative. The detector value has orderp; source torsion order and splitting are not established. The earlier052 zero meshes remain zero and do not conflict, since their integral lattices differ. This is a direct cote133 result, with no assertion about motives or weights.

## Curvilinear special fibre and vertical ideal (IDs054–056)

A curvilinear special fibre here means an Artinian local A/pA whose maximal ideal is principal, equivalently embedding dimension at most1. Its length n is over its own residue field; it is not the absolute Z_p-rank when that residue field has degree greater than1. The Cohen coefficient DVR has uniformizer p even for an imperfect residue field. The vertical class for n=ps is [(pi,X+t^s)]−[A[C_p]]; it has exact order p and has a whole-group retraction when v_p(n)=1. This differs from the standard mesh M_i and from a mere nonzero detector value.

## Completion and primary relations (IDs057–059)

Completion of a finite free coefficient algebra over any characteristic-zero DVR preserves the generic-specialization kernel and injects the full lattice K0. Every whole-group splitting supported in the completed kernel lifts. A principal p-special fibre therefore gives a regularity criterion for finite-free local coefficient rings over any DVR; p is the rational prime, not an arbitrary uniformizer. The Cohen coefficient DVR can differ from the original base, which permits inseparable residue extensions in the unramified monogenic clause. For n=ps and h=v_pi(p), the two exact ideal meshes give h*y=s*z. This distinguishes vanishing of a standard matrix family from non-generation of the coefficient ring, and distinguishes a nonzero order-p class from a direct summand. If n=p^k*m and p∤hm, m*z has exact split order p^k, with y its bottom order-p subgroup. The full generic kernel is not classified.
