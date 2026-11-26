# Cubic certificates and sources for prompt 69

The fixed test is the Artin factor attached to the augmentation representation on the three roots of \(X^3-269\). The companion research note gives its rational-prime statistic, its exact equivalence to the cyclotomic twist family under Dirichlet GRH, and an unconditional obstruction to recovering its coefficients from congruence classes. The zero-location assertions in the equivalence are hypotheses.

## Replaying the algebraic certificates

The supplement contains the full original `ALP_CONNES/evidence/cubic_logarithmic/` tree and `ALP_CONNES/evidence/pari_build.json` under `ours/replay/`, taken byte for byte from ALP_CONNES checkpoint 22. Run PARI/GP from `ours/replay/` so the paths in the scripts resolve. Use a working copy when invoking a generator, since `writebin` writes to the evidence tree. The producing run identified PARI/GP 2.19.1 and recorded the upstream source digest. Its `certificate_manifest.md` explains the assertions, hypotheses and computations whose attempted full certification did not finish.

The four GP scripts in the paper seed concern the pure cubic field and its real degree-nine first layer. `pure_cubic_base.gp` and `real_cubic_layer1.gp` start from defining polynomials. `real_cubic_field_action.gp` reads `real_cubic_layer1_preliminary.bin` written by the latter script. `real_cubic_logarithmic_gamma.gp` reads the resulting `real_cubic_field_action.bin`. The shorter `real_cubic_layer1_root_replay.gp` and `real_cubic_gamma_root_replay.gp` are included.

Over the complex splitting field \(E=\mathbb Q(\omega,\sqrt[3]{269})\), the base certificate reports ordinary class group \([7,7]\) and degree-zero logarithmic 3-class group \([9,3]\). For \(E_1=\mathbb Q(\mu_9,\sqrt[3]{269})\), `certify_layer1.gp` and `certify_layer1_quotient.gp` are recorded attempts. The successful certificate used a separate argument for an upper bound \(3^6\). The exact group and ordinary class number of this layer remain uncertified by that computation. The successful unramified-class-field, logarithmic-kernel and generator checks are named by the manifest.

There are 17 GP scripts. All seven distinct binary paths in their literal `read(...)` calls have matching retained files and generation code in this tree. No replay consumes the expected binary output of the unfinished full certification. This intake checked archive CRCs, member hashes and file dependencies. The recorded GP outcomes are attributed to the producing checkpoint.

## Exact source references

The earlier proof of the analytic implication AM-H04 is in the separate second run's ALP_MACHINE checkpoint 08, Hecke section lines 212–310. Its complete section is attached in the window-source directory, beside the archived excerpts of the Lean source and their source inventory. The generic theorem is at lines 83–84 of landauWindow.lean. The new proposition in the companion paper applies that theorem to the single product of all Dirichlet twists modulo a fixed modulus, checks the actual Laplace transform and residue sign, and removes higher prime powers only after compensating their exact linear term. No Lean build was performed for this transfer.

The cubic Hecke obstruction in ALP_MACHINE checkpoint 29 is AM-K021, section “The cubic relative period and the exact CM-height boundary.” R6 identifies the cubic Artin factor. R7 gives the class-function obstruction to recovering it by a finite CM-type height identity. The ray-theta period of the final sections supplies the logarithmic derivative. Q3 in `ours/CP29/ALP_MACHINE/research/current_research_status.md` still asks for an arithmetic comparison, its conductor and prime-norm costs, and the every-epsilon estimate.

The geometry references in the earlier ALP_MACHINE packet include the following.

- SGA 3, Exposé I, paragraph and Proposition 4.7.3 on gradings, and Exposé VII_A, sections 6.2–6.4, 7.2–7.4 and 8.1. The canonical English reader uses external native diagram and component sources. The supplement supplies these at the paths selected by its input-root macro.
- SGA 7 I, Exposé VII, sections 2.7 and 2.9 on symmetric biextensions and birigidified torsors. The French reader contains the actual statements. These passages supply the geometric framework for the checkpoint's separate theta calculation.
- SGA 4, Exposé XII **Theorem 5.1 and Corollary 5.2**, Exposé XV Theorem 2.1 and Exposé XVI Theorem 2.1. The French files are respectively `12/12.tex`, `15/15.tex` and `16/16.tex`.
- SGA 5, Exposé VI, paragraphs 1.2.1 and 1.4.2–1.4.3 cover the constructible \(\ell\)-adic sheaf references. The finite-field weight inputs are Deligne, *La conjecture de Weil* I, Theorem 1.6, and II, Corollary 3.3.9.
- The existing pack already contains EGA IV, Theorem 16.11.2 and Remarks 16.11.3(ii), FGA Bourbaki exposés 232 and 236, and SGA 6. All these readings retain their own authorship. The base-change and weight results have the geometric and finite-field scope of their statements.

Calegari's Theorem 1.2 in the attached `S5ArtinWeb.tex` asks that \(\zeta_H(s)\) be nonzero for all real \(0<s<1\). See source lines 148–151. The later workshop's claimed hypothesis is on \(\zeta_H/\zeta_F\) away from \(1/2\) and allows a central zero of arbitrary order. The original theorem, its local conditions on the extension, and the later conditional refinement are separate results.
