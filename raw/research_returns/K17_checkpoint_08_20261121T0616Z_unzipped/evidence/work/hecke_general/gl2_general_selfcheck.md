# K17-GL2-GENERAL and generic coverage: actual check record

Date: 2026-11-21. Author: /root/vandiver_k, GPT-6 Astra Pro.
Effort not exposed. Run K17.

I read back the entire final gl2_general_section.tex and every line of
gl2_general_certificate.py, hecke_combined_certificate.py, and the
separate gl2_e10_p19_certificate.py. All three exact programs executed
successfully. The complete basis proof was reconstructed from the
primary ring statement and the two cusp orders of D. The first-r
coefficient solve, including the n=7 correction for e=12, identifies
the full Hecke operator. Polynomial factors, evaluations, exact gcds,
and trial-division prime factors all agree.

I freshly read Cléry–van der Geer, arXiv:2110.00849v2, the complete
Gamma1(3) ring paragraph on printed page 12 and Remark 15.2 on page 33.
The proof is uniform for e at least three; only the displayed finite
arithmetic values are specialized to e=6,8,10,12.

I also read back the entire separate
work/hecke_coverage/u3_general_coverage_section.tex, including its
general pointwise polynomial-unit corollary. I compared it with the
entire previously checked source-interface and compact-transfer proofs.
Every parameter dependence is explicit: source exponents
(e-1,-1,-e-1), infinitesimal character (e,0,-e), compact highest weight
(e-1,0,1-e), and scaling p^(e-1)T=p^e times the unitary Satake trace.
The strengthened WitA and Unl conditions are retained and used.
All finite-place arguments and odd-rank temperedness remain unchanged.
No new global multiplicity assertion beyond the cited generic pure-inner
theorem is introduced. No comparison with the source's TrData occurs.

Tripod independently read all of the general GL2 proof and three
programs, replayed all three, and reported PASS in
gl2_general_tripod_audit.md. I read that entire audit.
The exact finite-model identities are established; the Selmer/K-group
application remains in the separately assembled coverage chain.
