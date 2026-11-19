"""Serialize explicit research audit records and mechanical coverage accounting."""
from pathlib import Path
import csv,json,re,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT.parents[2]
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
C=json.loads((ROOT/'claims.json').read_text())
P=json.loads((ROOT/'problems.json').read_text())
def tsv(name,head,rows):
 with (ROOT/name).open('w') as f:
  w=csv.writer(f,delimiter='\t');w.writerow(head);w.writerows(rows)
coverage=[]
for n in range(9,14):
 stem=f'J156-9-{n:02}';p=BASE/'sources/texts/codex'/f'{stem}_transcription.tex';q=BASE/'sources/notes/codex'/f'{stem}_notes.md'
 tx=p.read_text();nt=q.read_text();ss=re.findall(r'\\scanpage\{([^}]+)\}',tx)
 coverage.append([stem,'complete transcription and complete note read',','.join(ss),len(tx.splitlines()),len(nt.splitlines()),hashlib.sha256(p.read_bytes()).hexdigest(),hashlib.sha256(q.read_bytes()).hexdigest(),'outputs/'+stem+'_read.txt','Full sequential manual reading preceded claim construction; scan/line extraction is mechanical accounting only.'])
tsv('coverage.tsv',['folder','coverage','scan_markers','transcript_lines','note_lines','transcript_sha256','note_sha256','annotated_read','method'],coverage)

families={
1:('Complete ortholattices, join-map Hom orthocomplement, tensor product; orthosets adjointable; zbMATH orthotensor; MathOverflow orthotensor','Paseka–Vetterlein, Ischi, Coecke–Moore and the Chu-construction lead; no exact span result.'),
2:('Operational Galois adjunctions arXiv; Ischi/Fraser tensor; Numdam treillis orthocomplémentés; Foulis/Baer','Primary Coecke–Moore located; Numdam Baer-semigroup seminar is restricted background, not the requested general factorization.'),
3:('Orthocomplemented lattice tabulation; factorization of join maps; Shmuely title/PDF; MathOverflow orthogonal correspondences','Shmuely primary located by backwards bibliography; factorization queries gave no exact map-class theorem.'),
4:('Ischi publication/DOI; zbMATH Shmuely; Grothendieck spatios correspondances; complete ortholattice relation factorization','Domenach–Leclerc lead; archival mentions not exact published Grothendieck theorem; zbMATH linked record blocked403.'),
5:('Domenach Leclerc biclosed binary relations PDF; Ischi publication date; Grothendieck spatios EGA','Opened author preprint and publisher dates; checked Theorems4.1/5.1 rather than finite-context lookalikes.'),
6:('Grothendieck disjoncteurs; EGA orthocomplemented lattices; SGA orthocomplementation; MathOverflow ortholattice Galois','No exact Grothendieck publication endpoint or span factorization found; checked journal date of Domenach–Leclerc.')}
S=[]
for n,(query,result) in families.items():
 sid=f'IX-S{n}';claims=[c['id'] for c in C if sid in c['search_ids']]
 S.append([sid,'2026-11-19','Web search; primary follow-up; named database/site searches','Retained query family (not claimed as exact transport string): '+query,result,'Primary checks IX-R1–IX-R6 in source_checks.md; outputs/open_1.json through open_7.json', ';'.join(claims),f'outputs/search_{n}.json'])
exact=json.loads((ROOT/'outputs/exact_search_requests_7_8.json').read_text())
for b in exact:
 sid=b['id'];n=int(sid.removeprefix('IX-S'));queries=[x['q'] for x in b['args']['system2_search_query']]
 result=('Repeated primary-title and precise span queries locate the checked Shmuely, Domenach–Leclerc, Ischi and modern orthoset sources; no exact stated span theorem identified.' if n==7 else 'Named database/site follow-up gives Numdam backwards bibliography; zbMATH access/coverage limited, MathOverflow results largely irrelevant; EGA/SGA search finds no exact claim endpoint. No theorem inferred from the negative search.')
 S.append([sid,NOW,'system2_search_query',' || '.join(queries),result,'Exact requests preserved in outputs/exact_search_requests_7_8.json; previously checked primary sources remain the evidence.',';'.join(c['id'] for c in C if sid in c['search_ids']),f'outputs/search_{n}.json'])
tsv('search_log.tsv',['search_id','date','source','query','results','followup','claims','output'],S)

proof={31:'P1',32:'P5',33:'P4',34:'P11',35:'P2',36:'P3',37:'P7',38:'P4',39:'P10/P11',40:'direct graph/relation encoding in claim record',41:'notation/P5',42:'direct deletion/reattachment argument in claim record',43:'order/De Morgan argument in claim record',44:'direct canonical-preorder argument in claim record',45:'P5',46:'P5',47:'P5',48:'P6',49:'P6',50:'P6',51:'P6',52:'P4',53:'P4/P7',54:'P4/P7',55:'P7',56:'P7',57:'P8',58:'P8',59:'P9',60:'P9',61:'P11',62:'P11',63:'P9 and the distinction between a programme and a theorem',64:'P11',65:'P11',66:'P10'}
events=[]
WHO='GPT-6 Astra Pro; inherited reasoning effort; run /root/cotes_156_3_5'
for c in C:
 n=int(c['id'].rsplit('-',1)[1]);ty='independent re-proof'
 if n in (31,35,36):ty='refuted, with the refined statement’s id'
 elif n in (39,40,41,42,43,44,63,64,65):ty='used and rechecked in this run'
 if n==31:out='Inclusion-only equivalence false; equality-of-closures repair C-SA21-9-032. '+c['present_status']
 elif n in (35,36):out='Literal early lemma false; refined statements C-SA21-9-038/054/055. '+c['present_status']
 else:out=c['present_status']
 events.append([c['id'],'2026-11-19',WHO,ty,out,'proof_checks.md '+proof[n]+'; '+c['lines']])
cert={35:'early_lemma1_not_join_preserving',36:'early_lemma2_omits_generator_condition',58:'product_closed_vs_closed_fibers',60:'hom_has_no_orthocomplement',62:'pointwise_on_atoms_not_all_subsets',66:'span_obstruction_map'}
stamp=json.loads((ROOT/'outputs/finite_checks.json').read_text())['metadata']['time_utc']
for n,key in cert.items():
 out='Executed finite certificate passed; all displayed finite relation/lattice/map hypotheses are checked.'
 if n==66:out='Finite code verifies only the displayed map preserves joins. Exclusion of every intermediate K is the independent symbolic proof P10, not a computational claim.'
 events.append([f'C-SA21-9-{n:03}',stamp,WHO,'computation or formal certificate',out,'code/finite_checks.py; outputs/finite_checks.json:'+key])
refevents=[
 ('Birkhoff1948','used and rechecked in this run','Primary 1948 chapter IV, not V: §5 polarity/Theorem9 pp54–56, §6 Theorem10 p56, §7 Theorems11–12 pp58–59. Galois/closure and representation ingredients checked; no novel arbitrary-generator theorem inferred.','IX-R1'),
 ('Shmuely1974','targeted proof check','Checked §1 Galois identities, §3 Theorem1.3 closed-fiber G-ideals, §5 Theorem1.5 transpose and §6 Theorem1.6 completeness. Dualizing gives the all-join-map formulation; complete-lattice domain restriction retained.','IX-R2'),
 ('CoeckeMoore2000','targeted proof check','Checked §3[3.2–3.4] and relevant appendix proof: join/right adjoint equivalence, conjugate f†=CrC, involution and reversal of composition. §7 atomistic restrictions not imported into the general statement.','IX-R3'),
 ('DomenachLeclerc2001','targeted proof check','Checked primary author-preprint §4 Theorem4.1 and §5 Theorem5.1/Cor5.1, with their proof steps: arbitrary closure-space biclosed relations versus antitone Galois connections and join-generating presentations. Applied to C∘f; exact quantifiers match.','IX-R4'),
 ('PasekaVetterlein2025','targeted proof check','Checked v3 Lemma2.3/Proposition2.4 and Lemmas3.4–3.7. Join-dense presentation and closure-compatible adjoints match after zero-convention qualification; corrected Proposition6.10 not used. Publisher date resolves arXiv metadata discrepancy.','IX-R5'),
 ('Ischi2010','targeted proof check','Checked Definition2.10 and Theorems3.4,3.6,4.9. Four-atom factors are weakly connected and satisfy the simple-closure-space hypotheses; maximal versus minimal product gives the exact allowed countercase. The Hom obstruction was also independently counted.','IX-R6'),
]
for key,ty,out,loc in refevents:events.append([key,'2026-11-19',WHO,ty,out,'source_checks.md '+loc])
for p in P:
 events.append([p['id'],'2026-11-19',WHO,'used and rechecked in this run','All listed occurrences read; internal resolution and present mathematical status checked as stated. An unproved historical motive is not inferred.','problems.json; corresponding claim/proof and primary-source records'])
tsv('check_events.tsv',['statement_id','date','who','type','outcome','evidence'],events)
old=(ROOT/'progress.log').read_text() if (ROOT/'progress.log').exists() else ''
if not old:
 first=min((ROOT/'outputs'/f'J156-9-{n:02}_read.txt').stat().st_mtime for n in range(9,14))
 old=datetime.datetime.fromtimestamp(first,datetime.timezone.utc).isoformat()+'\tIX reading checkpoint: earliest saved full-read file timestamp; precise start time not reconstructed. Root global log records task start.\n'
old+=NOW+'\tStages2–5 serialized: 5 folders/39 scans fully read, 36 claims, 9 problems, 16 reading alarms, 21 links, 8 search batches, '+str(len(events))+' check events.\n'
(ROOT/'progress.log').write_text(old)
out={'at':NOW,'folders':len(coverage),'scans':sum(len(x[2].split(',')) for x in coverage),'claims':len(C),'problems':len(P),'search_batches':len(S),'check_events':len(events),'unmapped_claims':[c['id'] for c in C if not c['search_ids']]}
(ROOT/'outputs/author_logs_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
