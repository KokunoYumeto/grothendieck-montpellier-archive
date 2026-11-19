"""Manual mathematical classifications, applied to the already authored records.
The dictionaries below are research decisions, not keyword-generated verdicts.
Run after author_3.py, author_4.py, author_5.py and computations.py.
"""
from pathlib import Path
import json,csv,datetime,hashlib,re
ROOT=Path(__file__).resolve().parents[1]
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
claims=sum((json.loads((ROOT/f'claims_{n}.json').read_text()) for n in (3,4,5)),[])
by={x['id']:x for x in claims}
groups={
 'custom':('S03;S06;S07;S09;S10','Malgoire2002;CSG2026','Search found archival description, historical discussion and the recent restricted results listed separately; no exact published theorem for this version of the axioms was identified.'),
 'betweenness':('S01;S03;HUA;COUR','Courcelle2020;Bankston2013;Hua2026','Cut/betweenness literature was compared with the density, comparability and bidirectedness hypotheses; the precise later match is recorded individually.'),
 'elementary':('S01;COUR;BK','Birkhoff1948;Courcelle2020','The order-theoretic special case is elementary; no claim of historical priority is made.'),
 'intervals':('S04;S06;S08;BK','Birkhoff1948;Hua2026','Linear-order interval algebra is classical; no exact external treatment of the manuscript’s non-total moderated-interval package was located. Hua2026 §78 expressly leaves that package outside its scope.'),
 'topology':('S01;S04;S06;S07;BK','Birkhoff1948;Stong1966','General order-topology references do not identify this particular strict-interval topology on abstract tronçons. No external resolution of the stated tronçon questions was located.'),
 'partial_boolean':('S02;S04;S08;S09;KS','KochenSpecker1967','Partial Boolean operations predate the manuscript; the additional moderated closure/compatibility axioms require separate comparison. No exact external result for the full package was located.'),
 'boolean':('S02;BK;KS','Birkhoff1948;KochenSpecker1967','Boolean algebra/ring identities and finite generated-algebra structure are standard pre-1986 material; the stated boundary identification is assessed separately.'),
 'stratification':('S01;S05;S07;WWY;ESQ','WaasWoolfYokura2026;Esquisse1984','Modern stratification results address quotient Alexandrov spaces under explicit local-finiteness/frontier hypotheses; they do not settle every manuscript refinement or completion construction.'),
 'poset':('S01;S06;S10;BK;ST','Birkhoff1948;Stong1966','Standard poset/finite-space results supply context. No exact published result for the stated multistratum or two-order formulation was found in the recorded search.'),
 'lattice':('S01;S02;S10;BK','Birkhoff1948','Classical representation theory distinguishes join-primality from ordinary irreducibility. The specific manuscript assertion and later internal repair are recorded separately.'),
 'orthogonality':('S02;S10;BK;HUA','Birkhoff1948;Hua2026','Polarity closure is classical. Booleanity requires an additional condition; the exact later counterexample is separated from the general closure construction.'),
 'subdivision':('S03;S06;S07;S09;S10;ESQ','Esquisse1984;Malgoire2002','No exact later theorem for this changing abstract subdivision calculus was located. General tame-stratification ideas are contextual links, not proofs of the displayed axioms.'),
 'alexandrov':('S01;S04;S05;S06;ST;WWY','Alexandroff1937;Birkhoff1948;Stong1966;WaasWoolfYokura2026','The order/topology correspondence is classical; this manuscript’s admissible-family presentation and its refinements have been compared individually. Alexandroff metadata was opened but the full text could not be retrieved reliably.'),
 'stone':('S02;BK','Birkhoff1948','Classical Boolean representation and regular-open algebra are the exact standard ingredients.'),
 'extension_topology':('S04;S05;S08;S10;BORG','Borges1967','Topology-extension literature was searched; Borges studies simple extensions and related restrictions, not this exact arbitrary prescribed finer topology on a closed subspace. No exact matching external theorem was located.'),
 'quillen':('S02;S05;QUI','Quillen1973','Theorem A addresses contractible comma categories, hence principal-ideal inverse images for posets. It does not by itself identify the manuscript’s undefined universal homotopically-proper package.')}
for x in claims:
 q,refs,fate=groups[x.pop('search_group')]
 x['class']='D';x['fate']=fate+' Search record: '+q+'. D means no exact match located in this documented search, not proof of nondevelopment.'
 x['refs']=refs.split(';');x['fate_date']='Searched through 2026-11-19; no matching circulation/publication date established.'
 x['present_status']='As of 2026-11-19: '+x['present_status']
 x['confidence']='medium'
def setf(ch,nums,cl,fate,refs,date,confidence='high'):
 for n in nums:
  x=by[f'C-SA21-{ch}-{n:03}'];x['class']=cl;x['fate']=fate;x['refs']=refs;x['fate_date']=date;x['confidence']=confidence
pre='Known before June 1986; cited edition/publication dates supplied in references.bib. No claim of first discovery.'
setf(3,[5,7],'B','Exact later match: Hua2026 §78, pp.366–368. Independently checked against the manuscript hypotheses; source dependence and verification limits are recorded in source_checks.md. Courcelle2020 Theorem 3.5 is a related finite/countable reconstruction criterion, not an arbitrary-cardinality substitute.',['Hua2026','Courcelle2020'],'Hua preprint November 2026, version 2; day of first circulation unverified. Courcelle first arXiv circulation 2020-04-21; journal 2020.')
setf(3,[2],'C','The ordered-tronçon reconstruction part has an exact later match (C-SA21-3-005/007). The general-network anticipation and converse axiom characterization remain outside that result. Search: S03,S06,COUR,HUA.',['Hua2026','Courcelle2020'],'Partial result: November 2026; no date identified for the broader anticipation.')
setf(3,[6],'E','Elementary transitivity and orientation lemma; independently re-proved below. Compare the standard strict-betweenness convention in Courcelle2020 §2.',['Birkhoff1948','Courcelle2020'],pre)
setf(3,[22,27],'E','Standard finite Boolean computation; source check BK-3/KS-1. The refined statement 027 is ours, not manuscript text.',['Birkhoff1948','KochenSpecker1967'],pre)
setf(3,[21,23],'C','Partial Boolean algebra is pre-1986 (KS-1). The additional closure axioms and their relativization are the manuscript’s distinct package; no exact external continuation was found (S04,S08,S09).',['KochenSpecker1967'],'Partial Boolean background: 1967 issue (publisher DOI labels 1968); closure-package fate not identified through 2026-11-19.')
setf(4,[33],'E','Classical polarity/Galois-closure construction; source check BK-1.',['Birkhoff1948'],pre)
setf(4,[34],'B','Exact negative answer: Hua2026 §79, pp.369–370. This run also checks the figure hypotheses omitted from that Lean encoding; see seven-element certificate and source_checks.md.',['Hua2026','Birkhoff1948'],'Preprint November 2026, version 2; first-circulation day unverified.')
setf(4,[35],'D','This run’s independent five-cycle certificate is a new check, not a literature result. Hua2026 §79 separately supplies the smaller later counterexample; no historical priority asserted. Search: S02,S10,HUA.',['Hua2026'],'Current-run certificate 2026-11-19; matching published negative answer November 2026.')
setf(4,[27,29,31],'E','Standard lower-set/component construction once the stated representation hypotheses hold; source checks BK-2 and ST-1. Current-run repair 027 is separately attributed.',['Birkhoff1948','Stong1966'],pre)
setf(4,[1,2],'C','The explicit locally finite frontier/partition consequences have a modern counterpart in WaasWoolfYokura2026 §3 (Proposition 3.3, Corollary 3.4, Proposition 3.9). Its quotient-space theorem does not establish the manuscript’s full figure calculus.',['WaasWoolfYokura2026'],'First arXiv circulation 2024-07-25; v2 2025-07-08; journal 2026.')
setf(5,[3,4,5,12,14,17,22],'E','Classical preorder/Alexandrov operations, translated here to admissible-family notation; source checks ST-1, AX-1 and WWY-1. The translation is rechecked in proof_checks.md.',['Birkhoff1948','Stong1966','Alexandroff1937','WaasWoolfYokura2026'],pre)
setf(5,[7],'E','Bounded unions and principal lower sets give the standard join-prime representation; source check BK-2 and the explicit manuscript model.',['Birkhoff1948'],pre)
setf(5,[9,10],'E','Classical set polarity/Stone/regular-open facts; source checks BK-1 and BK-4. The suggested enlargement of the figure model remains a construction proposal.',['Birkhoff1948'],pre)
setf(5,[29],'C','Quillen1973 Theorem A (printed p.93 in the opened copy; §1) matches the principal-lower-ideal criterion. The stronger universal claim requires a precise homotopically-proper definition and base-change category; no exact external identification was found.',['Quillen1973'],'Theorem A published 1973, before these pages; manuscript universal formulation not identified through 2026-11-19.')
# Corrections are versioned, never silently applied to the transcription.
by['C-SA21-3-015']['present_status']='As of 2026-11-19: false for abstract tronçons under the displayed axioms. Q×{0,1}, ordered by equality or strictly increasing first coordinate, has indistinguishable twin points and is not T0 or sober. R², ordered by equality or strict increase in both coordinates, has Euclidean canonical topology and is Hausdorff while the order is not total. All tronçon conditions, including iterated strict cones, are checked in proof_checks.md. No external exact fate was found; these are current-run refutations.'
by['C-SA21-3-015']['confidence']='high'
by['C-SA21-3-005']['statement']=by['C-SA21-3-005']['statement'].replace('comparability itself is recovered by ∃c B(a,c,b)','for distinct a,b, comparability is recovered by ∃c B(a,c,b)')
by['C-SA21-5-003']['present_status']=by['C-SA21-5-003']['present_status'].replace('a “finite” core','a “finite” redundant additional family Ψ')
by['C-SA21-3-001']['status_on_pages']='proof sketched; false from the stated bare compatibility data (current-run counterexample)'
by['C-SA21-3-027']['status_on_pages']='not on the pages: refinement supplied by this run'
by['C-SA21-4-012']['status_on_pages']='not on the pages: refinement supplied by this run'
by['C-SA21-4-012']['present_status']='As of 2026-11-19: the well-foundedness/coverage repair is independently checked here; V scans2–4 supplies the author’s explicit later membership-coverage condition β. Neither repair is retroactively attributed to IV scan27.'
by['C-SA21-4-027']['status_on_pages']='not on these pages: refinement supplied by this run; later manuscript strengthening in VI'
by['C-SA21-4-035']['status_on_pages']='not on the pages: countermodel supplied by this run'
by['C-SA21-4-011']['present_status']+=' Corrected explicitly in V scans2–4 (C-SA21-5-001), with a forward reference to VIII manuscript37.'
by['C-SA21-4-011']['status_on_pages']='stated without proof; corrected by himself later in V scans2–4'
by['C-SA21-4-026']['present_status']+=' VI scan12, J156-6-02 lines77–88, strengthens strict irreducibility to X≤Sup_i F_i ⇒ X≤F_i for some i. This is the exact missing join-prime condition, not ordinary complete join-irreducibility.'
by['C-SA21-4-035']['present_status']='As of 2026-11-19: executed exhaustive certificate confirms 10 multistrata, 16 compatible lower-ideal figures and 12 biorthogonally closed supports, with a distributivity failure. The independent seven-element comparison model has 11 figures and six closed supports. All finite-poset, compatibility, hereditary, C1/C2/C3 and connectedness tests pass. Identity-subdivision axioms are checked manually, explicitly not represented as executed Lean verification.'
by['C-SA21-3-004']['computation']='Exact gap enumeration and symbolic proof in proof_checks.md; code/computations.py outputs gap_counts. The finite list illustrates the symbolic n+1 count and is not an infinite proof.'
by['C-SA21-3-007']['computation']='Symbolic strict-gap calculation in proof_checks.md; rational witnesses in outputs/computations.json: pair_cut_middle_on_rationals.'
by['C-SA21-3-012']['computation']='Exact rational gap witness in outputs/computations.json; the no-minimum proof is independent and symbolic in proof_checks.md.'
by['C-SA21-3-026']['computation']='outputs/computations.json: one_interval_boolean_atoms.'
for x in claims:
 x['statement']=x['statement'].replace('L\\T','L minus T').replace('X\\Y','X minus Y')
 # Every fate search is linked to a concrete group, even where the result is negative.
 if x['class']=='D' and not ('Search' in x['fate'] or 'search' in x['fate']):raise ValueError(x['id'])
(ROOT/'claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
# Coverage is mechanical accounting only; full-reading decisions precede this script.
base=ROOT.parents[2];rows=[]
for ch,count in [(3,5),(4,11),(5,6)]:
 for k in range(1,count+1):
  stem=f'J156-{ch}-{k:02}'
  p=base/'sources/texts/codex'/f'{stem}_transcription.tex';n=base/'sources/notes/codex'/f'{stem}_notes.md'
  t=p.read_text();nt=n.read_text();ss=re.findall(r'\\scanpage\{([^}]+)\}',t)
  rows.append([stem,'complete transcript and complete note read',','.join(ss),len(t.splitlines()),len(nt.splitlines()),hashlib.sha256(p.read_bytes()).hexdigest(),hashlib.sha256(n.read_bytes()).hexdigest(),'outputs/'+stem+'_read.txt','Manual mathematical records; no verdict inferred from title/keyword extraction'])
with (ROOT/'coverage.tsv').open('w') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['folder','coverage','scan_markers','transcript_lines','note_lines','transcript_sha256','note_sha256','annotated_read','method']);w.writerows(rows)
summary={'at':NOW,'claims':len(claims),'classes':{k:sum(x['class']==k for x in claims) for k in 'ABCDEF'},'folders':len(rows),'pending_fates':sum(x['class']=='PENDING' for x in claims)}
(ROOT/'outputs/finalize_claims_output.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))
