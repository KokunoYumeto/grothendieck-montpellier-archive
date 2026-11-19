# Anabelian and conjugate-topology source audit

Date: 2026-11-19. Root audit. This note records inspected maps and remaining obligations; it supplies no additional place-reconstruction theorem.

## Ayoub: exact comparison under examination

Opened the 257-page author PDF of *Anabelian presentation of the motivic Galois group in characteristic zero*, https://user.math.uzh.ch/ayoub/PDF-Files/Anabel.pdf . The published Cambridge article is FMS14(2026)e139,251pages; the locators below refer to the author PDF, not to a silently substituted pagination. Author PDF SHA256: eb90dbfd49c86ca2b7f33ff282bdb9e193dd22aa35991d468c2e592b788ed3ac.

Definition1.6.1(p49) constructs geometric sheaves from proper pushforwards, colimits and desuspension, and geometric local systems from dualizable objects. Theorem4.4.2(p234) identifies the spectral motivic group with automorphisms of that functor. Corollary4.4.15(pp248–249) gives the classical Picard-prestack statement. Corollary4.4.16(p249) gives the Galois group for torsion connected coefficient rings. Remark4.5.2(p250), rather than a lemma with that number, constructs the composition-compatible map from discrete topological paths to geometric-completion rational points, with Zariski-dense image.

The restriction problem being tested is to construct, from an automorphism of the smooth-projective integral cohomology/correspondence diagram, a compatible autoequivalence of this whole local-system functor. No such extension has yet been constructed here. A second required check is preservation of the actual image of the discrete-path map; Zariski density alone is not that check. Both obligations are retained with these exact maps.

## Bauer–Catanese–Grunewald: identity qualification in the retrieved source

Opened arXiv1303.2248v1,24pages, https://arxiv.org/pdf/1303.2248 . Header9March2013; manuscript footer30October2018. SHA256:19fb520d1d6db4681a5683da73a40af3abe85e1bce98d146b06265f46b945686.

Theorem0.1(p1), repeated as Theorem4.13(pp17–18), omits the exclusion of the identity from the stated automorphisms outside the conjugacy class of complex conjugation. At sigma=1, X^sigma=X and the identity map induces the same fundamental group, so this exact printed universal formulation fails. Its proof starts by asserting infinite order; the identity must also be excluded at that step. The proof then uses faithfulness on moduli components and at most two components with a specified fundamental group. The older arXiv0706.1466 proof is not used; the retrieved paper explicitly corrects that earlier argument.

No map has been established here from a comparison of the pure integral cohomology diagram to an isomorphism of the discrete fundamental groups in this theorem. Its faithful-action conclusion is therefore retained as a source lead with that specific missing construction, rather than used to close E.2.

## Schreieder: scope of the constructions inspected

Opened arXiv1304.5146v2,5December2013,26pages, https://arxiv.org/pdf/1304.5146 . SHA256:0d01a0ccd63212773ff31c5548e8187996447646f41d8a38fa1ee70ff24a2808. Read the introductory statements and the construction in Section7, especially p22. The construction there chooses an automorphism fixing i and a field of definition but moving a specified cyclotomic root. It does not supply the required instance for the quartic automorphism already chosen to fix every CM abelian extension. This is the exact failed substitution, not a claim that no other construction can relate these objects.

## Additional current-source lead, not a mathematical input

The current openai/math repository contains a September2026 manuscript claiming the rational Hodge conjecture for all CM abelian varieties. Its introduction, assembly section, repository README/history and formalization-scope page were opened; its full proof and Lean statement have not been audited in this run. The source is therefore not used to promote any assertion status. The downloaded CONTENTS file was searched for Katz, Hodge decomposition, elliptic periods, de Rham–Betti and related terms; no direct resolution of H1 or the integral E2 image was located. This is a search record, not evidence of absence from the literature.
