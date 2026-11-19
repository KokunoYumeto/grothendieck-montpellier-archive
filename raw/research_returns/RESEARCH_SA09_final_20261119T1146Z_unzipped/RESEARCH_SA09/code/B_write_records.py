"""Create statement and check-event fragments for integration by the root agent."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import csv

root=Path(__file__).resolve().parents[1]
date=datetime.now(ZoneInfo('Europe/Berlin')).isoformat(timespec='seconds')
who='GPT-6 Astra (OpenAI; ChatGPT Pro mode); effort inherited/not exposed; run /root/b1_b2_b3'
rows=[
 ('B0.1','Permutation, covering and Belyi correspondence; automorphisms are monodromy centralizers','Known','Schneps Lemma I.1 and Theorem I.5; Jones Theorem 1 and Sections 2-3','','138:98-99,106','Opened sources; target 0,1,infinity fixed.'),
 ('B1.1','Pinned-map count = |Gamma_T| sum_C |K_C|/|Aut C|; naive count iff all induced images on Fac are trivial','Proved','sections/B1_B2_B3.tex, B1.1','','138:98-100','All finite types, with or without connectedness; degree 0 and 1 specified; rigidity is a separate condition.'),
 ('B1.2','Pinned-map rigidity is false: torus datum E=Z/4, rho=+1, alpha=+2 has pinned C2 and only one pinned class','Refuted','sections/B1_B2_B3.tex, B1.2','B1.1','138:99-100','Correct replacement B1.1; exhaustive 24-permutation check.'),
 ('B1.3','The connected cellwise combinatorial kernel is C2 exactly for opposite-paired one-vertex one-face bouquets with 2g edges; otherwise trivial','Proved','sections/B1_B2_B3.tex, B1.3','','138:98-100,129-131','Full all-degree proof; includes half-edges.'),
 ('B2.1','Raw remainder P=-delta*p/7776 is quintic; effective cubic p=25c^3-12c^2-24c-16; explicit Q and factorization','Proved','sections/B1_B2_B3.tex, B2.1','','138:107-112','Exact rational polynomial certificate; all intermediate signs supplied.'),
 ('B2.2','All three Belyi functions are 1500*z^3*(z-1)^2*(z-c)/(32-52c-c^2), p(c)=0; each has trivial automorphisms','Proved','sections/B1_B2_B3.tex, B2.2','B0.1;B2.1','138:106-112','Completeness by unique normalization; every degeneration excluded algebraically.'),
 ('B2.3','Three combinatorial maps represented by rho=(123)(45), alpha=(14)(36),(14)(56),(14)(26); one real and a mirror pair','Proved','sections/B1_B2_B3.tex, B2.3','B2.2','138:106','All 5400 ordered pairs tested; 2160 admissible; 3 orbits of size 720.'),
 ('B2.4','Fields of moduli and definition Q(c)=Q(r), r^3=2; one S3 Galois orbit; normal closure Q(cuberoot(2),zeta_3)','Proved','sections/B1_B2_B3.tex, B2.4','B2.1;B2.2;B2.3','138:106-112','L5 orbit assertion true; raw P must be saturated by delta. Matching cubic already in Schneps IV Example 3.'),
 ('B2.5','Delta roots are 16/25 +/-12i/25 and are roots of raw P; their passport is [3,2,1;3,1,1,1;6]; doubtful signs corrected','Refuted','sections/B1_B2_B3.tex, B2.5','B2.1;B2.2','138:108-112','Corrects incorrect imaginary part and answers scan112 collision question affirmatively.'),
 ('B3.1','Complete finite clean holomorphic cellwise stabilizer list: Aff+(R) for one-loop sphere; R>0 for all oranges; C2 for opposite bouquets; trivial otherwise','Proved','sections/B1_B2_B3.tex, B3.1','B0.1;B1.3;Wendl Corollary 4.2.7','138:129-131','Connected compact theorem; disconnected answer is componentwise product.'),
 ('B3.2','Explicit clean orange models and hyperelliptic bouquet models; orange rigidity and complex-group readings are false','Proved','sections/B1_B2_B3.tex, B3.2','B3.1','138:130-131','b_n=-4z^n/(z^n-1)^2; X_g:y^2=x^(2g+1)-x, beta=x^(2g).'),
 ('B3.3','Belyi-function nonuniqueness is parametrized by the dartwise kernel; only sphere exceptions; cellwise preservation is not isotopy to identity','Proved','sections/B1_B2_B3.tex, B3.3','B3.1;B3.2','138:129-131','Torus involution acts -1 on H1; face centres kill continuous exceptions, not the already-deck C2.'),
 ('B3.4','Every cellwise holomorphic automorphism of a noncompact locally finite clean cellular map with compact ordinary cell attachments is identity','Proved under stated hypotheses','sections/B1_B2_B3.tex, B3.4','B1.3;B3.1;Wendl Theorem 4.2.1','138:131','Additional infinite-map extension; all compact maps in B3.1 satisfy its local finiteness hypotheses.'),
]
with (root/'notes/B_results.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['id','statement','status','where_proved','depends_on','manuscript_pages','notes']);w.writerows(rows)
events=[]
def add(statement,typ,outcome):events.append([statement,date,who,typ,outcome])
for row in rows:
    add(row[0],'used and rechecked in this run' if row[2]=='Known' else 'targeted proof check',
        'Passed: '+row[1]+'. '+row[6])
for sid in ['B1.2','B2.1','B2.2','B2.3','B2.4','B2.5','B3.2']:
    add(sid,'computation or formal certificate','Passed exact assertions in code/B1_B2_B3_certificate.py; scope and runtime in logs/B1_B2_B3_certificate.txt. Finite checks do not replace the general proofs.')
add('SA09-16 (138:98-100)','independent re-proof','Re-derived orbit formula and all torus groups; confirms nonrigidity. Exact criterion for manuscript count is trivial image on Fac, distinct from trivial pinned kernel.')
add('SA09-16 (138:99)','refuted, with the refined statement B1.1','Rigidity and naive multiplication fail; fully specified torus counterexample B1.2 verified by exact enumeration.')
add('SA09-17 (138:106)','computation or formal certificate','Complete S6 enumeration confirms 2160 admissible pairs / 3 orbits; two manuscript tables plus mirror. Table II rho(r5)=r4.')
add('SA09-17 (138:107-112)','independent re-proof','Re-derived derivative, P,Q, all doubtful intermediate signs, factorization, excluded critical collisions, and complete moduli fields.')
add('SA09-17 (138:111)','refuted, with the refined statement B2.5','Imaginary part 24/25 is false; exact roots 16/25 +/-12i/25.')
add('SA09-18 (138:130-131)','independent re-proof','Positive dilations preserve every orange; correct I/II/III groups are Aff+(R), R>0, R>0. Complete compact exception list proved in B3.1.')
add('SA09-18 (138:129)','refuted, with the refined statement B3.3','Fixing vertices/edges/faces is not equivalent to isotopy to identity: torus hyperelliptic involution acts -1 on H1.')
add('R8','used and rechecked in this run','Confirmed with fully specified 4-dart certificate and corrected count B1.1.')
add('R9','refuted, with the refined statement B2.1','Three maps and corrected delta roots confirmed. Calling the literal remainder coefficient P cubic is false: P=-delta*p/7776 is quintic; p is the effective cubic.')
add('R10','used and rechecked in this run','Confirmed and strengthened to full compact clean classification B3.1; finite C2 cellwise exceptions separated from function nonuniqueness.')
add('L5','independent re-proof','Orbit and cubic moduli-field assertions proved in B2.4. Raw P is not cubic and its delta factor must be removed; corrected equation p(c)=0.')
add('A1.4','independent re-proof','Confirmed arbitrary-module tensor-presentation formula and coefficient comparison, including degree zero; no Hom base-change assumption. See notes/B_peer_review_A1.md.')
add('A1.7','independent re-proof','Found and repaired a missing repeated-degree/off-diagonal strictness proof. Rechecked final full-map N and D multigrading criterion, typed counits and all bounds: passed. See notes/B_peer_review_A1.md.')
with (root/'notes/B_CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(events)
print('Wrote',len(rows),'statement records and',len(events),'check events at',date)
