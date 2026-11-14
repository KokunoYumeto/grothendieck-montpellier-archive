from review_root import review
from brown_comparison import record
from pathlib import Path
import json

review('brown_134-2_138',changes=[
 (r'\mspage{\hand{139}}',r'\margin{139}','The handwritten 139 is archive foliation at lower left, distinct from the typed - 11 - heading.')
],doubts={},notes=[
 'The p-double-prime is typed using the two vertical strokes of a double quote, as in the preceding diagram. It denotes the same double-prime label and remains p-double-prime in the formula.',
 'The handwritten archive folio 139 is moved to a margin annotation.',
 'The page ends after dualising complexes with its comma. No continuation from the following page is imported before the scan break.'
],summary='Both halves and all 19 supplemental witness rows inspected. The source has a very pretty fibre, square brackets, complexes of stacks, of n-stacks, homeomorphisms of compatibility, excercise, and at this moment. These literal translation and wording differences are preserved. The small diagram arrows have regular compact heads and straight shafts. The later Cox footnote and numbered subtitle are absent.')
record('brown_134-2_138')

review('brown_134-2_139',changes=[
 (r'\unsure{tne|the}','tne','The enlarged crop shows a low rounded n with no ascender: tne is the literal typing. It is settled as a reading, with a separate corrected-form slip variant.'),
 (r'\mspage{\hand{140}}',r'\margin{140}','The handwritten 140 is lower-left archive pagination.')
],doubts={'unsure':[('tne','doubt resolved','The middle letter is clearly n at x-height, unlike the ascenders elsewhere in the same line. The diplomatic text therefore prints tne; the corrected forms separately record the isolated n-for-h slip.')]},notes=[
 'The enlarged crop settles tne, with a low rounded n and no h ascender. The correct article the occurs repeatedly on the same page, supporting an explicitly recorded one-off slip correction in corrected forms.',
 'The archive folio 140 is handwritten; the original typed heading is - 12 -.',
 'The substantial blank before the inclusions of these pieces is visible and contains no erased or masked text to recover. Its blank indentation is retained.',
 'The small detached spot after the in on the others is lower and irregular, without the round impression of the typed full stops. It is a speck, not a textual period.'
],summary='Both halves, enlarged tne detail, and all 22 supplemental witness rows inspected. The span has a single source dot and no endpoint dots. The source says homotopy category of functions, eventually union of, and includes a large blank before the inclusions; these are retained. Tne is visually resolved, with a separate isolated-slip correction only in corrected forms. The later derivator and Esquisse notes are absent.')
record('brown_134-2_139',exceptions={175:('on tne foundations','the arXiv text corrects','The enlarged scan has a low n, settling the literal tne. The same page repeatedly types the article the. A master variant records this isolated n-for-h slip in corrected forms only.')})
p=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_2.json';a=json.loads(p.read_text());a=[r for r in a if r['source_id']!='BROWN-DIFF:175'];a.append(dict(key='brown_134-2_139',before='on tne foundations',after='on the foundations',kind='slip corrected',reason='Isolated n-for-h typing slip, visually settled as tne; the correct article the occurs repeatedly on the same checked page.',source_id='BROWN-DIFF:175'));p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
p=Path(__file__).resolve().parents[1]/'guide_sections/brown_appendix.tex'
s=r'''\subsection*{Brown's July translation: Constructible coefficients and tubular gluing (sites 134--138)}
The next step retains more than the ordinary homotopy type by fixing an equisingular stratification and studying coefficients locally constant on each stratum. Stability under the usual operations motivates the equisingularity condition. In the two-stratum example, sheaves are reconstructed from restrictions and a comparison through the punctured tubular neighborhood; a fibration from the boundary to the closed stratum and an inclusion into the complement provide a geometric description of the gluing functor. Equivalent spans replace the boundary by the punctured tube and then the closed stratum by its tubular neighborhood. This is the content corresponding to Appendix 16, and it supplies the local model for the diagrammatic treatment that follows. Brown's source has several consequential slips. Site 135 calls both complementary strata closed, points the second inclusion from X to $X_1$, prints an extra superscript star on $i_{1*}$, and says that local constancy is true of $X_1$ where the relevant object is the comparison functor applied to $F_1$. Its wording about stability ``not only for a finite partition ... but for all'' obscures the intended distinction between constructibility after refinement and stability for one fixed partition. Site 136 says ``sheaf'' where the revised version says ``scheme'', writes the bundle as $T/X$, and prints a closed interval in the punctured-cone formula, where deleting the collapsed endpoint requires a half-open interval. A neighborhood of $X_0$ in the disjoint open stratum must be interpreted as a punctured tubular object, not an ordinary inclusion of $X_0$ in $X_1$. The diagram's congruence signs are stronger than the homotopy comparisons established in the prose. All these literal features remain in the readers. The isolated is-for-in slip in ``inclusion of the boundary is a manifold'' on site 137 alone receives an apparatus correction. The later Cox note is absent from Brown's copy; his comment 10 supplies the separate historical update.

'''
if "Brown's July translation: Constructible coefficients" not in p.read_text():p.write_text(p.read_text()+s)
