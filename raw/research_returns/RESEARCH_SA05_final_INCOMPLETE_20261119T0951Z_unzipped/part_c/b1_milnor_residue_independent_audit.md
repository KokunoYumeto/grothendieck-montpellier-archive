# Independent audit of the ordinary Milnor-divisibility argument

19 November 2026, 09:23–09:26 UTC. This is an independent mathematical
and primary-text check by the Part C agent. It does not change the B.1
universal gate.

## 1. The actual written proof

We read the complete file sections/b1_milnor_divisibility.tex and pass
both prop:B-Milnor-divisible-kernel and cor:B-Milnor-free-quotient.
We also read the complete proof of Colliot-Thélène–Schreieder's
Proposition 3.7 in the retained 2026 primary text, and Schreieder's
Theorem 2.2 and Corollary 2.3 with their complete proofs, author
pp. 6–7, in the retained Milnor–Tate text.

The decisive bound is applied with cohomological degree and twist both
equal to \(n\) and refined-unramified index zero. It gives

\[
-n\le w\le\max(-n,-2)<0\qquad(n\ge1).
\]

This does not apply with the same force to the off-diagonal residue
group occurring in the unresolved B.1 assertion. Every ordinary Milnor
element is represented by finitely many symbols and therefore has a
finite orbit under Frobenius after fixing a finite-field model. Its
regulator cannot survive inside the displayed negative-weight group.
The torsion-freeness of the ordinary integral generic group removes
the rationalization without interchanging a filtered colimit and an
inverse limit.

The simultaneous induction on degree is well founded: the induction
statement is first known for every residue field in one lower degree;
the smooth-projective-model case uses it to kill the generic residues;
and alteration plus transfer then proves the same degree for arbitrary
function fields. Transfer need not have degree prime to the coefficient
prime, because the regulator target is torsion-free. The purely
inseparable factor causes no additional difficulty when the coefficient
prime differs from the characteristic.

The finite-support localization step is also correct. A chosen open
misses only finitely many prime divisors. A vanishing generic residue
vanishes on some open of that divisor; removing the remaining closed
subsets and all singular/intersection loci costs codimension at least
two. Purity then gives a lift across all codimension-one points.

For the free quotient, the residue map is taken on one fixed model.
Each ordinary symbol has finite support there. The separated quotient
injects into a direct sum of the corresponding quotients in one lower
degree, which are free by induction. Arbitrary function fields embed
in such a quotient after an alteration by restriction and transfer.
The divisibility of the regulator kernel and the canonical completion
isomorphism follow exactly as written. No saturated residue embedding
or Frobenius-stable basis has been inferred.

## 2. The literal all-model direct sum in the older source

We separately read the definition of \(S^{(n)}\), Lemma 4.3, and the
proof of Theorem 4.2, author pp. 13–15, in the retained Schreieder
primary text. The definition explicitly includes every projective
model and every prime-to-\(\ell\) alteration, up to isomorphism.
With that definition, the displayed sum of all iterated residues does
not in general land in a direct sum.

An example already lies in the theorem's unconditional degree-two
case. Take

\[
X=\mathbf P^1_t\times\mathbf P^1_u/\mathbf F_q,
\qquad \alpha=\{u,t\}\in K_2^M(\overline{\mathbf F}_q(t,u)).
\]

For every positive integer \(m\) prime to \(p\ell\), use the finite
alteration

\[
\tau_m:\mathbf P^1_s\times\mathbf P^1_u\longrightarrow X,
\qquad t=s^m.
\]

Take the first residue on \(s=0\), then choose the identity model
\(\mathbf P^1_u\) of its residue field and take the residue at
\(u=0\). With the convention that a uniformizer in the final slot
has positive residue, the values are

\[
\{u,s^m\}\longmapsto m\{u\}\longmapsto m\in\mathbf Z.
\]

The other standard sign convention changes a fixed sign and leaves
these values nonzero. The tuples are pairwise nonisomorphic because
their first alteration degrees are distinct. There are infinitely many
eligible \(m\), so this one ordinary symbol has infinitely many
nonzero coordinates in the proposed all-model target.

The exact finite certificate is code/part_c/check_milnor_all_model_support.py
with its saved JSON output. It evaluates the tame-symbol exponent formula
for \(p=5,\ell=3,m=1+15a\), \(0\le a<10\), and checks the distinct
degrees and nonzero residues. The displayed general formula, not finite
enumeration, proves the infinite-support assertion.

A direct product would accept this tuple but would not establish the
claimed free direct-sum ambient module. This diagnoses the literal
construction; it does not refute the existential statement of
Theorem 4.2. The source itself observes that one can choose one model
and one alteration at each node. Such fixed choices give finite-support
residue trees, and a direct induction on those trees can repair the
existential construction. One must not then appeal to the canonical
all-model compatibility without checking the chosen-tree version.

The new proof in section 1 makes only fixed-model residue maps and
therefore avoids this source issue altogether.

## Exact retained sources

The primary files read are
/workspace/scratch/6215ed17d0f0/primary_sources/part_b/post08/schreieder2024_milnor_tate.txt
and
/workspace/scratch/6215ed17d0f0/primary_sources/part_b/post08/ct_schreieder2026_divisibility.txt.
The Part B source catalog supplies their canonical bibliography keys,
original URLs, retrieval records, and precise author-version metadata.
We do not claim a full-paper audit of either source.

For the Milnor–Tate paper, the independently recorded Part B access
metadata identifies arXiv:2406.18706v2, submitted 8 December 2024 and
internally dated 23 November 2024, together with the author's PDF:
https://arxiv.org/pdf/2406.18706. The publisher records online publication
on 9 March 2026, but its full text was not obtained because the PDF link
redirected to a subscription page. The construction issue above is
therefore attributed only to the opened author/arXiv versions, not to
an uninspected published file.

## Additional review and timed rerun

Root read the complete written audit, code, and saved output at 09:32 UTC and passed the proof and certificate. This was a written/code/output review, not a root rerun. We reran the exact arithmetic certificate at 09:34:34 UTC with a monotonic timer. All assertions passed in 0.000012438998965080827 seconds, excluding JSON serialization and file I/O; the output states that timing scope explicitly.

## Common kernel and prime-specific completed spectra

At 09:37 UTC we read the actual strengthened statement and complete proof of cor:B-Milnor-free-quotient, together with Sections 7 and 9 of the owner note. The common-kernel proof passes: the image of the ell-divisible subgroup in the separated free quotient at another prime is ell-divisible, hence zero; symmetry gives equality. The common quotient is canonical, so all its completion comparisons preserve the specified Frobenius action.

The formal countermodel also passes. For every prime s different from 3, the quotient D = Z[1/3]/Z has neither s-primary torsion nor a nonzero quotient by multiplication by any power of s. The Tor sequence therefore identifies M/s^r M with N/s^r N, compatibly in r and with Frobenius. The completion of the direct sum N embeds in the product of its completed finite-orbit summands. A four-eigenvector projects to a vector killed by 4^d - 1 on an orbit of length d, hence to zero in each torsion-free characteristic-zero summand. At 3 the Tate module of D supplies the nonzero four-eigenline, and the displayed representatives prove its nonvanishing without finite numerical inference. These facts do not identify the formal module with a Milnor module and do not settle the original B.1 comparison.
