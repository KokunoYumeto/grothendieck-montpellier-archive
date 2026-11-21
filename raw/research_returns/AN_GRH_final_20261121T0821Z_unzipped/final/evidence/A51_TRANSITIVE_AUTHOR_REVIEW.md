# A51 transitive-deck supplement: author whole-proof review

Date: 2026-11-21. GPT-6 Astra Pro; effort not exposed; AN_GRH `/root/row_audit`.

**PASS, targeted proof check of the complete supplement**, including the determinant and the final targeting comparison. Source:

`work/row_audit/A51_TRANSITIVE_DECK_SUPPLEMENT.tex`

SHA256 `2d127609310816ba0388587bb9b72c55789e892cb74ce1938884b2afbf8b85c3`.

The complete first version at5c961b0a… was read, followed by the exact final clarification of the cyclic-block determinant and the MilneJV11.1 citation. Those changes do not alter the lemma. No code, numerical example, or geometric countermodel was constructed; no independent re-proof or formal verification is claimed.

## Actual geometric proof

The hypotheses are genus two, characteristic two, odd cyclic geometric degree n, and full deck Frobenius order phi(n). The primitive subvariety is the actual integral-projector image. Its geometric two-torsion is a module over the full finite etale product A=Z2[Z]/(Phi_n,2); it is not silently replaced by a single residue field.

Full transitivity makes A^tau=F2 and permutes the field factors transitively. Frobenius semilinearity forces equal module ranks on those factors. Since the actual primitive dimension is phi(n), the geometric two-rank bound forces rank zero or rank one over A. In rank one, Frobenius is c tau with c a unit. Its full norm lies in F2^×={1}, so its fth power is the identity. The already-proved integral descent supplies exactly one rational two-torsion generator. Thus rational primitive-unit vanishing is equivalent to geometric two-rank zero under these hypotheses.

The auxiliary-adic faithful summands have dimension two. Transporting bases around the full cycle gives the block-companion determinant det(1−TF)=det(1−T^f R), and abelian-variety integrality/top coefficient gives H_B(T)=1+S T^f+q^f T^{2f}. In the ordinary case the actual rational two-torsion makes S odd; the return scalar is one modulo two. The rational two-primary group is cyclic, so its exponent is exactly2^{v2(1+S+q^f)}, without an asserted valuation bound. In the rank-zero case it is trivial and S is even.

The final comparison uses f_r proportional to ell^r, so Q_r=q^{f_r} outgrows n_r. Weil bounds give #C(K_r)>n_r and an unbounded quotient kernel. Thus A49's sufficient counting proof does not apply to that prescribed quotient. This is not an assertion that the quotient must be uniform or that a unit character can never occur. Norms' faithful-component invisibility and the per-factor scope of NC.15 remain explicit.

## Known-input scope

The actual conductor algebra and descent are A45 SD.3–SD.9a, already wholly checked; the underlying module theorem is Stacks023N. Genus-two faithful character degree is recovered A1 B.2 and A49 OQ.7–OQ.8. The numerical two-rank bound and abelian Frobenius polynomial facts are the exact MilneAV8.5 inequality and19.1 passages checked for the main A51 source.

For the final curve point bound, Milne *Jacobian Varieties*, Theorem11.1, was directly reopened/read, including its displayed reduction to Proposition11.2 and ensuing proof. Primary URL: https://www.jmilne.org/math/xnotes/JVs.pdf ; retrieval `turn795070295view0`. This is passage-level reading, not a whole-book audit. No new bibliography key is needed.

The supplement documents a concrete limit of the attempted generator-bound repair. It supplies no universal cover and no reduction of the main witness gate. Final source/build files were not edited.
