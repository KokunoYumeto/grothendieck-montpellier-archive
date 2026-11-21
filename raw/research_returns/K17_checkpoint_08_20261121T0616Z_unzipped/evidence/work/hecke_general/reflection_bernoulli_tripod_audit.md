# Independent whole-proof audit of the isolated reflection lemma

**Verdict: PASS for K17-REFLECTOR.** Checker /root/tripod_integral,
GPT-6 Astra Pro, effort not exposed; actual check 2026-11-21 04:34 UTC.
I read the complete final TeX, reconstructed every step, freshly read the
complete proof of Sharifi's Theorem 4.4.2 and Corollary 4.4.4 in the
local primary PDF text, and visually read Ribet's Main Theorem (1.1),
printed p.151. No mathematical correction is requested.

## Character and Kummer argument

For the even character i=-e, class field theory identifies
B=A_p^[i]/p A_p^[i] with the Galois group of an elementary abelian
everywhere finitely unramified extension of F=Q(mu_p). The quotient is
Delta-stable, so this extension is Galois over Q. The Kummer radical V
is perfectly paired with B into mu_p; it has the single character
j=1-i=1+e and the same F_p dimension.

Every valuation of a Kummer representative a is divisible by p:
in the unramified extension containing a^(1/p), the normalized base
valuation is unchanged, while p times the valuation of the root is
the valuation of a. Thus (a)=a_ideal^p for a unique fractional ideal.
Multiplication by a pth power changes the root ideal by a principal
ideal. The resulting map V -> Cl(F)[p] is well-defined, additive and
Delta-equivariant. Its kernel consists of radicals representable by
units, because a principal root ideal can be removed by a pth power.

For a unit u, the quotient u/bar(u) has absolute value one in every
embedding and is an algebraic integer unit. Kronecker's theorem makes
it a root of unity. The identity
u^2=(u/bar(u))(u*bar(u)) shows that the unit group modulo roots of
unity and real units is killed by two. Since p is odd, its quotient
modulo pth powers has no odd characters except the omega character
from mu_p. The character j is odd and distinct from 1 under the
stated range. Therefore the map is injective on V, and

    dim_Fp(A_p/p A_p)^[i] <= dim_Fp(A_p^[j][p]).

If the reflected odd eigenspace vanishes, this forces the original
even eigenspace to vanish by finite p-group Nakayama. The proof does
not assume a unit-rank equality, Vandiver, or an all-character result.

## Bernoulli and K-group specialization

The index n=p-1-e is even and lies between 2 and p-3. Ribet's displayed
Main Theorem states C(chi^(1-n)) !=0 iff p divides B_n; the direction
used here is precisely the pre-existing Herbrand implication. Its
contrapositive gives the odd eigenspace [1+e] zero when the Bernoulli
numerator is not divisible by p. Reflection then gives [-e] zero.
I also checked the previously established (K2) statement and its
character computation in work/k_groups_section.tex: for e even,
K_(2e)(Z){p}=0 iff A_p^[-e]=0. This is a vanishing equivalence,
not an identification of the two finite groups or their orders.

At p=9496386083 and e=10 the needed index is 9496386072 and the
reflected character is [11]. The numerical nonvanishing certificate
is a separate input; I did not rerun the multi-billion-term Bernoulli
computation as part of this short proof audit.

## Primary sources actually inspected

- Ribet, *A Modular Construction of Unramified p-Extensions of
  Q(mu_p)*, Invent. Math. 34 (1976), Main Theorem (1.1), printed p.151.
  The author scan is locally work/references/ribet1976.pdf; its p.151
  image work/references/ribet_p151.png was visually inspected now.
- Sharifi, *Iwasawa Theory*, full author PDF
  https://www.math.ucla.edu/~sharifi/iwasawa.pdf, Theorem 4.4.2 and
  its complete proof pp.111–113; Corollary 4.4.4 p.113.
  Local source work/sharifi_full_iwasawa.pdf/.txt; the whole
  relevant argument was read now, including the exceptional omega
  term and the exact character order.

The checked TeX SHA256 is
37b466c5525735dcf724bedfcea9321f71f52aec8bb78eebf3cd915767ac3b9e.
This independently establishes the arithmetic implication and its
scope, conditional only on the separate exact Bernoulli residue for
the numerical specialization.
