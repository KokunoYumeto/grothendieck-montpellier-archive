## I.6 — Proved: residual columns are exact after closing images

Let R be a regular noetherian local ring of dimension d, p a nonmaximal prime of height h, and K_R its residual resolution. Give each Hom_R(E_p,K_R^j) the finite topology and use postcomposition with the residual differential. Then for j>h,

    closure(im[Hom(E_p,K_R^{j−1})→Hom(E_p,K_R^j)])
      = ker[Hom(E_p,K_R^j)→Hom(E_p,K_R^{j+1})].

At j=h the kernel is zero. In particular the last differential has dense image. This is a precise statement about relations among operators in the actual endomorphism algebra; it does not identify the closed two-sided ideal in an independently completed free algebra.

**Proof.** The differential is continuous, so the closure of the image is contained in the kernel. For the converse let f:E_p→K_R^j be a cycle and fix a finite set of inputs. By the cyclic generalized-fraction construction in I.4, these inputs lie in N=Re for e=e_n/u, and I=Ann_R(e) is p-primary with I R_p=(x_1^n,...,x_h^n). The module

    M=Ext_R^j(R/I,R)

is finite over R. Its localization at p is zero for j>h, because R_p/I R_p has the length-h Koszul free resolution. Consequently some v∈R\p annihilates all of M.

The element e/v is defined in E_p and has the same annihilator I as e. The restriction of f to R(e/v), identified with R/I, is a cycle in Hom_R(R/I,K_R). Restriction to Re multiplies its cohomology class by v, since f(e)=v f(e/v). That class is zero because vM=0. Therefore there is a map b:Re→K_R^{j−1} whose differential equals f on Re.

The cyclic source Re is finitely generated, so b has only finitely many nonzero component maps into the summands E_r of K_R^{j−1}. Extend each such component to E_p by injectivity of E_r, and sum the finitely many extensions to obtain g:E_p→K_R^{j−1}. Its differential agrees with f on all the prescribed inputs. Thus every finite neighborhood of f meets the image, proving the asserted equality.

For j=h, only the summand E_p can receive a map from E_p among height-h primes. Hence this Hom group is T=ÂR_p. Choose any prime r immediately above p and contained in the maximal ideal. Proposition I.4 says c↦δ_pr c is injective, so the next differential has zero kernel on T. ∎

For a height-gap-two interval p⊂q, apply this with R=A_q and j=h+1. It says that the kernel of postcomposition from the full adjacent-arrow family to Hom(E_p,E_q) is the closure of the family obtained by precomposing the residual differential with an element of ÂA_p. Thus the quadratic relation controls this particular kernel after passing to the actual Hom topologies. The additional quotient-topology and universal-map continuity problem remains: it is not legitimate to conclude that the same closure is obtained inside every candidate completed free algebra.
