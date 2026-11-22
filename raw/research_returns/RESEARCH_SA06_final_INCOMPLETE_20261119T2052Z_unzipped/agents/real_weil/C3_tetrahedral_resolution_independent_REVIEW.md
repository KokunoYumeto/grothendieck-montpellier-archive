# Independent complete audit of the tetrahedral resolution

**Verdict: PASS** for the exact geometric construction TG.1–TG.5 in `../frobenius/C3_tetrahedral_resolution.tex`. Complete typed text, complete finite certificate program, and every retained output case read at 16:05–16:07 UTC on 19 November 2026. This is an unnumbered geometric auxiliary; no top-Chow or negative-K multiplication conclusion is certified here.

Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode; RESEARCH_SA06; run `/root/real_weil`; effort setting not separately exposed.

## Re-derivation

The characteristic-five plane computation is correct: if a=0, the derivative conditions force b=0 and the equation excludes c≠0; if a≠0, the first and third derivatives give c=−b and a⁴+b⁴=0, while the equation gives a⁵=b⁵, impossible in characteristic five. The edge polynomial and its derivative have no common zero, and every vertex has G=1. In other characteristics, the Fermat derivatives give all required transverse plane/edge sections. Euler plus F=0 gives Q=G=0 at any singular point, independently of characteristic. The smooth-face calculation therefore excludes every nonzero singular point.

The local irreducibility argument is legitimate: a factorization by two nonunits in the four-dimensional ambient regular local UFD would have a two-dimensional intersection on which all derivatives of F vanish. Repeated factors likewise contradict regularity away from the origin. The resulting hypersurface is Cohen–Macaulay and regular in codimension one, hence a normal domain. Its strict henselization remains a normal local domain, and the base changes of the displayed regular charts remain regular.

At a simple edge zero, the change to uv=tw is étale. Blowing up (u,t) gives the actual saturated affine blowup algebras k[u,a,w] and k[t,b,v] (with the corresponding étale coefficient rings). The cancelled components must indeed be omitted. The chosen plane becomes Bl₀(A²), the other is unchanged, and the double curve maps isomorphically to the old edge. The closed fibre is ua=0 or t=0, hence reduced SNC with no new divisor. These checks make the global order argument precise: a later component centre is Cartier near every already resolved node and at every original triple vertex. The successive projective blowups consequently assign 15,10,5,0 distinct points to the four components and preserve the tetrahedral incidence complex.

The equality mO_Z=O_Z(−E) is retained through the charts, so the conormal is exactly the pullback of O(1). Its degree on the small exceptional curves is zero; the text correctly says nef and not ample. The separate weighted divisor argument also checks: the tautological invertible ideal is O(−E_i′); tensoring it with a sufficiently high pullback of the previous relatively ample negative divisor preserves positive coefficients on all four components because the modification is small. This produces a weighted D with −D relatively ample without changing the conormal statement.

## Primary sources and finite certificate

Freshly opened and read complete statements/proofs:

* Stacks31.33.2, Tag0804, affine Rees-chart construction: <https://stacks.math.columbia.edu/tag/0804>, retrieval `turn460256128view0`.
* Stacks31.33.7, Tag0807, identity for a Cartier centre: <https://stacks.math.columbia.edu/tag/0807>, `turn460256128view1`.
* Stacks31.33.13, Tag02NS, projectivity and relatively ample tautological sheaf: <https://stacks.math.columbia.edu/tag/02NS>, `turn460256128view2`.
* Stacks29.38.8, Tag0C4K, composite relative ampleness: <https://stacks.math.columbia.edu/tag/0C4K>, `turn460256128view3`.

The complete program `../frobenius/code/check_tetrahedral_resolution.py` and full `../frobenius/output/tetrahedral_resolution_certificate.json` were inspected. All 36 retained checks pass: all characteristic-five face charts and edges, vertices, seven finite Fermat-prime samples, the integer Euler identity, both Rees-chart equations and overlap identities, and the incidence count. Author timing is 0.09717690400430001 seconds, run start 16:04:19.720278 UTC. The general-prime proof is the written derivative argument, not an inference from those samples. I did not independently rerun the certificate or a TeX build.
