# H035.39: composition research record

The manuscript's two-scheme notion is prospective and not defined. The precise
affine question investigated here is closure, under composition, of additive
A-linear functors Mod(A)→Mod(A) satisfying Theorem 12(i), (iii a,b), (iv), (v),
(vi), with A a noetherian quotient of a regular ring. This reconstruction is
not substituted silently for the manuscript. The results ZIP was opened only after the full entry was frozen; it contains no result rows.

## Gate at 04:19 UTC, 19 November 2026

Only (iii a,b) remain. PROOFS.tex H035.39 proves the other axioms, including
a dense-open upgrade of (vi) that handles reducible quotients. For a finite
module M over a completion C, put V_n=G(M/I^nM), W=G(M)=lim V_n. The desired
comparison is F(W)→lim F(V_n). The hypotheses do not directly say W is finite
over C, nor do they directly identify {V_n} with {W/I^nW} in the pro-category.
Those are distinct issues; neither is asserted without proof.

## Positive local-completion lemma — proved 04:26 UTC

Let R be a countable noetherian local ring, C its maximal-ideal completion,
and G an additive R-linear functor preserving filtered colimits, finite on
finite R-modules, and satisfying the manuscript's comparison for every finite
C-module. Then **G(M) is finite over C for every finite C-module M**, and
{G(M/m^nM)} is pro-isomorphic to {G(M)/m^nG(M)}.

Proof. V_n=G(M/m^nM) is a finite-length R-module, killed by m^n. W=lim V_n
has its complete metrizable inverse-limit topology. The C-action on M induces
one on G(M); the comparison identifies it with the coordinatewise C-action
on the limit. For each finite R-module N, the module Hom_R(N,M) is finite over
C, because N has a finite presentation and C is noetherian. The evaluation
map Hom_R(N,M)⊗_R G(N)→W has finite C-module source. It is continuous: m^n
times its source maps to zero in V_n. A finite module over a complete
noetherian local ring is linearly compact in its m-adic topology, so its
continuous image in the Hausdorff linearly topologized W is closed.

Here the elementary linear-compactness fact can be checked directly: reduce
a family of closed affine cosets with the finite-intersection property modulo
m^r. Each finite-length quotient has the descending-chain condition, hence
a nonempty stable intersection. Their compatible intersections lift through
the surjective transition maps; completeness gives a point of all the original
closed cosets. This also proves that a continuous image is closed, by applying
the same argument to inverse images of neighbourhood cosets of a point in its
closure.

There are only countably many isomorphism classes of finite R-modules, since
each is the cokernel of a finite matrix over R. Enumerate them as N_i.
Finitarity says that every element of W comes from G(N) for some finite
submodule N⊂M. Thus W is the union of the increasing finite sums E_r of the
evaluation images for N_1,…,N_r. Each E_r is a closed finite C-submodule.
Baire's theorem for a complete metric space makes one E_r have nonempty
interior. Being a subgroup, it is open, so it contains the kernel of W→V_n
for some n. W/E_r is a subquotient of the finite-length module V_n. Both
E_r and W/E_r are finite over C, hence W is finite over C.

Each V_n is artinian, so the inverse system is Mittag–Leffler. Replace it by
its stable-image system U_n; this is a pro-isomorphism and U_{n+1}→U_n is
surjective. The limit W surjects onto each U_n. Let K_n be its kernels.
They contain m^nW and have zero intersection. Chevalley's lemma makes K_n
cofinal with the m-adic filtration of the finite complete module W.

For clarity, that use of Chevalley has a short proof here. For each r the
images (K_n+m^rW)/m^rW eventually stabilize, since W/m^rW has finite length.
If the stabilized image were nonzero for some r, these stable images form a
surjective inverse system and lift to a nonzero element of W in the closure
of every K_n. Each K_n is closed by Artin–Rees, giving an element of their
zero intersection, a contradiction. Thus K_n⊂m^rW for sufficiently large n.
It follows that {U_n}, and hence {V_n}, is pro-isomorphic to {W/m^nW}.

If F also satisfies the completion axiom, apply F levelwise to this
pro-isomorphism and take limits. Because W is finite over C, its axiom gives
F(W)=lim F(W/m^nW)=lim F(V_n). This proves the composition comparison (iii a)
for countable A, after replacing A by its countable localization A_p.

This proof uses countability of the finite-module isomorphism classes, not
countability of the underlying set of M or of the residue-field completion.
It does not extend the conclusion to arbitrary uncountable A by assertion.

## Algebraizable completed modules and Dedekind domains

The finiteness part above holds without countability if M is a direct summand
of C⊗_R N for a finite R-module N. Additive finitary functors commute with
flat scalar extension by Lazard, so G(C⊗N)=C⊗G(N) is finite; a summand is
finite too. If the completion ideal has artinian quotient, the stable-image
and Chevalley argument then proves the same pro-isomorphism and composition
comparison. Chevalley applies to a complete semilocal ring as well, by its
finite product decomposition, or by the identical finite-length proof.

Consequently the whole affine composition assertion holds over a Dedekind
domain. At a nonzero prime, the completed ring is a complete DVR and every
finite module is a sum of a free module and cyclic power-torsion modules;
these are algebraizable. At the zero prime the completion is the field itself.
For any nonzero nonunit a, the (a)-adic completion is the finite product of
the completed DVRs at primes dividing (a). A finite module over this product
is a direct summand of the completion of a finite A-module: use a sufficiently
large free summand, cyclic A/p^n summands, and the finitely many product
idempotents. The ideal has artinian quotient, so the preceding argument
applies. For a=0 the tower is constant, and for a a unit the completion is
zero. The other axioms were already proved in PROOFS.tex H035.39.

The same elementary constant-tower observation proves the assertion over an
artinian ring: every relevant local or principal completion is an idempotent
factor, and every finite completed module is already a finite A-module.

## Approaches tried and their precise limitations

1. **Replace the class by Auslander coherent functors.** This is insufficient.
   Coherent functors with a finite Hom presentation are closed under
   composition, by the abelian property of the coherent-functor category and
   a finite presentation of the outer functor. But the manuscript's axioms
   do not state such a presentation. Jaffe's proper underived-cohomology
   example and Hall's explicit derived/underived distinction make the
   substitution especially unsafe. No equality of the classes was proved.

2. **Apply F's completion axiom directly to G(M).** Invalid until G(M) is
   proved finite over the completed ring. Finiteness of G on finite A-modules
   alone says nothing immediate about a nonalgebraizable finite C-module.
   The countable lemma above resolves this only for maximal-ideal completion.

3. **Assume any finite inverse system is Mittag–Leffler.** False for principal
   completion with positive-dimensional residue ring. Finite modules there
   are not artinian. Maps given by successive multiplication by y provide
   the basic descending-image obstruction. The formal-functions lemma for
   cohomology has extra content, not a purely formal consequence of finiteness.

4. **Assume a zero-intersection descending filtration on a finite complete
   module is cofinal with an arbitrary principal-adic filtration.** False.
   In C=k[[x,y]], K_n=(x^n,y^n) has intersection zero and C=lim C/K_n,
   but K_n is never contained in (x). This does not itself yield a functor
   counterexample; it identifies a missing inference in a proposed proof.

5. **A natural-looking counterexample functor.** Over k[[x,y]], let
   T(M)=Σ_{n≥1} y^n M[x^n] and G(M)=M/T(M). This is additive and finitary,
   and finite on finite modules. It gives G(A)=A and
   G(A/x^n)=A/(x,y)^n, illustrating the noncofinal filtrations above.
   However it fails the original hypotheses at p=(x): y becomes invertible,
   T becomes x-power torsion, and on the completed DVR G(C)=C while
   G(C/x^n)=0. It is therefore rejected as a counterexample.

6. **Sums of torsion/socle or simple functors.** The elementary infinite
   torsion functor already fails completion on a free completed module.
   Direct sums of simple functors supported on finite indecomposables tend
   either to fail completion on those modules or to have only finitely many
   surviving summands on a finite completed module. No qualifying pair was
   produced. These attempts are not evidence for the full theorem.

7. **Flat base change alone.** It handles C⊗N and its summands, but a finite
   C-module can have formal relation coefficients that do not descend to A.
   The basic remaining test is A=k[x,y]_(x,y), C=k[[x,y]], with modules such
   as C/(y−h(x)) for a transcendental formal series h; principal completion
   also has nonartinian levels. No algebraization assumption is in the page.

8. **Matlis/linearly compact reformulation.** Maximal-ideal completion turns
   the outputs into a linearly compact limit of finite-length modules. The
   countable union of finite evaluation images yields the Baire argument
   above. For an uncountable base the same union is not countable; Baire
   cannot be invoked. No unsupported general boundedness assertion is used.

## Historical next attacks at 04:26 UTC (superseded by (A)–(F))

First determine whether (iii a) at every prime forces the nonartinian
principal-completion tower to be adic in the pro-category. The failed functor
in item 5 shows why the all-primes condition could be decisive. In parallel
within this single stream, look for a pointwise finite, finitary functor whose
formal output is infinite over an uncountable base, or a theorem forcing its
finiteness. Search exact hypotheses, not only the term “coherent functor.”


## 2026-11-19T05:05:53.995075+00:00 — Countable-base closure and a smaller general gate

PROOFS.tex, H035.39 arguments (A)–(D), now give a full countable-base proof. Exact inverse limits of finite modules over complete local rings follow from Matlis biduality. A finite inverse system is pro-zero if its limit vanishes after every completed localization: stabilize its support and test a generic point. Those facts prove the formal pro-comparison whenever the completed output is finite. All finite evaluation images are closed even for a nonartinian principal-adic tower, by testing closure at every completed maximal localization. Countability plus Baire then makes the output finite. No Mittag–Leffler assertion is made for a nonartinian tower.

The strongest remaining sufficient gate for arbitrary bases is completed-output finite generation. Baire does not handle the uncountable cover. Earlier attempts that stopped at nonartinian continuity are superseded by this argument. A failure of this sufficient finiteness property would not alone be a counterexample to composition.


## 2026-11-19T05:29:26.930813+00:00 — Maximal completions and residue-field values

Arguments (E)–(F) in PROOFS.tex remove the separate global principal-output issue. Finite local-completed outputs imply principal-output finiteness: countably many lifts of generators of the finite projection images become generators after every completed localization; Chevalley and Nakayama make their span the entire limit, then Baire makes that countably generated complete module finite. The general finite-output gate is equivalent to its local residue-field-valued subcase. For H=G/mG, exact inverse limits prove the maximal axiom, and its principal axiom follows by scalar extension to the maximal completion; rank and generic parameter conditions are automatic. Intrinsic maximal-adic completeness of G(M) makes finite output equivalent to finite-dimensional H(M). This is a reduction of the sufficient gate, not a claimed equivalence between failure of finiteness and failure of composition.


## 2026-11-19T05:49:43.454951+00:00 — Further local attacks; no additional gate reduction

1. **Countable descent.** A finite formal presentation uses only countably many
   coefficients, but the given functor need not descend to a countable subring
   with finite values there. Restriction or scalar extension also has not been
   shown to preserve the required completed-module comparisons. A countable
   coefficient description of M is therefore not a countable cover of H(M)
   by the evaluation images required by Baire. No descent theorem is claimed.

2. **Countably many evaluation types for a fixed M.** It would suffice to find
   a countable collection of finite R-modules whose evaluation images span
   H(M). Truncating the formal relation matrix does not produce actual maps
   from those approximations to M. The needed factorization, even modulo m
   on Hom, has not been established. Mittag–Leffler-module theorems found in
   Datta–Epstein–Tucker concern additional purity/flatness properties; their
   complete-base equivalences do not establish this assertion over R.

3. **Matlis-dual tensor targets.** For finite D-module T and its Matlis dual
   E_T, the functor N↦soc(N⊗_R E_T) is finitary and has finite-dimensional
   values on finite R-modules. It also has finite-dimensional values on finite
   D-modules: duality identifies those values with the vector-space dual of
   Hom_D(N,T)/m Hom_D(N,T). Hence it cannot provide an infinite-output example.
   More seriously, it need not satisfy completion. Take R=k[t]_(t),
   D=k[[t]], T=D and E_T=k((t))/k[[t]]. Then D⊗_R E_T=E_T and its socle is k,
   whereas (D/t^n)⊗_R E_T=0 since E_T is t-divisible. The proposed completion
   comparison is k→0. This is a rejected candidate, with the failed axiom
   explicit, not a counterexample to the manuscript.

4. **Formal coefficient annihilators.** Functors built from the kernel of a
   formal coefficient acting on N⊗_R D have finite values on finite R-modules
   after suitable reductions. On a formal input their expression involves
   D⊗_R D, not just D. The canonical completion comparison has not been
   verified. This candidate remains only an attempted construction; no
   calculation is claimed to disprove or establish its full axioms.

5. **Half-exact finiteness theorems.** Hall–Rydh (2019), Theorems 3.3 and 3.7
   and Remark 3.8, pp.767–768, require half-exactness. Their reported Flenner
   completion injection starts with a finite module over the original base.
   Neither point supplies the missing arbitrary additive-functor conclusion
   on a nonalgebraizable finite D-module. Ogus's primary lecture-note proof
   of the half-exact Nakayama lemma, Theorem 2, pp.1–2, confirms exactly where
   half-exactness is used. Flenner's original paper was not opened and is
   not cited as a checked theorem certificate.

6. **Direct composition without finite output.** There is a useful boundary
   check: an inner functor whose values are all k-vector spaces cannot itself
   create a completion counterexample. The restriction of any additive
   finitary outer F to Vect(k) is F(k)⊗_k−. Since F(k) is finite-dimensional,
   it commutes with inverse limits. Thus F(H(M))→lim F(H(M/m^nM)) is an
   isomorphism whenever the corresponding comparison for H is one, even if
   H(M) were infinite-dimensional. This confirms why the finite-output gate
   is sufficient rather than equivalent to composition. It is a side case,
   not a new reduction of the current general gate.

7. **Endomorphism finiteness and pure injectivity.** A finite D-module is
   finite over its endomorphism ring, and its linear compactness suggests
   pure-injective methods. Preservation of these finiteness properties by
   an arbitrary bounded finitary additive functor has not been proved.
   Results for finitely presented interpretation functors would reintroduce
   the stronger coherent-functor assumption. No such substitution is made.

The current gate remains exactly the local residue-field finite-output
question recorded at 05:29. The next substantive attacks are a direct
comparison for the outer functor on the linearly compact inner output, and
an explicit bounded noncoherent functor built from finite-module categories.
Both must retain the completed-module quantifier, not merely algebraizable
inputs.
