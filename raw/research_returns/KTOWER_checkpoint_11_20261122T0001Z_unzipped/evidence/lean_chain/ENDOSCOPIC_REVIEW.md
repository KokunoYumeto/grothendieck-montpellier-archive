# Independent whole-proof review of the endoscopic injection

Reviewer: `/root/lean_chain`, GPT-6 Astra Pro; effort not exposed. Date: 2026-11-21 UTC.

## Verdict and scope

I read the complete `evidence/unitary_audit/endoscopic_results.tex`, including the theorem KT-U3-ENDO-INJECT, corollary KT-U3-ENDO-SIX, all proofs, and the final limitation on exhaustion. The injection and the identification of the unique compact spaces at e=4 and e=6 pass this targeted proof review. No Lean kernel check is claimed. The earlier compact dimension calculation, classical dimension/CM classification, classical Hecke computations, Iwasawa description of the full stabilizer, and the standard local correspondence remain carried background. I did not independently reconstruct the global trace-formula proof of cyclic base change.

The conclusion is an injection of non-CM quadratic-twist pairs. It proves the full stable/endoscopic decomposition only when the already computed ambient dimension equals the lower bound, in particular e=4 and e=6. The proof correctly makes no all-weight exhaustion assertion.

## Source checks actually performed

The local KMSW text is the checkpoint07 carried `evidence/work/hecke_coverage/kmsw_inner_forms.txt`. The line numbers below count `text.split('\n')`, retaining form-feed characters within lines.

| Point checked | Exact source | Result |
|---|---|---|
| Radical of the centralizer | KMSW §0.4.4, printed p.27, lines1357–1375; repeated §1.6.1 p.80, lines4521–4534 | It is the identity component of the centralizer inside the dual derived group. For U3 that group is SL3. |
| Local conjugate parity | KMSW §1.2.3 p.60, lines3411–3456; §1.2.4 Lemma1.2.5 p.61, lines3479–3513 | The distinct characters at infinity each have positive parity. Their sum admits no negative-parity form. |
| Global parity and localization | KMSW Proposition1.3.1 p.67, lines3819–3850, and Proposition1.3.3 p.71, lines4014–4095 | The same embedding/parity localizes. Hence the global cuspidal rank-two constituent has positive conjugate parity. Both seed statements are needed for this deduction. |
| Packet characters and twist dependence | KMSW Theorem1.6.1(2) p.80, lines4521–4575 | The local pairing factors through S^natural. An element in S^rad has value one for every packet member, including the needed full-stabilizer member. |
| Global epsilon character | KMSW §1.7 p.89, lines5027–5067 | Generic parameters have trivial epsilon character. The text explicitly limits the unconditional result to generic parameters and pure inner twists. |
| Proved multiplicity formula | KMSW Theorem5.0.5 p.206, lines12021–12075, entire statement and proof read | Both required hypotheses are proved for a generic parameter on a pure inner form. The compact hermitian U3 used here is within this case. |
| Ramified principal series | Adler–Lansky, carried `adler_lansky_ramified.txt`, §4.4 pp.14–15, lines720–759; Proposition6.1 p.21, lines1121–1139; Proposition7.1 p.28, lines1477–1519 | The unitary unramified inducing character excludes the first two reducibility cases. The only reducible case is its nontrivial unramified quadratic value, and the relevant two constituents form the stated packet. |
| Real compact-root rule | Gan–Gross–Prasad, *Restrictions of representations of classical groups: examples*, Astérisque346 (2012), §2 printed p.115, directly read as rendered PDF page5 | The character product for positions i<j on a compact root is (-1)^(i+j). Therefore positions1 and3 have product+1. This is the real packet description quoted by the authors, not an appeal to their restriction conjecture. |
| Cyclic base change and self-twists | Langlands, *Base change for GL(2)*, author retypeset version, §2 p.13; Lemma11.3(b) p.133; Proposition11.4 p.136; Lemma11.7 p.142 | Read the relevant statements directly. They give the base-change and twist-fibre statements used here; the self-twist criterion identifies induction from the specified quadratic field. |

Public primary URLs used for the last two rows:

- https://www.numdam.org/item/AST_2012__346__111_0.pdf
- https://publications.ias.edu/sites/default/files/base-change-for-gl2_rpl_2.pdf

## Checks of the actual argument

For a nonfixed twist orbit, the cuspidal base change has trivial central character, is fixed by conjugation, and is self-dual. Its infinity characters have exponents e and -e, so the two-seed parity argument makes it a permitted constituent of the rank-three generic parameter. The conductor-one calculation at three gives unramified base change, and the distinct inertial characters exclude a non-tempered unitary principal series there.

The finite component-group argument handles repeated roots as well as distinct roots. If b differs from b^{-1}, the element -I2 lies in the connected reciprocal diagonal torus. For a repeated nontrivial character, it lies in SO2 or Sp2. If that character merges with the third trivial summand, diag(-1,-1,1) lies in SO3. Every displayed connected subgroup is contained in SL3. Thus the global generator maps into the exact S^rad used by KMSW, not merely into an unspecified connected group. This removes the dependence on which ramified constituent has the full-stabilizer vector.

At infinity, the two-dimensional constituent occupies the outer positions1 and3. The compact-root rule therefore gives value+1 for its product generator. Individual sign conventions and the two choices of definite hermitian signature do not affect this product. The finite and infinite values agree with the trivial global epsilon character. The generic/pure-inner multiplicity formula supplies an actual discrete automorphic representation, so the construction is not based solely on a match of a finite list of Hecke eigenvalues.

Twist-fibre uniqueness makes different two-element orbits distinct global parameters. Their automorphic summands are independent, which establishes the dimension lower bound. At e=4 and6 the existing ambient dimensions are one, so no room remains for a stable summand. The scaled split-prime trace is p^e+a_p, which yields the corollary's stated values from the carried classical data.

## Minor exposition correction communicated to the author

The conductor paragraph's conclusion is correct, but the sentence saying that equal inertia characters contradict a quadratic determinant is not a sufficient standalone justification. A precise short route is: conductor one and a ramified determinant force a(r)=1, no Swan part, and dim(V^I)=1; the inertial representation is therefore 1 plus epsilon. Monodromy commutes with these two distinct inertia lines and is nilpotent on each one-dimensional summand, hence zero. This avoids relying on the determinant alone. The author was notified; this is not a defect in the resulting local assertion.

Reviewed source SHA256 at the final read: `2ef56d8d99f626dc7443676f03970bc08e3a269fba9e255ef6c9c24c51a429c4`.
