# Uniform trace exclusion: what is now reduced, and what remains

Date: 2026-11-21. `/root/vandiver_k`, GPT-6 Astra Pro; effort not exposed;
run K17. The arithmetic implications below retain the stipulated source.

## 1. The source reduction is stronger than one-prime separation

The complete proof in `joint_trace_section.tex`, K17-S17-JOINT, shows

\[
 V_{\rm len}\ne0\quad\Longrightarrow\quad
 \exists\rho\in\mathrm{Adm3U\_s}\cup\mathrm{Adm2A}\quad
 \operatorname{tr}\bar\rho=\bar\Psi+1+\bar\Psi^{-1}
 \text{ on every element of }G_E.
\]

One point supplies every congruence simultaneously. This removes the need
to find one Frobenius element that separates every admissible form at once.
The parent and archive agent have independently reviewed this theorem; the
source manifest records the exact fixed commit and full-reading scope.

For each fixed even e and coefficient prime l, the same strict negative
Selmer group with N=2 and psi=1 is tested by each imaginary quadratic E
satisfying the source datum GD. Consequently a nonzero group forces such a
residual Eisenstein representation for every permitted E. To prove
vanishing, it suffices to find one E for which neither admissible branch
contains one. This is a sufficient criterion, not an equivalence: the proof
does not construct a Selmer class from an arbitrary automorphic congruence.

The actual full-space packet and local-level comparisons remain necessary
when choosing E. They have been checked for the two fields used in the
existing finite certificates. Merely changing E in a numerical formula is
not a coverage proof.

## 2. Exact finite detection, without a prime-size bound

Here is a useful purely linear-algebra consequence. Let W be a vector space
of dimension d over a field, and let (B_t) be any family of endomorphisms.
If the intersection of all kernels is zero, then some subfamily with at
most d members already has zero intersection.

**Proof.** Start with W. If the current intersection U is nonzero, the
assumption supplies an operator B_t which does not kill all of U; otherwise
U would be contained in every kernel. Intersecting with its kernel strictly
decreases dimension. After at most d steps the intersection is zero.

Apply this to the shifted Hecke operators on each full finite module after
reduction. It gives a finite certificate whenever the simultaneous residual
obstruction is absent. It does **not** bound the auxiliary prime norms,
prove that the obstruction is absent, or provide a uniform all-weight
choice of field. The exact remaining problem is an Eisenstein congruence
problem in the full admissible Hecke module.

## 3. A primary constant-term theorem does not supply that exclusion

The primary source examined is Ming-Lun Hsieh, *Eisenstein congruence on
unitary groups and Iwasawa main conjectures for CM fields*, author version
dated 16 September 2025, Sections 7.7–7.8, pp. 90–92, Theorem 7.18 and
Corollary 7.20. Local source: `hsieh_imccm.pdf`; URL and hash are in
`source_manifest.json`.

The theorem concerns an ordinary CM setting and a branch character
unramified on one p-adic CM half, with additional class-number, conductor,
and mu-invariant hypotheses. A nonunit product L of two p-adic L-functions
produces a surjection from a cuspidal Hecke quotient onto Lambda/(L).
The corollary gives **Eis contained in (L)**. Thus the implication is
congruence production; if L is a unit, this inclusion supplies no upper
bound on the congruence ideal and does not exclude congruences. Its complete
printed proof was read, including the use of the fundamental exact
sequence and the primitive Fourier functional.

These ordinary families also require a separate comparison with the full
regular compact module used here. No such comparison or reverse divisibility
is supplied by the cited assertion. Accordingly, isolated constant-term
units are not substituted for the full U3 determinant in this work.

## 4. A concrete obstruction to the current two-prime shortcut

The parent produced explicit vectors for the full E=Q(sqrt(-3)) U3 modules
at both higher4 residual moduli in each of e=26 and e=28. Each vector has
a coordinate one and is killed by both shifted operators at 7 and 13.
The larger residual modulus in each corresponding GL2 branch has the same
property. I independently checked every row of all six witnesses against
the original matrices; see
`../hecke_general/higher4/joint_trace_nullvectors_vandiver_audit.md` and its
direct-multiplication JSON report.

For any commutative ring R, if Av=Bv=0 and one coordinate of v is a unit,
the adjugate identity gives

\[
 \det(xA+yB)=0\quad\text{in }R[x,y].
\]

This proves that no linear combination of just these two operators removes
the corresponding residual support, even when the modulus is composite.
It does not show that a globally Eisenstein eigensystem exists: a further
operator can still destroy the common kernel. The independently checked
alternate-field certificates remain a different way of doing so.

## 5. Scope of this progress

The main conceptual advance is the globally quantified source theorem and
its joint integral matrix test. The remaining uniform requirement is a
proof excluding the residual Eisenstein system in at least one permitted
full automorphic datum for every weight and coefficient prime. Neither the
current polynomial size estimate nor the inspected constant-term theorem
provides that exclusion. No extrapolation from the verified finite weights
is made.
