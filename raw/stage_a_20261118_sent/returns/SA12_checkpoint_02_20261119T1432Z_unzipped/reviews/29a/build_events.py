"""Write events with explicit scope: textual comparison is not proof certification."""
import csv,json
from pathlib import Path
P=Path(__file__).parent
rows=[]
who='GPT-6 Astra Pro; inherited reasoning effort; SA12/review_29a'
def e(i,t,o): rows.append([i,'2026-11-19',who,t,o])
for i in json.loads((P/'items.json').read_text()):
    e(i['id'],'used and rechecked in this run','TEXTUAL SCOPE ONLY: manually compared the entry and actual Pro/Codex passage; '+i['check']+'. '+i['check_reason']+' No mathematical proof certification follows from this event.')
for c in json.loads((P/'claims.json').read_text()):
    e(c['id'],'used and rechecked in this run','STATEMENT/LITERATURE SCOPE ONLY: formulated from the read passage, separated hypotheses and reconstruction, and searched the fate recorded in claims.json/search_log.md. '+c['fate']+' This event alone does not certify the theorem.')
independent={5:'Finite common stratification and conservative stalks prove finiteness of Hom.',16:'Fixed-point sections give the two factors; connected-cover argument gives the product surjection.',26:'Valuative extension, purity and one fixed regular open give compatible model maps; dependent inputs separately cited.',27:'Compactness of one fixed source gives surjectivity onto the model inverse limit.',28:'Normal graph closures and purity give cofinal constancy if a regular proper model exists.',39:'All Frobenius iterates plus the fixed part detect nilpotent and invertible summands; one iterate does not.',40:'Artin–Schreier long exact sequence with H0=k and surjective F−1 gives the fixed-space equality.',41:'Normal-domain integrality argument proves torsion-free root quotient.',68:'Finite-jet dual algebra identities; regularity order is not resolved.',69:'Projection formula evaluated on each test function.',70:'Multiindex total-order filtration for external products.',71:'Derivations identify with the dual of m/m².',72:'First-jet Jacobian chain rule.',73:'Dual of quotient jet algebra equals ideal annihilator.',74:'Group-algebra universal property.',75:'Group algebra commutes with scalar extension.',78:'Cyclic-factor decomposition separates group-scheme length and geometric points.',80:'Coset representatives give free faithful group-algebra extension.',83:'Each finite torsor kills its own H1 class at a finite stage.',86:'Finite-level Cech root cocycle only; no pro-limit realization theorem certified.',88:'Fixed finite coefficient colimit-vanishing argument; no uniform stage in n.',90:'Regular divisor localization supplies the boundary correction.',93:'Root-pair groupoid, fixed L and n invertible: nil-invariant etale site/principal-unit nth roots. Formal effectiveness is not included.'}
for n,o in independent.items(): e(f'CL-SA12-{n:03}','independent re-proof',o+' Full scope in independent_checks.md.')
refuted={20:(18,'Blowup of a surface point creates an exceptional divisor; refutes automatic codimension preservation, not target theorem.'),21:(23,'P²_C over R splits geometrically; later scan113 supplies geometric irreducibility.'),22:(23,'Two planes meeting in a point have a disconnected generic hyperplane section; matches authorial rejection.'),30:(28,'Proper normal rational quotient surface has an étale double cover of its regular locus ramified at a valuation centred on every proper model; cannot extend.'),35:(34,'Exceptional divisor on a blowup refutes Pic(X) restriction isomorphism; proposed corrected letter is Y, undecided on ink.'),37:(33,'α_p⊂α_{p²} refutes points-plus-tangents criterion; no refutation of main Picard theorem.'),47:(46,'α_{p^m} refutes abstract bounded-dimension/geometric-torsion/tangent inference; geometric question remains separate.'),50:(49,'Supersingular elliptic curve refutes use of characteristic-primary rank; refinement requires ell≠p.'),51:(49,'C tensor_R C is a product, not a field; geometric integrality needed.'),84:(83,'P¹ has trivial π1 and nonzero H²(mu_n); unqualified all-curves margin too broad.'),91:(93,'Exact global units and boundary image Za in E×Gm deformation produce nonzero prime-to-characteristic torsion in Pic kernel; formal version also checked.')}
for n,(ref,o) in refuted.items(): e(f'CL-SA12-{n:03}',f'refuted, with refined statement\'s id CL-SA12-{ref:03}',o)
e('SA12-64','independent re-proof','Degree-one line bundle on an elliptic curve gives a nonsplit extension although π2(base)=0. The finite degree-n³ algebraic tame cover and its completion are checked in formal_elliptic_nonsplitting.md, using the opened Mumford theta-pairing theorem. This first tested an earlier-run contextual implication; actual later scan96 explicitly asserts triviality, so the counterexample also bears on root CL-SA12-203. Both transcription endpoints were read.')
e('SA12-8','independent re-proof','Product over distinct primes with unbounded elementary-abelian ranks has finitely many maps to each fixed finite target but is not finitely generated.')
e('SA12-25','independent re-proof','F_p[[T]] semidirect Z_p is generated by two elements while its additive kernel is not finitely generated; abstract warning only, no geometric realization.')
for n,calc in {5:'C01',8:'C02',15:'C02',20:'C03',30:'C04',29:'C05',31:'C05',37:'C06',39:'C07',47:'C06',50:'C08',51:'C09',78:'C10',80:'C11',68:'C12',69:'C12',70:'C12',71:'C12',72:'C17',73:'C18',82:'C13',87:'C15',91:'C16',93:'C16 and C19'}.items():
    e(f'CL-SA12-{n:03}','computation or formal certificate',f'{calc} in checks.py/checks.out. Finite symbolic checks are explicitly bounded examples, not certificates for the entire associated geometric theorem.')
e('SA12-64','computation or formal certificate','C14 finite Heisenberg commutator computation in checks.py/checks.out.')
e('Stacks0C6S',"refuted, with refined statement's id CL-SA12-093",'Opened current Lemma37.4.2; independent E×Gm thickening counterexample refutes unrestricted injectivity of Pic[n]. Its proof suppresses the global-unit connecting quotient. This tag is not carried as reliable background for that assertion.')
rows.append(['CL-SA12-091','2026-11-19','GPT-6 Astra Pro; root independent audit; SA12/root','targeted proof check','Root independently reopened Stacks0C6S and checked global units C* z^Z, the degree-zero H1 summand, boundary image Za, and the formal exponential version. Root-pair refinement remains valid because the power isomorphism reduces to unit z, a nontrivial mu_n torsor even when the underlying line bundle is trivial.'])
for key,o in {
'SGA7_IX':'Original PDF visually read IX7.1.5–7.2.6 pp402–407; exact construction, completion, neutral-component distinction, isotriviality and base-change wording compared. No independent proof of all cited descent results.',
'SGA3_VIII':'Opened primary reedition; VIII§§1–3 statement match and coset-basis argument checked. Reeditor footnote on Hom representability retained.',
'SGA1_1971':'Opened primary reedition; X2.8–2.12 finiteness/hyperplane statements read; broader generic/tame quantifiers not inferred from similarity.',
'DegliseGabber2007':'Opened theorem1.1–1.4 statements; distinguished f* constructibility, R1 conditions, finite H1 and finite generation.',
'ESS2021':'Opened abstract and author PDF; smooth-projective and good-compactification finite-presentation hypotheses read.',
'LSS2023':'Opened arXiv abstract; all connected proper schemes finite presentation and dates checked. Proof not independently rechecked.',
'EK2016':'Opened theorem1.1 and normal-variety comparison; exact Lef/Leff hypotheses read.',
'EKerr2016':'Opened one-page erratum; complete-intersection-of-ample-divisors hypothesis of theorem6.1 restored.',
'KLOS':'Opened author PDF §§10.3.4–5,10.3.9,10.3.13; classical rational Albanese and curve-bound distinction read.',
'Kleiman2005':'Opened Picard scheme paper; Remark5.8 and Ex6.13/Remark6.14 read. No claim this proves nonreduced birational τ invariance.',
'GM1971':'Opened publisher contents and bibliographic page only. Exact object/chapter mapping verified; chapter theorem text inaccessible, so no theorem proof certified.',
'Lipman1974':'Opened §2.4 and preceding proper setting; Pic inverse-limit and global-unit Mittag–Leffler issue read.',
'Stacks0C6R':'Opened exact units/Picard sequence; global-unit boundary retained and used in counterexample.',
'Stacks04DY':'Opened topological invariance statement; applied only to nilpotent finite-level etale/root-pair data.',
'Stacks03PK':'Opened Kummer sequence with n invertible; units/n contribution retained.',
'Stacks0BMB':'Opened purity statement and historical attribution; regularity retained.',
'Stacks0EC0':'Opened Kunz theorem, regular iff Frobenius flat.',
'Stacks0AY6':'Opened reflexive sheaf/codimension-two extension criteria.',
'StacksBlowup':'Opened definition and exceptional Cartier divisor description; matched explicit surface chart.',
'StacksArtinSchreier':'Opened Artin–Schreier sequence and Frobenius-linear lemma59.63.2.',
'StacksSpecialization':'Opened59.75; distinguished geometric specialization direction from special-to-general stalk map.',
'StacksUnramified':'Opened29.36 definitions; object-lifting counterexample does not contradict uniqueness of morphism lifts.'
}.items(): e(key,'used and rechecked in this run',o)
for key,o in {
'KatzLang1981':'Primary Lemma2 and its normalization/fpqc proof read; smooth-surjective normal-base hypotheses matched exactly. Section2 elementary-fibration references traced backward.',
'Mumford1966':'Primary §1 Theorem1 pp293–294 and symmetric multiplication formula p289 read and used in the finite tame-cover construction. The theta-group theorem itself was not independently reproved in full.',
'MoonenTheta':'Opened §§8.1–8.6 and8.24–8.25, version15 September2011; nondegenerate commutator and Heisenberg description compared with the explicit covering group.',
'Sutherland2012':'Opened introduction criterion for supersingularity; combined with independently computed F3 point count, not merely assumed from trace terminology.',
'Schwartz1947':'Opened §1 pp7–9 as historical distribution-calculus background; does not identify the six reused N385 sheets.',
'StacksDivisorLocalization':'Opened §§27–28 and Pic=Cl locally factorial criterion; independently derived the boundary localization consequence.',
'StacksFormalEtale':'Opened infinitesimal unique-lifting definition; did not infer algebraization of an arbitrary formal object.',
'EGAI1960':'Bibliographic metadata opened; exact citation endpoint separately identified in the search/read logs. Metadata access alone is not a theorem match.',
'SGA4I':'Read original PDF I8.13.2–4 pp136–138 and8.3.2–3 pp75–76 visually; hypotheses and small-category/pro-object scope distinguished. Proof of9.11/9.13 not independently checked.'
}.items(): e(key,'used and rechecked in this run',o)
e('PoonenSlavov2020','used and rechecked in this run','Opened Theorem1.8 and Lemma7.1 with§7 proof; checked the deduction that image dimension at least2 makes the bad-hyperplane locus proper. Did not independently reprove the statistical core of Theorem1.5. ArXiv first/revision dates checked at the opened record.')
for key,o in {
'Groth236':'Opened primary Bourbaki exposé236 PDF; used only as a real searched historical Picard source, without claiming it contains the exact nonreduced birational theorem.',
'NeronSamuel1952':'Opened Numdam metadata; historical lead only. Full article theorem text was not checked.',
'RuellingSaito2022':'Opened Corollary11.24; smooth/fibred torsion-Picard comparison distinguished from the normal-source Pic^tau problem.',
'Milne2008':'Opened author lecture notes; standard finite-coefficient curve, Kummer and cohomology framework used with the scopes in claims. No independent whole-course verification.',
'MoonenTateBT':'Opened chapterX10.9 and10.37 for prime-to-characteristic Tate modules and p-rank distinction.',
'ConradPic':'Opened curve Picard handout; proper flat geometrically integral curve hypotheses read. Not used to settle arbitrary normal-source birational invariance.',
'Stacks0CC6':'Opened Frobenius framework; finite-flat application separately restricted to regular finite-type schemes over a perfect field.',
'Stacks0BSE':'Opened tame/Kummer/Abhyankar statement; no blanket extension to every abbreviated formal category.',
'Stacks0G4C':'Opened37.32.1–3 and proof, including geometric irreducibility and base-locus hypotheses.',
'Stacks0BN6':'Opened connected-cover surjectivity criterion; used with normality/connectedness hypotheses retained.',
'Stacks0BUM':'Opened proper homotopy version; does not settle the draft nonproper adjective.',
'Stacks0BQJ':'Opened normalization/finite-cover framework; no generic descent theorem inferred from title alone.',
'Stacks0BX7':'Opened proper-target rational-map extension input; arbitrary dominance was not used as a pi1-surjectivity criterion.'
}.items(): e(key,'used and rechecked in this run',o)
for key in ['ContextLM1E11','ContextLM1E2','ContextMPL11Cote56','ContextHua29','ContextResults29','GiraudLetter','Jouanolou1983','SGA4XI','SGA2Picard']:
    e(key,'used and rechecked in this run','ATTRIBUTION ONLY: the reference or project label was read in an available source and retained as a lead. The referenced target was not opened by this reviewer; no result or proof status is certified. See references.bib annote and links.tsv.')
with (P/'CHECK_EVENTS.tsv').open('w') as f:
    w=csv.writer(f,delimiter='\t',lineterminator='\n');w.writerow(['statement_id','date','who','type','outcome']);w.writerows(rows)
print(f'{len(rows)} scoped check events saved.')
