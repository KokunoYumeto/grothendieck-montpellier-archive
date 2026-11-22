# Root literature search and source audit

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026. No priority is claimed for any result or proof in this package.

## Searches for existing work on the cotes

Both search engines were used, with exact and combined queries including “Grothendieck Chirurgie des surfaces conformes”, “Grothendieck cote 68 étude”, and “Grothendieck conformal surgery study”. We opened Michel Hua's current project record at https://hexagonmath.org/2611.00125v2 (version 2 dated 5 November 2026), its repository description, and the publisher-hosted transcription of the letter to Bers at https://csg.igrothendieck.org/wp-content/uploads/2024/09/L28d.pdf. The latter is a transcription of the historical letter, not a mathematical research treatment. We found the explicitly AI-produced modernized readings in Michel Hua's project. We did not find another dedicated published mathematical study of cotes67–68 in these searches. This is a search result with stated scope, not a proof of absence and not a novelty claim.

The quarter-theorem obstruction, orange-slice extremal-length argument and marking correction were already credited to Michel Hua's project in the supplied study. We retain that credit, independently reprove the arguments, and identify the actual new checks in CHECK_EVENTS.tsv. We do not attribute the present AI-produced manuscript to a person.

## Capping, range and collar searches

Queries included “grafting conformal radius”, “hyperbolic conformal radii gradient”, “conformal radii Strebel hyperbolic”, “geodesic boundary collar pointwise hyperbolic metric”, and “hyperbolic boundary Neumann monotonicity conformal”. The useful primary works were Mondello2011, Solynin1999, Fırat2021/2023, Ahlfors–Bers1960, and Wolpert's cusp-metric paper. Exact opened locators are in the bibliography and the individual proof notes.

Fırat2023 AppendixB equation(B.1) already identifies a logarithmic-radius derivative of the on-shell action in its sphere setting. The paper now credits this explicitly before the energy theorem. We do not infer the all-genus strict convexity or exact image from that formula; the moving-seam energy proof, boundary exclusion and recession comparison are supplied in full. The finite Hessian computation is labelled diagnostic throughout.

The general collar answer uses the uniquely determined curvature/Neumann equation. The sign-changing shape example is independently proved twice: through the shape derivative and through a completely specified supersolution with n=10000 and epsilon=10^-14. The only finite claims in the explicit construction are symbolic identities and exact inequalities; no numerical solution of the metric equation is asserted.

## Plumbing source comparisons

We opened the original Kra1990 full text, Wolpert1990 original PDF, Hubbard–Koch2014 original PDF/source, Hinich2010 original arXivv2, and Earle–Sipe1991 original published PDF. Relevant locators are recorded in the paper and bibliography. The retained-coordinate equation zw=t is checked directly, and its first-order tensor is kept distinct from a finite global coordinate. The Hinich counterexample is given with exact rational parameters and two independent arithmetic implementations; the paper corrects the swapped attachment wording in the arXivv2 paragraph.

Matsumoto's original2019 lecture notes were opened at https://www.ms.u-tokyo.ac.jp/publication/docs/lecturenotes17-matsumoto.pdf. Printedp27 and bibliography item24 onp61 really refer to *Holomorphic plumbing coordinates*, ContempMath575(2012)41–52. The §13/TheoremII locator is preserved as that later author's locator, not silently transferred to the different *On holomorphic families* chapter in volume573.

Fresh exact-title searches, the AMS chapter and whole-volume URLs, GoogleBooks' public metadata and page41 preview, and the public Academia book record were tried. The Academia record contains only front matter. The four ordinaryHTTP requests in `code/root_public_preview.py` returned429 for the two Google endpoints and403 for the two AMS endpoints. The recorded batch took14.749523993seconds. No authenticated session, challenge handling or request for a private file was used. The initial script launch failed before any request because the optional requests module was unavailable; the archived script now uses urllib from the standard library.

## Algebraic-cycle source check

We directly reread Ancona's original statements corresponding to the numerical Hodge-standard result and to the infinitely-many-primes corollary; the all-prime conclusion does not follow just by removing the qualification on the latter. Broe's original2026 preprint theorem and Kahn2003's original definitions and Theorem1 were inspected for the alternative deduction; Ancona's specialization theorem is applied with its stated coefficients. The manuscript expressly records the preprint dependency and the absence of an independent full-proof audit of that preprint. PartB's source notes retain the separate original-text access limitations for Gabber1994, Fujiwara1995 and Lieberman1968.

## What the search does not establish

Search failure does not make a proposition false, and inaccessible metadata does not verify a theorem. No unavailable original is marked opened because a later paper cites it. Conversely, the full proofs supplied here do not depend on a claim of originality or on the authority of the supplied AI study. Exact user-required source openings remain distinct requirements until completed.

## Original classics recovered before checkpoint03

19November2026,13:10–13:15UTC. Root opened Lavrentiev1934, *On the theory of conformal mappings*, original Russian87-page PDF from MathNet. PartI section2 Theorem3 (printed169–173) gives |F0′(z0)F1′(z1)|>=1/|z1-z0|^2 for normalized maps from disjoint simply connected domains to the disc. Taking reciprocals gives the two-radius product bound. Printed169 and173 were rendered and visually inspected; the Koebe theorem on173 and its proof on174 give the quarter bound and slit equality. Cache retrieval SHA/timing is in code/root_classic_sources_output.json. This supplies an actual original Lavrentiev locator; it does not claim that an original paper by Koebe himself was opened.

Bers1974 original four-page announcement, BullAMS80,1219–1222, opened all pages via the public original scan. Theorems1–4 and7 inspected; Theorem4 is an announcement, not a complete proof. Bers1975 original MathScand36,12–16 downloaded from the journal's migrated MSP endpoint; printed12–13 visually inspected for nodal type, signature and deformation definitions. Bers1981 original *Finite-dimensional Teichmüller spaces and generalizations*, BullAMS5,131–172, opened through Sarah Koch's University of Michigan copy. Exact bordered-space conventions and dimension occur in section2(F),p139; bordered extremal problem and doubling in section3(F),p141; dimension conclusion in4(E),p143. Sections15(D–G),159–160 explicitly distinguish real FN coordinates written as complex numbers from the actual complex structure. Section16(A) calls its lengthy proof a sketch. The paper cites only the checked scope.

Lehto–Virtanen1973 official Springer book metadata was opened; full mathematical text still not obtained. Exact-title searches in both engines found bibliographies and catalogue records, not the book. Pfluger1960/1961 was identified precisely as JIndianMathSoc(NS)24,401–412, GoldenJubilee1960 volume published1961. Penn's serial archive points to publicly readable early volumes only, and the exact GoogleBooks volume is snippet-only. No unseen theorem from either requested work is used.
