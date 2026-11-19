"""Counts-only status metadata, manually assigned after reading all 217 statuses.

No mathematical record is edited. One canonical row represents M027 + L011.
The explicit lists below are judgments, not keyword classifications.
"""
import csv,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
source={}
for folder in ['cote137','cote138_early','cote138_middle','cote138_late']:
 for c in json.loads((ROOT/'workers'/folder/'claims.json').read_text()):
  assert c['id'] not in source
  source[c['id']]=c
assert len(source)==217

P='proved there';S='proof sketched';U='stated without proof';R='corrected by himself later';F='false as stated';O='open on the pages';N='not identifiable'
manual={
'137':{
 P:[1,5,15,25,38,43],
 S:[2,6,7,10,11,18,21,28,29,31,32,37,41,45,46,47],
 U:[4,22,35,40,42,49,52],
 R:[8,26,34,39,44,48],
 F:[3,9,12,13,14,16,17,20,27,33],
 O:[19,23,24,30,36,50,51]},
'138E':{
 S:[1,3,4,12,17,18,24,25,26,27,31,36,40,42,45,47],
 U:[2,5,7,9,11,13,14,16,29,34,39],
 R:[6,33],
 F:[10,15,19,21,22,28,30,32,35,38,44],
 O:[8,20,23,37,41,43,46,48]},
'138M':{
 P:[35],
 S:[1,3,6,8,14,15],
 U:[9,13,19,23,25,26,27,31,32,33],
 R:[2,12,16],
 F:[5,10,11,17,21,24,28],
 O:[4,7,18,20,22,29,30,34]},
'138L':{
 P:[38,47,65],
 S:[12,30,31,39,40,42,45,54,63,68],
 U:[1,2,3,7,8,10,13,14,18,21,23,24,26,27,28,29,32,33,34,35,36,37,48,49,50,51,55,56,58,59,60,61,64,66,69,70,73,77,78],
 R:[6,52,67],
 F:[9,15,16,17,19,20,22,25,41,43,72,81],
 O:[4,5,44,46,53,57,62,71,74,75,76,79,82],
 N:[80]}}

reasons={
'137-052':'The component labels the inserted printed source as stated without proof. This counts its treatment in the packet, not a Grothendieck-authored theorem; Sullivan provenance remains in the mathematical record.',
'138E-006':'An explicit deletion and replacement changes surjectivity onto the arithmetic group to equality of images while retaining geometric-kernel surjectivity. Both source places and this distinction remain in original_status.',
'138E-033':'The failed cone/cubing attempts are replaced later by the six-bijection/cone construction. The reporting bucket follows the authorial revision, not a new declaration that every associated assertion was proved.',
'138M-001':'Displayed maps and local indices constitute a sketch; the missing full branch-divisor calculation prevents treating the page as a complete certificate.',
'138M-002':'The universal-cover assertion is explicitly struck out, and the later inverse-limit notation clarifies the object. The bucket includes this authorial withdrawal/correction.',
'138M-003':'The coordinate calculation is written, with doubtful digits. Its status remains a sketch rather than an unconditional completed coordinate proof.',
'138M-004':'Odd powers and the cubic example are present, but the requested rational coordinate functions are explicitly queried; the authorial question controls the reporting status.',
'138M-005':'The false reading is conditional on keeping the adjacent positive-conic model. The possibility of an unstated model change remains verbatim and is not decided by this bucket.',
'138M-006':'The page gives scratch elimination without a global ramification argument, so its appropriate reporting level is proof sketched.',
'138M-007':'The diagram has an explicit unfinished/questioned slot. The displayed finite quotient definition does not complete that diagram; no new claim of global nonidentifiability is imposed.',
'138M-008':'The coordinate bijection is supplied, while choices and inverse reconstruction remain implicit; this is a sketch.',
'138M-009':'Detailed conditions are asserted without a proof. Their later omission of a target-arrow condition is not silently imported as a different status for this record.',
'138M-010':'The failure is conditional on the earlier arbitrary-category target. The target-groupoid repair remains part of the original qualification.',
'138M-011':'The failure concerns the live formula without connectedness. Connectedness in cancelled setup is retained as a qualification, not silently restored.',
'138M-012':'The author explicitly changes centralizer to normalizer. This revision is counted under corrected by himself later even though the resulting normalizer calculation remains unfinished.',
'138M-013':'The identity and orbit assertions are displayed without proof; the doubtful index is retained rather than resolved by grouping.',
'138M-014':'Numerical manipulation of the formula and its consequences gives a proof sketch, without promoting the cited general theorem into a full on-page proof.',
'138M-015':'The triple classification and numerical argument are partly supplied. The unfinished/restarted four-point argument and conflicting inequalities remain qualified in original_status.',
'138M-016':'The requested correction bucket also records withdrawal: this assertion lies in an entirely cancelled draft. The bucket does not say that the underlying modern classification is false or that a live proof survives.',
'138M-017':'False as stated is conditional on applying the cancelled inseparability adjective to the group quotient. Cancellation and conditional scope remain explicit.',
'138M-018':'The genus-zero verification is expressly deferred inside a cancelled draft. It is counted as an on-page open step, not as a surviving current conjecture.',
'138M-019':'Compactification and orientation data are described without proof; no proof or new exception is inferred from the later literature.',
'138M-020':'The groupoid/peripheral comparison is expressly deferred, so it remains open on the pages despite available modern frameworks.',
'138M-021':'The failure is conditional on reading the arrow as an isomorphism with the entire exterior square. The corrected pairing interpretation remains in the claim record.',
'138M-022':'The marked refinement is explicitly flagged vérifier. The unmarked paradigm does not close that separate authorial verification step.',
'138M-023':'The fibre-product construction is asserted without proof, while the full involution system is not certified because indices are uncertain. The reporting bucket does not suppress that limitation.',
'138M-024':'The early nu>=1 injection is false, while the later nu>=2 version is valid. Because the later restriction is not labelled an explicit retraction, the primary authored false-as-stated status is retained rather than recast as an authorial correction.',
'138M-025':'The source says surjectivity is proved but supplies no proof. That verbal claim is counted as stated without proof, not proved there.',
'138M-026':'A torsor/twisted-target construction is said to work, with no complete descent proof. Construction assertions without an exhibited proof are grouped as stated without proof.',
'138M-027':'Canonical merger of CL-SA09-138M-027 and CL-SA09-138L-011. M027 originally reads “construction said to work: extension and multiplier displayed; no faithfulness claim is made.” L011 originally reads “stated without proof.” The merged arithmetic action/common-character record is stated without proof; the later Tate limit and puncture-independence statement do not supply a proof of faithfulness or change that status.',
'138M-028':'The false conclusion is conditional on taking the literal cyclic target as the cyclotomic action target. The unit-automorphism repair remains separate.',
'138M-029':'The naive version is cancelled, but the replacement is itself explicitly flagged. The record concerns that unresolved replacement, so the reporting group is open on the pages.',
'138M-030':'The order-two interpretation belongs to the flagged proposed reversal; the later reconstruction is not counted as an on-page proof.',
'138M-031':'Compatibility equations are displayed as a working construction, with a doubtful subscript and no proof sequence. Grouped as stated without proof, preserving the construction and notation qualifications.',
'138M-032':'The ambient tilded/untilded convention conflicts. The authored primary status is an unproved assertion; the conditional failure under the pure interpretation is not promoted into an unqualified false assertion by counts metadata.',
'138M-033':'The splitting and containment are asserted constructions without proof. Their statement is not an equality of the arithmetic image with the target; grouped as stated without proof.',
'138M-034':'Explicit wish, question and interrupted continuation constitute an on-page open programme, even though further definitions are needed for a modern theorem.',
'138M-035':'The conjugation identity supplying normality is explicitly written. The centrelessness requirement for naming the inner subgroup by the free profinite group is retained.',
'138L-006':'The author asks about equality and then explicitly rejects the rank-two case on the same page. This is an authorial correction; the current all-rank deduction does not replace that historical status.',
'138L-009':'The literal field-isomorphism reading is false, but the target symbol is uncertain. The conditional scope remains verbatim; this bucket does not decide the ink.',
'138L-013':'The primary authored status is stated without proof. Its additional warning that the unredefined literal symbols are false remains explicit; counts metadata does not resolve the missing acting group or torsor quotient.',
'138L-016':'The literal functor/faithfulness formulation fails, while the source itself leaves faithfulness uncertain. Both the counterexample scope and authorial uncertainty remain explicit.',
'138L-017':'The cell-pinning rigidity assertion is false in its unrestricted scope and is itself marked for verification. The false-as-stated bucket does not erase that self-flag.',
'138L-019':'The false count is the displayed uniform-count reading. The corrected orbit-stabilizer formula and conditional reading remain in the mathematical record.',
'138L-020':'The raw representability formulation fails, with part of its setup deleted. The deletion is retained rather than treated as a completed repair.',
'138L-025':'The surviving negation gives the false reading. The bucket does not infer the meaning of uncertain literal generator labels.',
'138L-037':'The surviving permutation assertion is unproved on the page. Uncertain entries and a cancelled trial remain explicit; the later exhaustive computation is not counted as the author’s proof.',
'138L-039':'Intermediate reduction steps are supplied, but signs and factors are doubtful; retained as a proof sketch with the original reading qualifications.',
'138L-043':'The failure is conditional on interpreting the display as quotient by the product ideal (PQ). The possible intended localization/saturation is not an ink correction.',
'138L-047':'The logarithmic-derivative identity is proved on the page. The unfilled final numerator is retained as an unfinished continuation, not silently counted as proved.',
'138L-048':'The degree equalities are stated without proof; the isolated 6N term remains unidentified. The identifiable degree assertion permits the requested stated-without-proof bucket without pretending to interpret the marginal symbol.',
'138L-049':'This is the unproved catalogue group/passport block. Its one conditional mismatch is preserved and separately indexed; the whole block is not recast as a single false theorem.',
'138L-051':'The bound and impossible cases are unproved source assertions. The arithmetically inconsistent degree heading remains a separate qualification and reading alarm.',
'138L-052':'The source explicitly replaces one group label within the same annotation. This is counted as the author’s correction without deciding every diagram interpretation.',
'138L-053':'The catalogue is a draft without a completeness proof; the current exhaustive census is not attributed to the page.',
'138L-054':'The isotopy-quotient argument is sketched. Its X/C notation changes remain explicit rather than being silently repaired by the reporting group.',
'138L-055':'Finite-quotient descent is explicitly assumed, and the proposed extension is given without proof. The bucket records the unproved extension, not an obligation to prove an assumption for all functors.',
'138L-057':'The universal powerset quotient has an unfinished denominator, so its classification remains an on-page open construction.',
'138L-059':'Graph and union assertions are stated without proof, with a damaged union clause. No additional theorem or definitive restoration is created by grouping.',
'138L-060':'A cellularity assertion is written without proof, but its quantifier is damaged. The finite modern repair is not substituted for the author’s undecided reading.',
'138L-061':'A construction is asserted without a proof of realization. It belongs in stated without proof rather than proved there merely because a standard construction now exists.',
'138L-062':'The exceptional case is left as a question; the uncertain arrow is retained. The current local explanation does not alter its on-page open status.',
'138L-064':'The source asserts equivalences and calls an implication evident, but does not define the rigidification space or prove contractibility. The reporting status is the unproved assertion; class F separately retains its identification limit.',
'138L-065':'The page displays the matrix square and solves (1-c)^2=1 to obtain c=0 or 2. This concrete computation is grouped as proved there; the nondegeneracy convention c!=1 remains in the modern statement.',
'138L-066':'The fibre identities are stated computationally, without a displayed general proof. Grouped as stated without proof; the additional false strict-clean interpretation remains verbatim and is not counted as an authorial correction.',
'138L-067':'The author raises literal uniqueness and immediately gives his own spherical counterexamples. Grouped as corrected by himself later, not left as an unanswered blanket question.',
'138L-068':'The classification theorem is invoked as the proof source, but the local application and identity-component uniqueness are not fully written. This is a proof sketch, not a fresh on-page proof of the entire classification theorem.',
'138L-069':'The primary source status is an unproved equivalence, with an explicitly false literal reverse implication. That caveat is retained; the counts group records the mode of assertion and does not reverse the counterexample verdict.',
'138L-070':'The group labels are asserted without proof and conflict with the real/equatorial conditions. The original field/group inconsistency remains explicit; no ink convention is decided.',
'138L-071':'The conformal argument is suggested while the claim remains expressly tentative. The current finite proof is not retroactively counted as proved there.',
'138L-075':'The page lists conditions and leaves implications unfinished; it does not assert all six equivalent. Grouped as an on-page open comparison.',
'138L-076':'A characterization is proposed and actively revised. Grouped as open on the pages; the corrected strict-clean criterion and the folded-edge interpretation remain separate from the source’s unresolved proposal.',
'138L-077':'The group label is an unproved assertion with a mismatch conditional on the map identification and the D4 convention. Those conditions are not promoted into an unconditional source error by a status count.',
'138L-078':'The group label is unproved and its mismatch depends on the nested-bouquet drawing interpretation. The conditional scope remains explicit.',
'138L-079':'An explicit elementary-orbit and operation programme is unfinished; a present-run example does not complete the universal programme.',
'138L-080':'The isolated symbols identify no definite function, quantifier or proposition. None of the six requested proof/open/correction categories can be assigned without inventing a statement, so not identifiable is unavoidable.',
'138L-081':'The unrestricted implication is false literally, but the fragment’s intended scope is uncertain. Both parts remain in original_status; the reporting group does not supply a missing premise.',
'138L-082':'The local check is visibly unfinished and its map letters uncertain. Grouped as an on-page open step, while the record’s class F continues to mark the unidentified factor assignment.'
}

rows=[];seen=set()
for family,buckets in manual.items():
 for group,numbers in buckets.items():
  for n in numbers:
   short=f'{family}-{n:03}';ident='CL-SA09-'+short
   assert ident in source and ident not in seen,(ident,group)
   seen.add(ident);original=source[ident]['status_on_pages']
   if ident=='CL-SA09-138M-027':
    original='stated without proof: arithmetic extension and multiplier displayed on83; the Tate limit and independence of puncture index are explicit on94–95. No faithfulness assertion is made.'
   reason=reasons.get(short,'The authored on-page status is exactly this requested reporting category. This metadata preserves the claim record and does not replace its hypotheses, fate or proof assessment.')
   # Every nonstandard status has a separately written semantic grouping reason.
   assert original==group or short in reasons,(ident,original,group)
   rows.append(dict(claim_id=ident,status_group=group,original_status=original,grouping_reason=reason))
expected=set(source)-{'CL-SA09-138L-011'}
assert seen==expected,(seen-expected,expected-seen)
assert len(rows)==216
rows.sort(key=lambda x:x['claim_id'])
path=ROOT/'claim_status_groups.tsv'
with path.open('w') as f:
 w=csv.DictWriter(f,fieldnames=['claim_id','status_group','original_status','grouping_reason'],delimiter='\t');w.writeheader();w.writerows(rows)
counts=dict(Counter(r['status_group'] for r in rows))
audit={'component_claims_read':len(source),'canonical_claims':len(rows),'alias_removed':'CL-SA09-138L-011','alias_target':'CL-SA09-138M-027','counts':counts,'manual_assignment':True,'mathematical_records_changed':False,'all_nonstandard_statuses_have_explicit_reasons':True,'policy':'Counts preserve the primary authored on-page description, with compound caveats retained verbatim. Authorial withdrawal/correction is distinct from present-day refutation. Current proofs are not retroactively attributed to the source.'}
(ROOT/'outputs'/'claim_status_groups_validation.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(audit,ensure_ascii=False,indent=2))
