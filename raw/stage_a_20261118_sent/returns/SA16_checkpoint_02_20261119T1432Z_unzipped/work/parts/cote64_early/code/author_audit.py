"""Serialize the research audit. All substantive decisions below are authored.

Reading/computation claims are not generated from note headings. The source-log
extractor retains exact recorded requests and retrieval identifiers, not excerpts.
Raw external text is retained only in the excluded external_cache directory.
"""
import csv, json, re, shutil, hashlib
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
WORKSPACE=ROOT.parents[2]
CACHE=WORKSPACE/'external_cache'/'cote64_early'
CACHE.mkdir(parents=True,exist_ok=True)
DATE='2026-11-19'
WHO='GPT-6 Astra Pro; effort inherited/unspecified; run SA16-2026-11-19-cote64-early'
items=json.loads((ROOT/'items.json').read_text())
claims=json.loads((ROOT/'claims.json').read_text())
problems=json.loads((ROOT/'problems.json').read_text())

def tsv(name,rows,fields=None):
    with (ROOT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields or list(rows[0]),delimiter='\t')
        w.writeheader();w.writerows(rows)

# A URL being opened and an exact theorem being checked are distinct statuses.
refs=[]
def ref(key,kind,fields,locator,used,limit,events,batches):
    fields=dict(fields)
    fields.setdefault('note','verified')
    refs.append({'key':key,'kind':kind,'fields':fields,'locator':locator,
      'used':used,'limit':limit,'events':events,'batches':batches})

ref('Burnside1897','book',dict(author='William Burnside',title='Theory of Groups of Finite Order',publisher='Cambridge University Press',year='1897',edition='1',url='https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/burnside1897b.pdf'),
 'Sections 142, 171–173; Theorem VIII in section 173, printed p. 271; sections 202–203, printed pp. 317–323.',
 'Opened the finite permutation, automorphism, dihedral and cube passages. The S4/D8 computations are independently reproduced in this run.',
 'The exact modern torsor dictionaries and the full 30-node Hasse diagram are not attributed to this book. Earlier Hölder priority was not established from the original.',
 'used and rechecked in this run',[4,5,9,15,16,17,18,19,20,21,22])
ref('BrauJones2016','article',dict(author='Julio Brau and Nathan Jones',title='Elliptic curves with 2-torsion contained in the 3-torsion field',journal='Proceedings of the American Mathematical Society',volume='144',pages='925--936',year='2016',doi='10.1090/proc/12786',url='https://homepages.math.uic.edu/~ncjones/2tin3t.pdf',eprint='1406.1262',archivePrefix='arXiv'),
 'Proof of Lemma 3.1, equation (26) and the two invariant planes, author PDF pp. 7–8.',
 'Compared the split GL2(Z/4) action and both F2 planes with the explicit matrix certificate.',
 'First arXiv circulation 2014-06-05; electronic publication 2015-07-08; volume publication 2016. The canonical square/module equivalence is not printed there.',
 'targeted proof check',[2,3,4,5,18,32,33])
ref('Beauville2010','incollection',dict(author='Arnaud Beauville',title='Finite subgroups of PGL(2,K)',booktitle='Vector Bundles and Complex Geometry',series='Contemporary Mathematics',volume='522',pages='23--29',year='2010',url='https://math.univ-cotedazur.fr/u/beauvill/pubs/PGL%282%29.pdf',eprint='0909.3942',archivePrefix='arXiv'),
 'Proposition 1.1 and proof of Theorem 4.2, case 3 (Klein normalizer).',
 'Read the field rationality restrictions and normalizer generators; compared with the structured octahedral local model.',
 'First arXiv 2009-09-22. The paper adopts a prime-to-characteristic convention and does not supply our arbitrary-base characteristic-3 argument.',
 'used and rechecked in this run',[3,4,5,9,16,23,26,27])
ref('DetinkoFlanneryHulpke2018','article',dict(author='Alla Detinko and Dane Flannery and Alexander Hulpke',title='Zariski Density and Computing in Arithmetic Groups',journal='Mathematics of Computation',volume='87',pages='967--986',year='2018',doi='10.1090/mcom/3236',url='https://arxiv.org/pdf/1611.05921',eprint='1611.05921',archivePrefix='arXiv'),
 'Theorem 2.5 and Lemma 2.6, opened revision v4, pp. 4–5.',
 'Read proper-supplement hypotheses and the trace-zero congruence kernel. Distinguished supplement from complement before proving SL nonsplitting independently.',
 'First arXiv 2016-11-17; publication 2018; opened v4 dated 2022-11-04. Theorem 2.5 must not be quoted as the exact nonsplitting statement.',
 'used and rechecked in this run',[6,7,8,9,10,12,13,25,31,33])
ref('Hua2026','misc',dict(author='Michel Hua',title="Énoncés des notes de travail de Grothendieck démontrés en Lean 4, et questions ouvertes",year='2026',month='November',howpublished='Author preprint, version 2',url='https://hexagonmath.org/pdf/2611.00125v2'),
 'Section 42, Theorem 42.1 and Counterexample 42.2, printed pp. 194–195 (PDF pp. 193–194).',
 'Read the characteristic-5 fixer argument and counterexample, and the explicit statement that the relative correspondence and mu4 refinement are not established there.',
 'Treat as an author reconstruction and November 2026 preprint. No Lean source was compiled or independently certified. This does not validate an unseen earlier Hua research report.',
 'targeted proof check',[11,12,13])
ref('SGA1','book',dict(author='Alexander Grothendieck and collaborators',title='Revêtements étales et groupe fondamental (SGA 1)',series='Lecture Notes in Mathematics',volume='224',publisher='Springer',year='1971',doi='10.1007/BFb0058656',url='https://arxiv.org/pdf/math/0206203',eprint='math/0206203',archivePrefix='arXiv'),
 'V Theorem 4.1 (retyped p. 104); VIII Theorem 2.1 (p. 158); IX Proposition 4.1 (p. 182); XI section 4 after Proposition 4.3 (pp. 227–228); XIII sections 2.0–2.1.5 (pp. 276–279).',
 'Read finite Galois categories, effective affine and finite-etale descent, the associated-bundle construction, and tame cyclic local inertia with its relative hypotheses.',
 'Seminar 1960–61; book 1971; retyped edition 2003, opened arXiv v2 2004-01-04. These are framework results, not exact statements of all manuscript dictionaries; no full independent proof of SGA is claimed.',
 'used and rechecked in this run',[6,7,8,9,10,16,18,23,24,27,28,29,30,31,32])
ref('MerkurjevScavia2024','misc',dict(author='Alexander Merkurjev and Federico Scavia',title='Lectures on the Massey Vanishing Conjecture',year='2024',month='July',howpublished='PCMI lecture notes',url='https://www.ias.edu/sites/default/files/pcmi-2024-07-04_0.pdf'),
 'Section 1.1, equations (1.3)–(1.4) and Example 1.4, pp. 3–4; the p=2 unipotent interpretation.',
 'Checked the explicit cocycle and cup-product lifting criterion against the D8 factor-set calculation.',
 'This source is a profinite/field statement. The site formulation and the octahedral interpretation are our separately labelled argument. No earliest-priority claim.',
 'targeted proof check',[17,18,19,20,24])
ref('Ledet2001','article',dict(author='Arne Ledet',title='Embedding problems and equivalence of quadratic forms',journal='Mathematica Scandinavica',volume='88',number='2',pages='279--302',year='2001',doi='10.7146/math.scand.a-14327',url='https://journals.msp.org/mscand/article/view/878',note='unverified'),
 'Bibliographic landing page opened; the proposed section 0.4 could not be accessed.',
 'Retained as a documented earlier-reference lead, not support for an exact theorem.',
 'Landing metadata gives publication 2001-06-01. Repeated PDF/author-site attempts failed. The exact result remains unverified despite verified bibliographic existence.',
 'carried as background without fault found',[1,4,5,6,7,8,9,14,15,16,17])
ref('Milnor2004','incollection',dict(author='John Milnor',title='On Lattès Maps',booktitle='Dynamics on the Riemann Sphere',publisher='European Mathematical Society',pages='9--43',year='2006',doi='10.4171/011-1/1',url='https://arxiv.org/pdf/math/0402147',eprint='math/0402147',archivePrefix='arXiv'),
 'Theorem 3.1, preprint pp. 3–4; local-degree equation (3), p. 5.',
 'Read the quotient of affine torus maps and local-degree mechanism. The exact normalized rational function and its algebraic multiplicities are independently checked here.',
 'First arXiv 2004-02-09; revised 2004-09-22; EMS publication 2006-01-10. Historical Lattès 1918 attribution is reported by Milnor; the original volume could not be opened.',
 'used and rechecked in this run',[6,7,8,9,10,13,20,26,33,34])
ref('Lattes1918','article',dict(author='Samuel Lattès',title="Sur l'itération des substitutions rationnelles et les fonctions de Poincaré",journal="Comptes rendus de l'Académie des sciences",volume='166',pages='26--28',year='1918',url='https://upload.wikimedia.org/wikipedia/commons/c/cf/Comptes_rendus_hebdomadaires_des_s%C3%A9ances_de_l%27Acad%C3%A9mie_des_sciences_%28IA_comptesrendusheb166acad%29.pdf',note='unverified'),
 'Original pp. 26–28 sought through the complete 1918 volume.',
 'Historical reference followed backwards from Milnor; no exact formula attributed to the inaccessible original.',
 'Web reader rejected the approximately 59 MB PDF. Bibliographic attribution is secondary to Milnor in this dossier.',
 'carried as background without fault found',[7,20,26,33])
ref('ConradLevel','misc',dict(author='Brian Conrad',title='Isogenies and level structures',howpublished='Math 248B handout',url='https://math.stanford.edu/~conrad/248BPage/handouts/level.pdf'),
 'Section 1; Definition 2.7 and Remark 2.8, p. 6; Proposition 3.1 and Proposition 3.2, pp. 7–8.',
 'Read the local coordinate proof of the canonical Legendre structure from P in E[2] and Q4 in E[4], its base-change compatibility, and sign reversal under Q4 -> -Q4.',
 'Undated handout; do not invent circulation date. Remark 2.8 excludes a natural ordinary S3 action. This construction is not automatically the later symmetric mu4 normalization.',
 'targeted proof check',[19,23,24,25])
ref('AntieauMeier2020','article',dict(author='Benjamin Antieau and Lennart Meier',title='The Brauer group of the moduli stack of elliptic curves',journal='Algebra & Number Theory',volume='14',number='9',pages='2295--2333',year='2020',doi='10.2140/ant.2020.14.2295',url='https://arxiv.org/pdf/1608.00851',eprint='1608.00851',archivePrefix='arXiv'),
 'Definition 4.4, Proposition 4.5 and Lemma 4.7, preprint pp. 14–16.',
 'Read the local Legendre normalization, the mu2 automorphism calculation, and the twisted S3 action on the atlas.',
 'First arXiv 2016-08-02; opened v3 2020-05-05; journal 2020. It proves the usual root-torsor mechanism, not the special manuscript mu4 normalization.',
 'targeted proof check',[19,23,24,33,34,35,36])
ref('Stacks0BD2','misc',dict(author='The Stacks Project Authors',title='The Stacks Project, Tag 0BD2',url='https://stacks.math.columbia.edu/tag/0BD2',howpublished='Accessed 2026-11-19'),
 'Lemma 31.18.6, the finite locally free norm and base change.',
 'Compared the determinant-norm convention with the local multiplication matrix.',
 'The sign in the tangent/leading-jet comparison is independently computed, not borrowed from this general statement.',
 'used and rechecked in this run',[6])
ref('Stacks03PK','misc',dict(author='The Stacks Project Authors',title='The Stacks Project, Kummer theory, Tag 03PK',url='https://stacks.math.columbia.edu/tag/03PK',howpublished='Accessed 2026-11-19'),
 'Lemma 59.28.1; equation 59.28.4.1; Lemma 59.28.5.',
 'Read the n-invertible Kummer sequence, root-pair isomorphism torsor and line-bundle classification.',
 'A root has mu_n automorphisms; the exact isomorphism statement is used, without replacing a groupoid by a set or claiming a global section.',
 'used and rechecked in this run',[7,8,9,10,12])
ref('StacksProjectiveBundle','misc',dict(author='The Stacks Project Authors',title='The Stacks Project, Projective bundles, Tag 01OA',url='https://stacks.math.columbia.edu/tag/01OA',howpublished='Accessed 2026-11-19'),
 'Section 27.21, Definition 27.21.1 and the universal invertible quotient.',
 'Read the quotient convention before deriving the rank-two tangent formula.',
 'The determinant sign-line identification is the current independent proof, not an assertion that this tag states the manuscript formula.',
 'used and rechecked in this run',[25,26])
ref('EGAII','article',dict(author='Alexander Grothendieck and Jean Dieudonné',title="Éléments de géométrie algébrique II. Étude globale élémentaire de quelques classes de morphismes",journal="Publications Mathématiques de l'IHÉS",volume='8',pages='5--222',year='1961',doi='10.1007/BF02699291',url='https://www.numdam.org/item/PMIHES_1961__8__5_0/'),
 'Proposition 4.1.6; Proposition 4.2.3 and Theorem 4.2.4; section 4.2.8–10, printed pp. 72–76.',
 'Read the tautological surjection, the invertible-quotient universal property and its base-change compatibility directly in the downloaded primary PDF. Compared the quotient convention with the tangent calculation.',
 'Publication 1961; received 1960-07-22. Full PDF and extracted text are excluded external cache. This section establishes the projective convention; the orientation sign-line tangent formula is our independent derivation.',
 'used and rechecked in this run',[25,26,27,31])
ref('MO443624','misc',dict(author='Alexander Hulpke and contributors',title='Does the map SL(n,Z/p^2) to SL(n,Z/p) split?',howpublished='MathOverflow question 443624',year='2023',url='https://mathoverflow.net/questions/443624/does-the-map-mathrmsln-mathbbz-p2-rightarrow-mathrmsln-mathbbz'),
 'Answer by ahulpke, 2023-03-28, corrected at 17:56.',
 'Read the explicit correction distinguishing supplements and complements and followed its primary-paper reference.',
 'Discovery and correction chain only; the SL2(Z/4) nonsplitting is proved directly in this dossier.',
 'used and rechecked in this run',[5,25,30,31])
ref('MO275292','misc',dict(author='David Speyer and Noam Elkies and contributors',title='Is every GL(2,Z/nZ) extension contained in some elliptic curve torsion field?',howpublished='MathOverflow question 275292 and comments',year='2017',url='https://mathoverflow.net/questions/275292/is-every-gl-2-mathbbz-n-mathbbz-extension-contained-in-some-elliptic-cur'),
 'Discussion dated 2017-07-12–14; correction from GL to PGL in the octahedral observation.',
 'Read the order-96/order-48 correction and compared it with the explicit action.',
 'Do not use the subsequent abbreviated S4 wording to drop the central C2. Our finite certificate determines the precise group.',
 'used and rechecked in this run',[18,25,30,31,32])
ref('Katz1970','article',dict(author='Nicholas M. Katz',title='Nilpotent connections and the monodromy theorem: applications of a result of Turrittin',journal="Publications Mathématiques de l'IHÉS",volume='39',pages='175--232',year='1970',doi='10.1007/BF02684688',url='https://web.math.princeton.edu/~nmk/old/nilpconn.pdf'),
 'Theorem 7.4, Corollary 7.5, printed p. 203; Theorem 10.0, printed pp. 209–210.',
 'Read smooth/proper, local-freeness and Frobenius/base-change hypotheses relevant to the earlier-run connection comparison.',
 'Background for SA16-207 only; no connection is constructed by these finite-module pages and no independent proof of Katz is claimed.',
 'carried as background without fault found',[27,28,35,36])
ref('OgusVologodsky2007','article',dict(author='Arthur Ogus and Vadim Vologodsky',title='Nonabelian Hodge theory in characteristic p',journal="Publications Mathématiques de l'IHÉS",volume='106',pages='1--138',year='2007',doi='10.1007/s10240-007-0010-z',url='https://www.numdam.org/item/10.1007/s10240-007-0010-z.pdf'),
 'Remark 2.2, printed p. 26; Theorem 2.8, printed p. 33.',
 'Read zero-p-curvature Cartier descent and the lifting/nilpotence hypotheses in the nonabelian correspondence.',
 'Background for SA16-207; no inference from finite torsors to a connection. The full theorem was not independently reproved.',
 'carried as background without fault found',[27,28,29,34,35,36])
ref('BouwWewers2006','article',dict(author='Irene I. Bouw and Stefan Wewers',title='Indigenous bundles with nilpotent p-curvature',journal='International Mathematics Research Notices',volume='2006',pages='Article 89254',year='2006',doi='10.1155/IMRN/2006/89254',url='https://arxiv.org/pdf/math/0505275',eprint='math/0505275',archivePrefix='arXiv'),
 'Definition 2.1, preprint p. 4; section 3.1, p. 5; section 5 differential-equation framework.',
 'Read the indigenous-bundle conditions, nontrivial marked monodromy, odd characteristic and active/nilpotent distinctions.',
 'Opened preprint v2 dated 2005-08-18; publication 2006 verified via author bibliography. Background for SA16-208, not a theorem about the manuscript finite objects.',
 'carried as background without fault found',[27,28,29,33,34,35,36])
ref('Hoshi2015','misc',dict(author='Yuichiro Hoshi',title='Nilpotent Admissible Indigenous Bundles via Cartier Operators in Characteristic Three',year='2015',month='April',howpublished='Author preprint',url='https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1811revised.pdf'),
 'Introduction hypotheses and Theorem B, pp. 3–4, referring to Theorem 5.2.',
 'Read the characteristic-3 Cartier criterion and its smooth/proper genus-at-least-two setting.',
 'Background for SA16-208; it does not identify the finite pinning data with an indigenous bundle. Journal metadata from the old notes is not relied on without a separately opened source.',
 'carried as background without fault found',[27,28,29,35,36])
ref('GrothendieckBibliography','misc',dict(author='Cercle des Savoirs Grothendieck',title='Published works of Alexander Grothendieck',url='https://csg.igrothendieck.org/published-works/',howpublished='Accessed 2026-11-19'),
 'Published-works bibliography.',
 'Opened as a bibliographic search endpoint for exact-work follow-up.',
 'An index is not proof of absence of a theorem, and does not validate unavailable project archives.',
 'used and rechecked in this run',[24])

# A family is an explicitly chosen coherent literature question; the map below is
# a coverage declaration, not an algorithmic verdict or classification.
family_batches={
 'FINITE':[4,5,9,14,15,16,17,18,19,20,21,22,23,24,30,31,32],
 'MOD4':[4,5,6,7,8,9,10,12,13,14,18,19,23,24,25,30,31,32,33],
 'LIFTING':[4,6,7,8,9,14,15,16,17,18,19,20,24,27,31,32],
 'OCTAHEDRAL':[4,5,9,11,12,13,16,18,23,24,26,27,32],
 'TWISTS':[6,7,10,16,19,20,23,24,27,28,29,30,31,32],
 'DOUBLING':[6,7,8,9,10,13,19,20,25,26,33,34],
 'KUMMER':[6,7,8,9,10,12,19,23,24,27,28,29,30,31,32,35,36],
 'PINNING':[6,7,8,10,11,12,13,19,23,24,25,26,27,31,32,33,34,35,36]
}
family_scope={
 'FINITE':'Classical S4/D8, square and cube constructions; exact groupoid-packaging and orientation-convention searches.',
 'MOD4':'GL2/SL2 over Z/4, invariant planes, splitting, projective octahedron and canonical torsor package.',
 'LIFTING':'Central D8/unipotent embedding, cup obstruction, site versus field hypotheses, Ledet backward search.',
 'OCTAHEDRAL':'Klein normalizers, relative octahedral configurations, characteristic-5 exception and orientation.',
 'TWISTS':'Effective descent, cubic trace conic, marked Klein torsors and genus-one involution construction.',
 'DOUBLING':'Legendre duplication, Lattes multiplication quotients, historical Lattes source and ramification multiplicities.',
 'KUMMER':'Tame local inertia, tangent-root categories, norm, Kummer automorphisms, quadratic Legendre specialization.',
 'PINNING':'Projective tangent convention, root torsors, Legendre atlas, level-four construction and symmetric mu4 normalization.'
}
outcomes={
 1:'Early discovery batch; original exact request was not saved. Ledet bibliographic lead only. Later recorded queries repeat the research question.',
 2:'Early discovery batch; original exact request was not saved. Official Brau–Jones metadata located; exact formulas opened subsequently.',
 3:'Early discovery batch; original exact request was not saved. Author PDFs for Brau–Jones and Beauville opened; subsequent exact requests are retained.',
 4:'Opened arXiv dates, Ledet landing and Burnside; located the Brau–Jones invariant-plane table and Beauville normalizer passage.',
 5:'Repository searches yielded modern mod-4 references and no exact octahedral relative theorem; Ledet link and finite-group passages followed.',
 6:'Norm lemma opened. SGA/Milnor/Pardini discovery; DFH DOI and Ledet PDF routes failed. No theorem adopted from an inaccessible source.',
 7:'SGA1, Milnor abstract and Pardini metadata opened; Kummer and congruence-group exact sources located; Ledet PDF route failed.',
 8:'DFH, Milnor and Stacks Kummer primary sources opened; exact theorem locators then followed. Ledet PDF route remained inaccessible.',
 9:'Located exact supplement, Lattes and root-pair statements; backward searches for Ledet/Hölder and targeted PGL/octahedral searches did not settle exact packaging.',
 10:'Read DFH Theorem 2.5, Milnor Theorem 3.1, Kummer root formula and SGA1 V Theorem 4.1 at exact passages.',
 11:'Opened Hua November 2026 preprint; searched within its long PDF before reading the relevant section.',
 12:'Located Hua section 42, checked supplement wording and exact Kummer root-pair isomorphism formula.',
 13:'Read Hua characteristic-5 exception and its expressly unproved relative extensions; checked DFH and Milnor exact statements.',
 14:'Exact square/module and dihedral-embedding searches found no independent canonical-package theorem. One literal query has site.zbmath.org, preserved as entered.',
 15:'Ledet PDF and author-publications access attempts failed; Burnside exact group sections located.',
 16:'Ledet landing metadata read; finite and cup-obstruction searches continued, including literal site.numdam.org and site.zbmath.org spellings.',
 17:'U3/cup-product searches found the precise Merkurjev–Scavia route; a Numdam dihedral-obstruction search did not establish the manuscript application.',
 18:'Opened Merkurjev–Scavia and Burnside; an elliptic-twists source proved peripheral. Followed primary finite-group and GL/PGL references.',
 19:'Opened Conrad and Antieau–Meier, plus Burnside. An unrelated twist source is not used as support. Located exact cup equations.',
 20:'Read cup-product calculation and finite-group statements; searched backwards to Lattes 1918 and for genus-one involution and Legendre duplication formulations.',
 21:'Located Burnside exact symmetric, dihedral and polyhedral sections.',
 22:'Read Burnside automorphism theorem and cube/dihedral passages directly; corrected the section citation to 203.',
 23:'Exact manuscript square/module and scheme/Klein searches did not find a fully matching independent theorem; obtained Antieau–Meier version dates and Conrad exact targets.',
 24:'Read Conrad no-ordinary-S3 warning, Antieau–Meier root atlas, Merkurjev–Scavia Example 1.4, and Grothendieck published-works bibliography.',
 25:'Read both MathOverflow correction chains, Stacks projective convention and Conrad Proposition 3.2. EGA full-PDF web access exceeded size limit.',
 26:'Searched EGA projective-bundle section and Euler convention, zbMATH Beauville and Numdam historical Lattes. Exact EGA extraction required a separate download.',
 27:'EGA web PDF and direct zbMATH page did not provide readable full text; Katz, Ogus–Vologodsky, Bouw–Wewers and Hoshi opened; SGA locators found.',
 28:'Located exact background hypotheses and read SGA tame/descent passages.',
 29:'Read background exact theorem hypotheses and SGA local tame passage. One SGA request landed in the wrong exposé; exact VIII theorem was subsequently read in batch 32.',
 30:'Located SGA associated-bundle and descent passages and both MathOverflow corrections; a literal contracted-product search had no exact match.',
 31:'Read SGA associated bundles, both MO corrections and Numdam EGA metadata. Affine-descent exact location was completed in batch 32; a course Euler calculation was background only.',
 32:'Direct searches for tangent Kummer, cubic trace conic, reflection groupoid and mu4 pinning found no fully matching general theorem. SGA VIII Theorem 2.1 and exact MO correction read; Brau DOI route failed.',
 33:'Verified publication metadata using official/author search results; opened DFH version history. The original Lattes volume exceeded the web-reader size limit.',
 34:'Read EMS publication date and Bouw author bibliography. Antieau DOI access failed; its primary arXiv PDF is the mathematical source. OV request landed near a different result and was followed correctly in batch 36.',
 35:'Located exact background theorem statements; read Antieau–Meier local proof beginning.',
 36:'Read Katz Theorem 10.0, OV Remark 2.2, Bouw–Wewers Definition 2.1, Hoshi Theorem B, and Antieau–Meier root-atlas proof.'
}

def extract_metadata(value):
    # Preserve IDs, URLs and provider source commands, without copyrighted prose.
    texts=[]
    def walk(v):
        if isinstance(v,dict):
            if v.get('type')=='text' and isinstance(v.get('text'),str): texts.append(v['text'])
            else:
                for x in v.values(): walk(x)
        elif isinstance(v,list):
            for x in v: walk(x)
    walk(value)
    text='\n'.join(texts)
    ids=sorted(set(re.findall(r'【([^】]+)】',text)))
    urls=sorted(set(re.findall(r'https?://[^\s<>"\\]+',text)))
    urls=[u.rstrip(').,;') for u in urls]
    commands=re.findall(r'Source: ([^\n]+)',text)
    return {'source_ref_ids':ids,'urls':urls,'provider_source_commands':commands}

logs=[]
for p in sorted((ROOT/'outputs').glob('web_*.json')):
    n=int(p.stem.split('_')[1]); rawpath=CACHE/p.name
    if not rawpath.exists(): shutil.copy2(p,rawpath)
    raw=json.loads(rawpath.read_text())
    request=raw.get('request')
    meta=extract_metadata(raw.get('result',raw))
    clean={'batch':n,'date':DATE,'request':request,
      'request_record_status':'exact recorded request' if request is not None else 'early request not saved; subsequent exact searches retained',
      **meta,'researcher_outcome':outcomes[n],
      'raw_external_text_location':'excluded external_cache/cote64_early/'+p.name}
    p.write_text(json.dumps(clean,ensure_ascii=False,indent=2)+'\n')
    fams=[k for k,v in family_batches.items() if n in v]
    if request is None:
        operations=[('unrecorded_early_discovery',{})]
    else:
        operations=[(op,arg) for op,args in request.items() if isinstance(args,list) for arg in args]
    for j,(op,arg) in enumerate(operations,1):
        q=arg.get('q','')
        target=arg.get('ref_id','')
        repos=[r for r,token in [('zbMATH Open','zbmath'),('arXiv','arxiv'),('MathOverflow','mathoverflow'),('Numdam','numdam'),('EGA','EGA'),('SGA','SGA'),('Grothendieck bibliography','igrothendieck'),('author site','~'),('Stacks Project','stacks.math')] if token.lower() in (q+' '+target).lower()]
        logs.append({'search_id':f'CE-S{n:03}-{j:02}','date':DATE,'operation':op,
          'exact_query_or_target':q or target,'exact_arguments_json':json.dumps(arg,ensure_ascii=False),
          'repositories':'; '.join(repos) or 'general web / source follow-up',
          'families':';'.join(fams),'claim_ids':';'.join(c['id'] for c in claims if c['literature_search_group'] in fams),
          'source_ref_ids':';'.join(meta['source_ref_ids']),
          'result':outcomes[n], 'record':'outputs/'+p.name})
logs.append({'search_id':'CE-EGA-01','date':DATE,'operation':'open',
  'exact_query_or_target':'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EGA/EGAII.pdf',
  'exact_arguments_json':json.dumps({'download':'urllib.request.urlretrieve','extract':['pdftotext','-layout'],'read_printed_pages':'72–76','read_sections':'4.1.5–4.2.10'},ensure_ascii=False),
  'repositories':'EGA; author archive mirror','families':'PINNING',
  'claim_ids':';'.join(c['id'] for c in claims if c['literature_search_group']=='PINNING'),
  'source_ref_ids':'Numdam metadata turn599533948view4; downloaded-primary-PDF checksum in EGAII_source.json',
  'result':'Completed the 24,238,251-byte source download, extracted text and read the exact tautological-quotient and universal-property passages. The orientation tangent formula remains the separate independent proof.',
  'record':'outputs/EGAII_source.json'})
tsv('search_log.tsv',logs)

coverage=[]
for c in claims:
    group=c['literature_search_group']; chosen=[r for r in logs if group in r['families'].split(';')]
    query=[r['search_id'] for r in chosen if 'search_query' in r['operation']]
    opened=[r['search_id'] for r in chosen if r['operation'] in ('open','find','click')]
    coverage.append({'claim_id':c['id'],'family':group,'scope':family_scope[group],
      'exact_search_ids':';'.join(query),'opened_followup_ids':';'.join(opened),
      'primary_refs_used':';'.join(c['refs']),'exact_match_and_limit':c['fate'],
      'status':'searched; an unmatched exact formulation is not treated as proved by a broad citation'})
tsv('claim_search_coverage.tsv',coverage)

with (ROOT/'references.bib').open('w') as f:
    for r in refs:
        f.write('@'+r['kind']+'{'+r['key']+',\n')
        for k,v in r['fields'].items():
            # Existing titles contain no unbalanced TeX braces.
            f.write('  '+k+' = {'+v.replace('&','\\&')+'},\n')
        f.write('  annote = {'+r['limit']+'}\n}\n\n')
tsv('reference_audit.tsv',[{'key':r['key'],'date':DATE,'url_opened':r['fields']['url'],
 'bibliography_note':r['fields']['note'],'exact_locator':r['locator'],
 'what_was_read_and_used':r['used'],'hypothesis_and_access_limits':r['limit'],
 'check_type':r['events'],'source_batches':';'.join(f'web_{n:03}' for n in r['batches'])} for r in refs])

events=[]
def event(s,typ,out,artifact='',scope=''):
    events.append({'statement_id':s,'date':DATE,'who':WHO,'type':typ,'outcome':out,
      'artifact':artifact,'scope':scope})
for it in items:
    event(it['id'],'used and rechecked in this run',
      'Compared the complete source-note entry/entries with the cited actual transcript passage: '+it['check']+'. '+it['check_reason'],
      'items.json; entries.tsv','Text comparison only; this event does not assert a mathematical proof check or an ink decision.')
for c in claims:
    event(c['id'],'used and rechecked in this run',
      'Read the recorded manuscript assertion and context; '+c['status_on_pages']+'. Literature fate searched: '+c['fate'],
      'claims.json; claim_search_coverage.tsv','Statement/hypothesis comparison and literature matching, not automatically a proof check.')

proof_sections={
 1:[211,213,215,224,305],2:[216,217,220,221,222,228,306,322,328],
 3:[226,229,230,330],4:[231,233,234,235,237,238,239,240,241,242,243,286,307],
 5:[244,245,246],6:[261,262,263,265,267,363],7:[260,269,270,271,273,275],
 8:[277,279,280,282,379,382],9:[289,290,291,292,293,391],10:[295,296,297,298]}
claim_by_n={int(c['id'].split('-')[-1]):c for c in claims}
for sec,ns in proof_sections.items():
    for n in ns:
        c=claim_by_n[n]
        event(c['id'],'independent re-proof',
          c['present_status'],f'proof_supplement.md section {sec}',
          'The proof establishes only the qualified result stated in the outcome. For C-SA16-391 it proves necessity of the correction, not the full candidate equivalence.')

computations={
 'finite_groups':[211,213,214,216,217,220,221,224,226,228,231,233,234,235,237,238,239,240,241,242,244,245,246,274,286,305,306,322,328],
 'cube_and_pgl':[229,230,261,262,263,265,330,363],
 'symbolic_checks':[270,271,277,279,280,282,289,379,382],
 'kummer_counterexample':[291,391],
 'scalar_quotient':[307]}
for program,ns in computations.items():
    for n in ns:
        c=claim_by_n[n]
        event(c['id'],'computation or formal certificate',c['computation'],
          f'code/{program}.py; outputs/{program}.json',
          'Executable finite/symbolic calculation, not a Lean certificate or a proof of an arbitrary-base assertion from finite samples.')
for n,refined in [(214,213),(216,306),(222,322),(228,328),(230,330),(263,363),(279,379),(282,382),(291,391)]:
    event(f'C-SA16-{n}',f'refuted, with the refined statement\'s id C-SA16-{refined}',claim_by_n[n]['present_status'],
      'claims.json; proof_supplement.md','Refutes the stated literal reading or unrestricted formulation; it does not decide the handwritten ink.')
for r in refs:
    event(r['key'],r['events'],r['used']+' '+r['limit'],
      'reference_audit.tsv; '+r['locator'],
      'Exact opened-result scope is stated here. Bibliographic metadata and an unavailable proposed theorem remain distinct.')
# Background-boundary comparisons are separate from the manuscript passage event.
event('SA16-207','used and rechecked in this run','Checked Katz and Ogus–Vologodsky hypotheses; no connection, p-curvature or lifting datum is supplied by the finite-module passage.','reference_audit.tsv: Katz1970; OgusVologodsky2007','Literature comparison only; no proof of either full theorem.')
event('SA16-208','used and rechecked in this run','Checked Bouw–Wewers and Hoshi definitions and characteristic/genus hypotheses; no indigenous bundle is constructed in the local manuscript passage.','reference_audit.tsv: BouwWewers2006; Hoshi2015','Literature comparison only; external project endpoints remain unavailable.')
event('SA16-203','computation or formal certificate','The earlier-run quarter-turn matrix has projective cycle lengths 4,1,1, determinant +1 and odd reduction sign.','code/finite_groups.py; outputs/finite_groups.json','Finite example only; no cusp endpoint was checked.')
tsv('check_events.tsv',events)

# Read coverage is a declaration of manual reading already performed; hashing does
# not infer that reading happened. It permits the recipient to identify the inputs.
manifest=[]
for package in ('MPL_64_002-039','MPL_64_040-077'):
    for sub,suffix in [('SA16_texts','transcription.tex'),('SA16_notes','notes.md'),('SA16_notes','doubts.md')]:
        p=WORKSPACE/'sources'/sub/'pro'/f'{package}_{suffix}'
        raw=p.read_bytes(); lines=raw.decode().splitlines()
        manifest.append({'file':str(p.relative_to(WORKSPACE)),'sha256':hashlib.sha256(raw).hexdigest(),
          'physical_lines':len(lines),'reading':'Read in full in this live run before consolidation; relevant passages were re-read during authoring.',
          'limitation':'No scan images or second-pass correction files supplied for these two packages.'})
tsv('read_manifest.tsv',manifest)

if __name__=='__main__':
    result={'references':len(refs),'search_operations':len(logs),
      'claim_search_rows':len(coverage),'check_events':len(events),'source_files_read':len(manifest)}
    (ROOT/'outputs'/'author_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
