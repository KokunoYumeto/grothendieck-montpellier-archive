import csv
import json
from pathlib import Path

UTC='2026-11-21 22:47:47 UTC'
p=Path('work/review_status.json'); d=json.loads(p.read_text())
entries=[
('NN-S016','/root/complexity; /root','PASS; complete combined proof read',
 'The complexity track read every line of the combined Chow, cycle-class, topology, integral degree/height, every-field and stabilization proof at22:45:05UTC. Root separately read the entire topology and degree addenda, checked the Chow argument and primary source interfaces, and added the explicit any-algebraically-closed-field sheaf-calculation clarification.',
 'Jointly authored proof; this is a targeted whole-proof reading, not an independent re-proof of the reviewer-authored portions. No formal verification or general affine-space recognition algorithm is claimed.',
 'work/root/chapter8.tex; work/complexity/c027_topology_addendum.tex; work/complexity/c027_degree_addendum.tex; complexity reviewer message22:45:05UTC'),
('NN-C029','/root','PASS; complete proof and homogeneous-component refinement read',
 'Read all preliminary partition circuits, factor-density and scope bounds, coefficient-independent E unrolling, local eight-specialization Boolean-ideal correction, integral ordinary identity, degree and height control, sparse-CNF first-violation specialization, IPS interpretation, homogeneous-component truncation and explicit affine isomorphism/inverse.',
 'Targeted proof reading, not a formal verification or independent re-proof. Rational circuit syntax is distinguished from integral output polynomials and from fixed-characteristic or constant-free circuits. General supplied IPS verification still needs PIT.',
 'work/complexity/c029_draft.py; NN-C016 reread; primary E and Grochow-Pitassi interfaces checked separately'),
('NN-G029','/root','PASS; complete proof including sparse-anchor NP corollary read',
 'Read the pointed homogenized-cone decomposition, lower-dimensional active-row arguments, Cramer/cofactor bounds, primitive ray selection, conic elimination and integer flooring; checked all exponent collision/order constraints and fixed trace anchors. Reread the complete sparse-anchor revision, unary-mass witness bit bounds, rank bound and exact sparse associativity verification.',
 'Targeted proof reading, not formal verification or a numerical solution of the unrestricted optimum. The cutoff is existence-preserving; it does not bound every existing degree. NP membership uses unary or polynomially bounded total mass.',
 'work/gct/g029_insert.tex; work/gct/verify_degree_cutoff_constants.py'),
('NN-A029','/root','PASS; complete exact-asymptotic proof read, with distinct-spectrum clarification reread',
 'Read the Gaussian/Helmholtz positivity-radius argument, harmonic leading-term strictness, compact uniform Weyl-HCIZ control of every partition, sector lower radius bound, explicit m=2/3 formulas, coalescent-prefix and infinite-tail error estimates, attainment of endpoint minima and both sharp liminf/limsup arguments. Reread the distinct-spectrum perturbation and exact positive reference scale corrections.',
 'Targeted full-proof reading, not formal verification or an independent re-proof. Actual endpoint multiplicities remain unknown; higher-m orbital radii have exact variational definitions but no asserted closed forms.',
 'work/analytic/orbital_detection_constants.tex; NN-A022/NN-A028; primary Zuber normalization')]
for fid,who,outcome,scope,limits,evidence in entries:
    d[fid]=dict(date_utc=UTC,who=who,model='GPT-6 Astra Pro',effort='not exposed by runtime',type='targeted proof check',outcome=outcome,scope_and_method=scope,limitations=limits,evidence=evidence)
p.write_text(json.dumps(d,indent=2)+'\n')
p=Path('work/root/CHECK_EVENTS.tsv')
with p.open() as f: fields=next(csv.reader(f,delimiter='\t'))
rows=[]
def event(fid,kind,outcome,scope,evidence,limits):
    rows.append(dict(statement_id=fid,date_utc=UTC,who='/root',model='GPT-6 Astra Pro',effort='not exposed by runtime',type=kind,outcome=outcome,scope_and_method=scope,limitations=limits,evidence=evidence))
event('NN-G029','computation or formal certificate','PASS: anchors1..5, mass11147, n5578 and degree bound<2^11170', 'Read every line and reran the updated sparse-anchor constants script. It reads the independently checked3352 table certificate, recomputes trace norm, actual dimension mass and the integer power bound.', 'work/gct/degree_cutoff_certificate.json', 'Numerical input audit only; no exhaustive optimization search or mechanical proof of the polyhedral lemma.')
event('NN-C027-fixed-modulus','targeted proof check','PASS: modular counting equivalence and higher p-adic digit extraction', 'Read the complete new paragraph: invertible p^h modulo a fixed modulus, both reductions, vanishing low digits when the characteristic divides the modulus, and exact quotient extraction from higher precision.', 'work/complexity/c027_draft.py fixed-modulus paragraph', 'A targeted addendum reading, separate from the earlier complete C027 proof review. No convention-dependent Mod_mP classification is asserted.')
event('Grochow-Pitassi-IPS-Def1.1-Lem4.2','used and rechecked in this run','PASS: primary definition and complete first-violation certificate proof', 'Opened the author manuscript and read Definition1.1, printed draftp1:4, and the complete Lemma4.2 proof with equations4-6, printed draftpp1:26-1:28. It explicitly dispenses with Boolean axioms in the clause-polynomial identity.', 'https://www.cs.toronto.edu/~toni/Papers/jacm-gp.pdf; work/complexity/grochow_pitassi_author.txt', 'The classical identity is credited as background; the new deduction is its E circuit-size bound and local verifier-ideal lift. Draft pagination is not presented as final journal pagination.')
with p.open('a',newline='') as f: csv.DictWriter(f,fieldnames=fields,delimiter='\t').writerows(rows)
print('Recorded',len(d),'whole-proof review records and',len(rows),'separate events.')
