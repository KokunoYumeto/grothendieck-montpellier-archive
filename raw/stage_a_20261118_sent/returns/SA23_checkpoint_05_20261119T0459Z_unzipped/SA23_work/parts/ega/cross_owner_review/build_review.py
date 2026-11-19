"""Serialize a manually conducted cross-owner object/claim comparison.

This script does not discover duplicates by keywords. Explicit proposals below
are the result of register review and direct rereading of candidate endpoints.
It changes no other owner's files and applies no merge.
"""
from pathlib import Path
import json,csv

HERE=Path(__file__).resolve().parent
PARTS=HERE.parent.parent
owners=['root','ega','bt','misc']
records={}
for owner in owners:
    for item in json.loads((PARTS/owner/'items.json').read_text()):
        if item.get('sources'):
            records[item['id']]=(owner,item)

def endpoint(item_id):
    owner,item=records[item_id]
    return {'owner':owner,'item':item_id,'entries':item['sources'],
            'cote':item['cote'],'scans':item['scans'],'source_lines':item['lines']}

proposals=[
 {
  'id':'XD-SA23-ega-01','decision':'merge indexed subject; preserve distinct subclaims',
  'target_item':'SA23-153','merge_items':['SA23-153','SA23-309'],
  'suggested_title':'Exponential and logarithm identities in nilpotent and complete algebras',
  'endpoints':[endpoint('SA23-153'),endpoint('SA23-309')],
  'common_statement':'Over a Q-algebra, exp and log are reciprocal on the stated nilpotent domains; commuting arguments carry addition to multiplication and conversely.',
  'source_based_reason':'The cote23 page explicitly specializes its complete linearly topological algebra to the discrete topology, where topological nilpotence becomes ordinary nilpotence (Pro1431–1446). Cote68 Th1 is this very finite algebraic specialization (Pro77–95), not merely a neighboring use of exp.',
  'claims':['C-SA23-ega-032','C-SA23-misc-005','C-SA23-misc-006','C-SA23-misc-007','C-SA23-misc-008'],
  'claim_merge_scope':'C-misc005/006 coincide with the discrete-case inverse and commuting-law components of C-ega032. Keep the topological convergence, power-stable-subspace and commutativity-converse components separately stated; do not collapse their scopes or status categories.',
  'preserve':['The false literal cote23 display log(gg′)=log(g)log(g′) and its dual-number refutation.','The separate cote68 marginal exp1=0 reading alarm.','Cote68’s live réciproque? question and its exact universal-identity interpretation.','Closedness/topology hypotheses in cote23 versus finite polynomial hypotheses in cote68.'],
  'direct_rereads':['sources/texts/pro/MPL_22+23_002-016_transcription.tex:1420–1460','sources/texts/pro/MPL_68_033-056+162-1+162-6_transcription.tex:74–133','sources/notes/pro/MPL_22+23_002-016_notes.md:E08','sources/notes/pro/MPL_68_033-056+162-1+162-6_notes.md:E01,U01'],
  'confidence':'high',
 },
 {
  'id':'XD-SA23-ega-02','decision':'merge indexed subject; preserve extensions',
  'target_item':'SA23-162','merge_items':['SA23-162','SA23-315'],
  'suggested_title':'Nilpotent derivations, tensor actions and unipotent algebra automorphisms',
  'endpoints':[endpoint('SA23-162'),endpoint('SA23-315')],
  'common_statement':'For a uniformly nilpotent endomorphism D of a module with a bilinear multiplication over a Q-algebra, D is a derivation if and only if exp(D) preserves the multiplication; associativity, a unit and commutativity are not required.',
  'source_based_reason':'Cote23 writes exactly this equivalence for a k-bilinear product (Pro1692–1700). Cote68 explicitly allows nonassociative/nonunital/noncommutative products and concludes that for nilpotent u the same criterion is equivalent to exp(u) being an algebra automorphism (Pro376–380). The hypotheses and object agree.',
  'claims':['C-SA23-ega-035','C-SA23-misc-016','C-SA23-misc-017','C-SA23-misc-039'],
  'claim_merge_scope':'C-misc017’s nilpotent one-exponential criterion is the first part of C-ega035. Keep the formal Ga version, tensor-generator calculation, tensor/symmetric/exterior extensions, and augmented-base BCH specialization as separately scoped subclaims.',
  'preserve':['Uniform nilpotence in the single exp(D) criterion.','The formal-parameter action statement for an arbitrary infinitesimal endomorphism.','Degreewise versus uniform nilpotence on an unbounded tensor algebra.','The square-zero/BCH specialization in cote23 and the fact that its supplied verification belongs to the earlier run.'],
  'direct_rereads':['sources/texts/pro/MPL_22+23_002-016_transcription.tex:1674–1700,1734–1774','sources/texts/pro/MPL_68_033-056+162-1+162-6_transcription.tex:359–385','sources/notes/pro/MPL_22+23_002-016_notes.md:E17,E21','sources/notes/pro/MPL_68_033-056+162-1+162-6_notes.md:E07'],
  'confidence':'high',
 },
 {
  'id':'XD-SA23-ega-03','decision':'merge indexed subject; retain nil versus nilpotent distinction',
  'target_item':'SA23-163','merge_items':['SA23-163','SA23-310'],
  'suggested_title':'Endomorphism ideals over a nilpotent scalar ideal',
  'endpoints':[endpoint('SA23-163'),endpoint('SA23-310')],
  'common_statement':'For a scalar ideal J with J^n=0 and a module M, L={u in End_K(M):u(M)⊂JM} satisfies L^n=0. Finite exp/log identify L with automorphisms reducing to the identity modulo J.',
  'source_based_reason':'Both sources write the same endomorphism ideal and identity-mod-J group. Cote23 inserts the common exponent and calls the whole ideal nilpotent (Pro1704–1731). Cote68 Example2 visibly inserts J nilpotent before the same construction (Pro112–130). The augmented-algebra version is a specialization of the scalar-ideal formulation.',
  'claims':['C-SA23-ega-035','C-SA23-misc-009','C-SA23-misc-010'],
  'claim_merge_scope':'C-misc010 matches the scalar-ideal subclaim attached to SA23-163 and used in C-ega035. C-misc009 is the preceding merely nil central-ideal example and must remain a separately quantified statement within the subject.',
  'preserve':['K-linearity over the scalar ring; this is what raises the J-adic filtration.','J^n=0 as a common ideal bound, stronger than each element of J being nilpotent.','The source explicitly includes the required hypothesis, contrary to the earlier contextual omission.','Do not merge with the false statement about a derivation whose image lies in an internal nilpotent ideal (SA23-326).'],
  'direct_rereads':['sources/texts/pro/MPL_22+23_002-016_transcription.tex:1704–1731','sources/texts/pro/MPL_68_033-056+162-1+162-6_transcription.tex:104–130','sources/notes/pro/MPL_22+23_002-016_notes.md:E18','sources/notes/pro/MPL_68_033-056+162-1+162-6_notes.md:E02'],
  'confidence':'high',
 }
]

# These comparisons were judged at the statement/object level in the four
# completed registers. The direct-source reread scope is explicitly above.
distinct=[
 ('SA23-68','SA23-118;SA23-119;SA23-120','Vector-bundle determinant/norm and Riemann–Roch formula on curves versus local completion traces, divisor e/f transfer and towers; different assertions.'),
 ('SA23-63','SA23-146;SA23-147;SA23-148','Universal integral Chern polynomial for regular immersions versus adjunction determinants and the elliptic cubic weight6 calculation.'),
 ('SA23-42;SA23-43;SA23-44;SA23-45;SA23-46;SA23-47;SA23-48;SA23-49;SA23-50;SA23-51;SA23-52;SA23-53;SA23-54;SA23-55;SA23-56;SA23-57;SA23-58','SA23-108;SA23-115;SA23-117','Relative perfectness/support K-theory versus cotangent Tor and regularity criteria; shared homological vocabulary does not identify a common theorem.'),
 ('SA23-21;SA23-22;SA23-23;SA23-24','SA23-336;SA23-337;SA23-338;SA23-339;SA23-340;SA23-341','Exterior operations and lambda induction versus axioms for a graded determinant-line functor and change-of-splitting invariance.'),
 ('SA23-153','SA23-320','Generic exp/log commuting formula versus the distinct composition-sign reading on a sheaf derivation/automorphism leaf; retain source-specific alarm and link the formal calculus.'),
 ('SA23-162','SA23-313;SA23-318','Uniformly nilpotent finite exponential criterion versus locally nilpotent Ga actions and intertwining statements with different quantifiers.'),
 ('SA23-163','SA23-326','Scalar-linear endomorphisms raise the scalar-ideal filtration; a derivation with image in an internal ideal need not. The latter false implication is a separate subject.'),
 ('SA23-157','SA23-311;SA23-316','Primitive-element kernel base change versus Hom/End base change under finite projectivity; different morphisms and finiteness obstructions.'),
 ('SA23-164','SA23-325','Relative derivation/Hom adjunction versus exp(D) fixes the base iff D vanishes on it; related base algebra but different statements.'),
 ('SA23-152;SA23-165','SA23-207;SA23-211;SA23-234','Coordinate integrability and infinitesimal conjugation versus group logarithmic forms and Cartan homotopies; operators and ambient objects differ.'),
 ('SA23-162','SA23-226','Automorphisms by exp/log versus the torsor comparing two smooth lifts across a square-zero extension; the latter is not merely an automorphism group calculation.'),
 ('SA23-159','SA23-238','Cartier Hopf algebra reconstruction versus a Tannakian tensor stabilizer; different categories and universal constructions.'),
]

target={
 'id':'XD-SA23-ega-T01',
 'source_routing':'The requested detached leaf is present as sources/texts/codex/K161-1-01_transcription.tex scan17, archive sheet15, lines579–636. The supplied routing is161-1; the request called it161-2. No physical relocation or renumbering is inferred.',
 'item_decision':{
  'decision':'consolidate only the common cocharacter subsubject; keep the undefined endpoint distinct',
  'proposed_shared_subject':'SA23-265',
  'additional_occurrence':'C-SA23-groupes-016 from SA23-904',
  'retain_item':'SA23-904',
  'retained_scope':'C-SA23-groupes-017: underdefined filtered-F-crystal/de Rham/Tate comparison endpoint on the detached leaf.',
  'do_not_alias_whole_item':True,
  'related_items':['SA23-263','SA23-264','SA23-266','SA23-268','SA23-269','SA23-270','SA23-275'],
 },
 'common_mathematics':{
  'assumptions':'Fix G, the scalar field Ω, a coefficient action σ on Ω, a representation ρ:π→G(Qp), and a tensor grading on the scalar-extended fibre functor invariant under the diagonal semilinear action ρ(σ)∘σ.',
  'identity':'ρ(σ) σ(j) ρ(σ)^−1 = j, equivalently σ(j)=ρ(σ)^−1 j ρ(σ).',
  'exact_match':'The detached leaf writes all three forms including its weight-space explanation (K161-1-01:601–618). The161-5 leaf defines the diagonal inner-twisted GΩ! and a π-invariant j! (Pro1301–1313; Codex318–322). After identifying the underlying Ω-group this is the identical conditional invariance statement.',
  'qualification':'This identifies a common construction, not a proof that the source category is crystalline, nor a choice of Tate line, a descent theorem, or a unique cocharacter determined by π-invariance alone.'
 },
 'claim_decisions':[
  {'claims':['C-SA23-groupes-016','C-SA23-bt-068','C-SA23-bt-069'],'decision':'shared conditional cocharacter-invariance component; retain full claim IDs because other components differ','reason':'C-groupes016 supplies an explicit source proof of the conditional conjugation formula. C-bt068 additionally records genuine twist-sign and action-order witness conflicts; C-bt069 additionally records an unfinished uniqueness qualification. Do not identify those residual components with the settled formula.'},
  {'claims':['C-SA23-groupes-017','C-SA23-bt-067'],'decision':'related, not duplicate','reason':'The detached final comparison is underdefined; bt067 has an actual pair of coefficient-only/diagonal equivariant fibre functors and an isomorphism torsor. Identifying their general framework does not determine the final P,Pf,G′,G′f symbols.'},
  {'claims':['C-SA23-groupes-017','C-SA23-bt-070','C-SA23-bt-071','C-SA23-bt-072'],'decision':'keep distinct','reason':'The161-5 source separately asks tensor/internal-Hom extension, uniqueness relative to comparison data, and a splitting torsor. The detached leaf does not fix the category, fields and admissibility needed to identify any exact one of these theorem/problem statements.'},
 ],
 'problem_decisions':{
  'retain':'MP-SA23-groupes-07',
  'related':['MP-SA23-bt-21','MP-SA23-bt-22','MP-SA23-bt-23'],
  'decision':'link; do not merge',
  'reason':'The groupes problem is source identification of undefined comparison symbols; bt21 is extension, bt22 is uniqueness, and bt23 is cocharacter uniqueness plus splitting. The conditional conjugation identity settles none of those missing hypotheses.'
 },
 'frozen_discrepancies':['Pro1344 SΩ(i) versus Codex333 SΩ(−i).','Pro1292 τ(α)uτ(α)^−1 versus Codex310 τ(α)^−1uτ(α).','The detached K/L comparison label and field diagram are unresolved.','All two-weight Hodge–Tate objects versus the actual BT-generated crystalline category remain distinct.','The Γ-extension problem and its actions are not specified by π-invariance of j.'],
 'direct_rereads':['sources/texts/codex/K161-1-01_transcription.tex:577–636','sources/notes/codex/K161-1-01_notes.md:complete','sources/texts/pro/MPL_93_221-236+161-5_transcription.tex:1125–1206,1275–1410','sources/texts/codex/K161-5-02_transcription.tex:264–378'],
 'confidence':'high for conditional identity; medium for contextual linkage of undefined endpoint',
 'applied':False,
}

for name,value in [('indexed_duplicate_proposals.json',proposals),('targeted_tannakian_review.json',target)]:
    (HERE/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
with (HERE/'related_not_duplicate.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['left_items','right_items','reason']);w.writerows(distinct)
merges={i:p['id'] for p in proposals for i in p['merge_items']}
with (HERE/'item_review_coverage.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['owner','item_id','entry_ids','review_level','decision','proposal'])
    for ident,(owner,item) in sorted(records.items(),key=lambda r:int(r[0].split('-')[-1])):
        w.writerow([owner,ident,';'.join(item['sources']),'manual object/claim comparison of completed registers; candidate endpoints reread where proposed','merge proposed' if ident in merges else 'retain; no cross-owner equivalent identified',merges.get(ident,'')])
checks=[]
for p in proposals:
    for source in p['direct_rereads']:
        checks.append([p['id'],'2026-11-19','direct transcription or indexed-note reread',source,'Endpoint read and manually compared; no scan inspection or textual emendation.'])
for source in target['direct_rereads']:
    checks.append([target['id'],'2026-11-19','direct transcription or Codex-note reread',source,'Conditional action, fields, prime labels and witness conflicts compared.'])
with (HERE/'source_checks.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['review_id','date','type','source','outcome']);w.writerows(checks)

counts={owner:sum(v[0]==owner for v in records.values()) for owner in owners}
entry_ids={e for _,i in records.values() for e in i['sources']}
summary={'indexed_items_reviewed':len(records),'by_owner':counts,'indexed_entry_ids':len(entry_ids),'proposed_merge_groups':len(proposals),'subject_count_if_accepted':len(records)-sum(len(p['merge_items'])-1 for p in proposals),'entry_ids_lost':0,'owner_files_mutated':False,'whole_tannakian_claims_or_problems_merged':False}
(HERE/'validation.json').write_text(json.dumps(summary,indent=2)+'\n')
md=f'''# Cross-owner duplicate review

The manual review covered **{len(records)} indexed subject records** across root, ega, bt and misc, representing **{len(entry_ids)} indexed entries**. Three subject merges are proposed. If all are accepted, this indexed subset has **{summary['subject_count_if_accepted']} consolidated subjects** and the same entry coverage. No other owner's file was changed and no merge was applied here.

The comparison used the mathematical object, quantifiers and asserted relation in each completed item/claim register. Candidate source paragraphs and their indexed notes were then reread directly. It is not a keyword or title matching exercise. Full candidate endpoints and limits are in the JSON; the286-row coverage file records the review scope. This is a cross-owner review, not a second complete proof audit or an intra-owner restructuring.

## Proposed indexed merges

| Target | Merge into that subject | Exact common object | Preserve separately |
|---|---|---|---|
|SA23-153|SA23-309|exp/log inverse and commuting product identities; cote23 explicitly includes the discrete finite case|Topological convergence; power-stable subspaces; commutativity converse; both literal reading alarms|
|SA23-162|SA23-315|Uniformly nilpotent derivation iff its exponential preserves an arbitrary bilinear product|Formal parameter version, tensor extensions, BCH and square-zero specialization|
|SA23-163|SA23-310|L={{u:uM⊂JM}} has Lⁿ=0 when Jⁿ=0, and exp identifies identity-mod-J automorphisms|Merely nil versus nilpotent scalar ideal; scalar linearity; the separate false internal-ideal derivation claim|

These are subject mergers. Individual mathematical subclaims, occurrence IDs, authorial versus reconstructed proofs, and different page statuses must survive. In particular, the correct cote68 logarithm formula is another witness; it does not repair the frozen cote23 transcription.

## Targeted Tannakian comparison

The requested detached leaf is routed in the supplied sources as **K161-1-01 scan17, archive sheet15**, although the request referred to cote161-2. Its explicit formula is precisely the conditional invariance statement implicit in the161-5 definition of the diagonal inner-twisted group and π-invariant cocharacter. The source endpoints are K161-1-01:601–618, Pro161-5:1301–1313 and CodexK161-5-02:318–322.

For integration, attach the common cocharacter subsubject of **C-SA23-groupes-016** to **SA23-265** as an additional archival occurrence. Retain **SA23-904** for the unresolved comparison endpoint **C-SA23-groupes-017**, with related links to SA23-263/264/266/268/269/270/275. Do not alias the whole item or whole claim: bt068 also contains the actual transcription conflicts, and bt069 contains an unfinished uniqueness assertion.

Keep **MP-SA23-groupes-07** distinct from **MP-SA23-bt-21–23**. The first is an identification problem for undefined comparison symbols. The others ask extension, rigidified uniqueness and cocharacter/splitting questions. The cocharacter identity alone supplies neither crystalline admissibility nor descent or canonical splittings. Pro/Codex Tate signs, U-action inverse order, K/L routing and the larger Γ action remain unresolved exactly as recorded.

## Retained distinctions

The related_not_duplicate.tsv table records twelve potentially tempting cross-owner comparisons that remain distinct. These include norm/trace objects, Chern versus adjunction formulas, homological criteria versus relative perfectness, determinant functors versus lambda operations, base-change maps, and several differential/representation constructions. Shared words or a common formal technique do not make their questions identical.

## Files and limits

`indexed_duplicate_proposals.json` supplies exact entry unions, item/claim scopes, source locators and preservation requirements. `targeted_tannakian_review.json` separates item, claim and problem decisions. `source_checks.tsv` records the endpoint rereads; `item_review_coverage.tsv` records all indexed items examined; `validation.json` states the counts. No new literature search was needed for this source-comparison task. No scans were available, and no alternative reading is silently preferred.
'''
(HERE/'indexed_duplicate_review.md').write_text(md)
print(json.dumps(summary))
