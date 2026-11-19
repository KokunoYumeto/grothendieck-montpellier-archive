# Sweep-3 tables for SA21 (agent a6d42bf6, horizontal sweep 3, 18 Nov 2026)
WHO = 'Claude Opus 5.5 at effort max, a6d42bf6fe2b0d8a8, horizontal sweep 3'
D = '2026-11-18'
SCAN = 'on the scan image (156-1.pdf / 156-2.pdf renders, sweep3 scratch)'

CHECK_EVENTS = [
 ['SA21-C3-01', D, WHO, 'independent re-proof: Scholie (iv) => (i), using L_Y = union of the L°_{Y_i} for Y_i <= Y, which follows from finite dimension (156-4/22-23)', 'holds', '156-4/024'],
 ['SA21-C3-02', D, WHO, 'targeted proof check: compatibility (a) => (b), first step (a common point gives X_i = X\'_j, since X_i meet X\'_j is closed, saturated and meets the dense open stratum U_i)', 'first step holds; the induction on dimension is only sketched on the page and was not checked', '156-4/007'],
 ['SA21-C3-03', D, WHO, 'independent re-proof: corollary of Cond 8 (if no X_1 with Y << X_1 < X, then the interior of Y-tilde lies in that of X-tilde)', 'holds', '156-4/044'],
 ['SA21-C3-04', D, WHO, 'targeted proof check: F is a sub-figure of G iff F refines G and is compatible with G', 'holds', '156-4/039'],
 ['SA21-C3-05', D, WHO, 'independent re-proof: in the finite case the figures are the finite downward-closed R-cliques of (M, <=, R), including the step that a finite clique has a Sup (induction with C3)', 'holds', '156-4/062'],
 ['SA21-C3-06', D, WHO, 'independent re-proof: C1-C2 correspondence of (F, <=) with families of subsets of M closed under bounded unions, with a smallest member A_X containing each X', 'holds', '156-4/055-056'],
 ['SA21-C3-07', D, WHO, 'targeted proof check: the smallest stratum through which a multistrate refines', 'holds', '156-4/080'],
 ['SA21-C3-08', D, WHO, 'independent re-proof: in the set-theoretic case the lattice of supports is Boolean, with Stone space the Stone-Cech compactification of the discrete set', 'holds', '156-4/069'],
 ['SA21-C3-09', D, WHO, 'targeted proof check of the displayed cosupport formula', 'refuted as written (it omits "no common lower element" and gives compatibility, not disjointness); refined as SA21-K9; his conclusion that Sigma depends only on (M, <=, R) stands', '156-4/069'],
 ['SA21-C3-10', D, WHO, 'targeted check of the reading against the scan image (200 dpi)', 'no negation visible in the ink; the conclusion needs "qu\'il n\'existe pas"; his slip, probable (SA21-K7)', '156-4/045'],
 ['SA21-C3-11', D, WHO, 'targeted check of the reading against the scan image (220 and 400 dpi) and of the condition', 'frozen transcription confirmed: a one-stroke <= written above a struck sign; the bars under both <= of the conclusion blacked out, leaving x<u<y,z; the condition as left fails at y = x; his slip in his own correction (SA21-K1)', '156-1/019'],
 ['SA21-C3-12', D, WHO, 'targeted check of the reading against the scan image (300 dpi)', 'frozen "W\'_t = X - V_t" confirmed (a clear V); his abuse of notation for X - W_t, W_t the inverse image of V_t (SA21-K2)', '156-2/003'],
 ['SA21-C3-13', D, WHO, 'targeted check of the reading against the scan image (300 and 500 dpi), and targeted proof check of the step', 'frozen "X minus {c}" confirmed (the c as clear as the a one line above); V is open and closed in X minus {a}, non-empty and not everything, so the step gives "X minus {a} ne serait pas connexe"; his slip (SA21-K3)', '156-2/006'],
]

CORRECTIONS = [
 ['SA21-K1', 'SA21-3', '156-1/019', 'his slip, made in his own correction (decided on the scan)', 'si x<=y,z, il existe u tel que x<u<y,z (ink: <= written above a struck sign; the bars of the conclusion\'s <= blacked out)', 'si x<y,z (strict antecedent), as on 156-1/013 and as his margin needs (divisible: x<y gives z with x<z<y)', 'A20; SA21-C3-11', WHO + ', ' + SCAN],
 ['SA21-K2', 'SA21-5', '156-2/003', 'his abuse of notation (decided on the scan)', "W'_t = X - V_t (V_t in X/A)", "W'_t = X - W_t, with W_t the inverse image of V_t in X", 'B04; SA21-C3-12', WHO + ', ' + SCAN],
 ['SA21-K3', 'SA21-5', '156-2/006', 'his slip of letter (decided on the scan)', 'X minus {c} ne serait pas connexe', 'X minus {a} ne serait pas connexe (V is open and closed in X minus {a})', 'B10; SA21-C3-13', WHO + ', ' + SCAN],
 ['SA21-K7', 'SA21-13', '156-4/045', 'his slip, probable (negation missing)', 'qu\'il existe une "Subdivision" du disque dont ils soient des noeuds', 'qu\'il n\'existe pas une "Subdivision" ... (the conclusion he draws needs the negation)', 'SA21-C3-10', WHO + ', on the scan at 200 dpi (no negation visible)'],
 ['SA21-K8', 'SA21-13', '156-4/048', 'his own correction', "C4 as first stated: G' union (F minus G) is a subdivision of F", "there is a subdivision of F inducing G', and G' meet F lies in G", 'his margin: "dementi par ... les strates fermees et strates augmentees"', 'G. himself, in the margin of 156-4/048 (recorded by ' + WHO + ')'],
 ['SA21-K9', 'SA21-13', '156-4/069', 'formula error', 'the displayed cosupport formula, without "no common lower element"', 'add the condition "no common lower element"; as written the formula gives compatibility, not disjointness', 'SA21-C3-09', WHO],
 ['SA21-K10', 'SA21-13', '156-4/075-083', 'his own correction', 'the axioms before C8_0, under which << need not be an order', 'the extra axiom C8_0, with which << is an order', 'his pages 156-4/075-083', 'G. himself (recorded by ' + WHO + ')'],
]

DEPENDS = [
 ['SA21-13', 'used by', 'SA21-14', 'his pages: 156-4/055-056 read in full; 156-5/002-014 read from its axiom lines', '156-5 works out as a sorite the model of the fourth system of 156-4 by families of subsets'],
 ['SA21-13', 'used by', 'SA21-10', 'his pages: 156-4 read in full; 156-6/002-009 read from its axiom lines', '156-6/2 restarts the contree with multistrates (lieux in multistrates in figures); 156-6/7 fixes the ombre of 156-4/36 and 88-89'],
 ['SA21-10', 'used by', 'SA21-15', 'his page 156-8/008', 'Mag 4 "etablit elegamment l\'axiome AtL3": the magasin axioms reorganize the atelier axioms'],
 ['SA21-14', 'used by', 'SA21-15', 'his page 156-8/018', 'a set-theoretic magasin is a set L with a family of subsets, the sorite of 156-5'],
 ['SA21-2', 'used by', 'SA21-12', 'his pages 156-3/002, 009-014 (axiom lines)', '156-3 restates the one-dimensional models of 156-1/2 through order and a betweenness relation ("l\'axiomatique par les segments")'],
 ['SA21-12', 'used by', 'SA21-10', 'his pages 156-9/005-007 (axiom lines)', 'the July 1986 restart from the one-dimensional model: points and intervals ordered by a < I_ab < b; preliminary figures are the flags'],
 ['SA21-15', 'related', 'SA21-8', 'his pages 156-8/003, 006 and our note (programme questions P01-P16)', 'the maquettes (T0 spaces) and the oriented maquettes of dimension <= 2 against the questions on finite T0 spaces and pro-objects of finite posets (H9)'],
 ['SA21-15', 'related', 'SA21-13', 'his pages 156-8/003 and 156-4/066-069; 156-9/003', 'the supports of 156-4 and the magasin class with Sigma_M = P(L); 156-9/3 asks whether supp x is an atom (H3)'],
 ['SA21-10', 'uses', '156-6/053 (At ens 1)', 'his pages 156-7/013 and 156-6/053, read on the scans by readers A and B', '"VI p.52" is GF VI = 156-6, p. 52; the two margins cite each other (H11 refuted)'],
 ['SA21-13', 'related', 'SA10-2', 'his pages 156-4/036, 088-089 and 156-6/005-007; our notes C150 Q1a-Q1d (149/133) and SA10-2 (cotes 67, 136, 147)', 'the 1986 definition of the ombre against the earlier uses (H05G; H4); the word does not occur in the transcriptions of cotes 150-151, which speak of voisinages tubulaires'],
 ['SA21-10', 'related', 'SA10-16', 'his pages 156-7/011, 014 (axiom lines) and 151/054 (read)', 'the 1986 polyhedral condition (two elements bounded below have an inf) is the strengthened condition (24) he declined in 1981'],
 ['SA21-13', 'related', 'SA11-12', 'his pages 156-4/032, 045 and 154/034-035, both read; the identification is my reading (H5)', '156-4/32, pseudo-discs with chords and nodes, against the chord systems of cote 154 (chords crossing at most once)'],
 ['SA21-13', 'related', 'SA10-5', 'my reading (H2), candidate', '156-4/70 "contree moderee" as the Hauptvermutung for subdivisions (Shiota for definable sets)'],
 ['SA21-13', 'related', 'SA11-4', 'my reading (H2), candidate', 'as the previous row, SA11 side'],
 ['SA21-13', 'related', 'SA20-12 to SA20-15 (cotes 120-121)', 'candidate: the 120-121 side not read tonight', 'figures (156-4/2-3, Cont 2) against the tame stratifications and adapted partitions of cotes 120-121 (H7)'],
]

_P = 'one transcription pass and one audit per folder (the _transcription.tex, _doubts.md and _audit.md of each folder)'
_N = 'a second reading pass against the scans, unsure marks first'
DELIVERABLES = [
 ['156-1 + 156-2', '46 scans', 'Pro package MPL_156-1+156-2 (transcription, notes, doubts)', '1 package', 'one Pro transcription pass with notes; sweeps 1-2 placed the notes; sweep 3 decided three readings on the scans (A20, B04, B10)', '472', '10.3', 'not counted', 'not counted', 'the remaining unsure marks', 'no', 'no', _N + '; then edition and translation'],
 ['156-3', '2-41 (40 scans)', 'Codex folders J156-3-*', '5', _P, '828', '20.7', '9', '1374', 'all unsure marks and doubt rows', 'no', 'no', _N + '; axiom pages first (scans 2-5, 9, 12-14, 20, 22-25, 29)'],
 ['156-4', '2-89 (88 scans)', 'Codex folders J156-4-*', '11', _P + '; read in full mathematically in sweep 3; one reading (scan 45) checked on the scan', '1836', '20.9', '17', '2784', 'all unsure marks and doubt rows; scan 45 (SA21-K7)', 'no', 'no', _N + '; the axiom pages 18-25 and 46-89 first'],
 ['156-5', '2-49 (48 scans)', 'Codex folders J156-5-*', '6', _P, '1001', '20.9', '4', '1623', 'all unsure marks and doubt rows', 'no', 'no', _N],
 ['156-6', '2-94 (93 scans)', 'Codex folders J156-6-*', '12', _P, '1749', '18.8', '9', '2879', 'all unsure marks and doubt rows', 'no', 'no', _N + '; scans 2-9 (the data of a contree, the ombre) first'],
 ['156-7', '2-9 (8 scans)', 'folder H156-01', '1', _P, '195', '24.4', '1', '305', 'all unsure marks and doubt rows', 'no', 'no', _N],
 ['156-7', '10-114 (105 scans)', 'Codex folders J156-7-*', '14', _P, '1823', '17.4', '14', '3076', 'all unsure marks and doubt rows', 'no', 'no', _N + '; scans 10-15 (At CD, polyhedral and simplicial ateliers) first'],
 ['156-8', '2-127 (126 scans)', 'Codex folders J156-8-*', '16', _P + '; scans 3-21 read in sweep 3 from their axiom lines', '1794', '14.2', '8', '3074', 'all unsure marks and doubt rows', 'no', 'no', _N + '; the recapitulation, scans 3-21, first'],
 ['156-9', '2-140 (138 scans)', 'Codex folders J156-9-*', '18', _P, '1988', '14.4', '10', '3268', 'all unsure marks and doubt rows', 'no', 'no', _N + '; scans 3-7 (table of contents, diagram of ateliers, the July restart) first'],
]
