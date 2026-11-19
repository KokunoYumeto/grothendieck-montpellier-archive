# Residual C4 research through the 09:50 review, with recovery notes

This is a reconstruction of the post-checkpoint09 report following the 10:14 UTC scratch reset. Original source readings and proof checks are retained as historical events; downloads and computations were rerun with separate actual timings.

## Main gate remains unresolved

For a surface A, C.4r identifies actual splitting from a product of Jacobians with an integral numerical representative of P²/2 on A×Â. For a threefold the analogous class is P⁴/24. The generic End(A)=Z, type(1,2) surface and arbitrary supersingular threefolds in characteristics two and three were not settled by the leads below. No method exclusion in this report is counted as main-gate movement.

## Genus-five full-span Prym curves

The complete integral Hom calculation is in `C4_genus5_integral_lattice_REPORT.md`. It allows every incoming and outgoing integral homomorphism through the indicated Jacobian, not only the maps originally displayed by the geometry. Conditional on the exact Prym premise, every composite is even, with ideal4Z for672 and2Z for48 of the720 symplectic mod-two markings. Parent and cycles independently checked this proof. Cycles' check was conditional on the geometric premise, not a fresh reopening of the primary geometry.

Primary: Clingher, Malmendier, and Shaska, *Geometry of Prym varieties for certain bielliptic curves of genus three and five*, arXiv2005.04839v2,7September2021. Complete primary PDF opened, diagram(1.3)p3 and Theorem1.2p5 read. The ramified-Prym quotient convention is not confused with the principally polarized étale Prym.

## October2026 supersingular derived-isogeny theorem

An Jiang, Zhiyuan Li, and Ziwei Lu, *Derived equivalences and isogenies of supersingular abelian varieties*, arXiv2610.24666v1,17October2026. Complete primary PDF downloaded and read. Definition1.1 allows twists and chains. Theorem1.2 and its proof in §3 pp5–6 show derived isogeny for all supersingular abelian varieties of the same dimension; the construction uses twisted Fourier–Mukai equivalences. It does not give an actual untwisted product decomposition or a prime-to-p factorization of the identity.

Theorem4.1 pp6–7 gives, in every characteristic and dimension g>2, supersingular examples A such that Aⁿ is never isomorphic to Âⁿ. The proof uses A=Eᵍ/H with an alpha_p subgroup defined by F_{p²}-linearly independent coefficients. An assumed isomorphism would produce an endomorphism of E^{gn} of degree p^{2n} whose kernel contains ker(F^{gn}), forcing p^{gn}|p^{2n}. This contradiction shows that principal polarizability of arbitrary supersingular threefolds is not a valid shortcut. It still does not obstruct being a direct summand of a larger product of Jacobians.

## EGFS monodromy scope

Engel–de Gaay Fortman–Schreieder, arXiv2507.15704v3, was reopened, including Theorem1.6. Its specified matroidal-family criterion uses independent boundary monodromy logarithms proportional to rank-one quadratic forms. In the family A×Â obtained by varying A, H¹ contains two isomorphic copies of the same variation, so every corresponding monodromy logarithm has even rank. Thus this precise criterion cannot simply be applied to that correlated subfamily. The very-general principally polarized fourfold theorem also does not specialize automatically to the three-dimensional type(1,2) product locus. No extension of the theorem was proved.

## New Chern-method exclusion after09:50

`C4_semihomogeneous_obstruction.tex` proves that all semihomogeneous Chern constructions miss P²/2 and have even mixed degree-three coefficients. The proof uses the full general semihomogeneous Chern identity, not just rank-two examples. It also covers Chern classes of the familiar odd-rank virtual Fourier transform of a universal one-point ideal sheaf, by its exact K₀ decomposition. Arbitrary moduli kernels and arbitrary algebraic cycles are outside its scope.

## Exact current Fourier/motive literature limitations

Li–Zou's author primary text, <https://www.math.uni-bielefeld.de/~hzou/papers/derivedab/>, was opened completely. Corollary1.2.2 relates derived isogenies to motive isomorphisms; §3.1 explicitly uses Chow correspondences with Q coefficients, and equation(3.1.1) is ch(P) in CH*(X×Y)_Q. The integral twisted Mukai lattice in §3.2 is a different realization. Neither the rational-motive theorem nor integrality of that cohomological realization supplies an integral numerical P²/2 cycle.

Hasan–Hassan–Lin–Manivel–McBeath–Moonen (2025), *Integral aspects of Fourier duality for abelian varieties*, DOI10.1007/s00229-025-01662-7, was opened at the complete publisher HTML. Theorem4.5 and §1.2 construct integral transforms lifting (2g+d)! times the classical transform; Theorem5.5 works after inverting (2g+d+1)!. This is a precise integral denominator theorem, but it does not remove the prime two in the residual surface problem. The statements and coefficient rings were checked; no claim that their full proof was independently rederived is made.

## Reproducibility

Fresh acquisition records, URLs, SHA256 hashes and times are in `output/residual_and_K2_sources_manifest.json`. The reconstructed genus-five script reproduces the720-marking result in a separately measured run. The original 09:37 run and the fresh 10:20 run are distinguished. No reconstructed artifact claims to be a byte-identical copy of a lost file.
