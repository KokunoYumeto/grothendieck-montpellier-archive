# Independent whole-proof review of A21

**PASS.** Read the complete source `work/effective_galois/A21_GENERIC_ODD_TORSION.tex`. The final checked source SHA256 is `edfc8cb14ee02980e82de31d9b857eed2fa62ca29707ad997ae2696b54c51111`. The only requested correction was bibliographic: the actual LSTX2017 title is “Lifting subgroups of symplectic groups over Z/ell Z.” The author incorporated it; the proof was unchanged.

## Generic monodromy

Achter–Pries Theorem4.5 explicitly permits genus2 and positive p-rank, in characteristic2. I opened its primary theorem and relevant proof sections. I also read Ozman–Pries Theorem4.2 and the whole proof of Proposition4.3, printed p465, from the recovered primary text: the full level-ell torsor is asserted irreducible. This is sufficient for the generic-point argument, without incorrectly assuming a smooth-open fundamental group surjection from a nonnormal base. Tricanonical frames have geometrically integral GL5 fibres; their pullback preserves irreducibility. A nonempty smooth affine open then preserves irreducibility of every level-ell torsor. The same chosen generic curve works for every ell; no infinite intersection of opens is taken.

The prime-to2 relative Frobenius isogeny identifies the Tate modules for C and C^(1) by a symplectic similitude, so it transports the full symplectic group. LSTX Theorem1 supplies full ell-adic image from full mod-ell image.

## Joint finite levels

LSTX Proposition1(b), including its proof, was read directly on the publisher page. It gives perfectness for every odd ell, including3, at every finite prime-power level. I also opened J.I. Hall, Classical Groups and Geometry, version6May2015, Theorem12.26 and its immediate proof, printed p173: the only exceptions are Sp2(2), Sp2(3), Sp4(2). Thus none affects Sp4(Fell) for odd ell. I do not claim to have independently reproved all prior lemmas of Hall's book or the full Achter–Pries theorem.

The congruence kernel is an ell-group. A nontrivial simple quotient of a perfect finite symplectic group is nonabelian and kills this kernel; its unique possibility is PSp4(Fell). The displayed order strictly increases with ell. Goursat's common-quotient argument and induction over distinct primes therefore give the full CRT product. A simple quotient of a product factors through one factor because the factor images are commuting normal subgroups. This checks the entire independence step, rather than presuming it from individual surjectivity.

## Theta contradiction

Symplectic Gram–Schmidt over each local ring proves transitivity on exact-order vectors; CRT then gives transitivity for arbitrary odd n. The translated Abel curve is defined over the generic field by the canonical locally exact differential bundle B. If it contains one exact-order-n point, it contains every such point. For ell dividing n, the points e1+j(n/ell)e2 are all exact order n and form an ell-point translation orbit. Each lies on both theta and theta+T. This contradicts the included genus-two Riemann–Roch proof that a nonzero translate intersection has at most two geometric points. The argument works also for ell=3 and for arbitrary composite n.

## Whole new factor

For a connected odd cyclic cover, each nontrivial original genus-two character space H1(C,M^i) is one-dimensional, including characters of proper conductor. The tensor exact sequence in GO.7 is correct with L_i=(M^i)^(1); its vanishing H0 term makes the Frobenius arrow i to2i injective and hence bijective. Since doubling permutes all nonzero residues, the entire nontrivial-character sum has stable rank n-1. Norm and pullback, together with genus(D)=n+1, give whole new factor dimension and rank n-1. No rank-zero primitive inference or higher-genus line-space argument is substituted here.

The assertion remains geometric generic. Finite lists give a common nonempty avoidance open, while no single avoidance open for all odd orders is asserted. No GRH or prime-density input is used.

Primary URLs reopened for this review:

- https://www.math.colostate.edu/~achter/math/prm0508.pdf (Theorem4.5, Lemma4.3, Section5.1/Lemma5.2; web refs turn629786725view0, turn129559844view1, turn676770197view0).
- https://link.springer.com/article/10.1007/s40993-017-0078-6 (Theorem1 and Proposition1(b); refs turn629786725view1, turn717258048view1).
- https://link.springer.com/content/pdf/10.1007/s40993-017-0078-6.pdf (title page visually checked; refs turn542988490view0, turn716993511view0).
- https://users.math.msu.edu/users/halljo/classes/MTH913_S15/cgg_2015-05-06.pdf (Theorem12.26; refs turn717258048view0, turn676770197view2).
