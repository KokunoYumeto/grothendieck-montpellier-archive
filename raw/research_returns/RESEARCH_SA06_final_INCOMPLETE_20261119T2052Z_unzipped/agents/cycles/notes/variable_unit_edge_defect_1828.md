# Variable-unit edge families: endpoint calculation and the remaining norm kernel

19 November 2026, 18:28 UTC research note, `/root/cycles`. This is an unregistered analysis of the parent’s proposed variable-unit construction. The local Dennis–Stein calculation and the norm-versus-intrinsic-defect distinction have been independently checked conceptually by `/root/frobenius`. A full independent global-descent audit has not been completed. No new coherent SNC family theorem, ordinary quotient vanishing, or surviving Chow class is claimed.

## 1. The proposed proper parameter

Let C be a smooth connected proper curve over an algebraically closed field k of positive characteristic, with base point c0. Fix a degree-zero line bundle L and a unit u. Cases L=O or u=1 give a zero edge class and may be omitted. Choose a smooth connected proper parameter curve A in Jac(C) through 0 and L, and write a0,a1 for those points. Let the normalized Poincaré bundle on C times A be M, trivial along C times a0 and c0 times A.

For sufficiently large n, Riemann–Roch supplies rational functions h on A with their only pole at a0 and with

    h(a1)=(u−1)^2/u.

One can impose a simple zero away from a0,a1 simultaneously by the usual prescribed-value and first-jet open conditions in a large linear system. Normalize the double cover

    g^2−(h+2)g+1=0

to obtain f:P→A. A simple zero of h makes the quadratic irreducible and separable: in odd characteristic the discriminant h(h+4) has odd valuation there; in characteristic two, after changing variable, the equation is an Artin–Schreier equation with right side 1/h and an odd pole. Thus P is a smooth connected proper curve. The field norm of g is 1. Every zero or pole of g lies over a0, because both roots are units wherever h is finite. At a point t over a1 one has g(t)=u. The pulled-back bundle M_P is trivial on every C-fibre above a0.

These statements concern an actual proper cover; an affine parameter is not being used as an ordinary-family substitute.

## 2. Localization provides an extension, but endpoint values need a calculation

Let B be the finite support of the zeros and poles of g, and U=P minus B. On C times U there is the actual class

    xi_U = g · ([M_P]−1) in K1(C times U)_Q.

Its localization boundary at p in B is ord_p(g) times ([M_P,p]−1), which is zero since M_P,p is trivial. Thus the regular closed-fibre localization sequence supplies an extension to K1(C times P)_Q.

Different extensions differ by pushforwards of K1(C) from the boundary fibres. Their pullbacks to any parameter fibre are zero: different fibres are disjoint, and self-intersection on the same fibre multiplies by lambda_−1 of its trivial normal line, namely zero. Thus the endpoint values do not depend on the chosen extension. This does not, by itself, say what those boundary endpoint values are.

The needed local calculation is explicit. Near p, choose a parameter t and write g=t^m v with v a unit. Using the given trivialization of M_P on C times p, its transition units can be written f_ij=1+t h_ij. On the punctured overlap, the degree-two Čech cup is

    {g,f_ij}=m{t,1+t h_ij}+{v,1+t h_ij}.

With Weibel’s sign convention, {t,1+t h_ij} extends as the Dennis–Stein symbol <t,−h_ij>. Its specialization at t=0 is <0,−h_ij>=0, while the second term specializes as {v,1}=0. Equality of the extended cocycles follows from the unramified K2 sheaf on the regular local overlaps. This establishes the local zero-specialization calculation; zero tame residue alone would not establish it.

For a fully global K1 formulation, take the weight-two part of the extension and subtract the pullback of its restriction along c0 times P. The boundary support ambiguity of weight two comes from the weight-one part of K1(C), namely constant units, and this normalization removes it. The higher coniveau contribution on the regular surface has weight three and cannot alter a weight-two endpoint on a curve. The expected resulting normalized class has endpoint zero above a0 and u([L]−1) at t. This paragraph records the exact descent/weight normalization to be independently audited, rather than silently replacing it by an arbitrary extension or by an unsupported Čech-to-K1 assertion.

## 3. The vertex restriction is a class on P, not its norm on A

Fix a marked point q on C. Its Poincaré evaluation is a degree-zero line bundle N_A on A, normalized at a0; its pullback is N=f^*N_A. Choose a rational section of N_A, normalized to value 1 at a0, whose divisor D_A=sum n_x[x] avoids a0 and the finitely many branch points. This is possible by the ordinary moving/Riemann–Roch argument on a curve. The normalized extension has the following expected weight-two vertex class, equivalently the Gersten representative of the cup just computed:

    eta_N = sum_x n_x sum_(y over x) g(y) [O_y] in SK1(P)_Q.

The normalization at a0 matters: changing an unnormalized boundary trivialization can add boundary point-unit terms. Constant-along-edge corrections remove such common base-point terms, but they cannot be discarded in an unnormalized formula.

Pushforward along f gives

    f_*(eta_N)=sum_x n_x Norm(g)(x) [O_x]=0.

This is the projection formula and Norm(g)=1. It proves that eta_N lies in the kernel of f_*:SK1(P)_Q→SK1(A)_Q. It does not prove eta_N=0. Away from branch points the two roots are g and g^−1, so the individual contribution has the form

    g(y)([O_y]−[O_iota(y)]),

which is a Prym-type point difference times a unit. The pushforward kills this antisymmetric expression automatically. No injectivity of that pushforward has been proved.

In the SNC totalization, the vertex condition is zero in K1(P)_Q itself. A vanishing pushforward to A cannot replace that condition. Pairing the vertex defects against a dual two-cycle produces the same formula with N_A equal to the Poincaré evaluation at the signed triple-point period. The common constant-along-edge corrections pair to zero. Thus nonzero periods are replaced by genuine SK1(P) norm-kernel questions; they are not removed by the norm computation.

## 4. Why two immediate repairs do not follow

Passing to another finite cover does not automatically erase a rational class: pullback followed by pushforward is multiplication by its nonzero degree, so rational pullback is injective. Pushing the parameter family back along f also does not isolate the desired endpoint; it sums both roots u and u^−1 and cancels the desired edge value along with the vertex norm.

An elliptic-isogeny parameter would be a narrower possibility. If f is an elliptic isogeny, torsion translations are expected to act trivially on the rational motive, making the norm injective on the relevant invariant group. But constructing a unit g with divisor supported over a0 and prescribed independent endpoint data is then an additional restriction. In particular, for a constant elliptic curve over the algebraic closure of a finite field, such torsion-supported divisors and their functions are constant-field data up to scalar and finite normalization. They do not freely realize an arbitrary independent pair (L,u). This is a sibling-proposed research observation, not a freshly source-audited result in this note.

## 5. Exact source scope and current limit

Freshly opened Weibel’s author-hosted Chapter III, https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf, and read Definition5.11, the identity <r,s>={r,1−rs} when r is a unit, and relations D1–D3 on printed43–44. The local zero specialization also follows directly from the displayed defining Steinberg-group word. The chapter cites the presentation theorem; this note does not claim to have opened the original Dennis–Stein article or independently proved that presentation theorem.

The complete Quillen localization/projection inputs were freshly read in the immediately preceding C.3br audit: §7 Proposition2.10 and Proposition3.2(3.3), with proofs. The existing arbitrary-scheme Adams and regular Gersten source chain is retained in the C.3bq/C.3br source ledgers. No new theorem claiming norm injectivity, arbitrary proper-family lifting, or vanishing of SK1 has been found or imported.

**Remaining precise issue:** determine whether the normalized vertex classes eta_N can be killed by actual endpoint-zero edge or component perfect families while preserving the prescribed u([L]−1) endpoint. The current norm-one cover alone does not do this. No status row or main-gate movement is attached to this note.


## Supersession after the complete C.3bt proof

The norm-only obstruction recorded above is retained as a failed method, but the particular marked restriction problem is resolved by C.3bt. Its additional interpolation forces h to vanish at every chosen section-divisor support, hence g=1 pointwise there. Thus the restrictions vanish themselves; no norm injectivity is asserted. The full proof and receipts are retained in the sibling C.3bt files.
