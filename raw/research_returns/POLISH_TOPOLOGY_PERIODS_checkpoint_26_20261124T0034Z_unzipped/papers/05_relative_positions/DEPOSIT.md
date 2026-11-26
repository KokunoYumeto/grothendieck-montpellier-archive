# Deposit preparation — PAPER-05, provisional

Title: The genus of Grothendieck’s relative-position surface

Author line: intentionally empty.

## Abstract

For a finite labelled non-pencil arrangement of projective pseudolines, we study the surface formed by ordinary one-element extensions and exceptional sweeps around the old lines. We give its Euler characteristic and nonorientable genus in terms of the numbers of extensions with specified zero sets, and exhibit two arrangements of six lines whose surfaces have 23 and 47 crosscaps. We prove a marked puncture comparison with the rank-three extension complex and identify the dual surface as a selected subcomplex after Möbius-band replacement. We characterize the full image of signed deployed polygons, reconstruct their weighted incidences, and give an explicit six-line counterexample to a proposed local triangle criterion. Exact finite calculations are supplied as additional certificates. The mathematics and text were produced by GPT-6 Astra (ChatGPT Pro mode); no human has checked the work.

Subject: topology of finite cell complexes; oriented matroids and pseudoline arrangements.

Keywords: extension space; nonorientable surface; relative position; signed polygon; Euler characteristic; Möbius band.

## Eight opening requirements

| Requirement | Location |
|---|---|
| Title and historical question | Title and Section 1; Grothendieck cote154 quotation, with PDF/archive/handwritten numbering distinguished |
| Abstract credit and method | Abstract and final Note on method |
| Full main statements | Section 1, Theorems1.1–1.5, including the marked comparison and complete polygon criterion |
| Significance | Section1 explains why the surface genus depends on extension multiplicities and can distinguish arrangements |
| Exact division of credit | Section1 and Sections3,7,8; Sturmfels–Ziegler, Las Vergnas via Bailey, Folkman–Lawrence via Richter-Gebert–Ziegler, and Hua are explicitly credited |
| Earlier and recent context | Section1, Section9 and eight bibliography records; broader primary comparison remains tracked |
| Scope | Section9; finite non-pencil arrangements, pseudoline extensions, and precise distinction from straight positions |
| Proof mechanism | Section1 proof overview; local links, alternating counts, marked gluing, signed chirotope and packet reconstruction |

## Preceding reviewed revision (10:01 UTC)

The preceding reviewed revision has41pages. Proposition8.7, pp.37–39, now constructs both the strict-transform cellulation and the explicit dual cellulation with234vertices,468edges and229faces, each face indexed by an ordinary straight position. Section6 prints the exact candidate, corner and basis-pair counts. Proposition3.1 states the contraction restriction on every extension except the two designated parallel points. All24changed pages were actually viewed, and the17unchanged pages were verified pixel-identical; the final method note was re-viewed after its layout correction. Three final fresh-copy pdfLaTeX passes have no warnings or boxes. Exact hashes are in notes/paper05_scope_reconciliation_release.json. The portable build uses the three local TeX inputs and no downloads.

## Checking and limits

Frozen independent records cover the counting identities and polygon arguments. Earlier local surface candidates required explicit post-freeze exceptional-adjacency clarifications. A later separate statement-only local-surface derivation was frozen before target comparison in notes/paper05_fresh_independent_surface.md; its exact scope and hash are recorded with it. The subsequent notes/paper05_fresh_surface_after_source_comparison.md separately checks the live proof, source hypotheses, and global pre-exception boundary and Möbius-band alignment; those after-source checks are not relabelled independent. The marked comparison now has a complete separate frozen statement-only graph-of-spaces derivation, including every labelled peripheral loop and the selected-square, whole-one-skeleton and fundamental-group conclusions. The full source comparison found no gap and required no post-freeze repair. Additional cell counts and blow-down formulas were checked after source access, separately from that independent derivation. The straight-position counts have two new implementations using different methods; the new explicit band replacement also realizes all the source numerical cell counts, without identifying an unspecified source gluing. The elementary tether/chord distinction is proved, while its archival interpretation remains pending direct inspection of the cited page.

## Authors carried and filing

Primary work carried: Alexander Grothendieck; Bernd Sturmfels; Günter M. Ziegler; Michel Las Vergnas; G. D. Bailey; Jon Folkman; Jim Lawrence; Jürgen Richter-Gebert; G. Liu; M. Hua. The authors and exact contribution locators are recorded for possible later notification; no message has been sent.

The method note names GPT-6 Astra, the separate instances’ actual checking scopes, earlier Claude Opus5.5 checks, and the absence of human checking. Newly authored text and code are dedicated under CC0 1.0. Proposed destination: homotopy-and-categories-workbench. The registry number, permanent work page, actual version commit and deposit manifest await assignment. No remote deposit is claimed.


## 2026-11-23T10:35:52.656355+00:00: independent incidence release

The current synchronized PDF remains41pages. Only page20 changed and was actually inspected; the other40pages have identical pixels to the preceding reviewed pair. Three pdfLaTeX passes succeeded, final log clean. The new named program **Incidence polygon gluing** independently reconstructs every finite endpoint pairing from extension incidences. All721faces,1592paired sides and6368endpoint flags agree; independent homology now uses these new pairings. Records: `../../notes/paper05_incidence_gluing_audit.md` and `../../notes/paper05_incidence_release.json`. Seven exact source scopes are accepted; C06 identification and the signed-polygon main gate remain separate.

Current source SHA256: `8a386a192b197e3a2465ece5153e1cf60741fd77b05000f6e86b04c77863dbc7`. Current PDF SHA256: `79c2a88b5188c6394166cac98223dc3557e5b21a170ff9c0e8a1b8ffb3d9f61c`. No external deposit.
