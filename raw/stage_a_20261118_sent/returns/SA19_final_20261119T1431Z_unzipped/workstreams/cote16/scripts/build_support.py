"""Coverage and check-event serialization from the actual reading/check ledger."""
import csv,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1];base=root.parents[2]
def tsv(name,fields,rows):
    with (root/name).open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(fields);w.writerows(rows)
text=(base/'source/SA19_texts/pro/MPL_16+47+54+44_transcription.tex').read_text().splitlines()
end=next(i for i,s in enumerate(text) if r'\cotefile{47}' in s)
marks=[(i+1,int(re.search(r'\\scanpage\{(\d+)\}',s).group(1))) for i,s in enumerate(text[:end]) if re.search(r'\\scanpage\{(\d+)\}',s)]
cov=[]
for j,(start,p) in enumerate(marks):
    stop=marks[j+1][0]-1 if j+1<len(marks) else end
    cov.append([16,p,start,stop,'entire supplied scan marker read','2026-11-19','All mathematical text, cancellations, margins, and unindexed per-scan notes read; applicable second-pass changes and checked-notes read. No manuscript images supplied.'])
tsv('reading_coverage.tsv',['cote','scan','first_line','last_line','coverage','date','qualification'],cov)
events=[];who='GPT-6 Astra Pro; inherited reasoning effort not exposed; SA19/cote16'
def ev(s,t,o):events.append([s,'2026-11-19',who,t,o])
items=json.loads((root/'items.json').read_text());claims=json.loads((root/'claims.json').read_text())
for x in items:
    ev(x['id'],'used and rechecked in this run','Documentary comparison of every source note with its actual cited transcription passage and second-pass current readings: '+x['check']+'. '+x['check_reason']+' This event is a text check, not a claim of mathematical proof.')
proof={201,202,203,204,205,206,207,210,211,212,213,215,216,217,223,224,225,226,227,228,229,233,234,235,236,237,238,239,242,247,248,249,250,253,254,255,257,260,261,264,265,266,268,270,273,279,280,281}
computes={207,208,209,211,212,215,217,223,225,227,228,229,235,236,237,238,247,254,266,268,279}
refutations={208:279,209:279,212:280,254:280,273:281}
for c in claims:
    n=int(c['id'].split('-')[-1])
    if n in refutations:
        ev(c['id'],"refuted, with the refined statement's id",f"Refuted the literal formulation; refined statement CL-SA19-{refutations[n]}. {c['computation']}")
    elif n in {227,268}:
        ev(c['id'],'targeted proof check','Literal detached assertion fails under the stated interpretation; the exact counterexample and missing qualification are documented. '+c['computation'])
    elif n in proof:
        ev(c['id'],'independent re-proof',c['computation']+' The hypotheses and reconstruction limits are those in this record; not a proof of any stronger source conjecture.')
    else:
        ev(c['id'],'carried as background without fault found','Source status and searched literature fate recorded; no independent proof claimed. '+c['fate'])
    if n in computes:ev(c['id'],'computation or formal certificate',c['computation']+' Finite tests are labelled as such; all-parameter arguments are in proof_checks.md.')
for key,outcome in [
 ('Kleiman1968','Primary propositions 2.9--2.13,2A9--2A10 and results3.12--3.16 read with hypotheses and compared to the source; independent finite-string and algebraic proofs are separately recorded.'),
 ('Deligne1980','Read primary Theorem4.1.1 and proof. Used only as rational ell-adic hard Lefschetz, not as an algebraic-cycle inverse theorem.'),
 ('Matlis1958','Read Theorem2.5, Proposition3.1, localization statements and Theorem3.10; matched decomposition and layer dimensions.'),
 ('Mumford1961','Read negative-definiteness proof and topological cokernel calculation; did not infer arbitrary-characteristic étale pairing compatibility.'),
 ('Jannsen1992','Read main theorem, Corollary1 and remarks; numerical semisimplicity and nilpotent-kernel assertions kept distinct from general homological semisimplicity.'),
 ('SGA3II1970','Read XV Proposition6.2(iii) proof and XV--XVII introduction; matched generic Cartan spreading and editorial provenance.'),
 ('Karoubi1968','Read expanded primary §2.3, its hypotheses and stated periodicity results; did not independently prove Bott periodicity.'),
 ('Stacks2026','Read exact tags in bibliography/research log; used hypotheses of each local algebra/homological result, not a general proof check of the whole project.'),
 ('AnconaEtAl2025','Read primary introduction and main scope. Special LSV/fibration theorem is not a universal proof of the standard conjectures.')]:
    ev(key,'used and rechecked in this run',outcome)
for key,outcome in [
 ('Grothendieck1968BrauerIII','Primary printed143–151 read in downloaded PDF via rendering/OCR; key pages visually checked. Remark8.5 explicitly preserves the pairing comparison gap, and this publication is not used as a proof that the author says he did not supply.'),
 ('Suzuki2024','Read introduction and exact mixed-characteristic hypotheses, Theorem1.6, Proposition11.2 and full Proposition11.10 proof. Used as an exact p-primary analogue, not a universal closure of the equal-characteristic historical gap.'),
 ('KatzMessing1974','All original printed73–77 read; Theorem2 statement/proof visually checked. Finite-field hypotheses and correspondence integrality kept. Page73 plus bibliography dates Deligne hard-Lefschetz circulation by1973.'),
 ('Sutherland2021','Read Theorem11.10 and Hensel/uniformizer proof with complete DVR and total tame hypotheses.'),
 ('Gabriel1962','Read IV§2Theorem2 and VI§§1–2, especially Theorem1, in parent-downloaded primary scan text. Used only with its explicit QCoh/noetherian conventions.'),
 ('Hartshorne1966','Read original1966II§7pp120–136, especially7.5–7.6,7.9,7.14,7.16–7.18 with proofs. Exact theorem lineage established; typescript authorship remains separate.'),
 ('Murfet2006','Read §8.2Lemma67 and Proposition68; followed cited Hartshorne original.'),
 ('LuntsSchnuerer2016','Read Theorem2.1 and proof p912 for locally-noetherian QCoh versus all-module injectivity. No matrix-factorization result used.')]:
    ev(key,'used and rechecked in this run',outcome)
for num,result in [(258,'Original HartshorneII7.17 theorem and proof matched; classification statement verified with its quasi-coherence and locally-noetherian assumptions.'),(269,'Complete-DVR result verified directly in Sutherland11.10; no missing Galois or canonical-generator conclusion inferred.'),(271,'Exact Stacks033C and025L statements/proofs read for normality and reducedness.'),(277,'Étale-local finite splitting verified in Stacks04HN; descent and constant-rank caveat retained.'),(284,'Read and matched Katz–MessingTheorem2(1)–(2) with proof; finite-field extension of the source question established.')]:
    ev(f'CL-SA19-{num}','used and rechecked in this run',result)
for key,result in [
 ('Grothendieck1969','Original scan opened at title/metadata level; precise mathematical comparisons use the fully readable Kleiman text. No full proof check claimed.'),
 ('Messing1975','Unverified bibliographic lead only; no proof or priority conclusion rests on it. Earlier1973 circulation now has direct Katz–Messing evidence.'),
 ('Hodge1938','Exact title/page/DOI lead from manuscript and later attribution; original publisher access failed. No original theorem proof or reception-history conclusion claimed.'),
 ('Karoubi1966','Named author/title and original announcement scan inspected at bibliographic level; expanded1968paper is the source for theorem scope.'),
 ('Shatz1964','Unverified backward-citation lead; opening failed. No theorem attributed to this paper without its missing assumptions.'),
 ('Shatz1966','Publisher metadata opened; exact reused English typescript not matched.'),
 ('Tate1959','Unverified backward-citation lead from the supplied fragment; no exact theorem matched.'),
 ('Serre1962','Classical local-fields bibliographic lead; exact theorem verification instead uses opened Sutherland11.10 and its proof.')]:
    ev(key,'carried as background without fault found',result)
for key,result in [
 ('SGA1','Opened full primary annotated reprint and read original-exposé statements X3.4 with its purity-based proof context, X3.8–3.9 and XI1.1; seminar1960–1961, original book1971 and2004reprint dates kept separate.'),
 ('EGAIV4','Metadata, galley number18.11 and modern exact related results checked; publication-text reading level recorded explicitly in bibliography/research log.'),
 ('RosenbergZelinsky1962','Primary introduction and Lemmas2.1–2.2 read for acyclicity and faithful-flat hypotheses. They do not uniquely identify the detached Proposition15.')]:
    ev(key,'used and rechecked in this run',result)
ev('CL-SA19-278','used and rechecked in this run','Full Stacks10.152.1 proof read. The finite unramified monogenic subalgebra is a quotient of a standard étale algebra, not necessarily that algebra itself; étale41.12.1 and finite-unramified41.17.3 compared. Audit statement corrected to retain this distinction.')
tsv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)
print(f'Coverage: {len(cov)} full scan markers. Check events: {len(events)}.')
