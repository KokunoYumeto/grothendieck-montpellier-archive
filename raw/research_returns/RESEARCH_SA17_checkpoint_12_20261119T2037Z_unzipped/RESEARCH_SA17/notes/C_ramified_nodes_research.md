# Ramified exponent-two normal nodes

## Status

The complete theorem C:ramified_exponent_two_node is in `sections/C_finish_ramified_nodes.tex`. Root and representations independently audited the entire written proof. Root recorded its audit at18:05:53UTC; representations confirmed the independent full written audit before promotion. The exact certificate ran successfully, with scope and runtime in `logs/C_finish_ramified_nodes.json`.

## Construction and detector

Write 2=v*pi^e and assume e>1. Put h=1+2/pi, a=1+pi and T=[[a,x],[-h*y/u,-a]] over xy=pi^2*u. Then a^2-1=pi^2*h and T^2=1. Evaluate x=pi+epsilon, y=pi*u-u*epsilon in completed-A[epsilon]/epsilon^2. This completion is essential for arbitrary formal series over noncomplete A. The target is complete for (pi,epsilon), with topology cofinal with the pi-adic one.

The constant involution T0 and nil coefficient U satisfy T0^2=1, T0U+UT0=0 and U^2=h. Its plus cycles have generator w+=(1,-1), its minus cycles w-=(1,-h). Difference and norm factor as pi*w-*(1,1) and pi*w+*(h,1). Thus both Tate groups are A/pi; U maps w+ to -w- and w- to -h*w+. The odd linear-nil Bockstein therefore has square1 on both residue Tate groups. The nonzero primary z-1 has even length1, whereas constant sign lines have Bockstein0. This is precisely the general ramified finite-length parity detector already proved in C:ramified_squarezero_criterion.

The generic eigenbasis [[x,x],[1-a,-1-a]] has determinant -2x, a unit after inverting2. Hence the detected class [T]-1-sign is generically zero. Every admissible representation sequence is split on its underlying projective modules, so specialization preserves exactness even though the detecting ring map is not flat.

## Ring scope

Both the polynomial localization and the formal node are normal two-dimensional singular domains over any DVR A. The formal irreducibility proof uses the UFD A[[x,y]], reduction modulo pi, and evaluation at x=0. Vertical height-one localizations are DVRs; away from pi the formal derivative d/dy of the equation is the unit x. Polynomial generic rings are localizations of a Laurent-polynomial PID, so their integer-localized K0 groups are all Z. No generic K0 computation for the formal node is used.

## Boundary of the extension

This settles exponent2 for all dyadic ramification indices; the earlier theorem settles every exponent over unramified DVRs. The current scalar tangent construction for xy=pi^(2r)*u gives Tate length min(r,e) under suitable unit hypotheses, and its parity can vanish. It therefore does not prove the whole ramified all-exponent family. No all-exponent assertion is released.

## Failure of a raw eigenlattice divisor invariant (2026-11-19T18:14:25Z)

For any of these nodes with exponent n>=2 and 2=v*pi^e, consider the triangular involution

    S = [[-1, pi^(e-1)*x], [0,1]].

It has an admissible exact sequence sign -> S -> trivial, split on the underlying free modules. Therefore [S]=sign+1 in the lattice Grothendieck group. Its plus eigenvectors (a,c) satisfy 2a=pi^(e-1)*x*c, or v*pi*a=x*c. Projection to c identifies the plus eigenlattice with

    (2 : pi^(e-1)*x) = (pi:x) = (pi,y).

The last equality follows by reducing modulo pi: in kappa[x,y]/(xy), localized at the origin, or in kappa[[x,y]]/(xy), the annihilator of x is exactly (y). The ideal (pi,y) is a height-one prime and hence a reflexive rank-one ideal in the normal node. It is not principal: pi and y have linearly independent images in m/m^2, whereas m*(pi,y) is contained in m^2. Its minimal number of generators is two.

Thus even a polynomial Swan class has a nonfree reflexive plus eigenlattice with nonzero divisor class. The determinant of the plus eigenlattice is not additive on all admissible sequences and cannot itself be a kernel detector. In the usual cyclic node divisor group, the correction just exhibited already contains a basic vertical divisor generator. No class-group criterion is asserted from this route.

## Exact scalar parity boundary

For n=2r with r<e, taking a=1+pi^r, h=1+2/pi^r, and the balanced tangent x=pi^r+epsilon, y=pi^r*u-u*epsilon gives Tate groups A/pi^r and Bockstein square h. The nonzero primary parity is r modulo2. For r>e, taking a=1+pi^(2r-e) instead gives a unit V=(a^2-1)/pi^(2r) and two Tate groups A/pi^e, so the same detector sees e modulo2. These computations are exploratory boundaries: zero of this invariant does not prove zero of the representation class. For odd n, an integral scalar tangent at x=pi^r, y=pi^(n-r) introduces an extra factor pi in the square of the odd map. A higher-rank or different invariant is still needed for the uncovered cases.

## Newly opened historical source

Opened the original Koji Uchida, *Remarks on Grothendieck Rings*, Tohoku Math. J.19 (1967), pp341-348, at https://www.jstage.jst.go.jp/article/tmj1949/19/3/19_3_341/_pdf/-char/ja . Its Theorems1-2, pp343-344, concern regular domains of prime characteristic. Section2 pp344-345 discusses G_0 of all finitely generated modules over orders and an example where a maximal-order class-group analogy fails. These are not an intrinsic comparison theorem for the exact category of R-projective group lattices over a singular mixed-characteristic base. In particular G_0 cannot silently replace that lattice category when regularity fails. This source is a checked boundary/background pointer, not used to prove the new node theorem.

## Novelty search

The exact queries and results are saved in `logs/C_ramified_nodes_search.json`. They did not locate this explicit family theorem. Search absence is not a priority claim; the proof is independent and the cited commutative-algebra and Bockstein dependencies are explicitly rechecked.

## Ramification two, exponent three: exact boundaries and a new gate (2026-11-19T18:43:57Z)

Let 2=v*pi^2 and xy=pi^3*u. For a scalar a with a^2 congruent to1 modulo pi^3, reduction modulo pi in the reduced ring first gives a=1+pi*b. If b is a unit, v_pi(a^2-1)=2; if b is divisible by pi, that valuation is at least4. Thus the former scalar construction cannot have (a^2-1)/pi^3 a unit. This explains an exact limitation of that construction, not vanishing of the comparison kernel.

An exact rank-four involution can be built using

    C = [[0,pi],[pi^2,0]],  a = I+C,
    D = (a^2-I)/pi^3 = I+v*[[0,1],[pi,0]],
    T = [[a,xI],[-D*y/u,-a]].

Here C^2=pi^3 I, all entries of D are integral, D is a unit matrix, and T^2=I. The usual generic block eigenbasis has determinant (-2x)^2 and gives two free plus and two free minus eigenmodules. However a specialization with xy-pi^3*u=pi^m*s has det(T-I)=pi^(2m) times a unit. Its sole nonzero residual curvature primary therefore has length2m, zero modulo m. This curvature test does not detect the class. After the ramified balanced tangent pi=w^2, x=w^3+epsilon, y=w^3*u-u*epsilon, the odd nil square is D with sole residual eigenvalue1; no nonzero primary parity has been established.

A different rank-two candidate is

    a=1+pi^2*b,
    T = [[a,x],[-pi*b*(v+b)*y/u,-a]].

Its square is exactly I because a^2-1=pi^4*b*(v+b). Specialize to A/(pi^3), with x=pi^2 and y=pi*u*s. Both sides of the node relation vanish, so s is arbitrary. The result is T=I+pi^2*N with residual matrix

    Nbar = [[b,1],[b*(v+b)*s,v+b]]

in characteristic2. Its trace is v. If the residue contains F4 and v=1, choose b=alpha with alpha^2+alpha+1=0 and s=alpha^2; its characteristic polynomial is z^2+z+alpha, irreducible and invariant under z -> z+1. This resembles the successful unramified primary Bockstein witness.

The existing mod4 Bockstein theorem DOES NOT apply to A/(pi^3): Ann(2)=(pi)/(pi^3) is strictly larger than (2), so division by2 does not give the required endomorphism on ordinary mod2 homology. A possible replacement is the second pi-Bockstein operator after removing lower-page homology. Its additivity on arbitrary admissible extensions is currently unproved: taking the next homology of an exact cyclic sequence need not preserve exactness without additional control. No result or check row claims that this construction proves nonvanishing. This is a precise remaining gate, and no parity-zero computation is interpreted as a vanishing theorem.

## Refutation of the proposed higher-page parity (2026-11-19T18:47:51Z)

The additivity gate in the preceding paragraph is now answered negatively for that proposed detector. This does not resolve the node class or refute any released theorem.

Use the smallest residue field F2 and the exact eight-element ring

    S = Z[pi]/(pi^2-2, pi^3).

Take N=[[0,1],[1,1]], whose irreducible polynomial f=z^2+z+1 is invariant under z -> z+1. Put T_N=I_2+pi^2*N and consider the admissible extension with middle involution

    E = [[T_N,pi*I_2],[0,I_2]].

Both diagonal actions square to the identity. The off-diagonal entry in E^2 is pi*(2I+pi^2*N)=0 in S, so E is also an involution. Its first normalized pi differential is [[0,I],[0,0]], hence acyclic. The proposed second page is therefore zero on E. On both endpoints the first normalized differential is zero; their second operators are respectively N and0. The f-primary parity would be1 on the submodule,0 on the quotient, and0 on the middle term, violating additivity.

The exact program `code/C_finish_ramified_higherpage_failure.py` was executed. It checks all512 ring triples for the ring identities used, and all530 matrices N overF2 in ranks1,2,3. Each yields the valid displayed extension and an acyclic first normalized middle differential;114 endpoint choices violate the proposed primary-parity additivity. The explicit rank-two matrix above is the smallest irreducible-primary witness. Runtime0.15944971499266103 seconds. Full output: `logs/C_finish_ramified_higherpage_failure.json`.

The program also verifies the reason the ordinary mod4 Bockstein theorem cannot be applied: Ann_S(2) has four elements, whereas the ideal(2) has two. Its output records the precise refuted proposal and explicitly excludes the original C.1 question and every released theorem. No nonvanishing or vanishing conclusion for the e=2,n=3 normal node follows from this certificate.
