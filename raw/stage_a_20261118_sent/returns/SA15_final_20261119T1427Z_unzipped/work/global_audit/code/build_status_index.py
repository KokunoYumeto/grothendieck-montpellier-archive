"""Curated documentary-status census; never edits any owner's register.

Every status_on_pages and origin field was read in full. The numbered groups
below are hand-selected decisions, not substring/keyword classification. The
program expands those decisions and checks complete, unique coverage.
"""
from pathlib import Path
from collections import Counter,defaultdict
from datetime import datetime,timezone
import csv,hashlib,json

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent
FILES=[
 ('P56',WORK/'cotes5_6/claims.json'),
 ('P67',WORK/'cotes6_7/claims.json'),
 ('P894',WORK/'cotes8_9_4/claims.json'),
 ('P78',WORK/'root_review/claims_c7.json'),
 ('P78',WORK/'root_review/claims_c8.json'),
 ('P78',WORK/'cotes6_7/supplementary_root_claims.json')]

LABELS={
 'proved':'proved there', 'sketch':'proof sketched', 'stated':'stated without proof',
 'corrected':'corrected or withdrawn by himself', 'false':'false as stated',
 'open':'open on the pages', 'mixed':'mixed or conditional page status',
 'insufficient':'insufficient text', 'refinement':'present-run refinement'}
REASONS={
 'proved':'The owner records an on-page proof or completed calculation. This census records that documentary description and does not certify the argument.',
 'sketch':'The owner records a proof or construction sketch, including a reused proof fragment where specified. Completeness is not promoted.',
 'stated':'The owner records an assertion, invoked ingredient, or stated construction without its proof on these pages. Local qualifications remain in the original field.',
 'corrected':'The author’s recorded correction or withdrawal governs the documentary census. A modern refutation is a separate assessment.',
 'false':'The owner status reports a literal or modern validity failure. It does not independently specify the historical proof status or show that the author retracted it.',
 'open':'The owner records an explicit question, reserved existence issue, conjectural expectation, or unresolved check on the pages. Later resolution does not change this documentary bucket.',
 'mixed':'The record combines different on-page statuses or a genuinely conditional programme; no single unqualified proof/open/withdrawal label is substituted.',
 'insufficient':'The supplied status does not support a historical proof-status assignment for a determinate manuscript claim; the specific reason is recorded below.',
 'refinement':'This is a separately stated refinement record of the present consolidation, not an additional manuscript assertion; earlier diagnostic provenance is retained verbatim.'}

curated={}
def select(prefix,bucket,numbers):
    # Ranges abbreviate manually chosen identifiers; no source text is searched.
    for token in numbers.split(','):
        token=token.strip()
        if not token:continue
        ns=range(int(token.split('-')[0]),int(token.split('-')[1])+1) if '-' in token else [int(token)]
        for n in ns:
            ident=f'{prefix}-C{n:03d}'
            assert ident not in curated,ident
            curated[ident]={'census_bucket':LABELS[bucket],'documentary_component':LABELS[bucket] if bucket not in ['false','refinement','insufficient'] else '',
                'modern_validity_component':'','status_mixture':'none','normalization_reason':REASONS[bucket],
                'is_present_run_refinement':bucket=='refinement'}
            if bucket=='false':
                curated[ident]['documentary_component']='Historical proof/retraction status not separately encoded in the owner status.'
                curated[ident]['modern_validity_component']='False under the literal reading or scope specified in the original owner status.'
                curated[ident]['status_mixture']='modern/literal validity judgment only'
            elif bucket=='mixed':curated[ident]['status_mixture']='mixed documentary or conditional scope'
            elif bucket=='refinement':
                curated[ident]['documentary_component']='Not an additional manuscript assertion.'
                curated[ident]['status_mixture']='separate present-run refinement record'

# P56: all151 full statuses and origins reviewed, including the9 earlier-run-only
# records that must not be mistaken for the5 appended explicit refinements.
select('P56','proved','4,6,9,17,18,29,35,55,74')
select('P56','sketch','5,7,8,10,12,15,16,19,21,23,25,26,27,28,32,34,38,40,46,50,54,56,64,67,72,73,75,79,81,84,86,87,91,92,94,97,98,100,101,105,108,110,121,125,136,137,138,143')
select('P56','stated','1,2,11,13,14,20,30,42,43,44,47,48,49,52,69,70,71,76,78,82,99,102,106,115,120,130,132,139,142')
select('P56','open','3,22,33,36,37,41,51,58,59,60,66,77,83,85,88,89,96,103,107,109,112,113,114,117,119,124,127,129,131,133,134,135,140,145,146')
select('P56','corrected','61,68,111,116,118,122,123,126,128')
select('P56','false','31,39,53,65,90,141,144')
select('P56','insufficient','24,45,57,62,63,80,93,95,104')
select('P56','refinement','147-151')

# P67:75 manuscript-claim records plus5 separately labelled refinements.
select('P67','open','1-5,10,11,32,35,39,47,49,50,53,55,62-65,67,68,73')
select('P67','sketch','6-8,12,15,17,19-22,27,28,30,31,33,34,36,41,48,51,56,59,69,72,74,75')
select('P67','stated','9,14,16,18,29,38,40,42,43,44,46,52,54,58,66,70')
select('P67','corrected','23,24,37,71')
select('P67','false','13,26,45,57,60,61')
select('P67','mixed','25')
select('P67','refinement','76-80')

# P894: owner explicitly confirmed and recorded79 manuscript origins and3
# refinement origins. A present-run counterexample does not change C023's origin.
select('P894','proved','39,57')
select('P894','sketch','15,27,33,37,40,50,55,61,70')
select('P894','stated','1-5,7-11,17-21,24,29,30,32,35,45-47,49,51,53,54,58,62-64,71,75,79,81')
select('P894','open','6,26,36,42,43,44,48,66,68,73,74')
select('P894','corrected','16,22,28,38,41,52,67,69,72')
select('P894','false','14,25,31')
select('P894','mixed','12,13,23,34,56,59,60,65,76,80')
select('P894','refinement','77,78,82')

# Root package P78 combines c7 and c8; the supplemental C071 remains attributed
# to the root package even though its file was written by the c6/c7 agent.
select('P78','proved','28,31,32,37,45,68,70')
select('P78','sketch','1-4,7,8,10,13,22,25,29,36,38,40,51,56,58-60,66,67,69')
select('P78','stated','6,14,24,44')
select('P78','open','5,9,11,12,17,19-21,23,30,42,43,54,61-63,65')
select('P78','corrected','15,27')
select('P78','false','39,46,47,49,55')
select('P78','mixed','16,18,26,33,35,41,48,50,53,57')
select('P78','insufficient','34,52,64')
select('P78','refinement','71-73')

def explain(ident,documentary=None,modern=None,mixture=None,reason=None):
    d=curated[ident]
    if documentary is not None:d['documentary_component']=documentary
    if modern is not None:d['modern_validity_component']=modern
    if mixture is not None:d['status_mixture']=mixture
    if reason is not None:d['normalization_reason']=reason

for n in [24,45,57,62,63,80,93,95,104]:
    explain(f'P56-C{n:03d}',documentary='Explicitly not a manuscript assertion/theorem; earlier-run idea or later comparison.',
        mixture='outside historical page-status census',
        reason='The allowed census vocabulary has no earlier-run-only bucket. “Insufficient text” here means no manuscript assertion to which a historical proof status can attach, not an archival gap and not uncertainty about the earlier idea. Its original provenance is preserved.')
explain('P56-C037',modern='The recorded p=3,n=2 example refutes the suggested residue-one normalization; the page itself asks the question.',mixture='documentary open question plus modern refutation')
explain('P56-C124',documentary='An explicit à vérifier / peut-être faux question; no settled denial is recorded.',reason='A conjectural possibility of falsity is not a modern refutation and is not an authorial withdrawal; the page remains open.')
for n in [148,149,151]:
    explain(f'P56-C{n:03d}',reason='The record explicitly states a restricted reconstruction as a separate refinement. Its diagnostic content originated in the earlier run, as the origin field says; this census does not recast that content as a new discovery.')

explain('P67-C025',documentary='Unique lifting has a sketch; the anti-equivalence remains explicitly marked vérifier.',reason='Different subclaims have different documentary statuses, so neither unqualified proof-sketch nor unqualified open status represents the whole record.')
explain('P67-C040',reason='The page refers the proof to mes papiers bleus. A reference to an unavailable separate proof remains stated without proof on these pages.')
explain('P67-C046',modern='The owner records the proposed ordinary-cusp example as invalid, not the general singular de Rham discrepancy as false.',mixture='documentary assertion plus invalid-example qualification',reason='Retain stated-without-proof status for the actual assertion and keep the failed proposed example separate; do not count the whole claim as false.')
explain('P67-C066',modern='The owner fate cites modern counterexamples to the asserted integral finiteness, including torsion on A¹ and examples modulo torsion.',mixture='documentary expected assertion plus modern refutation',reason='The owner describes a stated expected property without proof; the later counterexamples belong in the modern-validity component, not a historical withdrawal bucket.')

explain('P894-C003',documentary='The surviving assertion is stated without proof; an unnecessary flatness hypothesis was canceled.',reason='Deletion of a hypothesis does not withdraw the surviving claim. Preserve the cancellation qualifier without counting the whole record as author-withdrawn.')
explain('P894-C006',documentary='The universal nonvanishing expectation is open on the pages.',modern='The owner records a modern refutation at(d,p)=(2,2).',mixture='documentary open question plus modern refutation',reason='The phrase false as stated is the modern assessment of an on-page expectation. It does not turn the historical question into an authorial retraction.')
explain('P894-C010',modern='The two witnesses disagree on G versus G*; the owner does not decide the ink.',mixture='documentary assertion plus reading discrepancy')
explain('P894-C011',documentary='An assertion is made without proof, but its twists and cohomological degree are not fully identifiable.',reason='Incomplete identification of the exact formula does not erase the explicitly recorded stated-without-proof documentary status; no mathematical resolution is inferred.')
explain('P894-C012',documentary='A coefficient-pairing computation is present, conditional on unresolved truncation and coefficient-action conventions.',reason='The convention is materially unsettled, so the record is not counted as an unqualified completed proof.')
explain('P894-C013',documentary='The claim is self-flagged; Pro and Codex disagree whether the finite isomorphism is canceled.',reason='Conflicting cancellation testimony is preserved as mixed documentary status; the census does not decide which witness represents the ink.')
explain('P894-C022',documentary='The author says the unrestricted comparison is not true in general and gives the multiplicative counterexample.',modern='The owner independently confirms the author’s counterexample.',mixture='documentary correction plus modern validation of refutation')
explain('P894-C023',documentary='The running text leaves a test open; a marginal denial is attached ambiguously.',modern='A separately attributed present-run counterexample refutes the literal assertion.',mixture='mixed documentary status plus modern refutation',reason='The author’s question/negative report remains a manuscript record. Its modern counterexample_origin does not make the claim a present-run refinement.')
explain('P894-C032',documentary='The surviving compatibility assertion is stated without proof; the initial opposite arrow is canceled.',reason='A local canceled arrow changes variance; it does not withdraw the whole surviving assertion.')
explain('P894-C034',documentary='A determinant-line construction is given, while its additional compatibility is merely asserted.',reason='Construction and compatibility have different documentary proof statuses; both are retained.')
explain('P894-C037',documentary='The owner calls the proof sketched and records a local completion on scans27–28.',reason='Retain the owner’s proof-sketch level while preserving the local completion; the census does not upgrade the global argument.')
explain('P894-C038',modern='The owner also records the withdrawn statement as false.',mixture='documentary withdrawal plus modern refutation')
explain('P894-C039',documentary='The source gives a proof ending cqfd, using standard Rosati and degree facts.',reason='Named standard premises do not make every proof a conditional programme. The owner explicitly records a completed on-page proof, with its premises retained.')
explain('P894-C044',documentary='The determinant-normalization comparison remains an open check.',modern='The literal formula without determinant signs has a rank mismatch.',mixture='documentary open comparison plus literal-formula defect')
explain('P894-C056',documentary='A revised theorem is proved only conditional on admitted crystalline, duality and saturation inputs.',reason='The owner records both an altered statement and an explicitly conditional proof; the census preserves that combined status.')
explain('P894-C057',documentary='The displayed deduction is proved from the amended exact sequence.',reason='The owner records an on-page deduction from its expressly identified amended premise, not an unproved general programme.')
explain('P894-C059',documentary='The eigenvalue comparison is asserted conditional on algebraicity of a Lefschetz inverse.',reason='The conditional premise is part of the manuscript status; a modern theorem removing it does not rewrite that status.')
explain('P894-C060',documentary='The general injectivity question is open, while n=2 and sufficiently-high-degree cases are stated.',reason='The general problem and its special cases are retained together; neither is discarded for a simpler count.')
explain('P894-C065',documentary='Open in the running text; a margin says absent section7 proves it.',reason='An absent proof reported in a margin is not a proof present on these pages. The conflicting local descriptions remain mixed.')
explain('P894-C071',modern='The owner supplies a countermodel to the formal exact-sequence inference, expressly not a geometric counterexample.',mixture='documentary assertion plus missing-hypothesis/formal-inference alarm',reason='The census records an unproved manuscript assertion and distinguishes the kind of modern defect; it does not invent a geometric refutation.')
explain('P894-C074',documentary='The rank-growth assertion is a needed expectation in the programme.',reason='An expectation is counted as open on the pages; its exact later theorem changes fate, not documentary status.')
explain('P894-C076',documentary='The point-count programme is conditional on unproved monodromy and Frobenius-distribution inputs.',reason='The owner explicitly records a conditional programme, not an unconditional assertion or completed proof.')
explain('P894-C077',documentary='The motivating manuscript says any ℓ; the standalone raw-versus-finite inertia clarification is this run’s refinement.',reason='The owner has explicitly set origin to present-run refinement. The older stated-without-proof status describes the motivating phrase, not authorship of the standalone clarified theorem.')
explain('P894-C078',documentary='The margin contains a weaker μp-conditional trace statement; this record’s removal of that hypothesis is this run’s refinement.',reason='The owner has explicitly set origin to present-run refinement. Keep the manuscript conditional margin in the original field and do not attribute the stronger theorem to it.')
explain('P894-C080',documentary='Partial coefficient computation with two OK checks; the final display is unfinished.',reason='Successful local checks and an unfinished last display coexist; no complete-proof or wholly-open status replaces them.')
explain('P894-C082',documentary='The source separates a dimension-one boundary; the explicit P1 permutation test is this run’s standalone refinement.',reason='The owner has explicitly set origin to present-run refinement. The manuscript boundary remark is the motivation, not a claim that it contains this exact test.')

explain('P78-C016',documentary='Self-flagged proof sketch with contradictory equality/inequality readings.',reason='The owner cannot isolate one exact relation from the supplied text, so the documentary record remains mixed.')
explain('P78-C018',documentary='A lift construction is sketched; the broader classification remains open.',reason='Keep the construction and broader unresolved claim together rather than counting the entire record as proved or wholly open.')
explain('P78-C020',documentary='An explicit classification question is asked without proof.',reason='Asked without proof denotes a question, not an asserted theorem lacking a proof.')
explain('P78-C023',documentary='A self-flagged deformation framework; the final obstruction is marked sans doute.',reason='The owner records an unresolved proposed framework rather than a completed assertion or demonstrated obstruction theorem.')
explain('P78-C026',documentary='Reused draft containing surviving argument, canceled proof fragments and a deleted assertion.',reason='No one withdrawal label can describe the whole composite draft record; canceled material is not silently counted as live proof.')
explain('P78-C028',documentary='The owner records a proof in the reused typescript, while flagging local letter errors.',reason='Local letter alarms remain visible but do not replace the owner’s explicit documentary description of a proof.')
for n in [31,32]:
    explain(f'P78-C{n:03d}',documentary='The owner records the stated matrix or gauge identities as computed on the pages.',reason='For a calculation claim, computed on the pages is normalized to proved there as a documentary completion label, not as a new correctness audit.')
explain('P78-C033',documentary='Gauge equations are computed, but the final complex is inconsistent in sign/order.',modern='The owner identifies the missing compatible coboundary convention; no ink choice is made.',mixture='partial computation plus literal formula inconsistency',reason='The successful preceding calculation and defective final display are both retained.')
explain('P78-C034',documentary='Only diagrams are present; the relevant category and exact assertion are not defined.',reason='There is insufficient text to assign a proof or conjecture status to one determinate mathematical assertion.')
explain('P78-C035',documentary='The ℓ=p case is open; the ℓ≠p case is asserted.',reason='The coefficient-dependent documentary split is essential and cannot be collapsed to one open/proved label.')
explain('P78-C041',documentary='A PD hypothesis is used; the ramification-boundary analysis is not supplied on the pages.',reason='The standalone reconstructed iff/boundary statement exceeds the status of the hypothesis as used. Count the record as conditional/mixed, not an on-page theorem.')
explain('P78-C043',documentary='The page explicitly reserves existence; it does not assert arbitrary realization as a proved theorem.',modern='The owner gives a counterexample to arbitrary-filtered realization, not to the page’s reserved-existence wording.',mixture='documentary open existence plus modern scope restriction')
explain('P78-C045',documentary='The decomposition is deduced on the pages using Tate’s theorem.',reason='The owner records a deduction from a named theorem; count that documentary deduction as proved there without claiming that the premise is proved on these pages.')
explain('P78-C048',documentary='Several jet statements are described collectively as proved or sketched in the reused typescript.',reason='The alternative proof levels belong to one composite record; neither is selected for all subclaims.')
explain('P78-C050',documentary='The multilinear assertion is proved; symmetric and alternating variants are left as analogues.',reason='The core proof and the unstated analogue proofs are separate documentary levels and remain mixed in this composite claim.')
explain('P78-C052',documentary='Unlabelled numerical comparisons, without an identified geometric proposition.',modern='The owner records some literal alternatives as false or undefined and others as arithmetically correct.',mixture='unidentified claim plus mixed arithmetic outcomes',reason='The arithmetic fragments do not identify one geometric statement whose historical proof status can be counted.')
explain('P78-C053',documentary='A categorical assertion is conditional on a fibre functor that is assumed, not constructed.',reason='The manuscript’s missing realization premise is material; the conditional status is retained even though a modern conditional theorem is known.')
explain('P78-C054',documentary='The category/realization proposal is open and its definition incomplete.',modern='The owner’s rank-one test refutes unrestricted dual stability of effectivity, not every possible corrected category.',mixture='documentary open definition plus modern extrapolation counterexample')
explain('P78-C057',documentary='A scaling computation is present, but the printed equation omits its torsor factor.',modern='The owner supplies an explicitly reconstructed well-typed equation.',mixture='computation plus literal typing defect',reason='The successful scaling idea and the defective equation are preserved together; this manuscript record is not recast as a standalone present-run refinement.')
explain('P78-C061',documentary='The comparison programme is open; one p-adic comparison is literally blank.',reason='A blank reserved comparison is an open problem on the pages, not evidence that the proposed comparison was proved.')
explain('P78-C064',documentary='An agenda heading names compatibility without exact quantifiers.',reason='The agenda does not supply enough text to assign one determinate assertion a proof or conjecture status; the owner’s modern counterexample is not used to invent a historical theorem.')
explain('P78-C067',documentary='A proof sketch is present in reused fragments; the last proof is cut off.',reason='The owner already specifies sketch-level status. The cutoff is preserved and no complete proof is inferred.')
explain('P78-C070',documentary='A coefficient-change calculation is given and continues at cote8:79.',reason='The owner records the computation and checked continuation; count the calculation as documentary proved there without silently replacing derived tensor by ordinary tensor.')
explain('P78-C072',documentary='The manuscript’s parent literal assertion remains P78-C046; this separate K×/integral-lattice formulation is a present-run refinement.',reason='The actual origin field says present-run refinement, and refinement_provenance attributes the diagnostic to the earlier notes. The census preserves both, without counting a new manuscript assertion or claiming a new discovery.')
explain('P78-C073',documentary='The manuscript’s unrestricted parent assertion remains P78-C047; this separate open-inertia quantifier is a present-run refinement.',reason='The actual origin field says present-run refinement, and refinement_provenance retains the earlier-run period diagnostic. The restricted theorem is not substituted for the source’s literal quantifier.')

records=[];hashes={};transport_duplicates=[];seen_records={}
for package,path in FILES:
    assert path.exists(),f'Awaiting the owner’s promised supplementary file: {path}'
    raw=path.read_bytes();hashes[str(path.relative_to(WORK))]=hashlib.sha256(raw).hexdigest()
    payload=json.loads(raw)
    if isinstance(payload,dict):
        # A named container is accepted only as transport, not as classification.
        payload=payload['claims']
    for c in payload:
        if c['id'] in seen_records:
            first_path,first_claim=seen_records[c['id']]
            assert c==first_claim,(c['id'],'Non-identical copies require owner review',str(first_path),str(path))
            transport_duplicates.append({'legacy_claim_id':c['id'],'counted_file':str(first_path.relative_to(WORK)),'identical_copy_file':str(path.relative_to(WORK))})
            continue
        seen_records[c['id']]=(path,c)
        records.append((package,path,c))
ids=[c['id'] for _,_,c in records]
assert len(ids)==len(set(ids)), 'Duplicate legacy claim ID'
assert set(ids)==set(curated),{'unclassified':sorted(set(ids)-set(curated)),'extra_curated':sorted(set(curated)-set(ids))}

# An owner can change fate/class without changing this census. Changed status
# or provenance, however, requires another human/model reading, not a blind run.
prior=ROOT/'status_input_snapshot.json'
if prior.exists():
    reviewed={r['legacy_claim_id']:r for r in json.loads(prior.read_text())}
    assert set(reviewed)==set(ids),'Claim set changed; review the new/deleted records before rebuilding.'
    for _,_,c in records:
        before=reviewed[c['id']]
        assert before['status_on_pages']==c.get('status_on_pages'),(c['id'],'status changed; reread required')
        assert before['origin_present']==('origin' in c) and before['origin']==c.get('origin'),(c['id'],'origin changed; reread required')
        assert before['counterexample_origin']==c.get('counterexample_origin'),(c['id'],'counterexample origin changed; reread required')

rows=[];snapshot=[]
for package,path,c in records:
    ident=c['id'];decision=curated[ident]
    original_origin=c.get('origin')
    if isinstance(original_origin,(dict,list)):
        origin_text=json.dumps(original_origin,ensure_ascii=False)
    else:origin_text=original_origin or ''
    row={'legacy_claim_id':ident,'package':package,'owner_file':str(path.relative_to(WORK)),
        **decision,'status_on_pages_original':c.get('status_on_pages',''),
        'origin_original':origin_text,'origin_field_present':'origin' in c,
        'counterexample_origin_original':c.get('counterexample_origin',''),
        'refinement_provenance_original':c.get('refinement_provenance',''),
        'parent_claim_original':c.get('parent',''),
        'origin_provenance_note':'Root confirmed these P78 records are manuscript/reused-text claims; an omitted field is preserved as omitted.' if package=='P78' and 'origin' not in c else 'Origin is preserved from the owner register; no origin inferred from mathematical vocabulary.'}
    rows.append(row)
    snapshot.append({'legacy_claim_id':ident,'owner_file':row['owner_file'],'status_on_pages':c.get('status_on_pages'),
        'origin_present':'origin' in c,'origin':c.get('origin'),'counterexample_origin':c.get('counterexample_origin'),
        'refinement_provenance':c.get('refinement_provenance'),'parent':c.get('parent'),
        'his_statement':c.get('his_statement'),'statement':c.get('statement'),'owner_fate':c.get('fate')})

expected_refinements={f'P56-C{n:03d}' for n in range(147,152)}|{f'P67-C{n:03d}' for n in range(76,81)}|{'P894-C077','P894-C078','P894-C082','P78-C071','P78-C072','P78-C073'}
assert {r['legacy_claim_id'] for r in rows if r['is_present_run_refinement']}==expected_refinements
assert len(rows)==386
rows.sort(key=lambda r:(['P56','P67','P78','P894'].index(r['package']),int(r['legacy_claim_id'].split('-C')[1])))
fields=['legacy_claim_id','package','owner_file','census_bucket','documentary_component','modern_validity_component',
        'status_mixture','is_present_run_refinement','status_on_pages_original','origin_original','origin_field_present',
        'counterexample_origin_original','refinement_provenance_original','parent_claim_original','origin_provenance_note','normalization_reason']
with (ROOT/'status_index.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
(ROOT/'status_curated_map.json').write_text(json.dumps(curated,ensure_ascii=False,indent=2)+'\n')
(ROOT/'status_input_snapshot.json').write_text(json.dumps(snapshot,ensure_ascii=False,indent=2)+'\n')
by_package={p:dict(Counter(r['census_bucket'] for r in rows if r['package']==p)) for p in ['P56','P67','P78','P894']}
summary={'date_utc':datetime.now(timezone.utc).isoformat(),'records':len(rows),'counts':dict(Counter(r['census_bucket'] for r in rows)),
 'by_package':by_package,'present_run_refinements':sorted(expected_refinements),'refinement_count':len(expected_refinements),
 'earlier_run_only_records_outside_historical_census':[f'P56-C{n:03d}' for n in [24,45,57,62,63,80,93,95,104]],
 'source_sha256':hashes,'identical_transport_copies_counted_once':transport_duplicates,'owner_registers_modified':False,'method':'Manual identifier-specific normalization after full status/origin reading; modern validity and documentary status are separate columns. All mathematical verdicts remain unchanged.'}
(ROOT/'status_counts.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
