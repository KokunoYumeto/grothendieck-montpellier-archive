"""Write sweep3/SA12/DELIVERABLES.tsv and DEPENDS.tsv (SA12 lead a65dbdc241d1a129a, Claude Opus 5.5 at effort max,
19 Nov 2026). Counts from merge_sa12.py: pages = transcribed scans, words = words of 2+ letters in the .tex,
open_readings = \\unsure marks in the .tex. python -I -B tables_sa12.py"""
import csv
from pathlib import Path
S = Path(r"C:/Users/user/Documents/results_register/horizontal/sweep3/SA12")
TAB = chr(9)
PRO = "Pro transcription and Pro notes (GPT-6 Astra, ChatGPT Pro mode)"
CXB = "Codex web transcription with sheet notes and doubts (batch B, GPT-6 Astra at reasoning effort max)"
CXK = "Codex/Work transcription with sheet notes and Work math notes (batch K, GPT-6.2 Astra at reasoning effort max, ChatGPT Work)"
D = [
 ["SA12", "MPL_29_049-094", "29", "49-78, 82, 84-94", 42, 8638, 467,
  PRO + "; second witness K29-04, K29-05, K29-06 (" + CXK + ")",
  "read in full (reader A, a203d72bad105bea5)", "ready, with the corrections in CORRECTIONS.tsv",
  "odd scans 49-59: typescript n° 385 (distributions); 89-99: SGA 3 VIII-type typescript; Pic^tau 71-77, formal tame pi1 88-98"],
 ["SA12", "MPL_29_095-140", "29", "95-101, 103-112, 117-118, 124, 126, 129-133, 135, 137-140", 31, 7043, 298,
  PRO + "; second witness K29-07, K29-08", "read in full (reader A)", "ready, with the corrections listed",
  "Abhyankar 100-103; letter to Serre 1959 (125-130); Proposition 4 (139)"],
 ["SA12", "MPL_29_141-187", "29", "141-187", 47, 8320, 380, PRO + "; second witness K29-09, K29-10, K29-11",
  "read in full (reader B, a3c8d7ded052a745e)", "ready once the two ink corrections (143, 149) are made; Pro note N143.2 rests on the 143 misreading; 179 'aussi/alors fini' open",
  "Prop. 4 proof; Galois category axioms; progroupe for infinite covers; F(I) = C(K,I); 187 proposition"],
 ["SA12", "MPL_31_002-051", "31", "2-33, 35-39, 42-45, 47-51", 46, 9660, 443, PRO + "; no second witness",
  "read in full (the lead, a65dbdc241d1a129a)", "after the readings 31/020 (+2, decided), 31/023, 31/044 and the n/n+1 of 31/029",
  "flat cd_p of fields; Artin's cd theorems; Cartan; SGA 2 and SGA 3 typescripts reused"],
 ["SA12", "MPL_33_002-049 (with the parallel chat chatB)", "33", "2-49", 48, 9212, 233, PRO + "; chatB a parallel Pro witness",
  "not read in sweep 3", "not assessed in sweep 3; sweep 2 decided 33/023 on the scan", "1965 SGA 5 duality draft"],
 ["SA12", "MPL_33_050-097", "33", "50-97", 48, 10008, 365, PRO, "not read in sweep 3",
  "not assessed in sweep 3; sweep 2 decided 33/075 and 33/090 on the scan", "duality draft continued; E8 plates; EGA IV-1011"],
 ["SA12", "A29-01 (Codex)", "29", "3-6, 8-12, 79-81", 12, 3439, 58, CXB + "; only witness", "read in full (reader A)",
  "ready once the blank reserved spaces of the typed letters are printed as blanks with a note", "Grothendieck-Murre letters 1967 and 1969"],
 ["SA12", "C29-01..C29-04 (Codex)", "29", "13-17, 19-26, 29, 31-33, 35-39, 83", 23, 7134, 182, CXB + "; only witness",
  "read in full (reader A)", "ready, with the §4 number (31) and the case b) note (21-22)", "'Données de ramification', the sketch of 24.4.67; reply to Murre"],
 ["SA12", "C29-05..C29-07 (Codex)", "29", "102, 113-116, 119-123, 125, 127-128, 134, 136", 15, 5576, 154, CXB + "; only witness",
  "read in full (reader A)", "ready; 125 has the month (6 or 8) and the place open", "Bertini and variants; inertia; letter to Serre"],
 ["SA12", "K29-01 (Codex/Work)", "29", "2, 18, 27-28, 30, 34, 40-48", 15, 2455, 98, CXK + "; only witness",
  "read in full (reader A)", "40-48 NOT ready: handwritten, one witness, many doubtful words (48 read on the scan for its hypothesis line)",
  "'Finitudes (Pbs et conjectures)'; Lemma 1 ('réduit')"],
 ["SA12", "K29-02, K29-03 (Codex/Work)", "29", "188-189, 191-207, 209-217", 28, 6064, 221, CXK + "; only witness",
  "read in full (reader B, a3c8d7ded052a745e, after its resumption); 190 and 208 blank (decided on the scans)",
  "ready as a Codex-web reading with the 217 correction; a Pro pass is the remaining standard pass; open small readings 191, 210, 214",
  "'Opérateur d'homotopie pour d''' (188); cover 'Données de ramification / Catégories multigaloisiennes' (189); 191-207 a numbered sequence; 'Catégories multigaloisiennes' 209-217"],
 ["SA12", "K29-04..K29-11 (Codex/Work)", "29", "49-187 (second witness)", 120, 24419, 1169, CXK,
  "used as the second witness by readers A and B", "collated where the readers checked a reading", ""],
 ["SA12", "K31-01..K31-03 (Codex/Work)", "31", "52, 54-72, 74-88, 90-102", 47, 8553, 465, CXK + "; only witness",
  "read in full (the lead)", "after the readings 31/068 (p+q) and 31/061 (p-bases, poorly legible)",
  "cd des affines; Artin's affine Lefschetz; his conjectures (85); Lefschetz; specialization theorem"],
 ["SA12", "B37-01..B37-05 (Codex)", "37", "3-5, 7, 9-13, 15-16, 18, 23-25, 27, 30-31, 34-35, 39-45, 66-72, 74, 85-94, 96-98", 48, 11568, 295,
  CXB + "; only witness", "NOT read in sweep 3", "not assessed", "SGA and EGA re-editions 1967-71; Dieudonné letter 22.8.1967 (F31)"],
 ["SA12", "H37-01 (Codex)", "37", "52-55, 75-77", 7, 1626, 55, "Codex web transcription with sheet notes; only witness",
  "NOT read in sweep 3", "not assessed", "Hartshorne's letter of 4 Aug 1969 (Affine duality and cofiniteness) at 54-55"],
 ["SA12", "C32-01 (Codex)", "32", "7-10, 12-15", 8, 2600, 76, CXB + "; only witness", "NOT read in sweep 3", "not assessed",
  "Gysin homomorphism, local fundamental class (SA12-60)"],
 ["SA12", "H35-01 (Codex)", "35", "2-5", 4, 1256, 80, "Codex web transcription with sheet notes; only witness",
  "NOT read in sweep 3", "not assessed", "plan of SGA 7 (SA12-69)"],
]
H = ["topic", "package_or_folder", "cote", "scans", "pages", "words", "open_readings", "passes", "read_in_sweep3",
     "edition_and_translation", "note"]
with open(S / "DELIVERABLES.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter=TAB, lineterminator="\n"); w.writerow(H); w.writerows(D)
P = [
 ("SA12-11", "SA12-33", "29:025-026 (Rev^R(S) satisfies G1-G3 of SGA 1 V 4)", "Galois categories"),
 ("SA12-31", "SA12-19", "29:022 (Abhyankar: covers 'modérément ramifiés au sens large'); 29:100", ""),
 ("SA12-31", "SA12-30", "29:020-022 (Kummer data a) and b))", ""),
 ("SA12-32", "SA12-2", "29:043 (2) local pi1; 29:052-058", ""),
 ("SA12-32", "SA12-3", "29:041 b) proved; 29:061", ""),
 ("SA12-32", "SA12-8", "29:043 c) 'Prouvé Modulo conjecture d'invariance birationnelle de la ramification modérée'", ""),
 ("SA12-2", "SA12-1", "29:054 (Proposition) and 29:058 (curve induction) use Lemma 1 of 29:048-050", "Lemma 1 needs 'réduit' (ink, 29:048)"),
 ("SA12-3", "SA12-6", "29:061 'Bertini générique' [Réf]; 29:067; 29:113", ""),
 ("SA12-3", "SA12-1", "29:061 van Kampen through descent along the normalization", ""),
 ("SA12-4", "SA12-6", "29:062-063 (reduction to a generic curve)", ""),
 ("SA12-5", "SA12-6", "29:067-068 (Bertini corollary on the normal model)", "the Chow step of 29:066 holds for finite, not proper, maps"),
 ("SA12-8", "SA12-5", "29:070 uses only the projective case of 29:066", "survives the F12 gap"),
 ("SA12-9", "SA12-8", "29:073 (pi1(X) = pi1(Y) by purity on the regular Y)", ""),
 ("SA12-10", "SA12-8", "29:077 (pi1(X_reg) onto every proper normal model)", "rank formula needs l != p"),
 ("SA12-11", "SA12-16", "29:082-086 comment on chapters VIII-X of Murre's 1969 draft", ""),
 ("SA12-16", "SA12-21", "29:090-092 (Pi2^t in the exactness of the inertia sequence); 29:105", ""),
 ("SA12-16", "SA12-19", "29:100 (inertia along normal crossings)", ""),
 ("SA12-16", "SA12-30", "29:092 (reduction to a Kummer root)", ""),
 ("SA12-17", "SA12-16", "29:094 (Picard lifting for the extension class)", "true for X_0 proper over a field"),
 ("SA12-18", "SA12-16", "29:098 (Example II, X_0 = Spec Z)", ""),
 ("SA12-16", "SA12-6", "29:113-123 (Bertini variants feed the conjugacy of inertia, SGA 7 XVIII)", ""),
 ("SA12-22", "SA12-26", "29:126, 29:138 (rigidity lemma); 29:127-128 (pro-representability)", ""),
 ("SA12-35", "SA12-22", "29:143 (the pro-object pi_1^C is formal given Prop. 4)", "Prop. 4 false as stated (cusp), true in the étale case"),
 ("SA12-37", "SA12-22", "29:165-170 (Pi^1(S,xi;pi) for constant pi: left exactness and minimal elements)", ""),
 ("SA12-33", "SA12-34", "29:158-161 (axioms) and 29:153-157 (finite étale covers of rank n)", "29:209-217 unread"),
 ("SA12-38", "SA12-44", "31:065-070 (the phi-criterion uses cd of fields, 31:019-023)", ""),
 ("SA12-39", "SA12-44", "31:082-085 (the conjectures are calibrated on Artin's results and on Spec O_K)", ""),
 ("SA12-39", "SA12-41", "31:085 2° (the p-degree delta and cd_p of fields of characteristic p)", ""),
 ("SA12-39", "SA12-38", "31:070 ('probablement tjrs. le cas' bound and the henselian question)", ""),
 ("SA12-30", "SA12-33", "29:191-198 (axioms R1-R4 of a ramification datum on multi-Galois categories; 198 uses 217 (ii))", "continues 29:158"),
 ("SA12-30", "SA12-16", "29:199-201 (Kummer data, the mu_n-gerbe of n-th roots of O(D_i))", "tame theory, LNM 208"),
 ("SA12-30", "SA12-31", "29:199-201 (Kummer data against the 1967 sketch)", ""),
 ("SA12-33", "SA12-34", "29:210 (the frame torsors Isom([1,i],X) of 29:153-156)", ""),
 ("SA12-70", "SA12-30", "29:188 (the d''-homotopy sheet) against the typescript 33:095, 097", "link: the same formula"),
 ("SA12-37", "SA12-26", "29:187 (Zariski's main theorem)", ""),
 ("SA12-40", "SA12-39", "31:090-091 (Lefschetz from H^i(U,F) = 0 for i > n, U affine)", ""),
 ("SA12-40", "SA12-6", "31:093-097 (generic sections, specialization)", ""),
 ("SA12-40", "SA12-19", "31:096-097 (Lemma 3 by Abhyankar)", ""),
 ("SA12-40", "SA12-46", "31:090 (SGA 2 Lefschetz, the reused typescript 31:026-032)", ""),
 ("SA12-43", "SA12-67", "31:011-017 against Hartshorne's letter of 4 Aug 1969 (37:054-055)", "link (mine), cote 37 unread"),
]
with open(S / "DEPENDS.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter=TAB, lineterminator="\n")
    w.writerow(["item", "relation", "uses_item", "basis", "page_that_shows_it", "note"])
    for a, b, pg, note in P:
        w.writerow([a, "uses", b, "read in sweep 3", pg, note])
print(len(D), len(P), sum(r[4] for r in D))
