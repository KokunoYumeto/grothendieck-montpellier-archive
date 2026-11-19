# Independent targeted review of the Codex proof memorandum

19November2026. GPT-6 Astra Pro; effort not exposed by runtime; SA08/late.
This review was requested by the parent agent. It is a mathematical review of
specified arguments and source passages, not a second scan transcription.

## Normalization, §3 / C908

The rank statement for \(N\Lambda^r\Phi\) needs \(r\geq1\).
At \(r=0\), both exterior powers are constant \(k\) and their normalization is
concentrated in degree zero. The statement for \(N\Lambda^r\Psi\) also handles
\(r=0\) correctly. The separate warning that an unnormalized exterior term has
larger rank is sound. The exact all-module Yoneda argument has no finiteness
restriction; the algebraic-bidual warning belongs to a different restricted
test category.

## Half differential algebras, §6 / C919–920

I read K136-02 lines402–439 and459–481. For the simplex or a locally split
rank-one extension, the exterior-complex direct-sum proof is correct. Its
written proof must not be described as proving that an arbitrary flat quotient
forces local splitting. C919 already uses the safe locally split formulation;
its computation field now makes this scope explicit.

The diagram on352 specifies both endpoint products, so its first obstruction
is the difference of extension classes \(a_*e-c^*e'\), not simply the
obstruction to extending a map into the cycles. The latter would incorrectly
force a cycle-valued middle map. Equality of the pushout and pullback
extensions is equivalent to the desired middle map. Differences of two lifts
factor uniquely through the quotient into the cycle subobject, giving exactly
the Hom torsor printed on the page. Higher associativity, symmetry and
naturality constraints remain. The correction was applied to the proof
memorandum, C920 override and inherited MP100 formulation.

## Stable low homology, §10

The offsets2–5 are compatible with the stated low mod-prime coefficient
complexes. At2, the relevant polynomial generators have degrees2 and3 and
the first Bockstein sends the odd generator to the even one. The two pairs in
degrees2/3 and4/5 give exponent-two torsion. At3 the first pair is in degrees4/5.
The quoted stable-range restriction and exclusion of the fundamental degree
are essential. Tensoring with a free resolution of the coefficient group gives
the stated quotient and Tor groups. Any abstract direct-sum description
should not be strengthened to an unproved canonical decomposition. This
review checks the low-degree algebra using the source model already
established by the parent; it is not a new independent proof of Cartan's
complete theorem.

## Connectivity counterexample, §15

For \(n=p=4,G=\mathbb Z\), the proposed bound is11. Under the explicitly stated
ordinary-space-smash interpretation, degree10 of the source has the two
\(\mathbb Z/2\) summands from degrees(4,6) and(6,4). No Tor term in degree10
has nonzero inputs. The target \(K(\mathbb Z,8)\) has one \(\mathbb Z/2\) in
degree10 in the checked stable range. Thus the conditional counterexample is
valid. It does not decide which smash/tensor notation the missing ink intended.

## Euler normalization, §16

The maximal compact circle in \(\mathrm{SL}_2(\mathbb R)\) acts with weight1 on
the defining oriented plane and weight2 on the projective boundary circle.
Consequently the quotient map multiplies the integral Euler generator by2.
The magnitudes \(g-1\) and \(2g-2\) concern different associated bundles.
Orientation signs, a choice of lift and the holomorphic bundle identification
remain separate. The root argument is valid with these limitations.

## Dold natural transformations, §17 / C926

I read K136-02 lines842–890 and original Dold1961 printedpp259–263 from the
parent's OCR. Section1 defines an ordered tuple of independently varying FD
complexes. Theorem1.6 gives acyclicity of the natural-Hom complex over
\(\mathbb Z\). Sections1.7–1.12 choose a separate group-ring-free positive
complex \(W\) and construct \(W\to\operatorname{Hom}\). Section2 specializes
the independently constructed operations to equal inputs. This does not say
the entire natural-Hom complex itself is free.

For diagonal-only naturality in one simplicial set \(X\), compose the
Alexander–Whitney map with
\(f_{ab}(x_1,x_2)=(x_a,x_b)\), \(a,b\in\{1,2\}\). These give four natural chain
maps. On the discrete two-point set, applying them to the basis pair(0,1)
gives the four different basis vectors(0,0),(0,1),(1,0),(1,1). Normalized
chains of that discrete set have no positive-degree terms, so a chain
homotopy cannot change these outputs. Hence the four classes are
\(\mathbb Z\)-linearly independent in \(H_0\) of the diagonal natural-operation
complex. The insertion “pour X variable” alone does not imply \(H_0=\mathbb Z\).

A nonzero invariant vector by itself would not prove a group-ring module is
nonfree: free modules have invariant norm vectors. The discrete H0 test and
the actual distinction in Dold's construction are the appropriate arguments.
The source-read extent is corrected to pp258–263 for the parent's original
check; only the statement ofTheorem2.6, not its later proof, was reached there.

## Applied edits

At the parent's explicit request, I edited only §§3 and6 of
work/root/codex_proof_checks.md, the C908/C919/C920 overrides and peer events
before problem inheritance in programs/root_complete.py, and the Dold source
read-extent annotation in that program and work/root/references.bib.
I reran root_complete.py; its stdout is retained in
logs/late_root_peer_rebuild.txt. No other root classification was changed.
