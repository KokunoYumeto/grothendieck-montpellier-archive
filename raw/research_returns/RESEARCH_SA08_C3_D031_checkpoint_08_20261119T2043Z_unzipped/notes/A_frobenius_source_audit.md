# Weight Frobenius and exact saturation comparison

Read on 19 November 2026 by GPT-6 Astra (OpenAI), ChatGPT Pro mode, RESEARCH_SA08_C3_D031. We claim no priority.

Primary source: Bhargav Bhatt, Jacob Lurie and Akhil Mathew, *Revisiting the de Rham–Witt complex*, arXiv:1805.05501v3. The opened author PDF at https://people.math.harvard.edu/~lurie/papers/Crystalline.pdf has141 pages. It was read through the web PDF viewer; the attempted direct local author-PDF download returned403, as retained in the fetch log. That failed local download does not describe the separately successful PDF opening.

The arXiv v3 source at https://arxiv.org/src/1805.05501v3 was successfully fetched and extracted. Its archive has121,163 bytes and SHA256 `6d75a375457db2da2a5265a6080ea9e2a53b60db04e3ed0ba7eb7c650ac221de`; the fetch log records6.868 seconds. The arXiv final PDF has158 pages and is identified separately from the author PDF. No page-number transfer between the two is assumed.

The exact definitions used were read in `crystalline-v3-submitted-to-journal.tex`: eta and its alpha map at lines588–605; the filtered-colimit saturation construction at678–692; completion at859–874; and the Dieudonné algebra definition at1404–1413. In the author PDF these are Construction2.1.3 and Remark2.1.4,p13; Proposition2.3.1,p15; Construction2.5.1,p18; and Definition3.1.2,p29. The lifting branch reopened the primary author PDF and independently checked these locators and the entire A-WF01 proof.

A-WF01 supplies the actual endomorphism F on a supported torsionfree strict PD theory: its value in weight w and form degree q is multiplication by p^(w−q). Its alpha map is multiplication by p^w. The proof computes the coefficient colimit by the explicit stage-r subgroup p^(−rw)R inside Q; it then computes V on those coefficients and their zero images in every completion quotient. Every claimed failure is tied to these exact maps. No assertion about a different Frobenius or about a general comparison between the constructions is made.

## Literature searches preceding the recorded calculations

The root searched `"divided power algebra" "matrix factorization" ideal` and `"divided power" "saturation" "acyclic" differential positive degrees` at approximately18:47UTC. The returned matrix-factorization material did not supply the all-prime assertion of A-P01. That assertion is proved directly by the displayed coefficient matrices, colon identities, complete low-weight resolution, and exact integral primitive lattice.

Earlier source searches for divided-power acyclic closures, integral odd-generator Poincaré lemmas, saturated de Rham constructions, and strict cochain comparisons led to the primary sources recorded in the bibliography and branch audit notes. No search-result summary is used as a theorem. We do not assert originality of the elementary matrix-factorization calculation or of the eta construction; the exact application and maps used here are proved in full.
