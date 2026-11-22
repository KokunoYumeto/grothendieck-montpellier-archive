# Independent semihomogeneous construction audit

**Outcome: full typed proof and exact primary inputs passed.**

We read `agents/frobenius/C4_semihomogeneous_obstruction.tex` in full and independently rederived the restriction divisibility conditions, the even/odd valuation cases, the exclusion of the half-Poincare square from the generated numerical ring, and the degree-three parity conclusion. The pure square terms cannot enter the mixed bidegree (3,3), so the listed three mixed coefficients suffice. The degree-three generator list comprises third Chern classes, second Chern classes times divisors, and products of three divisors. The virtual Fourier-kernel example belongs to the excluded ring by its actual integral K0 decomposition; arbitrary moduli kernels are not claimed to do so.

We freshly opened the full published primary PDF of Gross, Kaur, Ulirsch and Werner, *Moduli*3,e8(2026), DOI10.1017/S2949764726100228, and read Theorems2.4 and2.6 on printedp6 and Lemma2.9 with its proof onpp6–7. Section2 explicitly works over any algebraically closed characteristic-zero field. The isogeny pushforward and common-slope simple/unipotent decomposition prove the numerical exponential Chern formula for every semihomogeneous bundle, without a simplicity restriction. The exact source URL is in frobenius/C4_semihomogeneous_references.bib; web retrieval was turn662430795view0.

For s=v2(r)>0, the restrictions give v2(a),v2(c)>=ceil((s−1)/2). If2v2(b)<=s, v2(2ac)>2v2(b) in both parities, contradicting integrality of chi. The only possible deficit in v2(a)+v2(c)>=s occurs for odd s and is again excluded by chi. For the third Chern class, v2(r−2)=1 when s>=2; when s=1 it is at least2 unless r=2, where the third Chern class is zero. The asserted bound gives an even mixed coefficient in every case. Odd rank has the explicit even factor r−1.

This is a method obstruction for a specified generated subring, not a result about the full integral numerical cycle lattice, and it does not close C4. The only editorial correction suggested was to remove the stray comma in superscripts R_sh^{,2} and R_sh^{,3}. No mathematical correction was needed.

Reviewer: GPT-6 Astra, inherited effort, /root/cycles; an independent targeted check in the same model/run, not independent-model verification.

Fresh audit receipt: 2026-11-19T10:26:24.679975+00:00
