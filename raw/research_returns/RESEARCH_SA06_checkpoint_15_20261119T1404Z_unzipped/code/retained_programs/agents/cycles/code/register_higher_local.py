"""Register the audited ordinary codimension-two local counterexample."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import time

started=time.perf_counter()
base=Path(__file__).resolve().parents[1]
columns=['id','statement','status','where_proved','depends_on','manuscript_pages_settled','notes']
row=['C.3ae',
     'For every complex local dimension N>=7 the ordinary codimension-two restriction cokernel can surject integrally onto the Picard variety of the Fermat quartic',
     'Refuted, with an explicit counterexample',
     'higher_local_surjectivity.tex, paragraph C.3ae',
     'C.3m construction; C.3e localization/self-intersection; Stacks42.58.1 Tag0FEY and42.59.9 Tag0FF8; conormal exterior sequence; exact quartic matrix and basepoint certificates',
     '14:107-112',
     'Actual fixed-product algebraic equivalence, integral and rational coefficients. The exact four integer matrices define every local pair. Cokernel maps onto Pic0(C); theta maps back with rho theta=-9. N5 was refuted in C3r; N<=3 has zero codim2 target; N4 and N6 remain undecided. The withdrawn unrestricted-CH scalar-spread route is retained in the event ledger. No novelty claim.']
with (base/'higher_local_results.csv').open('w',newline='') as f:
    w=csv.writer(f); w.writerow(columns); w.writerow(row)
who='GPT-6 Astra (OpenAI); inherited parent reasoning effort; /root/cycles'
frob='GPT-6 Astra (OpenAI); inherited parent reasoning effort; /root/frobenius'
root='GPT-6 Astra (OpenAI); inherited parent reasoning effort; /root'
events=[
 (who,'used and rechecked in this run','Read C3m construction and full proper-family argument; rechecked normalization, integral graph hypersurface, scheme-theoretic exceptional fibre, strict henselization, regular puncture and strict transform for the extra quartic factor.'),
 (who,'failed route and correction','Withdrew an attempted unrestricted-CH argument by spreading a generic-point preimage: finite pointed etale neighbourhoods can vary over the parameter, and their class on an open first neighbourhood need not extend over the proper parameter. H1 on an affine open loses the intended obstruction. No unrestricted-CH conclusion is retained.'),
 (who,'targeted proof check','Repaired the scope using actual ordinary algebraic-equivalence families on fixed X times a curve, compactified before taking closure on the fixed regular model. No interchange of strict henselization with scalar extension is used.'),
 (who,'computation or formal certificate','Constructed the exact64x57 integer obstruction matrix in dual Jacobian-ring bases. Rank57 modulo101 found at the first deterministic coefficient tuple, runtime0.04868981899926439 seconds; all coefficient and monomial data retained.'),
 (who,'computation or formal certificate','All12 charts of W times C have unit ideal for the two quartic equations and four fixed bilinear sections modulo101. Grevlex Groebner calculation runtime4.204962002000684 seconds. Properness over Z promotes the empty geometric finite-field fibre to the empty characteristic-zero generic fibre.'),
 (root,'independent computation or formal certificate','Independent DomainMatrix reconstruction proves the determinant of the first57 rows is47 modulo101. Runtime0.214309928 seconds. Root also read the full basepoint certificate and proper-image deduction.'),
 (frob,'independent computation or formal certificate','Independent column-based matrix assembly gives rank57, and independent lex Groebner bases are[1] in all12 charts for the same first tuple. Runtime4.596638515999075 seconds. Later check confirms first57-row minor47.'),
 (who,'targeted proof check','Defined sigma by localization and refined self-intersection, proved integral projective-bundle quotient for rank m>=3, and checked all fibre and transverse source-pullback compatibilities. The tau detector has tau H=0 and tau D=-9.'),
 (who,'used and rechecked in this run','Opened complete primary Stacks sections0FEX/0FEZ, then clicked exact Lemma42.58.1 Tag0FEY and Remark42.59.9 Tag0FF8; also read K-group/resolution sections0FDE/0FDD and explicit Hodge dlog in0FLE. The conormal Chern-character lift is proved directly.'),
 (who,'targeted proof check','Checked the full conormal wedge sequence relative to C, rational K0 lift, dual R4/R3 identifications, all Kunneth degrees, hyperplane annihilation and correction terms. Only ordinary families are killed; no semiregularity converse is assumed.'),
 (frob,'independent targeted proof and source check','Full typed proof passed at tool time08:53:01UTC, including sigma, Chern lift, Hodge projection, boundary terms, actual proper curves and integral cokernel. Review and separate canonical events are in agents/frobenius/C3ae_higher_local_surjectivity_independent_REVIEW.md and C3ae_quartic_certificate_independent_CHECK_EVENTS.tsv.'),
 (root,'independent targeted proof and source check','Root fully read the typed proof, reopened exact Tags0FEY/0FF8, and independently checked scheme construction, first neighbourhood, sigma, conormal lift, Hodge projection and proper families. Final PASS and integration authorization received before08:55UTC.'),
 (who,'computation or formal certificate','Supplementary exact symbolic check verifies line and point equations, Fermat gradients, curve boundary basis, Jacobian dimensions16/19, monomial spanning, tau H=0, tau D=-9 and dimension bookkeeping. Runtime0.05302022699834197 seconds; full code and JSON/stdout retained.'),
 (who,'typesetting verification','Standalone6-page four-pass LuaLaTeX/BibTeX check completed without diagnostics at08:52:21UTC, runtime2.952027564999298 seconds. Earlier missing display terminator and three prose overflows were repaired; logs retained. Root handles integrated visual QA.'),
 (who,'targeted proof check','Exact residual scope: codimension-two target is zero for N<=3; C3r refutes N5; this construction refutes every N>=7. N4 and N6 remain unproved for universal ordinary rational restriction surjectivity. No arbitrary-CH, characteristic-p or all-codimension extension inferred.')]
events.append((who,'literature scope check','Searched local Lefschetz, ordinary higher Chow restriction and infinitesimal obstruction. Opened full primary author PDFs of Patel-Ravindra Infinitesimal Lifting Theorem1.4 authorp3 and Infinitesimal Noether-Lefschetz Theorem7 authorp2; their introductions were read for precise smooth-projective/ample/formal scope. They are comparative sources, not inputs; no novelty claim made.'))
with (base/'higher_local_CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    w.writerow(['statement_id','date','who_model_effort_run','type','outcome'])
    for actor,kind,outcome in events:w.writerow(['C.3ae','2026-11-19',actor,kind,outcome])
record={'utc':datetime.now(timezone.utc).isoformat(),'rows':1,'events':len(events),'runtime_seconds':time.perf_counter()-started}
(base/'output/register_higher_local.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
