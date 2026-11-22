"""Retain the root's actual reading and audit scope; no theorem is promoted here."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
p = root / 'parts/D/post17_research/ROOT_POST17_AUDIT_RESEARCH.md'
s = p.read_text()
marker = '## Actual post-review11 root audits and primary reads'
assert marker not in s
s += '\n\n' + marker + '\n\nRecorded ' + now + '''.

The bounded-geometric-period file received a fresh complete root actual-file audit at13:06–13:08UTC, before review11. The proof counts only realized prime-to-p geometric classes, chooses witnesses, intersects their kernels, normalizes the resulting fixed global or complete-local cover, and uses a hereditary original-divisorial tame quotient and a coset-representative restriction-fibre bound. Previously fully audited H2, Kummer, finite-normal tame and selected-product inputs were reused; no new primary reread was claimed for that audit. It is a finite-cover closure of the one Brauer-zero reduction, with no uniform constant in the period bound.

After review11 root freshly read the complete actual file D_single_curve_Brauer_residues.tex and checked every map in the Kummer/localization quotient, the absolute-purity twist, exact order of the residue character, cyclic lifting including the action, connectedness and regular integrality, Stein normalization and puncture, pullback killing, and genus/normal-degree scaling. Root freshly opened and read the entire statements and written proofs of Stacks03RQ and0A48, then0C1D and its derivation in0C1B. Earlier complete ILO purity and local Pic-lifting audits were reused; no fresh reading of ILO is claimed. PASS was sent to D. Exact URLs:https://stacks.math.columbia.edu/tag/03RQ, https://stacks.math.columbia.edu/tag/0A48, https://stacks.math.columbia.edu/tag/0C1D, https://stacks.math.columbia.edu/tag/0C1B.

Root freshly read the complete actual file D_uniform_generation_cycle_charts.tex and the full published CFHR Lemma2.4 and Theorem1.1 proof, printed192–193, from parts/C/sources/CFHR1999/published.txt. The point ideal, automatic-adjunction supporting subcycle, generic evaluation injection, zero-dimensional Tor term, formal functions and proper-local global generation were checked. Root also fully reread the earlier first-power Noether-different proposition and integral-cycle proof, and reread the complete energy corollary. The new fixed-J divisor energy, Frobenius pC sandwich, cyclic determinant inequality, full nonreduced h0 bound, and actual fixed-determinant quotient chart were checked. A literal p,c1 typesetting typo was corrected by C. Root required and checked the explicit complete-base/previously-proved-energy scope and the literal Opened bibliography marker before sending PASS. No energy theorem for arbitrary nonalgebraizable complete covers, moving-determinant atlas, uniform finite-thickening realization or representation count is inferred. CFHR primary URL:https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7FEAD216C2F054EFB04C655991150B60/S0027763000025381a.pdf/embeddings_of_curves_and_surfaces.pdf. This was a scoped proof read, not a read of the whole article.

Root freshly read from the retained Lieblich math/0702240v4 text the complete Proposition3.2.1(pp10–11), Proposition4.1.4 with the preceding Lemmas4.1.1–3, Lemma4.2.5(pp12–13), and Sections5.1.5–5.1.8(pp18–19). The root-stack Brauer extension applies to excellent regular surfaces, while the regularity and eigenblock section explicitly fixes a prime ell. A composite-order orbit statement needs its own proof. No uniform formal-depth or quantitative atlas theorem is supplied by these passages. Retained source:parts/D/post17_research/sources/Lieblich2011_arithmetic_v4.pdf; arXiv:math/0702240v4,27May2009, published Crelle659(2011),1–41.

At13:17UTC root searched the exact queries `"local fundamental group" "finitely generated" characteristic p normal surface`, `"proper" "non-projective" "fundamental group" "finitely generated" characteristic`, and `"punctured" "Frobenius" "representation growth" fundamental group`. Results again included Suzuki's nilpotent-quotient paper and the proper-scheme finite-presentation theorem of Lara–Srinivas–Stix, with their distinct scopes. No new theorem removing the residual local or punctured-proper gate was located in this search. This is not an exhaustive literature or priority claim, and no theorem was applied merely from a search result.

Root suggested to C a further possible use of the generation theorem: for a fixed generically generated determinant line L, vanishing of H1(Y,L(-tZ)) lets generating tuples on tZ lift to actual bundles on Y, with proper-local generation. This does not prove fullness or cyclic Frobenius realization, nor a uniform Isom criterion. Comparing a geometric cycle thickening to the fixed base Noether-different ideal remains necessary; zero-dimensional basepoints cannot be discarded. This is research advice, not a new proved result.
'''
p.write_text(s)
record = dict(utc=now, note=str(p.relative_to(root)), sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
              new_central_theorems=0, movement=False, archive_created=False)
(root / 'code/output/post17_root_audits.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
