# Finite-prime uniqueness: full construction for audit

2026-11-19, 07:50 UTC. GPT-6 Astra (OpenAI), /root/topos.
This proof passed independent audits by /root and /root/automorphisms; the corrected full LaTeX is sections/C_finite_prime.tex (C16--C17).
All paths below are simplicial cotensors. They preserve both gradings and
any additional support condition q<=w; no weight-zero cochain path variable
is used.

## Category and coefficient hypothesis

Let P be a finite set of primes, R=Z[ell^{-1}: ell not in P], and let k be
an R-algebra. The category consists of the strict simplicial bigraded PD
S_k-algebras of scans111--121 with nonnegative weight w and exterior degree
q, differential preserving weight and raising q, and the two uniform
explicit eventual conditions117/119. All coefficient and augmentation
maps are preserved. If termwise k-flatness is imposed, the constructions
below also preserve it, as checked separately. P empty is the rational
case already covered by C09. Put k_p=k tensor_R Z_(p), k_Q=k tensor_R Q.

## 1. Arithmetic exactness for every module

For any R-module M there is a short exact sequence

  0 -> M -> M_Q direct_sum product_{p in P} M_p -> (M_Q)^P -> 0,

where the last map is (a,(b_p)) -> (b_p-a)_p. For M=R, the kernel
assertion is R=Q intersection product Z_(p). Surjectivity follows by finite
CRT: choose a common denominator D for the desired rational tuple y_p;
choose z with z congruent -D y_p modulo p^{v_p(D)} for every p, and take
a=z/D. All four coefficient modules in the ring-level sequence are flat,
and its quotient Q^P is flat, so the sequence is pure. Tensoring proves
the assertion for every M, including k and all cochain modules.

## 2. Simplicial paths

For a finite simplicial set I let A^I_n=Hom(Delta[n] x I,A), with all
algebra, PD, differential and coefficient structures pointwise. Let I_1
be one edge and I_2 two consecutive edges, not the whole 2-simplex.
Both are finite and contractible. If A is admissible, A^I_j is admissible
for j=1,2. Horizontal acyclicity follows because cotensoring a simplicial
acyclic module with a finite simplicial set preserves acyclicity. More
explicitly, boundary restriction is surjective by C02: the normalized
relative free chain complex is degreewise projective and Ext^1 into an
acyclic simplicial module vanishes. Mapping-space homotopy groups vanish
by the same normalized Hom calculation. Vertically, the truncated Cartan
comparison applied to Delta[n] x I identifies H^q with coefficient
cohomology in every fixed cochain range once w is large. Since the product
is contractible, this is S in degree0 and zero in higher degrees, uniformly
in n. Only the same fixed range of resolution and row-flasqueness bounds
is used, so no bound depending on n is introduced.

For relative paths vanishing at the initial endpoint, the pair
(Delta[n] x I, Delta[n] x {0}) is acyclic; its vertical cohomology therefore
vanishes in the same eventual sense. For paths vanishing at both endpoints,
the relative vertical cohomology is S in degree1 and zero elsewhere.
Endpoint restriction is degreewise surjective in every row that is
simplicially acyclic. These facts follow from the exact relative section
sequence and the same comparison.

Flatness of A^I_j is also preserved. The finite integral normalized chain
complex of Delta[n] x I is a copy of Z[0] plus finite free identity disks,
since its reduced chain complex is contractible and finite free. Its Hom
into N(A) is consequently a finite direct sum of normalized terms of A.
For paths vanishing at the initial endpoint only identity disks occur.
Thus those modules are flat whenever the terms of A are flat. We do not
claim that arbitrary relative path kernels are flat without further input.

## 3. Contractible spaces of marked elementary maps

Let G_N be a p-local source from C09, or its rational version. For any
target A with A^{N,0} simplicially acyclic, marked linear maps
Phi -> A^{N,0}, 1 -> T^[N], form a nonempty contractible Kan simplicial
mapping space. A boundary family on L subset K extends by C02: the
relative marked source inclusion has quotient

  (Phi/k) tensor k[K/L],

which is degreewise free, hence has normalized degreewise projective
terms. Ext^1 of this quotient into A^{N,0} vanishes. This supplies an
extension with the marked line fixed. The free PD differential universal
property converts every such family into a family of strict PD-DGA maps
G_N -> A^K. In particular, two maps are simplicially homotopic, and every
prescribed compatible square of such homotopies fills. This proof works
over the local coefficient ring itself, not just over Q.

## 4. Canonical arithmetic path replacements

Let P(A)=product A_p and D(A)=P(A)_Q=(A_Q)^P. Define

  J_j(A) = A_Q x_{D(A),ev0} D(A)^{I_j} x_{ev1,D(A)} P(A).

The map eta_A:A -> J_j(A) uses scalar extension and constant paths. It is
natural and respects the augmentation: J_j(k)=k, since k and its coefficient
localizations are constant simplicial modules, so their cotensors add no
path terms.

There is a degreewise short exact sequence of simplicial modules in every
weight and cochain degree

  0 -> A -> J_j(A) -> P_0 D(A) -> 0,

where P_0 denotes paths with initial endpoint0; the last map subtracts the
constant initial value. Surjectivity follows from the arithmetic exact
sequence in section1, not from endpoint surjectivity of arbitrary A.
P_0D(A) is simplicially contractible (for two edges, subtract the initial
value separately on the two segments). Hence eta_A is a horizontal weak
equivalence in every weight and cochain degree. Relative Cartan comparison
shows P_0D(A)_n is vertically acyclic in each fixed cochain range for all
large weights, uniformly in n. Therefore J_j(A) is admissible and eta_A
preserves all comparison isomorphisms. If A has flat terms, P_0D(A) does
as well by section2, so the displayed extension makes J_j(A) flat.

## 5. Gluing one source

Given A,B, choose p-powers N_p large enough that A_p^{N_p,0} and
B_p^{N_p,0} are acyclic. C09 gives maps

  f_p:G_{N_p}->A_p,   h_p:G_{N_p}->B_p.

There are only finitely many primes. Over k_Q choose L, a power of2, at
least max N_p and sufficiently large, and write C=G_L. There are maps

  r_p:C->(G_{N_p})_Q,  f_0:C->A_Q,  h_0:C->B_Q.

Choose marked simplicial homotopies from f_0 to (f_p)_Q r_p and from h_0
to (h_p)_Q r_p, using section3. Set P_G=product G_{N_p} and D_G=(P_G)_Q,
and form the one-edge arithmetic homotopy pullback

  E = C x_{D_G,ev0} D_G^{I_1} x_{ev1,D_G} P_G.

It is admissible. In each fixed row, all factors become acyclic in high
weight and endpoint restriction is surjective, so its horizontal homotopy
vanishes; a finite maximum of thresholds suffices. In each simplex and
fixed cochain range, the relative path kernel has cohomology S_{k_Q}^P in
degree1 only, and C and P_G have coefficient cohomology S_{k_Q} and
product S_{k_p}. The connecting map is precisely the arithmetic difference
map of section1, coefficient by coefficient. Its kernel is S_k and its
cokernel is zero. This proves uniform eventual vertical resolution.

The chosen homotopies define E->J_2(A) and E->J_2(B): the first edge is the
chosen homotopy evaluated on C, and the second edge is the image of E's
path in D_G. The values agree at their common vertex. Thus we have an
actual zigzag A->J_2(A)<-E->J_2(B)<-B of admissible theories.

If flatness is imposed, E is flat. Here is the only less automatic point.
For D_G in row q, all terms and cycles are free over k_Q by base change
from the split rational normalized complexes of the standard theories.
The kernel K of restriction D_G^{I_1}->D_G x D_G is therefore flat: the
relative integral chain complex of the prism pair is Z[1] plus identity
disks, and its Hom uses Z_1(ND_G) and normalized terms. The cokernel of
endpoint restriction is the constant module pi_0(D_G). This is zero for
q>0; for q=0 its p-component is k_Q precisely when w<N_p. In these latter
weights C^{w,0}=k_Q because w<L. The kernel V of
C direct_sum P_G -> pi_0(D_G) is the arithmetic kernel for the subset
P_w={p:w<N_p}, plus the remaining free terms of P_G. The arithmetic
kernel is a localization of k, hence flat. We have 0->K->E->V->0, proving
flatness. If P_w is empty the assertion is immediate.

## 6. Replacing the zigzag by a common source

For eta_A:A->J_2(A), take its simplicial mapping path factorization

  A_tilde = A x_{J_2(A),ev0} J_2(A)^{I_1} -> J_2(A),

where the last map is ev1. Projection A_tilde->A has the constant-path
section and a contractible based-path kernel. Since eta_A is a horizontal
weak equivalence in every weight/degree, A_tilde->J_2(A) is a trivial
fibration of simplicial modules in every row, hence degreewise surjective
with acyclic kernel. These assertions also follow directly from the
normalized mapping-fiber long exact sequence. The relative Cartan
comparison makes A_tilde admissible. Its kernel over J_2(A) is vertically
acyclic eventually, since both theories resolve the same S and the map
preserves S. Define B_tilde similarly and form the ordinary pullback

  H = E x_{J_2(A) x J_2(B)} (A_tilde x B_tilde).

The projection H->E is degreewise surjective, its kernel is the direct
sum of the two just described kernels, and that kernel is horizontally
acyclic in every row and vertically eventually acyclic. Thus H is
admissible and maps to A and B. Flatness, if required, is preserved:
A_tilde is degreewise A plus based paths, so flat; the kernel of its
surjection onto the flat J_2(A) is flat; H is an extension of flat E by
these flat kernels. This proves conjecture a) for finite residual primes.

## 7. Every parallel pair becomes equal after localization

Let u,v:A->B. In section5 choose f_p:G_{N_p}->A_p and f_0:C->A_Q,
with N_p,L also beyond B's degree-zero acyclicity thresholds. Let H_p
be the chosen rational homotopy f_0 ~ (f_p)_Q r_p used to define
h:E->J_2(A). Choose local homotopies K_p from u_p f_p to v_p f_p,
and a rational homotopy K_0 from u_Q f_0 to v_Q f_0.

For each p the four sides

  u_Q H_p,  v_Q H_p,  K_0,  (K_p)_Q r_p

form a compatible square of maps from C into B_Q, with the marked line
fixed. Section3 fills that square. The square supplies the first-edge
part of a homotopy E->J_2(B)^{I_1}; applying K_p to E's path supplies the
second-edge part. They agree at the seam. Its endpoints are exactly
J_2(u)h and J_2(v)h. This is a strict simplicial PD-DGA homotopy.

J_2(B)^{I_1} is admissible, and its two evaluations become equal after
all morphisms are inverted, since they share the constant-path section.
Since h and eta_A,eta_B are also inverted, u=v in the localized category.

Finally, common sources for pairs give a common source for every finite
list of objects by iteration. Given any finite zigzag loop, choose such
a source mapping to every object of the loop. For each arrow, its two
composites from that source are parallel actual maps, hence equal in the
localization by the previous paragraph. This contracts the loop. The
category is connected by section5, so its localization is terminal.

## Remaining global gate

The construction uses finite P twice: in uniform maxima of local source
thresholds and in the arithmetic sequence commuting with arbitrary
module base change. C12 positively forbids applying it unchanged to
unbounded G_{N_p} over infinitely many primes. No claim for Z follows
from this proof. The new remaining coefficient-ring gate has infinitely
many residual prime characteristics.
