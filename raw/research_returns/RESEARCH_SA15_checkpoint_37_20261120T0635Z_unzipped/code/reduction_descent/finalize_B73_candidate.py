from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

own = Path(__file__).resolve().parents[1]
source = own / 'B_rational_high_line_candidate.tex'
raw = source.read_bytes()
preserved = own / 'notes/B_rational_high_line.before_certificate.tex'
assert not preserved.exists()
preserved.write_bytes(raw)
old = '''classification is asserted. A finite exact supplement is being
prepared; it is not the source of the all-prime proof.'''
new = r'''classification is asserted.

The retained exact supplement is
\path{code/reduction_descent/verify_rational_high_line.py}.
Its author run passed in \(9.558507562003797\) seconds at
22:30:37 UTC on 19 November 2026. For \(p=5,7,11,13\), it
checks all \(360\) permitted sectors in the displayed range,
\(275{,}760\) rational first-level polygons, the
\(22{,}932\) degree-\(p\) and \(252{,}828\) degree-\(q\)
high inverse branches, and \(22{,}932\) actual second-high-quotient
root-count records. Exact rational arithmetic reconstructs the
Newton hulls and checks the displacement inequalities and all
remaining parameter branches. Another \(48\) records above
\(p^3\) test only the unbounded high-line recovery proposition;
they do not extend the exact-index theorem. This finite supplement
does not replace the all-prime proof or establish existence of
formal groups with any enumerated parameter.

A fresh targeted search using two engines was retained with its
actual queries and read scopes. It located Hattori's finite-flat
ramification-character work and Hoshi's tame-blind extension
bound. Only the explicitly logged introduction, theorem-statement
and short-corollary passages were newly read; no unexamined main
proof is claimed as audited, no new result is imported from a
snippet, and no priority conclusion is inferred. The proof here
uses the already audited Newton, actual-quotient, lower-break and
mixed-threshold dependencies indicated above.'''
text = raw.decode()
assert old in text
source.write_text(text.replace(old, new))

now = datetime.now(timezone.utc).isoformat()
queries = [
    {'engine':'system2', 'query':'"p-divisible" "height two" "inertia" "torsion"'},
    {'engine':'system2', 'query':'finite flat group schemes tame descent height two truncated ramification character bound'},
    {'engine':'system1', 'query':'"height two" "p^3" ramification torsion'},
    {'engine':'system1', 'query':'"p-divisible groups" tame character truncated inertia ramification'},
]
sources = [
    {
        'title':'Hattori, Tame characters and ramification of finite flat group schemes',
        'publication':'Journal of Number Theory 128(5), 1091-1108 (2008)',
        'doi':'10.1016/j.jnt.2007.05.006',
        'url':'https://eprints.lib.hokudai.ac.jp/repo/huscap/all/69652/re843.pdf',
        'search_refs':['turn160279701search0','turn160279701search24','turn747354256search0'],
        'opened_refs':['turn747354256view0','turn451190135view2'],
        'actually_read':'Introduction, Theorem 1.1, Corollary 1.2 and proof strategy, printed pp. 1-2 (PDF pp. 1-2 after the cover).',
        'main_proof_newly_read':False,
        'assessment':'Describes positive Abbes-Saito graded pieces and their tame characters. The opened passages do not give the exact finite-level comparison of finite special inertia types asserted here. No result imported.'
    },
    {
        'title':'Hattori, Hasse-Arf theorem for F_p-vector space schemes of rank two',
        'publication':'Author preprint dated May 1, 2007; author publication list identifies RIMS Bessatsu 4 (2007), 153-164.',
        'url':'https://www.comm.tcu.ac.jp/~shinh/HAFp/hasse-arfFp.pdf',
        'search_refs':['turn160279701search6'],
        'opened_refs':['turn928264162view0','turn238308553view0'],
        'actually_read':'Introduction pp. 1-2, including Conjecture 1.2 and reducible rank-two scope; visible opening of Section 2 and Lemma 2.2 proof on p. 4. The whole article and main proof were not newly read.',
        'main_proof_newly_read':False,
        'assessment':'Related rank-two finite-flat ramification, Breuil/Kummer base-change context. No theorem imported into B73.'
    },
    {
        'title':'Hoshi, Tame-blind Extension of Morphisms of Truncated Barsotti-Tate Group Schemes',
        'publication':'Journal of Mathematical Sciences, the University of Tokyo 16 (2009), 23-54.',
        'url':'https://www.ms.u-tokyo.ac.jp/journal/pdf/jms160102.pdf',
        'search_refs':['turn160279701search25'],
        'opened_refs':['turn451190135view0','turn928264162view1','turn928264162view2','turn238308553view1'],
        'actually_read':'Introduction printed pp. 23-28, including Theorem 0.1, Corollary 0.2, epsilon_Fon=2+v_p(e_K), and graph-proof outline; complete Corollary 3.5 statement and its one-line proof, pp. 50-51.',
        'main_proof_newly_read':False,
        'short_corollary_proof_newly_read':True,
        'assessment':'Integral isomorphism extension at truncation levels greater than 4(2+v_p(e)); broad contextual bound, not an identification of the exact B73 least character threshold. Full Theorem 3.4 proof was not newly reread in this targeted search.'
    }
]
search = {
    'status':'TARGETED_PRIMARY_LITERATURE_SEARCH_RECORDED',
    'recorded_utc':now,
    'search_window_utc':'2026-11-19 approximately 22:31-22:33 UTC; exact per-call timestamps were not separately recorded.',
    'queries':queries,
    'sources':sources,
    'author_homepage_opened':{
        'url':'https://www.comm.tcu.ac.jp/~shinh/',
        'refs':['turn747354256view1','turn451190135view1'],
        'scope':'Relevant publication-list entries, including rank-two and canonical-subgroup work; metadata only.'
    },
    'additional_results_not_used':[
        {'ref':'turn160279701search26','url':'https://www.comm.tcu.ac.jp/shinh/ramcorr/ramcorr2.pdf','scope':'Search snippet only; not newly opened or read.'},
        {'ref':'turn160279701search28','url':'https://www.math.purdue.edu/~tongliu/pub/reduction.pdf','scope':'Search snippet only; not newly opened or read.'},
        {'ref':'turn747354256search1','title':'Phillips, Local monodromy of one-dimensional p-divisible groups','scope':'Search abstract indicates equal-characteristic setting; not newly opened or used.'},
        {'ref':'turn747354256search2','title':'Kottwitz and Wake, Primitive elements for p-divisible groups','scope':'Search snippet only; not newly opened or used.'},
        {'ref':'turn747354256search7','title':'Stix notes','scope':'Search result only; not used.'},
        {'ref':'turn747354256search8','title':'Serre tame-inertia material','scope':'Search result only; not used.'}
    ],
    'conclusion':'No exact B73 threshold was identified in the specifically retrieved and opened material. This bounded search is not a completeness or priority claim. Existing fully audited dependencies, not newly read snippets, support the mathematical proof.'
}
(own/'outputs/B73_literature_search.json').write_text(json.dumps(search,indent=2)+'\n')
md = '# B73 targeted primary-literature search\n\nRecorded '+now+'\n\n'
md += 'The search was requested before promotion. The following is a bounded retrieval record, not a novelty or priority claim. No new theorem was imported from a snippet.\n\n## Actual queries\n\n'
for item in queries:
    md += '- '+item['engine']+': `'+item['query']+'`\n'
md += '\n## Opened primary sources and actual read scopes\n\n'
for item in sources:
    md += '### '+item['title']+'\n\n'+item['publication']+'\n\n'+item['url']+'\n\n'
    md += '**Actually read:** '+item['actually_read']+'\n\n'
    md += '**Assessment:** '+item['assessment']+'\n\n'
    md += 'Opened retrieval references: '+', '.join(item['opened_refs'])+'.\n\n'
md += '## Limitations and mathematical source chain\n\n'+search['conclusion']+'\n\n'
md += 'The full main proofs of the Hattori papers and of Hoshi Theorem 3.4 were not newly read during this search. Hoshi Corollary 3.5 and its complete short proof were read. The B73 proof uses the previously fully audited Hopkins-Gross Newton coefficient results, Tate/descent conventions, B60 exact lower-break lemma, B69/B71 actual quotient constructions, B63 mixed threshold and lower examples, and B61 minimal-ramification result. Their precise internal citations are retained in the candidate.\n'
(own/'notes/POST_CP26_B73_LITERATURE_SEARCH.md').write_text(md)

(own/'notes/B73_superseded_weaker_outline.md').write_text('''# B73 superseded weaker outline

Before the final rational-high-branch proof, the contemplated extension used a nonscalar first high quotient to align its high line. In a straddling pair q*b1<e<q*b2, it then compared the second divisible parameter p^3*b1 with the prime parameter s-q*b2 using the strict first-level break inequality. This produced only a necessary arithmetic inequality and was insufficient as a uniform extension.

The saved complete proof instead proves actual first-level rationality from the intrinsic second stable line and recovers the high line from the degree-p or degree-q inverse point field, even for scalar residual representations. Its second quotient compares tame and genuinely wild first-level modules. The earlier outline was superseded as weaker, not refuted. No failed executed computation is associated with it.
''')

output_path=own/'code/verify_rational_high_line.output.json'
out=json.loads(output_path.read_text())
program=own/'code/verify_rational_high_line.py'
labels=re.findall(r'\\label\{([^}]+)\}',source.read_text())
assert len(labels)==6 and out['status']=='PASS'
record={
    'status':'CANDIDATE_COMPLETE_PROOF_AND_EXACT_SUPPLEMENT',
    'actual_utc':now,
    'candidate':source.name,
    'candidate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'pre_certificate_sha256':hashlib.sha256(raw).hexdigest(),
    'labels':labels,
    'claim':'Full B4 height-two exact index nu_min(p,e,2)=2 iff p<e<p^3, for p>=5, mu_p in K and p not dividing e; arbitrary perfect residue via the proved unramified-base reduction.',
    'program':str(program.relative_to(own)),
    'program_sha256':hashlib.sha256(program.read_bytes()).hexdigest(),
    'output':str(output_path.relative_to(own)),
    'output_sha256':hashlib.sha256(output_path.read_bytes()).hexdigest(),
    'author_runtime_seconds':out['elapsed_seconds'],
    'author_actual_utc':out['actual_utc'],
    'counts':out['counts'],
    'literature_search':'outputs/B73_literature_search.json',
    'independent_audits':'Requested; no promotion from this record.',
    'executed_failures':[],
    'superseded_weaker_outline':'notes/B73_superseded_weaker_outline.md'
}
(own/'outputs/B73_candidate_record.json').write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
    for label in labels:
        f.write('\t'.join([now,label,'CANDIDATE_COMPLETE_CHECKED',record['claim'],source.name+';outputs/B73_candidate_record.json','Author all-prime proof and exact finite checker PASS; primary search/read scopes retained; independent root and companion audits pending'])+'\n')
    f.write('\t'.join([now,'B73-LITERATURE','SEARCHED_READ_SCOPE_RECORDED','Targeted primary search; no priority claim','outputs/B73_literature_search.json;notes/POST_CP26_B73_LITERATURE_SEARCH.md','Both engines; exact query strings and limited actual read scopes; no theorem imported from a snippet'])+'\n')
print(json.dumps(record,indent=2))
