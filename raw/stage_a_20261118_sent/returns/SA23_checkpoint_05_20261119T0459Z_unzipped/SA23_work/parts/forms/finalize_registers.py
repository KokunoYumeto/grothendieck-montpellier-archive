from pathlib import Path
import json,csv,datetime
P=Path(__file__).parent
cs=json.loads((P/'claims.json').read_text());its=json.loads((P/'items.json').read_text());R=json.loads((P/'reference_checks.json').read_text());docs=json.loads((P/'document_records.json').read_text()) if (P/'document_records.json').exists() else []
L=[]
def l(kind,fr,to,what,evidence,notes='unindexed supplied transcriptions'):
 L.append([kind,fr,to,what,evidence,notes])
l('folder','162-5 API scans2–17,physical39–734','162-5 API scans32–48,physical740–1363','Repeated typed Tapis notes merged by subject, with differing margins retained.','Both complete witnesses directly read; no chronological ordering inferred.')
l('folder','162-5 Codex scan22,physical31–36','162-5 API scans2,32,physical39–45,740–746','Distinct6September and10September1968 date lines.','Both date lines directly read; not merged into one manuscript date.')
l('folder','24 Blass scans34–35,physical1301–1338;C-SA23-forms-014','25 scans30–31,physical1225–1293;C-SA23-hyp-017','The finite-etale7.4 properness statement conflicts with the next projectivity remark in both typed witnesses.','Both endpoints directly read by forms; root independently read both. Cancellation extent in Blass remains undecided.')
l('folder','24 Blass scan48,physical1797–1804;C-SA23-forms-020','25 scans139–141,physical5520–5620, and158–160,physical6261–6374;C-SA23-hyp-078/-029','Ordinary versus non-supersingular quadratic singularities: early live/cancelled definitions at139–141; explicit smooth-projective-tangent-quadric correction at158–160.','Forms directly read Blass; root directly read both cote25 loci and reported the exact distinction. This does not erase the typed discrepancy.')
l('folder','24 Blass scans43–51,physical1603–1956;C-SA23-forms-019/-021','25 scans37–45,physical1505–1860;C-SA23-hyp-021/-022','Conormal incidence, differential of dual projection and reflexivity argument.','Forms read all Blass; root read both typed loci. Same projective-convention and immersion qualifications preserved.')
l('published work','24 Blass scans43–51,physical1603–1956;C-SA23-forms-019/-020/-021','forms_SGA7Katz,SGA7IIXVII3.1,3.3,3.5,pp216–217,221–228','Published conormal presentation and precise nondegenerate Hessian criterion.','Original SGA7 text/OCR read; includes parity distinction and immersion setup.')
l('published work','24 Blass scans52–53,physical1958–2016;C-SA23-forms-022','forms_SGA7Katz,XVIIExample3.4,pp225–226','Requested inseparable-dual example is supplied by the smooth degree-p+1 Fermat hypersurface.','Both passages directly read; gradient and Gauss differential recomputed.')
l('published work','24 Blass scans63–71,physical2345–2645;C-SA23-forms-026/-031','forms_SGA7Katz,XVII2.2,2.5.1–2.5.2,pp215–216','Degree≥2 Veronese Lefschetz-pencil existence, with ordinary rather than automatically nondegenerate singularities.','Both source passages read; characteristic2 qualification explicit.')
l('published work','24 Blass scans55–62,physical2126–2336;C-SA23-forms-024/-025','forms_Benoist2011,Theorem1.5;forms_PoonenSlavov,Theorem1.5 andExample1.7','Modern depth obstruction and fixed-base/equidimensionality bounds match parts of the draft.','Exact introductory statements/examples opened and read; not a restoration of damaged iff clauses.')
l('published work','162-5 API scans57–68,physical1656–2090;C-SA23-forms-058–063','forms_QuillenEtale,Topology7(1968)pp111–116','Attached potential proof corresponds to the published explicitly incomplete etale sketch.','Entire attached and published texts read; conjecture/lemma labels compared.')
l('published work','162-5 API scans61–68,physical1813–2090;C-SA23-forms-061/-062','forms_Friedlander,Theorem5.3 and§6Theorem6.8,pp37–38,45','Later theorem supplies the completed punctured-bundle fibration and completes the complex Adams route.','Exact rank,noetherian,profiniteπ1,and prime-completion hypotheses read.')
l('published work','162-5 API scan57,physical1660–1697;C-SA23-forms-058','forms_QuillenAdams,Topology10(1971)Theorem1.1,pp67–70','Final Adams theorem proved by a different method.','Primary introduction explicitly separates its non-etale proof from Friedlander completion.')
l('published work','162-5 API scans50–55,physical1369–1650;C-SA23-forms-055–057','Quillen1968Inventiones5pp237–242,forms_QuillenPositive','Attached text is the published paper itself.','Entire supplied offprint read; author and received date not inferred from neighboring notes.')
l('published work','162-5 API scans14–15,45–46,physical573–653,1217–1290;C-SA23-forms-047','forms_Thom,II.10–II.13 andIV.12','Additive splitting and polynomial coefficient ring, correcting the reversed excluded-degree margin.','Original selected theorem statements/proofs read; no multiplicative conclusion attributed to Thom’s additive theorem.')
l('published work','162-5 API scan45,physical1232–1245;C-SA23-forms-048','forms_Szymik,Theorem1.3,Proposition5.1,Theorem5.6;Boardman1980Theorem1.1 through that primary source','Homotopy-multiplicative section exists; E-infinity strengthening fails.','Exact theorem hypotheses read. Original Boardman link inaccessible and separately marked unverified.')
l('published work','162-5 API scans8,38,physical302–325,985–1009;C-SA23-forms-041','forms_HopkinsSinger,AppendixB.2,pp428–431','Picard self-commutor obstructs strict commutativity.','Both passages read; superline counterexample independently checked.')
l('published work','162-5 API scans10–11,40–41,physical399–442,1077–1117;C-SA23-forms-044','forms_QuillenK§2;forms_Segal§0–1;forms_Schlichting§0.3 andProposition2.2','Development of exact/monoidal K-theory and limits of unenhanced triangulated categories.','Primary definitions and exact counterexample scope read; different enhancements not conflated.')
l('published work','162-5 Codex scans28–31,physical225–343;C-SA23-forms-071/-073','forms_StacksCrystals,60.15.1,tag07J6','First-order connection and second-order cocycle force integrability.','Full primary construction/proof read; does not establish every flat-conormal converse.')
l('published work','162-5 Codex scan27,physical215–218;C-SA23-forms-069','forms_FormalModuli,Theorem9.2.2 pp43–44','Verified locally projective formal-groupoid comparison is a partial match to the attributed flat-conormal theorem.','Both hypotheses read; flat conormal and projective tangent are not equated.')
l('published work','162-5 API scans9,39,physical350–360,1033–1044;C-SA23-forms-043','forms_Stasheff,Theorem17 printed pp282–283','A4 space with no A5 structure gives the checked negative answer for bare homotopy-group objects.','Full primary theorem and proof read by forms and independently by root; Adams attribution and1963 publication retained.')
with (P/'links.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['kind','from','to','what','evidence','note_ids']);w.writerows(L)
who='GPT-6 Astra Pro; effort not independently exposed; run SA23-20261119; owner forms'
refuted={4,6,10,20,25,29,32,38,41,49,52,66,67,73,80,82}
# These numbers are manually selected mathematical checks, not verdicts inferred from headings.
source_match={7,19,21,22,23,24,26,28,34,35,37,43,44,47,48,50,54,58,59,60,61,62,64,68,69,70,71,74,83,84}
e=[]
for c in cs:
 n=int(c['id'].rsplit('-',1)[1])
 typ='refuted, with refinement in same claim' if n in refuted else ('used and rechecked in this run' if n in source_match else 'targeted proof check')
 if c['class']=='F':typ='carried as background without fault found'
 e.append([c['id'],'2026-11-19',who,typ,c['computation']])
for c in docs:e.append([c['id'],'2026-11-19',who,'carried as background without fault found','Document metadata record, excluded from mathematical claim counts. '+c['computation']])
for i in its:
 matches=[c['id'] for c in cs if i['id'] in c['items']]
 dmatches=[c['id'] for c in docs if i['id'] in c['items']]
 e.append([i['id'],'2026-11-19',who,'used and rechecked in this run' if matches else 'carried as background without fault found','Manually consolidated from direct readings; mathematical checks in '+','.join(matches)+'. This is not a new indexed-entry verdict.' if matches else 'Document metadata checked against supplied text; records '+','.join(dmatches)+'. Excluded from mathematical claim counts.'])
background_refs={'forms_Derived','forms_MultiNerve','forms_StacksDimension','forms_StacksCoherent','forms_StacksDiff','forms_StacksConstructible','forms_StacksQuasiSections','forms_ArchiveMetadata'}
for k,r in R.items():e.append([k,'2026-11-19',who,'used and rechecked in this run' if r['note']=='verified' and k not in background_refs else 'carried as background without fault found',r['annotation']+'; verification flag='+r['note']+'; a verified URL is not a claim that the whole work was proof-checked.'])
if (P/'compute_checks.output.json').exists():
 for k,v in json.loads((P/'compute_checks.output.json').read_text()).items():e.append([k,'2026-11-19',who,'computation or formal certificate','Executed exact code; scope limited as recorded; claims '+','.join(v['claims'])])
for q in json.loads((P/'problems.json').read_text())+json.loads((P/'editorial_tasks.json').read_text()):
 e.append([q['id'],'2026-11-19',who,'manual source-question provenance audit',q['origin']+'. '+q['source_cue']])
with (P/'check_events.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(e)
logs=[]
for k,r in R.items():logs.append({'id':'R-forms-'+k,'date':'2026-11-19','engine':'direct primary-source navigation and locator inspection','query':None,'navigation_target':r['url'],'claims':[c['id'] for c in cs if k in c['refs']],'url':r['url'],'locator':r['annotation'],'outcome':'Exact scope and access limitation recorded in annotation. Bibliographic verification: '+r['note']})
if (P/'web_query_audit.json').exists():logs+=json.loads((P/'web_query_audit.json').read_text())
if (P/'fate_search_audit.json').exists():logs+=json.loads((P/'fate_search_audit.json').read_text())
(P/'search_log.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in logs))
with (P/'progress.log').open('a') as f:f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+' '+str(len(L))+' links; '+str(len(e))+' check events; reference audit saved.\n')
print(len(L),'links;',len(e),'check events;',len(logs),'current search/read audit rows')
