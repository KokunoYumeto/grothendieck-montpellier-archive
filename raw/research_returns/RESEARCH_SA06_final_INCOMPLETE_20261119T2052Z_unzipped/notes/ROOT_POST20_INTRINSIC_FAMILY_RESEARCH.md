# Intrinsic proper-family research after checkpoint 20

GPT-6 Astra (OpenAI), ChatGPT Pro mode, `/root`. Research window beginning17:50UTC,19November2026; updated18:12UTC. This note retains attempts and their exact limits. It is not a new universal vanishing or nonvanishing theorem and does not by itself count as hourly main-gate movement.

## 1. Present certified position

C.3bm gives the intrinsic perfect-family presentation for every algebraizable normal strict-local threefold with regular puncture in positive characteristic. C.3bo removes component degrees and Albanese coordinates in that entire branch. C.3bn gives endpoint comparison under the stated regular projective modification hypotheses in every dimension, without requiring SNC support. C.3bp extends the mixed component-Albanese elimination when that higher-dimensional support is SNC. These last conditional scopes must not be confused with an arbitrary-dimensional resolution-existence theorem.

C.3bq now supplies a complete restricted edge/triple correction: the kernel of component restriction is a proper-family relation if every signed triple-point period on the double curves vanishes (in particular if rational dual H2 vanishes). Its ordinary-vanishing corollary separately assumes zero component rational Albanese kernels. C.3br supplies a different complete restricted theorem: no triples plus joint rational Picard restriction surjectivity kills all component degree-zero CH0, including their Albanese kernels. Negative rational double curves give the joint restriction right inverse explicitly. Neither restricted result makes all remaining intrinsic classes vanish.

## 2. Why component Albanese vanishing alone did not solve graph gluing

For E=S union_C T, a Poincare family on a curve A in S restricts along C times its proper parameter to a finite sum of point classes on C externally multiplied by evaluation-line classes on the parameter. A line twist from the parameter can remove a selected degree/Albanese coordinate after rational division, but does not thereby kill the Albanese kernel of the product C times the parameter. A zero component Albanese image does not imply that this perfect edge class vanishes.

The C.3br construction avoids that inference: use the graph of a smooth proper curve through the desired component points, then cancel each of its finitely many edge intersection coefficients by actual rational component divisor lifts at that fixed parameter value. Joint Picard surjectivity is exactly the hypothesis needed for this finite correction. In the triple-free setting the corrected tuple lifts through the actual two-column K-theory fibre sequence. No full Poincare family is required to lift on the other component.

The proposed extension to rational edges with triple points remains a question. One can choose the graph and divisor representatives away from the finitely many triple points. However equality of their edge K0 classes still need not give compatible trivializations in the three-column homotopy totalization. The missing check is the actual vertex K1 obstruction, including whether moving supports away from vertices supplies the required coherent nullhomotopies. This extension has been assigned for independent investigation; it is not asserted here.

## 3. Triple-point periods can lie in a component-Albanese kernel

For a rational dual-complex 2-cycle, the signed marked-point divisor on each edge has degree zero. Pushing the entire signed vector into the direct sum of component Albanese varieties gives zero: at each triple point its two incident contributions on a fixed component cancel with opposite signs. This only places the period vector in the kernel of the edge-to-component Albanese map. It does not force each individual edge period to vanish, and if all components are rational it imposes no additional condition.

A concrete candidate is the union of two smooth transverse quadrics and a plane in P3. Its quadric–quadric edge is a smooth elliptic quartic; the other edges are smooth conics, and the plane cuts four triple points. The dual complex has three vertices, three edges and four faces, hence rational H2 of dimension three. Generic differences of the four points on the elliptic edge need not be torsion over a transcendental algebraically closed field. An explicit isolated-hypersurface and small-resolution construction is being checked by frobenius to test whether this configuration retains ample negative exceptional geometry. No counterexample to ordinary top vanishing is claimed: failure of the sufficient period hypothesis is a different assertion.

The alternative Kollár plumbing route would require its precise contraction input. Root freshly reopened the primary paper https://content.algebraicgeometry.nl/2014-1/2014-1-004.pdf and read the introductory scope and Theorem2 proof in this window; earlier full Lemma15/16 reads remain explicitly recorded by the owner. Artin's cited contraction theorem was not freshly opened by root, and no theorem is imported through an unverified citation. The new explicit hypersurface route is intended to avoid that extra input, if its complete geometry passes.

## 4. The raw valuation detector fails on already certified proper relations

Let a constant SNC surface be defined over an algebraically closed field k0 of characteristic p, extend to k=algebraic closure of k0(u), and use a valuation over u=0. On the smooth strata, localization and purity suggest a normalized residue K_n(generic stratum) to K_(n−1)(constant stratum), compatible with rational closed-cover descent. After normalizing ramification indices it is tempting to seek a map K0(E_k)_Q to K_-1(E_k0)_Q and to use it against ordinary proper-family relations.

That raw target cannot work. In the already certified tetrahedral model, the shifted field summand gives a vertex class kappa{a,u} in K0(E_k)_Q. The explicit proper-symbol family, followed by its actual double boundary, makes this a defining J_K relation. Its valuation residue is ±kappa a in the vertex K1(k0)_Q term. Choose k0=algebraic closure of Fp(v) and a=v, so this residue is nonzero. If k0 is Fpbar the coefficient is torsion instead; the transcendental coefficient-field qualification is essential.

The natural full-product tetrahedral splitting makes the obstruction sharper. For a smooth proper connected parameter P over k0, its degree-minus-one group is the shifted K1(P)_Q term; every endpoint evaluation there is the same global unit, while the SK1 part evaluates to zero. Thus its ordinary smooth-proper endpoint differences are zero, although the residue of the degree-zero proper relation above is nonzero. Merely quotienting the residue target by its own ordinary degree-minus-one proper relations is therefore insufficient. A valid target must account for degenerations of the original proper parameter, including singular special fibres. The cycles owner is recording the exact localization normalization and source audit for this countertest.

This rules out the earlier naive assertion that residues of proper relations necessarily lie in a maximal proper subgroup of a semiabelian presentation of K_-1. The torus already receives nonzero residues of certified proper relations. It does not decide whether some further abelian quotient can survive all bad-reduction relations. No valuation-induced ordinary-quotient map has been proved here.

## 5. Exact searches and source limits

The root searches in this window were:

- `"algebraic equivalence" "K_0" singular varieties proper curves`;
- `"zero cycles" "normal crossing" "Albanese" proper algebraic equivalence`;
- `"Picard" "dual complex" "algebraic K-theory" normal crossings`;
- `"local Chow group" "algebraic equivalence" finite`;
- `"Chow groups" "punctured" "algebraic equivalence"`;
- `Kollar prescribed exceptional divisor negative normal bundle simple normal crossings singularity`;
- `"algebraic equivalence" "local rings" Chow Kurano`;
- `"Chow groups" "algebraic equivalence" "local" Srinivas`;
- `"dual complex" "Picard" "period" normal crossing surface`;
- `"generalized Albanese" "projective" "normal crossing" surface`;
- `"algebraic equivalence" "Levine-Weibel" Chow`;
- `"proper" "algebraic part" "Albanese" singular zero cycles`.

Root opened Dao and Kurano, *Hochster's theta pairing and numerical equivalence*, author primary https://www.isc.meiji.ac.jp/~kurano/ronbun/kurano32.pdf . We read the introductory statements and the entire Remark6.4 proof, authorpp20–21. It compares an affine-parameter algebraic-equivalence relation in G0 with numerical equivalence through Euler/rank arguments. It does not prove finiteness of the proper-perfect-family quotient here, and does not identify that quotient with numerical equivalence. No whole-paper reading is claimed and no new numbered result uses this source.

Search-only leads included Friedlander–Walker semitopological K-theory, Krishna–Park algebraic cobordism modulo algebraic equivalence, Achter–Casalaina-Martin–Vial parameter spaces, and generalized/logarithmic Albanese papers. They are not promoted to opened theorem inputs. In particular, a relation allowing affine parameters, a statement about ordinary covariant Chow cycles, or an algebraic-representative theorem is not silently substituted for actual perfect classes on our fixed singular product with a smooth proper parameter.

The root also read the complete retained `agents/real_weil/POSITIVE_HIGH_RESTRICTION_RESEARCH.md`, `notes/ROOT_FINITE_THICKENING_BOUNDARY_RESEARCH.md`, and `agents/frobenius/C3_SNC_top_RESEARCH.md`, including their supersession scopes. Only the first230lines of the342-line `agents/cycles/absolute_picard_kernel.tex` were freshly reread in this window; no new complete reread is claimed. The higher rational restriction boundary gate remains distinct from this intrinsic top-quotient research.

No literature-absence or priority claim follows from these searches. The failed raw residue route, possible period-failure geometry and new restricted cases are not a substitute for a strictly smaller universal main gate at the scheduled review.

## 6. Subsequent exact method audit

Root read the entire cycles note `agents/cycles/notes/tetrahedral_valuation_method_limit_1811.md`, including the natural TS base-change argument, vanishing of its degree-minus-one proper-relation subgroup, normalized ramification colimit, and the separate nodal G0 warning. Root freshly opened the official Weibel ChapterIII primary https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf and read Lemma6.3 with its complete proof and Ramification6.3.1, chapterp51. The residue convention is partial({uniformizer,unit})=unit, and dividing by the ramification index gives exactly the compatible rational map on the selected field summand. This independently confirms the specified method failure; it does not establish a general singular-scheme specialization map.

## 7. Audited subsequent cases and limits,18:29UTC

C.3bs now proves the precise H²(Delta,Q)=0 extension of C.3br, with the separate full joint rational Picard restriction hypothesis. Root read the entire DC.1–DC.6 proof and both full independent receipts; the final source differs from the audited draft only in its status heading. Its all-j constant pullback right inverse gives the actual edge-fibre injections for every fixed proper parameter. This removes all component degree-zero classes in that scope; nonzero H² still carries the possible K1(parameter) vertex obstruction. The earlier question in section2 is therefore answered only in this precisely stated branch.

The explicit NP.1–NP.8 construction and NP.9 Picard-span exclusion have also passed root and independent audits. Root read the entire proofs and the19 finite certificates; the final cycles receipt and owner report were subsequently read at18:28UTC. They remain auxiliary research records, without an ordinary-Chow survival claim and without changing the universal main gate. In particular, scalar monodromy exclusion for component Picard classes is not already an exclusion for proper parameter classes whose coefficients themselves have monodromy.

## 8. Additional searches and unsuccessful original SGA acquisition

Further exact queries included `"Somekawa" "algebraic equivalence"`, `"K-theory" "proper" "algebraic equivalence" singular`, `"semiabelian" "K-group" "algebraic" "equivalence"`, `Somekawa group semiabelian algebraic equivalence proper families K theory`, `SGA 6 X 7.11 7.12 equivalence algebrique K pdf`, `"SGA 6" "7.11" "algébrique"`, `"SGA 6" "Spécialisation" "7."`, `"SGA 6" "7.11" "page"`, `"SGA 6" "Spécialisation en théorie" "Appendice"`, `"SGA 6" "K" "7.12"`, `"SGA6.pdf"`, `"sga6" "pdf" Grothendieck 1971 225`, `"Formalisme des intersections sur les schémas algébriques propres" pdf`, `"Jussila" "BFb" "intersections"`, `"SGA 6" "7.12" spécialisation`, `"SGA 6" pdf "560"`, and targeted page575/579/580 queries. The last page guesses did not furnish the required original proof.

The original full SGA6 PDF at https://wstein.org/sga/sga/pdf/sga6.pdf exceeded the web tool's size limit (54,325,694bytes). The archive index and individual page576/577 HTML pages opened, but their JPEG calls returned only a textual image placeholder, not an image actually viewed. The retained program `code/fetch_sga6_specialization_pages.py` attempted the fifteen original page JPEGs570–584 with four workers and30second request timeouts; all fifteen returned HTTP403. It ran18:18:47.161279–18:19:10.212732UTC,23.051512043seconds. The complete failures are retained in `logs/sga6_specialization_acquisition.json`; no OCR text or successful original-image acquisition resulted.

The official chapter DOI10.1007/BFb0066294, ExposéXpp519–594, was located, but https://link.springer.com/content/pdf/10.1007/BFb0066294.pdf was inaccessible. The iut-theory.org and www variants timed out. https://geotoppos.org/divers/SGA6.pdf opened only a24page front-matter/table-of-contents file, not ExposéX. The new machine reconstruction at grothendiecksga.com was returned in search snippets, while direct French and English page opens failed (English retried18:28UTC). No original SGA6X7.11–7.12 proof is claimed read or imported. Search snippets suggest a proper-perfect definition at7.11 and a coherent-G0 specialization at7.12, with a perfect-K interpretation when both fibres are regular. This is a search lead only; it supplies no singular-perfect or negative-K specialization theorem for our quotient.

The exact targeted snippet queries were `site:grothendiecksga.com/read/sga6/fr/X-7.html "7.11" "parfait"`, the same URL with `"7.12" "régulier"`, and the same URL with `"K_" "7.3.1"`. Search-only Somekawa-related leads included Kahn–Yamazaki arXiv1108.2764, Gazaki arXiv1805.05496, Déglise's dimensional homotopy work and Somekawa1990. None has yet become an opened primary theorem input in this block. No priority or literature-absence claim is made.
