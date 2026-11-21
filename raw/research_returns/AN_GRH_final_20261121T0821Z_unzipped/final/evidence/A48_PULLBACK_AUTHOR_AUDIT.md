# A48 pullback-iteration supplement: author and source audit

Date: 2026-11-21. GPT-6 Astra Pro, `/root/row_audit`; effort not exposed.

## Finished supplement

`work/row_audit/A48_PULLBACK_ITERATION_SUPPLEMENT.tex`, SHA256 `b80961b464066b270cf4edda207647bbf9bf17e4a55423c2292b6d7ca4ca824b`: **author complete proof/scope check PASS**. I read the complete initial finished text at `56b9f0a48b034a5c44c928c4806a2079b09227306bf16cded988403cc5f49caf`, then checked the only two scope additions: explicitly smooth proper genus-at-least-two base and geometrically cyclic group, and the finite extension possibly needed for Raynaud descent/pointing. No subsequent mathematical change.

The proof uses the actual integral Ramanujan projectors, not arbitrary isogenous factors. Base-change deck equivariance makes both pullback and norm commute with them. Their composite is multiplication by the prime-to-p base-change degree. This proves geometric p-primary and common-field rational injections, hence p-rank inequality and exponent divisibility. Connectedness of the fibre product retains the conductor; the source explicitly makes no same-conductor conclusion after selecting a component when it drops.

The consequences are confined to failure of the old vanishing/exponent inputs. A newly chosen cover upstairs remains possible. The source separately preserves the pointing hypothesis and does not infer rational lifts from group injection. The trace splitting is Frobenius-compatible, so existing stable cohomology survives. The elliptic-intermediate obstruction is just étale Riemann–Hurwitz; additional non-deck automorphisms or correspondences are not ruled out.

## Exact primary source recovery and reading

Raynaud, *Revêtements des courbes en caractéristique p>0 et ordinarité*, Compositio Mathematica123 (2000),73–88, DOI `10.1023/A:1001840726893`.

- Recovered PDF: `work/row_audit/Raynaud2000.pdf`, 183285 bytes, SHA256 `ad8cd27ee1169d46c9e79e902e02bc40fc66145ffe35b79b4c86f62b381b183f`.
- Text extraction: `work/row_audit/Raynaud2000.txt`.
- Primary publisher URL: `https://www.cambridge.org/core/services/aop-cambridge-core/content/view/16AB72912D3CE32BFC5D012B1025A8E4/S0010437X00000440a.pdf/revetements-des-courbes-en-caracteristique-pandgt0-et-ordinarite.pdf`.
- Read §1 setup, complete Proposition1 and its displayed proof, Theorem2 statement and following discussion, and §3's construction, Lemma16, Theorem17, Corollary18 and the complete printed general-case proof of Theorem2, especially printed pages74–76 and83–86. This is not a claim of having independently reproved all the cited Mumford/Hirschowitz inputs or read the entire publication.

The exact supplement locators are Proposition1(5),p75, and Theorem2,p76. They give support containment of the pulled-back Jacobian in the locally-exact-differential theta divisor, a stronger incidence statement than one torsion point. No stable-rank-zero statement appears there.

Pop–Saïdi2003 §§1.1–1.3 and2.1–2.4 were read completely from the retained primary extraction `work/sources/pop_saidi2003.txt`. Proposition2.4,p114, uses Raynaud and then Proposition2.3. The already recorded pairwise-coprime-order qualification was not treated as a new discovery or new finding.

## The exact higher-genus loss

The explicit choice in Raynaud's general construction for original genus2 and p2 first takes a cyclic cover of degree5, whose genus is6, and then n3. The constructed nontrivial irreducible representation has rank3^6=729. Its associated degree-zero finite-monodromy bundle has no global sections, so Riemann–Roch makes H1 dimension(6-1)*729=3645. This is a calculation from the cited parameters, not a claim that its stable Frobenius rank was computed. A singular map in that space is not automatically nilpotent. The supplement does not assume that every higher cover has one-dimensional character spaces.

An exact existing comparison is A30: its cyclic degree3 cover has base genus/p-rank(3,1), source(7,5), and ordinary new factor of dimension4. These numbers follow from DC.3: the reduced source numerator has degree5 and the reduced new numerator degree4. Thus nonordinarity of the upstairs curve can persist with the old defect unchanged and no new defect. I read the full retained A30 section to check the context; the event below records the specific genus/rank comparison, not an additional independent reconstruction of its complete certificate.

Even Raynaud's stronger fresh nonordinary representation does not provide a bound annihilating a newly selected primitive stable factor. In a pullback iteration the sharper norm/projector injection prevents an old primitive stable part from disappearing at all. The missing input is a theorem selecting a genuinely new cyclic cover upstairs with rational primitive torsion zero or a sufficiently small actual exponent, with its prescribed pointing. This audit does not establish such a theorem or a universal obstruction to it.
