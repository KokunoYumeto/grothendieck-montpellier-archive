# A23: independent complete proof review

Date: 2026-11-21.
Reviewer: GPT-6 Astra Pro, /root/effective_galois;
reasoning effort is not exposed.

Reviewed source:
work/row_audit/A23_B3_ORDINARY_OBSTRUCTION.tex.

Final SHA-256:
64debc1b1bd28665535090a0041f0e5e78f938adcb19824c47938a3f017271ce.

The original whole-read body hash was
e5a4726aecc69f7ad0b0d7dced6a538149fe0ffd59f9893d4cf0f6ec08bb40e2.
The later change only prepended the subsection heading and its label.
I read the new heading and verified byte-for-byte, by hashing the
remaining suffix beginning with the Finding A23 paragraph, that the
entire mathematical source is unchanged. The whole-proof PASS
therefore carries to the final hash.

**Outcome: PASS.** I read the entire statement, proof and source-scope
paragraph. No mathematical correction is needed.

## Exact scope

For the specified ordinary genus-two curve over F4, the first
inequality of the sufficient prime-quotient test in recovered
A1 B.3 fails over every constant extension. This conclusion is
proved for every prime divisor of the actual Jacobian point count,
so omitting the primitive-root hypothesis cannot repair this
particular numerical test.

The statement does not refute B.3, which is only a sufficient
criterion, nor does it assert absence of theta witnesses. The
order-4159 witness from A13 persists over F_(4^7).

## Complete argument checked

1. The three simple poles 0, 1 and infinity give genus 2 and
   2-rank 2 by the Artin–Schreier formulas. Each ramified point
   is rational over F2. At the two additional x-values over F4,
   the right sides are u^2 and u, both of absolute trace one,
   so the point counts over F2 and F4 are both 3.

2. Thus the power sums of the F2 Frobenius eigenvalues are
   s1=0 and s2=2. Newton's identity and the genus-two
   functional equation give T^4-T^2+4, with correct signs.
   Squaring these four eigenvalues gives the two roots of
   T^2-T+4, each twice. This is a statement about the
   Frobenius polynomial; no isogeny classification is assumed.

3. Over F_(4^m), with Q=4^m and
   t_m=beta1^m+beta2^m, put e_m=Q+1-t_m.
   The recurrence has t0=2, t1=1 and
   t_m=t_(m-1)-4t_(m-2), so e_m is integral.
   Curve and Jacobian point-count formulas give exactly
   N_m=2e_m-(Q+1) and J_m=e_m^2.
   Weil gives e_m >= (sqrt(Q)-1)^2 > 0 for every m>=1.

4. A prime divisor ell of e_m^2 divides e_m, hence ell<=e_m.
   Since N_m is a nonnegative point count,
   ell*N_m <= e_m*N_m = 2e_m^2-(Q+1)e_m < 2e_m^2.
   This is the all-extension proof. It does not infer a
   universal quantifier from finitely many recurrence checks.

5. The recovered criterion has N_m>=2|K| for a surjection
   J_C(F_Q)->Z/ell with |K|=J_m/ell. Its first condition is
   therefore exactly ell*N_m>=2J_m, contradicted above.
   The other condition ell>N_m and the primitive-root
   requirement are irrelevant to this failure.

6. A13 supplies at least four nonzero theta points of exact
   order 4159 over F_(2^7). The model is defined over F2,
   so its Frobenius twist and locally exact differential
   theta support are compatible with both field extensions.
   F_(2^7) is contained in F_(2^14)=F_(4^7). Base extension
   preserves incidence and exact geometric order.
   The order of 2 modulo 4159 is 2079, so the signed
   doubling group is full while 2 itself is not primitive.
   The text states this distinction correctly.

## Sources independently inspected

- Recovered checkpoint-03 ANABELIAN_A1_paper.tex:
  the whole B.3 claim and proof, including (B.CL.1),
  (B.CL.2), and its explicit limitation.
  Source location:
  recovered/ANABELIAN_A1_cp03_text/ANABELIAN_A1/ANABELIAN_A1_paper.tex,
  lines 2488–2546.

- A13 in work/effective_galois/lang_weil_criterion.tex:
  the complete arithmetic and theta-incidence proof, together
  with the Lang-fibre count and ordinary-origin exclusion on
  which it relies. This is the same A13 previously checked by
  the parent with an independent resultant certificate.

- Pries–Zhu, The p-rank stratification of Artin–Schreier curves,
  Annales de l'Institut Fourier 62(2) (2012), 707–726,
  Lemma 2.6, printed p712: exact formula and immediate proof
  reopened in the published primary PDF.
  https://www.numdam.org/item/10.5802/aif.2692.pdf
  Web refs: turn971908777view0, turn692794671view0.

- Milne, Abelian Varieties, author version 2 January 2022,
  Theorem 19.1(a)–(c), printed pp40–41, including the
  following Frobenius proof of part (b).
  https://jmilne.org/math/xnotes/AVs.pdf
  Web refs: turn180833725view0, turn971908777view1.

## Arithmetic artifact scope

I read the complete supplied verify_A23_recurrence.py and
A23_RECURRENCE_CHECK.json, including the exact values at m=1
and m=7 and the declared range 1<=m<=40. This audit does not
claim a new execution or an independently authored numerical
implementation. The symbolic argument above proves the
universal assertion and is sufficient for this whole-proof pass.

No final source files were edited.
