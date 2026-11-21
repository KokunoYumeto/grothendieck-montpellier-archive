from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import csv, json

base = Path(__file__).resolve().parents[2]
root = base / 'work/root'
checks = base / 'work/checks'
now = datetime.now(timezone.utc).isoformat()
fields = ['statement_id','date','who','model','effort','run','type','outcome']

def event(path, sid, kind, outcome):
    with path.open('a', newline='') as f:
        csv.writer(f, delimiter='\t').writerow([sid,now,'/root','GPT-6 Astra Pro','not exposed','GRH_NIGHT_20261121',kind,outcome])

proof = (root/'meyer_hecke_comparison.tex').read_text()
section = root/'section.tex'
assert 'MT-M22.' not in section.read_text()
section.write_text(section.read_text()+'\n'+proof)
rows = json.loads((root/'rows.json').read_text())
rows.append(dict(
 id='MT-M22',
 statement='For each fixed primitive unitary Hecke function, the canonical completed-function closed convolution quotient is isomorphic to its fixed compact-character sector in Meyer’s adelic summation zero-space, including the quotient Frechet topology, bounded/precompact bornology, convolution action and all multiplicities.',
 input='neither; Meyer2005 adelic image and embedding theorems plus MT-M18 unconditional synthesis and explicit continuous section; no GRH, simplicity or derivative hypothesis',
 status='proved here as an explicit comparison; the source spectral realization and trace theorem are classical, not claimed as new',
 where_the_proof_is='GRH_NIGHT.tex MT-M22; work/root/meyer_hecke_comparison.tex; Meyer math/0311468v3 Definition4.1/(22), Lemma5.4 and Section5.7 pp45–47',
 where_it_lives='Masullo arithmetic quotient comparison route; Tate Poisson summation, idele norm direction; cote1 and SA23 geo-H-lidskii/geo-H-genus; arbitrary draft or cohomological map remains separate'))
(root/'rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')

qp = root/'questions.tsv'
with qp.open(newline='') as f:
    reader=csv.DictReader(f,delimiter='\t'); qfields=reader.fieldnames; qs=list(reader)
for q in qs:
    if q['id']=='Q-MAS-INFINITE-BASIS':
        q['state']='proved canonical spectral synthesis, adapted absolute basis and nuclear/Hilbert trace unconditionally MT-M18/M19. MT-M21/M22 identify the quotient with Meyer over Q and every fixed Hecke sector, including topology and bornology. Prescribed individual jets retain exactly MT-M16 leading-coefficient gate. MT-M20 faithful positive Hilbert completion is iff GRH+simple. A particular full draft/cohomological map remains separately unproved.'
    if q['id']=='Q-MAS-LATTICE':
        q['state']='proved MT-M07/M08 for the lattice divisor. The distinct arithmetic-divisor synthesis and adapted trace construction are now proved unconditionally in MT-M18/M19 and identified with Meyer’s actual adelic quotient in MT-M21/M22.'
qs.append(dict(id='Q-MAS-MEYER-HECKE',source_and_locator='Meyer2005 math/0311468v3 Section5.7 pp45–47 and Lemma5.4; MT-M18; Masullo comparison route',question='Does the fixed-character adelic summation quotient equal the canonical full Hecke jet quotient with its actual topological and bornological structures?',state='proved MT-M22: explicit Euler-convention match, exact image/kernel equality, quotient Frechet topology, compact-character projection and continuous block section give bounded/precompact lifting. Constants may depend on the fixed character; no uniform all-character assertion.'))
with qp.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=qfields,delimiter='\t');w.writeheader();w.writerows(qs)

sources=json.loads((root/'sources.json').read_text())
for s in sources:
    if s['id']=='MEYER05-ID':
        s['locator']='Author version math/0311468v3, Definition4.1/(22)pp24–25; Theorem5.1pp38–39; Lemma5.4pp40–41; Theorem5.8pp43–44; Section5.7pp45–47, including Lemma5.10 and Theorem5.11'
        s['inspection']='Primary arXivv3 retrieved. Root and complexity read the full Section5.7 image argument, Lemma5.4 embedding proof, and Theorem5.11 short proof, with scope-specific checks of definitions, levels and character convention. Complexity inspected source images46–47. MT-M22 has complete author and root proof readings. No complete-paper audit claimed.'
        s['web_refs'] += ['turn979524474view1','turn340790906view2']
(root/'sources.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n')
event(root/'events.tsv','MT-M22','targeted proof check','Read the whole final proof including the added Arzela–Ascoli bounded/precompact argument. Checked inverse Euler coefficient convention, pure-norm twist, fixed character modulation, reflected Hecke factor, exact source image criterion, gamma and finite-Euler division, Poisson intersection, compact projection and continuous bounded lifting. No gap found; classical source realization not claimed as new.')
event(checks/'source_events.tsv','MEYER05-ID','used and rechecked in this run','Freshly read the whole Section5.7 image argument and Lemma5.4 proof from primary author text, including all conditions retained in M22. Kappa and inverse character checked in the new proof. Source Theorem5.11 proof read; no whole-paper certification.')

for sid,detail in [
 ('AG-THETA-NONINT','canonical reduced-theta convention, square-lattice e2*=0, formal logarithm, sigma coefficients, first nonintegral coefficient and persistence under integral units/parameter changes; not a refutation of A or the stated normalized derivative claim'),
 ('AG-CM-INTEGRAL-MODEL','KRY Proposition5.1 full proof and Cases1–2; level-three rigidification, degree48h/w, connected component, unramified base, simultaneous differential normalization and inert height'),
 ('AG-CM-MODEL-DEGREE','NT-H02 class-number factor, w=2 at D>=10^10, degree multiplication and unchanged unramified/local-differential properties')]:
    event(checks/'root_peer_reviews.tsv',sid,'targeted proof check','Read the entire proof in work/geometry_programme/section.tex; checked '+detail+'. No gap found. Scope is a complete proof reading, not formal verification.')

c4=Fraction(-2,5)+Fraction(-1,60)
c8=Fraction(2,3)+5*Fraction(-2,5)*Fraction(-1,60)+Fraction(-1,10080)
assert c4==Fraction(-5,12) and c8==Fraction(1411,2016)
assert c8.numerator%7==4 and c8.denominator==7*288
certificate=dict(statement_id='AG-THETA-NONINT',date=now,coefficient_t4=str(c4),coefficient_t8=str(c8),numerator_mod7=c8.numerator%7,denominator_7_unit_part=288,valuation7=-1,scope='exact rational coefficient calculation; full formal-series identity is proved in the paper')
(checks/'root_theta_nonintegrality.json').write_text(json.dumps(certificate,indent=2)+'\n')
event(checks/'root_peer_reviews.tsv','AG-THETA-NONINT','computation or formal certificate','Executed independent standard-library Fraction arithmetic for t4 and t8; obtained -5/12 and1411/2016 with numerator4 mod7 and denominator7*288. Certificate work/checks/root_theta_nonintegrality.json; finite calculation, not a formal assistant proof.')

old='the remaining\ngeometric step is identification of the independently\ndefined adelic/cohomological operator with this one and\na positivity argument in that model.'
new='MT-M21--MT-M22 identify the specified Meyer adelic summation\nquotient with this model. The remaining geometric step is\nthe particular draft/cohomological comparison and a positivity\nargument defined independently of the zeros.'
for p in [root/'block_trace_hilbert.tex',root/'section.tex']:
    text=p.read_text();assert old in text;p.write_text(text.replace(old,new))

with (root/'implications.md').open('a') as f:
    f.write('\n## Every fixed Hecke sector has an actual adelic comparison\n\nMT-M22 extends the Q comparison to every fixed primitive unitary Hecke character. It matches Meyer’s inverse Euler-factor convention explicitly, proves exact equality of his summation image and the full zero-jet ideal, and transports the quotient topology and bornology by a continuous block section. Thus MT-M18/M19 act on this independently defined adelic quotient, not merely on an abstract equal-spectrum space. No GRH is used for the comparison; A_D/M_H supply trace positivity in their respective scopes. Identification with a particular Masullo map or an étale-cohomology construction remains separate.\n')
    f.write('\n## Multiple zeros give an actual arithmetic obstruction\n\nNT-L16 quantifies the mean-square growth forced by a multiple pole of an inverse Hecke function. NT-L17 supplies concrete Kummer fields whose Dedekind zeta functions have infinitely many multiple zeros unconditionally. The universal weak-Mertens strengthening is therefore false. By MT-M20 their faithful full-jet quotients cannot carry positive Hilbert adjoint-square actions, even when M_H supplies positive traces. This is an arithmetic example, not only a possible abstract nilpotent block.\n')
    f.write('\n## CM normalization and ramified conductor refinement\n\nAG-CM-INTEGRAL-MODEL constructs a full-CM good elliptic scheme over an extension of degree at most48h_K/w_K unramified away from3, with a differential integral at any finite prescribed set of inert p>=5. AG-CM-MODEL-DEGREE makes that degree bound explicit from A_D. Thus the model-existence gate in the class and ray formulas is closed. AG-FG-POLE and AG-THETA-PCOND treat ramified conductor points with an explicit normalized denominator and pole-loss estimate. AG-THETA-NONINT proves that the canonical reduced theta itself need not be formally integral at an inert prime; the exact E:y²=4x³−4x coefficient1411/2016 has7-adic valuation−1. These statements distinguish the integral elliptic functions already controlled from an unproved blanket theta-integrality transfer.\n')
with (root/'ledger_history.md').open('a') as f:
    f.write(f'\n### {now} — fixed Hecke adelic comparison and CM model existence\n\nMT-M22 has a complete author and root reading and closes the fixed-character Meyer comparison, including topology and bornology. AG-CM-INTEGRAL-MODEL and AG-CM-MODEL-DEGREE have complete author and root readings; the good unramified model existence gate is now closed for every imaginary quadratic field with finitely prescribed inert primes. AG-THETA-NONINT has a complete root reading and an exact separate coefficient computation. NT-L16/L17 and AG-FG-POLE/THETA-PCOND retain their precisely scoped hypotheses. These are actual question-status/gate changes before the first scheduled review.\n')
print(json.dumps({'time':now,'root_rows':len(rows),'new_id':'MT-M22','peer_proofs':3,'coefficient':str(c8)}))
