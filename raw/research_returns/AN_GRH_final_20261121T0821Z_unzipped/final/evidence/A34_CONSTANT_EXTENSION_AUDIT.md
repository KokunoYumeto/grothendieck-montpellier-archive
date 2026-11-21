# A34 constant-extension supplement: full-proof check

- Date: 2026-11-21 UTC.
- Writer/checker: GPT-6 Astra Pro; effort not exposed; `/root/effective_galois`.
- Source: `A34_CONSTANT_EXTENSION_SUPPLEMENT.tex`.
- SHA-256: `25daf5277ed18f7cea32e13bc8d5b3368b22dd884b757461198a5b019743a308`.
- Outcome: **PASS, complete producer self-check**. Independent final-text reviews requested separately from root, row, and GT.
- Formal verification: false.

The observation and the simplification using the two Hensel roots were proposed by `/root/row_audit` after the original A34 proof. I previously checked the argument in `A34_CONSTANT_EXTENSION_REFINEMENT.md` and have now written and reread the complete TeX supplement. This is a refinement for the one existing degree-nineteen cover; no new cover or new finite arithmetic implementation is introduced.

## Input and source checks

The supplement uses only the already checked character polynomial `1+cT+64T^2`, the exact order seven of `c mod 2`, the certified congruence `1+c^7 = 6 mod 8`, and the finite O-module exponent formula (BE.8). These were proved and independently checked in the existing A34 proof and its two retained finite certificates.

Hensel's lemma is cited precisely as the Stacks Project, Lemma 10.153.9, Tag 04GM, with the simple-root definition in 10.153.1. I opened and read the entire lemma and its proof, and the definition plus uniqueness Lemma 10.153.2. Primary URLs:

- <https://stacks.math.columbia.edu/tag/04GM>, web ref `turn910056806view0`;
- <https://stacks.math.columbia.edu/tag/04GE>, web ref `turn910056806view1`.

The existing coefficient ring is a complete unramified DVR of degree eighteen. The reduction of `X^2+cX+64` has distinct roots zero and `c mod 2`; the unit root u and its other root w=64/u therefore lie in the ring, with `v_2(w)=6`. The equation gives `u=-c mod 64`, so the certified seventh-power congruence becomes `u^7=3 mod 8` with the correct sign.

## Entire proof check

1. Constant deck action remains defined over every constant extension, so the same faithful character factor has roots `u^m,w^m`. No unproved identification of an étale Tate eigenvalue with u is used.
2. `1-w^m` is a unit. The earlier finite O-module argument thus gives exactly `M_m=2^{v_2(1-u^m)}` and relative class-number valuation eighteen times this exponent valuation.
3. The residue order of u is seven; hence the valuation is zero precisely outside multiples of seven.
4. If `a=u^7`, the congruence `a=3 mod 8` gives valuations one and two for `a-1` and `a+1`. An odd exponent leaves the difference valuation unchanged by a unit geometric sum. The first squaring gives valuation three; each further squaring adds one because the previous even power is one modulo eight. This proves the exact even-exponent case `v_2(m)+2` in the unramified extension ring, not just in Z2.
5. The criterion comparison is exact: M is one or two when 14 does not divide m, and at least eight otherwise. Accordingly the right side `(2M-1)^2` is one, nine, or at least 225. The source carefully limits the negative assertion to failure of this sufficient inequality.

All five displayed-math blocks are balanced. The longest display (BE.26) is split into two lines before integration. No canonical final source was changed.
