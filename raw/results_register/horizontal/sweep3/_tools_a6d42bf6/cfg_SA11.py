# Sweep-3 tables for SA11 (agent a6d42bf6, horizontal sweep 3, 18 Nov 2026)
WHO = 'Claude Opus 5.5 at effort max, a6d42bf6fe2b0d8a8, horizontal sweep 3'
D = '2026-11-18'

CHECK_EVENTS = [
 ['SA11-C3-01', D, WHO, 'targeted check of the disk construction: the complement of an open Moebius band around L is a disc; each D_i meets the boundary (the double cover of L) in two points and traces a chord', 'holds', '154/034'],
 ['SA11-C3-02', D, WHO, 'independent proof that parallelism of chords is an equivalence relation for chord systems coming from a relative position', 'holds (two chords are disjoint exactly when the pseudolines meet on L; D_j meets L once, which gives transitivity)', '154/035'],
 ['SA11-C3-03', D, WHO, 'targeted proof check, by a sketch not written out in full, of his claim that conditions (a)-(b) are sufficient', 'holds by the sketch: chords of different classes cross, so their ends are in antipodal cyclic order; contracting each packet and gluing the boundary antipodally gives the projective plane with the arrangement and L', '154/035'],
]

CORRECTIONS = []

DEPENDS = [
 ['SA11-12', 'related', 'SA21-13', 'his pages 154/034-035 (read) and 156-4/032, 045 (read); the identification is my reading', 'discs with chords crossing at most once (1985-86) and the pseudo-discs with chords and nodes of 156-4 (SA21 H5)'],
 ['SA11-12', 'used by', 'SA11-8', 'his pages 154/038-043, read', 'the discs of relative positions are glued along transition arcs into the cellular surface of relative positions (Esquisse section 8)'],
 ['SA11-12', 'used by', 'SA11-10', 'his pages 154/034-043 (read) and the sweep-2 map', 'the polygon invariant and his conjectured injectivity (SA11-C1) rest on the discs and their characteristic polygons'],
]

_N = 'a second reading pass against the scans, unsure marks first'
DELIVERABLES = [
 ['154', '1-45 (44 scans)', 'Pro package MPL_154_001-045', '1 package', 'one Pro pass (transcription, notes, doubts); scans 34-43 read in full in sweep 3', '464', '10.5', '4', '554', 'the unsure marks', 'no', 'no', _N + '; the disk model, scans 34-43, first'],
 ['154', '46-76 (31 scans)', 'Pro package MPL_81_038-055+154_046-076 (cote 154 part)', '1 package', 'one Pro pass (transcription, notes, doubts)', '508', '16.4', '0', '652', 'the unsure marks', 'no', 'no', _N],
 ['154', '46-61 (16 scans)', 'Codex folder K154-01', '1', 'one Codex transcription (a second witness for 46-61)', '208', '13.0', '6', 'none', 'the unsure marks; compare with the Pro witness', 'no', 'no', 'collate the two witnesses, then ' + _N],
 ['154', '62-76 (15 scans)', 'Codex folder K154-02', '1', 'one Codex transcription with notes (a second witness for 62-76)', '110', '7.3', '0', 'none', 'the unsure marks; compare with the Pro witness', 'no', 'no', 'collate the two witnesses, then ' + _N],
 ['154', '77-126 (49 scans)', 'Pro package MPL_154_077-126', '1 package', 'one Pro pass (transcription, notes, doubts)', '446', '9.1', '1', '518', 'the unsure marks', 'no', 'no', _N],
 ['154', '127-176 (50 scans)', 'Pro package MPL_154_127-176', '1 package', 'one Pro pass (transcription, notes, doubts)', '657', '13.1', '30', '765', 'the unsure marks; 30 illegible places', 'no', 'no', _N + '; the 30 illegible places first'],
 ['121 + 153 + 155', '33 scans', 'Pro package MPL_121_049-073+153+155', '1 package', 'one Pro pass (transcription, notes, doubts)', '258', '7.8', '2', '492', 'the unsure marks', 'no', 'no', _N + '; 121 by this agent, 153 and 155 by ae4ae3dc17acaa440'],
]
