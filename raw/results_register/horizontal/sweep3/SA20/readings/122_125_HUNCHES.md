# SA20 hunches from the reading `122_125` (sweep 3, wave 2)

By Claude Opus 5.5 at effort max, reader 122_125, horizontal sweep 3, 19 Nov 2026. "From memory" marks literature not
opened in this run.

## Cote 122 (SA20-18, SA20-19)

**H20-122_125-1. The variation is forced by his "donnée fondamentale": because π acts trivially on L, T − 1 factors
through u, and the factor is the variation.**
- *What may be true:*
  - In D(Λ[π]), the triangle (a′) is K^∨[−2n] →u K →ρ L^triv →, with ρ equivariant and π acting trivially on L (020:
    "on met dessus op. triviale de π").
  - So ρ∘(T − 1) = (T − 1)∘ρ = 0, and T − 1: K → K factors as u∘V for some V: K → K^∨[−2n] ≅ RΓ_c(M°).
  - V should be the variation map of Picard–Lefschetz theory, Var: H^n(M) → H^n_c(M°), so that T − 1 = u∘Var.
  - The equivariant structure of u, which he insists on ("dans D(Λ[π])"), is what makes V canonical. In D(Λ) alone, V
    is defined only up to Hom(K, L[−1]).
- *Consequences:*
  - His "(signe ?)" becomes the classical relation between the intersection form and the Seifert form, u = −(S ±
    (−1)^n S^t) with S = Var^{−1} on the middle degree (Lamotke 1975; Arnold–Gusein-Zade–Varchenko II; from memory).
  - The sign question of 022 has a definite answer once Var is fixed.
- *Grounds:*
  - 020 (a), the trivial action on L;
  - 022, u in D(Λ[π]) and "ρ et ρ′ sont transposés (signe ?)";
  - 024, the "données nouvelles" u₁, λ, μ that RΓ^π extracts;
  - the Pro notes RN020, on the H¹(π, ·) part of the equivariant class.
- *Relation to H20-7:* sharpens H20-7, which identifies (a′) with "the variation and intersection-form structure" without
  the mechanism.
- *Links:*
  - SGA 7 XIII–XV (variation, Picard–Lefschetz; from memory);
  - WG H2(b): for n = 1, V is the Dehn twist's variation on the annulus, whose cohomological shadow (Part 1, item 6 of the
    working) H2 lifts to π₁.

## Cote 125 (SA20-W2)

**H20-122_125-2. Cote 125 is a statement of the duality criterion for the cohomological dimension of complements,
about 1961–62, in the generality of a projective Cohen–Macaulay X, both directions, with the injectivity clause.**
- *What may be true:*
  - For X projective Cohen–Macaulay of dimension r and Y closed: cd(X − Y) < m iff H^q(X, F) → H^q(X̂, F̂) is bijective
    for q < r − m and injective for q = r − m, for all locally free F.
  - It also suffices to test F = O(n), n ≫ 0, by H^0 and the vanishing of H^i(X̂, Ô(n)) for 0 < i < r − m.
  - That is the chain of 003, closed in steps 1–6 of the working.
- *What is in print* (from memory, to be checked on the books):
  - SGA 2 XII §1 (projective duality) and XIII (the problem of cd(P − Y));
  - Hartshorne, Ample subvarieties (LNM 156, 1970), III.3.4;
  - Hartshorne, Compositio Math. 23 (1971), Prop. 2.9, for X = P^n. This reference is from Michel Hua's project, which
    reads it as stating one direction without the injectivity clause.
  - Ogus 1973 and Speiser 1973 (de Rham and Frobenius forms).
- *Grounds:*
  - 003 (the chain, with "dualité" on the arrow, the Kif-kif reduction and the NB on p = m);
  - 005 (the formal duality written out);
  - 008 (the boxed form for P ⊃ X);
  - the paper: the pre-EGA typescript pages III-5 and III-18 of 004 and 007;
  - the title "Dualité locale et dualité projective", the subjects of SGA 2 V and XII §1.
- *What would settle it:*
  - the exact statements of SGA 2 XII §1–2 and of Ample subvarieties III.3.4, for which generality and which direction;
  - an identification of the typescript (EGA III drafts).
- *Links:*
  - SA20-18, the local side ("Lefschetz local", 122/028);
  - Michel Hua's project's literature trail for 125 (Halic, Ottem, Lau on q-ample subvarieties), credited there.

**H20-122_125-3. The frame of 125/006 is the inductive step of a formal Lefschetz theorem: from (X′, Y′ = Y ∩ X′) to
(X, Y).**
- *What may be true:*
  - The paired long exact sequences of a hypersurface section X′ ⊂ X, in their local-cohomology form ("plus général",
    supports Y and Y′) and their completed form (X̂, X̂′), are what an induction on hyperplane sections needs.
  - They transport the comparison H^q(X, F) → H^q(X̂, F̂) from X′ to X, with the injectivity clause at the boundary
    degree.
  - His "?" on 006 is the one identification the induction needs on X′. It holds (working, step 9), so nothing on the
    page blocks the induction.
- *Grounds:*
  - the degrees r, r − 1, r of the pairings on 006;
  - 008's item 2, "En théorie de Lefschetz … relations entre une variété (projective, ou locale) et son complété formel
    le long d'une section hyperplane".
- *Links:* SGA 2 X–XII (Lef and Leff conditions; from memory); H20-122_125-2.
