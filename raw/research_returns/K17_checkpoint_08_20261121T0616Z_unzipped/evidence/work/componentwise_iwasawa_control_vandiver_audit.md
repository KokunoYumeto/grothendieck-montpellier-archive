# Independent whole-proof audit: componentwise Iwasawa control

Date: 2026-11-21 UTC. Reviewer: /root/vandiver_k.
Model: GPT-6 Astra Pro. Effort: not exposed. Run: K17.

## Verdict

PASS for the complete proposition and corollary in
componentwise_iwasawa_control_section.tex, relative to the stated,
already checked finite K-group vanishings. No Greenberg or full Vandiver
assumption is introduced. The extension to further proved finite
K-group components is valid with the same proof.

The entire final TeX and its bibliography were read. I independently
reconstructed every argument, including the exceptional odd characters.

## Finite norm control

Freshly read the complete author source
work/sharifi_full_iwasawa.txt at Lemma 1.3.8 and proof,
Corollary 1.3.9, Proposition 1.3.11 and full proof, and
Corollary 1.3.12 and proof, printed pp.16–18.
Also read Proposition 3.2.11 and its complete proof and
Remark 3.2.12, pp.80–81. The bibliography locators agree.

For F_n/F_0 there is exactly one ramified finite prime, and it is
totally ramified; the extension is cyclic. Norm is therefore both
surjective and injective after coinvariants. The author's direct
class-field proof in the new section is correct: the maximal quotient
abelian over F_0 has inertia isomorphic to the cyclic layer group;
in its abelian Galois group this inertia complements the unramified
kernel. Its fixed field is exactly the p-Hilbert class field of F_0.
This identifies the isomorphism with the canonical norm map.

The integral Teichmuller idempotents commute with the cyclic layer
action and the norm. If a character coinvariant is zero, its mod-p
quotient equals its image under sigma-1, while
(sigma-1)^(p^n)=0. Hence the entire finite character module is zero.
Taking the inverse limit of these zero modules requires no inverse
limit exactness theorem or hidden correction.

## Reflected p-ramified modules

Freshly read Wake–Wang-Erickson, Ordinary pseudorepresentations and
modular forms, full setup Section 2.1 and Proposition 2.2.6 with
its complete proof, printed pp.2–4. In tame level one, any
nontrivial even theta is primitive, and chi=omega^-1 theta
is odd, so condition (b) is automatic. The remaining excluded
theta is omega², exactly as in the new proof.

The left Ext module is the p-ramified fraktur Iwasawa module,
not the unramified module. The source proves Ext1 equals X_theta,
Ext2 equals zero, and equivalence of vanishing with actual
integral rank-one freeness. Undoing inversion and Tate twist
preserves freeness, giving the character omega theta^-1.
Setting theta=omega^(-2j) therefore gives omega^(2j+1),
with no inverse-character or Tate-twist discrepancy.

## Exceptional characters and finite range

Freshly read Sharifi Theorem 5.5.31 and its full printed proof,
p.148, and the construction and statement of Proposition 6.1.1,
pp.151–152. Also freshly read the full proof of
Wake–Wang-Erickson Lemma 5.2.7, p.13, which explicitly records
X_omega=X_(omega^-1)=0 by Stickelberger.

The global odd units contribute precisely the root-of-unity
term. Coleman therefore gives M_(omega^-1)=Lambda and
M_omega=ker(Lambda -> Z_p(1))=(gamma-u)Lambda.
The latter principal ideal is free of rank one even though its
inclusion in Lambda is not a unit multiple. The valuation direction
at the sole p-prime is even and contributes to neither odd character.
The characters are distinct for p>=5, the asserted range.

Finally I read the actual promoted nine-degree periodic corollary
in work/hecke_minus7/k32_vanishing_section.tex. It supplies exactly
the components j=1 through 9 used here. The trivial j=0 component
descends to Cl(Q)=0 because the extension degree p-1 is a unit
on p-primary groups. All repetitions for small p are harmless;
CC.1 includes p=3, while the ramified-module freeness statement
correctly begins at p=5.

The torsion companion in the cubic criterion is the Lambda-torsion
part of precisely this p-ramified module, so it vanishes in these
characters. No unproved cubic residue condition is inferred in
any remaining character. The final scope limitation is accurate.
