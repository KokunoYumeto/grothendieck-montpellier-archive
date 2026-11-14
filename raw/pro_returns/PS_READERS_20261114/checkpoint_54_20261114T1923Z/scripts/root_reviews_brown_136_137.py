from review_root import review
from brown_comparison import record
from pathlib import Path
import json

review('brown_134-2_136',changes=[
 (r'\amalg_{\partial T}',r'\underset{\partial T}{\hand{\amalg}}','The amalgamation sign is hand-drawn with two uneven upright strokes on a thick baseline; its partial-T label is typed directly below.')
],doubts={},notes=[
 'The typed heading is - 9 -; the lower-left handwritten 137 is an archive folio and its margin placement is correct.',
 'Both interval endpoints close with a right-facing square bracket. The second is closed in the source even though the punctured-cone description requires a half-open interval; this is explained in the guide.',
 'The diagram has a wave over two horizontal bars in each of its two comparison signs, whereas the preceding running formulas use a wave over one bar. The congruence-versus-simeq distinction is retained.'
],summary='Both halves, enlarged amalgamation symbol and diagram, and all 15 supplemental witness rows inspected. The source plainly has that, sheaf, T/X, tilde-X_1, and the closed interval endpoint. The amalgamation sign is pen with a typed base label. The diagram arrowheads have the compact typewriter form and separate straight shafts, unlike the thick freehand triangle on site 132; the source notation remains otherwise unchanged.')
record('brown_134-2_136')

review('brown_134-2_137',changes=[],doubts={},notes=[
 'The original heading is typed - 10 -; handwritten 138 at lower left is archive pagination and remains in the margin annotation.',
 'Deformation, write, and a little have darker typewriter impressions. They are not handwriting. Both diagram targets and prime labels are clear; the horizontal arrowheads show doubled type impressions, not an extra mathematical arrow.'
],summary='Both halves and all four supplemental witness rows inspected. Both spans point from punctured T right to X_1 and down to X_0 or T; p-prime and p-double-prime are clear, with no missing label on the last horizontal arrow. The literal phrase inclusion of the boundary is a manifold has an isolated is-for-in typing slip; an explicit master variant corrects only that phrase in the corrected forms. The text still says X_1, not tilde-X_1, when naming the sheaf base.')
record('brown_134-2_137',exceptions={147:('the inclusion of the boundary is a manifold with boundary','the arXiv text corrects','The scan types is. The immediately preceding inclusion construction and ordinary in in in practice on the same page settle an isolated s-for-n typing slip. The master records is to in in corrected forms only; no other geometric claim is changed.')})
p=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_2.json';a=json.loads(p.read_text());a=[r for r in a if r['source_id']!='BROWN-DIFF:147'];a.append(dict(key='brown_134-2_137',before='the inclusion of the boundary is a manifold',after='the inclusion of the boundary in a manifold',kind='slip corrected',reason='Isolated s-for-n typing slip in the preposition introducing the ambient manifold; the same page correctly types in in the immediately preceding in practice. The diplomatic form preserves is.',source_id='BROWN-DIFF:147'));p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
