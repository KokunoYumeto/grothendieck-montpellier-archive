# Cote 47, scan 9: the factor chi in the Chern classes of the Fourier transform

Claude Opus 5.5 at effort max (agent a28ea31fa17dd65e1), sweep 2 part 2, 18 Nov 2026. Read on the scan image
(`07_varietes_abeliennes/47.pdf` page 9, at 90 and 220 dpi) against the Codex transcription K47-01 and the Work math notes
K47-01 (Q1, Q2, M1, M3).

## Where it is

Cote 47 (SA18-13, the Fourier transform of abelian schemes; also SA07-13 = SA18-13 and SA14-1's carry question). Scans
3-8 build the transform phi_L for a line bundle L on A x_S B and its proposition 1 (with Lemma 2 admitted and a
"vérification de compatibilité" left open, scans 6-8); scan 9 proposes to "calculer" the class of phi_L(cl(L)) in K(B).

## What the page says (read on the image)

- The heuristic (margin: "indépendant des résultats de Mumford"): "phi_L(cl(L)) = chi L'^{-1/chi}" with chi = chi(delta)
  in H^0(S, Z), for L of class delta with chi(delta) != 0, L' the line bundle of class -delta' on B.
- The Chern character: ch phi_L = chi exp(-D'/chi) = chi - D' + D'^2/(2 chi) - D'^3/(3! chi^2) ... + (-1)^n D'^n/(n! chi^{n-1}).
  Correct.
- The total Chern class: c(phi_L) = (1 - D'/chi)^chi = 1 - D' + chi(chi-1)/(2 chi) D'^2 - chi(chi-1)(chi-2)/(3! chi^2) D'^3 + ...
  + (-1)^n chi(chi-1)...(chi-n+1)/(n! chi^{n-1}) D'^n. **The denominators read 2chi, 3!chi^2, n!chi^{n-1} on the image**
  (220 dpi crop): the transcription is right, the slip is on the page.
- "Ces formules sont-elles bien vraies mod torsion ?" (large ? in the margin). True at least over an algebraically closed
  field modulo l-adic cohomological equivalence. "Ceci donne des propriétés de divisibilité intéressantes de delta', savoir
  (chi-1)...(chi-k+1)/(k! chi^{k-2}) delta'^k est 'entier'", the denominator again read on the image.

## The decision

The coefficient of D'^k in (1 - D'/chi)^chi is (-1)^k C(chi, k)/chi^k = (-1)^k chi(chi-1)...(chi-k+1)/(k! chi^k). The page
writes chi^{k-1}, the denominator of the Chern character's terms, where the total Chern class needs chi^k: every written
coefficient of degree k >= 2 is chi times too large. Check at chi = 3: the quadratic and cubic coefficients are 1/3 and
-1/27; the page's give 1 and -1/9 (the Work note M1's numbers, confirmed). The page's own linear term -D' contradicts its
general term at n = 1 (which gives -chi D'), a second sign of the slip.

The divisibility statement inherits the slip. Integrality of c_k gives (chi-1)...(chi-k+1)/(k! chi^{k-1}) D'^k integral;
the page's (chi-1)...(chi-k+1)/(k! chi^{k-2}) delta'^k is chi times that, so it is true but weaker than what the formula
yields. (The cancelled symbols before the fraction, noted by M3, do not change this.)

(mine) The heuristic matches what Mukai proved later for semi-homogeneous bundles (ch E = r exp(c_1(E)/r), c(E) =
(1 + c_1(E)/r)^r); the transform of a non-degenerate line bundle is of that kind.

## Agreements and conflicts

- Work K47-01 M1 (coefficient discrepancy) and M3 (compare the denominator k! chi^{k-2}): both confirmed on the image.
- Part-1 flag (SA18, "suspected misreading or slip"): decided: a slip of his, not a misreading. Kind changed from
  "suspected misreading" to a correction (SA18 CORRECTIONS).

## Check events

- work:K47-01#6: the expansion recomputed ((1 - x/chi)^chi, chi = 3) and the denominators read on the image: the page has
  chi^{k-1} where chi^k is right; the note agrees.
