# Trace and window workstream — 22 November 2026

## Delivered module and scope

trace_windows.tex contains AC-T01–AC-T14, with 14 complete proofs.
trace_windows_questions.tsv has 17 treated questions.
trace_windows_events.tsv records 33 events as of 00:29:50 UTC.
All own proofs were reread in full; the middle of the initial full-file output was truncated, then reread separately.

The input A is used exactly as stipulated. No independent Lean validation is claimed.

## Central checked consequences

- All unitary rational idele-class characters are covered by A.
- The whole centered Weil trace form, hence CCM07's positive Hermitian trace pairing, is nonnegative.
- C99's original Sobolev spectral realization now exhausts the zero locations; its strict delta-dependent multiplicity truncation and possible Jordan blocks remain in the source statement.
- A scalar positive trace-pairing completion and a separate multiplicity-preserving self-adjoint diagonal trace model are constructed.
- Every primitive Dirichlet character has an explicit finite-window form: logarithmic digamma multiplier, finite compressed prime translations, and the polar rank-two term only for zeta.
- The Dirichlet window form is closed with compact resolvent; its fixed-window spectrum is strictly positive under A.
- The exact Sonin comparison retains the prolate remainder and finite prime terms. The semilocal cutoff finite part has the sign implied by the Weil form, not a pointwise cutoff trace sign.
- A compactly supported differentiated/scaled bump refutes global positivity of the archimedean term alone.
- Finite conductor and parity twisting are fully computed by Gauss sums; the prolate image projection is an explicit finite Gram matrix construction.
- A closes MA-FT-002 in every rational/Dirichlet sector at every positive strip width, with all source path/profile conditions.
- The exact norm of each compressed translation pair is a path-adjacency norm. Root is using AC-T14 in the cubic269 finite-window certificate.

## Remaining analytic gate

T-CUT is (T.26): trace-defect convergence of conductor/parity-adapted prolate image projections. The source's positive-characteristic proof uses exact simultaneous support and Q' <= S; neither survives verbatim at the real place. The finite conductor Fourier calculation is complete, but inverse Gram estimates / E-image tails are not.

C99 explicitly asserts the zeta number-field analogue at the end of §VIII. The module distinguishes the formal consequence of accepting that source assertion from a complete new proof of its all-character extension. It does not declare the assertion false.

The MAS_ARTIN comparison is a second genuinely attempted route. Its actual spaces are weighted one-sided PW closures, its limit is a slow-band joint limit, and its full test class has g(0)=0. Thus it leaves both an operator comparison and an identity-contact normalization before it identifies C99's unweighted prolate cutoff. Scalar equality on g(0)=0 leaves a delta_0 ambiguity.

## Source locators

C99: Theorem III.1; Corollary III.2; paragraph after III.(30); Theorem V.3; Theorem VII.4; Theorem VIII.5; Lemma VIII.3; VIII.(23), (30)–(33); Appendix II Theorem6.

CCM07: Definition4.10 (motH1AKCK); Proposition4.13; Theorem4.16; Lemma4.17; Theorem6.1; Proposition6.2; Corollary6.3; Proposition6.4; Proposition7.2. Labels appear in the paper module.

CC20: Theorem1; Proposition13; Theorem17; Proposition25; Theorem27; Proposition32; Theorem44; Remark45; Proposition46; Lemma49. The numerical constant chain supporting Theorem44/Remark45 is cited, not independently recertified.

S25: Proposition3.3 (Hilbert), Proposition3.5 (compres), Theorem3.6 (thmsmallest). The zeta compact-resolvent theorem is prior work, not claimed as a new result.

MAS_ARTIN checkpoint10: modules/full_test_slow_band.tex, MA-FT-001/002, equations MA-FT.(2), (5)–(7). Entire proof read; named lower-level operator dependencies remain background.

External primary source for strictness in all Dirichlet sectors:
E. Carneiro, V. Chandee, M. B. Milinovich, *A note on the zeros of zeta and L-functions*, arXiv:1503.00955v1, Theorem5(4.4), Example8; zero count equation(4.1).
URL https://arxiv.org/pdf/1503.00955
Theorem5 and Example8 were opened and read directly. Root must open this URL before using a web reference in final chat.
The only imported quantitative fact is the O(logT/loglogT) S(t,chi) bound; the Jensen application is proved here.

## Correction notes

- Explicit Fourier labels use inverse Dirichlet character on compact units, matching the rational-idele representative convention.
- Complex endpoint terms require 2 Re(Mf(0) conjugate(Mf(1))); CCM07's real-looking formula omitted conjugations.
- Operator non-self-adjointness under A is not claimed as a proved logical independence result: the original source theorem does not establish normality, and multiple zeros give a conditional obstruction.
- The finite translation sum is not falsely called a finite-rank operator.
- A source operator comparison is never inferred from equality of scalar zero sums.
