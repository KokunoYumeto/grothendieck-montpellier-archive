# AI-8. Exact all-CM Artin image by transfer and a totally real enlargement

Proved work argument; independent audits requested. Keep included TeX
unchanged during CP06 compile/QA.

## 1. The immediate imaginary-quadratic corollary

Let sigma in Gamma_Qcm admit a comparison on the full geometric
CM/Artin diagram. E.2.20 makes its common local scalar one global
sign, which can be absorbed in the global weight sign.
For an imaginary-quadratic K, choose an elliptic CM object with
identity type and one finite K-idele s representing sigma|K^ab.
The exact E.2.20d equation is lambda s in K^times.
Thus s is a principal finite idele. Its Artin action is trivial:
the missing infinite component lies in C^times, which is connected
and has trivial Artin image. Therefore sigma fixes K^ab pointwise.
This proves ray-field fixation by the actual reciprocity map;
no inference from ring-class fields alone is used.

## 2. The two-type consequence over any Galois CM field F(i)

Let F/Q be finite, totally real and Galois, and put L=F(i).
For an arbitrary finite L-idele s with
Art_L(s)=sigma|L^ab, the two CM-type comparisons of E.2.20
give

    s=b t,  b in L^times, t in A_f,F^times.              (1)

Indeed flip the identity/conjugate pair, obtain s/c(s) in
L^times, and use the explicit Hilbert-90 element already
proved there. The principal factor b has trivial Artin
image because L is totally imaginary. Hence

    sigma|L^ab = Art_L(j_F^L(t)),

where j_F^L is extension of finite ideles. This step
does not itself say that t has trivial Artin action.

## 3. A finite target and its exact transfer quotient

Fix an arbitrary finite abelian extension M/L inside Qbar.
Define the continuous homomorphism

    v_M: Gamma_F^ab --Ver_{F->L}--> Gamma_L^ab
                         --res_M--> Gal(M/L).           (2)

Here Gamma_L is the index-two open subgroup of Gamma_F.
The transfer is the actual finite-index group transfer,
not restriction. Its compatibility with extension of
ideles is

    Art_L(j_F^L(u)) = Ver_{F->L}(Art_F(u)).              (3)

Milne CFT2020 Chapter V Section3, Proposition3.18 and its
following Artin diagram, printedp162, gives the finite
Galois/ideal formula. Passing to the inverse limit gives
(3). Equivalently, for each finite target, use an ideal
representative prime to its modulus; weak approximation
and the principal-idele relation turn the ideal formula
into the stated finite-idele formula.

For every real embedding tau:F->R, choose its actual
complex conjugation c_tau in Gamma_F. It has order two
and lies outside Gamma_L, since i becomes nonreal at
every embedding of F. Compute its transfer using the
coset representatives 1,c_tau:

    Ver_{F->L}(c_tau)=c_tau^2=1 in Gamma_L^ab.          (4)

This is an exact coset computation. It does not require
that M/F be Galois or that conjugation act by inversion
on Gal(M/L).

The finite quotient v_M defines a finite abelian
extension N/F by

    Gamma_N^ab-preimage = ker(v_M) inside Gamma_F.

More plainly, N is the fixed field of the inverse
image of ker(v_M) under Gamma_F->Gamma_F^ab; its Galois
group is im(v_M). By (4), the conjugation at EVERY real
place acts trivially on N. Thus every embedding of N
is real, and N is totally real.

This is the essential finite enlargement: the class
field of the transfer quotient is totally real.
No statement identifying M with a CM division field
is used.

## 4. Enlarge the real field, then use the CM equation again

Choose a finite totally real Galois field F'/Q containing
F and N, for example the normal closure of N over Q.
Its normal closure is totally real because every
conjugate of a totally real algebraic number is real.
Put L'=F'(i). Then L'/Q is Galois and CM, contains L,
and

    L intersection F'=F,
    [L':L]=[F':F].

Use the CM/Artin comparison on the two types of L'
to choose a finite L'-idele s' representing sigma|L'^ab
and write, by (1) at this larger field,

    s'=b' t',  b' in L'^times, t' in A_f,F'^times.

Norm compatibility with Artin maps gives

    sigma|L^ab
      =Art_L(Norm_{L'/L}(s'))
      =Art_L(j_F^L(Norm_{F'/F}(t'))).                  (5)

The first equality uses the actual field inclusion
L^ab L' subset L'^ab, because abelian extensions
remain abelian after base change. The second uses
triviality of principal finite ideles in the CM field
L and the exact norm identity

    Norm_{L'/L}(t')=j_F^L(Norm_{F'/F}(t')).

That identity follows from linear disjointness of
L=F(i) and the totally real extension F' over F,
or directly from extension of scalars in the
determinant defining the field norm.

Put a=Art_F(Norm_{F'/F}(t')). A second application of
the norm/restriction diagram makes a trivial on N,
since N subset F' and Art_F'(t') fixes its base field
F'. Therefore a lies in ker(v_M). Equations (2),
(3) and (5) now give

    sigma|M=v_M(a)=1.

Since M/L was arbitrary finite abelian, sigma fixes
L^ab pointwise.

## 5. All CM fields and the exact diagram image

Let K be any finite CM field. Its normal closure
is CM; adjoining i still gives a finite Galois CM
field L. With F=L^+, one has L=F(i), and F/Q is
Galois and totally real. The previous argument
makes sigma trivial on L^ab.

The composite K^ab L/L is abelian, hence lies in
L^ab. Thus sigma fixes K^ab. Varying K proves

    sigma in Gamma_Fcm,

where Fcm is the compositum of K^ab over all finite
CM fields K.

Conversely E.2.6 constructs one actual integral
CM/Artin comparison for every sigma in Gamma_Fcm,
using the exact main CM theorem with idele1,
the Tate-integral quasi-isogeny argument, exterior
cohomology, all labelled correspondence/projector
maps and all finite-model Artin blocks.
Actual complex conjugation supplies the other coset.
Consequently the Artin image of the complete
geometric CM/Artin integral diagram is exactly

    Gamma_Fcm disjoint-union c Gamma_Fcm.             (6)

The Artin kernel is the global weight sign, by the
same all-cyclic-quotient and product argument as
E.2.15, carried out inside CM abelian varieties.
Each fibre has exactly two elements.

Restriction from the full geometric abelian diagram
therefore gives

    I_ab = Sigma_Fcm disjoint-union c Sigma_Fcm,
    Sigma_Fcm = {sigma in Gamma_Fcm:
      rho_A(sigma)(Lambda_A)=Lambda_{sigma A}
      for EVERY abelian variety A/Qbar}.             (7)

Necessity combines (6) with E.2.16; sufficiency is
exactly E.2.16. This identifies the CM part of the
remaining Artin condition without equating a
reflex-generated division field and K^ab.

The existing quartic construction E.2.6 already has
swapping elements of Gamma_Fcm, so (6) alone does
not decide the full-abelian integrality condition
in (7), the quartic place-pair, or extension to
all pure motives.

## 6. Source and proof checks

2026-11-19: re-opened Milne CFT2020 complete author
PDF and read ChapterV Proposition3.18 and adjoining
Artin diagram, printedp162, exact web reference
turn162187549view1. The passage to finite ideles
is supplied above via finite targets and ideal
representatives; the norm/restriction diagram
is the previously opened PropositionV.5.2 and
following diagram, p178, with TheoremV.5.3 pp178-179.
Two-type formulas, model existence and exact
quasi-isogeny normalization were independently
checked for E.2.20 in Milne CM2020.

Root and elliptic_splitting were asked to independently
attack the finite transfer quotient N, its total
reality, and the norm from F' construction. No
independent-audit completion is claimed here yet.

## 7. Completed independent audits and canonical dependencies

Canonical result E.2.21. Root and elliptic_splitting independently
passed the complete proof, including their own primary CFT source
opening. Integrated after CP06 save. Fprime may be chosen as the
normal closure of N/Q; since F/Q is Galois, Fprime/F is a compositum
of conjugate abelian extensions and hence is itself abelian.
Dependencies: E.2.3 actual Artin-block descent; E.2.5 and E.2.15
uniform CM restriction; E.2.9 and E.2.14 common projective scalar
inside CM quotients; E.2.20 two-type Hilbert90 equations; E.2.6
CM converse; E.2.16 all-abelian lattice sufficiency. Sources:
GenMilneCM2020 and GenMilneCFT2020. E.2.21 does not depend on
any equality of a CM division field with all K^ab.
