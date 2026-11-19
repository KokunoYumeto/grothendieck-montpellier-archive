"""Record the individually performed supplementary parent audit; no verdict inference."""
from pathlib import Path
import json, csv, datetime
O=Path(__file__).resolve().parents[1]
WHO='GPT-6 Astra Pro / inherited effort / agent16'
DATE='2026-11-19'
log={
 'scope':'Supplementary independent review of root claims/problems; not the package source review.',
 'requests':[
  {'open':['https://people.reed.edu/~ormsbyk/kgroup/resources/Algebraic_KTheory_and_quadratic_forms.pdf']},
  {'find':[{'ref_id':'turn382986011view0','pattern':'Theorem 4.1'},{'ref_id':'turn382986011view0','pattern':'s2'}]},
  {'system2_search_query':[
   {'q':'coherent ringed space noetherian stalks compact unique continuation coherent sheaves noetherian Siu Frisch theorem'},
   {'q':'Grothendieck lemme B anneau noethérien polyèdre analytique compact faisceau cohérent suite croissante'}]},
  {'system1_search_query':[
   {'q':'"ringed space" "unique continuation" noetherian'},
   {'q':'"coherent" "stalks" "ascending" "compact" Noetherian Frisch Siu'}],
   'open':['https://people.math.harvard.edu/~siu/siu_reprints/siu_noetherian_stein_ring_proc_ams1969.pdf','https://webusers.imj-prg.fr/~patrick.polo/SGA3/Expo12.pdf']},
  {'screenshot':[{'ref_id':'turn893736152view0','pageno':0},{'ref_id':'turn893736152view0','pageno':1}]}
 ],
 'source_results':[
  {'key':'R-Milnor1970','refs':['turn382986011view0','turn333528165view0','turn333528165view1'], 'url':'https://people.reed.edu/~ormsbyk/kgroup/resources/Algebraic_KTheory_and_quadratic_forms.pdf','locator':'Theorem4.1, printedpp331–332, PDFpp14–15','result':'Opened and read: s1 and s2 explicitly bijective. Supports the root two-step comparison with the separately cited Merkurjev theorem.'},
  {'key':'R-Siu1969','refs':['turn893736152view0','turn106483328view0','turn106483328view1'],'url':'https://people.math.harvard.edu/~siu/siu_reprints/siu_noetherian_stein_ring_proc_ams1969.pdf','locator':'Theorem1, printedp483; parent-created local image public_sources/siu1969_page1.png personally viewed','result':'PDF opened but no parsed text. Screenshot request did not yield a visible image in the functions output; therefore used the existing rendered local first page, actually viewed. Exact theorem is analytic, not an abstract ringed-space criterion.'},
  {'key':'R-SGA3XII','refs':['turn893736152view1'],'url':'https://webusers.imj-prg.fr/~patrick.polo/SGA3/Expo12.pdf','locator':'Remark1.6, PDFp3/printedp121/originalp184; lines109–117 in opened extraction','result':'Opened and read: genericGm/specialGa family asserted. Supports classA for existence; does not print the x+y+3xy reconstruction.'}
 ],
 'search_result_limits':'Scheme and analytic results appeared; no exact abstract Lemma B match was identified. No new verification is claimed for unopened search-result URLs or for Merkurjev, which was not reopened in this supplement.',
 'copyright_note':'Queries, bibliographic metadata, locators and own summaries only; no public-source body excerpts retained.'
}
(O/'research/root_audit_web.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
events=[]
def event(s,t,o): events.append(dict(statement_id=s,date=DATE,who=WHO,type=t,outcome=o))
for s,t,o in [
 ('CL-SA18-11064','independent proof check','Verified SL4 nested-torus counterexample: primitive connected kernel, centralizersD, S4 stabilizersC2 and1; maximal-T repair valid.'),
 ('CL-SA18-11065','reference check','Opened SGA3XII Remark1.6: original existence assertion published; explicit group law is present reconstruction.'),
 ('CL-SA18-11085','reference check','Independently opened Milnor1970 Theorem4.1 pp331–332; degree2 isomorphism explicit. No new Merkurjev source verification claimed.'),
 ('CL-SA18-11096','independent proof check','RP2 constant-C counterexample meets the main LemmaA hypotheses; sign local system has H1=0 and Gamma=0. Marginal variant excluded.'),
 ('CL-SA18-11097','independent proof check','Global generation plus coherent kernels, quasi-compactness and H1 vanishing gives finite global presentations and the repaired equivalence.'),
 ('CL-SA18-11100','independent proof check','Verified uniform product-kernel coherence and idempotent-supported coordinate lifting in the one-variable elimination counterexample.'),
 ('CL-SA18-11102','targeted proof check','Source lines447–464 contain no proof sketch; full abstract fixed-neighborhood stabilization step not verified. Analytic special case only established by openedSiu.'),
 ('MP-SA18-11036','literature scope check','Actual two-engine searches found no exact abstract lemma. Siu1969 Theorem1 is an analytic compact criterion; retain distinction.'),
 ('CL-SA18-11109a','independent proof check','Semilocal dimension counterexample has two2-dimensional components and twoheight2 maxima, but saturated chains of lengths1 and2.'),
 ('CL-SA18-11110a','independent proof check','Literal lattice is a product by an integral generator subtraction. ClassB is not established by this new diagnosis plus a general reducibility reference.'),
 ('CL-SA18-11110b','independent proof check','Alternative lattice nonprojective by absence of complementary elliptic line; origin must distinguish manuscript goal from current construction.'),
 ('R-Milnor1970','reference check','Personally opened and read Theorem4.1 pp331–332; degree1 and2 maps bijective.'),
 ('R-Siu1969','reference check','Personally opened PDF and viewed rendered first page483; exact Stein compact theorem read.'),
 ('R-SGA3XII','reference check','Personally opened primary re-edition; Remark1.6 existence assertion read.')
]: event(s,t,o)
with (O/'root_audit_CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(events)
counts={'root_claim_records_screened':114,'root_problem_records_screened':39,'argument_sections_read':['R'+str(i) for i in range(1,12)],'supplemental_check_events':len(events),'primary_references_independently_reopened':3,'substantive_source_status_and_scope_flags':1,'smaller_locator_or_attribution_flags':2,'root_files_modified':0,'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(O/'outputs/root_audit_counts.json').write_text(json.dumps(counts,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(counts,ensure_ascii=False,indent=2))
