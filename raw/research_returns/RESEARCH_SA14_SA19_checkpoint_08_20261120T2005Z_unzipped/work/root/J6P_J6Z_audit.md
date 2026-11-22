# Independent audit of J6P and J6Z

Date: 2026-11-20 17:38 UTC. Auditor: GPT-6 Astra (OpenAI, ChatGPT Pro mode), root run; effort inherited and not exposed.

Outcome: PASS within the exact stated scope, including the separately conditional finite-kernel clause.

We read `work/dgj/attempt_J6_pencil.tex` in full. We independently opened Achter–Casalaina-Martin–Vial, *A functorial approach to regular homomorphisms*, author PDF (40 pages), and checked Lemma4.7, Theorems5.10 and6.1, Proposition8.2, and Remark8.6. We independently opened Conrad's 17 June2006 author PDF *Chow's K/k-image and K/k-trace, and the Lang–Néron theorem*, Definition6.1 and Theorem6.2 p20 and Theorem7.1 p23. We opened Jiang's publisher full text, §2.3 Theorem2.8(3), to verify the codimension-two blowup formula. Hard and weak Lefschetz were checked against the previously opened Deligne1980 §§4.1.1 and4.1.6.

J6P requires a smooth codimension-two pencil axis and a smooth generic member; these conditions are genuinely used. A miniversal cycle on the generic member pulls back along the trace and spreads by closure on T times the smooth blowup. Normalization at zero gives a regular map between abelian varieties, hence a homomorphism. Its generic restriction is r times the trace morphism.

The inverse to the codimension-two Chow decomposition is (p_*,-q_*e^*); the minus sign follows from the normal bundle O_E(-1). These operations preserve algebraic equivalence and parameter families, so the same decomposition holds for universal regular representatives. Restriction of the exceptional summand is b_* on Picvar(B), without an excess term. A smooth member exists because the pencil is proper and generically smooth. Two applications of weak Lefschetz make Picvar(X) to Picvar(B) an isogeny for n>=4. The identity b_*(L|B)=j^*(H L) then absorbs the exceptional summand in the image from X. The universal trace property gives the opposite inclusion.

For n>=5, weak Lefschetz makes H3 of the generic member constant. ACMV Proposition8.2 supplies an injective integral Tate realization after choosing a prime avoiding the characteristic and a miniversal integer. Constancy rationally forces constancy integrally because a Tate module is torsion-free. All prime-power torsion is therefore K-rational. Its divisible image in the finitely generated Lang–Néron quotient is zero; torsion density forces the trace image to be the full target.

The finite-kernel argument is correct only with the explicitly stated injectivity of the target universal regular homomorphism on cycle torsion. Miniversal cycles detect the Tate module of a positive-dimensional putative kernel, while this torsion hypothesis kills its restricted cycle Tate module. Weak Lefschetz is injective on H3 for n>=4, giving the contradiction rationally. Proposition8.2 alone does not supply the missing hypothesis in positive characteristic, and the proof does not claim that it does.

J6Z follows by composing Picvar(X) with intersection by H^(n-2). On Y this induces the hard-Lefschetz isogeny Picvar(Y) to Alb(Y), and restriction on Picvar is itself an isogeny. Thus the target Albanese is covered. The equality of its incidence quotient with the Albanese follows from the Poincare family, as in the already checked incidence construction.

These conclusions do not settle singular pencil axes, an unspecified manuscript equivalence relation, higher codimension, or positive-characteristic finite kernel without the torsion hypothesis.
