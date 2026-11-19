"""Attach explicit evidence bases where no exact external theorem is cited.

Metadata only: no new research or mathematical verdict, and no fabricated
bibliographic keys. The two root-checked comparisons are contextual, not exact
matches for the undefined motivic question.
"""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
DATA={
 'P56-P011':{
  'reference_scope_note':'The literal normalization question is resolved by the recorded elementary counterexample. No external theorem is needed or claimed for that calculation; refs remains empty intentionally.',
  'evidence_basis':[
   {'path':'work/cotes5_6/outputs/algebra_checks.json','locator':'c_n_mod_p_counterexample','supports':'p=3,n=2 gives c_n=1/2 with residue2.'},
   {'path':'work/cotes5_6/code/recheck_algebra.py','locator':'factorial coefficient and modular residue calculation','supports':'Executed exact arithmetic underlying the counterexample.'},
   {'path':'work/cotes5_6/reviews/independent_proofs.md','locator':'Valuations and p-typical coefficients','supports':'General p-unit valuation, distinguished from residue-one normalization.'}]},
 'P56-P014':{
  'reference_scope_note':'The positive finite graded cases and local m³ lemma are independently proved; the earlier-run Artin counterexample is exactly recomputed. The formal-curve convention remains unidentified, so no unrelated completed/derived comparison theorem is cited as its solution.',
  'evidence_basis':[
   {'path':'work/cotes5_6/reviews/independent_proofs.md','locator':'Finite graded de Rham algebras and the local m³ lemma','supports':'Euler contraction, the local m³ deduction, and the scope of the non-graded Artin test.'},
   {'path':'work/cotes5_6/outputs/algebra_checks.json','locator':'graded_monomial_de_rham; artinian_de_rham_H0_counterexample','supports':'Five exact finite quotient complexes and the16-dimensional Jacobian-algebra counterexample.'},
   {'path':'work/cotes5_6/outputs/reading_c5_s037.txt','locator':'Transcription1007–1032 and associated notes','supports':'The actual examples and unresolved differential convention.'}]},
 'P56-P047':{
  'reference_scope_note':'No exact external theorem matches the page’s undefined motive/filtration-faithfulness assertion. The root-checked Tannakian and filtered-(φ,N) comparisons below are bounded context, not a theorem solving the manuscript question; refs remains empty for an exact match.',
  'evidence_basis':[
   {'path':'work/cotes5_6/outputs/reading_c6_s025.txt','locator':'Transcription1830–1843; P56-I145/P56-C135','supports':'The author’s foundational reservation and absence of a fixed category/functor.'},
   {'path':'work/cotes5_6/search_families.json','locator':'integral_reconstruction','supports':'Logged source searches and the explicit refusal to identify a bare filtered invariant with a stronger integral realization theory.'},
   {'path':'work/root_review/reference_evidence.json','locator':'DeligneMilne1982, Proposition2.21; ColmezFontaine2000, TheoremA','supports':'A precise Tannakian full-faithfulness/subobject criterion and an admissibility theorem in a defined filtered-(φ,N) category; neither is unrestricted motive-faithfulness.','checked_by':'root; evidence records read in this metadata update','scope':'Context only; not an exact identification of the manuscript assertion.'}]},
 'P56-P048':{
  'reference_scope_note':'The foreign typescript source and preceding definitions were not identified despite the logged searches. Exact elementary conditional estimates are available, but a broad height-theory citation would not verify the omitted descent/normalization theorem.',
  'evidence_basis':[
   {'path':'work/cotes5_6/outputs/reading_c5_s012.txt','locator':'Transcription377–385','supports':'The literal limiting-descent assertion and missing predecessor.'},
   {'path':'work/cotes5_6/outputs/reading_c5_s034.txt','locator':'Transcription944–966','supports':'The quasi-function homomorphism/symmetry fragment with missing definitions.'},
   {'path':'work/cotes5_6/search_families.json','locator':'foreign_height; exact queries and unsuccessful source matches','supports':'Néron-context and bibliographic searches did not establish exact provenance.'},
   {'path':'work/cotes5_6/reviews/independent_proofs.md','locator':'Height fragments(P56-C012,C016)','supports':'Conditional dimension and dyadic estimates only; not the missing descent theorem.'}]}}

def enrich(problems):
    byid={p['id']:p for p in problems}
    assert set(DATA)<=set(byid)
    for ident,metadata in DATA.items():
        assert byid[ident]['refs']==[],(ident,'Unexpected exact references; review metadata')
        byid[ident].update(metadata)
    return problems

if __name__=='__main__':
    p=ROOT/'problems.json';problems=json.loads(p.read_text())
    enrich(problems)
    p.write_text(json.dumps(problems,ensure_ascii=False,indent=2)+'\n')
    print('Added explicit evidence_basis and reference_scope_note to P56-P011,P014,P047,P048; no references invented and no mathematical verdict changed.')
