# SA18: research packages (concepts) (sweep 3, wave 1)

Merged by Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, sweep 3 wave 1 (merge) from the readers' files in readings/. Each section is the reader's text, unchanged.

## From readings/c45_c56.md (Research packages (concepts))

- **R1. Rigidity of Chevalley Lie algebras in small characteristic.**
  - Question: for each simple root system Φ and prime p, and for the adjoint and simply connected Chevalley Lie
    algebras 𝔤 over F_p, decide whether H^i(𝔤, 𝔤) = 0 for i = 0, 1, 2. Decide whether Aut^0_{Z[1/N]}(𝔤_Z) is the adjoint
    Chevalley group scheme exactly over the primes where these vanish.
  - Why: his 45:38 programme ("cela suffirait à construire les Tchevalley sur Z") and his 45:40 question.
  - Rests on: 45:37-42 and 45:18-26; item SA18-1.
  - Strongest reduction: on the page, (1)+(2)+(3) ⇒ Aut^0 smooth and equal to G. In this reading, dim H^1(pgl_2, pgl_2)
    = 3 in characteristic 2, so the construction fails there.
  - Material: the pages; Chevalley bases; a computer algebra computation of Der and H^2 for rank ≤ 4 and p ≤ 7;
    Hogeweij, Hiss, Strade.
- **R2. Fourier identities over a base.**
  - Question: for an abelian scheme A/S of relative dimension g over a smooth base S over a field (characteristic 0, then
    p), prove or refute ψ_D(ab) = (-1)^g ψ_D(a) * ψ_D(b) in CH(Â)_Q with no Todd factor. Equivalently, decide whether
    Todd(H^1_dR(A/S)) = 1 in CH_Q(S).
  - Why: the corrected box of 47:11, and the base-change form of Beauville's identities used in motivic decompositions.
  - Rests on: 47:3-11; `sweep2/REPORTS/cote47_scan009_chi_factor.md`; SA18-13, SA18-14, SA07.
  - Strongest reduction: this reading reduces it to Todd(H^1_dR) = 1. Characteristic 0 follows from Esnault-Viehweg
    (2002). Characteristic p is open to me (van der Geer).
  - Material: cote 47 and 54 transcriptions; Mukai (1981), Beauville (1983), Deninger-Murre (1991), Esnault-Viehweg
    (2002), van der Geer (1999).
- **R3. Infinitesimal kernels over fields of dimension ≤ 1.**
  - Question: let k have characteristic p with Br(K') = 0 for all finite separable K'/k (e.g. F̄_p(t)). Prove or refute
    that H^1_fppf(k, G) → H^1_fppf(k, G/K) is onto for every affine algebraic G and infinitesimal normal K, and that every
    nonabelian H^2 class of an algebraic lien over k is neutral.
  - Why: Lemma 4 of 45:8-9 and case (ii) of 45:14 rest on a false Frattini step. The rest of his theorems stands.
  - Rests on: 45:2-17; SA18-2, SA18-6.
  - Strongest reduction: by his Lemmas 3 and 5 and the commutator dévissage, to K of height one with perfect restricted
    Lie algebra, e.g. Frobenius kernels of semisimple groups and their twisted forms.
  - Material: the pages; Giraud, Cohomologie non abélienne; Springer (1966); Demazure-Gabriel; results on fppf
    cohomology of infinitesimal groups over imperfect fields.
- **R4. The abelian subscheme of Pic in mixed and positive characteristic.**
  - Question: for f: X → S smooth projective with geometrically connected fibres over a reduced locally noetherian S,
    prove or refute that there is a unique abelian subscheme A ⊂ Pic_{X/S} with |A| = ∪_s |Pic^0(X_s)|.
  - Why: proved on 51:19-22 only in residue characteristic 0 ("Sinon, il faut regarder de plus près").
  - Rests on: 51:17-22 and 49:3-10; SA18-17.
  - Strongest reduction: on the page, to the triviality of the finite p-group kernel of A → P over a DVR.
  - Material: the cote 49 and 51 transcriptions; FGA VI; Kleiman, The Picard scheme (§9.5); Igusa's example.
- **R5. Purity for good reduction.**
  - Question: decide his 51:23 d) for torsors under abelian schemes over regular S: is the set of points where P_K has
    good reduction the complement of a pure codimension-one closed set? Decide also the underlying purity statement for
    abelian schemes, separately in the cases where it is known and where counterexamples exist.
  - Why: his question "Analogue th. de pureté pour la bonne réduction des schémas abéliens?". It links SA15 (p-divisible
    groups, Néron models).
  - Rests on: 51:23, 51:9-12; SA15-19.
  - Strongest reduction: c) on the page, H^1(S, G) ⊂ H^1(K, G) for regular S (Weil extension). Known for abelian schemes
    in mixed characteristic with e ≤ p - 1 (Vasiu-Zink 2010, from memory).
  - Material: the pages; `sweep3/SA15/readings/c9_c100.md`; Faltings-Chai V.6; Vasiu-Zink; de Jong-Oort.
- **R6. Contractions of finitely generated ideals over coherent rings.**
  - Question: settle 55:8. If A is coherent and J ⊂ A[T] is finitely generated, is J ∩ A finitely generated? Prove it,
    or give an explicit counterexample, e.g. in Soublin's ring ∏_n Q[[x, y]].
  - Why: his coherence question for compact Stein algebras of finite presentation.
  - Rests on: 55:2-12; SA18-18.
  - Strongest reduction: on the page, the question is reduced to pure commutative algebra. It holds when A is
    noetherian (compact semianalytic Stein sets, Frisch).
  - Material: the pages; Glaz, Commutative coherent rings (LNM 1371); Soublin (1970).
- **R7. Maximal tori of the quasi-split type outside Borel subgroups.**
  - Question: for G quasi-split over a field k with quasi-split torus T_1, decide whether a maximal torus T ≅ T_1 (as
    k-tori) must lie in a Borel subgroup over k. Decide it first over finite fields (twisted classes of W·τ that are
    conjugate in GL(X) but not under W), then in general.
  - Why: his Question 1 on 45:55 ("J'en doute"); his N.B. on 45:53 settles split T_1 over connected S.
  - Rests on: 45:45-57; SA18-2.
  - Strongest reduction: over F_q, the condition is a statement about twisted conjugacy classes in W(Φ) ⋊ ⟨τ⟩, a finite
    computation for each type (start with ^3D_4 and ^2E_6).
  - Material: the pages; Carter, Finite groups of Lie type; a computation in GAP/CHEVIE.
