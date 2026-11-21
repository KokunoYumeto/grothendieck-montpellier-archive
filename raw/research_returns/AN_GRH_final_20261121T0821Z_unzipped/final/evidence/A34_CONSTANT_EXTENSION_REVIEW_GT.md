# Independent whole-proof review of A34's constant-extension supplement

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

**PASS.** I read the complete statement, three-case formula, consequence, and entire proof of `work/effective_galois/A34_CONSTANT_EXTENSION_SUPPLEMENT.tex`, SHA256 `25daf5277ed18f7cea32e13bc8d5b3368b22dd884b757461198a5b019743a308`.

The fixed, already certified cyclic degree-19 cover over F64 has rational Prym two-primary exponent

- 1 if 7 does not divide the constant-extension degree m;
- 2 if 7 divides m and m is odd;
- `2^(v2(m)+2)` if 14 divides m.

Thus this particular A34 inequality holds exactly when 14 does not divide m. Failure of the inequality is correctly kept separate from failure of section separation.

## Checks of the full argument

The unramified degree-18 ring O = Z2[zeta19] is a complete discrete valuation ring. The established character polynomial has roots of `X^2+cX+64`. Its reduction has distinct roots 0 and cbar because c is a unit. Hensel therefore gives a unit root u; the other root is w = 64/u. Dividing the root equation by the unit u gives `u = -c mod 64O` exactly.

The previously certified congruences imply that ubar has exact order seven and `u^7 = 3 mod 8O`. With the deck action constant, base extension raises both Frobenius roots to their mth powers. Consequently the faithful character factor at 1 has valuation `v2(1-u^m)`, since `1-w^m` is a unit. The use of the earlier finite O-module proof of (BE.8) is valid after every stated extension and gives the exponent, not merely the order, of the rational two-primary group. This distinction is essential and is maintained.

For 7 not dividing m, reduction proves valuation zero. Otherwise m = 7j and a = u^7 has `v2(a-1)=1`, `v2(a+1)=2`. An odd power preserves the first valuation. The first squaring gives valuation three; each later squaring increases it by exactly one because the previous even power is one modulo eight. A final odd power leaves that valuation unchanged. This proves all three cases, including the boundary m = 14, where the exponent is eight. Substitution into `19 > (2M-1)^2` gives the exact stated successful set.

No new execution of the degree-19 divisor-arithmetic certificate was needed or claimed here: its c congruences and character polynomial were fully checked in the previous A34 review. This event is a new independent whole-proof review of the constant-extension deduction.

## Primary input reopened

Stacks Project Lemma 10.153.9, Tag 04GM, https://stacks.math.columbia.edu/tag/04GM . I read the complete statement and displayed Newton-lifting proof; retrieval reference `turn810580300view0`. It proves complete local rings are Henselian and directly justifies the simple-root lift used here.
