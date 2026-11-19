"""Serialize audit records from authored assessments and actual tool receipts.

This program makes no source-entry verdict, theorem identification or claim
classification. The semantic assessments below were made by reading the sources.
Long external text remains temporary; deliverables retain reproducible receipts.
"""
from pathlib import Path
import csv, hashlib, json, re, shutil
P=Path(__file__).resolve().parents[1]
DATE='2026-11-19'
WHO='GPT-6 Astra Pro; effort not exposed; SA14-20261119; picard_lefschetz'
C=json.loads((P/'claims.json').read_text())
I=json.loads((P/'items.json').read_text())
M=json.loads((P/'problems.json').read_text())

def tsv(name, rows, fields):
    with (P/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)

# Manually assessed thematic searches. A list is a navigation map of actual
# calls, never an automatic subject classification or an inferred verdict.
GROUPS={
'01':([35,36], 'Classical divisor conventions', 'Opened modern Weil-divisor conventions and EGA material. The fragment is reused print; its physical edition is not identified. No original-priority assertion.'),
'02':([7,8,9,15,16,21,22,23,24,56,57], 'Henselian approximation and punctured Picard', 'Artin finite-order approximation and Elkik III.1 p.573 are different exact results. Elkik gives the punctured Picard isomorphism; Artin plus the checked ample-locus lemmas gives conditional projectivity descent. The uncertain R¹-support target remains unidentified. MO searches were discovery only.'),
'03':([1,3,4,7,9,15,19,25,26,28,31,32,34,35,37,38,39,40,45,46,47,51,52,53,58,59], 'Picard, numerical quotient and finiteness', 'Opened FGA236 and its addendum, Kleiman2005, and the actual SGA6 XII/XIII scan. Matched proper-field affine pullback, relative generic quasi-affine pullback, multiplication finite type, tau finiteness and NS bounds. FGA2.10(i) concerns sigma, not tau; FGA2.8 includes conjectures. Broad scheme quotient/correspondence hypotheses remain bounded identification remainders. Initial SGA6 TOC copy was not accepted as theorem evidence.'),
'04':([1,2,3,4,5,6,9,16,20,21,51,52,53,59], 'Igusa, Hodge dimensions and deformation', 'Opened FGA2.6/2.9 and Oda4.9/5.11/5.12. The inversion example is finite-flat but nonsmooth; it is not Mumford’s nonflat example. Oda’s absolute stable-subspace result does not establish the unspecified relative lifting constructions.'),
'05':([1,2,3,4,6], 'Neron-Severi specialization', 'Opened Maulik–Poonen Proposition3.6 and Example3.12. Genuine p-primary nonsaturation established; their CM construction is not the missing manuscript finite-subgroup family. First arXiv and publication dates separately checked.'),
'06':([4,6,9,20,21], 'Tate modules and p-primary groups', 'Opened Oda as group-scheme comparison context. The abstract-group lattice structure, variance and rationalization are independently proved in P8–P10; no false attribution of these elementary facts to Oda as their origin.'),
'07':([19,20,21,24,25,27,39,40], 'Roos and derived limits', 'Opened Laudal§1.1/Cor1.3.2 and followed the Roos1961/1962 bibliography. Original Roos bodies not accessed. Exact detached L_k bound cannot be identified; the two spectral-sequence constructions are checked under explicit module/index-category hypotheses.'),
'08':([2,3,6,9,10], 'Pinching, nonprojective schemes and generalized Jacobians', 'Opened Ferrand2.2,5.4,6.2–6.3,7.1. Matched the pushout and affine-orbit framework, while separating existence from the global-functions calculation. Units, normalization and nodal controls independently worked out; external arithmetic/pro-tower leads not inferred.'),
'09':([1,3,4,10,11,13,15,16,48,49,50], 'Formal Lefschetz, Picard and covers', 'Opened SGA2 IX–XIII exact theorem loci and Raynaud1974. Derived full faithfulness/cover consequences retain depth and existence assumptions. Suzuki proves maximal pro-nilpotent finite generation only; not the full local fundamental-group conjecture.'),
'10':([19,20,36], 'Associated primes and depth', 'Opened Stacks0312/0FCC and Raynaud’s exact local depth hypotheses. The closure of an associated point, not merely the point, must miss the divisor in the vanishing argument.'),
'11':([1,12,13,14,15,48,49,50], 'Connectedness and local fundamental groups', 'Opened SGA2 XIII2.1 including its following converse; the finite-hyperplane argument agrees with the source. Literal ordinary generic-fibre connectedness is refuted by P1. Opened Suzuki Th1.2 and its Conj1.1. Recent bounded searches did not establish a later full-pi1 theorem or certify2026 openness; zbMATH access/search gaps recorded.'),
'12':([1,3,4,7,9,12,15,16], 'Local Hom and formal algebraization', 'Opened Raynaud I0/I1.1–1.5 and SGA2 IX2.2. Exact depth-controlled Hom comparison checked. Unrestricted Serre-quotient fullness is refuted; undefined a,b,cprime,T1 essential-image clauses remain unidentified.'),
'13':([7,8,12,15,16], 'Permanence and proper support', 'Searched SGA2/Raynaud, arXiv and MathOverflow for the precise projective-flat permanence formulation. Opened relevant comparison/existence theorems; P21 supplies only a conditional perfect-complex route. No exact broad permanence theorem is silently credited.'),
'14':([1,3,4,10,11,13], 'Duality and graded coherent cohomology', 'Opened SGA2 XII1,3.1–3.2,5.2–5.6. Reused formal-existence sheets match exactly with their hypotheses. Positive graded finite generation, negative twists and the degree0 endpoint are kept separate; P3/P4 refute the literal conflations.'),
'15':([8,12,15,17,18,23,24,36,56,57], 'Cones, line bundles and projectivity', 'Downloaded and read EGAII8.7.2–8.8.6, including visual8.7.5/8.8.6; opened Traverso3.6 and Stacks0D2S/0B44. Projective cone and affine total space are distinct. Seminormality gives a sufficient homotopy-invariance setting; undefined primes/tildes cannot be repaired from the conclusion.'),
'16':([3,4,10], 'Parafactoriality', 'Opened SGA2 XI3.4–3.5/3.13. The categorical criterion includes depth≥2. A DVR refutes the unrestricted factorial-to-parafactorial categorical assertion although both Picard groups vanish.'),
'17':([19,35,36,41,42,43,44,54,55,57], 'Reused scalar, field and determinant algebra', 'Opened Stacks p-basis, relative-constant and invertible-module statements. Name searches for Zariski mainly returned the different finite-type-field lemma. P25 verifies the actual normalized-coefficient relative-constants statement; the exact Bourbaki edition is unlocated. Determinant/rank calculations were redone symbolically.'),
'18':([19,25,26,28,29,30,51,52], 'Group monomorphisms and rank variation', 'Opened SGA3 II VIII7.2 and X8.7. The characteristic-zero monomorphism statement is matched with flatness/presentation hypotheses. X8.7 gives the smooth-group variation case; the merely flat extension is called probable, so no general modern settlement is claimed.'),
'19':([25,26,27,28,31,32,33,34,39,40,41,42,43,44], 'Brauer–Witt and the detached R_p page', 'Opened Brauer1951§2.6 and Theorem p.250; Fontaine1971§§6–8. Decomposed is not ground-field split. Fontaine gives the exact R_p definition/result, but the missing manuscript definition is not restored. Serre1960 metadata was found but body inaccessible; physical leaf identification remains unverified.')
}

TEMP=Path('/tmp/SA14_PL_web_outputs');TEMP.mkdir(exist_ok=True)
raws={}
for f in sorted((P/'outputs').glob('web_*.json')):
    n=int(re.search(r'web_(\d+)',f.name).group(1))
    saved=TEMP/f.name
    d=json.loads((saved if saved.exists() else f).read_text())
    raws[n]=(f,d)

def textparts(x):
    if isinstance(x,dict):
        if x.get('type')=='text' and isinstance(x.get('text'),str):yield x['text']
        else:
            for v in x.values():yield from textparts(v)
    elif isinstance(x,list):
        for v in x:yield from textparts(v)

def refs_of(d):
    out=[]
    for s in textparts(d.get('result',{})):
        for m in re.finditer(r'^([^\n]{0,500})\((https?://[^\n]+?)\)\s*\n【([^】]+)】',s,re.M):
            q={'title':m.group(1).strip(),'url':m.group(2),'ref_id':m.group(3)}
            if q not in out:out.append(q)
    return out

search=[]
for k,(ns,subject,outcome) in GROUPS.items():
    sid='PL-S'+k
    cs=[x['id'] for x in C if sid in x['search_events']]
    queries=[]; urls=[]; engines=[]
    for n in ns:
        if n not in raws:continue
        q=raws[n][1]['request']
        for engine in ['system1_search_query','system2_search_query']:
            for query in q.get(engine,[]) or []:
                if query['q'] not in queries:queries.append(query['q'])
                if engine not in engines:engines.append(engine)
        for r in refs_of(raws[n][1]):
            if r['url'] not in urls:urls.append(r['url'])
    search.append(dict(event_id=sid,date=DATE,platform='; '.join(engines)+'; primary-source open/find/click as recorded',subject=subject,queries=json.dumps(queries,ensure_ascii=False),claims=';'.join(cs),opened_or_returned_sources=json.dumps(urls,ensure_ascii=False),result=outcome,limits='Search hits are discovery; verified exact endpoints are those named in references.bib and the authored claim fates. No claim of exhaustive2026 absence.',raw_records=';'.join(f'PL-W{n:03d}' for n in ns)))

receipts=[]
for n,(f,d) in raws.items():
    q=d['request'];rs=refs_of(d)
    groups=['PL-S'+k for k,(ns,_,_) in GROUPS.items() if n in ns]
    cs=sorted({x['id'] for x in C if any(g in x['search_events'] for g in groups)})
    payload=json.dumps(d,ensure_ascii=False,sort_keys=True).encode()
    digest=hashlib.sha256(payload).hexdigest()
    search.append(dict(event_id=f'PL-W{n:03d}',date=DATE,platform='web search service',subject='Actual web operation; semantic assessment in '+','.join(groups),queries=json.dumps(q,ensure_ascii=False),claims=';'.join(cs),opened_or_returned_sources=json.dumps(rs,ensure_ascii=False),result='Actual request/response received. Returned sources include unsuccessful/discovery hits; this row does not assert every returned source was read or verified.',limits='Exact checked statements and failed-match limits are in the PL-S group rows and references.bib.',raw_records=f'outputs/{f.name}'))
    saved=TEMP/f.name
    if not saved.exists():shutil.copy2(f,saved)
    receipt={'request':q,'response_sha256_canonical_json':digest,'returned_sources':rs,'semantic_search_events':groups,'temporary_raw_response':str(saved),'note':'Receipt only. Long external text/images are deliberately not redistributed; actual inspected statements are described in the authored registers and bibliography.'}
    f.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    receipts.append(dict(source=f'PL-W{n:03d}',url=';'.join(r['url'] for r in rs),sha256=digest,bytes=len(payload),temporary_path=str(saved),inspected_loci='Actual operation and returned-reference receipt; read statements separately logged',verification='request/response receipt, not an assertion that every returned hit was used'))
tsv('search_log.tsv',search,['event_id','date','platform','subject','queries','claims','opened_or_returned_sources','result','limits','raw_records'])

pdfs=[
('Grothendieck1961EGAII','/tmp/SA14_EGA_II.pdf','https://www.numdam.org/item/PMIHES_1961__8__5_0.pdf','4.5.1–5;4.6.8–12;8.7.2–8.8.6; images originalpp176,181'),
('Grothendieck1962FGA236','/tmp/SA14_FGA236.pdf','https://www.numdam.org/article/SB_1961-1962__7__221_0.pdf','§§1–4 as logged; images originalpp222–223,234–235'),
('RaynaudKleiman1971SGA6XII;Kleiman1971SGA6XIII','/tmp/SA14_SGA6_MSRI.pdf','https://library.slmath.org/books/sga/sga/pdf/sga6.pdf','Images printedpp595–598,635–636,647–648,650–652; physicalPDFpages598–601,638–639,650–651,653–655')]
for key,local,url,loci in pdfs:
    f=Path(local); b=f.read_bytes()
    receipts.append(dict(source=key,url=url,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),temporary_path=local,inspected_loci=loci,verification='Primary PDF downloaded; specified passages actually read. Entire PDF not redistributed.'))
tsv('source_receipts.tsv',receipts,['source','url','sha256','bytes','temporary_path','inspected_loci','verification'])

events=[]
def e(s,t,out):events.append(dict(statement_id=s,date=DATE,who=WHO,type=t,outcome=out))
for x in I:
    e(x['id'],'used and rechecked in this run','Text concordance, not mathematical proof. Actual note entries and transcription passages compared: '+ '; '.join(x['lines'])+'. '+x['check']+': '+x['check_reason'])
for x in C:
    e(x['id'],'used and rechecked in this run','Text concordance, not mathematical proof. Diplomatic passage read at '+'; '.join(x['lines'])+'. Page status: '+x['status_on_pages']+'. Literature concordance/limits: '+x['fate']+' Search events: '+','.join(x['search_events']))
for x in M:
    e(x['id'],'used and rechecked in this run','Question and exact state-of-art comparison, not mathematical proof. '+x['state_of_art']+' Historical limit: '+x['why_open'])

# Actual mathematical checks, with the scope of each proof rather than a blanket
# certification of every broader claim that cites it.
PROOFS=[
('P1',[273],'refuted, with the refined statement\'s id','Ordinary-fibre specialization refuted; replacement must specify geometric connectedness. All literal hypotheses checked in P1; h≥0 variant included.'),
('P2',[292],'refuted, with the refined statement\'s id','Faithfulness refuted by 1 and1+t on a DVR despite H¹/H² vanishing; Picard classes and line-bundle categories separated.'),
('P3',[311,313,315],'targeted proof check','Skyscraper controls refute the stated degree0 equivalence/vacuous-boundary conclusion and distinguish the twist signs; they do not refute correctly ranged positive-degree results.'),
('P4',[310],'refuted, with the refined statement\'s id','Localization exactness gives injectivity of alpha, not its surjectivity, from the indicated restriction-map surjectivity.'),
('P5',[301],'independent re-proof','Hom-depth bound proved from a finite presentation and a regular sequence; min(2,depth target) scope retained.'),
('P6',[302,314],'targeted proof check','Precise Hom comparison deduced from opened Raynaud hypotheses, with closure-missing depth estimate; not a re-proof of Raynaud’s entire theorem.'),
('P7',[306],'refuted, with the refined statement\'s id','Unrestricted quotient-category fullness refuted by the explicit unbounded-pole formal series; the clean depth-controlled category is not refuted.'),
('P8',[221],'independent re-proof','Smith-normal-form splitting criterion checked for divisible finite-corank p-groups; the testing finite group must be nonzero.'),
('P9',[218,219,220],'independent re-proof','Abstract p-group finite-cotype structure, variance and Q_p rationalization checked through finitely generated Z_p modules.'),
('P10',[216,217],'targeted proof check','Conditional finite-subgroup descent/divisibility mechanism checked. Literal pF=G for nonzero G⊂X[p] fails; no missing family constructed.'),
('P11',[213,214,244],'targeted proof check','Inversion/translation control and its tangent dimensions checked. A[2] is finite locally free: this control is flat and cannot establish Mumford nonflatness.'),
('P12',[228,229],'targeted proof check','Inverted-axis gluing forces constant restrictions of global functions and excludes quasi-affineness; finite-quotient existence is explicitly not inferred.'),
('P13',[234,236],'independent re-proof','Two projective planes glued along an elliptic curve with independent restricted hyperplane classes give Picard-trivial pushout, subject to the stated existing-pushout hypotheses.'),
('P14',[237,325,328],'independent re-proof','Units and component rescaling compute the pinching Picard kernel and nodal torus; additive H¹(O) is not substituted for multiplicative H¹(O*).'),
('P15',[327,328],'independent re-proof','Normalization exact sequence yields delta genus formula and nodal graph rank.'),
('P16',[326],'refuted, with the refined statement\'s id','DVR refutes unrestricted categorical factorial⇒parafactorial; the dimensional repair and exact depth/Pic criterion are stated.'),
('P17',[324,331],'targeted proof check','Grading contraction and line-bundle descent deduced using opened Traverso homotopy invariance under seminormality. No proof for all singular cones asserted.'),
('P18',[329,330],'targeted proof check','Projective-bundle Picard decomposition and conditional cone contraction calculation checked; direct-image and section hypotheses retained.'),
('P19',[224,319,320],'independent re-proof','Diangle composition, rank criterion and Jacobi complementary-minor identity rederived; symbolic residual recorded.'),
('P20',[280,281,282,283,286,287,288,289],'targeted proof check','Low-degree Lefschetz/generator argument and finite algebra/cover consequences checked with extension and Hom hypotheses; no blanket category equivalence from cohomology alone.'),
('P21',[293,294,295,296],'targeted proof check','Conditional perfect-complex/proper-support route examined. This is a mechanism and a missing-hypothesis audit, not a proof of the broad permanence conjecture.'),
('P22',[210,211,212,249],'independent re-proof','Rigidification inverses checked at sheaf level. Missing NS factor refutes only the transient full-Pic replacement; later source correction is preserved.'),
('P23',[222,291],'independent re-proof','Square-zero unit sequence gives H² obstruction, H¹ torsor and H⁰ automorphisms; cup-product identification explained.'),
('P24',[225,227],'targeted proof check','Two derived-limit/Ext spectral sequences checked under the stated diagram-module hypotheses; detached Roos bound remains unidentified.'),
('P25',[230,231,232,235],'independent re-proof','Actual relative-constants coefficient lemma proved by normalized finite orbits; regular-extension and p-basis algebra checked separately.'),
('P26',[255],'independent re-proof','Positive-dimensional abelian variety over an infinite characteristic-p field yields infinitely many p-torsion dual-number sections despite a finite torsion scheme.'),
('P27',[260,318],'independent re-proof','Scalar extension and fractional-invertible-ideal/rank-one-projective equivalence verified.'),
('P28',[284],'independent re-proof','Associated-point contradiction requires the closure to miss the divisor, and is proved with that condition.'),
('P29',[300,303],'targeted proof check','Exact completion/Serre kernel and eventual t-power-torsion removal checked under noetherian hypotheses.'),
('P30',[309,312,314,316,317],'targeted proof check','Duality indices, localization and lim¹/degree0 endpoints checked with the exact hypotheses; published comparison theorem is not re-proved wholesale.'),
('P31',[321,322],'targeted proof check','Character induction to decomposability checked conditional on the opened Brauer theorem; no independent proof of Brauer–Witt or restoration of missing R_p definition claimed.'),
('P32',[202,332],'targeted proof check','Projectivity follows from finite-order approximation of a completed ample line bundle and the opened ample-locus theorem; no arbitrary fpqc projectivity-descent claim.')]
for proof,ids,typ,out in PROOFS:
    for n in ids:e(f'C-SA14-{n}',typ,f'Refined checked statement {proof}; outputs/proof_checks.md#{proof}. '+out)

e('C-SA14-206',"refuted, with the refined statement's id",'Refined statement P22-cosets in outputs/proof_checks.md: a nonidentity quotient coset is disjoint from the kernel; corrected ambient is the full group.')
e('C-SA14-207','targeted proof check','P22-cosets in outputs/proof_checks.md proves the closed-kernel diagonal criterion under an existing represented fppf quotient. Scheme existence and unramifiedness are not inferred.')

CALCS={
'split_special_fibre':[273], 'automorphism_faithfulness':[292], 'skyscraper_twists':[311,313,315],
'diangles':[224], 'tate_lattice_tests':[218,219,221], 'tate_isogeny_test':[216,217,220],
'p_subgroup_equality':[216], 'igusa_tangent_control':[213,214], 'glued_curve_restrictions':[228],
'elliptic_gluing_pic':[234,236], 'nodal_graph_genus':[327,328], 'jacobi_cofactor':[320],
'rank_minor_checks':[319], 'formal_pole_growth':[306], 'localization_direction':[310], 'cutting_dimension':[272,275]}
calc=json.loads((P/'outputs/calculations.json').read_text())
for name,ids in CALCS.items():
    assert name in calc,name
    for n in ids:e(f'C-SA14-{n}','computation or formal certificate','Actual saved exact computation/control: scripts/calculations.py, outputs/calculations.json#'+name+'. Scope is given in the authored claim and proof check; finite tests do not by themselves prove the general theorem.')

bib=(P/'references.bib').read_text()
for m in re.finditer(r'@\w+\{([^,]+),(.*?)(?=\n@|\Z)',bib,re.S):
    key,body=m.groups()
    a=re.search(r'annote\s*=\s*\{(.*)\}\s*\n\}',body,re.S)
    ann=a.group(1).strip() if a else 'See checked bibliography metadata.'
    if 'note = {unverified}' in body:
        e(key,'carried as background without fault found','Unverified backward/source-identification lead only; no theorem body or exact result certified. '+ann)
    else:e(key,'used and rechecked in this run','Text concordance, not mathematical proof. '+ann)
tsv('CHECK_EVENTS.tsv',events,['statement_id','date','who','type','outcome'])
report={'search_rows':len(search),'source_receipts':len(receipts),'check_events':len(events),'proof_checks':len(PROOFS),'calculation_sections':len(CALCS)}
(P/'outputs/audit_build_report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
