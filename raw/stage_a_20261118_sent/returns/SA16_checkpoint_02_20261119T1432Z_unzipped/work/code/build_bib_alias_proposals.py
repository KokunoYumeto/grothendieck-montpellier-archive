"""Serialize manually adjudicated bibliography aliases and audit findings.

This parser only preserves source records. It does not infer identities, statuses,
verification results, or mathematical verdicts. Every grouping/finding below was
authored after reading the records and their cited scopes.
"""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path('/workspace/scratch/208fb206de03')
PARTS = ['cote62', 'cote63', 'cote64_early', 'cote64_late', 'cote62/supplement_katz']

def balanced(s, i):
    assert s[i] == '{'
    start, depth = i + 1, 1
    i += 1
    while i < len(s):
        if s[i] == '\\':
            i += 2
            continue
        if s[i] == '{': depth += 1
        if s[i] == '}':
            depth -= 1
            if depth == 0: return s[start:i], i + 1
        i += 1
    raise ValueError('Unclosed braced value')

def parse_bib(p):
    s = p.read_text()
    records = {}
    i = 0
    while True:
        m = re.search(r'@(\w+)\s*\{', s[i:])
        if not m: break
        typ = m.group(1)
        b = i + m.end() - 1
        body, i = balanced(s, b)
        key, body = body.split(',', 1)
        r = {'key': key.strip(), 'type': typ}
        j = 0
        while j < len(body):
            m2 = re.match(r'[\s,]*(\w+)\s*=\s*', body[j:])
            if not m2:
                assert not body[j:].strip(' \t\r\n,'), body[j:]
                break
            field = m2.group(1)
            j += m2.end()
            if body[j] == '{':
                value, j = balanced(body, j)
            elif body[j] == '"':
                k = j + 1
                while body[k] != '"' or body[k-1] == '\\': k += 1
                value, j = body[j+1:k], k+1
            else:
                k = body.find(',', j)
                if k < 0: k = len(body)
                value, j = body[j:k].strip(), k
            r[field] = value
        assert r['key'] not in records
        records[r['key']] = r
    return records

records = {}
inputs = []
for part in PARTS:
    p = ROOT/'work/parts'/part/'references.bib'
    parsed = parse_bib(p)
    reg = p.with_name('reference_registry.json')
    registry = {r['key']: r for r in json.loads(reg.read_text())} if reg.exists() else {}
    for key, bib in parsed.items():
        records[(part, key)] = {'part': part, 'key': key, 'bib_fields': bib,
                                'registry_fields': registry.get(key),
                                'bib_path': str(p.relative_to(ROOT)),
                                'registry_path': str(reg.relative_to(ROOT)) if reg.exists() else None}
    for x in [p] + ([reg] if reg.exists() else []):
        inputs.append({'path': str(x.relative_to(ROOT)),
                       'sha256': hashlib.sha256(x.read_bytes()).hexdigest()})
    assert len(parsed) == {'cote62':50,'cote63':40,'cote64_early':23,'cote64_late':27,'cote62/supplement_katz':7}[part]

def members(pairs):
    return [records[tuple(pair)] for pair in pairs]

groups = []
def alias(canonical, pairs, identity, normalize, guard):
    groups.append({'id': 'BIB-ALIAS-%02d' % (len(groups)+1), 'decision': 'same_work_merge_with_scopes_preserved',
                   'canonical_key': canonical, 'members': members(pairs),
                   'identity_evidence': identity, 'canonical_metadata_proposal': normalize,
                   'required_scope_preservation': guard, 'confidence': 'high'})

alias('Beauville2010', [['cote62','Beauville2010'],['cote64_early','Beauville2010']],
      'Same author, exact title, 2010 Contemporary Mathematics 522 pp23–29, arXiv0909.3942 and same author PDF (parentheses URL-encoded in one entry).',
      {'author':'Arnaud Beauville','title':'Finite subgroups of PGL(2,K)','year':'2010','eprint':'0909.3942','booktitle':'Vector Bundles and Complex Geometry','series':'Contemporary Mathematics','volume':'522','pages':'23--29'},
      'Keep the field/prime-to-characteristic hypotheses. Section4 centralizers do not supply the independently reconstructed arbitrary-base or characteristic3 assertions.')
alias('Hua2026', [['cote62','Hua2026'],['cote63','Hua2026'],['cote64_early','Hua2026'],['cote64_late','Hua2026']],
      'Same author, title (accent/spacing variants only), version2 URL https://hexagonmath.org/pdf/2611.00125v2, November2026.',
      {'author':'Michel Hua','title':'Énoncés des notes de travail de Grothendieck démontrés en Lean 4, et questions ouvertes','year':'2026','url':'https://hexagonmath.org/pdf/2611.00125v2','howpublished':'Author reconstruction and preprint, version 2'},
      'Preserve separate checked passages §18 pp89–90, §42 pp193–195, §50 pp239–240. No Lean certificate was rerun. Section50 excludes general-base descent from its field result. This accessible preprint cannot verify an unavailable earlier Hua context report.')
alias('SGA1', [['cote62','SGA1'],['cote64_early','SGA1'],['cote64_late','SGA1']],
      'Same work/title, Springer LNM224 (1971), same arXiv math/0206203 re-edition. Opened arXiv metadata confirms v2 2004-01-04 and identifies its relationship to the 1971 book.',
      {'title':'Revêtements étales et groupe fondamental (SGA 1)','year':'1971','series':'Lecture Notes in Mathematics','volume':'224','doi':'10.1007/BFb0058656','eprint':'math/0206203','edition_note':'1971 work; opened SMF recomposition/arXiv v2 (2004-01-04). Keep original and recomposed page locators separately.','author_role_note':'1971 book: Alexander Grothendieck et al.; arXiv metadata lists Alexander Grothendieck and Michele Raynaud; Michel Raynaud supplies updating remarks. Do not collapse the two Raynaud names/roles by inference.'},
      'Keep every part’s exact exposé/theorem and page convention. The opened text is a later recomposition; neither a complete proof audit of SGA1 nor all manuscript dictionaries follows from that access.')
alias('StacksKummer', [['cote62','StacksKummer'],['cote63','StacksKummer'],['cote64_early','Stacks03PK']],
      'Identical stable tag03PK and URL, same corporate author and Kummer-theory section.',
      {'author':'{The Stacks Project Authors}','title':'The Stacks Project, Kummer theory, Tag 03PK','url':'https://stacks.math.columbia.edu/tag/03PK'},
      'Preserve invertibility/topology hypotheses and distinctions among root groupoids, torsors, coarse classes and global sections. Access date is not a first-publication date.')
alias('StacksCompletion', [['cote62','StacksCompletion'],['cote64_late','Stacks0BNH']],
      'Identical stable tag0BNH and URL, same corporate author.',
      {'author':'{The Stacks Project Authors}','title':'The Stacks Project, Completion for Noetherian rings, Tag 0BNH','url':'https://stacks.math.columbia.edu/tag/0BNH'},
      'Keep cote62 Lemmas10.97.1–5 and late64 Lemma10.97.1 as separately checked scopes; do not imply late64 checked all five.')
alias('EGAIII2', [['cote62','EGAIII2'],['cote63','EGAIII']],
      'Same Grothendieck–Dieudonné EGAIII seconde partie, IHES17(1963)5–91; Numdam HTML/PDF URLs differ only by representation. DOI10.1007/BF02684890 belongs to this fascicle.',
      {'author':'Alexander Grothendieck and Jean Dieudonné','title':'Éléments de géométrie algébrique III: Étude cohomologique des faisceaux cohérents, seconde partie','year':'1963','journal':'Publications Mathématiques de l’IHÉS','volume':'17','pages':'5--91','doi':'10.1007/BF02684890'},
      'Preserve §7.7.5(II),7.7.10,7.8.4,7.8.6,7.9.9 and exact pages. Constant fibre dimensions in7.8.4 do not eliminate the reduced-base hypothesis. Distinct from EGAII and EGAIV2.')
alias('Katz1976', [['cote63','Katz1976'],['cote62/supplement_katz','Katz1976']],
      'Identical Nicholas M. Katz title, year, author PDF, Annals104(3)459–571; root supplies DOI10.2307/1970966.',
      {'author':'Nicholas M. Katz','title':'p-adic interpolation of real analytic Eisenstein series','year':'1976','journal':'Annals of Mathematics','volume':'104','number':'3','pages':'459--571','doi':'10.2307/1970966'},
      'Keep Lemma1.3.6 pp467–468, Lemma4.0.7 and Question4.0.8 p501. CM implies algebraicity in the opened lemma; the precise converse remains a question in this source. No deRham/Betti rationality substitution.')
alias('MOHodgeCM2010', [['cote63','MOHodgeCM2010'],['cote62/supplement_katz','MOHodgeCM2010']],
      'Identical MathOverflow question ID13681, title and2010 date. Original question author Andrea Mori; comments by other participants must keep their own attribution.',
      {'author':'Andrea Mori','title':'Cohomological characterization of CM curves','year':'2010','url':'https://mathoverflow.net/questions/13681/cohomological-characterization-of-cm-curves','date_note':'Question2010-02-01; discussion comments2010-02-02; no answer visible2026-11-19'},
      'This records an exact question and search/status lead, not a peer-reviewed proof or proof of present-day openness.')
alias('AntieauMeier2020', [['cote64_early','AntieauMeier2020'],['cote64_late','AntieauMeier2020']],
      'Exact same author pair, title and DOI10.2140/ant.2020.14.2295; same arXiv1608.00851.',
      {'author':'Benjamin Antieau and Lennart Meier','title':'The Brauer group of the moduli stack of elliptic curves','journal':'Algebra & Number Theory','year':'2020','volume':'14','number':'9','pages':'2295--2333','doi':'10.2140/ant.2020.14.2295','eprint':'1608.00851'},
      'Keep early64 root-torsor context and late64 Definition4.4/Proposition4.5/Lemma4.7. Neither scope establishes the special manuscript mu4 normalization without its additional argument.')
alias('ConradLevel', [['cote64_early','ConradLevel'],['cote64_late','ConradLevel']],
      'Same Brian Conrad handout at identical Stanford248B URL; title variant only adds course prefix.',
      {'author':'Brian Conrad','title':'Isogenies and level structures','howpublished':'Math 248B handout','url':'https://math.stanford.edu/~conrad/248BPage/handouts/level.pdf','publication_date':None,'date_note':'Handout undated. Winter2011 is course context corroborated indirectly in the late64 record; no independent publication date established.'},
      'Do not silently promote the course year into an exact publication/circulation date. Preserve Remark2.8’s natural-action limitation and late64’s broader exact proposition locators.')
alias('Katz1970', [['cote64_early','Katz1970'],['cote64_late','Katz1970']],
      'Exact same author,title,DOI10.1007/BF02684688,IHES39(1970)175–232 and author PDF.',
      {'author':'Nicholas M. Katz','title':'Nilpotent connections and the monodromy theorem: applications of a result of Turrittin','year':'1970','journal':'Publications Mathématiques de l’IHÉS','volume':'39','pages':'175--232','doi':'10.1007/BF02684688'},
      'Early64 uses background only; late64 reads Theorems5.1 and5.10. A union of bibliographic scopes must not retrospectively label early64’s finite-module pages as constructing a connection.')
alias('DLMF2315', [['cote62','DLMF2315'],['cote63','DLMF23Modular']],
      'Identical NIST DLMF section23.15 URL and corporate author; live page heading independently rechecked as Definitions.',
      {'author':'{NIST Digital Library of Mathematical Functions}','title':'NIST DLMF Section23.15: Definitions','url':'https://dlmf.nist.gov/23.15','urldate':'2026-11-19'},
      'Preserve lambda, normalizedJ and nome conventions. DLMF numerical/formula conventions do not prove an exact CM algebraicity converse.')

findings = []
def finding(key, field, before, proposed, evidence, status='proposed', severity='metadata_correction'):
    findings.append({'id':'BIB-AUDIT-%02d' % (len(findings)+1),'part':'cote63','key':key,
                     'field':field,'before_audit':before,'proposal':proposed,'evidence':evidence,
                     'status':status,'severity':severity,'current_snapshot':records[('cote63',key)]})

finding('SGA4','year/volume/title/doi','year1972 with volumes269,270,305 despite citing ExposésXII andXVI',
        'Cited tomeIII:1973,LNM305,DOI10.1007/BFb0070714; alternatively cite the complete set with1972–1973.',
        'Opened Springer tomeIII record, https://link.springer.com/book/10.1007/BFb0070714, copyright1973 and LNM305; table of contents includes the cited proper/smooth base-change chapters.',
        'corrected_by_parent_and_rechecked')
finding('SGA4','author/editor roles','Seminar directors listed as author of narrowed tomeIII',
        'For tomeIII use volume authors Pierre Deligne and Michael Artin, and retain Michael Artin/Alexander Grothendieck/Jean-Louis Verdier as seminar directors/editors with role explicit. Both cited ExposésXII/XVI are by Artin.',
        'Same opened Springer primary publisher record names P.Deligne,M.Artin as authors and attributes the two cited chapter titles to M.Artin.')
finding('Katz1976','locators','Sections1.2–1.3 pp465–468',
        'Sections1.2–1.3 pp464–468; exact Lemma1.3.6 pp467–468 remains unchanged.',
        'Previously opened author scan https://web.math.princeton.edu/~nmk/old/padicinterp.pdf, table of contents and printedpp464–468; supplement check events record exact lemma.',
        'corrected_by_parent_and_rechecked')
finding('DLMF23Modular','title','Chapter23: modular functions',
        'NIST DLMF Section23.15: Definitions; alias toDLMF2315.',
        'Opened exact live page https://dlmf.nist.gov/23.15, heading§23.15Definitions.',
        'corrected_by_parent_and_rechecked')
finding('DLMF27Partitions','title/locators','Chapter27: partitions; Equations27.14.2–5',
        'Section27.14:Unrestricted Partitions; include27.14.6 for the partition recurrence actually used.',
        'Opened https://dlmf.nist.gov/27.14; product27.14.2,generating series27.14.3,pentagonal expansion27.14.4–5,recurrence27.14.6.',
        'corrected_by_parent_and_rechecked')
finding('MOHodgeCM2010','author','MathOverflow contributors',
        'Andrea Mori as question author; separately attribute cited comments. Do not parse a parenthetical role as part of a personal name.',
        'Supplement directly opened question13681 and its dated discussion; preserved in supplement search log and primary URL.',
        'corrected_by_parent_and_rechecked')
finding('Katz1981SerreTate','booktitle','Algebraic Surfaces',
        'Prefer exact French title Surfaces algébriques: Séminaire de géométrie algébrique d’Orsay1976–78. Editors Jean Giraud,Luc Illusie,Michel Raynaud;1981,LNM868,chapterpp138–202.',
        'Opened publisher https://link.springer.com/book/10.1007/BFb0090642, exact book title/editors/copyright and chapter table of contents.',
        severity='title_normalization_not_mathematical_error')
finding('EGAIII','doi/key','DOI absent; broad keyEGAIII for seconde partie',
        'Alias keyEGAIII2; add DOI10.1007/BF02684890; retain1963,IHES17,pp5–91.',
        'Cote62 opened Numdam full original fascicle and its metadata; identical title/author/year/volume in both records. external_cache/cote62/EGAIII2.pdf; https://www.numdam.org/item/PMIHES_1963__17__5_0/.',
        severity='metadata_completion')
finding('SGA6','author/editor','Pierre Berthelot and Alexander Grothendieck and Luc Illusie, editors in author field',
        'Use editor field for the three names; remove literal comma-editors from the parsed last personal name.',
        'The root record itself explicitly identifies these names as editors; this is a BibTeX role/format correction.')
finding('SGA7II','author/editor','Pierre Deligne and Nicholas Katz, editors in author field',
        'Use editor field for Pierre Deligne and Nicholas M. Katz; remove literal comma-editors from the parsed last personal name.',
        'The root record explicitly identifies the names as editors; this is a BibTeX role/format correction.')
finding('Deligne1968','date_scope','1968 preprint; expanded/reproduced publication in1975',
        '1968 catalogued preprint; separately verified1975 publication of the same-titled work. Exact textual expansion/reproduction relationship was not checked because1968 pages were not retrieved.',
        'Root verification_scope says only the catalog record opened. The current expanded/reproduced wording exceeds that directly checked scope.',
        severity='scope_overstatement')
finding('ArtebaniDolgachev2009','verification_scope','Hesse formulas used for the characteristic-3 comparison',
        'Hesse formulas and level3 group context used for the mixed-characteristic2 comparison. Distinguish opened classical formulas from any integral universal-family identification reconstructed separately.',
        'Read root C-SA16-851,852,853,858 and associated problems: all explicit local tangent computations concern mixed characteristic2 and level3. No root cited claim here is a characteristic3 Hesse theorem.',
        severity='scope_mismatch')
finding('DLMF23Weierstrass','reference granularity','One keyURL23.2 cites sections23.2,23.3,23.6',
        'Retain as a composite with all threeURLs, or expand citations toDLMF232,DLMF233,DLMF236. Do not make a one-to-one alias toDLMF232.',
        'Root locators explicitly cover three distinct section pages; cote62 has individually opened references for each.',
        severity='composite_reference')

guards=[]
def guard(part,key,access,restriction):
    guards.append({'part':part,'key':key,'source_record':records[(part,key)],
                   'access_level_to_preserve':access,'must_not_promote_to':restriction})
guard('cote63','Deligne1968','Bibliographic catalog only;1968preprint pages not supplied','Original1968primary text opened or textual equivalence to1975 independently verified')
guard('cote63','Atkin1968','Metadata fromSerre bibliography; supplied author-archive transcription read; independent published fulltext not retrieved','Independent comparison with the published chapter or full published proof checked')
guard('cote63','Atkin1969','Published fulltext unverified; bibliography and supplied archival text read','Published chapter opened; keep note=unverified')
guard('cote63','Atkin1968Density','Publisher metadata and abstract','Full primary proof check or unsupported first-discovery priority')
guard('cote63','AtkinLehner1970','Publisher metadata and abstract; full proof inaccessible','Full primary proof read')
guard('cote63','GarvanShomanov2026','2026publication metadata fromauthor list;publisher403;proof accessed in2025preprint','2026publisher text opened or automatic identity of all version details')
guard('cote63','Stark1967','Original inaccessible;metadata/result viaStark2007','1967primary proof read;keep note=unverified')
guard('cote63','Stark1969','Original inaccessible;metadata/result viaStark2007','1969primary proof read;keep note=unverified')
guard('cote63','Deuring1941','Publisher metadata andSerre bibliography','Original full mathematical text read')
guard('cote63','FultonIntersection','Publisher metadata only;mathematical primary proof read inFulton1975','1998book proof read')
for key in ['SGA4','SGA6','SGA7II']:
    guard('cote63',key,'Exact statements accessed in the identified digital transcription; underlying original page image access is not established by these registry fields','Original scanned publication pages compared, or independent proof audit of the entire volume')
guard('cote63','ArtebaniDolgachev2009','Opened Hesse equations/group context','Integral moduli identifications in mixed characteristic2 established solely by those classical formulas')
guard('cote62','DelsarteInventoryUnverified','Institutional lead;PDF403;exact inventory entry unread','Exact draft identity/date verified;keep note=unverified')
guard('cote62','WW1927Metadata','DLMF bibliographic entry and historical backreferences;fullbook fetch failed','Historical textbook proof directly read')
guard('cote64_early','Ledet2001','Metadata only;primary inaccessible','Primary theorem hypotheses checked;keep note=unverified')
guard('cote64_early','Lattes1918','Secondary discussion inMilnor;originallargePDFnotread','1918primary text opened;keep note=unverified')
guard('cote64_late','Nielsen1917','Bibliographic lead only','1917primary text read;keep note=unverified')
guard('cote64_late','MagnusKarrassSolitar1966','Book not opened; citation viaBux–Ershov–Rapinchuk','1966book proof directly read;keep note=unverified')
guard('cote62/supplement_katz','BouillotUnverified','Search lead tothesischapter5;webtimeout/502andlocal503','Title/date/exact theorem or current-status resolution verified;keep note=unverified')
guard('cote62/supplement_katz','UQGeneratedAnswer2025','Page provenance verified; generated mathematical argument explicitly rejected','Positive mathematical authority forKatz converse; note=verified refers only to the stated provenance scope')

keep=[]
def separate(pairs,why):
    keep.append({'members':members(pairs),'decision':'keep_distinct_keys','reason':why})
separate([['cote63','Deligne1968'],['cote63','Deligne1975']], 'Different dated manifestations;1968catalogonly,1975textopened. No original1968textualcomparison.')
separate([['cote63','GarvanShomanov2025'],['cote63','GarvanShomanov2026']], 'Preprint and later publication have title/date/access differences. Preserve a related-version link; do not erase2026publisher403 or substitute metadata verification for proof access.')
separate([['cote64_late','Hain2008'],['cote64_late','Hain2021']], '2011publishedwork/2008lecture/arXivrevision and later2021authorrevision have distinct dates and page locators. Related versions, not an exact one-record alias.')
separate([['cote64_late','Voight2016'],['cote64_late','VoightErrata2021']], 'Article and errata are separate works; corrections must remain independently traceable.')
separate([['cote62','AOV2008'],['cote62','AOVCorr2014']], 'Original article and corrigendum are distinct works; a merge could hide corrected hypotheses.')
separate([['cote64_early','EGAII'],['cote62','EGAIII2'],['cote64_late','EGAIV2']], 'Different EGA fascicles with different titles,years,volumes andDOIs.')
separate([['cote63','SerrePadic1973'],['cote63','SerreBourbaki1973'],['cote64_late','Serre1970']], 'Distinct Serre works; shared modular-form subject and seminar/publication date differences do not identify them.')
separate([['cote62','GrothHilbert1961'],['cote64_late','GrothCartanI'],['cote64_late','GrothCartanX']], 'Distinct seminar texts/exposés; sharedauthorandperiod do not identify theworks.')

targeted_requests=[
 {'id':'BIB-AUDIT-WEB-001','request':{'open':['https://dlmf.nist.gov/23.15','https://dlmf.nist.gov/27.14','https://link.springer.com/book/10.1007/BFb0070714']},'outcome':'Read exact section titles; partition recurrence27.14.6;SGA4tomeIII1973LNM305 andvolume/chapterauthorroles.','raw_response':'external_cache/cote62/bib_audit/web_001.json'},
 {'id':'BIB-AUDIT-WEB-002','request':{'system2_search_query':[{'q':'Katz Serre Tate local moduli Surfaces algébriques 868 1981 138 202 Springer'}]},'outcome':'Located exact publisher book record. Search snippets themselves not used as mathematical proof.','raw_response':'external_cache/cote62/bib_audit/web_002.json'},
 {'id':'BIB-AUDIT-WEB-003','request':{'open':['https://link.springer.com/book/10.1007/BFb0090642','https://arxiv.org/abs/math/0206203']},'outcome':'Opened Katz1981volume title/editors/chapterpages andSGA1re-edition identity,authors,submissionhistory;no new theorem proof claimed.','raw_response':'external_cache/cote62/bib_audit/web_003.json'}]

out={
 'schema':'SA16-bibliography-alias-proposal-v1',
 'created_date':'2026-11-19',
 'reviewer':'GPT-6 Astra Pro; effort inherited/unspecified; run SA16-2026-11-19-cote62; independent bibliography review',
 'status':'proposal_only; parent performs final merge',
 'scope':'Read all147bibliography entries across4parts and Katz supplement, plus all97availableJSONregistry records. Targeted root metadata/scope audit uses already opened sources and three narrowly scoped metadata retrievals. No claim that every reference’s proof was reread for this audit.',
 'input_files':inputs,
 'input_counts':{'cote62':50,'cote63':40,'cote64_early':23,'cote64_late':27,'cote62/supplement_katz':7,'total_bib_records':147,'available_registry_records':97},
 'verification_policy':[
   'Keep bibliographic identity separate from edition/version identity and mathematical verification scope.',
   'A note=verified may mean exactly the recorded metadata or passage; never expand it to whole-text access or proof verification.',
   'Retain per-part source records and checked locators, including inaccessible-primary flags, alongside each canonical key.',
   'Do not replace an unverified source flag merely because a different source or edition establishes the underlying mathematics.',
   'Access dates on changing web resources are not first-circulation dates.',
   'All aliases and audit conclusions were manually authored; code only parses, validates references and serializes them.'
 ],
 'root_audit_findings':findings,
 'exact_alias_groups':groups,
 'composite_references':[{'source':records[('cote63','DLMF23Weierstrass')], 'decision':'retain_composite_or_expand_to_three_keys', 'candidate_expansion':['DLMF232','DLMF233','DLMF236'], 'targets':members([['cote62','DLMF232'],['cote62','DLMF233'],['cote62','DLMF236']]), 'reason':'One root key covers three separately titled section pages; not a single exact alias.'}],
 'keep_separate':keep,
 'verification_scope_guards':guards,
 'non_errors_to_preserve':[
   'Milnor2004 is a circulation-year key for a2006publication; do not change the record’s publication year to2004 merely to match the key.',
   'Hain2008 is a lecture-year key for a2011publication; preserve lecture,preprint,publication andrevision dates separately.',
   'Serre1970 is a seminar-year key for a1971publication; this is not a metadata inconsistency.',
   'Root Katz1976 explicitly distinguishes proved CM algebraicity from Question4.0.8; no overclaim was found in that scope statement.',
   'Root EGAIII correctly preserves the nonreduced-base caveat; the proposed alias does not alter its theorem scope.'
 ],
 'targeted_web_requests':targeted_requests,
 'authorized_part_edit_exception':'Parent specifically requested binary note normalization forUQGeneratedAnswer2025 during this audit. Only that note string was changed toverified in supplement references.bib,reference_registry.json,and builder; the explicit mathematical rejection remains in verification_scope. No other part files edited by this reviewer.',
 'check_events':[
   {'id':'BIB-REVIEW-01','type':'used and rechecked in this run','outcome':'Compared root40bibliographic records against source scopes and known primary metadata; flagged13precise corrections/composite/scope issues, some already corrected by parent.'},
   {'id':'BIB-REVIEW-02','type':'used and rechecked in this run','outcome':'Manually matched12exactsame-workgroups across147records and preserved every member’s original scope fields.'},
   {'id':'BIB-REVIEW-03','type':'used and rechecked in this run','outcome':'Read rootC851,C852,C853,C858 to identify characteristic2/level3 scope mismatch inArtebaniDolgachev2009 registry; this is a citation-scope review, not a new proof audit.'},
   {'id':'BIB-REVIEW-04','type':'used and rechecked in this run','outcome':'Recorded22access/scope guards and8related-but-distinct groups. No metadata-only record promoted to full primary verification.'}
 ]
}
assert len(groups)==12
assert len(findings)==13
assert len(guards)==22
assert len(keep)==8
seen=set()
for g in groups:
    for member in g['members']:
        pair=(member['part'],member['key'])
        assert pair not in seen,pair
        seen.add(pair)
for part in PARTS:
    for r in [x for x in records.values() if x['part']==part]:
        assert r['bib_fields'].get('note') in ['verified','unverified'],(part,r['key'],r['bib_fields'].get('note'))
dest=ROOT/'work/outputs/bib_alias_proposals.json'
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'output':str(dest.relative_to(ROOT)),'records':len(records),'alias_groups':len(groups),'alias_members':len(seen),'root_findings':len(findings),'scope_guards':len(guards),'keep_separate_groups':len(keep)},indent=2))
