# Common monodromy forms: exact map audit

Auditor: OpenAI GPT-6 Astra, effort inherited, elliptic_splitting.
Date: 19 November 2026. Work-only investigation of the unrestricted abelian-family route. No extension of E.2.26 is asserted.

## 1. The map needed by the existing approximation argument

Let V_B be the fixed rational Betti realization of a finite abelian family and let
beta_l: V_B tensor Q_l -> V_l
be its specified Betti–etale comparisons. Write H_l=beta_l^{-1}G_l^der beta_l inside GL(V_B tensor Q_l). Applying the rational strong-approximation argument used in E.2.26 requires an actual rational representation j:J->GL(V_B) with local image j(J_Q_l)=H_l, or another proved rational subgroup whose adelic image contains the specific torsor difference and the correcting open subgroup. An abstract family of local root-data identifications is not itself this j.

For example, suppose a common rational representation r:G->GL(W) and local intertwining isomorphisms b_l:W tensor Q_l->V_l have been constructed. Choose any rational isomorphism b:W->V_B. In the fixed Betti coordinates put q_l=beta_l^{-1}b_l b^{-1}. Then

H_l=q_l (b r(G^der) b^{-1})_Q_l q_l^{-1}.

This equation is the exact relationship. Strong approximation in r(G^der)(Q) approximates matrices rational in the W structure. After transport by q_l their components need not be the scalar extensions of one matrix rational in V_B. Producing a common rational q, or an adequate rationally embedded subgroup and rational coset for the actual adelic difference, is the additional map obligation. No assertion that such a descent is impossible is made.

## 2. Opened common-form theorem and its hypotheses

The complete Chun Yin Hui manuscript arXiv1805.08383v3,2November2022,36pages, was opened and downloaded. Theorem1.6 p6 requires positive-density ordinary places, a common complex tautological representation, and the stated invariance-of-roots condition. Its common-Q-form representation conclusion also assumes irreducibility. Corollary1.9 pp6–7 includes HypothesisH and local representation isomorphisms phi_l. Theorem1.11 p7 treats an End=Z abelian variety under ordinary-density and formal-character hypotheses. Representation isomorphism is defined on p2 through a local vector-space isomorphism; the theorem does not identify it with beta_l. Thus these exact statements do not yet supply the j of section1 for an arbitrary finite abelian family.

Primary URL: https://arxiv.org/pdf/1805.08383 . Opened references turn801676643view0, turn704256714view1–3. Local work/sources_elliptic/hui_rationality2022.pdf/.txt. No final-journal text is claimed read.

The complete19-page original Larsen–Pink author PDF was also opened at https://people.math.ethz.ch/~pinkri/ftp/LP3.pdf, reference turn801676643view1. Its introduction pp1–2 explicitly formulates the common-form representation isomorphism and the stronger specified-comparison assertion separately. The exact sufficient comparison in its Theorem4.3 uses equality of ranks with the Hodge group. We do not use this source to claim a current nonexistence theorem.

## 3. Direct containment in the Mumford–Tate derived group implies MT

There is a short exact implication for the particular proposed substitute. Let M be the Mumford–Tate group and suppose the actual connected monodromy G_l inside M_Q_l contains M_Q_l^der. Commelin Lemma4.18, already opened and used in E.2.26, identifies their connected centers in this fixed realization. For connected reductive groups in characteristic zero, multiplication Z(M)^0 times M^der -> M is surjective: its image is a connected closed subgroup with Lie algebra z(m)+[m,m]=m. Both factors are then contained in G_l, so M_Q_l is contained in G_l. The opposite containment is the known comparison inclusion, and equality follows. An open subgroup of M^der(Q_l) inside the actual image has Zariski closure M^der, so it satisfies the same implication.

This proves why that specific direct containment settles the Mumford–Tate equality for the selected family. It does not prove equivalence between every imaginable common rational form and Mumford–Tate, and does not exclude a different approximation construction.
