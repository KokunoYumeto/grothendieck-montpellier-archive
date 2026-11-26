"""Writes ../CHECK_EVENTS.tsv for paper D1; statement numbers are read from src/D1_paper.aux.
By afbbdefd94c5db150 (Claude Fable 5.2 at effort max), 25 Nov 2026. Run from papers/D1."""
import re, io
aux = open('src/D1_paper.aux', encoding='utf-8', errors='replace').read()
num = {m.group(1): m.group(2) for m in re.finditer(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}', aux)}
W = 'afbbdefd94c5db150 (Claude Fable 5.2 at effort max; this writing run)'
R13 = 'afbbdefd94c5db150 (Claude Fable 5.2 at effort max; referee reading of TOTAL_EXACT_2)'
I13 = 'a5ead5c6 (Claude Fable 5.2 at effort high; intake of TOTAL_EXACT_2)'
I17 = 'afbbdefd94c5db150 (Claude Fable 5.2 at effort max; intake of DER_FOLLOWUP)'
T12 = 'a0a83137 (Claude Fable 5.2 at effort max; review of TOTAL_ASPHERICITY)'
P13 = 'abe075dc (Claude Opus 5.5 at effort max; review of PRESHEAF_TOTALITY)'
C24 = 'a24b3bc6 (Claude Opus 5.5 at effort high; program of 24 Nov)'
RE = 'independent re-proof'
TP = 'targeted proof check'
UR = 'used and rechecked in this run'
CO = 'computation or formal certificate'
BG = 'carried as background without fault found'
rows = []

def add(label, kind, date, who, typ, out):
    rows.append(("%s %s [%s]" % (kind, num.get(label, '?'), label), date, who, typ, out))

add('lem:acyclic', 'Lemma', '2026-11-25', W, RE, 'holds; proof by cyclic covers, written by the writer; read by nobody else')
add('prop:total', 'Proposition', '2026-11-12', T12, TP, 'TOTASPH C.5 found correct')
add('prop:total', 'Proposition', '2026-11-25', W, RE, 'holds; proved again without reopening the run; read by nobody else')
add('rem:hocolim', 'Remark', '2026-11-25', W, RE, 'argument written by the writer; its two citations (Bousfield-Kan XII.5.2; Goerss-Jardine IV 1.7) are from memory and unconfirmed')
add('prop:incl', 'Proposition', '2026-11-12', T12, TP, 'TOTASPH C.6 (exact implies total) found correct')
add('prop:incl', 'Proposition', '2026-11-25', W, RE, 'holds; same route as DER_FOLLOWUP D.2, which the writer followed on 17 Nov')
add('lem:succ', 'Lemma', '2026-11-25', W, RE, 'holds (doubling along two disjoint cosieves)')
add('prop:qf', 'Proposition', '2026-11-25', W, RE, 'holds; the direction from H_1 = 0 to (QF1), (QF2); compare TOTASPH C.11 and Isbell-Mitchell 1976, not reopened')
add('prop:sifted', 'Proposition', '2026-11-13', P13, TP, 'PRETOT F.3 is among the 54 statements reviewed, none found wrong')
add('prop:sifted', 'Proposition', '2026-11-25', W, RE, 'holds; the proof in the paper is the writer own; the proof of the run was not reread')
add('lem:squares', 'Lemma', '2026-11-25', W, RE, 'holds')
add('prop:reduction', 'Proposition', '2026-11-13', I13, TP, 'TOTEX2 A.33 followed, no fault')
add('prop:reduction', 'Proposition', '2026-11-13', R13, TP, 'TOTEX2 A.33, A.34 correct, no gap')
add('prop:reduction', 'Proposition', '2026-11-17', I17, TP, 'DER_FOLLOWUP A.7 (the same argument) followed in full, sound')
add('prop:reduction', 'Proposition', '2026-11-25', W, UR, 'every step derived again in the setting (K1)-(K4), which is the formulation of the writer')
add('lem:bridgeset', 'Lemma', '2026-11-13', R13, TP, 'the set-level part of TOTEX2 A.30 correct')
add('lem:bridgeset', 'Lemma', '2026-11-25', W, UR, 'rewritten with an explicit description of the classes and derived again; read by nobody else in this form')
for lab, kind, src in [('lem:calc', 'Lemma', 'A.21'), ('prop:generic', 'Proposition', 'A.31 and A.33 (rich limit)'),
                       ('lem:AMequiv', 'Lemma', 'A.33'), ('lem:K2delta', 'Lemma', 'A.33 (F)'),
                       ('lem:SCdelta', 'Lemma', 'A.33'), ('lem:bridgedelta', 'Lemma', 'A.30'),
                       ('prop:stabdelta', 'Proposition', 'A.31'), ('cor:opendelta', 'Corollary', 'A.32'),
                       ('thm:total', 'Theorem', 'A.34')]:
    add(lab, kind, '2026-11-13', R13, TP, 'TOTEX2 %s correct, no gap' % src)
    add(lab, kind, '2026-11-25', W, UR, 'TOTEX2 %s reread in the source and every step derived again while writing' % src)
add('thm:total', 'Theorem', '2026-11-13', I13, TP, 'TOTEX2 A.1 followed in full, no fault')
add('thm:notexact', 'Theorem', '2026-11-13', R13, TP, 'TOTEX2 A.24 correct, no gap')
add('thm:notexact', 'Theorem', '2026-11-25', W, UR, 'derived again; stated as: Theta is injective and colim Theta = 0')
add('thm:notexact', 'Theorem', '2026-11-24', C24, CO, 'all 31,176 objects with 3 to 7 vertices: no affine equalizer of v1, v2, v3 over Q, F_2, F_3, F_5 (evidence on small targets, not a proof)')
add('thm:notexact', 'Theorem', '2026-11-25', W, CO, 'the same program rerun: output identical (31,176 objects; 1,515 with an arrow from W; 0 targets); checks/totex2_affine_equalizer_check_rerun_20261125.out')
for lab, kind, src in [('lem:anchored', 'Lemma', 'A.3, A.5'), ('prop:generic2', 'Proposition', 'A.6 (the limit)'),
                       ('lem:K24two', 'Lemma', 'A.5, A.6')]:
    add(lab, kind, '2026-11-17', I17, TP, 'DER_FOLLOWUP %s followed in full, sound' % src)
    add(lab, kind, '2026-11-25', W, UR, 'derived again in the anchored form, for degree 2 and coefficients F_2')
add('lem:stab2a', 'Lemma', '2026-11-25', W, RE, 'holds; new arrangement of DER_FOLLOWUP A.6 (the bridge set with an anchor in the intersection); read by nobody else')
add('lem:stab2b', 'Lemma', '2026-11-25', W, RE, 'holds; argument of the writer; read by nobody else')
add('prop:open2', 'Proposition', '2026-11-17', I17, TP, 'DER_FOLLOWUP A.6 (the statement, by another proof) followed in full, sound')
add('prop:open2', 'Proposition', '2026-11-25', W, RE, 'holds; the empty intersection is reduced to the non-empty one; read by nobody else')
add('lem:pi1', 'Lemma', '2026-11-25', W, RE, 'holds; elementary argument in place of DER_FOLLOWUP A.4; read by nobody else')
add('lem:H2', 'Lemma', '2026-11-25', W, RE, 'holds; explicit cocycle and cycle, compare DER_FOLLOWUP A.8; read by nobody else')
add('thm:twographs', 'Theorem', '2026-11-17', I17, TP, 'DER_FOLLOWUP A.7, A.8 (every degree n >= 2) followed in full, sound')
add('thm:twographs', 'Theorem', '2026-11-25', W, UR, 'assembled from the statements above')
add('sec:manuscript', 'Section', '2026-11-25', W, BG, 'II ms. 34-36ter read in our transcription only; the two French quotations are not yet compared with the edition')
add('thm:C', 'Theorem', '2026-11-25', W, UR, 'assembled; rests on Isbell-Mitchell 1973, Theorems 1 and 3, cited from memory and not reopened')
# --- 25 Nov 2026, second pass: the independent check and the repair run -------------------------------------
n_first = len(rows)
chk = io.open('CHECK_D1_INDEPENDENT_CHECK_EVENTS.tsv', encoding='utf-8').read().split('\n')
chk_rows = [tuple(l.split('\t')) for l in chk[1:] if l.strip()]
assert all(len(r) == 5 for r in chk_rows), 'checker rows must have 5 columns'
rows.extend(chk_rows)
n_checker = len(chk_rows)
W2 = 'afbbdefd94c5db150 (Claude Fable 5.2 at effort max; repair run after the independent check)'

def add2(statement, typ, out):
    rows.append((statement, '2026-11-25', W2, typ, out))

def st(label, kind):
    return "%s %s [%s]" % (kind, num.get(label, '?'), label)

add2(st('thm:A', 'Theorem'), UR, 'R1 applied: "non-empty" added to the statement in the introduction')
add2(st('thm:C', 'Theorem'), UR, 'R7 applied; derived again: if aff C is filtered and V is a non-empty full cosieve of C, then aff V is filtered (a common successor or an equalizing arrow in aff C has its target in V)')
add2(st('def:classes', 'Definition'), UR, 'R4 and R8 applied (conditions I and IV of Isbell-Mitchell 1976; the definition of Adamek-Koubek-Reiterman; Rosicky Remark 4.5(1)); the words "in their terminology" for affine equalizer removed (Isbell-Mitchell 1973 say that pairs can be filtered in aff C)')
add2(st('thm:twographs', 'Theorem'), UR, 'R2 applied: the use of the first assertion made explicit')
add2(st('sec:manuscript', 'Section'), TP, 'R5 and R6 applied, with one correction of R5 after looking at the edition (PDF p. 24, printed p. 22): footnote 43 "Faux." marks Proposition 2.19 and footnote 45 "C\'est faux." marks the step of its proof "totalement 0-connexe implique W-infinity-aspherique"; the corollary has no footnote. Proposition 2.19 is now named in the text (sifted implies total, false). The content of the last parenthesis of R5 derived again: for X = Delta and H an acyclic simplicial set that is not weakly contractible, the inclusion i is in W-infinity and X/H is not W-infinity-aspherical')
add2('Citation [AKR]', BG, 'R3 applied: title and volume as read by the independent checker in the scan')
add2('Citation [AR]', UR, 'confirmed in the open-access copy (Theory Appl. Categ. 8 (2001), no. 3, 33-53, tac.mta.ca): Definition 1.1 (sifted: colimits over D commute in Set with finite products) and Theorem 1.6 (for non-empty D: sifted iff all categories of cospans are connected); the text now cites both')
add2('Citation [Kbook]', UR, 'new reference, confirmed in the free copy on the author page (Kbook.IV.pdf): IV.3.2 (a natural transformation gives a homotopy), Example IV.3.2.2 (initial or terminal object), IV.3.5.1 and Exercise IV.3.1 (covering spaces and morphism-inverting functors), IV.3.7 (Quillen Theorem A)')
add2('Citation [Quillen]', BG, 'not opened: no free or receipted copy; cited without section; the locators Proposition 1, Proposition 2, Corollary 2 of the first version were from memory and are removed; bibliographic data (Lecture Notes in Math. 341, pp. 85-147) as on the public Wikipedia page of Theorems A and B')
add2('Citation [JardineL8]', UR, 'new reference, confirmed in the free copy on the author page (lecture008a.pdf): Lemma 21.1 (a levelwise weak equivalence of bisimplicial sets gives a weak equivalence of diagonals); Sections 21-22 (the homotopy colimit as the diagonal of the bisimplicial set with the coproduct of the X(i_0) over the n-simplices of the nerve in degree n)')
add2('Citation [GJ]', BG, 'not opened: no free or receipted copy; now cited at chapter level (Chapter IV, Bisimplicial sets, as on the publisher chapter page); the locator "IV, Proposition 1.7" of the first version was wrong: the nLab page "bisimplicial set" and arXiv:2306.02217 give the diagonal lemma as Proposition IV.1.9')
add2('Citation [BK]', BG, 'not opened: no free copy; now cited at chapter level (Chapter XII, Homotopy direct limits, as on the publisher chapter page); "XII.5.2" was from memory and is removed')
add2('Citation [CWM]', BG, 'not opened; IX.3 confirmed at the level of public tables of contents (Chapter IX Special Limits, 3 Final Functors)')
add2('Citation [Weibel]', BG, 'not opened; now cited as Section 2.6 (Adjoint Functors and Left/Right Exactness, as in the public contents pages); "Theorem 2.6.15" was from memory and is removed')
add2('Citation [Seidel]', BG, 'not opened; title, year and pages as in the record of the TU/e research portal; the definition of a two-graph agrees with the one on A. E. Brouwer\'s page (each 4-set contains an even number of the triples); the words "in the sense of Seidel" replaced by "in the usual sense; see"')
add2('Abstract', UR, 'three one-clause glosses added (quasi-filtered, two-graphs, sifted); the gloss of sifted is Definition 1.1 of Adamek-Rosicky, equivalent to the definition used in the paper by their Theorem 1.6')
print('first pass rows', n_first, '; checker rows', n_checker, '; repair-run rows', len(rows) - n_first - n_checker)
out = io.open('CHECK_EVENTS.tsv', 'w', encoding='utf-8', newline='\n')
out.write('statement\tdate\twho\ttype\toutcome\n')
for r in rows:
    out.write('\t'.join(r) + '\n')
out.close()
print(len(rows), 'rows; unresolved labels:', [r[0] for r in rows if ' ? ' in r[0]])
