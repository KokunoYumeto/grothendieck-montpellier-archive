# Square-zero K₂ source audit and recovery

Reconstructed after the 10:14 UTC scratch reset. The original source readings and symbol checks preceded that reset. The original van der Kallen scan was read visually on all four pages; Weibel's exact modern convention was reopened on recovery at the URLs below.

- Wilberd van der Kallen (1971), *Le K₂ des nombres duaux*, C. R. Acad. Sci. Paris A273, A1204–A1207, <https://webspace.science.uu.nl/~kalle101/K2nd1971.pdf>. Unnumbered theorem and corollary A1204; proof A1205–A1207. The isomorphism for dual numbers assumes 1/2 in the base ring, not characteristic zero.
- Charles Weibel, *The K-book*, author-hosted Chapter III, <https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf>. Definition5.11 p43 says `⟨r,s⟩={r,1−rs}` for r a unit. Theorem5.11.1(b) p44 is the relative Dennis–Stein presentation, for an ideal contained in the Jacobson radical. Exercise5.14(a)–(c) pp46–47 gives the differential quotient, its two-infinitesimal-symbol kernel, and the odd-characteristic dual-number isomorphism.

The map with `{1+tc,u}↦+tc dlog u` is **the negative** of the map of Exercise5.14(a). It sends `⟨m,r⟩` to `−m dr`. This conventional negation was explicitly corrected before09:59:01 UTC in the original audit and is retained in all reconstructed files. In characteristic two the proof uses the quotient only; it does not claim the two-infinitesimal symbols vanish or that sheaf cohomology is surjected onto.

Fresh downloads after recovery reproduce the original hashes exactly:

| File | Bytes | SHA256 |
|---|---:|---|
| van_der_Kallen1971_dual_numbers.pdf | 669146 | 75508c6ae2fe8cccc19aab19caa4e9981aaf3adc1cede609950807a0ef1b72f2 |
| Weibel_Kbook_III.pdf | 708651 | ba1bc2d25680ab25c4baadc5ab28e39d1077dc66bb12ca4e2174b6cb55f81307 |

The complete acquisition program, fresh timings, and per-source UTC are in `code/acquire_residual_and_K2_sources.py`, `output/acquire_residual_and_K2_sources.out`, and `output/residual_and_K2_sources_manifest.json`.
