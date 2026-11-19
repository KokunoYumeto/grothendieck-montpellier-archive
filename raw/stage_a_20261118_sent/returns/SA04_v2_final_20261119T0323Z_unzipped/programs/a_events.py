"""Record completed evidence operations; never infer verdicts from source cues.

The item, claim, reference and proof descriptions were authored after actual
reading. This program serializes those records and links actual saved searches.
It does not label a statement comparison as a proof or a finite test as a theorem.
"""
from pathlib import Path
import csv,json,re

WORK=Path(__file__).resolve().parents[1]
OUT=WORK/'parts/a'
DATE='2026-11-19'
WHO='GPT-6 Astra Pro; inherited reasoning effort not exposed; SA04/notes_93_a'
claims=json.loads((OUT/'claims.json').read_text())
items=json.loads((OUT/'items.json').read_text())
references=list(csv.DictReader((OUT/'reference_checks.tsv').open(),delimiter='\t'))
refmap={r['key']:r for r in references}
events=[]
def event(sid,typ,outcome):
    events.append(dict(statement_id=sid,date=DATE,who=WHO,type=typ,outcome=outcome))

for item in items:
    event(item['id'],'used and rechecked in this run',
      'TEXTUAL COMPARISON ONLY, not a mathematical proof. '+
      'Source: '+'; '.join(item['lines'])+'. '+item['check_reason'])

for claim in claims:
    event(claim['id'],'used and rechecked in this run',
      'TEXTUAL STATEMENT AND HYPOTHESIS COMPARISON, not a proof. '+
      'Source: '+'; '.join(claim['lines'])+'. Page status: '+claim['status_on_pages']+'. '+claim['computation'].get('source_page_assessment',''))
    event(claim['id'],'used and rechecked in this run',
      'LITERATURE FATE COMPARISON, not an independent proof. '+claim['fate']+
      ' Exact primary locators: '+'; '.join(k+': '+refmap[k]['locator'] for k in claim['refs'])+'.')

for reference in references:
    limited=reference['key'] in {'Cohen1959','HillePhillips1957','Arlettaz1990','BerthelotMessing1990','Bourbaki1967','Bourbaki2019','GrothPublishedWorks'}
    event(reference['key'],'used and rechecked in this run',
      ('BIBLIOGRAPHIC/METADATA CHECK ONLY; no independent proof check of the original work. ' if limited else 'REFERENCE STATEMENT/HYPOTHESIS CHECK; not an independent re-proof. ')+
      reference['locator']+'. '+reference['verification']+' URL: '+reference['url'])

# These are actual written arguments in proof_checks.md, with precise scope.
proofs={
 2:('targeted proof check','Domain and codomain composition identifies the two reversed FV identity subscripts. This does not decide the ink.'),
 8:('targeted proof check','For a finite projective module over a perfect-ring Witt ring, p-torsion freeness gives injective F,V and the two mod-p kernel/image identities. Projectivity of the Hodge quotient and the general all-crystal assertion are not proved by this argument.'),
 18:('independent re-proof','The disjoint union of Fp-points has global endomorphisms product Zp; the compatible family p^(-n) has no uniform denominator. Hence global isogeny localization fails morphism descent. Extension of an additive functor to the localization is its universal property.'),
 23:('targeted proof check','The displayed rank-two example has total tH=tN=1 but the stable e0 line has tH=1>0=tN. This refutes a rank-only admissibility criterion, using necessity of weak admissibility from Colmez–Fontaine as an external input.'),
 34:('independent re-proof','The finite geometric sum is 1-gamma+gamma(1-gamma)^n and converges to 1-gamma for 0<gamma<1. The proposed infinite sum is1. This is an arithmetic discrepancy, not a certification of the full factorization induction.'),
 35:('targeted proof check','Only the endpoint of the corrected induction is checked: continuity of multiplication gives z=xy once the required convergences are known. Existence of the factorization and the induction are supplied by de Jeu–Jiang, not independently re-proved here.'),
 36:('independent re-proof','Finite Fourier coefficient extraction gives the universal coefficient formula with factor2pi. The uniform growth bound kills every coefficient above alpha. The written proof is general; the program normalization check is supplementary.'),
 37:('independent re-proof','The same extraction kills the integer endpoint coefficient under uniform little-o, or pointwise little-o with the preceding uniform big-O domination. The undominated raywise statement is not proved.'),
 38:('targeted proof check','Apply the verified weighted-entire-function result to the entire resolvent with coefficients x^j. Nilpotence follows under the stated uniformity/domination hypothesis and with the same element x throughout.'),
 39:('independent re-proof','The polynomial (z-1)^(-2) has inside coefficients n+1 and outside coefficients n-1, refuting the big-O strict-degree formulation. Under little-o, the finite/tail split proves the epsilon boundary estimate after rescaling its constant.'),
 40:('independent re-proof','For A=|w+1/2| and B=|w-1/2|, A²-B²=2R cos(theta). The outside-disk estimate therefore needs the opposite sign. The w=-2 example satisfies R>=1 and has positive left side and negative right side.'),
 42:('independent re-proof','The resolvent identity gives R_lambda(1+(lambda-lambda0)R_lambda0)=R_lambda0, establishing the centre-norm Neumann radius. The scalar example 1/lambda on C* satisfies the printed moving-norm bound but its proposed series diverges.'),
 43:('independent re-proof','The corrected local Neumann expression yields R prime=-R²; induction proves R^(n)=(-1)^n n!R^(n+1) for every n. No initial continuity assumption is needed.'),
 44:('independent re-proof','Comparison of all Laurent coefficients in the two-variable resolvent identity yields c0²=0, c1²=c1, their orthogonality, corner relations and recurrence c_(n+1)=c_n c2. This proves the general decomposition; the matrix example is supplementary.'),
 45:('independent re-proof','Invert one value and use the resolvent identity in both product orders to show every value is the inverse of lambda-x. Conversely each genuine resolvent value is invertible.'),
 46:('independent re-proof','The rational identity in the commutative subalgebra generated by x proves the local geometric-series pseudo-resolvent identity on its norm-convergence disk.'),
 47:('independent re-proof','The scalar u=1,w=2,C=2,gamma=0 example satisfies every antecedent for every positive eta and refutes the target yw-u. The corrected target yw-w follows from gamma a^(-1)(w-uw) and the Neumann norm estimate.'),
 50:('targeted proof check','For compact X the compact-support singular-cohomology direct limit has terminal compact set K=X, giving ordinary cohomology. This does not establish a general sheaf/singular comparison.'),
 51:('targeted proof check','Alternating dimensions in bounded finite long exact sequences prove the Euler identity, conditional on existence of the specified closed/open support sequence.'),
 52:('targeted proof check','Finite exact-sequence dimension cancellation proves the excisive Mayer–Vietoris identity and finiteness implications. The point-in-circle example refutes the version with the union hypothesis omitted. Mere closedness is not independently promoted to singular excision.'),
 53:('independent re-proof','Homotopy domination splits ordinary cohomology, and homotopy equivalence preserves its Euler number. R and a point show that arbitrary homotopy equivalence does not preserve compact-support Euler number.'),
 54:('independent re-proof','The hemisphere/equator recurrence gives chi(S^n)=1+(-1)^n for every n; a compact-support cell gives chi_c(R^n)=(-1)^n and ordinary contractibility gives1.'),
 55:('independent re-proof','Successive application of closed/open additivity to the finite excisive cellular filtration gives the alternating cell count. These hypotheses are explicit.'),
 56:('independent re-proof','For bounded finite chain complexes, Euler of the tensor product is the product of the two Euler numbers. Application to spaces retains the Kunneth and support hypotheses; it is not a theorem about arbitrary non-excisive spaces.'),
 57:('targeted proof check','The locally finite RP^n telescope and its double cover are locally compact CW spaces with finite rational cohomology; the base and cover have Euler1 and the fibre Euler2. This verifies all hypotheses of the overly broad ordinary formula and refutes it. The later conical formulation is not refuted.'),
 58:('targeted proof check','Finite-base cellular local-coefficient Euler calculation plus the finite Serre/Leray spectral sequence proves multiplicativity under the corrected numerable-fibration and finiteness hypotheses. The spectral-sequence theorem is an external input.'),
 59:('targeted proof check','Rank-r local systems contribute r-dimensional groups on every finite cell, proving the finite-cell formula. The sign local system on the telescope has zero rational cohomology, refuting the constant-coefficient-finiteness-only version.'),
 62:('targeted proof check','The recursive compact finite-dimensional cone interpretation gives metrizability and local contractibility. The passage to ANR and then finite CW type uses Guilbault–Moran Proposition2.9 and West Corollary5.3; those deep implications are not independently re-proved.'),
 63:('targeted proof check','Finite zero-dimensional compact links and cones on finite graphs verify the local low-dimensional assertions. No general global singular triangulation theorem is claimed.'),
 65:('targeted proof check','Closed/open subtraction at the compactification point gives chi_c(X)=chi(hat X)-1 under the stated finite-support comparison hypotheses.'),
 66:('targeted proof check','Compactness follows by removing an open half-cone from a compactification. Boundary cone charts require the stated link/join closure of the chosen recursive category; this condition is not silently omitted.'),
 67:('independent re-proof','The radial formula is continuous, remains positive, fixes the core and glues to the exterior identity, proving the strong deformation retraction. Program checks at four radii are supplementary.'),
 68:('independent re-proof','Apply excisive core/cone additivity and the radial retraction to obtain chi(X)-chi_c(X)=chi(S_omega). This uses the actual end-cone hypotheses.'),
 69:('targeted proof check','Finite relative-cell induction and compact comparison determine both Euler functions in the stated finite-polyhedral category.'),
 70:('targeted proof check','Conditional modern completion: external finite CW homotopy models determine compactification and core Euler values, and closed/open subtraction determines compact supports. The exact recursive interpretation is essential; this is not a proof of triangulability.'),
 71:('targeted proof check','The finite-cell alternating count is independent of the field. This says nothing about field independence of membership in every broader cohomological finiteness category.'),
 72:('targeted proof check','The order complex of the face poset is the barycentric subdivision of a finite simplicial homotopy model. No minimal-cardinality bound or homeomorphism to the original conical space is established.'),
 80:('independent re-proof','The product K(C2,1) times K(C2,2) has split two-type while the complete normalized cochain calculation gives nonzero H³(C2;C2). This distinguishes the group from its Postnikov class.'),
 83:('targeted proof check','The reduced quadratic-module identities, induced action, normalized section cocycle and nonzero H³(C2;C4) class are checked. Realization by a single-loop two-type uses Baues–Conduche §§4.5,4.7 as an external theorem.'),
 120:('targeted proof check','The Schwarzian identities, Mobius zero and formal ODE quotient calculation are checked. Existence of independent local analytic ODE solutions and the sheaf interpretation use the opened Deligne/Dumas results. No global single-valued solution is asserted.'),
 121:('targeted proof check','Only the universal polynomial pole-support localization lemma is proved by unique factorization. This is not a proof of the manuscript whole analytic operator classification or its redundant-surjectivity claim.'),
 122:('independent re-proof','The Hasse composition identity vanishes in the integral localized polynomial ring, proving the construction before all characteristic specializations. The factor12, square, cube and characteristic2/3 tests are exact; no uniqueness classification follows.')
}
for n,(typ,description) in proofs.items():
    event(f'C-SA04-{n}',typ,description+' Evidence: parts/a/proof_checks.md.')

computed={23,34,36,37,38,39,40,42,43,44,46,47,52,53,54,56,57,59,67,68,80,83,120,122}
for n in sorted(computed):
    claim=next(c for c in claims if c['id']==f'C-SA04-{n}')
    event(claim['id'],'computation or formal certificate',claim['computation']['detail']+
      ' Re-executed successfully. Scope is the displayed exact algebra, finite cochain enumeration, or explicitly supplementary finite example; not analytic convergence or topological realization. Program programs/a_computations.py; stdout outputs/a_computations.txt.')
event('SA04-120','computation or formal certificate','Six displayed budget sums recomputed by exact integers:277,298,316,342,361,354. Program programs/a_computations.py, output outputs/a_computations.txt. No authorship or chronology inferred.')

# Refutation events point from the literal note item to its refined claim.
refutations={
 35:(34,'Unit-element geometric weights give incompatible finite and infinite limits.'),
 37:(36,'The unnormalized Fourier integral has factor2pi; coefficient vanishing survives.'),
 40:(39,'Big-O coefficient reading is contradicted by (z-1)^(-2), alpha=1; little-o is the supported refinement.'),
 42:(40,'The outside Cayley bound at w=-2 reads5/2<=-9/2; change the sign mathematically, leaving the ink undecided.'),
 51:(42,'The moving-point Neumann bound is satisfied by1/lambda at lambda0=1,lambda=3 while the series diverges; use the centre norm.'),
 57:(47,'The literal yw-u target fails for u=1,w=2,gamma=0; the refined yw-w estimate is proved.'),
 90:(58,'Only the earlier constant-coefficient-finiteness-only ordinary multiplicativity is refuted by the telescope double cover. The later conical restriction survives.'),
 91:(59,'Finite constant-coefficient cohomology alone does not force local-system Euler=rank times Euler; the sign local system on the telescope refutes that broad scope.'),
 158:(122,'Hasse square computation gives1/(4t²) where2t is invertible, not the retained1/(2t).')
}
for n,(refined,description) in refutations.items():
    event(f'SA04-{n}',"refuted, with the refined statement's id",f'Refined statement: C-SA04-{refined}. '+description+' This is a mathematical refutation of the literal reading, not a decision about manuscript ink.')

event('RDeligne1968','used and rechecked in this run','BIBLIOGRAPHIC TITLE CHECK ONLY. Independently opened IHES catalogue M/68/28; title Courbes elliptiques: Formulaire d’après J. Tate and date1968. The URL resolves to catalogue metadata, not an extracted primary PDF. See cross_merge_recommendations.md.')
event('RDeligne1975','used and rechecked in this run','BIBLIOGRAPHIC TITLE/PAGE-SEQUENCE CHECK ONLY. Opened William Stein Antwerp image-index page; title Courbes elliptiques: Formulaire (d’après J. Tate), image sequence53–73. Year1975 rests on root’s separate edition evidence, not this index alone.')
event('C-SA04-607','used and rechecked in this run','TEXTUAL ATTRIBUTION CHECK ONLY. The supplied K93-11 scan28 line205 names Marcus Wanderley; the root claim anchor J. Wanderley should be corrected. No independent proof of the orientation theorem is asserted.')
event('C-SA04-217','used and rechecked in this run','EXACT DUPLICATE/HYPOTHESIS COMPARISON ONLY. Pro80:1286–1292 repeats the all-base projective-invariance component already proved in C-SA04-122. Merge claim217 into122, move only entry205 from item217 to153, and retain entry206/item217/claim218 for the distinct ordinary-differential criterion. Agreed with notes_93_b; see cross_merge_recommendations.md.')

# The parent requested a final continuous cote100 Codex witness comparison.
# These events attest actual reading and comparison only, never a new proof.
c100_start=len(events)
event('C-SA04-655','used and rechecked in this run','CONTINUOUS TEXTUAL WITNESS CHECK ONLY. Read every line1–304 of codex/K100-01_transcription.tex, scans2–14, against root claims655–657,677–678,685,687. Re-read the portion hidden by the first combined-display truncation. Source hashes and exact observations are in parts/a/c100_codex_witness_audit.md; all read output is retained in outputs/. No new theorem or proof claimed.')
event('C-SA04-661','used and rechecked in this run','CONTINUOUS TEXTUAL WITNESS CHECK ONLY. Read every line1–336 of codex/K100-02_transcription.tex, scans15–27, against the local-system, descent, GIT and EGA records. Re-read the portion hidden by the first combined-display truncation. See parts/a/c100_codex_witness_audit.md. No proof event inferred from the reading.')
event('C-SA04-665','used and rechecked in this run','CONTINUOUS TEXTUAL WITNESS CHECK ONLY. Read every line1–251 of codex/K100-03_transcription.tex, scans28–40, including all reused GIT sheets, the Illusie letter, algebraization and Baire arguments. Compared root claims664–669,679–686. See parts/a/c100_codex_witness_audit.md.')
event('C-SA04-672','used and rechecked in this run','CONTINUOUS TEXTUAL WITNESS CHECK ONLY. Read every line1–394 of codex/K100-04_transcription.tex, scans41–46 and48–53, including full Neron/BT typescript, strengthening and EGA corrections. Compared root claims670–676,683–685. No scan47 label occurs in the supplied file. See parts/a/c100_codex_witness_audit.md.')
event('C-SA04-686','used and rechecked in this run','LOCATOR CORRECTION ONLY. Both witnesses place the Illusie letter on scan30: Pro2029–2048 and CodexK100-03:40–59. The previous root scan32/Pro2077–2097 locator instead points to GIT definitions. Parent notified; no other-stream file changed.')
event('C-SA04-676','used and rechecked in this run','HYPOTHESIS COMPARISON ONLY. Pro2429–2430,2539–2545 and CodexK100-04:217–220,375–393 remove the initial semiabelian restriction and invoke absence of Ga because the generic fibre admits a Neron model. This is the manuscript rationale; it is not a new proof of the no-Ga theorem.')
event('C-SA04-670','used and rechecked in this run','READING COMPARISON ONLY. Pro2292 says rationnellement projectif, whereas CodexK100-04:28–30 says algebrique et projectif in condition(iv). Preserve both; no physical scan examined. Full variant table is parts/a/c100_witness_readings.tsv.')
event('C-SA04-671','used and rechecked in this run','READING COMPARISON ONLY. Pro2345 uses et between no infinitesimal automorphisms and enough sections; CodexK100-04:98–104 uses ou. Codex153 also leaves projectif|quasi-fini open where Pro2385 favors projectif. No ink decision made; parent notified.')
event('C-SA04-664','used and rechecked in this run','READING COMPARISON ONLY. CodexK100-03:34 reads a une section where Pro2012 is opaque; this explains split effective descent after the algebraically closed residue-field reduction. Mathematical coherence is a reason for scan inspection, not permission to overwrite Pro.')
event('C-SA04-666','used and rechecked in this run','READING COMPARISON ONLY. Pro2107–2109 has ouvert et ferme with a separately cancelled ferme, whereas CodexK100-03:120–126 gives an induced open subscheme and cancelled ferme. The cancellation scope is unresolved; finite unramified polarization pieces are a separate assertion.')
event('C-SA04-673','used and rechecked in this run','SOURCE SUBCLAIM COMPARISON ONLY. CodexK100-04:325–330 and Pro2501 agree that the author claims the Tate theorem for an etale target and for a target whose generic connected part is multiplicative, while acknowledging the characteristic-zero limit of the general theorem then available. This restricted source claim is not a new proof of unrestricted equal-characteristic full faithfulness.')
event('C-SA04-684','used and rechecked in this run','HYPOTHESIS COMPARISON ONLY. CodexK100-04:39–65 and Pro2305–2325 retain local finite presentation in15.6.3/15.6.4, quasi-separatedness in15.6.4, and the additional finite-presentation scope of the universal-openness/projective-limit assertion. No independent proof or new literature fate is claimed by this witness check.')

with (OUT/'c100_witness_events.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events[c100_start:])

event('C-SA04-676','targeted proof check','Independent review of the root-supplied Lie-lattice proof, not an independently originated re-proof. A closed Ga_K subgroup gives nonzero tangent vector v, including in characteristicp. Neron extension of i composed with multiplication by pi^(-n) fixes zero by uniqueness and forces pi^(-n)v into the finite free Lie(G/R) for every n. Its pi-adic intersection is zero, a contradiction. Smooth local finite presentation suffices even when G is not globally finite type; henselianity/completeness are unnecessary. This proves only the no-Ga implication, not the image-factorization or BT extension theorem. Written scope and details: parts/a/proof_checks.md section6. Root supplied the BLR primary citation; A does not claim a separate fresh reading of that source.')

for n,old,new in [(43,130,131),(44,132,133),(45,134,135),(46,136,137)]:
    event(f'C-SA04-{n}','used and rechecked in this run',f'LOCATOR CORRECTION ONLY. Re-read Pro/MPL_93_047-091_transcription.tex:120–145. Previous exact line{old} was a blank separator; the actual statement is at line{new}. The associated item already had the correct locator. Claim serializer corrected; mathematical statement, status and fate unchanged. A navigation audit of all structured exact source references found no other blank exact lines. Program programs/a_locator_audit.py; before/final outputs outputs/a_locator_audit_before.txt and outputs/a_locator_audit.txt. This is a textual reference check, not a mathematical proof.')

with (OUT/'CHECK_EVENTS.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)

# Preserve exact performed operations, but remove external quoted source text.
batches={}
for file in sorted(OUT.glob('search_capture*.json')):
    data=json.loads(file.read_text());clean=[]
    for record in data:
        rawbatch=record['batch'];batch=int(re.search(r'(\d+)',str(rawbatch)).group(1))
        args=record.get('query',record.get('args'))
        sources=[]
        for source in record.get('sources',[]):
            if isinstance(source,dict):
                sources.append(source);continue
            lines=source.splitlines();head='\n'.join(lines[:2])
            ref=re.search(r'【([^】]+)】',head)
            urls=re.findall(r'https?://[^\s)]+',lines[0] if lines else '')
            sources.append({'title_url':(lines[0] if lines else '')[:400],'ref':ref.group(1) if ref else '', 'url':urls[0] if urls else '', 'failure':'Fetch/lookup error' if re.search(r'Internal Error|Failed to fetch|403|404|502|Timeout',head) else None})
        # Older capture12–29 uses results, not sources.
        if not sources:
            for source in record.get('results',[]):
                if isinstance(source,dict):sources.append(source)
                else:
                    head=str(source).splitlines()[:2];joined='\n'.join(head);ref=re.search(r'【([^】]+)】',joined)
                    sources.append({'title_url':head[0][:400] if head else '', 'ref':ref.group(1) if ref else ''})
        entry={'batch':batch,'query':args,'sources':sources}
        clean.append(entry);batches[batch]=entry
    file.write_text(json.dumps(clean,ensure_ascii=False,indent=2)+'\n')

groupmap={}
def assign(numbers,batchids):
    for n in numbers:groupmap[n]=batchids
assign(range(1,16),[1,2,3,6,7,8,10,12,13,14,22,24,25,26,27,28,29,32,33,35])
assign([16,17,18,19],[1,2,3,6,10,12,13,22,24,32,33])
assign([20],[6,7,8,10,13,15,32,33])
assign([21,22],[1,2,3,6,23,24,25,31,34,35])
assign([23,24,27,28],[1,2,3,12,34])
assign([25,26],[6,23,24,25,30,31,35])
assign(range(29,34),[2,3,6,7,8,17,24,26,27,28,29,35])
groupmap[29]+=[44,45,46,47]
assign([34,35,47],[7,10,13,14,16,30,35,38,39,40,41,42])
assign(range(36,42),[7,20,21,22,38,39,40,41,42])
assign(range(42,47),[7,20,21,22,31,34,35,38,39,40,41,42])
assign([48,49],[1,2,7,10,12,13,32,33,34])
assign(range(50,73),[4,9,15,16,17,23,30,31,34,35,36,37])
assign(range(80,85),[5,8,9,12,14,24,25,30,31,33,34])
assign(range(120,124),[4,8,9,12,15,20,21,23])
logs=[]
for batch,record in sorted(batches.items()):
    claimids=[c['id'] for c in claims if batch in groupmap[int(c['id'].rsplit('-',1)[1])]]
    logs.append(dict(search_id=f'A-SEARCH-{batch:02d}',date=DATE,claim_ids='; '.join(claimids),operation='actual saved web operation',query=json.dumps(record['query'],ensure_ascii=False),opened_sources=json.dumps(record['sources'],ensure_ascii=False),exact_locator='Reference-specific locators are in reference_checks.tsv and the per-claim rows below.',result='The retrieved pages/metadata were read and used only to the extent specified in the claim fate and reference-result ledger.',limitations='Queries include discovery results, not all opened or authoritative. Search hits alone are not proof. For batches18/19 the request arguments were not preserved; returned source identifiers remain. Fetch failures are not evidence that a work does not exist.'))
for claim in claims:
    n=int(claim['id'].rsplit('-',1)[1]);selected=groupmap[n]
    assert all(b in batches for b in selected),(n,selected,set(batches))
    logs.append(dict(search_id='A-FATE-'+str(n),date=DATE,claim_ids=claim['id'],operation='claim-level fate assessment from performed searches',query='Relevant actual search/reading batches: '+', '.join(f'A-SEARCH-{b:02d}' for b in selected),opened_sources='; '.join(k+' '+refmap[k]['url'] for k in claim['refs']),exact_locator='; '.join(k+': '+refmap[k]['locator'] for k in claim['refs']),result=claim['fate'],limitations=claim['present_status']+' Confidence: '+claim['confidence']+'. Claims lacking an exact match are not thereby declared globally open.'))
with (OUT/'search_log.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['search_id','date','claim_ids','operation','query','opened_sources','exact_locator','result','limitations'],delimiter='\t');w.writeheader();w.writerows(logs)
print(json.dumps({'check_events':len(events),'item_comparisons':len(items),'claim_fates':len(claims),'reference_checks':len(references),'actual_search_batches':len(batches),'search_log_rows':len(logs),'proof_events':len(proofs),'computed_claim_events':len(computed)},indent=2))
