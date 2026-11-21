# Independent odd-discriminant family review

Reviewer `/root/lean_chain`; GPT-6 Astra Pro; effort not exposed.
21 November 2026. Time and exact hashes are recorded in
`odd_discriminant_family_review_manifest.json`.

**PASS** after a complete read of both new proofs in
`../main_gate/odd_discriminant_two_unit_family.tex`:
`KT-ODD-DISCRIMINANT-TWO-UNIT-FAMILY` and
`KT-ODD-DISCRIMINANT-GD`.

For each p≥7 congruent to 3 modulo4, write p±4=m u². Both m and
u are odd, m is square-free and m≡3 modulo4, so D=−m is an odd
negative fundamental discriminant. Neither m nor u is divisible by p.
The symbols at p are exactly opposite: the plus field is inert and
the minus field is split, since D≡∓4/u² modulo p.

The imaginary class bound is a correct direct application of the
finite character sum in Benmerieme–Movahhedi Theorem4.1. For m>3,
h(E)≤(m−1)/2≤(p+3)/2<p; for m=3 the roots-of-unity factor gives
h=1. The imaginary quadratic B1 formula then gives a p-unit because
p≥7 does not divide either possible roots-of-unity count2 or6.

For the real field of discriminant d=pm, the explicit element
alpha=(p±2+u sqrt(d))/2 is integral, has norm1, and is greater than1.
No norm−1 unit exists, since reducing its Pell equation modulo p
would make −1 a square. If alpha were a proper power epsilon^n of
the fundamental unit, n≥2, its trace would be at least
Tr(epsilon²)=d y²+2≥3p+2, contradicting its exact trace p±2.
Thus the displayed element really is fundamental, without assuming
that u=1 or that p±4 is square-free.

At the unique prime over p, pi=sqrt(d) has valuation1 and p has
valuation2. The formula `s alpha−1=s(p+u pi)/2` has valuation1.
If alpha=z^p, the residue of z is s; therefore sz=1+w with v(w)≥1.
Every nonconstant term of (1+w)^p has valuation at least3. This
contradicts the preceding valuation1 and proves the exact local
non-pth-power condition.

Le's stated bound uses the field discriminant, so it gives
h(F)≤floor(sqrt(pm)/2)≤sqrt(p(p+4))/2<p. Combined with the verified
fundamental-unit condition, Benmerieme–Movahhedi Corollary2.6 applies
for every p≥7, including the ramified prime in this real quadratic
field. Corollary2.2 then supplies the p-adic L-value unit.

The primitive character product with omega^((p−1)/2)=chi_{−p}
is chi_D. The imprimitive product differs by the p Euler factor,
which is1 modulo p because (p−1)/2≥3. Hence their Eq3.2 has exactly
the displayed normalized Bernoulli value. The previously audited
all-weight transport applies to every nonnegative t, including weights
larger than p and indices divisible by p.

Both twists have order (p−1)/2: e≡(p−3)/2 and2e≡−2 modulo p−1.
This order is odd and greater than2. The third unit is equivalent to
the separate normalized value B_(p−2),chi_D/(p−2); it is not proved
by the preceding argument.

Every literal GD field at N=2,psi=1 is now satisfied. The complete
independent source check is in `GD_ODD_FIELD_SCOPE.md`. In particular,
the remaining eta noncontainment condition follows from nontrivial
quadratic inertia at a prime q dividing m, q≠p, while the mod-p
cyclotomic character is unramified there. There is no hidden
split-at-p or e<p condition.

## Exact primary reading scope

I read the entire four-page Le1994 paper, including Theorem(a) and
its complete Section3 proof, and the entire one-page1995 correction.
The correction changes only the attribution of reference[2] to
B.Oriat. The theorem's numerical initial range and the analytic lemmas
imported by Le were not independently recomputed here.

I also read Benmerieme–Movahhedi's Corollary2.2 and its preceding
residue formula derivation; the complete Proposition2.3 proof and
the Proposition2.4/Corollary2.6 reduction; the full context of Eq3.2;
and the exact Theorem4.1 class-number formula. These primary inputs
have precisely the scope used by the proof. The family does not
rely on an unseen display or the authors' unexpanded “same method”
remark about p(p−4).

The source's actual Type-II exclusion still needs the third unit.
The new two-unit theorem can exclude ordinary lower-weight rank-two
sources under their explicit hypotheses; it does not itself exclude
all stable rank-three sources or prove another K-group vanishing.
No Lean kernel execution is claimed.
