# Cote 57, scan 144: what "à vérifier" qualifies

Claude Opus 5.5 at effort max (agent a28ea31fa17dd65e1), sweep 2 part 2, 18 Nov 2026. Read on the scan image
(`08_picard/57.pdf` page 144, 90 dpi) against the Pro transcription MPL_57_133-179 (scans 142-144) and its notes FW01-FW07,
P05, SF07.

## Where it is

Cote 57, scans 141-147 ("Curve Picard", cover on 141; SA14-17, the Kummer class for the Picard of a curve). Scan 143 is
his letter to W. A. Benjamin (IHES letterhead, Massy, 21 November 1966) on the front matter of "Huit exposés ..." and the
Bourbaki copyright (SA14-13).

## What the pages say

- 57:142: f: X -> S projective smooth with geometrically connected fibres of dimension 1, Y closed in X and étale over S
  (e.g. disjoint sections), U = X - Y, n prime to the residue characteristics. In the spectral sequence
  E_2^{pq} = H^p(S, R^q_! f_U(mu_n)) => H^*_prop(U, mu_n), with R^1 = _nE and R^2 = Z/n, the differential
  E_2^{02} -> E_2^{21} gives a canonical element xi_n in H^2(S, _nE); for n = l^nu, xi(l) in H^2(S, T_l(E)); "cet élément est
  nul si U a une section sur S". E is the generalized Jacobian, an extension of J = Pic^0_{X/S} by T = G_m^I/G_m.
- 57:144 (read on the image): Z is X with Y collapsed (the cokernel of X u (Y x_S Y) => X), E = Pic^0_{Z/S}, the canonical
  torsor P = Pic^1_{Z/S} under E, its class eta in H^1(S, E) (boxed), and the boxed relation **xi_n = delta_n(eta)**, with
  delta_n: H^1(S, E) -> H^2(S, _nE) the coboundary of the Kummer sequence 0 -> _nE -> E -> E -> 0. **"à vérifier ......"
  stands in the left margin at the height of this boxed relation.**

## The decision

"À vérifier" qualifies the relation xi_n = delta_n(eta): the class from the spectral sequence of the open curve equals the
Kummer coboundary of the class of the degree-1 Picard torsor of the pinched curve. It is not the Fourier check of cote 47
(the "vérification de compatibilité" of 47:6-8, SA18-13). The Pro notes say exactly this: SF07 ("Kummer/transgression
comparison expressly left open") names the step; FW02 ("the current 'à vérifier' is a Kummer-boundary comparison") says
the torsor P is not the Poincaré bundle of the Fourier argument and that the source identifies neither with the other;
FW01 says the cote 47 gap is the derived restriction of the map c at a zero-section point (47:7-8) and that these pages
do not supply it. My part-1 flag (SA14) suspected the notes of reading 57:144 as the Fourier check; they do not. The flag
is closed as my misreading of the note headings (SA14 CORRECTIONS).

## Links

- SA14-17 (the Kummer class; this relation is its centre) and SA19-1 (generalized Jacobians).
- (mine) The class xi(l) is the obstruction to a section of U over S in Kummer form, the same mechanism the anabelian runs
  use for points as sections (register: ANABELIAN_149_PUSH, ANABELIAN_A1, generalized Jacobian and prime-to-p Kummer). The
  CLAIM_LINKS of SA14 record the register statements that bear on it.

## Check events

- MPL_57_133-179 FW01, FW02 and SF07: the place of "à vérifier" checked on the image (57:144): it qualifies
  xi_n = delta_n(eta); the three notes agree with the page.
