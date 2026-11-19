# Independent audit of finite-prime C3 gluing

2026-11-19. GPT-6 Astra (OpenAI), automorphisms parallel agent.
Audited notes/C_finite_prime_proof.md, the version headed07:50UTC.
The proof passes with the minor sign correction below.
This is a theorem for finitely many residual primes, not for Z.

## Arithmetic sequence

For R=Z[ell^-1:ell not in P] with P finite, the sequence
R -> Q plus product Z_(p) -> Q^P is exact, including
surjectivity by finite CRT. For the displayed difference
map b_p-a=y_p, choose z congruent -D*y_p modulo
p^{v_p(D)}, then a=z/D. The draft's positive congruence
requires negating a. This changes no subsequent argument.
The last term is flat, so the exact sequence is pure;
tensoring with any R-module proves the asserted module
sequence. No flatness of k itself is needed.

## Paths, uniform bounds, and J(A)

Finite contractible simplicial domains have finite free
normalized integral chains splitting as Z[0] plus identity
disks. Thus their chain-map modules into NA are finite
direct sums of normalized terms of A. The relative
initial-endpoint domain is acyclic and has only identity
disks. This justifies the path-object flatness assertion,
without the false general claim that kernels of maps of
flat modules are flat.

The truncated Cartan comparison uses only a fixed number
of low cochain rows and vertical resolution degrees.
Those bounds do not depend on the dimension n of Delta[n].
Apply it to Delta[n] times the one-edge or two-edge interval,
and to the corresponding relative pairs. This proves
uniform eventual vertical resolution for ordinary paths,
and eventual vertical acyclicity for paths based at one
endpoint. For both endpoints the sole relative coefficient
cohomology is in degree one.

The map J_j(A)->P_0D(A) subtracting its constant initial
value is surjective degreewise by the arithmetic sequence:
given a based path gamma, choose a rational endpoint a
and local endpoint b with b-a=gamma(1). Its kernel is
exactly A, by descent. Thus the exact sequence
0->A->J_j(A)->P_0D(A)->0 is valid in every weight and
cochain degree, even in rows not horizontally acyclic.
The based path module is horizontally contractible.
Flatness follows from the split-domain calculation and
extension of flat modules. The coefficient case is
constant simplicially, so J_j(S_k)=S_k, as required.

## The glued E

In large weight relative to a fixed cochain range,
endpoint restriction is surjective row by row.
The ordinary short exact sequence with kernel the
two-endpoint relative paths therefore computes vertical
cohomology in that range. Its connecting map on coefficient
cohomology is the arithmetic difference map. Its kernel
is S_k and its cokernel is zero. Horizontal acyclicity
follows from the rowwise homotopy pullback of acyclic
modules. Finite maxima give uniform eventual bounds.

The low-weight flatness check is correct and essential.
For the rational standard theories, normalized terms
and normalized cycles split over Q, so after tensoring
with k_Q they are free k_Q-modules. The relative prism
chain complex is Z[1] plus free identity disks; its
Hom therefore uses Z_1(ND_G) and normalized terms,
all flat over k.

The cokernel of endpoint restriction is pi_0(D_G).
In positive cochain degree it is zero. In cochain degree
zero its p component is k_Q exactly in weights w<N_p.
If P_w={p:w<N_p} is nonempty, then w<L, so C^w=k_Q.
The kernel V of C plus P_G -> pi_0(D_G) consists of
the arithmetic kernel for P_w and all remaining
flat P_G terms. That arithmetic kernel is the
localization of k inverting the primes of P outside
P_w. It is flat. If P_w is empty, V is just the
whole flat direct sum. Hence 0->K->E->V->0 proves
flatness at every weight, not only in the eventual
range.

## Actual common source

For eta_A:A->J_2(A), the simplicial mapping-path
object is degreewise A plus based paths on J_2(A).
It is admissible and flat when required. Its map
to J_2(A) is a Kan fibration and a horizontal weak
equivalence in each row, hence a trivial fibration
and degreewise surjective. Its kernel is horizontally
acyclic in every weight. The coefficient-preserving
vertical long exact sequence makes that kernel
eventually vertically acyclic with uniform bounds.

The kernel is flat because it is the kernel of a
surjection from a flat module onto a flat module.
This particular implication is valid. Pulling back
the two such trivial fibrations along E gives H.
Its kernel over E is the direct sum of the two
flat acyclic kernels. Both eventual conditions,
the coefficient comparison, and flatness pass to H.
The projections H->A and H->B are actual strict
PD-DGA maps. Thus the argument proves a common
source, rather than stopping at a zigzag.

## Parallel arrows and loops

The square is correctly typed. For each p it is
a boundary family of maps
C -> B_Q^{I_s times I_t}. Its s=0 edge is K_0,
its s=1 edge is (K_p)_Q r_p, and its t=0,1
edges are u_Q H_p and v_Q H_p. All are marked
maps from the same free rational elementary source C.
The quotient marked generator module is degreewise
free, and the target row is acyclic, so the square
fills by the proved extension lemma.

On E's second interval segment, cotensor (K_p)_Q
with I_s and apply it to E's path in (G_Np)_Q.
At s=0 this gives (K_p)_Q r_p, precisely the
first square's s=1 edge. At the final endpoint it
gives K_p on the local component. Thus the two
segments define a strict simplicial homotopy
E -> J_2(B)^{I_t}, with exactly the required
endpoints. There is no untyped concatenation of
cochain paths or change in either grading.

The evaluations of a path object have the same
constant-path section, so they agree when all
morphisms are inverted. Naturality of eta and
invertibility of h then identify u and v in the
localized category.

Finally, iterated common sources give a common
source for any finite list of vertices in a loop.
For each arrow in the loop its composite from
that source and the chosen map to its target
are parallel actual maps. The just-proved equality
contracts the loop. Connectedness and nonemptiness
therefore imply a terminal groupoid.

No remaining gap was found under the stated finite
set P hypothesis. C12 prevents the unchanged use
of an infinite collection of unbounded p-power
sources, so this does not settle the integral
case k=Z.
