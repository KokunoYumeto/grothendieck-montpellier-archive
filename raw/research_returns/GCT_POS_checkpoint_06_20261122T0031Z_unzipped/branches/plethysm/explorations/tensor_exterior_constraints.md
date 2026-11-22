# Established tensor exterior constraints and the strict-index gate

Date: 2026-11-21. Author/checker: `/root/plethysm_proof`, GPT-6 Astra Pro;
effort not exposed; run GCT_POS.

## Primary source, credit, and reading scope

Briand, E., Orellana, R., & Rosas, M. (2015). Rectangular symmetries for
coefficients of symmetric functions. *The Electronic Journal of
Combinatorics, 22*(3), P3.15. https://doi.org/10.37236/4808

Journal PDF:
https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i3p15/pdf_1/

Read the entire section4, including the proof of Theorem6, Corollary8
and Remark9, printed pp.8–10. Corollary8 states the rectangular complement
identity and vanishing beyond the square boundary; Remark9 supplies
the exterior-algebra interpretation. The paper credits Stembridge's
earlier equation(C.1). Also opened and read all of Stembridge's sectionB
and sectionC through(C.1), pp.2–4 of *Appendix to: Generalized Stability
of Kronecker Coefficients* (14 August2014):
https://dept.math.lsa.umich.edu/~jrs/papers/kron-app.pdf

These identities are established background, not new findings of this run.

## The exact tensor constraint

Write k_n(s)=g((s^n),(s^n),(s^n)), and let U=C^s. Schur–Weyl duality
in the alternating projector gives

\[
\Lambda^{ns}(U^{\otimes3})
 =\bigoplus_{\lambda,\mu,\nu\vdash ns}
  (S_\lambda U\otimes S_\mu U\otimes S_\nu U)^{
   \oplus\dim\operatorname{Hom}_{S_{ns}}
    (\mathrm{sgn},[\lambda]\otimes[\mu]\otimes[\nu])}.
\]

The special-linear invariant summands have
lambda=mu=nu=(n^s). Tensoring all three symmetric-group factors by sign
changes their product by sign, so their alternating multiplicity equals
g((s^n),(s^n),(s^n)). Consequently

\[
k_n(s)=\dim\bigl(\Lambda^{ns}((\mathbb C^s)^{\otimes3})
                   \bigr)^{SL_s^3}
\le {s^3\choose ns}.
\]

The exterior space is zero when n>s². Its top exterior power at n=s²
has dimension1 and is trivial on SL_s³, giving k_(s²)(s)=1.
Exterior duality with respect to this top power yields

\[
k_n(s)=k_{s^2-n}(s)\qquad(0\le n\le s^2),
\]

where k_0(s)=1. This proof uses only the alternating projector and
finite-dimensional duality, and does not infer positivity from divisibility
of the exterior degree by s.

## A concrete feature absent from PNEW014

Take any even m>=4 and set n=m². In the formal construction PNEW014,
S=m. At s=m the auxiliary correction J and both waves vanish, while
Q0(m)=1 and Q(m)=binomial(m+E,E), with E=2binomial(n,3)+1. Hence its
formal tensor coefficient is

\[
 f(m)={m+E\choose E}+3>1=k_{m^2}(m).
\]

Thus PNEW014 does **not** satisfy this stronger exterior constraint.
The exact checker records m=4,6,8, including n=16,s=4. This reinforces
the stated scope of that countermodel: it blocks inference from its listed
structural features, not from all coefficients of the actual tensor ring
or from the full rectangular symmetry array. No repair or enlargement
of the countermodel is attempted here.

## Why this alone does not settle strict PH2 or SH(a)

The displayed bound is for the attained value k_n(s). A strict constituent
test evaluates a polynomial q_(n,r)(x) at an x that need not lie in its
residue class r. Complementation changes n to s²−n as s varies; it does
not identify a constituent of one fixed n with a constituent of another
fixed n. In particular the square-boundary value1 and the zero triangle
n>s² do not bound the constant periodic waves at an off-residue x.

The presently missing step is a uniform estimate transferring these
attained exterior bounds to the negative/off-residue part of every
constituent, or an actual tensor wave-amplitude lower bound that survives
the possible three-primary pole lifts. Neither is proved here. Initial
degree vanishing reaches only s<sqrt(n), a polynomial scale, so it does
not by itself refute a polynomial strict-index bound.

## Local caution in the printed explanatory remark

Remark9's sentence asserting nonzero invariants whenever the exterior
degree is a multiple of dim(U) is too strong. For dim(U)=3 and degree6,
the asserted multiplicity is g((3,3),(3,3),(3,3))=0. The checker computes
this independently as the exact S6 character sum. The correct necessary
divisibility condition and the multiplicity identity suffice for the
argument above; the sufficiency wording is not used. No defect in the
complement identity is inferred from this local sentence.

Certificate:
`../certificates/tensor_exterior_constraints.json`.
Replay: `python deliverables/branches/plethysm/scripts/check_tensor_exterior_constraints.py`.
