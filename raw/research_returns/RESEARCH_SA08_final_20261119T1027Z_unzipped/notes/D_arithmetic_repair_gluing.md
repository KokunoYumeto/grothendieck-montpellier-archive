# C30: conditional arithmetic common-source reduction

2026-11-19, GPT-6 Astra (OpenAI), agent /root/shadows_coalgebras.

Full proof: `sections/D_arithmetic_repair_gluing.tex`.

## Exact hypothesis and conclusion

Start with C21's common partial model P->A,B. Suppose for every prime p
there is an admissible p-local repair P_p->E_p->A_p,B_p whose first map
is an actual isomorphism in all form degrees below d_p, in every weight
and simplex, and d_p tends to infinity. Then there is a global admissible
common source H->A,B. This proves common-source existence/connectivity
under the repair hypothesis. It does not assert the repairs exist and
does not trivialize loops in the localized category.

The core statement permits arbitrary k without optional flatness.
For k=Z, flat local repairs and targets yield a flat common source.
Optional flatness over arbitrary k needs additional control and is not
claimed. The support condition q<=w is preserved.

## Arithmetic algebra, without an infinite product of cochain modules

Let R=product_p Z_(p) and R_Q=R tensor Q. The sequence

    0 -> Z -> Q direct_sum R -> R_Q -> 0

is exact and pure. A denominator D of an element of R_Q has only
finitely many prime factors; finite CRT supplies a rational a such
that the difference lies in R. The kernel is the intersection of all
Z_(p) inside Q. The quotient is Q-linear, hence Z-flat, proving purity.
Thus tensoring with *any* module preserves exactness. In particular,
M_R means M tensor R, not product_p M_p.

For each form degree q choose the finite set
F_q={p:d_p<=q} union {p:p<=q+2}. Define E_R^q by finite idempotent
gluing: its p-components for p in F_q are E_p^q, and its complementary
component is (1-e_Fq) P_R^q. Enlarging F_q changes nothing because
new components lie in a degree where P_p->E_p is an isomorphism.
Use a common finite refinement to define d, products, divided powers,
simplicial operators, augmentation, and maps to A_R,B_R.

In each fixed form range only finitely many local repairs occur.
Outside that finite set the product ring inverts C21's factorial, so
P already resolves the coefficients in the required vertical range.
Finite maxima of local bounds give both uniform eventual axioms.
This is an actual admissible R_k-theory, not merely a family of objects.

## Two-region path gluing and actual maps

P_Q is admissible and maps to (E_R)_Q. Form the one-edge arithmetic
path pullback of P_Q and E_R over (E_R)_Q. The interval-path comparison
C16 and the pure arithmetic exact sequence prove admissibility. The
coefficient connecting map is exactly the arithmetic difference map,
so its kernel is S_k and its cokernel vanishes.

For each original target C use the canonical arithmetic path replacement
J(C)=C_Q x (C_RQ)^I x C_R. There is a rowwise exact sequence
0->C->J(C)->P_0(C_RQ)->0. Arithmetic purity, not endpoint-surjectivity
of an arbitrary row, proves the last surjection. Thus C->J(C) is a
horizontal weak equivalence in every row and an eventual vertical
equivalence. The endpoint diagrams commute strictly because the local
repair maps extend those of P, giving E->J(A),J(B).

The simplicial mapping-path factorizations of A->J(A) and B->J(B)
are trivial fibrations row by row. Pulling them back along E gives
an actual admissible H with maps H->A,B. This is the finite-prime
common-source step of C17 with the new pure two-region arithmetic
square; the special elementary-source homotopy argument used for
loops in C17 is deliberately not imported.

## Remaining construction gate

The remaining required object is a p-local repair *of C21's entire
partial model*, retaining low degrees and its maps to both targets.
C18's isolated disk closure and C24's conditional bar pushout do not
yet provide its source boundary maps. A rational quasi-isomorphism,
agreement only on cohomology, or separate unbounded sources G_Np do
not satisfy the stated hypothesis. The low-degree agreement is what
makes the finite idempotent construction uniform.
