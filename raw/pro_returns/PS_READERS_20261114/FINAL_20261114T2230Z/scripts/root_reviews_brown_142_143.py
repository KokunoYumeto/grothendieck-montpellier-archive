from review_root import review
from brown_comparison import record
from pathlib import Path

review('brown_134-2_142',changes=[
 (r'\mspage{\hand{143}}',r'\margin{143}','The handwritten 143 is lower-left archive foliation, separate from the typed - 15 - heading.')
],doubts={},notes=[
 'The blank between of and product is visibly empty. No cup symbol or word is recoverable and none is supplied from the revised witness.',
 'The only handwriting is the lower-left archive 143. The double-struck L over the tensor product and the double-struck R before Hom have regular typewriter forms and remain typed.'
],summary='Both halves and all 28 supplemental witness rows inspected. The blank before product is retained. The source has singular pi_1-module, ones disposal, give, and n-stacks of constructible sheaves without an added locally constant qualification. The absence of the later negative-answer footnote matters to the status of the proposed abelian reconstruction; it is explained in the guide. All visible text and the two paragraphs are complete.')
record('brown_134-2_142')

review('brown_134-2_143',changes=[
 (r'\mspage{\hand{144}}',r'\margin{144}','The handwritten 144 is the lower-left archive folio, not part of the typed signature or original - 16 - heading.')
],doubts={},notes=[
 'The double-struck R and the double-struck L over tensor have regular special type-element forms. The L of Lg-star is plain. The functor symbols, lower shriek and star, upper star and shriek, and inclusion primes are all clear and remain typed.',
 'Only the archive 144 is handwritten; the entire closing salutation and Alexandre Grothendieck signature, including its final period, are typed.'
],summary='Both halves and all 18 supplemental witness rows inspected. The source says fibrations and cofibrations, not the later fibres/cofibres, and retains the full typed NB on Quillen at the beginning of the years 70. The later derivator note is absent. The request about the Bloch-Quillen formula, verbose, Very cordially to you, and the complete typed signature are all preserved. No visual doubts remain.')
record('brown_134-2_143')

p=Path(__file__).resolve().parents[1]/'guide_sections/brown_appendix.tex'
s=r'''\subsection*{Brown's July translation: Linearization and reconstruction (sites 141--143)}
The closing mathematical discussion asks how much cohomological information reconstructs a homotopy type: twisted coefficients, exact-sequence functoriality, products, and other cohomology operations lead to the candidate of a triangulated derived category with derived tensor product and Hom. Grothendieck expresses uncertainty about that abelian candidate and greater confidence in reconstruction from the full higher categories of stacks. The stratified version should similarly recover mixed homotopy information from coefficients subordinate to a fixed stratification and the operations along inclusions of unions of strata. This is the precursor to Appendix 18 and to the later demand for a richer notion than a bare triangulated category. Brown's text must be read with its limitations: site 142 says n-stacks of constructible sheaves where the ordinary reconstruction discussion requires a locally constant qualification; the following paragraph separately imposes local constancy on each stratum. The blank before product is genuinely empty and is not filled with the witness's cup. Most significantly, the later author's footnote reporting a negative answer to the proposed abelian recovery is absent from this earlier copy, so Brown's question remains open in its own textual state. Site 143 prints operations of fibrations and cofibrations and retains a full NB about Quillen's early-1970s approach; the revised 1983 version changes these to fibers and cofibers, cancels the NB, and adds the derivator discussion. These are distinct conceptual and chronological layers. The letter closes with the request for the Bloch--Quillen formula, not with a claimed solution to the reconstruction program.

'''
s=s.replace('is genuinely empty','is empty')
if "Brown's July translation: Linearization and reconstruction" not in p.read_text():p.write_text(p.read_text()+s)
overview=r'''\subsection*{Brown's translation and comments: Overview of the appendix}
The complete appendix preserves Brown's earlier English copy as an independent textual state: an introductory note, eleven comments updating the program in 1982, the February 1975 postscript on local systems and integration, and a July extract moving from weak higher structures to stratified topology and reconstruction. The February claims about successive deloopings must be read with the July withdrawal of the simple identification of iterated loop structures with strict commutativity. Brown's comments then distinguish the accomplishments of crossed complexes, group-groupoids, and multiple groupoids from the still broader homotopy program. The July extract explicitly omits the biduality and homology discussion; the corresponding material, added subtitles, and retrospective notes in the 1983 version are not interpolated. The guide's detailed paragraphs identify consequential translation slips and source formulas, while the supplemental Brown concordance accounts for every supplied witness difference. This copy is particularly useful for following the development of the program: its earlier questions coexist with the later author's retractions only when the two versions are compared, not when they are silently merged.

'''
if "Brown's translation and comments: Overview" not in p.read_text():p.write_text(overview+p.read_text())
