import sys
sys.path.insert(0,'edition/scripts')
from audit_blass_late_helpers import complete
R=[
 (r'\margin{(}leur',r'leur','The first long handwritten bracket starts beside the preceding part importante line and extends through mes collègues. Move its textual anchor to the first line of that span.'),
 ('part importante',r'\margin{\hand{(}}part importante','The first marginal curved bracket is pen and begins alongside part importante; its full span is described in the note.'),
 (r'\margin{(}de la survie',r'\margin{\hand{(}}\margin{\hand{$\vert$}}de la survie','The second curved bracket is pen. A separate short, slightly curved pen stroke lies just to its left; it is retained graphically as a short vertical mark, without assigning a textual role.'),
 ("aujourd'\nhui", "aujourd'%\nhui",'The typescript breaks after the apostrophe without an additional word space. The percent preserves that boundary when the transcription is typeset.'),
 ('------------------------','-------------------------','The enlarged underline consists of twenty-five separate typed dash strikes. The source encoded only twenty-four.'),
 (r'\margin{76}',r'\margin{\hand{76}}','Both lower-left folio digits76 are handwritten.'),
 ('A. GROTHENDIECK.','% NOTE: The first marginal bracket spans part importante through mes collègues; the second spans vités/de la survie through notre planète. Its separate short left stroke is retained as a graphic mark, with no assigned textual role.\n% NOTE: The black wedge below parmi is a hole in the paper: its mirror counterpart is visible on cote24 site75. It is not transcribed as an ink arrow.\n% NOTE: This separate sheet is retained in the diplomatic reader only, according to the requested inclusion rule.\nA. GROTHENDIECK.','Record the bracket spans, the separately visible tick and the paired physical-paper evidence for the wedge. Retain the sheet under the requested reader-selection rule.')
]
M={
 10:'The first long curved bracket is handwritten. Its upper end begins beside part importante and its lower end reaches below mes collègues; the checked anchor is moved to that span’s start.',
 15:'The second bracket is handwritten and spans the vités/de la survie region through notre planète. A separate short pen stroke to its left is retained graphically with no invented letter or punctuation function.',
 64:'The lower-left76 is handwritten; both digits are clear. It remains a marginal folio rather than replacing the typed -3- at the top.'
}
N=[
 'The sheet carries the French passage beginning fondation d’un mouvement and the signature A.GROTHENDIECK., followed by the publications list. It is retained under the requested diplomatic-only inclusion rule, without inserting it into the Blass mathematical sequence.',
 'Empty separator in the supplied NOTES field; no additional reading concern is present.',
 'The upper -3- is typed: the3 matches the body numeral in the publications list, and the heavy dashes match typed hyphen strokes. The lower-left76 is pen and is now marked explicitly as such.',
 'Empty separator in the supplied NOTES field; no additional reading concern is present.',
 'Both long brackets are pen. The first spans part importante through mes collègues; the second begins near the end of vités and continues through notre planète. Its short separate left tick is restored graphically. The apparent small mark at part importante is the upper end of the first curved bracket, not a securely separate addition.',
 'Empty separator in the supplied NOTES field; no additional reading concern is present.',
 'Paired enlargement with site75 establishes the dark wedge as a hole: the same triangular gap and paper flap appear in mirror position on the other side. No ink arrow is inferred from that shape.',
 'Empty separator in the supplied NOTES field; no additional reading concern is present.',
 'The pale reversed handwriting around the signature and heading corresponds in orientation and layout to the note on site75, including the large bent insertion leader. It is show-through and is not duplicated here.',
 'Empty separator in the supplied NOTES field; no additional reading concern is present.',
 'Fasceaux is typed without i and retained. Both printed place-name occurrences place the tilde over o, encoded Sa-tilde-o as supplied. The irregular type strikes still support Crelle and nucléaires; no bibliographic correction is made.',
 'Empty separator in the supplied NOTES field; no additional reading concern is present.',
 'The main heading has twenty-five individually visible typed dash strikes; the count is corrected. All three subject headings have continuous typed underlines, with the visible wording and scope retained.',
 'Empty separator in the supplied NOTES field; no additional reading concern is present.',
 'Tears and folds were inspected around all four edges. The text remains legible at the visible boundaries; the internal hole below parmi is separately recorded.',
 'Empty separator in the supplied NOTES field; no additional reading concern is present.',
 'There is no long direct-facing handwritten text on this side. The brackets, short tick and folio76 are the direct pen additions; the note seen faintly through the sheet is transcribed on site75.'
]
E=[]
def d(line,before,image,decision,reason,category='visual-check'):
 E.append(dict(line=line,before=before,image=image,decision=decision,reason=reason,category=category))
d('7–19','French statement and signature','Every typed word, accent, punctuation and line-end continuation read','confirmed','Both scan parts were compared, preserving the broken aujourd’hui line boundary, va-/leur and acti-/vités, the complete survival statement and the typed signature.','full-text')
d('24–44','Bibliographic items1–7','All titles, names, years, volumes and page figures read individually','confirmed','The literal scans support the supplied figures:74/1952/168–186;192/1953/35–64 and77–95;1954/240p;3/1954/57–123;16/1955/329p;8/1953/1–79;84/1956/319–384. Names, accents and typewriter irregularities remain uncorrected from outside references.','full-text')
d('46–62','Bibliographic items8–11 and final ellipsis','All words, digits, accents, underlines and three terminal dots read','confirmed','Retain9/1957/119–221;84/1956/1–7 with fasceaux;79/1957/121–138;13/1960/61 and exposés7 à17. The three final dots are separately visible near the right side.','full-text')
d('5–64','Both sides of the physical sheet compared for mirrored layers','Show-through and paper hole distinguished by matching visible forms','comparison-recorded','Site75 shows the reverse-facing publications text and the mirror position of the internal hole; site76 shows the reverse-facing pen note and bent leader. No cote25 reading is used to reconstruct either side.','cote24-comparison')
rec=complete('ega24_24_076',R,M,N,E,visual_notes='Both supplied scans read completely, including every statement word, all eleven publication items, all numerical figures, underlines, twenty-five heading dashes, the three terminal dots, all margins and folios. Enlargements compared the typed3, both curved pen brackets and separate tick, and the physical hole against its mirror counterpart on75. The sheet is preserved for the diplomatic reader only, as requested.')
print(rec['key'],rec['lines_read'],len(rec['decisions']))
