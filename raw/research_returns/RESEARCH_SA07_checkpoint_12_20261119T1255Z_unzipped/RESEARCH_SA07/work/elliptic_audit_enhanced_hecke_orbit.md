# Independent targeted audit: enhanced degree-one Hecke orbit

Input: work/H1_Hecke_enhanced_orbit_audit.md, Sections1--4 and the
explicit comparison map in Section6. Audited19November2026 around12:49UTC.
Verdict: **pass after the sign/coframe correction now incorporated**.
The Orr/Gao full theorem proofs are not independently re-proved here.

1. The retained Movasati primary arXiv0806.3926v1, Section2 p4 and
   Proposition2/proof p7, was independently reopened. The period map has
   cycles as rows, forms as columns and a common factor1/sqrt(2pi i).
   The explicit nonzero derivative determinant proves local biholomorphy
   in four variables. The identity F0=det(x)^(-1) identifies the t0=1
   slice with determinant1 in normalized matrices. Transposing and
   multiplying by sqrt(2pi i) therefore gives the framed threefold's
   local period chart with determinant2pi i, exactly as used.

2. For M in SL2(Q), Lambda_M=omega M Z^2 has the same area as Lambda.
   Choosing q with qLambda subset Lambda_M makes [u]->[qu] an actual
   isogeny phi of degreeq^2. It is algebraic for an algebraic E because
   its kernel q^(-1)Lambda_M/Lambda is a finite torsion subgroup; the
   quotient differential and the subsequent rational scaling byq are
   both algebraic. The element phi/q in Hom tensorQ has degree1 and
   invertible algebraic de Rham pullback. Cup products multiply by1
   after this rational scaling, so its inverse transport preserves the
   symplectic frame.

3. The period formula PM can also be checked without describing the
   quasi-isogeny as a holomorphic map. In the chosen integral bases,
   phi_* on homology has matrix A=qM^(-1), which is integral by the
   choice of q. If Q is the target period matrix with forms as rows,
   the period matrix of phi^* target forms is QA=qQM^(-1). The
   pullback condition for phi/q gives QM^(-1)=P, hence Q=PM.
   This establishes the exact matrix and its inverse-pullback direction.
   G_K transports the actual phi and the algebraic forms; no step
   commutes a Galois element with analytic complex conjugation.

4. Any algebraic Z containing this whole orbit pulls back in the
   local period chart to holomorphic equations vanishing at PM for
   rational M nearI. The coordinate parametrization
   (a,b,c)->[[a,b],[c,(1+bc)/a]] gives density of rational matrices
   in a real open subset of SL2(R). Successive one-variable identity
   theorems make each holomorphic equation vanish on the complex
   neighbourhood. Since M->PM identifies SL2(C) with the fixed
   determinant hypersurface, Z contains an analytic open subset of
   the irreducible framed threefold and therefore equals the whole
   threefold. No unproved orbit-classification theorem enters.

5. The original draft used positive quasiperiods for the class xi.
   This is corrected: our fixed xi=x dx/y has periods -eta_i, so
   eta_frame=xi+h omega has row r=-c conjugate(omega). The determinant
   is2pi i and the t0=1 slice is preserved. For real M of determinant1,
   rM=-c conjugate(omega M) and the area/c are unchanged. Therefore
   these target frames remain the actual Hodge frames. The real-linear
   map x->r x fromR^2 toC is invertible; rM=r forces each column of
   M-I to vanish. Integral re-marking changes only the chosen cycles
   and does not create a distinct framed point on the fixed-period
   leaf. This proves the stated fixed-period assertion.

6. The universal-extension tangent map in Section6 is now explicitly
   written in coordinates dual to(omega,-xi), whose period matrix
   has second row positive eta_i. The inverse image of s=h u is
   (eta1-h omega1)z1+(eta2-h omega2)z2=0, hence
   z1+conjugate(tau)z2=0. This algebraic-line test is correct because
   the first coefficient is nonzero; its projective coordinate is
   conjugate(tau). No Betti-algebraicity follows from algebraic h in
   the other named coframe without this additional coordinate.

7. Scope: the entire enhanced degree-one rational quasi-isogeny orbit
   has full Zariski closure for every complex starting point. This
   rules out the particular proposed proper locus containing the
   entire orbit. It does not rule out a specially selected suborbit
   on a further algebraic locus, and it supplies no transcendence of
   the nonzero h at E_star. No main-gate movement is inferred.

Own opened primary refs: turn379214889view0--2, original full20-page
Movasati2008v1; PDFpage7 visual request turn442013928view0. The exact
mathematical determinant/cycle map was read in extracted primary text.
