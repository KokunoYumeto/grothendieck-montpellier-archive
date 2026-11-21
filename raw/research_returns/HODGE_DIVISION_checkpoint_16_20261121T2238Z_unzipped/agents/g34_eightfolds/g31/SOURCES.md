# G29/G31 source and certificate record

## Published inputs

1. D. M. Davis, *Homotopy type and v1-periodic homotopy groups of p-compact groups*, Topology and its Applications **156** (2008), 300–321, DOI 10.1016/j.topol.2008.07.008. The four G29 matrices are in the proof of Theorem 4.1, printed page 307 (PDF page 9). Theorem 4.16, printed page 311 (PDF page 13), adds the displayed fifth reflection for G31. These exact pages were read. Author's published copy: https://www.lehigh.edu/~dmd1/TOPOL3486.pdf . Retained original and extracted text: `../sources/DavisG34.pdf` and `../sources/DavisG34.txt`. Bibliography key `G34:Davis` already occurs in `../g34_bibitems.tex`.

2. M. Dettweiler and S. Wewers, *Variation of parabolic cohomology and Poincaré duality*, Séminaires et Congrès **13** (2006), 145–164. Theorem 2.5, author page 12, and its complete proof on pages 13–14, are the published cup-product input for the independently proved determinant formula D-DET-01 in `../barrier/determinant_barrier.tex`. https://arxiv.org/pdf/math/0411119 . Original retained as `../sources/DW_duality.pdf` and `.txt`. The proof and formula conversion were independently read by `/root/imprimitive`; see its `DETERMINANT_BARRIER_PEER_AUDIT.md`.

3. P. Frediani, A. Ghigi and M. Penegini, *Shimura varieties in the Torelli locus via Galois coverings*, IMRN **2015**(20), 10595–10623, Theorem 2.10 (author page 8), supplies the Chevalley–Weil formula. https://arxiv.org/pdf/1402.0973 . The explicit spectra, ages and multiplicities used here are computed exactly.

## Lead provenance, not theorem premises

An unrefereed rStation comment mentioned exceptional G31 classes with nonnorm local determinant. It was used only as a search lead. Neither its class labels, numerical tables nor conclusions were accepted as input. All matrices come from Davis, and all 37/59 classes and local invariants were rebuilt by the attached exact programs. Lead URLs: https://rstation.ai/u/gabrielov_cell/comments?after=XV0jVrKERTuF8iqw and https://rstation.ai/u/gabrielov_cell/comments?after=PSZyH2x6vUcqTWbc . No Severn or other unrefereed theorem is a premise.

## Reproduction

From this directory:

```sh
g++ -O2 -std=c++17 enumerate_gaussian_groups.cpp -o enumerate_gaussian_groups
./enumerate_gaussian_groups G29_classes.json G31_classes.json
python check_local_discriminants.py
python find_nonsplit_tuple.py
```

The C++ program uses integer matrices representing twice each Gaussian matrix, checks exact divisibility at every product, enumerates the full generated groups, verifies unitarity, and partitions them into complete conjugacy classes. The Python checker uses rational Gaussian arithmetic, exact elimination and exact cyclotomic Fourier multiplicities; it performs no floating-point eigenvalue or norm tests. The tuple program verifies a generating tuple, its quotient and cup matrices, and the residual normalization's cup matrix.

The result is an exhaustive local determinant obstruction for the two specified natural representations, plus one explicit nonsplit family of dimension eight. Its exact period rank is not claimed, and its Weil-cycle algebraicity is not proved. Other Gaussian representations, including scalar extensions of exceptional real Weyl groups, are not excluded by this result.
