"""Serialize manually checked source metadata and the exact final search batches.

This script does not infer mathematical verdicts. Source summaries and limits are
human-authored by the reviewing agent after opening the indicated passages.
"""
from pathlib import Path
import csv, json, re, shutil, hashlib
from datetime import datetime, timezone

B=Path(__file__).resolve().parents[1]
ROOT=B.parents[2]
CACHE=ROOT/'external_cache'/'cote64_late'
CACHE.mkdir(parents=True,exist_ok=True)
DATE='2026-11-19'
R=[]
def ref(key,typ,title,author,year,url,locator,summary,history='',**extra):
    R.append(dict(key=key,type=typ,title=title,author=author,year=year,url=url,
                  locator=locator,summary=summary,history=history,note=extra.pop('note','verified'),**extra))

ref('AntieauMeier2020','article','The Brauer group of the moduli stack of elliptic curves',
    'Benjamin Antieau and Lennart Meier','2020','https://arxiv.org/pdf/1608.00851',
    'Definition 4.4; Proposition 4.5; Lemma 4.7',
    'The ordered level-two stack has a Legendre presentation as a C2 root gerbe. Its S3 symmetry is twisted. This is an exact local comparison for square-root reconstruction, but it does not assert the manuscript’s symmetric μ4-equivariant pinning normalization.',
    'First arXiv circulation 2016-08-02; v3 2020-05-05; journal publication 2020.',
    journal='Algebra & Number Theory',volume='14',pages='2295--2333',doi='10.2140/ant.2020.14.2295')
ref('ConradLevel','misc','Math 248B: Isogenies and level structures','Brian Conrad','2011',
    'https://math.stanford.edu/~conrad/248BPage/handouts/level.pdf',
    'Proposition 2.1; Definition 2.7; Remark 2.8; Propositions 3.1--3.2; Theorem 3.3; Remark 3.4',
    'Level N≥3 is rigid over Z[1/N]; level two retains ±1. Ordinary Legendre structure consists of an invariant differential and an ordered two-torsion basis satisfying a coordinate normalization. Proposition 3.2 constructs it canonically from the specified mixed level-two/four data, compatibly with base change. Remark 2.8 warns that an ordinary S3 action is unavailable. This is not an identification of equations 73 and 83c in the manuscript.',
    'Stanford Math 248B course, winter 2011, corroborated by the course notes cited in Dan Dore’s 2017 seminar notes. No separate publication date established.')
ref('GrothCartanI','article',"Techniques de construction en géométrie analytique. I. Description axiomatique de l'espace de Teichmüller et de ses variantes",'Alexander Grothendieck','1960--1961',
    'https://www.numdam.org/item/SHC_1960-1961__13_1_A4_0.pdf',
    'Exposés 7--8, §2, especially Definition 2.3 and Lemma 2.4',
    'Defines the level-structure framework behind Torelli and Jacobi terminology and discusses rigidifying actions. The general argument there assumes genus at least two. It is terminology and descent context, not a genus-one proof that can be imported without checking the hypothesis.',
    'Séminaire Henri Cartan, 1960--1961; the opened record gives that seminar year, not a separately established first circulation day.',
    journal='Séminaire Henri Cartan',volume='13',number='1',pages='1--33')
ref('GrothCartanX','article',"Techniques de construction en géométrie analytique. X. Construction de l'espace de Teichmüller",'Alexander Grothendieck','1961',
    'https://www.numdam.org/item/SHC_1960-1961__13_2_A4_0.pdf',
    'Exposé 17, introduction, printed 17-01',
    'The introduction explicitly sets genus one aside, describing its lattice-quotient families of complex tori as the elementary model. It provides an exact earlier connection for the analytic line of work, while leaving its construction to the reader.',
    'Lecture dated 1961-05-08; Séminaire Henri Cartan 13 (1960--1961), exposé 17.',
    journal='Séminaire Henri Cartan',volume='13',number='2',pages='1--20')
ref('SGA1','book','Revêtements étales et groupe fondamental (SGA 1)','Alexander Grothendieck','1971',
    'https://arxiv.org/pdf/math/0206203',
    'VIII, Theorem 1.1, Remark 1.12 and §2 opening (recomposition pp.153--158; original pp.195--202); XII, Theorem 5.1 (recomposition p.251; original p.333)',
    'Faithfully flat quasi-compact descent is effective for quasi-coherent modules, including locally free modules of fixed rank, and respects tensor operations. This supports the root-line and tensor-twist background. The Riemann existence theorem compares finite étale algebraic and analytic covers of a locally finite-type complex scheme. That theorem alone supplies no arithmetic Galois image.',
    'Seminar 1960--1961; Springer Lecture Notes in Mathematics 224, 1971; SMF recomposition 2003; opened arXiv v2 dated 2004-01-04.',
    publisher='Springer',series='Lecture Notes in Mathematics',volume='224')
ref('Hain2008','incollection','Lectures on moduli spaces of elliptic curves','Richard Hain','2011',
    'https://arxiv.org/pdf/0812.1803',
    '§§2.3--2.4; Proposition 3.15; Proposition 5.16; Proposition 8.2, Corollary 8.3 and Remark 8.4',
    'The framed universal family and the tangent/Hodge-line comparison match the analytic objects used here. The differential-frame complement has braid-group fundamental group. Proposition 3.15’s literal strict C2×S3 quotient fails the harmonic stabilizer test; see the independent counterexample R-SA16-L64-Hain315. This bounded defect does not invalidate the other stated comparisons.',
    'Lectures July 2008; first arXiv submission 2008-12-09; publication in ALM 16 (2011), pp.95--166, confirmed by the author’s bibliography; opened arXiv v3 2014-03-25, text header 2014-03-26.',
    booktitle='Transformation Groups and Moduli Spaces of Curves',series='Advanced Lectures in Mathematics',volume='16',pages='95--166')
ref('Hain2021','misc','Lectures on moduli spaces of elliptic curves: author revision','Richard Hain','2021',
    'https://sites.math.duke.edu/~hain/teaching/mth790/hain_final_rev_2021.pdf',
    'Proposition 3.15; §8, especially pp.66--68',
    'The same strict quotient statement remains in this author revision. The braid-group comparison is also retained. The manuscript audit uses its own stabilizer computation rather than assuming that a later file silently repairs the quotient.',
    'Author file dated 2021-11-13; this is a revision date, not a new journal-publication date.')
ref('MilneEC2021','book','Elliptic Curves','James S. Milne','2021',
    'https://www.jmilne.org/math/Books/EC2.pdf',
    'I, Theorem 4.13; II, §1; III, Proposition 2.6 and Theorems 3.10, 3.12, 3.16',
    'Riemann–Roch, cubic models, chord-and-tangent addition, the Weierstrass differential equation, complex uniformization and prime-to-characteristic torsion provide the standard comparisons. Each manuscript coefficient and sign was recomputed independently. This source does not determine the unstated principal-part convention ε_n.',
    'Lecture-note antecedent 1996; first book edition 2006; second-edition web release announced 2020, opened PDF copyright 2021. These are edition dates, not discovery dates.',
    edition='2')
ref('BuxErshovRapinchuk2011','article','The congruence subgroup property for Aut F_2: a group-theoretic proof of Asada’s theorem',
    'Kai-Uwe Bux and Mikhail Ershov and Andrei S. Rapinchuk','2011',
    'https://arxiv.org/pdf/0909.0304',
    '§1, Main Theorem; §3, the recall of Out(F2)=GL2(Z)',
    'Recalls the discrete outer-automorphism theorem, pointing back to Magnus–Karrass–Solitar §3.5. Its Main Theorem concerns the action on the full profinite free group. It must be separated from the noninjective classical homological congruence-completion map.',
    'First arXiv circulation 2009-09-02; v2 2011-04-21; journal publication 2011.',
    journal='Groups, Geometry, and Dynamics',volume='5',pages='327--353',doi='10.4171/GGD/130')
ref('Nielsen1917','article','Die Isomorphismen der allgemeinen, unendlichen Gruppe mit zwei Erzeugenden','Jakob Nielsen','1917',
    'https://ths.math.ku.dk/nielsen_j/biblio.htm',
    'Bibliography item 2; collected-papers bibliography context only',
    'Bibliographic metadata was checked against the Copenhagen author bibliography and a Zenodo record. The original article text could not be opened. No theorem or proof is credited on the strength of this metadata; the modern discrete statement was read in Bux–Ershov–Rapinchuk §3.',
    'Publication 1917; a separate first circulation date was not established.',
    journal='Mathematische Annalen',volume='78',pages='385--397',note='unverified')
ref('MagnusKarrassSolitar1966','book','Combinatorial Group Theory','Wilhelm Magnus and Abraham Karrass and Donald Solitar','1966',
    'https://arxiv.org/pdf/0909.0304',
    '§3.5, cited backward from Bux–Ershov–Rapinchuk §3',
    'Backward bibliographic lead only; this book’s own text was not opened. The exact modern statement used in this run was opened in the later primary paper.',
    'Publication 1966 as recorded by the opened bibliography; circulation not established.',
    publisher='Interscience',note='unverified')
ref('Katz1970','article','Nilpotent connections and the monodromy theorem: applications of a result of Turrittin','Nicholas M. Katz','1970',
    'https://web.math.princeton.edu/~nmk/old/nilpconn.pdf',
    'Theorem 5.1, pp.190--191; Theorem 5.10, pp.196--198',
    'Zero p-curvature is the Cartier-descent condition. Gauss–Manin p-curvature is nilpotent with the stated cohomological bound; for H1 the exponent is at most two. This supports the separation of the earlier runs’ connection terminology. The explicit Legendre matrices here are independently recomputed examples.',
    'Received 1970-06-25; published in IHES volume 39 (1970). No earlier circulation date established.',
    journal='Publications Mathématiques de l’IHÉS',volume='39',pages='175--232',doi='10.1007/BF02684688')
ref('Voight2016','article','Discriminants and the monoid of quadratic rings','John Voight','2016',
    'https://msp.org/pjm/2016/283-2/pjm-v283-n2-p.pdf',
    'Lemma 3.7 and Lemma 3.10, p.500; Proposition 3.13, p.501',
    'A quadratic algebra with presentation x²−tx+n has discriminant t²−4n; invertible discriminant characterizes separability. Relative discriminants satisfy a square congruence modulo four. These are the exact local algebra ingredients used for the signed-radicand test; the specialized global Z[T] criterion is proved separately in this run.',
    'arXiv 1504.05228 first circulated April 2015; v3 dated 2016-01-13. Pacific Journal of Mathematics publication August 2016. The precise first submission day was not verified.',
    journal='Pacific Journal of Mathematics',volume='283',number='2',pages='483--510',doi='10.2140/pjm.2016.283.483')
ref('VoightErrata2021','misc','Errata: Discriminants and the monoid of quadratic rings','John Voight','2021',
    'https://jvoight.github.io/articles/monoid-errata.pdf',
    'One-page errata, Definition 3.1 and Theorem 3.28',
    'The two listed errata concern a definition typo and a Picard sheaf distinction. Neither changes the local discriminant statements used here.',
    'Dated 2021-01-17. The author’s revised article of the same date was also opened.')
ref('EGAIV2','article','Éléments de géométrie algébrique IV: Étude locale des schémas et des morphismes de schémas, deuxième partie',
    'Alexander Grothendieck and Jean Dieudonné','1965',
    'https://www.numdam.org/item/PMIHES_1965__24__5_0.pdf',
    'Theorem 5.8.6, printed p.108; definitions on p.107',
    'For a locally noetherian scheme, normality is equivalent to R1 and S2. The complete theorem and proof were read in the downloaded primary PDF. Applied to the quadratic hypersurface, this removes the proposed finite set of residual nonnormal points once height-one normality holds.',
    'Volume publication 1965; the opened Numdam record reports receipt in December 1963. No independent first-circulation date established.',
    journal='Publications Mathématiques de l’IHÉS',volume='24',pages='5--231',doi='10.1007/BF02684322',
    sha256='c3e960aa1c5c37046e8892d8a3cac098e2738164136b5cdaa5d5d893f89931da')
ref('Serre1970','article','p-torsion des courbes elliptiques (d’après Y. Manin)','Jean-Pierre Serre','1971',
    'https://numdam.org/item/SB_1969-1970__12__281_0.pdf',
    'Exposé 380, §1.1, printed p.281',
    'The initial elliptic-curve model, j invariant and exceptional automorphism groups give a pre-manuscript source for the standard stabilizer comparison. This is the Bourbaki exposé on p-torsion, not Serre’s differently titled later paper on Galois properties.',
    'Lecture May--June 1970; published in the 1971 Bourbaki volume, pp.281--294.',
    journal='Séminaire Bourbaki',number='380',pages='281--294')
ref('GroupNamesDic3','misc','Dic3: the dicyclic group of order 12','{GroupNames}','2026',
    'https://people.maths.bris.ac.uk/~matyd/GroupNames/1/Dic3.html',
    'Presentation, aliases, derived and central series',
    'The presentation and invariants agree with the complete finite-group enumeration in this run. This database comparison is not evidence for historical priority, nor does it identify the manuscript’s surrounding incomplete diagram.',
    'Current page checked 2026-11-19; no first-publication date established.')
ref('Zavyalov2019','misc','Notes for the Big Monodromy Lemma from Venkatesh-Lawrence Paper','Bogdan Zavyalov','2019',
    'https://bogdanzavyalov.com/refs/notes/Big_Monodromy.pdf',
    '§3.1, Theorem 3.5 and Corollary 3.6, pp.5--7, including footnotes 5 and 7',
    'Relates ordinary Legendre structure to a subgroup Γ(2)′ with diagonal entries 1 modulo four, using Conrad’s level-four construction. Footnotes leave the inverse-functor check and monodromy signs explicit. This subgroup is not automatically the normal complement reported by an earlier La Longue Marche run.',
    'Introduction identifies a 2019 Stanford working-seminar talk as the occasion. No formal journal-publication date found.')
ref('Hua2026','misc','Énoncés des notes de travail de Grothendieck démontrés en Lean 4, et questions ouvertes','Michel Hua','2026',
    'https://hexagonmath.org/pdf/2611.00125v2',
    '§42, pp.193--195; comparison with §18 and §50 only as separately indicated',
    'The public modernization flags the symmetric pinning comparison as not Lean-verified. It is a credited later comparison, not a replacement for the manuscript or a certificate checked by this run.',
    'Public preprint version opened November 2026. Earlier-run references to context/hua_project/64.modern.tex concern a different, unavailable context file.')

stacks=[
 ('Stacks031W','031W','Lemma 10.158.2','For a perfect field of characteristic p, vanishing differential in a field extension is characterized by being a pth power. It gives the function-field input for the corrected filtered derivation kernel.'),
 ('Stacks00P7','00P7','Lemma 10.119.7','For a one-dimensional noetherian local domain, the equivalent DVR, regular-local and normal formulations justify the local normality arguments. They do not permit silently replacing a DVR by a higher-dimensional regular local ring.'),
 ('Stacks031O','031O','Lemma 10.157.4','The modern R1-and-S2 normality criterion was opened with its proof and matched to the quadratic hypersurface hypotheses.'),
 ('Stacks02JN','02JN','Lemma 10.104.2','Quotienting a Cohen–Macaulay local ring by a regular sequence gives the Cohen–Macaulay property required for S2 of the hypersurface.'),
 ('Stacks0BNH','0BNH','Lemma 10.97.1','Exactness of completion for finite modules over a noetherian ring supports the explicitly specified adic completion. The equivalence of two adic topologies is a separate hypothesis checked in this run.'),
 ('Stacks02GI','02GI','Definition 29.37.1','The monic-polynomial and invertible-derivative presentation gives the standard étale test used for the normalized quadratic chart.'),
 ('Stacks0AP2','0AP2','Lemma 15.45.4','The opened étale-local comparison over Dedekind domains supplies background for one-dimensional étale normality; the precise DVR cases are proved independently here.'),
 ('Stacks0BYA','0BYA','Section 53.9','The plane-curve discussion supplies the smooth plane-cubic genus calculation used in the inverse cubic construction.')]
for key,tag,loc,summary in stacks:
    ref(key,'misc','The Stacks Project, Tag '+tag,'{The Stacks Project Authors}','2026',
        'https://stacks.math.columbia.edu/tag/'+tag,loc,summary,
        'Version accessed 2026-11-19. No discovery or first-circulation date inferred from the current web version.')

fields=['author','title','journal','booktitle','series','volume','number','pages','edition','publisher','year','doi','url','note']
with (B/'references.bib').open('w') as f:
    for x in R:
        f.write('@'+x['type']+'{'+x['key']+',\n')
        for k in fields:
            if k in x: f.write('  '+k+' = {'+str(x[k])+'},\n')
        f.write('  urldate = {2026-11-19},\n')
        f.write('  annote = {'+x['locator']+'. '+x['history']+'},\n}\n\n')

intro='''# Literature comparison for late cote 64

All dates and source statuses below are as checked on 19 November 2026. “Verified” means that the indicated source and passage were opened; the check-event table distinguishes reading a result from checking its proof. Nielsen’s original paper and the Magnus–Karrass–Solitar book remain primary-text-unverified backward leads. They are not used as substitutes for the modern primary statement actually opened.

The six search groups are **PIN** (root torsors, symmetric Legendre pinning and level four), **GROUP** (squares, the order-twelve extension and the cancelled diagram), **ALG** (pole filtrations, derivations, cubics and division), **LINEAR** (the tautological sequence and cyclic coordinates), **AN** (complex structures, framed families, modular and outer actions), and **ARITH** (quadratic orders, normality and dyadic normalization). Every claim has at least one group and an exact search-log mapping. Search results are not counted as proof. Sources were opened and their precise scope compared with the claim; the independent proofs are in `proof_notes.md`.

Class E records standard mathematics predating these pages, often through a modern exact exposition, rather than asserting that this manuscript-specific coordinate formula was separately published under this notation. Where no exact external formulation was located, that limit is stated. In particular C-SA16-561 is independently proved from the classical quadratic-order calculation and the 1965 normality criterion; no claim of locating its first occurrence is made. Class C for six pinning claims records an uncompleted exact comparison, not evidence that representability of ordinary level structures is a modern open problem. Class F records a genuinely unidentified hypothesis, normalization or diagram.

The final searches included arXiv, Numdam, targeted zbMATH Open and MathOverflow queries, EGA, SGA, Grothendieck’s published bibliography, and backward author-bibliography references. Some targeted zbMATH and MathOverflow queries returned no exact matching theorem; this has no force as evidence of nonexistence. The exact queries and the batched results actually seen are in `search_log.tsv` and `search_requests.json`. External PDFs and raw retrieval excerpts are not redistributed in this deliverable.

'''
with (B/'literature_notes.md').open('w') as f:
    f.write(intro)
    for x in R:
        f.write('## '+x['key']+'\n\n')
        f.write('['+x['title']+']('+x['url']+'). **'+x['note']+'**. '+x['locator']+'.\n\n')
        f.write(x['summary']+'\n\n'+x['history']+'\n\n')
        if x.get('sha256'):f.write('Downloaded PDF SHA-256: `'+x['sha256']+'`. The entire source remains outside the deliverable.\n\n')

# Do not duplicate source prose in metadata outputs.
meta=[{k:v for k,v in x.items() if k!='summary'} for x in R]
(B/'source_metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')

claims=json.loads((B/'claims.json').read_text())
search_rows=[]; req=[]
batch_notes={
 0:'Batch located Conrad, Antieau–Meier and a later Zavyalov comparison; no exact symmetric-pinning result from the targeted zbMATH query. Primary passages opened; see literature_notes.md.',
 1:'Batch returned Milne, Stacks 031W, a related MathOverflow discussion and Numdam leads. It supplied no special normalization of epsilon_n. Primary passages opened; see literature_notes.md.',
 2:'Batch returned Hain and Cartan I/X; no exact zbMATH result or original Nielsen text from this batch. Backward author-bibliography search separately checked; modern primary statement opened.',
 3:'Batch returned EGA metadata, Voight-related results and only related MathOverflow discussions. No exact specialized Z[T] theorem located; relevant primary ingredients opened and the specialized assertion independently proved.',
 4:'Batch returned GroupNames, the Grothendieck published bibliography and SGA1 metadata. No exact zbMATH result located. Group computation and primary descent passage checked separately.'}

def all_text(x):
    if isinstance(x,dict):
        if x.get('type')=='text':yield x.get('text','')
        else:
            for y in x.values():yield from all_text(y)
    elif isinstance(x,list):
        for y in x:yield from all_text(y)

for n in range(5):
    p=B/'outputs'/f'search_closure_{n}.json'
    if not p.exists():p=CACHE/p.name
    d=json.loads(p.read_text());d=d.get('value',d)
    txt='\n'.join(all_text(d['result']))
    urls=sorted(set(re.findall(r'https?://[^\s<>"\\)\]]+',txt)))
    sourceids=sorted(set(re.findall(r'【(turn\w+)】',txt)))
    gr=d['group'].split(';')
    ids=[c['id'] for c in claims if set(c['search_groups'])&set(gr)]
    for k,q in enumerate(d['queries'],1):
        sid=f'L64-SEARCH-{n+1:02}-{k:02}'
        search_rows.append(dict(search_id=sid,date=DATE,claims=';'.join(ids),group=';'.join(gr),
            repository=';'.join(re.findall(r'site:([^ ]+)',q)) or ('Grothendieck published bibliography; SGA' if 'Grothendieck' in q else 'Web discovery'),
            query=q,engine=d['engine'],result=batch_notes[n],opened_refs=';'.join(sorted(set(r for c in claims if c['id'] in ids for r in c['refs']))),
            result_urls=';'.join(urls),scope='Batch-level result; individual hits are not falsely assigned to a particular query.'))
        req.append(dict(search_id=sid,query=q,engine=d['engine'],group=gr,batch=n+1,result_source_ids=sourceids,result_urls=urls))

for x in R:
    ids=[c['id'] for c in claims if x['key'] in c['refs']]
    search_rows.append(dict(search_id='L64-OPEN-'+x['key'],date=DATE,claims=';'.join(ids),group='primary-source retrieval',repository=x['url'].split('/')[2],
        query='OPEN '+x['url']+'; locator: '+x['locator'],engine='web open/find; EGA IV2 additionally direct PDF download',
        result=x['note']+'; '+('Primary text unavailable; metadata only.' if x['note']=='unverified' else 'Indicated source passage opened and compared. See literature_notes.md.'),
        opened_refs=x['key'],result_urls=x['url'],scope=x['locator']))

cols=['search_id','date','claims','group','repository','query','engine','result','opened_refs','result_urls','scope']
with (B/'search_log.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols,delimiter='\t');w.writeheader();w.writerows(search_rows)
with (B/'claim_search_coverage.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['claim_id','groups','exact_query_rows','opened_reference_rows','scope'])
    for c in claims:
        q=[x['search_id'] for x in search_rows if x['search_id'].startswith('L64-SEARCH') and c['id'] in x['claims'].split(';')]
        w.writerow([c['id'],';'.join(c['search_groups']),';'.join(q),';'.join('L64-OPEN-'+r for r in c['refs']),c['fate']])
        assert q,c['id']

# Preserve recoverable exploratory request metadata without redistributing excerpts.
expl=[]
webfiles={p.name:p for p in CACHE.glob('web*.json')}
webfiles.update({p.name:p for p in (B/'outputs').glob('web*.json')})
for p in [webfiles[n] for n in sorted(webfiles)]:
    d=json.loads(p.read_text());txt='\n'.join(all_text(d))
    commands=sorted(set(re.findall(r'Source: ([^\n]+)',txt)))
    urls=sorted(set(re.findall(r'https?://[^\s<>"\\)\]]+',txt)))
    expl.append(dict(raw_file=p.name,requests_visible_in_provider_output=commands,result_urls=urls,
                     sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
                     note='Raw provider output retained only in external cache; commands not present in it are not invented.'))
(B/'search_requests.json').write_text(json.dumps(dict(final_searches=req,exploratory_retrieval_metadata=expl),ensure_ascii=False,indent=2)+'\n')
for p in list((B/'outputs').glob('web*.json'))+list((B/'outputs').glob('search_closure_*.json')):
    shutil.move(str(p),str(CACHE/p.name))

with (B/'progress.log').open('a') as f:
    f.write(datetime.now(timezone.utc).isoformat()+'\tSTAGE2_SOURCES\tAll 66 claims mapped to exact searched groups; primary-source locators and verification scope serialized. Raw external excerpts moved outside deliverables.\n')
print('References:',len(R),'verified:',sum(r['note']=='verified' for r in R),'unverified primary text:',sum(r['note']=='unverified' for r in R))
print('Search log rows:',len(search_rows),'claim coverage:',len(claims))
print('Raw external retrievals moved to:',CACHE)
