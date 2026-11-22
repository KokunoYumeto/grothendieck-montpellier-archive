# Relative Milnor quotient: exact scope and validation

The auxiliary proof is `K2_relative_Milnor_all_characteristics.tex`. It establishes, for a square-zero invertible-ideal thickening E of a smooth k-variety V, the canonical quotient

J_r = ker(K_r^M(E) → K_r^M(V)) → I ⊗ Ω^{r−1}_{V/k}.

It is normalized by {1+i,u₂,…,u_r} ↦ i dlog(u₂)…dlog(u_r), is independent of a splitting or frame, and exists in every characteristic. In characteristic p the relative sheaf J_r is killed by p. The proof uses tensor presentations, actual lifts of Steinberg relations, and the canonical rank-one conormal exterior kernel. It does not assert that the quotient is an isomorphism at p=2 or that Milnor and Quillen K-theory agree on E.

The proof also gives the actual transition-symbol cup formula for products of line bundles, first in degree two and then explicitly in every degree, and the resulting relative-to-absolute cohomology injection if H^{r−1}(V,K_r^M) is p-divisible. The latter hypothesis is exactly the separately audited cycles-agent lemma. The optional Dennis–Stein calculation is independent support in degree two and is not required for the main Milnor argument.

## Exact primary openings

- The Stacks Project, Section 10.138, Tag 00TH: https://stacks.math.columbia.edu/tag/00TH. Freshly opened and read Definition 10.138.1, Proposition 10.138.13 and the adjoining lifting discussion on 19 November 2026. The square-zero conormal injectivity is proved directly in our text after choosing a local splitting; it is not attributed to a regular-immersion theorem.
- Weibel, *The K-book*, author-hosted Chapter III: https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf. Freshly opened and read Definition 5.11 p.43, relations (D1)–(D3), Theorem 5.11.1(b) p.44, and Exercise 5.14 pp.46–47. The historical sign is kept explicit: our positive Steinberg normalization is the negative of the exercise's Dennis–Stein map.

## Independent checks received

- Parent `/root`: full typed proof PASS reported at 14:43:04 UTC, including all-r exponent and conormal quotient and the Čech-to-sheaf-cohomology interpretation. The explicit all-r cup paragraph (RM.7) was appended afterward as the identical general transition-symbol calculation; parent was notified.
- `/root/cycles`: full typed auxiliary proof PASS reported at 14:44:02 UTC, including all-r/all-p quotient, p=2, cup compatibility and optional Dennis–Stein signs; reviewer freshly opened the exact Stacks and Weibel inputs. Its detailed report is `agents/cycles/relative_milnor_all_characteristics_independent_REVIEW.md`.

## Build

`code/build_relative_Milnor.py` records all exact commands, each elapsed time and return code. The actual run started 2026-11-19 14:45:06.407722 UTC and finished 14:45:17.003512 UTC, total 10.59577256400371 seconds. All five passes returned zero. The 3-page PDF has 120425 bytes; the final log has no warnings, overfull boxes, missing references or undefined commands. Exact output and metadata are `output/K2_relative_Milnor_build.out` and `.json`.

This is an auxiliary theorem supporting the proposed C.3bj argument. It is not an independent registration of the complete geometric counterexample and does not certify that theorem's incidence geometry, exceptional-image argument or actual-family construction.

All three rendered pages were individually inspected at 14:46:11 UTC. Displays, paragraph breaks and references are legible and contained within the page. Images are retained as `output/K2_relative_Milnor_QA-1.png` through `-3.png`. The auxiliary heading retains its pre-registration wording; the independent receipts above are the exact current review record.
