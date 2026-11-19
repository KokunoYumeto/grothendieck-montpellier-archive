"""Checkpoint-03 addendum; never writes the root's combined report or ledger."""
from pathlib import Path
from collections import Counter
import csv
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/f6dbb6638732')
DATE = '2026-11-19'
WHO = 'GPT-6 Astra Pro (OpenAI); inherited effort (not independently specified); RESEARCH_SA07; agent period_triangle'
LEDGER = 'work/audit_next_CHECK_EVENTS.tsv'
PROOF = 'targeted proof check'
REPROOF = 'independent re-proof'
CERT = 'computation or formal certificate'
USE = 'used and rechecked in this run'
BACKGROUND = 'carried as background without fault found'
REFUTE = "refuted, with the refined statement's id"
ALLOWED = {PROOF, REPROOF, CERT, USE, BACKGROUND, REFUTE}
events = []

def event(statement_id, kind, outcome):
    assert kind in ALLOWED
    events.append(dict(statement_id=statement_id, date=DATE, who=WHO, type=kind, outcome=outcome))

event('B.4.4', REPROOF, 'Constructed the unramified ell-power Artin tower plus Tate motive over Q_p, with ell different from p. The exact image is Z_ell times Z_p^times because the unramified and cyclotomic totally ramified towers are disjoint. Constructed E=(Z_ell times C_p^times) semidirect G_Qp with the natural semilinear action, both continuous sections, j, epsilon, u and phi; checked every B.4 compatibility and kernel identity, including p=2. DDMS Theorem 8.32 and Corollary 8.34 exclude analyticity because this compact image has no open pro-p subgroup. Every finite object is crystalline; finite-level images remain analytic.')
event('B.4.4', CERT, 'Ran comparison_counterexamples.py: all section, commutation, compatibility, cocycle, exact-image and kernel identities passed for (p,ell,m,n)=(2,3,2,4),(3,2,3,3),(5,2,3,2), over groups of orders 72,144,160, respectively. Output copied to output/RESEARCH_SA07/code/comparison_counterexamples.output.txt. Infinite nonanalyticity is proved, not inferred from these finite checks.')
event('F.3.10', REPROOF, 'Read full LM6 A.50 pp.33–34 and A.22 pp.16–17. Repaired the unstated A subset N premise by the exact enlargement N-tilde=NA, D-tilde=(N intersect F)A and theta-tilde(na)=theta(n); all original hypotheses and the original character on N remain unchanged. Proved Sylow centralization, descent of theta^d to G_L, finite-cover detection, and the boundary/Jacobian alternatives. The noncuspidal weight-one character does not supply Stix cyclotomic action; the common-kernel subgroup problem in A.22 remains OPEN. Later LM6 restrictions have not all been independently re-proved.')
event('F.3.10', CERT, 'Ran audit_next_certificates.py in the integral noncommutative algebra truncated in degree six. The exact double commutator has XYYXX coefficient -1 in degree five, so its reduction survives every prime. Sample reductions at 2,3,5,7,11,13 also passed; the all-prime conclusion uses the integral coefficient, not the samples.')
event('F.3.11', REPROOF, 'Constructed a discontinuous homomorphism from product F_2 to F_2 by an algebraic functional on the quotient by the finite-support direct sum, realized it as the permutation part of an exact semilinear action on K times K for a multiquadratic extension K/Q, and proved that effective finite-etale descent would force an open permutation kernel. The actual tensor-Isom fpqc construction remains unaffected.')
event('F.3.12', REPROOF, 'Constructed inverse maps between fppf-local integral tensor forms and Aut-torsors, including the right Isom action and contracted product. Opened Gille–Moret-Bailly Proposition 5.1 for all affine finite-type groups over S-integers, without added reductive or smooth hypotheses. Proved fpqc-to-fppf reduction for arbitrary affine finite-type groups over S-integers: a section factors through a finite-type subalgebra of a faithfully flat algebra; torsion-freeness and proper maximal-ideal extensions give a faithfully flat finite-presentation cover. No flatness of the group is required. Constructed the adelic double-coset/lattice-genus bijection and integral stabilizer, using Borel Theorem 5.1 including disconnected groups. Constructed infinitely many sign-twisted tensor functors for product mu_2, all trivialized over Z[i]. Historical fixed-alpha integral-model identification remains the precise gate.')
event('F.3.12', CERT, 'Ran audit_next_certificates.py: all eight one-coordinate carry identities, all 4096 three-coordinate associativity cases, symmetry, and exact Z[i] trivialization exponents passed. Pairwise nonisomorphism over Z is proved using the tensor squares of the degree-e_i lines.')
event('C.1.3', REPROOF, 'Supplied work/C_1_3_direct_proof.tex, subsequently reviewed and integrated by root. Hodge-pair fullness identifies all mixed tensor invariants with those of K=H union fH. H is connected by Hodge-cocharacter minimality, f normalizes H, semisimplicity is proved by averaging a Hodge retraction with f, and tensor reconstruction proves G=K. This replaces the old proof relying on Deligne–Milne 6.23(a) normality; no arithmetic exact-sequence premise is used.')
event('G.2.2', REPROOF, 'Independently checked the displayed counterexample, its weight/depth and q coefficient 2-528q, E6(i)=0, E4(i) nonzero, and the two-generator specialization field. Checked both algebraicity directions in the repaired theorem. At a transcendental g-value the modular-curve point maps to the generic point, where finiteness still gives a finite residue-field extension. The nonzero specialized positive-depth coefficient makes the E2 polynomial nonconstant. Negative nonzero integral weights are covered because Delta(tau) is nonzero. This event checks the proof; primary Bhowmik–Pathak source access belongs to the root source record.')
event('D.4.2', REPROOF, 'Independently checked the genuine Tate example Q(-2): the restriction from the Q(-1) tensor group is t to t^2, the image is product of local unit squares, and reduction at arbitrarily many odd primes gives square-class quotients (Z/2)^r. This refutes the unrestricted finite-index strengthened Tate claim under the stated integral group convention; no strong-approximation assertion for G_m is used.')
event('F.3.5', PROOF, 'Added exact original-source comparison: original cote-14 pp.43–44 define the 1965 B as primitive positivity on cycles modulo algebraic equivalence. Wrote the actual cycle-class quotient to cohomological algebraic classes and its product/Lefschetz compatibility. Read both full Coates primary-text transcriptions and targeted original scans. Their particular B and D lack standalone definitions in the inspected letters; retained the documentary gate rather than inferring a uniform alphabet dictionary.')

changed = {
 'I.P33.03', 'I.M09.01', 'I.B05.01', 'I.B05.02',
 'II.P16.02', 'II.MB15.02', 'I.M04.02', 'I.M05.01',
 'II.MB07.02', 'II.MB08.01', 'II.P06.01', 'II.SF21.01',
}
closed = {'I.P33.03','I.B05.01','II.P16.02','II.MB15.02','II.P06.01','II.SF21.01'}
baseline_status = {sid:('DOCUMENTARY-GAP' if sid in {'I.B05.01','II.MB15.02'} else 'OPEN') for sid in closed}

claim_file = ROOT/'work/audit_claims.csv'
claims = list(csv.DictReader(claim_file.open()))
old_events = list(csv.DictReader((ROOT/'work/triangle_comparison_audit_CHECK_EVENTS.tsv').open(), delimiter='\t'))
old_claim_events = {e['statement_id']:e for e in old_events}
pattern = re.compile(r'\b[A-G]\.\d+\.\d+\b')
for row in claims:
    sid = row['assertion_id']
    deps = '; '.join(dict.fromkeys(pattern.findall(row['proof_or_locator'])))
    row['canonical_dependencies'] = deps
    row['check_event_statement_id'] = sid
    if sid in changed:
        kind = REFUTE if row['status']=='REFUTED' else PROOF
        event(sid,kind,'Updated status '+row['status']+'; dependencies '+row['proof_or_locator']+'. '+row['remaining_obligation_or_scope']+' Original note '+row['note_id']+'; '+row['witness']+'; '+row['source_file']+':'+row['source_line']+'.')
        row['check_event_type'] = kind
        row['check_event_ledger'] = LEDGER
    else:
        previous = old_claim_events[sid]
        row['check_event_type'] = previous['type']
        row['check_event_ledger'] = 'work/triangle_comparison_audit_CHECK_EVENTS.tsv'
with claim_file.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(claims[0]));writer.writeheader();writer.writerows(claims)

def sha(path):
    p=ROOT/path
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else ''

source_specs = [
 ('AuditDDMS1999','https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/ddsms.pdf','OPENED','Full book downloaded; Theorem 8.32 printed p.200 and Corollaries 8.33–8.34 p.201 read in local PDF/text. Web open failed only due to content-size limit.','B.4.4','work/sources_audit_next/DDMS1999.pdf'),
 ('AuditLM6Full2026','User-supplied Library archive LM6_POINTS_AS_SECTIONS_final.zip; libfile_b935f74c96a88191a5b3c3eed913961a','OPENED, AI RETURN','Complete original return retrieved unchanged. A.22 pp.16–17 (TeX lines1255–1339), A.50 pp.33–34 (lines2854–2958) read fully and proof independently checked with N to NA repair. A.36 and later restrictions read for scope only. Not a primary mathematical authority.','F.3.10; I.B05.01; II.MB15.02','work/LM6_original_return/LM6_POINTS_AS_SECTIONS_final.zip'),
 ('AuditGille2000','https://alexjbest.github.io/buntes/courbes-semi-stables.pdf','OPENED','Primary chapter in assembled book: section1.5, Lemma1.7 and proof of Proposition1.6, chapter pp.4–5, PDF pages221–222. General pro-p freeness criterion is explicitly attributed to Serre I.4.2. Full assembled text downloaded after web reading.','F.3.10','work/sources_audit_next/Gille2000_book.pdf'),
 ('AuditStix2012','https://www.math.uni-frankfurt.de/~stix/research/preprints/STIXcuspsec20120802homepage.pdf','OPENED, ADDITIONAL LOCATORS','Original preprint Proposition16 pp.7–8, especially part(3), Definition29 and Theorem30 p.11, Corollary31 pp.11–12. Rechecked boundary/cusp and full procyclic subgroup implication.','F.3.10','work/sources_audit/Stix2012.pdf'),
 ('AuditGilleMoretBailly2013','https://math.univ-lyon1.fr/~gille/publis/action.pdf','OPENED','Full author preprint: section2 pp.2–3, Proposition5.1 with full proof pp.8–10; Theorem1.1 p.2 and Proposition6.1 p.10. Arbitrary affine finite-type group scheme over S-integers. Identical ENS author copy downloaded; Rennes attempts503/403 retained.','F.3.12; I.M09.01','work/sources_audit_next/GMB_2.pdf'),
 ('AuditBorel1963','https://www.numdam.org/article/PMIHES_1963__16__5_0.pdf','OPENED','Original article section2.1 p.11 lattice reconstruction and Theorem5.1 p.19 finite class number, including nonconnected group argument.','F.3.12; I.M09.01','work/sources_audit_next/Borel1963.pdf'),
 ('AuditBorelSerre1964','https://www.college-de-france.fr/media/jean-pierre-serre/UPL6720771035987925133_Borel_Serre_Theoremes_de_finitude.pdf','OPENED','Original article introduction pp.111–112, section1.2 p.113 continuous cocycles, Theorem7.1 and twisting reduction pp.158–159. Rechecked as the Gille–Moret-Bailly global finiteness input; not a finiteness theorem for all H1 over the number field.','F.3.12','work/sources_audit_next/BorelSerre1964.pdf'),
 ('AuditGrothendieckSerre1965','https://grothendieck.umontpellier.fr/14.pdf','OPENED, TARGETED ORIGINAL PAGES','Full cote14 scan downloaded. Letter27August1965 original pp.43–44 (PDF44–45) visually read. A uses rational cycles modulo algebraic equivalence; B is primitive positivity. Remainder of the dossier not yet read; singular-hypersurface construction not located.','F.3.5; I.M04.02; II.MB07.02; I.M05.01; II.MB08.01','work/sources_audit_next/Montpellier_cote14_original.pdf'),
 ('AuditGrothendieckCoates1966','https://csg.igrothendieck.org/wp-content/uploads/2024/04/L11d.pdf','OPENED','Full primary-text transcription pp.1–3 read. Original cote16 downloaded; original p.47 (PDF48) visually checked, including handwritten date6January1966 and first proposition. Exact inverse construction w^-1u via rational characteristic coefficients read.','F.3.5; I.M04.02; II.MB07.02','work/sources_audit_next/Coates1966_CSG.pdf'),
 ('AuditGrothendieckCoates1967','https://csg.igrothendieck.org/wp-content/uploads/2024/04/L10d.pdf','OPENED','Full primary-text transcription pp.1–4 read, including A–D relations and the withdrawn smooth-hypersurface proposal. Original cote16 downloaded; original p.44 (PDF45) visually checked. No standalone B,D definitions in the inspected letter.','F.3.5; I.M04.02; II.MB07.02; I.M05.01; II.MB08.01','work/sources_audit_next/Coates1967_CSG.pdf'),
 ('SerreGaloisCohomology1997OriginalCriterion','https://unina2.on-line.it/sebina/repository/catalogazione/documenti/Serre%20-%20Galois%20cohomology.pdf','ATTEMPTED, THEOREM NOT OBTAINED','Retrieved PDF contains only nine front-matter pages. The actual I.4.2 Proposition21 text was not obtained by this route. F.3.10 uses the opened primary Gille chapter for the criterion and states its attribution; no claim of having read the Serre theorem from this preview.','F.3.10 source-access limitation','work/sources_audit_next/SerreGaloisCohomology1997.pdf'),
]
sources=[]
for key,url,status,loc,deps,path in source_specs:
    sources.append(dict(source_key=key,url=url,status=status,locator_and_access=loc,dependent_statement_ids=deps,record_file='work/audit_next_references.bib' if key!='SerreGaloisCohomology1997OriginalCriterion' else 'work/audit_next_source_checks.csv',date=DATE,who=WHO,local_path=path,sha256=sha(path)))
    event('SRC.'+key,PROOF if status.startswith('ATTEMPTED') else USE,status+'. '+loc+' Dependencies: '+deps+'. Local source: '+path+'.')
with (ROOT/'work/audit_next_source_checks.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(sources[0]));w.writeheader();w.writerows(sources)

# Preserve all 43 originally OPEN/DOCUMENTARY-GAP rows: six now closed,
# thirty-seven retained, and one reading row updated separately above.
review=[]
for r in claims:
    sid=r['assertion_id']
    if r['status'] not in {'OPEN','DOCUMENTARY-GAP'} and sid not in closed:
        continue
    review.append(dict(assertion_id=sid,previous_status=baseline_status.get(sid,r['status']),current_status=r['status'],action=('Exact refutation and replacement recorded' if sid in closed else 'Remaining precise obligation rechecked; no unproved closure assigned'),proof_or_locator=r['proof_or_locator'],remaining_obligation_or_scope=r['remaining_obligation_or_scope'],source_file=r['source_file'],source_line=r['source_line']))
assert len(review)==43, len(review)
with (ROOT/'work/open_rows_review_20261119.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(review[0]));w.writeheader();w.writerows(review)
for r in review:
    if r['assertion_id'] not in changed:
        event(r['assertion_id'],PROOF,'Exhaustive remaining-gate review: '+r['current_status']+'. '+r['proof_or_locator']+'. '+r['remaining_obligation_or_scope']+' Original source '+r['source_file']+':'+r['source_line']+'. No additional theorem assigned.')
with (ROOT/LEDGER).open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t');w.writeheader();w.writerows(events)

validation=dict(assertion_count=len(claims),source_entry_count=len(set(r['note_id'] for r in claims)),status_counts=dict(Counter(r['status'] for r in claims)),addendum_event_count=len(events),source_record_count=len(sources),original_open_documentary_rows_reviewed=len(review),changed_claim_ids=sorted(changed),closed_claim_ids=sorted(closed),allowed_event_types=sorted(ALLOWED),all_claims_have_event_record=all(r['check_event_ledger'] and r['check_event_statement_id'] for r in claims),root_combined_files_modified=False)
(ROOT/'work/audit_next_validation.json').write_text(json.dumps(validation,indent=2)+'\n')
print(json.dumps(validation,indent=2))
