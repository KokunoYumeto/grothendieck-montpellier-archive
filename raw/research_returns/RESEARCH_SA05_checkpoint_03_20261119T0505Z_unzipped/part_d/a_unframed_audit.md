# Independent audit: framed versus unframed adelic realizations in A.3(c)

Date: 2026-11-19. Author: GPT-6 Astra (OpenAI, ChatGPT Pro mode), Part D agent.

## Conclusion and exact scope

The finite-support square-class counterexample in `A:enrichment` refutes classification of **framed** local neutralizations by the bare H-gerbe class. It does not refute classification of unframed coherent realization systems with their prescribed Artin restrictions. Under that latter, precise interpretation the equivalence class of the realization system is unique. This distinction should appear explicitly in the theorem statement, not only in its last paragraph.

Use the bands already proved in Part A:

\[
 H=P_0\times\mu_2\longrightarrow P=P_0\times\mathbb G_m
 \longrightarrow G,\qquad G/P=A=\widehat{\mathbb Z}.
\]

The word coherent must mean a genuine object over the prime-to-p finite adele ring, or the equivalent compatible integral tensor system. Merely having an object independently at every prime and an Artin isomorphism independently at every prime is not the same assertion. The Artin restriction is prescribed **up to isomorphism as an adelic tensor functor**, and no choice of that isomorphism is retained in the unframed object.

At p the relevant full-G object is the ordinary Qp-valued functor obtained by forgetting the crystalline Frobenius over Fp. Its Artin restriction is the unramified algebra-valued functor; relative to F0 its torsor is the specific eta_p of `A:eta`. We compare only full-G objects whose Artin restrictions have that same isomorphism class. At the real place use a fixed-band realization morphism from the real realization gerbe, not an R-valued fibre functor, since the latter does not exist.

## Exact primary source checked

J. S. Milne, *Gerbes and abelian motives*, version 1.1, 21 February 2003:

- Proposition 3.6, p.25: `lim^1 P^K(Q) -> lim^1 P^K(A)` is an isomorphism.
- Proposition 3.10, equations (29) and (31), p.25: these groups identify canonically with H1(Q,P) and H1(A,P), respectively.
- Proposition 3.12, p.26: P(Q)=Q^times.
- Section 6.2, p.36: the precise coherent local data are a prime-to-p adelic object, an xp-morphism from the crystalline realization gerbe, and an x-infinity-morphism from the real realization gerbe.
- Theorem 6.3 and its proof, pp.36–37: local triples form an H1(A,P)-torsor; global equivalences form an H1(Q,P)-torsor; the displayed isomorphism proves uniqueness of the system's equivalence class, and uniqueness of a P-equivalence up to a 2-isomorphism with residual Q^times.
- Remark 6.4, p.37: the weight-zero version has no residual rational-point ambiguity.

Primary URL: <https://www.jmilne.org/math/articles/2003b.pdf>.
Reopened web reference: `turn288595131view1`.
Local source: `../sources/Milne_2003_Gerbes.txt`; entire relevant statements and proof read.

## Torsor proof for full G, including the ordinary p-adic functor

Let x and x' be two objects of a commutative G-gerbe over a local coefficient field k. Their isomorphism sheaf D=Isom(x,x') is a G-torsor. Its pushout to A is the isomorphism torsor of their Artin restrictions. If those restrictions are isomorphic, then

\[
 [D]\in\ker\bigl(H^1(k,G)\longrightarrow H^1(k,A)\bigr).
\]

Exactness of the torsor sequence for `1 -> P -> G -> A -> 1` therefore gives a class d in H1(k,P) mapping to [D]. The lift is not claimed canonical: choosing an isomorphism of the Artin restrictions gives a P-reduction of D, and changing that isomorphism changes this reduction by the usual boundary action of A(k). Only existence of one lift is needed.

This applies at p as soon as both crystalline Artin restrictions represent eta_p, regardless of the fact that the rigidified P-gerbe itself is not neutral over Qp. The compared objects are objects of the neutral **full G-gerbe**. In particular, the argument does not incorrectly put a Qp-valued fibre functor on the isocrystal category over the algebraic closure of Fp.

The identical torsor argument works for two morphisms from a fixed source gerbe with fixed band homomorphism: the stack of such morphisms is acted on simply transitively by target-band torsors once a base morphism exists. This is the morphism classification reviewed by Milne in Section 5 and used in Theorem 6.3. At the real place the image in H1(R,A) is automatically zero because continuous homomorphisms from Gal(C/R) to the torsion-free profinite group Zhat are zero. The crystalline source after geometric base change has the same prescribed band morphism xp; its P-level version is exactly the one in Section 6.2.

Apply the same argument to the genuine adelic object away from p, choosing one adelic isomorphism of the Artin restrictions. Together with the single p-adic and real differences, this produces a class

\[
 d_{\mathbb A}\in H^1(\mathbb A,P).
\]

Here the adelic cohomology is Milne's continuous protorus cohomology, with the finite product decomposition into the prime-to-p finite adeles, Qp, and R. No replacement by an unrestricted product of unrelated local cohomology groups is made.

Propositions 3.6 and 3.10 give a unique class d_Q in H1(Q,P) localizing to d_A. Finally,

\[
 H^1(\mathbb Q,H)=H^1(\mathbb Q,P_0)\times
   \mathbb Q^\times/\mathbb Q^{\times2}
 \longrightarrow H^1(\mathbb Q,P)=H^1(\mathbb Q,P_0)
\]

is surjective, by Hilbert 90 for the Gm factor. Thus d_Q lifts to a global H-torsor, whose band-preserving equivalence preserves the original Artin–Tate rigidification and carries one unframed realization system to the other. The grading and augmentation are preserved because the band diagram is fixed.

This proves transitivity on the **equivalence classes of systems**. It does not assert a unique H-equivalence: different mu2 lifts remain possible. The residual Q^times statement in Theorem 6.3 applies to the P-system and must not silently be substituted for the automorphism group of the more rigid H-system.

## Why the explicit counterexample disappears upon forgetting the frames

The local square-class twist lies in H1(k,mu2). Its image under `mu2 -> Gm` is zero by Hilbert 90, hence its image in H1(k,P), and then H1(k,G), is zero. Thus the two full local G-functors are isomorphic after forgetting the Tate comparison frame. A non-globalizable family of square classes can still prevent these isomorphisms from respecting all retained local frames. The two conclusions are compatible.

## Limits of the positive statement

1. Arbitrary full-G local functors without their prescribed Artin isomorphism classes are not covered: their difference can have nonzero image in H1(k,Zhat).
2. An arbitrary product of local objects is not automatically a coherent adelic object.
3. At p the ordinary functor over Fp and the nonneutral geometric isocrystal gerbe are distinct objects and have been kept distinct.
4. The statement proves existence of a compatible equivalence, not uniqueness of a framed equivalence or a canonical choice of comparison isomorphisms.

## Final audit of the integrated proposition

The integrated `A:unframed-adelic` proposition and its proof in
`sections/part_a.tex` were read after insertion. The torsor lift, the
ordinary crystalline functor at p, the global H-to-P surjectivity, and
the claimed scope of uniqueness all pass the independent audit.

The real morphism step is valid for a specific descent reason. For two
morphisms of gerbes with the same homomorphism of commutative bands,
the local isomorphism sheaf is acted on by the target band. Automorphisms
of a source object act on both morphisms through the same band map;
their two actions cancel on the isomorphism sheaf. Consequently that
sheaf descends from the source gerbe to the coefficient field as a
G-torsor. Its class maps to zero in H1(R,Zhat), and the same exact torsor
sequence gives a P-lift. No R-valued object of the nonneutral motivic
gerbe is introduced in this argument.

One wording refinement was sent to the root: the proposition should
explicitly require that the **adelic** Artin restriction is isomorphic
to F0 tensored with A_f^p, since pointwise local isomorphism classes
alone do not supply the adelic reduction used in the proof. The proof
already states the required adelic comparison.
