"""Write a per-finding framework index without attributing later theorems to Grothendieck."""
from pathlib import Path
import csv

ROOT=Path(__file__).resolve().parents[1]
c44='Cote44, PDF scan2 / archive footer1, Theorem4; PDF scan4 / footer3, Theorem5'
c16='Cote16, PDF scans45–46 / archive footers44–45, Coates letter on algebraic Lefschetz inverse and cycle-rank symmetry'
s7='SGA7 I, ExposéVII, §2.4 pp164–165, Example2.9.5 p175 and Remark2.9.6 p176'
s6='SGA6, Exposé0, §1, equations(1.1)–(1.3), p1 (PDF scan8)'
adams='SGA6, ExposéV, Appendix7.1 pp360–361 and Proposition7.5 pp362–364 (PDF scans367–371)'
fga='FGA, Bourbaki exposé221, Lemme2.4 p255 and Théorème3.2 p260'

groups=[
 ('Polarized cycle degree and finite maps',
  ['T6.1','T6.2','T6.3','T6.4','T6.6','B3','B4','B5'],
  c44+'; '+fga,
  'Intersection with a polarization in homological and numerical cycle groups; proper pushforward retains generic multiplicity. Analytic norms are evaluated in the Betti realization, not treated as integral cycle classes.',
  'Projection formula, surface Hodge index theorem, supplied032 §7; exact normalization proved in these findings.'),
 ('Correspondences, Picard duality and biextensions',
  ['T6.5','T6.7','T6.8','T6.9','T6.20','DER5'],
  s7+'; '+c16,
  'Divisor kernels are algebraic correspondences from birigidified line bundles; norm/trace and normalized correspondence cancellation take place in cycle groups. The Albanese and Fourier–Mukai comparisons require the separately cited later results.',
  'Supplied032 Lemma2.2/Proposition3.1; BMM Theorem9.1; Mukai Theorem2.2 and equation3.7; Perry trace naturality.'),
 ('Theta norms and their arithmetic normalization',
  [f'T6.{i}' for i in range(10,20)]+['T6.21','T6.22','T6.23','B1','B1a','B2','B14','B14a','B17','LN7'],
  c44+'; '+s7,
  'The theta identities calculate polarization pairings in Betti realization and constrain integral correspondence inputs. These are framework placements only: no Rallis formula, GRH estimate, automorphic classification, or CM eigenline-content theorem is attributed to these Grothendieck pages.',
  'Haan Theorem3.4; Gan–Qiu–Takeda Theorem11.4; BMM; Shin4.8/5.13; Labesse5.3/5.9; Alpöge supplied declarations; Masullo conditional §1.2; exact locators in the findings.'),
 ('Weil projectors and integral realization lattices',
  ['B6','B7','B8','B9','B16','B18','B23','B26','T6.24'],
  c16+'; '+s6,
  'The generic quadratic action defines correspondences on the middle homological motive; B16 gives an exact Chow idempotent using a later motivic theorem. Integral Betti intersection lattices and their positive middle pairing control division. The algebraic correspondences also admit étale realizations after spreading out; no new integral Tate or positivity theorem is inferred.',
  'Moonen §2.1, Proposition2.5 and Corollary2.6; Deninger–Murre degree projectors as imported there; MilneANT4.1–4.2 for B23.'),
 ('CM isogeny transport and bounded source geometry',
  ['B10','B11','B12','B13','B15','B19','B20','B21','B22','B22a','B24','B25','B25a','T6.25'],
  c44+'; '+s7+'; '+fga,
  'Integral CM Hom modules define genuine isogeny correspondences; their determinant indices and polarization metrics remain distinct. Hilbert boundedness and stabilizers control reduced-image multiplicities. B24 counts polarized CM points with fixed field and type; this is not a theorem about integral Shimura models.',
  'MilneANT4.19/4.26 and4.4/5.1; Ullmo–Yafaev Proposition4.1(1); Fulton Examples8.4.5–8.4.7; Stacks02LS; B22a has its separate sum-dimension source.'),
 ('Embedded and map-level deformation; bounded division',
  [f'S-{i:02d}' for i in range(1,8)]+['S-11']+[f'DIV{i}' for i in range(1,6)],
  fga+'; '+s6+'; '+c16,
  'Hilbert spaces parameterize bounded integral cycles, and their proper images propagate a fixed multiplier and signed degree. A morphism, reduced image, embedding and perfect pushforward are different deformation objects. Full Hodge compatibility is retained before invoking a deformation theorem.',
  'Bloch semiregularity; Buchweitz–Flenner Theorem5.2 and Proposition8.2; Stacks068X; Fulton18.3/18.3.11; suppliedMarkman Theorem1.5.1 and Corollary1.6.1.'),
 ('Perfect objects, Chern characters and full trace kernels',
  ['S-08','S-09','S-10']+[f'S-{i:02d}' for i in range(12,17)]+[f'S-{i:02d}' for i in range(18,42)]+['DER1','DER2','DER3','DER6'],
  s6+'; '+s7,
  'Perfect K-theory and Chern character provide the algebraic intersection framework. Hochschild evaluation, equivariant categories and full semiregularity are later refinements, not statements located in these SGA pages. A numerical K-class is never identified with a semiregular object without proof.',
  'Buchweitz–Flenner; Perry2026 Theorem1.2 and trace naturality; Perry2018 Theorem4.4; Bayer–Perry3.3/3.4/3.15; Shklyarov3.2–3.5; Orlov2.10/2.13; prior rStation37/v4 criterion explicitly attributed.'),
 ('Integral untwisting and effective Chern cycles',
  ['S-17','DER4','DER7'],
  adams+'; '+s6+'; '+fga,
  'Homogeneous Adams operations and determinant weights descend an integral K-class from a finite gerbe after successful deformation. Effective Chern degeneracy cycles and projective parameter spaces then give fixed signed-cycle bounds. These operations do not construct the initial semiregular object.',
  'Knudsen–Mumford Definition4 pp40–42 and Theorem2 p42; Perry2026 Kummer-gerbe construction; Stacks0F8F; the generation and fixed-multiplier proofs in DER4/DER7.'),
]

rows=[]
for title,ids,loc,role,later in groups:
    for fid in ids:
        rows.append([fid,title,loc,role,later])
for i in range(1,6):
    base=next(r for r in rows if r[0]=='B19')
    rows.append([f'B19.{i}',*base[1:]])
seen=set()
for r in rows:
    if r[0] in seen: raise ValueError('Duplicate finding '+r[0])
    seen.add(r[0])
with (ROOT/'FRAMEWORK_LOCATORS.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n')
    w.writerow(['finding_id','framework','exact_grothendieck_locator','role_and_limit','later_primary_inputs'])
    w.writerows(rows)

out=['# Per-finding Grothendieck framework placement',
     '',
     'The index `FRAMEWORK_LOCATORS.tsv` has one row for every numbered finding, including the explicit B19 substatements. The grouped descriptions below enumerate the same findings. A locator is a framework placement unless the proof expressly invokes a result on that page. Later analytic, categorical and number-theoretic theorems are attributed to their actual authors; they are not retroactively attributed to Grothendieck. Provisional identifiers, if present in this index, acquire no proved status from being indexed.',
     '',
     'The archival scan convention includes the cover; the corresponding archive footer is given as well. No mathematical transcription error has been established. In particular the Tate and standard-conjecture consequences admitted in the prompt are not enlarged by the analytic estimates or by these framework assignments.', '']
for title,ids,loc,role,later in groups:
    out.extend(['## '+title,'', '**Findings:** '+', '.join(ids)+'.','', '**Exact placement:** '+loc+'.','',role,'','**Later inputs:** '+later,''])
(ROOT/'FRAMEWORK.md').write_text('\n'.join(out))
print(len(rows),'per-finding framework rows')
