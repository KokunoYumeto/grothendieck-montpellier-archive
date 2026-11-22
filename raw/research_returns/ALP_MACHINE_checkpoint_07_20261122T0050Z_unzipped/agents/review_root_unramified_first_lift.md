# Independent whole-proof review of AM-R-009

Reviewer: /root/lift_accounting, GPT-6 Astra Pro, ALP_MACHINE.
Reviewed file: work/research/first_lift_unramified_host.md,
including the amended compact character (R9.27) and Gaussian
normalization (R9.21)–(R9.22).

**Result: PASS in the stated actual-first-lift scope.**
The review does not independently reprove the accepted DP57 host
or AM-DO-022's full all-finite moved-phase theorem.

The trace form is the product form: writing an element of \(E'\)
as \(x+iy\), relative trace to \(E\) kills the two cross terms and
multiplies \(x\bar x'+y\bar y'\) by two. The coefficient \(\xi/2\)
therefore gives exactly \(\operatorname{Tr}_{E/\mathbf Q}
\xi(x\bar x'+y\bar y')\). No isogeny or product-polarization
substitution is needed.

The eigen-coordinate labels check directly:
\(i\) sends \(w_j^+\) to \(iw_j^+\) and \(w_j^-\) to
\(-iw_j^-\); \(\zeta_{28}=\zeta_7^2i^{-1}\) therefore gives
\(8j-7\) and \(8j+7\). Their sorted set is
\(\{1,3,9,15,17,23\}\). The chain rule gives
\(\partial_{w_2^+}=(\partial_{u_2}-i\partial_{v_2})/2\).
The fourth derivative sees only the quadratic term of each
sigma factor, and is
\(2^{-4}\binom42(-i)^2(-2)^2=-3/2\). On two copies this is
\(9/4\), with the actual common period \(C^4\) retained.

The norm character \(\mu_E\circ N_{E'/E}\) has the required
restriction by the field identity \(E'=EF'\), \(E\cap F'=F\).
Restriction of the displayed CM labels to \(E\) is
\((1,3,2,1,3,2)\); hence the infinity exponent vector and
\(\boldsymbol\nu\) in (R9.11) follow. In the corrected Hom
source action the rank-two vacuum exponent is \(-1\) at
each place, so the nonzero degree-eight vector has root-unit
exponent \(-68-72=-140\), divisible by28.

The class-one input was independently checked in the primary
Masley (1976) PDF, printed p.179. I downloaded and rendered
that page, read the Main Theorem and its table, and verified
that28 is absent while \(\varphi(28)=12\le24\). The table is
not being inferred from incomplete plain-text extraction.
The norm-one ideal proof is valid: the idele ideal has zero
exponents at nonsplit primes and opposite exponents at split
pairs, so it is \(B/\bar B\). A principal \(B=(b)\) gives the
required rational norm-one element \(b/\bar b\). This avoids
any extra assertion about signatures of real units.
Kronecker's theorem gives the intersection \(\mu_{28}\).
The finite component count and probability-Haar projector
norms then follow exactly.

For the refinement \(\lambda_f=1\), I directly opened Pan
(2001), section6.2, printed p.197: the lemma explicitly has
a one-dimensional moving space and two-dimensional isotropic
opposite space, and gives \(\alpha=1\) and
\(\beta=\chi((t-1)\delta)\). Thus the rank-one case is
covered, not inferred from an even-moving-rank statement.
With \(\chi_T=1\), the actual selfdual lattice normalization
specified in DO022 has scalar1. The nonsplit places are odd
unramified, and the dyadic places are relative split, covered
by the independently established DO020 formula. This proves
the use of \(K=K_0\), \(h_K=1\), and unit-norm source input
in the reviewed result.

The corrected Gaussian factor is necessary and correct.
Four ordinary Jacobian factors give vacuum squared norm
\(\det(2Y)^{-2}\). Each \(w_2^+\) creation mode has
commutator \(\pi/(2G_2)\); two fourth derivatives therefore
give squared norm
\(\det(2Y)^{-2}(4!)^2(\pi/(2G_2))^8\).
Dividing \((9/4)C^4\) by its positive square root gives
\(C^4\det(2Y)(3/32)(2G_2/\pi)^4\), exactly (R9.22).
No earlier unit-vacuum normalization is used in this review.

Finally,
\(\sum c_\tau\tau=116\equiv4\bmod28\).
The residue character with exponent24 on the generator
\(2\bmod29\) restricts to the inverse infinity character
on all roots of unity. It has order7. The class-one
decomposition gives the global unitary character with
the stated fixed conductor. At nonsplit places its local
character is identically1, since the local norm-one group
is compact; at split places the exact determinant-root
formula applies. Thus the repaired first functions differ
by \(\gamma(\det g)\), retain their identity values and
norms, and have type \(\det^2\operatorname{Sym}^{d_\tau}\).
Their contragredient matches the second trivial-character
source Fock type in the literal bilinear convention.

ALP-LIFT-12 may now be applied structurally to this host:
R009 supplies its actual first vector and fixed repair,
and DP57's finite unramifiedness makes \(I_4\) hyperbolic
at every nonsplit finite place. This yields an actual
nonzero second lift for some unrestricted Schwartz
input. It does not give the source's prescribed even-rank
starting row, a prescribed second finite kernel, or
arithmetic second-image cost data.

Primary source locators:
Masley (1976), Main Theorem and table, printed p.179
(local rendering lift_refs/masley1976_p179.png);
Pan (2001), section6.2 lemma and (6.2.a), printed p.197;
AM-DO-022, sections1–3, accepted host/lattice convention;
ALP-LIFT-11, (R23)–(R26), corrected bilinear repair.
