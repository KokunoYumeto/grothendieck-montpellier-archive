# Independent audit of the ordinary Igusa deformation calculation

Auditor: /root/fhi. Date: 20 November 2026.
Reviewed file: work/dgj/attempt_D4_ordinary.tex.
Outcome: the ordinary-case flatness argument and the stated hull calculation pass this independent audit. No hidden assertion of surjectivity on R-valued torsion points was found. No supersingular conclusion is included.

## Exact primary checks

I independently opened:

- Nicholas Katz, *Serre–Tate local moduli*, Theorem 2.1, printed pp.148–149, and the pushout-homomorphism recovery, pp.150–152. URL: https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf .
- Mumford–Fogarty, *Geometric Invariant Theory*, second edition, Proposition 6.15, pp.124–126, through the primary-book OCR mirror https://dokumen.pub/geometric-invariant-theory-2nbsped-3540112901-9783540112907.html . The proposition explicitly assumes smooth proper, not projective, and applies across a small Artinian extension.
- Chai's complete seven-page *Mumford's example of non-flat Pic-tau*, dated 6 March 2008. URL: https://www2.math.upenn.edu/~chai/papers_pdf/mumford_ex_v2.pdf . Direct retrieval returned 403, but opening the already indexed full source reference succeeded. Theorem 2.4, pp.6–7, really does assume both elliptic curves ordinary and really does assert nonflatness of the universal first-order Pic-tau. The concluding inference and Remark (1) have no omitted qualification repairing the issue described below.

## 1. Lifting the cover

Finite étale invariance under nilpotent thickenings lifts the cover and its deck transformation. Smoothness and properness of the cover follow from those of the deformed quotient and the finite étale map. A lift of the marked origin exists because the cover is smooth over the Artinian local base. The precise Mumford–Fogarty proposition gives its abelian-scheme structure, successively over a small-extension filtration.

Writing the deck transformation as a translation followed by an origin-preserving automorphism is legitimate. Rigidity makes the latter a group automorphism, and its square is the identity because it lifts the identity group homomorphism. Thus the affine involution equation is exactly (1+sigma)c=0.

A marked isomorphism of deformed quotient surfaces lifts uniquely to the marked cover isomorphism restricting to the identity on the original cover. The alternative deck lift does not restrict to the identity and is thereby excluded.

## 2. The canonical lift c0 and the Serre–Tate row

This was the most important point-coordinate check.

Let P_n be the specified compatible point of order 2^(n+1), with 2^n P_n=P. For n sufficiently large the formal kernel of A(R)→A0(k) is killed by 2^n. This is explicit in Katz's Lemma 1.1.1 and in the recovery on p.151. Therefore

    c0 = [2^n](any lift of P_n)

is independent of the lift. For consecutive n, the difference 2*lift(P_(n+1))−lift(P_n) belongs to that killed formal kernel, proving compatibility and independence of large n. It is functorial in the base after choosing the original compatible Tate sequence.

Since sigma0 fixes every P_n, the difference sigma(lift(P_n))−lift(P_n) is in the formal kernel. Hence sigma(c0)=c0 exactly, not merely after reduction.

Katz recovers the pushout homomorphism from a level-m Tate point by multiplying an arbitrary lift by 2^m. Here P_n is the level n+1 Tate point, so [2]c0 is precisely the pushout-homomorphism value at e2. Pairing with the chosen dual Tate basis gives

    [2]c0 = (q21,q22).

There is no inverse or off-by-one error under the stated Katz convention.

The ordinary formal group is canonically identified, using the dual Tate basis, with the product of two formal multiplicative groups. The lift of sigma acts there by inversion on the first coordinate and the identity on the second, because toroidal formal-group homomorphisms lift uniquely from the residue field. Every lift of (0,P) is c0+z. Its norm under 1+sigma is therefore (q21,q22*z2^2). Consequently q21=1 and q22*z2^2=1 are necessary and sufficient for the affine involution.

The automorphism lift criterion in Katz Theorem 2.1(4) separately gives q12^2=q21^2=1. Combining these conditions gives exactly the displayed ring W(k)[[t,s,u,v]]/(s^2+2s).

## 3. The dual extension

For B=A^vee, Katz's duality rule transposes q. Its matrix is

    ((q11,1),(q12,q22)).

Apply the homomorphism-lifting criterion to the original inclusion E0^vee→B0. For the second dual Tate basis vector, the source pairing is 1; the target pairing is the (1,2) entry of B's matrix, namely q21 of A. Thus its necessary condition is q21=1, exactly as claimed.

The projection B0→F0^vee has the same condition: it tests the second column of B's matrix. The two diagonal equations prescribe the elliptic deformations with parameters q11 and q22. The compositions vanish by rigidity.

For completeness, the fibrewise geometric argument is sufficient. A lifted proper homomorphism whose closed fibre is the elliptic inclusion is a closed immersion: it is unramified by the cotangent criterion and proper with finite fibres; its kernel has only its identity section. The projection is smooth, since it is a morphism between smooth R-schemes with smooth closed fibre (equivalently its differential is surjective by Nakayama). Its smooth elliptic kernel is the lifted inclusion, as the closed fibres agree. This yields the asserted exact sequence of abelian schemes.

## 4. Fixed group

In any such extension 0→E→B→F→0 with sigma acting as −1 on E and +1 on F, put G=ker(1−sigma). If b is a section of F, lift it fppf locally to a of B. The element (1−sigma)a lies in E. Multiplication by 2 on E is finite faithfully flat, so after a further fppf cover there is z in E with 2z=(1−sigma)a. Then a−z is fixed.

The kernel of G→F is exactly E[2]. This proves fppf exactness and makes G→F an E[2]-torsor. It is finite locally free of degree four, and G is flat over R. This uses fppf local division, never division in E(R).

## 5. Relative Pic-tau exactness

The finite étale quotient A→X is a torsor under the constant group Z/2, even when 2 is nilpotent in R. Translation acts trivially on the relative Picard functor of A. Therefore the image of pullback from Pic-tau_X lies in the fixed subgroup G of A^vee.

Conversely, take an invariant relative class in A^vee over a base change T. Fppf locally on T, choose a representative line bundle L and an isomorphism alpha:tau^*L→L. Equality of relative classes may initially leave a line bundle from T; trivializing it fppf locally supplies the actual alpha. The cocycle defect alpha*tau^*alpha is a global unit on A_T, hence a unit from T because an abelian scheme has universally trivial direct image of its structure sheaf. Adjoining a square root of its inverse is a finite faithfully flat cover of T: the polynomial is monic, and its constant term is a unit. Rescaling alpha gives a genuine linearization and therefore a descended line bundle D on X.

Its class lies in Pic-tau: D^2=Nm(L), and on each geometric fibre the norm morphism sends the connected Pic0(A) into Pic0(X). Hence D is torsion modulo Pic0 on every fibre. This fibrewise condition defines the relative open Pic-tau subfunctor; nilpotent base structure introduces no stronger condition.

Conversely a Pic-tau class pulls into A^vee because the Néron–Severi group of every geometric abelian fibre is torsion free. Thus the claimed surjection onto all of G, rather than a smaller subgroup, is justified.

The kernel consists of linearizations of the trivial line bundle, modulo its scalar automorphisms. Since the deck action is trivial on base units, these are exactly the characters of the constant group Z/2, namely mu_2. The kernel and surjectivity statements hold as fppf sheaves over arbitrary T. Therefore Pic-tau_X→G is a mu_2-torsor, finite locally free of degree two. Composed with G→F^vee, it is finite locally free of degree eight, so Pic-tau_X/R is flat.

Representability is also consistent: a torsor under a finite locally free group over a scheme is represented by a scheme after effective fppf descent. No smoothness or existence of an R-section is inferred.

## 6. Hull and algebraization

The triple functor is represented by the stated complete local ring because the marked abelian deformation is represented by its Serre–Tate matrix, the automorphism lift is unique, and c has the explicit formal coordinates above.

Forgetting the origin is formally smooth: a lifted surface gives its uniquely lifted cover, and any specified origin at the previous Artinian stage lifts by smoothness. At first order, a marked cover isomorphism is a formal translation followed by the uniquely marked abelian isomorphism. Changing origin alters c by plus or minus (1−sigma)d; in the first formal coordinate this is a square or its inverse. Every principal unit over k[epsilon]/epsilon^2 has square 1. Thus no first-order parameter is identified, giving the required tangent bijection. The sign convention for the origin shift does not affect this conclusion.

For algebraization, the product polarization multiplied by 2 satisfies Katz's lifting condition qij^2=qji^2. Its lift is symmetric by rigidity. Pulling the Poincaré bundle back along the diagonal associated with that symmetric homomorphism gives a compatible ample bundle whose special polarization is 4 times the original one. Formal existence then algebraizes the family and its compatible automorphism and point. An invariant ample bundle supplies the projective quotient.

These hull and algebraization steps are not logically needed to conclude flatness for every ordinary Artinian deformation: lifting the cover, applying Serre–Tate, and the two torsor sequences already prove that statement.

## 7. The written Chai conclusion

Chai's obstruction calculation addresses extending a prescribed line bundle, equivalently an R-valued section of a particular Picard component. A finite flat torsor under a nonsmooth group can have no R-valued section. Its absolute tangent space at the special point can also have smaller dimension and smaller tangent-to-base image than those of the group itself.

Thus the passage on p.7 from differing tangent behaviour of two components to contradiction with flatness is invalid. The stronger factorization claim in Remark (1) does not follow from a first-order lifting obstruction either. The displayed ordinary calculation above gives the contrary flatness conclusion, while remaining compatible with the nonzero obstruction for an off-neutral line bundle and with the tangent-space calculation.

I found no remaining defect in (I2)–(I7), nor in the stated ordinary hull, under the stated hypotheses. The supersingular first elliptic factor remains outside this audit.


## Additional targeted check: no abelian lift of the special Picvar

Over R=k[ε]/(ε²), take q12=1+ε, q11=q21=q22=1 and formal translation coordinates z1=z2=1. These parameters satisfy the already audited affine-involution equations, so give an actual ordinary Igusa deformation with flat Picτ. Suppose an abelian subgroup B of Picτ lifted its special Picvar B0=(F0/〈P〉)∨. Pullback to the cover would give f:B→A∨ lifting (0,φ∨), where φ:F0→F0/〈P〉 is the étale degree-two quotient.

The dual isogeny φ∨ has kernel μ2, so its map on the étale Tate module is a unit. Conversely f0∨ kills the E0 étale Tate generator. In Katz’s homomorphism-lifting equation, choose x to generate T2(B0)ét and choose y to be that E0 generator in T2(A0)ét. The left side qB(x,f0∨y) equals 1. The right side is qA∨(f0x,y)=q12 to a 2-adic unit power, hence is 1+ε. This is impossible in R. The contradiction is independent of which elliptic deformation B was proposed. Thus no compatible abelian subgroup lift exists. This does not contradict Picτ flatness: the nonsmooth Picard group need not contain an abelian deformation of its reduced special neutral component. Targeted audit passed and communicated to DGJ and root on 2026-11-20.
