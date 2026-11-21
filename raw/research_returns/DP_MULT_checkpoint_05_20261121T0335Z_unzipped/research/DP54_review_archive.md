# DP54: independent complete proof and integrated preservation review

**Verdict: PASS.** The entire original memo, §§1–8, and the entire intended integrated theorem, proof, and final scope paragraph were actually read and challenged. No mathematical correction was required. Main paper was not edited.

## Reading provenance

- Checker: `/root/archive_binomial`, GPT-6 Astra Pro; runtime effort is not exposed.
- Date: 2026-11-21 UTC.
- Original whole reading observed at 03:30:28; complete integrated reading observed at 03:33:42; independent source verification completed at 03:33:55.
- Original SHA256: `8f4af88346a1da513b3b462df85eb43cc19d8beb49d9bdd7a62f1c17e0312349`.
- Integrated SHA256: `326e06c8d81f55841abfe947851aa8931aa3c9793caee1853632586b17194b94`.
- Exact complete theorem/proof hash, source image hashes, and actual main insertion count are preserved in `late_proof_snapshots/DP54_archive_review_metadata.json`. These are reading records, not a claim of machine proof or Lean execution.

## Mathematical challenge

1. **Ampleness and sign.** Equality with the positive canonical principal polarization is essential and is present. On the algebraically closed closed fibre, the difference from an ample theta line has zero associated homomorphism and belongs to Picard zero. Surjectivity of the ample theta homomorphism makes the difference a translate. Thus the particular line is ample. Descent of ampleness and spreading from the closed fibre apply to the proper scheme over the noetherian local DVR; every open neighbourhood of the closed point is the whole base. This avoids the false implication that every line inducing an isogeny is ample.

2. **Integral finite thickenings and extension.** The smooth zero section has finite free infinitesimal neighbourhoods, represented in the chosen formal parameters by the truncated power-series ring. Restricting the formal frame to such a neighbourhood gives a genuine finite frame. Serre vanishing applies to the coherent ideal power and yields an integral restriction surjection. The prescribed coefficient `U^{-kappa}` is integral with value one, so the lift is nonzero and has unit algebraic prefactor. No algebraization of an infinite frame is assumed.

3. **Rational logarithm substitution.** Although the exponential coordinates can have denominators, their zero constant term preserves total order over the fraction field. Therefore the integral finite-jet congruence survives substitution. In a finite product of copies every prefactor error has total degree beyond the selected bound, so the same section can be used in every copy.

4. **Square tensor levels and exact valuations.** A finite jet functional applied to the exponential with scalar exponent is a polynomial in that scalar. The minimum coefficient valuation supplies the displayed congruence bound; selecting a sufficiently deep congruence to one preserves every finite nonzero selected value. Arbitrarily large positive integers in that congruence class permit the independent Serre threshold to be met with square tensor exponent. The normalization by a power of `M` is a unit. Nothing requires the tensor power to be bounded as derivative order grows.

5. **Sharp ordinary and harmonic sequences.** Every nonzero finite witness from the previously proved local results can be treated separately. Product jet matching supplies the two-column harmonic witnesses with the same section in both copies. This transfers each selected valuation to a global algebraic section of a possibly different power. It proves no asymptotic statement for a single fixed section or fixed tensor power and no membership in the prescribed translated theta family. The distinction is explicit throughout.

6. **Number-field approximation.** The selected localization of the cyclotomic ring has the stated unramified degree-three completion. The curve, automorphism, polarization, trace-one endomorphism, and line descend to that localization. Proper coherent cohomology makes the section module finite; flatness of the abelian scheme and invertibility of the sheaf imply torsion-freeness, hence freeness over the DVR. Flat cohomology base change identifies the completed module. Density in a finite free basis and continuity of every finite linear or product-polynomial jet evaluation preserve finitely many nonzero valuations and the unit value at zero. Exact formal coefficients need not descend, and the theorem correctly does not claim that they do.

## Exact primary sources independently read

Original rendered pages 117, 118, and 119 of Milne's 1986 *Abelian Varieties* were actually viewed. Proposition 9.2 and the following definition of Picard zero on p.118 give the kernel characterization; Proposition 10.1 on p.119 states the surjectivity for an ample line over an algebraically closed field. The local PNG hashes are recorded. The source is the official author copy: https://www.jmilne.org/math/articles/1986b.pdf .

The following current Stacks statements were opened and read directly:

- Lemma35.25.6, within Tag02LB: fpqc descent of relative ampleness of a fixed invertible sheaf.
- Lemma30.21.4, Tag0D2N: closed-fibre ampleness spreads over a neighbourhood under properness and noetherian base.
- Lemma30.16.1(4), Tag0B5T: Serre vanishing in precisely the proper/noetherian/ample/coherent form used; part(3) also gives finite coherent cohomology. The same ampleness argument applies over the number-field localization if that exact finiteness locator is desired in the final paragraph.
- Lemma30.16.2, Tag02O1: corresponding relative higher-direct-image vanishing.
- Lemma30.5.2(2), Tag02KH: cohomology commutes with flat base change for a quasi-compact quasi-separated morphism and quasi-coherent sheaf.

An earlier combined source-output call was truncated; no source-reading claim is based on that failed output. The actual readable opens and pixel views above were performed separately afterward.

## Preserved scope

The theorem now proves that each finite sharp local kernel jet can occur in a global algebraic theta section at a sufficiently large square tensor level. It supplies neither an effective tensor threshold nor heights/norms/costs, neither a fixed section realizing all orders nor the source's specified translated family, and no shorter-chain or full global multiplicity conclusion. Those are real remaining quantitative and family-identification gates, not objections to the established finite-jet existence theorem.
