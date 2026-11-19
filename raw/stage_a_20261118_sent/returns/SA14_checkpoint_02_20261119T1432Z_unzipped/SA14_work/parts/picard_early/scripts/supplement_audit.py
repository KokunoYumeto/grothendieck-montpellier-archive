"""Record the supplemental, manually completed root audit; no claim verdicts inferred."""
import csv, json, pathlib

B = pathlib.Path(__file__).resolve().parents[1]
STAMP = '2026-11-19T14:19:32Z'
WHO = 'GPT-6 Astra Pro; effort not exposed; SA14-20261119; picard_early'

def read(name):
    with (B/name).open(newline='') as f:
        r=csv.DictReader(f, delimiter='\t')
        return r.fieldnames,list(r)

def write(name, fields, rows):
    with (B/name).open('w', newline='') as f:
        w=csv.DictWriter(f, fieldnames=fields, delimiter='\t')
        w.writeheader();w.writerows(rows)

fields, rows=read('read_log.tsv')
for row in rows:
    row['reading']=row['reading'].replace('Actual full chunk read in the session; Actual full chunk read in the session;', 'Actual full chunk read in the session;')
reads=[
 ('SA14_work/research/root_proofs.md','section1','section12','Complete authored proof dossier read for an independent issue audit, with special attention to sections4–6.'),
 ('SA14_work/parts/root/claims.json','C-SA14-601','C-SA14-686','All statement/fate fields read. The initially truncated combined display was followed by a separate complete display ofC629–657.'),
 ('sources/SA14_texts/codex/A57-02_transcription.tex','1','32','Scans20–23: full equivalence-relation, correspondence-separatedness and Murre-letter argument reread.'),
 ('sources/SA14_texts/codex/K57-03_transcription.tex','395','430','Scan64: read general Q-base group conormal question distinctly from Picard smoothness.'),
 ('sources/SA14_texts/codex/K57-02_transcription.tex','276','341','Scans45–49: read finite-etale rigidity lemma, historical separated-scheme wording, proof and group application.'),
 ('sources/SA14_texts/codex/K57-08_transcription.tex','125–148','170–194','Scans138 and140: finite Stein factor, rigidification, exact sequence and fpqc descent. These are two actual displayed chunks, not intervening lines.'),
 ('sources/SA14_texts/codex/K57-10_transcription.tex','164','335','Scans173–179: raw Picard presheaf, Zariski-local and fpqc versions, section and Brauer–Severi example.'),
 ('https://arxiv.org/pdf/1902.07448','PDFpage1','PDFpage5','Full Bertolin–Galluzzi v2 paper read; special semiabelian hypotheses and RaynaudIII Proposition4.3 citation recorded.'),
 ('https://webusers.imj-prg.fr/~patrick.polo/SGA3/origExp6B.pdf','PDFpage6','PDFpage6','Proposition1.6 and Corollary1.6.1 read, extracted lines244–268; local finite presentation and absence of prior flatness checked.'),
 ('https://webusers.imj-prg.fr/~patrick.polo/SGA3/Expo11.pdf','PDFpage1','PDFpage1','Primary title header and author read to verify R_SGA3XI; no title correction needed.'),
]
for source,start,end,reading in reads:
    if not any(r['source']==source and r['chunk_start']==start and r['chunk_end']==end for r in rows):
        rows.append(dict(recorded_at_utc=STAMP,source=source,chunk_start=start,chunk_end=end,reading=reading,provenance='Supplemental audit; timestamp records this retrospective log entry, not the original display time. Only the named actual chunks are claimed as read.'))
write('read_log.tsv',fields,rows)

fields,rows=read('CHECK_EVENTS.tsv')
events=[
 ('C-SA14-612','targeted proof check','Supplemental root audit: the initial broad modern wording needed ambient separation or closed embeddings. Source45–49 preserves historical separated-scheme convention; doubled-trait group supplies a counterexample without either condition. Root has since added the condition.'),
 ('C-SA14-639','independent re-proof','Supplemental root audit: normalization inverse, vanishing of the Brauer boundary under a section, and rigidified descent are correct in universalH0=O_S scope. Scans138–140 additionally require a separate finite-Stein-factor record; this is a coverage omission, not a refutation ofC639.'),
 ('C-SA14-640','targeted proof check','Supplemental root audit: claim uses finite etale divisor correctly; root_proofs section6 prose finite reduced is insufficient over an imperfect field and should match the claim. Invertible-n generalized-Jacobian torsion and R2 compact-support calculation are consistent under the written claim hypotheses.'),
 ('C-SA14-674','targeted proof check','Supplemental bounded search: modern algebraic-space Picard representability and Bertolin–Galluzzi semiabelian special case checked. Exact general RaynaudIII Proposition4.3 primary text was not obtained. KeepC; no claim that the general theorem remains mathematically open in2026.'),
 ('C-SA14-686','targeted proof check','Supplemental exact primary theorem check: SGA3 VI_B Proposition1.6, PDFpage6, proves characteristic-zero locally-finitely-presented group smooth along identity iff conormal locally free; no prior flatness is required. Distinct from Cartier field Corollary1.6.1.'),
 ('C-SA14-687','independent re-proof','Supplemental refinement for root: finite Stein factor Σ/S, section of X→Σ and universal O_Σ≅φ_*O_X give quotient Pic(X_T)/Pic(Σ_T) as a rigidified fpqc sheaf. Finite Σ/S makes its line bundles Zariski-locally trivial overT, so this quotient is the usual relative Picard sheaf. No finite-flatness hypothesis onΣ/S is needed; detailed argument in supplement_root_audit.md.'),
 ('R_SGA3XI','used and rechecked in this run','Supplemental primary header check: title Critères de représentabilité. Applications aux sous-groupes de type multiplicatif des schémas en groupes affines, byA.Grothendieck, confirmed on opened Expo11 PDFpage1. This event verifies bibliographic title, not every theorem in the exposé.'),
]
for sid,kind,outcome in events:
    if not any(r['statement_id']==sid and r['outcome']==outcome for r in rows):
        rows.append(dict(statement_id=sid,date='2026-11-19',who=WHO,type=kind,outcome=outcome))
write('CHECK_EVENTS.tsv',fields,rows)

write('supplement_search_log.tsv',['search_id','root_claim_ids','queries','opened_sources','result','raw_records'],[
 dict(search_id='PE-S21',root_claim_ids='C-SA14-674',queries='Search-theme summary, not retained literal input: Corr Picard separated Murre; functeur des correspondances séparé; Murre correspondences separated Picard functor; functor Corr separatedness algebraic; Picard rigidity algebraic spaces proper flat; A note on divisorial correspondences arxiv; Raynaud III4.3; Raynaud III.4.3; Raynaud III, Proposition4.3',opened_sources='https://arxiv.org/pdf/1902.07448; https://link.springer.com/book/10.1007/BFb0059504; https://link.springer.com/chapter/10.1007/BFb0059509; https://stacks.math.columbia.edu/tag/0D2C; https://link.springer.com/article/10.1007/s00574-023-00378-0',result='Full Bertolin–Galluzzi paper gives special hypotheses and cites RaynaudIII4.3; only Raynaud book/chapter metadata available. Algebraic-space Picard existence alone does not finish the checked rigidity argument. ClassC retained with bounded source gap, not present-day openness assertion.',raw_records='outputs/web_58.json through outputs/web_70.json; exact final query Raynaud [doublequote]correspondances[doublequote] [doublequote]4.3[doublequote] and output in outputs/web_72.json; supplement_root_audit.md'),
 dict(search_id='PE-S22',root_claim_ids='C-SA14-686',queries='Search-theme summary, not retained literal input: SGA3 VI_B Proposition1.6 conormal smooth characteristic zero; schéma en groupes conormal localement libre caractéristique zéro lisse',opened_sources='https://webusers.imj-prg.fr/~patrick.polo/SGA3/origExp6B.pdf',result='Exact Proposition1.6 read at PDFpage6/printed202: locally finite presentation alongidentity explicit, no prior flatness. Field Cartier theorem separate.',raw_records='outputs/web_60.json; outputs/web_61.json; exact final query SGA3 [doublequote]conormal[doublequote] [doublequote]1.6[doublequote] and output in outputs/web_72.json; supplement_root_audit.md'),
 dict(search_id='PE-S23',root_claim_ids='C-SA14-612;R_SGA3XI',queries='Direct open of primary SGA3 ExpoXI for exact header',opened_sources='https://webusers.imj-prg.fr/~patrick.polo/SGA3/Expo11.pdf',result='Existing root bibliography title confirmed; no replacement invented.',raw_records='outputs/web_71.json; supplement_root_audit.md')
])
print(json.dumps({'supplemental_read_chunks':len(reads),'supplemental_check_events':len(events),'supplemental_search_groups':3},indent=2))
