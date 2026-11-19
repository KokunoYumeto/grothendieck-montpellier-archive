"""Literal extraction from manually selected and individually read line ranges.

This script does not choose ranges, classify claims, or change any register.
Each selection and scope note below was manually assessed against the source.
"""
from pathlib import Path
import json,re,hashlib,datetime

B=Path(__file__).resolve().parents[2]
P=B/'SA23_work/integration'
source=B/'sources/texts/api/ega_v_cote25_combined.tex'
raw=source.read_bytes();lines=raw.decode().splitlines()
claims={c['id']:c for c in json.loads((B/'SA23_work/parts/hyperplanes/claims.json').read_text())}
decisions=[]
def select(n,spans,reason,missing=(),note=''):
    decisions.append(dict(number=n,spans=spans,reason=reason,missing=list(missing),note=note))

select(18,[(1301,1303,'literal equality claim'),(1316,1318,'associated-support version with inequality'),
           (1342,1345,'codepth and inserted S_(k-1) qualification'),(1369,1369,'later inserted same-S_k claim')],
       'The current first19-line excerpt shows equality2 and the module bound but omits the exact same-S_k assertion assessed as false. Keep the insertion at1369 and the nearby S_(k-1) qualification visible.')
select(21,[(1508,1518,'smooth/unramified hypotheses and conormal definition'),
           (1591,1595,'scheme equality and dimension'),(1676,1685,'theorem with ramification and ordinary-point wording')],
       'Replace the tangent-space preamble with the actual hypotheses and Theorem8.7(a,b). The literal ordinary-point wording must remain as transcribed, alongside the modern qualification.',
       [(1508,1518,'The recorded range starts1572 and omits the hypotheses and conormal definition; scan37 is already listed.')])
select(23,[(1870,1876,'characteristic-zero corollary'),(1884,1890,'general pencil and one singular point'),
           (1907,1911,'initial reglee terminology'),(1913,1918,'explicit request for inseparable examples'),
           (2112,2115,'authorial withdrawal of terminology')],
       'The original excerpt begins in the preceding double-tangent discussion and does not reach the actual pencil conclusion or the later terminology retraction.',
       [(2112,2115,'The retraction on scan51 lies outside1852–1930, although scan51 is listed in the record.')])
select(26,[(2083,2087,'complete conjectural clause8.17(a)')],
       'The present range and excerpt start in the final codimension line; they omit the subject, geometric irreducibility and image-dimension hypotheses.',
       [(2083,2085,'The first three lines of the conjecture are outside the current2086–2116 range.')],
       'Do not substitute the surface example8.17(b) or inserted surface clause(c) for this arbitrary-morphism conjecture.')
select(35,[(2562,2567,'arbitrary quasi-coherent E and quotient functor'),
           (2584,2596,'quasi-compactness and deletion of finite type before smoothness')],
       'Select the actual finiteness assertions and preserve the deletion of de type fini. The initial current excerpt reaches quasi-compactness but stops before the smoothness clause.')
select(37,[(2610,2614,'residue-point lifting and infinite-field sentence, first half'),
           (2625,2625,'infinite-field sentence, continuation'),
           (2627,2629,'projective subbundle from a quotient, first half'),
           (2631,2638,'subbundle/functor interpretation, continuation'),
           (2645,2648,'exact Grassmann duality formula'),(2672,2677,'containment as quotient factorization')],
       'The modern statement combines clauses occurring before the recorded start2650. The current quote instead starts with the geometric explanation after the duality formula.',
       [(2610,2614,'Residue-point lifting and infinite-field density are on scan63, missing from both the current line range and scan list.'),
        (2625,2638,'The completion of the density sentence and projective-subbundle definition precede2650.'),
        (2645,2648,'The exact Grass_n(E)=Grass_(r-n)(dual E) formula is before the current range.')],
       'Ranges are intentionally split at page furniture and a transcription NOTE. Join only with an explicit excerpt separator; do not rewrite the broken sentence or dual notation.')
select(41,[(2918,2923,'hypotheses and singular incidence'),(2953,2963,'stratum definition, formula, admitted range and calculation doubt')],
       'Use the actual displayed codimension formula and both bounds on k; the initial excerpt spends its space on the general incidence description. Preserve sauf erreur de calcul.')
select(45,[(3323,3332,'complete proposed relative elementary-neighborhood variant')],
       'The current quote starts in the previous proof and finite-field discussion. These lines state the projective-flat, geometric R2, finite-subscheme and avoidance hypotheses directly.',
       note='The source says sans demonstration and asserts the variant; this literal wording is more precise than making it an explicit interrogative sentence.')
select(57,[(3885,3894,'faint finite-partition witness and uniqueness'),
           (3929,3938,'clear Z-indexed witness and uniqueness'),(3988,3995,'uniqueness relative to the comparison isomorphism')],
       'Keep both witnesses instead of quoting faint heading material. The chosen-isomorphism qualification occurs in the proof and should accompany the bare uniqueness wording.',
       note='All uncertainty markup in the faint witness is retained. The source itself does not insert quasi-compactness; that remains part of the modern assessment.')
select(68,[(4962,4966,'first literal every-t regularity condition'),
           (4967,4975,'proposition with geometric quantifier'),(4977,4983,'authorial injectivity interpretation and requested explanation')],
       'The current excerpt starts at the line-bundle construction. The two exact quantifiers omitting nonzero are both on scan124 and are the clauses being assessed.')
select(70,[(5054,5067,'deleted unrestricted5.3'),(5076,5080,'revised4.3 hypotheses, first half'),
           (5090,5093,'associated-component hypothesis and conclusion, continuation'),
           (5100,5108,'authorial warning and explicit counterexample')],
       'Use the deleted assertion and its revised replacement, with the author’s own counterexample, rather than the preceding Grassmann interpretation.',
       note='The deletion wrapper is retained; the page break between5080 and5090 is a genuine excerpt boundary, not a license to restore missing wording.')
select(72,[(5194,5197,'infinitesimal base-change reduction, first half'),
           (5208,5214,'Artin-local reduction and infinitesimal difference'),
           (5227,5235,'tangent space for Div'),(5246,5249,'normal-bundle continuation and tangent space for Hom'),
           (5258,5264,'explicit dependence on deferred infinitesimal calculations')],
       'The modern tangent formulas occur well after the current opening quotation. Preserve the displayed O_(P_o) in the Hom formula: replacing it by the modern O_(X_o) in a literal quote would silently repair the source.')
select(74,[(5302,5308,'Proposition4.4(a) and extra hypotheses for(b)'),
           (5325,5328,'regular nonzero meromorphic-section condition'),
           (5336,5348,'deferred proof, base-extension concern and requested general formulation')],
       'The current opening passage concerns descent. These selected clauses contain the actual rational-member assertion and the explicit deferred-proof/generalization cues.')
select(76,[(5362,5362,'letter date'),(5415,5421,'entire deleted constructibility and filtered-limit argument')],
       'Replace the letter’s table-of-contents and authorship discussion with the actual mathematical argument. Preserve its deletion wrapper and uncertain depth symbol.')
select(78,[(5593,5599,'clear early polar-form definition'),(5601,5608,'cancelled multiplicity claim'),
           (6266,6282,'explicit recognition of the characteristic2 error'),
           (6306,6310,'ordinary means smooth quadratic form'),(6349,6354,'definition through the projective zero locus')],
       'An excerpt from the faint opening page does not exhibit the later self-correction. The clear early witness and the exact correction must be quoted as distinct occurrences.',
       [(6266,6282,'The scan158 self-correction is outside the current5520–5620 range.'),
        (6306,6310,'The scan159 replacement terminology is outside the current range.'),
        (6349,6354,'The scan160 smooth-projective-zero-locus definition is outside the current range.')],
       'The first early witness at scan139 remains in the source record; this quotation uses its clearer scan140 counterpart and does not adjudicate the faint text.')
select(79,[(5642,5644,'principal-part setup'),(5646,5650,'proposition with cancelled second-jet assertion'),
           (5668,5673,'singular-zero scheme'),(5690,5697,'polar map and determinant'),
           (5708,5714,'zero scheme of the determinant and deferred proposition')],
       'Quote the actual cancelled d2 assertion and its replacement, rather than the preceding general remarks about singularities.',
       [(5708,5714,'The explicit closed subscheme defined by the determinant continues onto scan143, beyond the current5624–5701 range and scan141–142 list.')])
select(82,[(5749,5765,'exact sequence and literal sheaf-injectivity criterion')],
       'The source starts with the needed sequence but the decisive sentence is5756–5757. Keep both the X/S parenthetical hypothesis and the literal W lisse sur X wording; neither should be silently corrected.')
select(84,[(5913,5924,'isolated singularity and early ambient-dimension threshold'),
           (6460,6469,'later intrinsic local-ring threshold'),
           (6471,6486,'geometric version with intrinsic dimension d')],
       'The current first lines discuss determinant diagrams, not normality. The later intrinsic threshold is a separate supporting/correcting occurrence.',
       [(6460,6469,'The scan163 local-ring threshold is absent from the current5871–5942 range.'),
        (6471,6486,'The scan163 geometric intrinsic-dimension statement is likewise absent.')])
select(90,[(6162,6174,'page15 equivalence wording to which the correction refers'),
           (6201,6207,'constant-rank lemma with scheme-theoretic exterior-power vanishing'),
           (6581,6583,'explicit correction of page15 line10'),
           (6707,6716,'later local-free cokernel and kernel base-change assertion')],
       'The current excerpt contains the lemma but omits the earlier equivalence targeted by the correction and the later base-change sentence.',
       [(6162,6174,'Scan154/page15 is the actual earlier equivalence; it is absent from both current lines and scans.'),
        (6581,6583,'Scan166 correction is listed by scan but has no physical-line occurrence.'),
        (6707,6716,'Scan169 kernel base-change assertion is listed by scan but has no physical-line occurrence.')],
       'Precision flag: scan166 says page15 line10, the i.e. is abusive. Its direct antecedent is scan154 line6164, not explicitly the separately stated lemma on scan155/page16. Keep the two source formulations distinct.')
select(91,[(6241,6245,'complete rank-drop lower-bound footnote')],
       'The existing excerpt begins with the unrelated ramification-identity exercise. These five lines contain the false lower bound, including the inserted regular-base assumption.')
select(103,[(7218,7225,'definition of orthogonal stabilizer'),
            (7226,7238,'isomorphism object as orthogonal torsor'),
            (7249,7254,'explicit equivalence of fibered categories by flat descent')],
       'The existing quote and entire physical-line range discuss the earlier classification of forms and never reach the stated torsor equivalence.',
       [(7218,7238,'The orthogonal torsor construction is on scan182, after the current7128–7203 range and outside the scan180–181 list.'),
        (7249,7254,'The categorical equivalence is explicitly stated on scan183, also absent from both locator fields.')])
select(104,[(7256,7262,'exact smoothness criterion'),(7277,7280,'odd-characteristic2 obstruction context'),
            (7292,7299,'inseparability and mu2/SO reduction')],
       'The current excerpt is an algebraically closed-field classification proof. The smoothness criterion and mu2 quotient appear only later; retain the exceptional-rank/characteristic context.')
select(105,[(7256,7273,'smoothness hypothesis, etale triviality and finite-etale strengthening'),
            (7275,7280,'local-base strengthening and explicit exceptional case'),
            (7292,7300,'inseparable rank1 example and finite-flat/mu2 reduction')],
       'Replace the earlier classification proof with16.13–16.14, which actually states the local trivialization results and the characteristic2 example.',
       note='Question-scope flag: these paragraphs assert the cover results and provide the rank1 counterexample; they do not ask for that example. The nearby explicit question at7193–7195 and7210–7216 concerns prior knowledge/terminology of the corrected discriminant and16.9. If the modern last sentence means a cover-specific question, no such cue was located in7167–7304.')

scan_at={};scan=None
for i,line in enumerate(lines,1):
    m=re.search(r'\\scanpage\{25/(\d+)\}',line)
    if m:scan=int(m.group(1))
    scan_at[i]=scan

records=[]
for d in decisions:
    cid=f"C-SA23-hyp-{d['number']:03d}";c=claims[cid]
    excerpts=[]
    for a,b,role in d['spans']:
        text='\n'.join(lines[a-1:b])
        assert not any(x.startswith('%') or x.startswith('\\clearpage') or x.startswith('\\scanpage') or x.startswith('\\mspage') for x in lines[a-1:b]),(cid,a,b,'page furniture in selection')
        excerpts.append(dict(first_line=a,last_line=b,scans=sorted({scan_at[i] for i in range(a,b+1)}),role=role,verbatim=text))
    gaps=[dict(first_line=a,last_line=b,scans=sorted({scan_at[i] for i in range(a,b+1)}),reason=why,
               recommended_locator=f'texts/api/ega_v_cote25_combined.tex:{a}–{b}') for a,b,why in d['missing']]
    records.append(dict(claim_id=cid,assessed_statement_snapshot=c['statement'],
        original_lines=c['lines'],original_scans=c['scans'],
        action='replace literal excerpt; preserve full assessed scope',selection_reason=d['reason'],
        selected_excerpts=excerpts,
        recommended_quote_locators=[f'texts/api/ega_v_cote25_combined.tex:{a}–{b}' for a,b,_ in d['spans']],
        missing_occurrence_locators=gaps,scope_or_reading_note=d['note']))

out=dict(date='2026-11-19',owner='bt',task='Bounded manual quotation and occurrence-locator audit of selected hyperplanes claims',
         source_path='sources/texts/api/ega_v_cote25_combined.tex',source_sha256=hashlib.sha256(raw).hexdigest(),
         method='Every selected passage was read directly with physical line numbers and compared with the modern statement. The code only copies the manually selected literal ranges and attaches scan metadata. No proofs or literature were redone; no source or claim register was altered.',
         application_note='Keep each verbatim segment literal, including deletion, insertion and uncertainty markup. Separate noncontiguous segments explicitly. Recommended quote locators supplement, rather than erase, the existing full assessed scope. Missing occurrences need separate locator additions. Scope flags on090 and105 require editorial judgment, not an automatic replacement.',
         counts=dict(records=len(records),records_with_missing_occurrences=sum(bool(r['missing_occurrence_locators']) for r in records),
                     selected_segments=sum(len(r['selected_excerpts']) for r in records)),records=records)
(P/'hyperplanes_quote_audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out['counts']))
print('Source hash unchanged:',hashlib.sha256(source.read_bytes()).hexdigest()==out['source_sha256'])
