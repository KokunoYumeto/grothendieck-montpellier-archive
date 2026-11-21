from pathlib import Path
from datetime import datetime, timezone
import csv, json

base = Path(__file__).resolve().parents[2]
root = base/'work/root'
checks = base/'work/checks'
now = datetime.now(timezone.utc).isoformat()

def event(path, sid, kind, outcome):
    with path.open('a',newline='') as f:
        csv.writer(f,delimiter='\t').writerow([sid,now,'/root','GPT-6 Astra Pro','not exposed','GRH_NIGHT_20261121',kind,outcome])

rows=json.loads((root/'rows.json').read_text())
assert not any(x['id'] in ('MT-M23','MT-ART09') for x in rows)
for name in ['nonabelian_multiple_zeros.tex','artin_relative_order.tex']:
    with (root/'section.tex').open('a') as f: f.write('\n'+(root/name).read_text())
rows.extend([
dict(id='MT-M23',statement='Every top field L of a nonabelian Galois extension has limsup I_L(X)/log^3 X>0 and infinite weak-Mertens limsup; exponent5 is available when its group has an irreducible representation of degree at least3. Its full-jet quotient has no faithful positive Hilbert convolution action, although its unconditional adapted trace model exists and M_H gives nonnegative adjoint-square traces.',input='neither for multiple zeros, mean-square obstruction and faithful-positivity obstruction; Masullo (conditional) only for trace positivity',status='proved here as complete consequences of the classical HKMS multiple-zero theorems and NT-L16/MT-M20; multiple-zero theorem itself is classical',where_the_proof_is='GRH_NIGHT.tex MT-M23; work/root/nonabelian_multiple_zeros.tex; HKMS2022 Theorems1.1–1.2 authorp2, proofs Sections3–5 pp5–8',where_it_lives='Masullo faithful positivity route; Q-MAS-FAITHFUL-POSITIVITY; cote1/SA23 geo-H-lidskii; extends NT-L17 beyond monomial fields'),
dict(id='MT-ART09',statement='For solvable G=Gal(L/K), all Artin functions are holomorphic at s0≠1 when q=ord_s0(ζ_L/ζ_K)≤max(2,p2−2), with p2 the second smallest prime divisor; p-groups already satisfy global Artin holomorphy. If4∤|G|, q≤3 also suffices. Under M_H any critical-strip pole therefore requires Re(s0)=1/2 and a relative zero of order above the applicable bound.',input='neither for Wong local holomorphy criteria; Masullo (conditional) for confinement of the residual possible poles to the critical line',status='classical with exact locators for the relative-order criterion; proved here for the combined explicitly scoped M_H transfer',where_the_proof_is='GRH_NIGHT.tex MT-ART09; work/root/artin_relative_order.tex; Wong2019 Theorems1.3–1.4 p254 with proofs259–260, Corollaries5.1/5.3 pp259–260',where_it_lives='Q-ARTIN-POS; sharper solvable Artin-holomorphy gate; augmentation Artin motive, representation K0, cote1 and AG-C1')])
(root/'rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
sources=json.loads((root/'sources.json').read_text())
sources.extend([
dict(id='HKMS22',title='Daniel Hu, Ikuya Kaneko, Spencer Martin and Carl Schildkraut, Order of zeros of Dedekind zeta functions, Proc.AMS150(2022),5111–5120, DOI10.1090/proc/16041',locator='Author2107.03269v2 Theorems1.1–1.2 p2; complete proofs Sections3–5 pp5–8; general degree>=4 statement is Conjecture6.2',url='https://arxiv.org/pdf/2107.03269',inspection='Root read the entire nine-page author paper, including both proofs of Theorem1.1 and the full Theorem1.2 proof. Cited group-theory and Stark prerequisites were not all independently reproved. Source multiplicity result is classical.',web_refs=['turn815619183view0','turn630350878view0','turn654483820view2']),
dict(id='WONG19',title='Peng-Jie Wong, Zeros of Dedekind zeta functions and holomorphy of Artin L-functions, J.Ramanujan Math.Soc.34(2019),253–261',locator='Theorems1.3–1.4 p254, complete proofs259–260; Section4 lemmata256–258; Corollaries5.1 and5.3 pp259–260; Theorems5.2/5.4 additional Sylow variants',url='https://www-math.nsysu.edu.tw/~pjwong/stuff/LowOrderZero.pdf',inspection='Root read the complete mathematical text pp253–260 and reference list p261, including both main proofs and all Section4 lemmata. Exact solvability hypothesis retained from theorem statements, despite broader abstract wording; classical theorem cited, not independently reproved.',web_refs=['turn283237953view1','turn843690954view0','turn843690954view1','turn591947073view0'])])
(root/'sources.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2)+'\n')
for sid,desc in [
('MT-M23','Read the whole new proof after writing it; checked the off-line functional-equation dichotomy, actual zero multiplicity, sharp NT-L16 coefficient, lower-power limsup passage and exact faithful full-jet hypotheses. The general multiple-zero inputs are cited HKMS theorems, not claimed new.'),
('MT-ART09','Read the whole new formulation and transfer proof; checked s0≠1, solvability, second-prime and p-group branches, max of classical thresholds, relative order rather than top-field order, and the critical-strip scope of Brauer confinement. No assertion that M_H bounds multiplicities.')]:
    event(root/'events.tsv',sid,'targeted proof check',desc)
for sid,desc in [
('HKMS22','Read entire nine-page primary author version, both Theorem1.1 proofs and Section5 proof of Theorem1.2; hypotheses and Conjecture6.2 boundary checked. Cited prerequisites not all reproved.'),
('WONG19','Read whole mathematical paper including Section4 lemmata and full proofs of Theorems1.3–1.4. Checked source body solvability requirement, second prime definition and Corollary5.3 condition4∤|G|.')]:
    event(checks/'source_events.tsv',sid,'used and rechecked in this run',desc)
for sid,desc in [
('NT-E01','division-field compositum, torsion cyclicity criterion, precise Dedekind RH family and no positivity assertion; quantitative density theorem cited with exact locators'),
('NT-E02','finite-group inclusion–exclusion, infinite product positivity and unconditional empty-Frobenius-set obstruction; entanglement factorization cited'),
('NT-E03','abelian U and equal-diagonal H, entire quotient factors transferring Dedekind RH downward, abelian B/U and B/H, and quadratic split-prime choice'),
('NT-E04','uniform-in-k estimate, explicit mixed division/ray-class field family and scope of imported theorem; no reduction to Dirichlet GRH alone'),
('NT-E05','all-discriminant positive class-number constant, ordered discriminants, partial-sum bound10D^(7/10)/7, PNT partition, both inequality branches and final log exponents'),
('NT-L16','entire strengthened wave/Gram proof including differentiated Laplace transform, normalization sqrt((2k)!), finite-set Bessel limit, countable nonnegative sum and off-critical contradiction'),
('NT-L17','whole proof after its L16 constant was updated; Kummer character orbit, all-prime factors, infinite zeros, new factorial constant and unconditional dichotomy')]:
    event(checks/'root_peer_reviews.tsv',sid,'targeted proof check','Read whole submitted proof/formulation in elliptic_reductions.tex or mertens_obstruction.tex; checked '+desc+'. No gap found. This is a complete proof reading, not a formal certificate or a fresh complete audit of every cited classical source.')
qp=root/'questions.tsv'
with qp.open(newline='') as f:
    rr=csv.DictReader(f,delimiter='\t'); fields=rr.fieldnames; qs=list(rr)
for q in qs:
    if q['id']=='Q-ARTIN-POS':
        q['state']='current general gate MT-ART02: positive semidefinite local Heilbronn matrix at multiple zeta zeros. Solvable branch narrowed by MT-ART09 to critical relative-zeta zeros of order≥max(2,p2−2)+1, or≥4 if4∤|G|. M_H supplies location, not the remaining order bound.'
    if q['id']=='Q-MAS-FAITHFUL-POSITIVITY':
        q['state']+=' MT-M23 supplies actual unconditional obstruction for every nonabelian Galois top field; infinite multiple zeros are classical HKMS, not only an abstract possibility.'
qs.extend([
dict(id='Q-ARTIN-RELATIVE-ORDER',source_and_locator='Wong2019 Theorems1.3–1.4; Q-ARTIN-POS',question='Can the solvable local Artin gate remove zeros inherited from the base field?',state='proved MT-ART09: use q=ord(ζ_L/ζ_K), with thresholds max(2,p2−2) and at least3 when4∤|G|; possible poles under M_H confined to the remaining higher-order relative zeros.'),
dict(id='Q-MAS-NONABELIAN-MULTIPLICITY',source_and_locator='HKMS2022 Theorems1.1–1.2; NT-L16/L17; MT-M20',question='Is the weak-Mertens/faithful-positivity obstruction confined to explicit monomial Kummer examples?',state='refuted by classical HKMS theorem and proved transfer MT-M23: all nonabelian Galois top fields obstruct, with log^3 mean-square growth, and log^5 when an irreducible degree≥3 occurs.')])
with qp.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(qs)
with (root/'implications.md').open('a') as f:
    f.write('\n## Relative Artin orders and every nonabelian Galois top field\n\nMT-ART09 removes the base-field zero contribution from the solvable Artin holomorphy gate using Wong’s exact classical theorem: under M_H only sufficiently high-order critical zeros of ζ_L/ζ_K remain. MT-M23 uses the unconditional HKMS multiple-zero theorem for every nonabelian Galois top field to rule out universal weak Mertens and faithful positive full-jet Hilbert actions. The obstruction is compatible with GRH and positive traces, and does not affect the unconditional adapted basis of MT-M18.\n')
with (root/'ledger_history.md').open('a') as f:
    f.write(f'\n### {now} — relative solvable Artin gate and general multiple-zero obstruction\n\nQ-ARTIN-POS has a strictly smaller solvable branch: relative zeta order replaces top-field order, with Wong’s precise thresholds. Q-MAS-NONABELIAN-MULTIPLICITY is closed by MT-M23 using the complete classical HKMS proofs. NT-E01–05 and the strengthened NT-L16/L17 have complete root readings. In particular NT-E05 has a checked sharper logarithmic exponent from the explicit class-number input.\n')
print(json.dumps({'date':now,'root_rows':len(rows),'new':['MT-M23','MT-ART09'],'peer_readings':7}))
