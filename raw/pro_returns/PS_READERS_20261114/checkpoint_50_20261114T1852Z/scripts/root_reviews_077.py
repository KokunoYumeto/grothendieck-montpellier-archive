from review_root import review
from pathlib import Path

review('ps_134-2_077',changes=[
(r'\over{\unsure{22}}{\unsure{61}}',r'\over{\unsure{22}}{61}','The live handwritten61 is clear; only the old typed digits remain uncertain.'),
(r"\hand{\unsure{'s|s}}",r"\hand{'s}",'A distinct raised apostrophe separates the handwritten r and s. Preserve the literal your\'s, without normalizing it.'),
(r'\mspage{77}',r'\margin{\hand{77}}','The lower-left77 is pencil archive foliation, not a second typescript folio.')
],doubts={'unsure':[
(r'\unsure{22}','doubt retained','The former typed digits are covered by the61;22 remains plausible but not secure.'),
('61','doubt resolved','The pen6 and1 are independently legible; the separate bis follows them.'),
(r"'s",'doubt resolved','The raised curved apostrophe and following s are both visible.')
],'illegible':[]},notes=[
'The live folio is61bis. The old typed digits remain doubtful22. The original intervening hyphen is visible beneath the start of bis.',
'The r is written over the old comma; a distinct apostrophe and s follow, so the resulting word is literally your\'s. No terminal comma is supplied.',
'The entire N.B. paragraph is cancelled by repeated slanted pen strokes; its typed words remain readable and stay in the diplomatic form and apparatus.',
'Both and and to are cancelled by dense but localized pen strokes, with their underlying words recoverable.',
'The lower-left77 is pencil archive foliation.'
],summary='Both halves and enlarged folio and subscription inspected. The lower half is blank except archive77. Resolved live61 and the apostrophe in your\'s, preserving uncertain old22. Confirmed the cancelled Quillen N.B., the two small deletions, the typed signature and its final period. The arXiv witness regularizes the subscription and supplies a terminal comma absent from the live source.',differences={
1244:(r"you\over{,}{r}\hand{'s}",'our transcription corrected','The image settles the apostrophe. The original comma is overwritten by r, so the live subscription is your\'s with no terminal comma; the witness prints yours,.')
})

p=Path(__file__).resolve().parents[1]/'guide_sections/134_2_appendix.tex';s=p.read_text()
if '\\subsection*{Appendix 18:' not in s:
 s+=r'''
\subsection*{Appendix 18: Linearization and recovery of a homotopy type}
Cote 134-2, sites 75--77 (folios 60--61bis), asks which algebraic data could recover the geometric constructions of Appendices16--17. Grothendieck first considers cohomology with variable twisted constant coefficients, its exact-sequence structure, cup products, and further operations, assuming the fundamental group and its coefficient category given. He then proposes the triangulated category of complexes with locally constant cohomology, together with derived tensor product and internal Hom, as a more satisfactory candidate, while explicitly changing have little idea to the cautious do'nt really know. Note31 revisits whether these abelian data suffice. By contrast, he expects the full non-abelian system of categories of locally constant higher stacks to recover the fundamental infinity-groupoid; the claim depends on the earlier higher-categorical program, not merely on the list of ordinary cohomology groups. For a fixed stratification, the analogous proposal uses complexes whose cohomology is locally constant on each stratum and, as needed, the four operations for maps between locally closed unions of strata. The question about knowing what a triangulated category is concerns the adequate formalism and its non-commutative analogue; note32 adds the derivator perspective. The final line of site76 changes fibrations and cofibrations to fibers and cofibers in the author's spelling: pen es overwrites at, the remaining ions and old closing quotes are cancelled, and new quotes close the shortened words. This physical correction is more specific than the initial transcription's deletion of the whole ending. The witness changes more simply to more simple. Site77 cancels an N.B. crediting an early Quillen approach, ends the letter with a question about the Bloch--Quillen formula, and retains the typed signature. The subscription is literally your's, with its old comma overwritten and no surviving terminal comma; the readers preserve it. The following notes qualify several earlier claims and are essential to distinguishing the 1975 letters from their later annotated reprinting.
'''
 p.write_text(s)
