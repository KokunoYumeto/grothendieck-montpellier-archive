"""Record actual complete proof readings and source-interface checks."""
import csv
import json
from pathlib import Path

base = Path(__file__).resolve().parent
path = base / 'review_status.json'
reviews = json.loads(path.read_text())

def review(fid, date, scope, evidence, who='/root'):
    reviews[fid] = dict(date_utc=date, who=who, model='GPT-6 Astra Pro',
        effort='not exposed by runtime', type='targeted proof check',
        outcome='PASS; complete deduction proof read', scope_and_method=scope,
        limitations='Targeted whole-proof reading, not independent re-proof or formal verification. Imported classical interfaces have separate source scope.',
        evidence=evidence)

review('NN-A033', '2026-11-21 23:28:23 UTC',
    'Read every line of the full central-order certificate. Checked paired Hadamard factorization, arbitrary off-line quartet positivity, absolute convergence, Euler logarithmic derivative signs, archimedean constants, every written rational inequality, mod-four multiplicity forcing and the conjugation/parity argument yielding the real O(t^2) remainder and strictly positive velocity. Freshly read primary completion/order/functional-equation statements in Hasanalizade-Shen-Wong section2.1.',
    'work/analytic/central_order_certificate.tex; Hasanalizade-Shen-Wong2022 equations2.1-2.2 p279')
review('NN-C033', '2026-11-21 23:29:14 UTC',
    'Read entire c033_draft.py, all finite checker code and the relevant full E measurement/Taylor/swap proofs. Checked integral generating series, exact integer fibers without reduced-kernel substitution, deterministic finite-field construction, ring-valued Boolean differences, Hasse CRT with arbitrary jet order, coefficient-algebra identities, coordinate descent, ordinary ideal multipliers/maps and constant-free formal-degree processing. Reran the finite checker separately.',
    'work/complexity/c033_draft.py; sources/LIT_OpenAI_ETH_is_False/main_full_version.tex Lemmas3.2/3.3/4.1-4.3 and Proposition3.4; work/complexity/finite_checks_small_characteristic.py')
review('NN-S018', '2026-11-21 23:32:10 UTC',
    'Read complete chapter10 and checked the review returned by /root/gct, who also fully read S017. Checked null reduced diagonal, primitive Bott pullback, Adams action, torsion-free Newton identities, Stirling recurrence, gcd filtration, odd-v order-two quotient and parsimonious padding. Applied reviewer wording corrections and freshly verified Riou Theorems1.1.2/2.3.1, Proposition2.3.2 and section2.4 for the integral unstable lambda-operation interface.',
    'work/root/chapter10.tex; /root/gct whole-proof review; Riou0907.2710v2 printedpp4,10-11')
path.write_text(json.dumps(reviews, ensure_ascii=False, indent=2)+'\n')

events_path = base / 'root/CHECK_EVENTS.tsv'
with events_path.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t'); fields=reader.fieldnames; rows=list(reader)

def event(fid, date, typ, outcome, scope, limitations, evidence, who='/root'):
    record=dict(statement_id=fid,date_utc=date,who=who,model='GPT-6 Astra Pro',
        effort='not exposed by runtime',type=typ,outcome=outcome,
        scope_and_method=scope,limitations=limitations,evidence=evidence)
    if not any(r.get('statement_id')==fid and r.get('date_utc')==date and r.get('type')==typ for r in rows): rows.append(record)

event('NN-C033', '2026-11-21 23:29:14 UTC', 'computation or formal certificate',
    'PASS156 integral parameter cases;61488 coefficient comparisons;9230 eigenvector identities;14784 F8 integer-fiber comparisons;36 Hasse-CRT basis recoveries',
    'Read full checker and reran it; jet orders2,3,4 explicitly include orders at least the characteristic.',
    'Finite arithmetic computations only; not formal verification or a proof of the asymptotic algorithm.',
    'work/complexity/finite_checks_small_characteristic.py; work/complexity/FINITE_CHECK_SMALL_CHARACTERISTIC_RESULTS.json')
event('NN-A032-unconditional-refinement', '2026-11-21 23:32:10 UTC', 'targeted proof check',
    'PASS; complete added argument and revised theorem read',
    'Read the unconditional paired logarithmic-derivative paragraph and surrounding theorem. Checked absolute convergence and positivity of the real parts of inverse quadratic denominators for all strip zeros; strictness uses infinitely many noncentral zeros. A remains explicitly necessary for the asserted positive leading coefficient and branch counts.',
    'Does not assert any real quadratic central zero exists or remove A from the leading-coefficient conclusion.',
    'work/analytic/central_dirichlet_sign.tex; NN-A033 paired Hadamard argument')
event('Riou0907.2710v2-Th1.1.2-Th2.3.1-Prop2.3.2', '2026-11-21 23:32:10 UTC',
    'used and rechecked in this run', 'PASS exact unstable special-lambda-ring interface',
    'Read regular-base conventions, Theorems1.1.2 and1.1.4, full short proof of Theorem2.3.1 and Proposition2.3.2, and opening of section2.4. This gives integral operations on K0 of arbitrary motivic spaces and their naturality under the sphere equivalence and regular base change.',
    'Theorem1.1.4 is imported; its entire antecedent proof was not independently reproduced.',
    'https://www.imo.universite-paris-saclay.fr/~joel.riou/doc/operations.pdf; arXiv0907.2710v2 printedpp3-4,10-11; NN-S018')
event('PPR-BGL-20070417;SGA6-gamma-projective-bundle', '2026-11-21 23:32:10 UTC',
    'used and rechecked in this run', 'PASS exact representability/Bott/gamma interfaces',
    'Recorded retrospectively after primary reads in this run: PPR regular-base conventions and Lemma1.2.6,Corollaries1.2.7-1.2.8,Lemmas1.3.2-1.3.3,Proposition1.3.5; Schlichting-Tripathi introductioneq1.1 ordinary K-theory; SGA6 V3.2(ii),3.10.1 and VI1.1. Ordinary K-theory here imposes no invertibility-of-two hypothesis.',
    'Primary statements and the short relevant Bott proofs were read; no independent proof of K-theory representability or scanned-page claim for the SGA transcription.',
    'https://www.math.uni-bielefeld.de/lag/man/251.pdf; https://grothendiecksga.com/read/sga6/fr/V-3.html; https://grothendiecksga.com/read/sga6/fr/VI-1.html; NN-S018')
event('MVW-13.17-15.2-15.5-16.26-19.1', '2026-11-21 23:32:10 UTC',
    'used and rechecked in this run', 'PASS precise perfect-field motive/higher-Chow interface',
    'Recorded retrospectively after exact primary reads in this run: Example13.17,Theorem15.2,Corollary15.5,Remark16.26 and Theorem19.1. Remark16.26 supplies cancellation over perfect fields; no resolution hypothesis is silently transferred from Theorem16.25. Example13.17 is correctly labeled Example.',
    'Classical motive and higher-Chow theorems are imported; not an independent proof of the book.',
    'Mazza-Voevodsky-Weibel,Lecture notes on motivic cohomology; NN-S017')
event('HSW2022-eq2.1-2.2', '2026-11-21 23:28:23 UTC',
    'used and rechecked in this run', 'PASS exact Dedekind completion, entire order and functional equation',
    'Freshly opened publisher offprint and read section2.1 equations2.1-2.2 printedp279. Checked gamma convention differs from A033 by constant2^r2, which leaves logarithmic derivatives unchanged.',
    'The classical analytic statements are imported; no independent re-proof of their full analytic continuation theorem.',
    'https://www-math.nsysu.edu.tw/~pjwong/stuff/DedekindZeros.pdf; NN-A033')

with events_path.open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t');writer.writeheader();writer.writerows(rows)
print('Root review map:',len(reviews),'Root check events:',len(rows))
