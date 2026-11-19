"""Serialize links adjudicated by reading both supplied endpoints.

External project endpoints were not supplied; those rows explicitly preserve
unverified leads rather than claiming to have passed a two-endpoint check.
"""
from pathlib import Path
import csv,json
B=Path(__file__).resolve().parents[1]
rows=[]
def link(kind,src,dst,what,evidence,notes):
    rows.append(dict(kind=kind,**{'from':src,'to':dst},what=what,evidence=evidence,
                     note_ids=';'.join('MPL_43_094-142#'+str(n) for n in notes)))

link('folder','43/132:1524–1539;43/133:1568–1577','16/21:860–896;16/23:945–976',
     'Finite Kummer, Picard/Néron–Severi and Brauer limits, with different dimension and topology hypotheses.',
     'Both passages directly read. Cote16(8.7) has NS⊗Z_l and T_lBr; the smooth geometric curve has Br=0. The l-primary qualification and finite-generation/divisibility assumptions are not transferred silently.',[6,8,16,20,23])
link('folder','43/120:1215–1226','16/19:725–778;16/21:860–896;16/23:945–976',
     'Different divisible groups: local geometric H¹(K,A), Picard identity group and Brauer divisible part.',
     'Both endpoints read. They are related duality constructions but none is an arithmetic S-unit theorem; no identification of their groups is claimed.',[3,4,5,22])
link('folder','43/132:1533–1539','16/19:725–778',
     'Picard-scheme points versus line bundles and descent obstruction.',
     'Both exact passages read. The curve five-term sequence retains Br(k); cote16 uses its own complete-local/algebraically-closed residue setup.',[7])
link('folder','43/106:490–545;43/133:1577','16/21:860–896;44/8:2966–2984',
     'The notation T(J) is not defined by merely matching it to T_l elsewhere.',
     '43/106 calls T a Greenberg–Néron–Grothendieck realization; cote16 and cote44 explicitly specify l-adic Tate modules. Both endpoints read; a category dictionary is required.',[9,17,23,54])
link('folder','43/102:299–326;43/112:786–822;43/133:1565–1586','16/28:1156–1186;16/30:1207–1236;16/52:1883–1925',
     'Local class-field coefficients, multiplicative complexes, and tame Kummer ramification.',
     'All cited faces read. Cote16/28 is the bibliography of the English cohomology text on30, not the Brauer pages; [27] there is Tate. Similar operations supply comparison tasks, not an equality of complexes.',[1,11,12,13,14,30])
link('folder','43/113:842–882','16/52:1910–1922',
     'Cancelled normal-closure reciprocity draft and the tame local Kummer plan.',
     'Both read. The source supplies local Galois/inertia maps and a root-of-uniformizer construction; no point-to-section injectivity theorem occurs at either endpoint.',[2,19])
link('folder','43/97:101–126','16/37:1449–1461;16/39:1526–1540',
     'Injective-preservation questions must distinguish a sheaf realization from the Matlis stalk construction.',
     'Both read. Cote16 proves a particular injective O-module construction; this is not a proof that the Néron functor has an exact left adjoint.',[27])
link('folder','43/123:1281–1311;43/125:1342–1371','16/39:1528–1540;16/37:1451–1461',
     'Local support duality, injective hulls and finite Artin layers.',
     'Both read. Matlis-layer data supplies the local model; the coherent first argument and completion conditions remain necessary in the support comparison.',[36,37,38,44])
link('folder','43/125:1342–1371','44/3:2807–2843',
     'Formal completion diagrams appear in both packets.',
     'Both faces read. The cote44 face is a cancelled completion draft; shared notation does not establish the unfinished final arrow in43/125.',[37])
link('folder','43/128:1394–1423;43/115:944–979','16/41:1589–1611',
     'Boundedness and derived Hom versus proper coherent direct-image dévissage.',
     'Both read. Cote16 uses coherent cohomology and explicit boundedness/way-out hypotheses; the Néron/Weil all-sheaf bound cannot be borrowed from it.',[28,29,39,77])
link('folder','43/137:1754–1774','16/56:2010–2040;54/4–6:2656–2713',
     'Faithful-flat module criteria and the flat descent of étale/regular properties.',
     'Both sets of passages read, including the companion flatness drafts. Flatness of A→B is retained; these algebraic criteria do not alone define the manuscript site.',[75,82])
link('folder','43/124:1333–1338;43/139:1800–1804;43/141:1854–1862','16/37:1451–1455',
     'Stalkwise tests in two different sheaf settings.',
     'Both read. Evaluation splits the tensor embedding on stalks; the injective-hull Hom adjunction is a separate O-module argument. Neither supplies a global evaluation splitting.',[83,84,85])
link('folder','43/100:173–235;43/106:490–545;43/114:884–943;43/130:1474–1512','47/3–8:2086–2419;47/11:2528–2573',
     'Curve/local duality diagrams and the separate Fourier kernel transform.',
     'Both ranges read, including the separate duality formula on47/11. No Fourier kernel or second unit-fibre inversion witness occurs in the Pro43 range. The comparison θ on47/8 remains a distinct map.',[31,32,34,40,43,47,48,50,51,69,86])
link('folder','43/133:1585–1586','47/7–8:2333–2419',
     'Oda’s finite pairing compatibility is not the Fourier unit-fibre compatibility.',
     'Both endpoints read. The former concerns an isogeny/p-divisible pairing; the latter Rp_*W→e_*(det t_B∨)[−n]. No transport between these maps was supplied.',[69])
link('folder','43/118:1070–1136;43/131:1514–1522;43/134:1615–1621','44/8:2966–2984',
     'Explicit dates belong to document units, not neighboring sheets.',
     'Both read. The cancelled administrative list has September1963 strings; the cycle letter is dated12August1964. No precedence of43/133 follows.',[52,79,89])
link('folder','43/128:1394–1423;43/132–133:1524–1613','44/2:2780–2806;44/9:2985–3001',
     'Ordinary curve Jacobian versus cycle-family kernel N(ξ) and incidence quotient.',
     'Both read. The curve pages contain no φ_ξ, higher-codimension cycle family or its proposed kernel characterization.',[1,53])
link('folder','43/117:1057–1059;43/133:1577','44/2:2780–2806;44/8:2966–2984',
     'Tate rank of a fixed local/curve group versus uniform Betti bound for cycle Jacobians.',
     'Both read. The quantifiers differ; no bound for all Alb(S)/N(ξ) follows from the fixed-curve table. Saito1979 supplies a precise later Picard-homomorphism bound.',[54])
link('folder','43/133:1568–1586','44/2:2780–2806;44/8:2966–2984',
     'The ordinary Jacobian is the dimension-one Picard/Albanese endpoint.',
     'Both read. The shared endpoint is actual; the all-codimension incidence/Picard construction requires separate proof.',[55])
link('folder','43/133:1585–1586','44/8–9:2966–3001',
     'Finite Cartier self-duality is distinct from the positive descended cycle correspondence.',
     'Both read. The latter constructs D=r_*(p*z·q*z), proposes a quotient and asks positivity. The curve table supplies neither integral descent nor ampleness.',[56,70])
link('folder','43/107:547–589;43/117:1028–1040;43/142:1866–1869','44/4:2844–2888',
     'Local Tate-type pairing versus the stated Néron–Tate/intersection formula.',
     'Both read. The pencil, cycle codimensions and (−1)^m convention occur in44/4 Theorem5; no transport through that pencil is constructed in Pro43.',[57])
link('folder','43/118:1070–1136;43/133:1564–1613','44/4:2844–2888',
     'A cancelled hyperplane-section outline is not the P^i hyperplane theorem.',
     'Both read. The companion Theorem6 has three dimension ranges and fixed-part assertion; the Pro43 outline proves none of them.',[58])
link('folder','43/132:1541–1563;43/130:1510','44/6:2939–2947',
     'Coefficient σ/τ and unspecified θ are distinct from cycle τ-equivalence.',
     'Both read. Cote44 Theorem7 compares numerical and τ-equivalence; the other passage locally defines a finite coefficient group. Letter resemblance is not a mathematical link.',[59])
link('folder','43/117:1028–1040;43/107:547–589','54/3:2609–2655',
     'Different dualities of dual abelian varieties: local component groups and de Rham degree one.',
     'Both read. Neither a common word duality nor a dimension count identifies the pairings or their complementary cohomological degrees.',[15,32,33,35])
link('folder','43/133:1580–1586;43/120:1185–1199','54/5:2682–2704;54/7:2714–2733',
     'Finite isogeny kernels, Cartier duality, F/V orthogonality and infinitesimal group data.',
     'Both read. Exact annihilator identities and Frobenius twists are supplied in computations§15 using Oda; no positivity or blanket splitting follows.',[18,60,61,62,65,66,67,68,70])
link('folder','43/133:1580–1586','54/7:2714–2733',
     'Filtered A[p] reconstruction and the later de Rham–Dieudonné comparison.',
     'Both read. Pro43 has a finite coefficient table; the explicit reconstruction question is on54/7. Oda Cor5.11 answers it for abelian varieties over perfect fields, with full F/V structure.',[63,64])
link('folder','43/94–98:2–166','43/92–93 (K43-06):371–440',
     'Immediate preceding definition of the Weil topology and its unresolved derived generic direct image.',
     'Both read. The earlier face explicitly worries about losing infinitesimal groups and imposes filtered continuity; the later withdrawal must be read against that setup.',[24,25,26,27,28,29,30,88])
link('folder','43/123,125:1281–1311,1342–1371;43/135–140:1623–1847','43/89–90 (K43-06):272–362',
     'Support/local duality and the open-complement degree shift recur earlier in the folder.',
     'Both read. The earlier formulas retain −i−1 on the punctured scheme; they reinforce the need for a shift but do not decide uncertain later ink.',[36,37,44,46,47,48,49])
link('folder','43/125:1342–1344','43/161–162 (K43-08):5–36',
     'Same support-Ext filtered-colimit theorem, with finiteness hypotheses visible earlier in the Codex portion.',
     'Both read. Scan161 inserts F coherent, distinguishes locally noetherian sheaf and noetherian global cases; scan162 finishes the injective torsion argument. CL-SA19-054 and root CL-SA19-647 are duplicate occurrences.',[37])
link('folder','43/106–107:490–589;43/112:786–839','43/143–145 (K43-06:445–526;K43-07:5–29)',
     'Ordinary local Tate duality, Shatz finite-flat rows and the arithmetic global sequence.',
     'Both read. Ordinary local complementary degree2 differs from the geometric residue-field shift before descent. The copied Tate text also keeps prime-to-residue-characteristic hypotheses in its opening finite étale setup.',[12,13,15,19,31,32,33])

link('published work','43/94,97–98,128','Grothendieck1957 Theorem2.4.1,p148',
     'Conditional composite-functor spectral sequence.',
     'Primary theorem read; independent adjunction proof in computations§1. Section4.2 is outside the partial PDF and is not marked read.',[24,27,28,29,39])
link('published work','43/123:1281–1311','SGA2 ExposéV Theorem2.1;ExposéIV',
     'Regular-local duality with the missing dimension and dualizing module specified.',
     'Primary statement and relevant proof context directly read; formula H_m^i(M)=D Ext^(r−i)(M,A) requires regular local A and finite M.',[36])
link('published work','43/125:1342–1371','SGA2 VI Theorem2.3(a,b),recomposedpp59–60;IX Theorem2.1',
     'Support Ext as a colimit; separate formal-functions comparison.',
     'Both exact published passages read. Coherence/noetherian and formal-function finiteness/Mittag–Leffler hypotheses retained.',[37])
link('published work','43/135–140','SGA2 I2.3bis,Theorems2.6,2.8;XIV2.3',
     'Support functors, localization and codimension-one prime-to-p normalization.',
     'Primary locators read. The wild finite-flat case and arbitrary-sheaf completion are separate questions.',[44,45,46,47,48,49])
link('published work','43/133:1577–1583','SGA1 IX Remark5.8,finalparagraph,recomposedp194(original252–253);X2.7',
     'Abelianized étale fundamental group of the curve and its Jacobian.',
     'Primary symmetric-power/projective-bundle proof directly read. It concerns the étale realization, not all infinitesimal J[p].',[9,10,23])
link('published work','43/108:591–630','EGAIV3 15.5.4–15.5.8,pp233–236',
     'Connected-component semicontinuity and local constancy under reduced-fibre hypotheses.',
     'Published proof and properness counterexample read; cancelled draft hypotheses are not silently repaired.',[74])
link('published work','43/110:722–784','EGAIV3 12.2.1(xi),12.2.1.4,12.2.2(iii),12.2.3(vi),pp179–183',
     'Flat multiplicity theorem and the explicitly retained universal-openness/associated-prime question.',
     'Primary pages read. The 1966 question is an exact backward-reference match; its ultimate later resolution was not located. The literal inequality⇒flat counterexample is a different assertion.',[75,76])
link('published work','43/115:944–979','EGAIII1 III3.2.1,pp116–117',
     'Proper coherent direct-image theorem via Chow/Leray dévissage.',
     'The primary proof reproduces the same large twist and projective modification. No theorem about the different Néron realization follows.',[77])
link('published work','43/116:1019–1023','EGAIV3 12.1.1(vi),12.2.1(vii),pp179–180',
     'Nearby Cohen–Macaulay fibre openness theorem.',
     'Published hypotheses read. Missing draft references1.1(ii) and2.6 still unidentified, so this is a precise nearby theorem rather than an exact answer to the cancelled question.',[78])
link('published work','43/121:1237–1267','EGAIII1 OIII11.10.2,p49;III2.5.2–2.5.3,pp109–110',
     'Euler additivity and Hilbert–Euler polynomial for all integer twists.',
     'Primary statements/proofs read; zero-sheaf test prevents unqualified strict positivity.',[80])
link('published work','43/129:1431–1470','EGAIV2 Cor6.3.1 via directly read Stacks0338 Lemma10.163.1;Stacks00OO,00OG',
     'Flat local depth/dimension formula and regular polynomial fibres.',
     'Modern primary proofs read; the exact EGAIV2 original PDF was not read. Missing final listP remains blank.',[81])
link('published work','43/101,103,105','Atiyah1961 pp308–310,Theorems6.2,6.5;Lemmas6.3–6.4;finalquestion',
     'Exact identification of reused Thom Complexes leaves and their ordering.',
     'Primary PDF directly read. This identifies Atiyah’s text, not Grothendieck authorship of its homotopy conjecture or dates of adjacent sheets.',[71,72,73,87,89])
link('published work','43/124,126,139,141','Cartan1951XV §§5–6;Cartan1951XVI p4;Grothendieck1957 §3.3,p159',
     'Classical fine/soft-sheaf machinery and tensor embedding.',
     'Relevant primary statements/proofs read. The exact numbered typescript239 source is not identified merely by the theorem match.',[83,84,85])
link('published work','43/117,119–120','Suzuki2014 TheoremA,Proposition3.4.3,Theorem5.2.2.1',
     'Modern local geometric duality and perfect component pairing over perfect residue fields.',
     'Exact theorem and coefficient/site hypotheses read; derived bidual and component structures retained.',[5,15,16,17,18,35])
link('published work','43/119–120','RibeiroRosengarten2025 Theorem4.3;introp3;Breen1975 vanishingrange',
     'Correct low-degree fppf abelian-scheme Ext and obstruction to blanket higher zeros.',
     'Primary text read. Finite Kummer gives internal degrees0–2; higher rows and μ∞ continuity are separate.',[16,18])
link('published work','43/130,132–133,135–138','ArtinMilne1976 Cor4.9,p124;Suzuki2018 Theorem3.1.3,Props2.7.6–2.7.7',
     'Finite-flat curve duality and localization-compatible trace.',
     'Primary text directly read, including Artin–Milne perfect-site hypotheses. Printed [2] and Suzuki Serre-dual shifts use declared conventions, not an ink emendation.',[6,8,39,40,41,42,46,47])
link('published work','43/133:1580–1586','Oda1969 Cor1.3,Def3.5,Prop3.13,Thm3.19,Cor5.11–5.12,pp69–70,82,86,89,131–132',
     'Exact finite Cartier/de Rham–Dieudonné comparison.',
     'Primary conventions read. Perfect field, Frobenius twists, group scheme versus points, and general injection versus abelian isomorphism distinguished.',[60,61,62,63,64,65,66,68,70])
link('published work','43/133:1585–1586;47/8:comparisonquestion','Oda1969 Definition1.9,Propositions1.12,1.15,pp75–78',
     'ρ(L)=e(L) is a completed finite pairing compatibility.',
     'The named construction and proof continuation onp78 read. This neither proves the Fourier θ compatibility nor positivity of arbitrary symmetric correspondences.',[69,70])
link('published work','43/133:fixedcurve;44/2,8–9:cycleprogramme','Saito1979 Proposition3.4,Theorem3.6,Proposition4.4,pp109–113',
     'Picard-homomorphism Betti bound, incidence quotient and complementary duality up to isogeny.',
     'Primary statements and bound proof read. Proposition4.4 cites its proof elsewhere; universal regular representatives and integral isomorphisms are not asserted.',[53,54,55,56])

unverified='External target files are absent from this package. Only the exact pointer and its qualification in the earlier note were read; target theorem, proof and reported review status remain UNVERIFIED. '
link('our projects','43/102,113,128,132–133','README bridgeB11;WG2 §1.1 #3;149 Théorème3;142 Proposition2',
     'Earlier-run generalized-Abel/Kummer comparison with the1983 arithmetic-section argument.',
     unverified+'The local/curve ingredients are present; modulus, base point, section map and the proposed arithmetic comparison are not constructed in this Pro range.',[1,2])
link('our projects','43/113;43/132–133','FLAGGED_149 B5;LM6 F.35;CYCLOTOMIC_KERNEL C1',
     'Named point-to-section injectivity and Kummer-boundary map comparison.',
     unverified+'The notes require base-point/conjugacy conventions and the induced fundamental-group map; no return claim is upgraded.',[2])
link('our projects','43/109,112,119–120,132–133','149/85;README G_m(S);LM6 F.43;INTAKE20261114 §4.4',
     'Arithmetic-unit finite generation and all-orders nondivisibility leads.',
     unverified+'Q× and Z[1/6]× examples are independently proved in computations§22. LM6F.43 is only a shared source-range pointer, not a reproduced unit theorem; the intake mentions Q^solv and is not a referee verdict.',[3,4,5,22])
link('our projects','43/112,119–120,132–133,135','FLAGGED_149 B9;FLAGGED_149 Z142g;LM6 B.27',
     'Prime-to-p covering towers and compatible p-primary point differences.',
     unverified+'The finite coefficient rows specify maps to compare, but no actual tower or compatible-point construction is supplied; open-return status is unchanged.',[8,10,16,20,45,67,68])
link('our projects','43/113','CYCLOTOMIC_KERNEL C1;FLAGGED_149 A9;LM6 B.22;LM6 F.43',
     'Normal-closure inertia/reciprocity and extension reconstruction.',
     unverified+'The cancelled source diagram does supply local maps; it does not establish the external intrinsic group reconstruction theorem.',[19])
link('our projects','43/117,133','WG H1;FLAGGED_149 F8a;LM6 A.50',
     'Character targets for a proposed normalizer/centralizer argument.',
     unverified+'The relevant subgroup action, invariants, and map from a normalizer are not on these pages. WG H1 remains an unchecked hunch.',[15,21,30])
link('our projects','43/118,128,130–134;44/2,4,6,8–9','WG2 §2.3 #12;WG2 §1.1 #3',
     'Earlier-form and cycle-Jacobian planning questions.',
     unverified+'Both supplied folder endpoints were read, but shared date adjacency or coefficient letters do not identify an earlier all-codimension theorem.',[9,23,40,43,52,53,54,55,58,59,64])
link('our projects','43/107,117,133,142;44/2,4,8–9','WG H9;WG2 §2.3 #12',
     'Positivity, cycle duality and height-pairing hunches.',
     unverified+'Curve Jacobian polarization is a known endpoint; it does not verify integral descent or the cycle-height sign in arbitrary dimension.',[56,57,58,70])
link('our projects','43/101,103,105,108,110,115–118,121,124,126,129,137,139,141','MPL_136_095-141 §1.5;MPL_136_189-234 R008;MPL_136_235-281 N16',
     'Earlier-run reused-sheet provenance comparisons.',
     unverified+'These are first-pass provenance leads only. Atiyah/EGA exact matches made here have independent primary evidence; the239/338 typescript provenance remains unresolved.',[71,72,73,74,75,77,78,79,80,81,82,83,84,85,89])
link('our projects','43/94–142:entirerange','La Longue Marche;Les Dérivateurs;S6 (general context only)',
     'No extra named theorem target is manufactured from the general project framing.',
     unverified+'The entry-specific pointers above exhaust the named project leads found here. No separate S6 or Dérivateurs theorem identifier occurs in these89 entries.',[89])

# Expand the thematic project summaries into one exact named-target row each,
# preserving every citing entry from the separate mechanical pointer index.
pointer_path=B/'external_pointer_index.tsv'
if pointer_path.exists():
    pointers=list(csv.DictReader(pointer_path.open(),delimiter='\t'))
    thematic=[r for r in rows if r['kind']=='our projects']
    rows=[r for r in rows if r['kind']!='our projects']
    item_records=json.loads((B/'items.json').read_text())
    by_entry={e:i for i in item_records for e in i['sources']}
    for target in dict.fromkeys(p['target'] for p in pointers):
        hits=[p for p in pointers if p['target']==target]
        es=sorted({p['entry_id'] for p in hits},key=lambda s:int(s.split('#')[1]))
        scans=sorted({n for e in es for n in by_entry[e]['scans']})
        candidates=[r for r in thematic if target in r['to']]
        if target.startswith('MPL_136_'):
            candidates=[r for r in thematic if 'MPL_136_' in r['to']]
        if target=='README bridge B11':
            candidates=[r for r in thematic if 'bridgeB11' in r['to']]
        if target=='INTAKE 20261114 §4.4':
            candidates=[r for r in thematic if 'INTAKE20261114' in r['to']]
        if target=='MPL_136_095-141 §1.5':
            candidates=[r for r in thematic if 'MPL_136_095-141' in r['to']]
        rows.append(dict(kind='our projects',**{'from':'43/scans'+','.join(map(str,scans)),'to':target},
                         what='; '.join(dict.fromkeys(r['what'] for r in candidates)) or 'Named earlier-run comparison or planning pointer.',
                         evidence=unverified+'Every citing entry is retained here; external_pointer_index.tsv preserves its verbatim context and original qualification. '+
                         (' '.join(dict.fromkeys(r['evidence'].removeprefix(unverified) for r in candidates))),
                         note_ids=';'.join(es)))

with (B/'links.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['kind','from','to','what','evidence','note_ids'],delimiter='\t')
    w.writeheader();w.writerows(rows)
with (B/'our_projects.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['kind','from','to','what','evidence','note_ids'],delimiter='\t')
    w.writeheader();w.writerows(r for r in rows if r['kind']=='our projects')
print(f'{len(rows)} links saved; {sum(r["kind"]=="our projects" for r in rows)} separated external-project leads')
