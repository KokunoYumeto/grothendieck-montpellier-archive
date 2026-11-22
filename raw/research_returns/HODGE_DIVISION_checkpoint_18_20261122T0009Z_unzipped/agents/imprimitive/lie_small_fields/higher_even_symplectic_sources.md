# Higher even symplectic source and exploration record

Date: 2026-11-21. Agent /root/imprimitive; GPT-6 Astra Pro; effort inherited/not exposed; HODGE_DIVISION.

## Unconditional finite result

The complete CTblLib tables S8(2), S10(2), S12(2) are retained; S8/S10 name ATLAS provenance, while S12 is attributed to Christoph Koehler, computed using group-theoretic and character-theoretic methods, with no separate refereed-publication claim. They include full provenance, classes, rows, sizes, orders, power maps and indicators. Exact GAP exporter checked orthogonality and reality. The separate Python verifier checks every nonidentity entry of every nontrivial row with rational triangle bounds; all maxima are attained by rational entries. New expanded run: 756 rows, 271785 entries, PASS0.418s. Minima35/155/651; maxima3/5,17/31,11/21. The prior two-table input is retained as v1 to identify the peer computation honestly.

The multiplier and outer-automorphism facts for Sp(2n,2),n>=4 were read explicitly in Gluck--Magaard, Absolute Fourth Moments and Finiteness of Linear Groups, Communications in Algebra34(2006),3387--3407, DOI10.1080/00927870600788448, author manuscript p25, https://www.academia.edu/29518749/Absolute_Fourth_Moments_and_Finiteness_of_Linear_Groups . Those classification statements do not assume the fourth-moment hypothesis used elsewhere in that paper. HHM2015 Chapter5Table1, numberedp35, independently gives the exceptional-multiplier list.

## Precisely conditional all-rank argument

The only unresolved source premise is GM1998: for Sp(2n,2),n>=5, every nonidentity semisimple element in a proper parabolic has all nontrivial ordinary-character ratios<=5/6. Located as Theorem3.1(b) with exact finite exceptions in a zbMATH review reproduced at https://portal.mardi4nfdi.de/wiki/Publication%3A1270990 . Review and bibliographic metadata are NOT treated as a verified primary theorem. Article: Gluck--Magaard, Cross-Characteristic Character and Fixed Point Space Ratios for Groups of Lie Type, J.Algebra204(1998),188--201, DOI10.1006/jabr.1997.7277. Crossref and Birmingham institutional metadata confirm identity. The review has an incorrect1999 display date.

Repeated legitimate publisher/author/repository searches did not supply the full original. Elsevier article/PDF/API/reader URLs returned403; institutional page has metadata only. No access control was bypassed. OpenAlex lists four citing papers: Magaard--Malle--Tiep2002, Zalesski2008 minimum polynomials, Tiep--Zalesski2008 eigenvalues, and Gluck--Magaard2006. Relevant complete sections of the accessible2002/2006 papers do not restate the needed5/6 semisimple estimate. Primary-restatement search is paused for a new peer-review priority.

Verified additional inputs: Gow1981 Products of Two Involutions in Classical Groups of Characteristic2,J.Algebra71,583--591,theoremprintedp583 and complete section3pp589--591; original scan https://www.academia.edu/115642614/Products_of_two_involutions_in_classical_groups_of_characteristic_2 . Liebeck2017 Character ratios for finite groups of Lie type,and applications,ContempMath694,193--208, authorpp2--4 definitions and Theorem2.4(i), https://www.ma.imperial.ac.uk/~mwl/princeton-survey-final.pdf ; unipotent3/4 holds for q<=4, nonunipotent part is19/20 and not silently strengthened.

## Failed or rejected expectations

A proposed all-rank1/2 character-ratio bound is refuted already by the three retained finite tables. Initial GAP exploratory direct cyclotomic ordering was rejected: GAP ordering is not real ordering. Retained bad script is named probe_sp2n2_bad_order.g; corrected probes and all certificates use rational/integer estimates only. The unrestricted3/4 estimate described as plausible in the2006 introduction is not used. No finite-table extrapolation is used in the conditional argument.

G34 independently whole-reviewed the entire higher-rank proof and reconstructed the original279-row/45209-entry packet, PASS conditional precisely on GM. Expanded third-table peer reconstruction is separately pending; no earlier peer event is retroactively enlarged.

## The former source gate is now removed by a new proof

The canonical `higher_even_symplectic_section.tex` proves the entire n>=4 family unconditionally. The archived conditional draft is preserved for the research record, but GM1998 is no longer a mathematical premise. For odd-prime elements in a proper parabolic the new proof constructs an elementary abelian2-subgroup U without fixed points, then applies the verified Gluck unipotent3/4 estimate and exact character-weight orbit averaging. Elliptic elements use the elementary torus-centralizer estimate and degree floor, improved to3/4. The resulting universal projective support1/8 gives the actual Hurwitz degree ceiling24<35.

G34 whole-read the complete new proof at SHA72e295707440f2e06e39658d2b3528f61d9587227e99e6f18196b075515dbc3c and reported PASS, with a separate own exact symbolic matrix certificate. Author matrix-mask certificate check_higher_even_elementary.py/.json actually passed10802shear equivariance checks,17472line-radical products, an explicit order3 U of order16 and all five dual-character3-cycles, and the all-rank arithmetic in0.836965s. These finite checks supplement rather than replace the universal proof.

Fresh frozen Liebeck2017 authorPDF has383678bytes and SHAe6e0a0148264d0b2a46a6a6e7fdc09096a6837155510a7482584ef99dd2300fc. Exact §§2 definitions and2.4(i) reread, including the distinct19/20 nonunipotent statement, which is not used.
