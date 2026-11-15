from review_root import review
from brown_comparison import record
from pathlib import Path

review('brown_134-2_140',changes=[],doubts={},notes=[
 'The original heading is typed - 13 -; the lower-left handwritten 141 is archive foliation and its margin annotation is correct.',
 'The mark before P- consists of the two short strokes of a typed opening double quote, darkened by impression; no cancellation or replacement is visible.',
 'The exclamation point after Rf is below the baseline, while that after g is raised. Their opposite subscript/superscript placement is clear and retained. The mixture of f and g in the four operations is also literal.'
],summary='Both halves and all 31 supplemental witness rows inspected. The source clearly prints non-etale tubular neighbourhoods, although the preceding construction and revised witness say etale. It retains One thought, no way to retrieve more, finer homotopy type, and the f/g mixture in the four operations. P_X and P_Y have baseline hyphens, not superscript minus signs. No new paragraph follows non-singular strata in this copy.')
record('brown_134-2_140')

review('brown_134-2_141',changes=[],doubts={},notes=[
 'The lower-left handwritten 142 is archive pagination and is correctly retained in the margin.',
 'The small detached dash under the final exclamation point has no link to the text, no second matching stroke, and no legible character form. It is a stray mark rather than added punctuation.'
],summary='Both halves and all 23 supplemental witness rows inspected. Everything, the singular finiteness theorem, in homotopy, elementary constituents, and more fun even mystery are literal. The two later paragraph beginnings are retained without an invented subtitle or stars. The cohomological product has i and j on its factors, i+j on its target, and a typed tensor-product sign; no index or arrow correction is needed.')
record('brown_134-2_141')

p=Path(__file__).resolve().parents[1]/'guide_sections/brown_appendix.tex'
s=r'''\subsection*{Brown's July translation: Diagrammatic and fine homotopy types (sites 138--141)}
The tubular span is generalized to a diagram of homotopy types with locally constant coefficients on its vertices and compatibility maps along its arrows. Tame equisingular spaces are proposed to admit a finite dévissage by manifolds with boundary, locally trivial fibrations, and boundary inclusions; adapted stratifications of a map should then express the direct and inverse image operations. Passage to finer stratifications is intended to retain all constructible information in the fine homotopy type. This corresponds to Appendix 17 and anticipates the main text's insistence on homotopy theories of diagrams. The distinction is essential: one needs to localize the category of diagrams, rather than simply replace each object by its image in the ordinary homotopy category and discard coherence. Brown's site 139 obscures that contrast with ``as based'' and the literal ``category of functions'', where the revised version speaks of fractions; the later note explicitly connecting the construction to derivators is absent. Site 138 says homeomorphisms for the compatibility maps of sheaves, although these are homomorphisms and need not be invertible. Site 140 mixes f and its restriction g in the displayed four operations and prints ``non-étale tubular neighbourhoods'', conflicting with the étale construction just proposed. These remain source-level cautions. The finiteness claim on site 141 is part of an explicitly unfinished program: prime-to-characteristic profinite completions of finite polyhedral or compact manifold models are envisaged, with nonliftable positive-characteristic varieties singled out as mysterious. Its stronger present-tense wording should not be read as a proof of the proposed theory. The next paragraph expressly says that a precise algebraic program has not yet been drawn up and turns to linearization.

'''
if "Brown's July translation: Diagrammatic and fine" not in p.read_text():p.write_text(p.read_text()+s)
