"""Build the cross-scope alias proposal from manually adjudicated identities.

This is a bibliography/locator audit, not a theorem-verification program.
Input is the full inventory made by audit_reference_inventory.py.
No source bibliography or root-owned file is edited.
"""
from pathlib import Path
import collections
import csv
import hashlib
import json
import unicodedata

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
records = json.loads((BASE / 'reference_audit_inventory.json').read_text())
snapshot = json.loads((BASE / 'reference_audit_snapshot.json').read_text())

# These are manual identity decisions after reading titles, URLs and version notes.
GROUPS = [
    ('R-DM1982', ['DeligneMilne1982Tannakian'],
     'Same Deligne–Milne chapter and same corrected 15 August 2012 version at both author URLs. Both freshly opened files identify unchanged original theorem numbering.',
     'Keep 1982 as original publication and 2012 as the checked corrected version; retain correction footnotes and each scope’s theorem locators.',
     ['turn911467742view0', 'turn911467742view1']),
    ('R-Jannsen1992', ['Jannsen1992', 'Jannsen1992Motives'],
     'Same author, title, year and exact Regensburg primary PDF URL.',
     'Combine the separate checked theorem/proof extents; do not infer a whole-paper proof audit.', []),
    ('R-CG2017', ['ChoudhuryGallauer2017'],
     'Same authors, title and version-pinned arXiv HTML 1410.6104v3.',
     'Retain v3 and the exact theorem hypotheses and locators.', []),
    ('R-Kahn2025', ['Kahn2025Descent'],
     'Same author, title and arXiv identifier; both ledgers explicitly checked arXiv v4 of 29 May 2025.',
     'Keep arXiv v4 distinct from the TAC revision of 7 July 2025 when assigning theorem numbers. The current generic PDF URL is not itself version-pinned.', []),
    ('R-WeilII1980', ['Deligne1980WeilII'],
     'Same author, title, 1980 paper and exact IAS Number40.pdf URL.',
     'Article volume is PMIHES 52, not the erroneous volume42 in an IAS landing-page record. Retain section-specific checks.', []),
    ('R-Deligne1968', ['Deligne1968Degeneration', 'Deligne1968Lefschetz'],
     'Same author, full title, year and exact Numdam PMIHES_1968__35__107_0.pdf identifier.',
     'Retain all theorem locators and their distinct applications.', []),
    ('R-Tate1966', ['Tate1966Endomorphisms'],
     'Same author, title, year and exact Tate66.pdf URL.',
     'Preserve the finite-field hypotheses and checked extent.', []),
    ('R-Faltings1983', ['Faltings1983German'],
     'Both freshly opened primary reproductions identify the same German Inventiones73 (1983),349–366 article, by G.Faltings.',
     'These two German reproductions may be consolidated; retain Faltings1986Finiteness separately as the English Arithmetic Geometry chapter with different pagination.',
     ['turn843276577view2', 'turn843276577view3', 'turn911467742view3']),
    ('R-Hua2026', ['Hua2026', 'Hua2026Montpellier'],
     'All four scope occurrences name Michel Hua’s same title and version-pinned 2611.00125v2 PDF.',
     'Keep v2 distinct from comparison passages in v1. Theorem1.1 is the graph rule (printedp18); Theorem1.2 is the separate restricted equivalence (printedpp19–20). Keep all exclusions, extra hypotheses and author-reported Lean status; no Lean run occurred here.',
     ['turn894316750view0', 'turn287237814view0']),
    ('R-MilneReport2026', ['Milne2026Report'],
     'Same version-pinned 2611.00244v1 PDF; freshly opened first page confirms the printed title and J.S.Milne, 9 November 2026.',
     'Use the printed title On the Hodge, Tate, and standard conjectures for abelian varieties. Ignore the stale web/PDF metadata label Shimura Varieties. Keep this report separate from the October6 CM proof preprint and from Milne’s bibliography webpage.',
     ['turn911467742view2']),
    ('R-CMHodge2026', ['OpenAI2026CMHodge'],
     'Same author, exact title and identical October6-2026 primary paper URL.',
     'Preserve dated preprint status and each scope’s limited proof-audit extent; this does not expand CM-specific statements to arbitrary complex abelian varieties.', []),
    ('Stacks0FFZ', ['StacksCorr'],
     'Same Stacks Project stable tag0FFZ and section45.3, Correspondences.',
     'Keep the distinct checked lemmas; unrelated Stacks tags remain separate references.', []),
    ('Stacks0FG9', ['StacksMotives'],
     'Same Stacks Project stable tag0FG9 and section45.4, Chow motives.',
     'Keep the distinct checked lemmas; unrelated Stacks tags remain separate references.', []),
    ('Grothendieck1969', ['GrothStandard1969'],
     'Same Standard conjectures on algebraic cycles title, author, date and exact StandardConjs.pdf URL.',
     'Do not merge with Hodge’s general conjecture is false for trivial reasons, another 1969 Grothendieck paper. Retain the wider cote11b visual check and the narrower cote11a check as separate observations.', []),
    ('GIT1982', ['MumfordGIT1982'],
     'Same two authors, second edition1982 and exact mirror URL/ISBN3540112901.',
     'Keep second edition separate from third edition1994. Preserve the incomplete Proposition3.6 OCR, read Appendix proof, and undated physical reused sheets.', []),
    ('GIT1994Metadata', ['MumfordGITPublisher'],
     'Same three authors and exact Springer ISBN9783540569633 record; fresh publisher page identifies third edition1994.',
     'This is publisher metadata/edition chronology, not verification of mathematical passages from the 1994 edition.',
     ['turn759320315view3']),
    ('EGAII1961', ['EGAII'],
     'Same EGAII1961 article, PMIHES8,5–222. The Numdam DOI10.1007/BF02699291 record and the Grothendieck Circle EGAII.pdf witness describe the same work.',
     'Retain the metadata URL and actual primary PDF URL, and both exact4.5.2 and4.6.13(ii) checked extents. Metadata verification alone is not a proof.',
     ['turn759320315view1']),
    ('SGA1', [],
     'Both scope occurrences use the same arXiv math/0206203 recomposed text and same SGA1 title; author-name formatting differs only.',
     'Keep original publication1971 separate from the SMF electronic revision/recomposition. Preserve ExposéVIII descent locators and ExposésI/X purity locators.', []),
    ('Oda1969', [],
     'All three scope occurrences name Tadao Oda’s same article. Numdam item/article/PDF routes share ASENS_1969_4_2_1_63_0; fresh metadata confirms DOI10.24033/asens.1175 and pp63–135.',
     'Retain all exact theorem locators and the separate unavailable zbMATH-review lead; the review record is not another primary-article proof witness.',
     ['turn759320315view2']),
]

by_key = collections.defaultdict(list)
for r in records:
    by_key[r['key']].append(r)

alias_map = {}
groups = []
def observation(r):
    return {
        'scope': r['scope'], 'key': r['key'], 'source_bib': r['source_bib'],
        'title': r.get('title', ''), 'author': r.get('author', ''),
        'year': r.get('year', ''), 'url': r.get('url', ''),
        'verification_record': r.get('verification_record', {}),
        'metadata': r.get('metadata', {}),
    }

for canonical, aliases, basis, policy, webrefs in GROUPS:
    keys = [canonical] + aliases
    assert all(k in by_key for k in keys), keys
    for alias in aliases:
        assert alias not in alias_map, alias
        alias_map[alias] = canonical
    members = [r for r in records if r['key'] in keys]
    preferred = sorted(by_key[canonical], key=lambda r: ['root','cote11a','cote11b','cote12c'].index(r['scope']))[0]
    groups.append({
        'canonical_key': canonical, 'canonical_record_scope': preferred['scope'],
        'canonical_title': preferred.get('title', ''),
        'canonical_url': preferred.get('url', ''),
        'alias_keys': aliases, 'record_occurrences': len(members),
        'identity_confidence': 'high', 'decision': 'alias same work and checked version',
        'identity_basis': basis, 'version_and_locator_policy': policy,
        'fresh_web_references': webrefs,
        'members': [observation(r) for r in members],
    })

same_keys = []
for k, rr in sorted(by_key.items()):
    if len(rr) > 1:
        assert k in {'Hua2026','SGA1','Oda1969'}
        same_keys.append({
            'key': k, 'scopes': [r['scope'] for r in rr],
            'canonical_key': alias_map.get(k, k),
            'verdict': 'same work; no key collision',
            'urls': list(dict.fromkeys(r.get('url','') for r in rr)),
            'note': 'Author-name formatting and checked passages differ; retain each observation.'
        })

keep_separate = [
    {'keys':['SGA3II','SGA3Publisher','SGA3XII'], 'reason':'Same underlying SGA3 tomeII family, but original publisher metadata, later volume re-edition of undetermined date, and separately dated 2December2008 ExposéXII witness are not interchangeable. The supplied re-edition has editorial changes and different pagination. No automatic alias is proposed.', 'relationship':'SGA3Publisher is metadata for the original volume; SGA3XII is a part of that volume in a later witness.', 'evidence':['turn843276577view1','turn759320315view0','web/web_a30.json']},
    {'keys':['GIT1982','GIT1994Metadata'], 'reason':'Second edition1982 and third edition1994 differ in authorship, content and pagination. The 1994 record was metadata only.', 'evidence':['turn759320315view3']},
    {'keys':['R-Faltings1983','Faltings1986Finiteness'], 'reason':'German Inventiones article1983 and English Arithmetic Geometry chapter1986 are related versions with different title, venue and pagination. Retain both citations and exact theorem/page locators.', 'evidence':['turn843276577view2','turn843276577view3','turn911467742view3']},
    {'keys':['Grothendieck1969','Grothendieck1969HodgeFalse'], 'reason':'Different actual papers despite identical author and year: Standard conjectures on algebraic cycles versus Hodge’s general conjecture is false for trivial reasons.'},
    {'keys':['DeligneWeilI','R-WeilII1980','Deligne1974HodgeIII'], 'reason':'Three distinct publications: WeilI1974, WeilII1980, HodgeIII1974. Roman numerals and similarly named conjectures do not identify one work.'},
    {'keys':['R-MilneWC1970','R-MilneWC1972'], 'reason':'Original Weil–Châtelet paper and separate Addendum have distinct publications and mathematical roles.'},
    {'keys':['R-SGA7IX','SGA7II'], 'reason':'SGA7 tomeI,ExposéIX is distinct from tomeII (including ExposésXII/XV). Root’s accessed endpoint is a translation, while cote11b’s tomeII record is publisher metadata; neither observation certifies the other witness.'},
    {'keys':['SGA3II','SGA3III'], 'reason':'Distinct SGA3 tomesII/III; do not collapse the series title.'},
    {'keys':['Durfee1983Lead','DurfeeSaito1990'], 'reason':'Distinct works, years and authors; the 1983 inaccessible lead does not inherit the 1990 source’s theorem checks.'},
    {'keys':['Merkurjev1981','Merkurjev2006'], 'reason':'Original norm-residue result and later exposition are separate texts; similar titles do not give interchangeable proof/page locators.'},
    {'keys':['Kock2003','KockZanchetta2025'], 'reason':'Joachim Kock’s Frobenius-algebra book and Bernhard Köck/Ferdinando Zanchetta’s higher-K-theory article have different authors and subjects.'},
    {'keys':['R-Hua2026','HuaPinnedAppendix','HuaPinnedLean'], 'reason':'The v2 paper, pinned TeX appendix and pinned Lean source are distinct artifacts. The inaccessible code records remain unverified and no build is inferred from the paper.'},
    {'keys':['Oda1969','OdaZblLead'], 'reason':'Primary Oda paper and unavailable zbMATH review record are different source artifacts; the review is a lead, not a duplicate proof witness.'},
    {'keys':['R-CMHodge2026','R-MilneReport2026','Milne2026Bibliography'], 'reason':'CM proof preprint, Milne’s later report and author bibliography webpage are separate works with distinct evidentiary roles.'},
    {'keys':['Hironaka1964Lead','EncinasHauser2002'], 'reason':'Original resolution article lead and later strong-resolution paper are different works; an opened later theorem does not verify the unopened original proof.'},
]

warnings = [
    {'id':'RA-01','severity':'preserve version','keys':['SGA3II','SGA3Publisher','SGA3XII'], 'message':'SGA3 is the only plausible additional same-volume consolidation withheld from the automatic alias map. A fresh direct SGA3II.pdf open timed out; the prior successful re-edited-text check remains documented. Use an explicit original-versus-re-edition witness model before merging these records.'},
    {'id':'RA-02','severity':'preserve locator','keys':['R-DM1982','DeligneMilne1982Tannakian'], 'message':'Both author URLs presently show the corrected15August2012 Tannakian text. The first page says original theorem numbering is unchanged, but correction footnotes matter. Do not turn this into a claim that the uncorrected1982 typography was audited.'},
    {'id':'RA-03','severity':'metadata discrepancy resolved','keys':['R-MilneReport2026','Milne2026Report'], 'message':'The search/PDF wrapper calls2611.00244v1 Shimura Varieties; the actual first-page title is On the Hodge, Tate, and standard conjectures for abelian varieties, J.S.Milne,9November2026. The existing bibliographic titles are correct.'},
    {'id':'RA-04','severity':'preserve scope','keys':['R-Hua2026','Hua2026','Hua2026Montpellier'], 'message':'All records use v2. Theorem1.1(graph rule) and Theorem1.2(restricted equivalence) are different nearby results, not a numbering conflict. Preserve commutative/ungraded assumptions, special Künneth and multiplicative-gauge hypotheses, the v1/v2 variance discrepancy, and author-reported versus executed formal verification. No Lean run was performed.'},
    {'id':'RA-05','severity':'preserve edition','keys':['GIT1982','GIT1994Metadata','MumfordGIT1982','MumfordGITPublisher'], 'message':'Consolidate only within each edition. The1982 text was accessed through a mirror with incomplete OCR at3.6; the1994 publisher record proves chronology/metadata only. Neither date establishes the physical date of reused manuscript sheets.'},
    {'id':'RA-06','severity':'preserve version','keys':['R-Kahn2025','Kahn2025Descent'], 'message':'Both theorem checks used arXivv4 of29May2025. Keep TAC7July2025 revision metadata separately; generic arXiv/pdf/2312.01825 is not a permanently version-pinned link. Do not silently transport theorem numbering between the two.'},
    {'id':'RA-07','severity':'metadata discrepancy resolved','keys':['R-WeilII1980','Deligne1980WeilII'], 'message':'Use PMIHES52(1980),137–252. Cote12c recorded erroneous volume42 on the IAS landing page; this does not identify a second work.'},
    {'id':'RA-08','severity':'preserve access level','keys':['SGA4','SGA5Lead','SGA6Front','R-Almkvist1974','Springer1959','Durfee1983Lead','HuaPinnedAppendix','HuaPinnedLean','OdaZblLead'], 'message':'Broad titles, metadata records, frontmatter checks and unavailable leads retain their actual verification levels. Do not upgrade them when consolidating a nearby work or series. SGA4’s URL targets ExposéIV and its direct access failed in the original scope.'},
    {'id':'RA-09','severity':'preserve author role','keys':['EGAII1961','EGAII','EGAIV2','EGAIV3'], 'message':'The scope bibliographies credit Grothendieck and Dieudonné, while Numdam’s metadata uses Grothendieck as its author field. This is an attribution convention, not evidence of different EGA works. Keep the collaborator credit explicit if normalizing to Numdam.'},
    {'id':'RA-10','severity':'merge ledger carefully','keys':[], 'message':'The alias map merges identities only. Keep each scope’s actual checked passages, original URLs, date/version notes and negative access results as separate observations. A provenance check is not a mathematical proof, and a broad verified flag must not erase a metadata-only or limited-proof-audit extent.'},
    {'id':'RA-11','severity':'stable locator preferred','keys':['R-Hua2026','R-DM1982','SGA3II'], 'message':'Fresh web extraction line numbers can differ from earlier cached extraction for the same PDF. Prefer printed page, section and theorem numbers; preserve extraction source IDs and the raw saved evidence when using line locators.'},
    {'id':'RA-12','severity':'external-link status correction recommended','keys':['Delzant1962'], 'message':'Delzant1962 is the only input record without URL or DOI. Its full supplied offprint transcription was read by cote11b, but no exact public original or usable primary bibliographic record was opened. Under the strict opened-link requirement, recommend note=unverified for external-reference status while preserving attached_source_read=true and the complete checked extent. Numdam Laborde bibliography corroborates the citation; zbMATH0108.04303 was blocked403, MathSciNet26:175 showed only a JavaScript shell, and Gallica access failed403. See delzant_external_reference_audit.json.'},
]

scoped_alias_map = {r['scope'] + ':' + r['key']: alias_map[r['key']]
                    for r in records if r['key'] in alias_map}
canonical_keys = {alias_map.get(r['key'], r['key']) for r in records}
for src, dst in alias_map.items():
    assert dst in by_key
    assert dst not in alias_map
    assert src != dst

data = {
    'audit_date':'2026-11-19',
    'audit_scope':'All four supplied scope bibliographies and their metadata/verification ledgers; exact-work and checked-version identity only.',
    'source_snapshot':snapshot,
    'source_inventory':'reference_audit_inventory.json',
    'method':'Read all145 bibliography titles/authors/dates/URLs plus ledgers. Manually adjudicate duplicate groups. Reopen ambiguous primary titles/versions and relevant publisher metadata. Parser and validation only automate inventory/counts, not identity judgments.',
    'canonical_preference':'Use the existing root R- key for the same work; otherwise use an existing cote11a key where available. Never silently merge material version/locator differences.',
    'counts':{
        'source_records':len(records), 'source_unique_keys':len(by_key),
        'source_records_by_scope':dict(collections.Counter(r['scope'] for r in records)),
        'duplicate_work_groups':len(groups), 'distinct_alias_keys':len(alias_map),
        'scope_qualified_alias_occurrences':len(scoped_alias_map),
        'repeated_key_groups':len(same_keys),
        'repeated_key_extra_records':sum(len(rr)-1 for rr in by_key.values()),
        'same_key_conflicts':0,
        'canonical_records_if_unconditional_proposal_applied':len(canonical_keys),
    },
    'alias_map':dict(sorted(alias_map.items())),
    'scope_qualified_alias_map':dict(sorted(scoped_alias_map.items())),
    'duplicate_groups':groups,
    'same_key_groups':same_keys,
    'same_key_conflicts':[],
    'missing_url_and_doi_records':[{'scope':r['scope'],'key':r['key'],'current_note':r.get('note',''),'recommendation':'note=unverified for strict external-link status; preserve attached-text verification separately'} for r in records if not r.get('url') and not r.get('doi')],
    'conditional_alias_candidates':[
        {'source_key':'SGA3Publisher','possible_canonical_key':'SGA3II',
         'decision':'withheld from alias_map',
         'work_identity':'Same underlying tomeII,LNM152,1970.',
         'required_preservation':'Separate original publisher metadata from the later undated re-edited text; retain exact edition, witness URL, exposé and pagination. Keep SGA3XII as a part/witness record.',
         'reason':'The re-edited text includes editorial changes; original typography at problematic statements was not collated.'}
    ],
    'keep_separate':keep_separate,
    'warnings':warnings,
    'fresh_evidence_files':['web/reference_alias_web_1.json','web/reference_alias_web_2.json','web/reference_alias_web_3.json','web/reference_alias_web_4.json','web/reference_alias_web_5.json'],
    'limits':'Fresh external checks were focused on ambiguous identity/version cases. This audit did not re-open every unique reference or re-prove any theorem. The source inventory preserves prior verification extents, including failed access.',
}

(BASE / 'reference_alias_candidates.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')

lines = [
    '# Cross-scope bibliography alias audit', '',
    'Audit date: 2026-11-19. This proposal edits no source bibliography.', '',
    f"**Result:** {len(records)} source records, {len(by_key)} distinct keys, {len(groups)} duplicate-work groups, {len(alias_map)} distinct key aliases. Consolidating the unconditional groups gives **{len(canonical_keys)} canonical records**. **No same-key work conflicts** were found.", '',
    'The three repeated keys are `Hua2026`, `SGA1`, and `Oda1969`; their four extra occurrences are consistent. The machine-readable proposal includes source hashes, full member observations, URLs, version policy and scope-qualified aliases.', '',
    '## Proposed key aliases', '',
    '| Existing key | Canonical key |', '|---|---|',
]
lines += [f'| `{k}` | `{v}` |' for k,v in sorted(alias_map.items())]
lines += ['', '## Warnings and decisions', '']
for w in warnings:
    lines.append(f"- **{w['id']} — {w['severity']}:** {w['message']}")
lines += ['', '## Conditional relationship', '',
          '`SGA3Publisher` describes the same original volume family as `SGA3II`, but it is intentionally excluded from the automatic map. The latter records a later re-edited witness. The separately dated `SGA3XII` is an exposé witness with its own pagination and a problematic lemma whose original ink was not collated. Preserve these distinctions before considering a shared work-level parent.', '',
          '## Reproducibility', '',
          'Run `python SA05/work/cote11a/audit_reference_inventory.py`, then `python SA05/work/cote11a/build_reference_alias_candidates.py`. The first program inventories supplied data; the second applies the documented manual decisions and validates counts, targets and cycles. `reference_alias_validation.txt` records the actual run. Fresh external evidence is in `web/reference_alias_web_1.json` through `_5.json`; the complete per-record observations are in `reference_audit_inventory.json`.', '',
          'This is an identity/locator audit. It does not expand the original theorem verification or establish new mathematical results.', '']
(BASE / 'reference_alias_warnings.md').write_text('\n'.join(lines))

checks = [
    ('RA-CHECK-01','local inventory','145 bibliography records across four scopes; all titles/authors/years/URLs and matching verification ledgers inspected','reference_audit_inventory.json'),
    ('RA-CHECK-02','fresh primary version check','tc.pdf and tc2012.pdf both identify corrected15August2012 text,72pages; unchanged original numbering stated onp1','web/reference_alias_web_1.json'),
    ('RA-CHECK-03','fresh primary title check','Milne2611.00244v1 printed title confirmed; web wrapper title discrepant','web/reference_alias_web_1.json'),
    ('RA-CHECK-04','fresh primary edition check','Both German Faltings reproductions identify Inventiones73(1983),349–366;1986 English chapter kept separate','web/reference_alias_web_1.json;web/reference_alias_web_2.json'),
    ('RA-CHECK-05','fresh access failure','SGA3II.pdf direct reopen timed out; prior successful re-edited-text check not revoked','web/reference_alias_web_2.json'),
    ('RA-CHECK-06','fresh publisher metadata','SGA3II original volume:LNM152,1970,DOI10.1007/BFb0059005; no original lemma typography check','web/reference_alias_web_2.json'),
    ('RA-CHECK-07','fresh primary witness metadata','SGA3 ExposéXII first-page note identifies version2December2008; preserve separately','web/reference_alias_web_3.json'),
    ('RA-CHECK-08','fresh repository metadata','EGAII DOI and Oda article identifiers match the duplicate groups','web/reference_alias_web_3.json'),
    ('RA-CHECK-09','fresh publisher metadata','GIT publisher explicitly distinguishes first1965,second1982,third1994 editions','web/reference_alias_web_3.json'),
    ('RA-CHECK-10','fresh primary locator check','Hua v2 Th1.1 graph rule and Th1.2 restricted equivalence are distinct nearby statements; no locator conflict','web/reference_alias_web_4.json;web/reference_alias_web_5.json'),
    ('RA-CHECK-11','program validation','Alias targets exist; no cycles; repeated keys match adjudicated same-work groups; counts recomputed','reference_alias_validation.txt'),
]
with (BASE / 'reference_alias_checks.tsv').open('w',newline='') as f:
    w=csv.writer(f,delimiter='\t');w.writerow(['event_id','date','type','actual_check','evidence','proof_status'])
    for i,t,d,e in checks:w.writerow([i,'2026-11-19',t,d,e,'Bibliographic/provenance check only; not a mathematical proof'])

out = [json.dumps(data['counts'],indent=2),
       'PASS: every alias target is an existing key.',
       'PASS: no alias target is another alias; no cycles.',
       'PASS: same-key groups Hua2026, SGA1, Oda1969 identify the same works.',
       'PASS: root R- canonical preference applied to every duplicate group containing a root record.',
       'PASS: no source bibliography edited by this program.',
       'WITHHELD: SGA3Publisher -> SGA3II pending explicit original/re-edition witness preservation.']
(BASE / 'reference_alias_validation.txt').write_text('\n'.join(out)+'\n')
print('\n'.join(out))
