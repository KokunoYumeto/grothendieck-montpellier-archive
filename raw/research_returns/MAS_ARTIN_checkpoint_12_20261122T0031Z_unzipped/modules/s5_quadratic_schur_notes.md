# MA-RB-005: quadratic Schur tests

Date: 2026-11-21.
Author and author checker: GPT-6 Astra Pro; effort inherited/not externally exposed; MAS_ARTIN /root/s5_audit.

## Result and current scope

The complete proof is in modules/s5_quadratic_schur.tex, equations MA-RB.46–60. Its complete author post-writing reading passed. Root and pf26_audit have now independently read the entire proof and passed it; root has integrated the module.

At the actual remaining comparison pole gamma in (1/2,1), the four partial twisted symmetric-square functions have exact orders

1. Q4: v1+e−k.
2. Q4_eta: v0+e+k.
3. Q5: v0+n+x1.
4. Q5_eta: b+v1+n+x1+2k.

Takeda's actual holomorphy theorem applies to all four. The new five-dimensional exterior-square functions equal the first two by a general GSp4 weight identity, so no additional exterior-square lift is assumed. The exceptional Schur factor ratio is Delta(T)=((1+T)/(1−T))^2 for both symmetric and exterior squares; the external sign twist replaces it by its inverse.

The only nonautomatic order inequality is the already proved v1+e≥k. The formal genuine order character k(V eta+W) of MA-RB-004 gives orders (0,k,0,3k) and regular order9k. These specified quadratic and ordinary exterior-power holomorphy constraints do not improve the residual arithmetic gate. They do imply extra actual zeros of Q4_eta and Q5_eta; no nonvanishing of those functions is available from the theorem used.

This is not a proof of R_B, a proof of unconditional comparison, an arithmetic counterexample, or a claim about all possible Schur functors. Higher symmetric-power holomorphy is not inferred from a quadratic theorem. The analytic remaining gate remains the common real zero of B and L_(V eta)L_X on the interval specified in MA-RB-002.

## Verification and inputs

Read the complete written proof after writing. Checked every entry of the new character calculation, the symbolic ten-weight identity, all exceptional multiplicities and reciprocal-polynomial orientations, partial factors at gamma, unitary hypotheses, exact pointwise orders, and formal witness. The extra ordinary exterior-power identities are elementary complement identities for determinant-one reciprocal multisets and the symplectic four-dimensional multiset.

The new executable exact certificate checks two character identities, one symbolic general GSp4 identity, four exceptional ratios, and six order expressions. It reuses the previously verified S5 table and does not rerun the old certificates. The script and JSON are checks/s5/s5_quadratic_schur.py and .json; execution passed.

Freshly read the supplied Calegari LaTeX surrounding Lemma4.2 and its complete proof/parameter formula, and Theorem4.7 through Lemma4.8's local-factor proof (source lines548–606 and730–816). The earlier verified similitude theorem, finite table and all-place comparison data are retained. Takeda Theorem7.1 and its terminal proof, primary printed pp49–50, were freshly read in the MA-RB-002 audit; this module verifies the additional representation/twist hypotheses, without claiming a new full audit of its upstream Eisenstein and integral inputs.

Root owns integration and final packaging.

The fresh peer source review detected the literal mu plus mu error in Calegari Lemma4.2. MA-S5-008 now supplies the complete corrected degree1+5 constituent proof and classification/self-twist completion. A brief explicit forward reference was added to RB005 after its reviews; this does not change its Schur calculations or conclusion.
