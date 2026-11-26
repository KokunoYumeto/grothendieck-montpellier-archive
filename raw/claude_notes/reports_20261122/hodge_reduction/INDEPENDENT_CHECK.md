# Check of the reduction of the Hodge conjecture for abelian varieties to bounded cycle degrees

By Claude Opus 5.5 at effort high (agent a8d753525905811ab), for the main session (Claude Opus 5.5 at effort max),
22 November 2026.

## 0. This check is not blind

I didn't write the statement, and for this check I opened neither the seed, the bridge files, the HODGE_DIVISION returns
nor their intakes. But I had read two of the bridge files earlier, in the same agent:

- `HODGE_BRIDGE_SKETCH_20261121.md`, whole (21 Nov, 00:41 UTC);
- `HODGE_DIVISION_ATTACK_20261121.md`: its headings, lines 131–200 and 405–460 (21 Nov, about 12:03 and 12:32 UTC);
- on 22 Nov at 17:58 UTC, minutes before this task, single lines of the same file from a grep. One states a bound of the
  shape N ≤ (deg Z⁺ + deg Z⁻)/(d!·√V·h). Others say that every Hodge class lies on a Mumford–Tate special subvariety,
  and mention a dichotomy by André–Oort;
- the statements C44-W02 and W03 of C44_POS (a detector bound in characteristic p), read for that run's intake.

So the bound in Lemma C and the covering in Lemma B can't count as blind rediscoveries. The proofs below were written
from the statement and checked step by step, with nothing looked up in those files. **If the result needs a blind
check, it needs an agent who hasn't seen the bridge files.**

## 1. Verdicts

| Claim | Verdict | Point |
|---|---|---|
| (1) ⇒ (2) | **proved** | bounded at every complex point, by Baire over C |
| (2) ⇒ (1) | **proved** | the locus c_t ≤ D is closed; every Hodge class is covered up to isogeny |
| (1) ⇒ (3) | **proved, with repair R1; false as literally written** | R1: the map to A_(g,N) comes from a morphism of Shimura data |
| (3) ⇒ (2) | **proved, with R1** | one place outside a finite set, and one ℓ there, suffice for each x |
| (3) ⇒ (1) | **proved, even without R1** | only the families of Lemma B are used |
| Rider: any one dense set in (2) | **proved** | in each family, for any choice of the set |
| Rider: any prescribed infinite set of good places | **proved** | under (1) all but finitely many places work |
| Rider: only published inputs | **true** | section 5. No 032, no Tate conjecture, no absolute Hodge cycles, no André–Oort, no independence of ℓ |
| Novelty | not assessed | spreading out and Baire are standard |

With R1 the equivalence holds family by family: for a fixed (S,θ,t), boundedness on one dense set, condition (3), and
algebraicity of t_s at every point are equivalent.

## 2. The repaired statement

**R1, the map.** S is a connected component Γ\X⁺ of a Shimura variety at neat level, and S → A_(g,N) is induced by a
morphism of Shimura data into (GSp_2g, H^±). Then every CM point goes to a CM abelian variety, which has a model over a
number field. It is enough to assume that the chosen points x go to abelian varieties definable over Q̄.

*Why it is needed.* With "a map" read as any morphism, take S a modular curve and the constant map to a principally
polarized elliptic curve E with transcendental j, and t = θ. Then c_t = 1 everywhere. No CM point of S has a model over a
number field. If (3) asserts that there is one, (3) is false unconditionally, and "(1) ⇔ (3)" would assert that the
Hodge conjecture is false. If (3) is read as vacuous at such points, the global equivalence survives through Lemma B,
but the equivalence for the single family doesn't follow.

**R2, conventions (no change of substance).**
- "Effective integral cycle" means an effective cycle with integer coefficients, possibly 0 or reducible.
  deg_θ Z = ∫_Z θ^(g−p).
- A model of x is (A,θ) over a number field L, an embedding L → C and an isomorphism with (A_x,θ_x). For a place v,
  choose v̄ on Q̄ above v. The reduction of t_x is its image under the specialization isomorphism at v̄. It needn't be
  fixed by Galois. "Some v̄" and "every v̄" give equivalent conditions.
- In (3), D is uniform in x. The set of places, v̄, ℓ, M and the cycles may depend on x, and all but the first may
  depend on v.

**Theorem.** Let (S,θ,t) satisfy R1 and put d = g−p. The following are equivalent.
- (a) t_s is algebraic for every s in S(C).
- (b) c_t is bounded on S(C).
- (c) c_t is bounded on some Zariski-dense subset of S(C).
- (d) There is D such that for every CM point x and every model there are infinitely many good places v at which, for
  some ℓ_v prime to v, the reduction of t_x in H^2p(Q_ℓ_v(p)) is (cl Z⁺ − cl Z⁻)/M, with both degrees at most D and any
  integer M ≥ 1.
- (e) The same, with the places taken in any prescribed infinite set of good places.
- (f) There is D such that for every such x and model this holds at all but finitely many places, for every ℓ prime to v,
  with M ≤ D too.

In (d)–(f) the CM points may be replaced by any dense set of points whose abelian varieties are definable over Q̄, and
"every model" by "some model". The rational Hodge conjecture for all complex abelian varieties is equivalent to (a) for
all these families.

## 3. Attempts to refute

| Attack | Result |
|---|---|
| Non-principal polarization | Harmless over C: every abelian variety is isogenous to a principally polarized one, and algebraicity of a rational class is invariant under isogeny. |
| A not defined over a number field | Harmless: it is a point of a special family over C, and the bound on CM points passes to it by closedness. Only the points tested in (3) need models (R1). |
| A Hodge class outside every family | None exists (Lemma B). At level N ≥ 3 the multiplier of Γ is 1, so the twist has no monodromy. |
| ℓ varies with v; independence of ℓ in characteristic p | Never used. At a non-exceptional place the cycles lift to cycles in characteristic 0, where the comparison with Betti cohomology gives the equality for every ℓ. One ℓ at one such place is enough. |
| M unbounded | Impossible: M²q_t ≤ binom(2d,d)(deg Z⁺ + deg Z⁻)², with q_t > 0 constant on S (Lemma C). M isn't needed to identify the class either. |
| Vertical components | Real, and the reason for asking for infinitely many places. A cycle on a vertical component needn't lift. For a given (x,D) these components lie over finitely many places, which are discarded. I don't claim that one arbitrary place suffices. |
| Reduced cycles don't specialize to reduced schemes | Harmless: use fundamental cycles of points of Hilbert schemes, with the trace map of SGA 4 XVIII 2.9. Embedded components of lower dimension don't contribute. |
| Descent from C to Q̄ | The class is constant on connected components of the Hilbert scheme over Q̄, and each has a Q̄-point, with the same degrees. |
| Galois orbit of t_x | Harmless: at a good place inertia acts trivially, and the argument works for any choice of v̄. |
| Baire over countable fields | It fails there and isn't used there. It is applied only to S(C). Finiteness of c_t at every CM point, or at every Q̄-point, doesn't give boundedness: a countable set is a union of countably many closed points. |
| D depending on x | Then (3) says only that each t_x is algebraic. It doesn't give (1) by this argument. The uniformity is the whole content of the reduction. |
| CM points not dense, or S a point | They are dense (Lemma B). When S is a point everything is trivial. |

## 4. Proof

Throughout, (S,θ,t) is a family, f: A → S, and d = g−p. Cohomology classes of cycles of dimension d lie in degree 2p
with twist p. The variety S is irreducible and quasi-projective (Baily–Borel), and the map to A_(g,N) is algebraic
(Borel).

### Lemma A. Bounded cycles form a projective scheme with locally constant classes

Let T be a noetherian scheme and (A,θ) a principally polarized abelian scheme over T. Pulling the Poincaré bundle back
by (1,θ) gives a relatively ample line bundle of class 2θ. Its cube O(1) is relatively very ample, and its degree on
cycles of dimension d is 6^d deg_θ. Every integral subvariety of a geometric fibre has deg_θ a positive integer.

By SGA 6 XIII 6.11(i), an integral subscheme of dimension d and O(1)-degree at most 6^d D over an algebraically closed
field has its Hilbert polynomial in a finite set depending only on (g,d,D). Let H_D be the disjoint union, over
the finite tuples (P_1,…,P_a; Q_1,…,Q_b) of such polynomials with each of the two degree sums at most 6^d D, of the
fibre products over T of the Hilb^(P_i) and Hilb^(Q_j) of A/T. It is projective over T (FGA 221). Sending a point to
the fundamental d-cycles of its subschemes shows that its geometric points give exactly the pairs (Z⁺,Z⁻) of effective
cycles with deg_θ ≤ D. Conversely, write a cycle as a sum of integral subvarieties, repeated by multiplicity. There
are at most D of them on each side.

Let ℓ be invertible on an open part of T, and work over it. For the universal subscheme Z over a component of H_D,
which is flat with fibres of dimension at most d, the composite

  R^2d f_* Q_ℓ(d) → R^2d (f|Z)_* Q_ℓ(d) → Q_ℓ

with the trace (SGA 4 XVIII 2.9, limit over Z/ℓ^n) commutes with base change and is, on each geometric fibre, the
functional of the fundamental cycle. By Poincaré duality it is a section γ^± of the lisse sheaf R^2p f_* Q_ℓ(p) on H_D.
Its value at a point is the class of the cycle. Two sections of a lisse sheaf agree on a set that is open and closed.

**Consequence over T = S ⊗ C.** For each integer 1 ≤ M ≤ D the locus of H_D where γ⁺ − γ⁻ = M t is open and closed,
hence proper over S. So S_D = {s : c_t(s) ≤ D} is Zariski closed.

### Proposition 1. (a) ⇒ (b), (c) ⇒ (a), and trivially (b) ⇒ (c)

- (a) ⇒ (b): a rational combination of cycles gives some M, Z⁺, Z⁻, so S(C) is the union of the S_D, D in N. An
  irreducible complex variety isn't a countable union of proper closed subvarieties, so some S_D = S.
- (c) ⇒ (a): if c_t ≤ D on a dense set then S_D is closed and dense, hence S.

This uses no property of S beyond being an irreducible variety. It proves the rider on dense sets.

### Lemma B. Every Hodge class lies in a special family, and CM points are dense

Let t₀ ≠ 0 be a Hodge class of codimension p on A₀. Choose an isogeny φ: B → A₀ with B principally polarized
(Mumford, §23). As φ_*φ* = deg φ, it is enough that φ*t₀ be algebraic. So assume that A₀ = B has a principal
polarization ψ.

Put V = H₁(B,Q), let h be its Hodge structure, G its Mumford–Tate group in GSp(V,ψ), ν the multiplier, and X the
G(R)-conjugacy class of h. (G,X) is a Shimura datum: the types on Lie G are (−1,1), (0,0), (1,−1), the polarization
gives the Cartan involution, and G^ad has no Q-factor on which h is trivial, by minimality of G. It maps to
(GSp, H^±). The tensor t₀ in ∧^2p V^∨ ⊗ ν^p is fixed by G, so it has type (p,p) at every h′ in X.

Choose a level N ≥ 3 on H₁(B,Z), a neat K in G(A_f) mapping into K(N), and let S = Γ\X⁺ be the component of [h,1]. An
element γ of Γ has ν(γ) a positive rational unit, so ν(γ) = 1, and γ fixes t₀. Thus t₀ is a global section t, and S is
smooth, connected, with a map to A_(g,N) through which the point of B passes.

CM points are dense in X⁺ for every Shimura datum. Any h′ factors through a maximal torus of G_R. A rational element of
Lie G close to a regular element of its Lie algebra has as centralizer a maximal Q-torus, conjugate over R to that
torus by some u near 1. Then u h′ u⁻¹ is a CM point near h′. Under R1 its abelian variety is CM, hence defined over a
number field.

Therefore (2) ⇒ (1): apply Proposition 1 to this family. And (1) ⇒ (2) by Proposition 1 in any family.

### Lemma C. The multiplier is bounded by the degrees

On A×A let θ₁, θ₂ be the pullbacks of θ, μ and δ the pullbacks by (a,b) ↦ a+b and a−b, and P = μ − θ₁ − θ₂. Put
m = 2d and q_t = |∫_(A_s×A_s) (t_s × t_s) P^m|.

**q_t is a positive constant.** It is constant, all classes being flat. Let x in ∧^m H₁(A_s,R) be Poincaré dual to
t_s, E the Riemann form and J the complex structure. Cup product with P^m gives, up to a sign depending only on (g,p),
q_t = m! |(∧^m E)(x,x)|. As x has type (−d,−d), Jx = x, so (∧^m E)(x,x) = (∧^m G)(x,x), where G(u,w) = E(u,Jw) is
positive definite. So q_t = m! |x|² > 0.

**The bound.** Let Z, Z′ be effective d-cycles. Then μ + δ = 2(θ₁+θ₂), P = (μ−δ)/2, and μ, δ are nef. Expanding P^m and
bounding each term by the positive one,

  |∫_(Z×Z′) P^m| ≤ ∫_(Z×Z′) (θ₁+θ₂)^m = binom(2d,d) deg Z deg Z′.

Thus M t = cl Z⁺ − cl Z⁻ implies

  M² q_t ≤ binom(2d,d) (deg Z⁺ + deg Z⁻)²,  equivalently  M |x| ≤ (deg Z⁺ + deg Z⁻)/d!.

With both degrees at most D, M ≤ D₁ := 2D (binom(2d,d)/q_t)^(1/2), independently of s and ℓ. The same inequality holds
verbatim on a smooth reduction.

### Proposition 2. Suppose (d) at one point x, with constant D. Then c_t(x) ≤ max(D,D₁)

Let (A,θ) be the model over L. Choose n so that it extends to a principally polarized abelian scheme over
R = O_L[1/n], and form H_D over R. It has finitely many irreducible components. Those not dominating Spec R lie over a
finite set E of places. Take one of the given places v outside E and the places dividing n, with v̄, ℓ, M and the pair
z in H_D(k(v̄)), so that γ⁺(z) − γ⁻(z) = M·sp(t_x).

Let W be an irreducible component through z, with reduced structure. It dominates R, hence is flat. So after base
change to the strict henselization of R at v̄, the point z is the specialization of a point η of the generic fibre, by
going down. Two embeddings of Q̄ compatible with this differ by inertia, which acts trivially on H^2p(A_Q̄,Q_ℓ(p)).
The sections γ^± are compatible with specialization, so M·sp(t_x) = sp(γ⁺(η) − γ⁻(η)). Specialization is an
isomorphism (SGA 4 XVI 2.2), so M t_x = γ⁺(η) − γ⁻(η).

The connected component of η in H_D over Q̄ has a Q̄-point, with the same classes and degrees. After embedding Q̄ in C
this is an equation in Betti cohomology, because H^2p(Q) → H^2p(Q_ℓ) is injective. So t_x = (cl Z⁺ − cl Z⁻)/M on A_x,
with degrees at most D, and M ≤ D₁ by Lemma C.

This proves (d) ⇒ (c), the CM points being dense. The proof used one place outside the finite set and one ℓ.

### Proposition 3. (b) ⇒ (f) ⇒ (e) ⇒ (d)

Let D bound c_t, take x, a model over L and cycles on A_x over C with M ≤ D and degrees ≤ D. Their point of H_D over Q̄
lies on a connected component with a Q̄-point having the same classes, so they may be taken over a finite extension L′
in Q̄. At each good place w of L′ properness extends this point of H_D to the valuation ring. The special point gives
effective cycles of the same degrees, and Lemma A gives the same classes for every ℓ prime to w. All but finitely many
places of L are covered, for every v̄ above them. This is (f).

(f) ⇒ (e), since an infinite set minus a finite one is infinite, and (e) ⇒ (d) by prescribing all good places.

### Conclusion

(1) ⇒ (2) by Proposition 1; (2) ⇒ (1) by Lemma B and Proposition 1; (2) ⇒ (3) by Propositions 1 and 3; (3) ⇒ (2) by
Proposition 2. Without R1, (3) for the families of Lemma B alone still gives (1), hence (2).

## 5. Inputs

| Input | Locator | Opened for this check? |
|---|---|---|
| Boundedness of integral subvarieties of bounded degree | Kleiman, SGA 6 XIII, Def. 6.9 and Cor. 6.11 | **opened**: statements and the short deduction of 6.11, in our transcription `sga_scan_check_20261105\sga6\current\main.tex` 16548–16567 |
| Trace map for flat morphisms, with base change | Deligne, SGA 4 XVIII Th. 2.9 | **opened**: statement, in `sga_scan_check_20261105\sga4\current\18\18.tex` 4123–4227; proof not read |
| Specialization in smooth proper cohomology | SGA 4 XVI Cor. 2.2 | **opened**: statement, `sga4\current\16` |
| Poincaré duality | SGA 4 XVIII 3.2.5 | not opened |
| Cycle class and comparison with Betti cohomology | SGA 4½, Cycle; SGA 4 XI 4.4 | not opened |
| Hilbert schemes | Grothendieck, FGA, exposé 221, Th. 3.2 | not opened |
| Principally polarized varieties up to isogeny; Lefschetz (3L very ample) | Mumford, *Abelian Varieties*, §23 Cor. 1 of Th. 4; §17 | not opened |
| Line bundle of class 2θ; fine moduli for N ≥ 3 | Mumford, *Geometric Invariant Theory*, 6.10, 7.9 | not opened |
| Shimura data | Deligne, *Variétés de Shimura*, Corvallis 1979, 2.1.1 | not opened |
| Algebraicity of S and of the map | Baily–Borel, Ann. of Math. 84 (1966), Th. 10.11; Borel, J. Diff. Geom. 6 (1972), Th. 3.10 | not opened |
| CM abelian varieties over number fields | Shimura–Taniyama; Shimura, *Abelian Varieties with Complex Multiplication and Modular Functions*, §12.4 | not opened |
| Intersection of nef classes with effective cycles | Kleiman, Ann. of Math. 84 (1966); Lazarsfeld, *Positivity* I, 1.4.9 | not opened |

The locators of the unopened works are from memory and must be verified before publication. Three searches by the
general terms of SGA 6, SGA 4 and Shimura varieties were made. The statement wasn't sent.

## 6. Computation

`check_a8d75352\poincare_form.py`, output `poincare_form.out`, beside this file. In exact integers, for every
(g,p) with g ≤ 4, on 56 random classes, it verifies |∫(t × Ct)P^m| = m!|t|² with a sign depending only on (g,p). It
also verifies the intersection bound on 625 pairs of elliptic curves in E×E. This tests Lemma C; it isn't a proof.

## 7. Check events

```
statement_id	date	who	type	outcome
HR (1)=>(2)	2026-11-22	Claude Opus 5.5 at effort high, agent a8d753525905811ab	independent re-proof	proved; not blind (section 0)
HR (2)=>(1)	2026-11-22	Claude Opus 5.5 at effort high, agent a8d753525905811ab	independent re-proof	proved; not blind (section 0)
HR (1)=>(3)	2026-11-22	Claude Opus 5.5 at effort high, agent a8d753525905811ab	refuted	as literally written (arbitrary map, existence of a model); refined statement HR (1)=>(3) with R1
HR (1)=>(3) with R1	2026-11-22	Claude Opus 5.5 at effort high, agent a8d753525905811ab	independent re-proof	proved; not blind (section 0)
HR (3)=>(2) with R1	2026-11-22	Claude Opus 5.5 at effort high, agent a8d753525905811ab	independent re-proof	proved; one non-exceptional place and one l suffice
HR (3)=>(1)	2026-11-22	Claude Opus 5.5 at effort high, agent a8d753525905811ab	independent re-proof	proved without R1
HR rider dense set	2026-11-22	Claude Opus 5.5 at effort high, agent a8d753525905811ab	independent re-proof	proved
HR rider places	2026-11-22	Claude Opus 5.5 at effort high, agent a8d753525905811ab	independent re-proof	proved
HR rider published inputs	2026-11-22	Claude Opus 5.5 at effort high, agent a8d753525905811ab	targeted proof check	true; three statements opened, the other inputs cited from memory
HR Lemma C	2026-11-22	Claude Opus 5.5 at effort high, agent a8d753525905811ab	computation or formal certificate	identity on 56 random classes for g<=4 and bound on 625 pairs PASS
```
