# Gaussian Weyl-component sources and finite certificates

1. R. W. Carter, *Conjugacy classes in the Weyl group*, Compositio Mathematica25 (1972),1–59. Primary PDF https://www.numdam.org/item/CM_1972__25_1_1_0.pdf retained as `Carter1972.pdf` and layout text. Visually read Table1 p48, Proposition21/Table3 pp22–23, Table9 p50 (E6), Table10 pp51–52 (E7), and Table11 pp52–54 (E8). The class classification and completeness are published inputs.

2. Author-maintained CHEVIE files by M. Geck, J. Michel and the CHEVIE team, `pkg/chevie/tbl/weyle6.g`, `weyle7.g`, `weyle8.g`, in https://github.com/jmichel7/gap3-jm . The files were retrieved by `/root`; immutable hashes are retained in the compact witness JSON. The explicit E6/E7 class words and Cartan matrices were read directly. At the group specialization v=q=1 their meaning is unchanged. CHEVIE manual §87.1, https://webusers.imj-prg.fr/~jean.michel/gap3/htm/chap087.htm, explicitly documents `classtext` as complete class representatives. The retained authored input JSON contains mathematical witness data, not the full third-party library code. Background publication: J. Michel, *The development version of the CHEVIE package of GAP3*, Journal of Algebra435(2015),308–336.

3. A. M. Cohen, *Finite complex reflection groups*, Ann. Sci. ENS9(1976),379–436, DOI10.24033/asens.1313; full erratum ENS11(1978),613, DOI10.24033/asens.1358. For the new Gaussian reduction, Lemma2.7 pp389–390 and Proposition2.13 pp391–392 were read in addition to the previously checked classification and corrected Proposition5.14. Sources: https://www.numdam.org/article/ASENS_1976_4_9_3_379_0.pdf and https://www.numdam.org/article/ASENS_1978_4_11_4_613_0.pdf . Uniqueness of imprimitivity and D4 triality normalizers are used with their precise exceptions.

4. G. Malle, *On the rationality and fake degrees of characters of cyclotomic algebras*, J. Math. Sci. Univ. Tokyo6(1999),647–677. Tables8.1–8.2 pp674–675 were re-read visually for the Gaussian field, including the omissions explained on p676. https://www.ms.u-tokyo.ac.jp/journal/pdf/jms060402.pdf . These leave G8 in rank2 and G29/G31 in rank4 among nonreal primitive reflection groups over Q(i).

5. E. Looijenga, *Prym representations of mapping class groups*, Geometriae Dedicata64(1997),69–83, DOI10.1023/A:1004909416648. The hyperbolic cyclic Prym input in D-GAUSS02 is Proposition2.2, authorp5, with cut-surface proofpp8–9; actual variation rank descent is proved in the new argument. Original author PS https://webspace.science.uu.nl/~looij101/pr2.ps is retained with converted PDF/text by `/root/imprimitive`. Its full cited proof was independently read in `../MONOMIAL_SIXFOLD_AUDIT.md`.

The elementary rational normalizer proofs, all-rank A_m excess argument, cyclic-factor isogeny and induced-block comparison are new proof text. The F4 root realization and Phi matrix are the already independently checked data of D-GF4-01. No unrefereed Weyl-source theorem or numerical period test is a premise.

## Commands

```sh
python check_e6_e7.py
g++ -O2 -std=c++17 enumerate_f4_gaussian.cpp -o enumerate_f4_gaussian
./enumerate_f4_gaussian F4_gaussian_classes.json
python check_f4_gaussian.py
python audit_e8_local.py
```

The E6/E7 computations use the compact retained witness inputs after their first extraction. The F4 program independently enumerates all4608 elements and58classes. The E8 audit uses root's compact mathematical class-word data and compares all224 local invariants through a different exact arithmetic backend and determinant method. None of these commands claims actual E8 period rank nine.
