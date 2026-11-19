"""Authored link meanings; literal mention extraction only supplies provenance IDs."""
from pathlib import Path
import csv,re,json
W=Path(__file__).resolve().parents[1];BASE=W.parents[2]/'source'
# This worker is W=/.../SA09_work/workers/cote137; sources are three parents above W.
BASE=W.parents[2]/'source'
T1='MPL_137_002-044_transcription.tex';T2='MPL_137_045-086_transcription.tex'
N={}
for stem in ['MPL_137_002-044','MPL_137_045-086']:
 s=(BASE/'SA09_notes/pro'/f'{stem}_notes.md').read_text();idx=0
 for b in re.split(r'(?m)(?=^###? )',s):
  if stem.endswith('045-086') and b.startswith('### '):idx+=1;key=f'{stem}#{idx}'
  elif stem.endswith('002-044') and (m:=re.match(r'## (R\d+)',b)):key=f'{stem}/{m[1]} (unindexed supplied note)'
  else:key=f'{stem}/frontmatter'
  N[key]=N.get(key,'')+'\n'+b
def mentions(*words):return ';'.join(k for k,b in N.items() if any(x in b for x in words))
L=[]
def link(kind,fr,to,what,evidence,ids):
 L.append(dict(kind=kind,**{'from':fr,'to':to},what=what,evidence=evidence,note_ids=ids))
 with (W/'links.tsv').open('w') as f:
  w=csv.DictWriter(f,fieldnames=['kind','from','to','what','evidence','note_ids'],delimiter='\t');w.writeheader();w.writerows(L)
def p(t,sc,l):return f'137/{sc}; {t}:{l}'
def local(sc1,l1,sc2,l2,what,ids,t1=T1,t2=T2):
 link('folder',p(t1,sc1,l1),p(t2,sc2,l2),what,'Both supplied transcription endpoints read. Relationship is this run’s comparison unless an explicit reference is noted.',ids)

local(4,'113-130',73,'998','Weight-n PD/exterior comparison precedes the later explicitly truncated de Rham application. Same programme; the later paragraph does not supply all missing chain-map details.','MPL_137_002-044/R005;MPL_137_045-086#27;MPL_137_045-086#28')
local('28;38-39','1193-1209;1529-1565','65-86','782-1310','The postponed tensor/Γ coefficient-functor reconstruction develops into multiplicative functors and polynomial/tensor-PD categories. It remains distinct from homotopy reconstruction.','MPL_137_002-044/R045;MPL_137_002-044/R057;MPL_137_002-044/R101;MPL_137_002-044/R102;MPL_137_045-086#17;MPL_137_045-086#44;MPL_137_045-086#49')
local(44,'1965-1997',45,'1-47','Literal continuation of Proposition3: existence of the products and the generator evaluation check.','MPL_137_002-044/R074;MPL_137_002-044/R075;MPL_137_002-044/R076;MPL_137_002-044/R107;MPL_137_045-086#1')
local(37,'1491-1495',62,'729-760','Earlier margin calls C abelian; later passage cancels abelian and warns about noninvertible bimorphisms. The categories and base hypotheses must be aligned before treating this as an authorial correction.','MPL_137_002-044/R055;MPL_137_045-086#12;MPL_137_045-086#77')
local(7,'188-215',11,'352-366','Missing degree-zero sphere and leading factorial are checked against the explicit later rank formula.','MPL_137_002-044/R007;MPL_137_002-044/R008;MPL_137_002-044/R009',t2=T1)
local(17,'631-635',11,'352-366','The deleted μ_i in normalized rank conflicts with disk/sphere ranks; a single identity disk detects it.','MPL_137_002-044/R030',t2=T1)
local(23,'1006-1017',24,'1023-1048','Extension obstruction labels must agree with the next page’s qm=np and primitive pair p=tm′,q=tn′.','MPL_137_002-044/R040',t2=T1)
local(41,'1738-1763',42,'1824-1827','Cancelled Karoubi claim is to be distinguished from the later explicit hypothesis that finite projectives are free.','MPL_137_002-044/R066;MPL_137_002-044/R069',t2=T1)
local(51,'258-301',56,'523-528','Initial evaluation/exactness assertion is qualified later by the abelian-target clause.','MPL_137_045-086#4;MPL_137_045-086#7',t1=T2)
local(60,'674-679',63,'764','Disk/sphere essential-image wording conflicts with the explicit split-homology category Q; preserve both layers.','MPL_137_045-086#11;MPL_137_045-086#74;MPL_137_045-086#76',t1=T2)
local(69,'917',71,'968-972','The missing tensor unit on contractible generators motivates the separate unit map into cycles and its kernel-free alternative.','MPL_137_045-086#22;MPL_137_045-086#80;MPL_137_045-086#82',t1=T2)
local(76,'1059-1094',77,'1096-1111','Authorial withdrawal of scalar-weight uniqueness leads to chosen multidegrees and consideration of all coefficient algebras.','MPL_137_045-086#33;MPL_137_045-086#34;MPL_137_045-086#86;MPL_137_045-086#87',t1=T2)
local(78,'1143-1151',80,'1193-1196','Question about Γ⁰(0) as tensor unit receives a conditional answer after stronger comparison isomorphisms.','MPL_137_045-086#37;MPL_137_045-086#88',t1=T2)
local(82,'1240-1248',83,'1265-1274','Degree-zero unit is an added axiom explicitly remembered after the preliminary list.','MPL_137_045-086#42;MPL_137_045-086#91',t1=T2)

link('published work',p(T1,'14-15','474-544'),'SGA6I, I2.1--2.2 and I4.7--4.8; https://grothendiecksga.com/read/sga6/fr/I-2.html ; https://grothendiecksga.com/read/sga6/fr/I-4.html','Same finiteness vocabulary; the archive’s representative/rank claims require correction. This source predates the manuscript catalogue date.','Both primary-text endpoints read; Illusie’s exposé is distinguished from a later Grothendieck-original theorem.',mentions('pseudo-coh','pseudocoh'))
link('published work',p(T2,'75-86','1006-1310'),'SGA4XVII5.5.2.2--6; https://grothendiecksga.com/read/sga4/fr/XVII-5.html','The module example of polynomial laws, Γ representation and exponential formula is established there; the arbitrary-category equivalence remains a separate problem.','Both endpoints checked; SGA text predates these sheets.', 'MPL_137_045-086#31;MPL_137_045-086#34;MPL_137_045-086#36;MPL_137_045-086#44;MPL_137_045-086#49')
link('published work',p(T1,39,'1551-1565'),'Grothendieck1966, Theorems1/1-prime; https://www.numdam.org/article/PMIHES_1966__29__95_0.pdf','Earlier algebraic de Rham comparison over C is related background, with a different output from integral homotopy reconstruction.','Both passages read; no exact equivalence claim.', 'MPL_137_002-044/R059;MPL_137_045-086#30')
link('published work',p(T1,39,'1551-1565'),'GrothendieckPS1983 §119, original500--503/printed448--450; https://thescrivener.github.io/PursuingStacks/ps-online.pdf','Later failure of a proposed integral schematic/discrete comparison and a replacement binomial-cochain question.','Opened later primary text; not a blanket refutation of every enriched PD theory. The explicit cocycle equation was independently checked.', 'MPL_137_002-044/R084;MPL_137_002-044/R085;MPL_137_002-044/R086;MPL_137_045-086#51;MPL_137_045-086#52')
link('published work',p(T2,'81-86','1203-1310'),'GrothendieckPS1983 §120, original506--507/printed453--454; https://thescrivener.github.io/PursuingStacks/ps-online.pdf','Later analyzer discussion separates composition, additive diagonal, multiplicative diagonal and constants; a comparison to plethories is an earlier-run idea.','Both endpoints read. No identity of the operation theories is inferred.', 'MPL_137_002-044/R087;MPL_137_045-086#39;MPL_137_045-086#47;MPL_137_045-086#64')
link('published work',p(T1,39,'1562-1565'),'GrothendieckPS1983 §121, original508--509/printed454--455; https://thescrivener.github.io/PursuingStacks/ps-online.pdf','Later text explicitly distinguishes a conservative Eilenberg--Mac Lane functor from full faithfulness.','Both endpoints read, particularly equations(3)--(5); this is a methodological comparison, not proof of137 reconstruction.', 'MPL_137_002-044/R098;MPL_137_045-086#55;MPL_137_045-086#56')
link('published work',p(T2,65,'782-809'),'GrothendieckPS1983 §124, original521/printed466; https://thescrivener.github.io/PursuingStacks/ps-online.pdf','Later programme distinguishes schematic semisimplicial models, PD de Rham complexes and categories with diagonals.','Both endpoints read; the common word multiplication does not identify these models.', 'MPL_137_045-086#17')
link('published work',p(T2,'67-69','850-917'),'GrothendieckPS1983 §128, original538--541/printed480--483; https://thescrivener.github.io/PursuingStacks/ps-online.pdf','Later V/W bundles and co-semisimplicial commutative algebras provide a concrete comparison target; arbitrary affine schemes are expressly questioned.','Opened both endpoints, including original540 and the elliptic-curve-minus-point caution at541. No chain-level equivalence with137 is supplied.', 'MPL_137_002-044/R077;MPL_137_045-086#21;MPL_137_045-086#65')
link('published work',p(T2,'46-47','51-141'),'GrothendieckPS1983 §134, original557--560/printed497--499; https://thescrivener.github.io/PursuingStacks/ps-online.pdf','Later integrator functor must be normalized before invoking Dold--Kan; ordinary linearization is distinguished from weak-homotopy detection.','Both endpoints checked, particularly original559. Older half-simplicial usage includes degeneracies.', 'MPL_137_002-044/R097;MPL_137_045-086#2;MPL_137_045-086#14')
link('published work',p(T1,'3;5','44-79;134-174'),'SullivanTypescript1975, printed112 and105; https://www.math.stonybrook.edu/~dennis/publications/PDF/DS-pub-0017.pdf','Exact provenance of the embedded English printed pages; neither is a Grothendieck-original theorem statement.','Matching pages visually checked; precise typescript edition uncertain because author bibliography pagination differs.', 'MPL_137_002-044/R003;MPL_137_002-044/R006;MPL_137_002-044/R090')

absent='The supplied note and its local transcription endpoint were read; the named project/report endpoint is absent from the attachments. This row preserves a reported lead/status only, not an independently checked project result.'
def project(name,words,fr,what):link('our projects',fr,name,what,absent,mentions(*words))
project('Hua, modernised reading of cote137; hua_project/137.modern.tex; hua_project/README.md',['Hua, modernised reading','hua_project/137.modern.tex'],p(T1,'2-44','1-1997')+'; '+p(T2,'45-86','1-1311'),'AI-produced contextual modernization reported throughout the notes. Its strong-unit, naive-truncation, bilinear-composition and index readings must not replace the diplomatic text. The separately opened Hua2026 public preprint is a distinct source.')
project('Hua finding137-perfect-complexes-universal-sigma-exact',['137-perfect-complexes-universal-sigma-exact'],p(T1,'40-44','1571-1997')+'; '+p(T2,'45-64','1-778'),'Reported candidate/new-to-project intake; not historical priority or a formal certificate. The restricted additive theorem and target-Σ limitation are separated in CL-SA09-137-031/032.')
project('Hua finding137-polynomial-categories-pd-tensor-categories',['137-polynomial-categories-pd-tensor-categories'],p(T2,'75-86','1006-1310'),'Reported candidate: homogeneous core does not establish full tensor, mixed-degree, constant and multigrading equivalence.')
project('WG2 §Week #3',['WG2 §Week #3'],p(T1,'2-44','1-1997')+'; '+p(T2,'45-86','1-1311'),'Unchecked broad cochain programme. The present pages support precise operations and bounds; they provide no completed integral reconstruction or inferred geometric example.')
project('WG2 §2.4 #5',['WG2 §2.4 #5'],p(T1,'28;38-39','1193-1209;1519-1567')+'; '+p(T2,'73-86','998-1310'),'Unchecked PD/Fourier-Chern and reconstruction planning thread. No Fourier transform, its Chern class, or algebraic abelian variety is identified in supplied137. The printed real Jacobian is a different example.')
project('WG H6',['WG H6'],p(T2,'65-86','782-1310'),'Unchecked local-system/schematization hunch. The manuscript does not prove a finite-dimensional-local-system characterization or the required comparison functor.')
project('MPL_133 B01',['MPL_133 B01','B01/B06'],p(T1,'7-19','178-742')+'; '+p(T2,'76-77','1043-1119'),'First-pass rank/binomial lead. Numerical Newton coefficients do not amount to a binomial operation algebra; finite-field scalar weights require separate data.')
project('MPL_133 B05',['MPL_133 B05','B05/B06'],p(T1,39,'1551-1565')+'; '+p(T2,73,'998'),'First-pass later-comparison correction. Public PS§119 was independently checked, but this absent report’s detailed assertions and status were not.')
project('MPL_133 B06',['MPL_133 B06','B05/B06','B01/B06'],p(T1,'28;38-39','1193-1209;1529-1565')+'; '+p(T2,'65-72','782-994'),'First-pass strict cosimplicial versus ordinary DGA multiplication/enrichment lead. Transported tensor, ordinary total tensor, binary homotopies and higher coherent operations are distinct.')
project('MPL_133 §2 and §88; reported133/006--009',['MPL_133 §2','MPL_133 §88'],p(T1,'7;38','178-221;1519-1547')+'; '+p(T2,'75-86','1006-1310'),'First-pass/truncated reports distinguish quadratic Witt theory from a separate finite-G-set/Burnside thread. DressSiebeneicher1989 supports a literature comparison only; no interpretation of absent133 scans is certified.')
project('MPL_136_047-094 §2',['MPL_136_047-094 §2'],p(T2,'63-73','764-998'),'First-pass functorial-cochain/resolution lead. Comparison maps are unique up to homotopy with fixed augmentation, not a choice of all higher coherence.')
project('MPL_136_189-234 §2',['MPL_136_189-234 §2'],p(T1,4,'113-130')+'; '+p(T2,73,'998'),'First-pass bounded weightwise PD comparison lead. The source insertion through degree n is retained; no unbounded reconstruction is inferred.')
project('MPL_136_235-281 §86',['MPL_136_235-281 §86'],p(T2,'73-86','998-1310'),'First-pass literature/reconstruction lead. Horel and Mandell were checked independently, but exact manuscript-to-modern comparison remains unconstructed.')
project('GALOIS G.6/E.11',['GALOIS G.6/E.11'],p(T1,'38-39','1529-1565'),'Reported open bare-derivator higher-coefficient problem, with missing monoidal enhancement. No derivator functor or localizer identity is supplied by137.')
project('RESIDUE I.7',['RESIDUE I.7'],p(T1,'38-39','1529-1565'),'Reported open accessibility/localizer and derivator-enhancement problem; individual complex dévissage establishes no classification of category weak equivalences.')
project('TOTASPH D.7/RESIDUE F.5',['TOTASPH D.7/RESIDUE F.5'],p(T1,'29-34','1213-1398'),'Reported older open total-asphericity⇒exact-colimits implication. Ordinary density on these pages is not a parallel-pair equalization theorem.')
project('TOTEX2 D.1; TOTEX2 D.2',['TOTEX2 D.1','TOTEX2 D.2'],p(T1,'29-34','1213-1398'),'Reported later strict filtered⊊exact⊊total⊊quasi-filtered chain and total⇒filtered refutation, with intake CONSISTENT/zero-wrong. These conflict with treating the older implication as still unqualifiedly open; reconcile original reports before importing statuses.')
project('IMPL I1',['IMPL I1'],p(T1,'31-36;43','1280-1459;1924-1951'),'Reported compact Pontryagin duality uses Hom(−,R/Z), unlike finite-free Hom_k(−,k). No derived-limit comparison is inherited from the manuscript pairing.')
project('CATHOT F.8',['CATHOT F.8'],p(T1,'29-34','1213-1398'),'Reported proved space-valued finite-category test theorem and noncompactness distinction. Ordinary set/abelian-group density here does not prove the higher statement.')
project('PRETOT A.12; TOTASPH C.10',['PRETOT A.12','TOTASPH C.10'],p(T1,14,'474-510')+'; '+p(T2,'46-47','51-141'),'Reported Δ_inj examples cannot be identified with the manuscript’s Dold--Puppe half-simplicial objects, which include degeneracies. Claimed reviews/zero-wrong status remain reports.')
project('LM4; LM7',['LM4','LM7'],p(T1,'2-44','1-1997'),'Frontmatter cites reviews of unrelated projects. No mathematical conclusion in137 inherits their reported referee approval.')
project('Planning README B7',['README\'s **B7**','README’s **B7**','B7 proposal'],p(T1,39,'1551-1565')+'; '+p(T2,'65-86','782-1310'),'Reported integral structured-cochain reconstruction guess. Recognition, completion, affinization and full mapping recovery must be separate targets; source alone resolves none of them.')
project('cote153 analyzer lead',['cote153','cote 153'],p(T2,'81-86','1211-1310'),'Reported analyzer comparison does not identify the absent cote153 object with a binomial plethory. Public PS§120 is independently available, but it is a different endpoint.')

# These updates are individually authored after reading the named project text.
# They certify textual correspondence and dated report status, not proof validity.
updates={x['name']:x for x in json.loads((W/'project_endpoints.json').read_text())}
for row in L:
 if row['to'] in updates:
  u=updates[row['to']];row['what']=u['what'];row['evidence']=u['evidence']+' Bibliography: '+u['reference']+'.'
verified=[dict(x) for x in L if x['kind']=='our projects' and x['to'] in updates]
leads=[dict(x) for x in L if x['kind']=='our projects' and x['to'] not in updates]
for row in verified:
 if row['to']=='PRETOT A.12; TOTASPH C.10':
  residual=dict(row);residual['to']='PRETOT A.12';residual['what']='Reported PRETOT A.12 comparison remains unmatched. The distinct TOTASPH C.10 endpoint was read and appears in verified_project_links.tsv.';residual['evidence']='Title PRETOT and narrower content PRETOT A.12 searches found other project prompts, not the requested return. No PRETOT theorem or review status is certified.';leads.append(residual)
  row['to']='TOTASPH C.10';row['what']=row['what'].replace('Verification of TOTASPH’s wording does not identify or certify the unavailable PRETOT A.12 endpoint.','The unavailable PRETOT A.12 endpoint is preserved separately in project_leads.tsv.')
base=[x for x in L if x['kind']!='our projects']
for filename,rows in [('links.tsv',base),('verified_project_links.tsv',verified),('project_leads.tsv',leads)]:
 with (W/filename).open('w') as f:
  w=csv.DictWriter(f,fieldnames=['kind','from','to','what','evidence','note_ids'],delimiter='\t');w.writeheader();w.writerows(rows)

print(json.dumps({'links':len(base),'verified_project_links':len(verified),'reported_project_leads':len(leads),'folder_links':sum(x['kind']=='folder' for x in base),'published_links':sum(x['kind']=='published work' for x in base),'reference_index_method':'literal mention indexing only; meanings and statuses authored after reading'}))
