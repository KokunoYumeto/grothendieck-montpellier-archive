"""Prepare the already audited CP22 integrations. No mathematical calculation."""
from pathlib import Path
import datetime, json

w = Path(__file__).resolve().parents[1]
promoted = [
    'agents/monodromy/nonordinary_ppav_polar_Lang_conditional.tex',
    'agents/monodromy/p_rank_zero_ppav_degree_one_groups.tex',
    'agents/monodromy/p_rank_one_ppav_degree_one_groups.tex',
    'agents/reduction_descent/B_tame_full_wild_projective.tex',
    'agents/reduction_descent/B_tame_full_wild_quadratic.tex',
    'agents/obstructions_crystals/A3_mixed_positive_index_monad.tex',
]
for rel in promoted:
    assert (w / rel).exists(), rel
    assert '\\status{Candidate' not in (w / rel).read_text(), rel

p = w / 'code/consolidate.py'
s = p.read_text()
needle = "                 'obstructions_crystals/A3_mixed_positive_index_trace_zero.tex',"
assert needle in s
if "'obstructions_crystals/A3_mixed_positive_index_monad.tex'" not in s:
    s = s.replace(needle, needle + "\n                 'obstructions_crystals/A3_mixed_positive_index_monad.tex',")
needle = "   out.write('\\n\\\\input{sections/A_nonordinary_ppav_Coble_ranks}\\n')"
assert needle in s
if "'monodromy/nonordinary_ppav_polar_Lang_conditional.tex'" not in s:
    addition = """
   for extra in ['monodromy/nonordinary_ppav_polar_Lang_conditional.tex',
                 'monodromy/p_rank_zero_ppav_degree_one_groups.tex',
                 'monodromy/p_rank_one_ppav_degree_one_groups.tex']:
    path=a/extra
    if path.exists() and '\\\\status{Candidate' not in path.read_text():
     out.write('\\n'+path.read_text()+'\\n')"""
    s = s.replace(needle, needle + addition)
needle = "                    'B_tame_cubic_wild_exhaustion.tex']:"
assert needle in s
if "'B_tame_full_wild_projective.tex'" not in s:
    s = s.replace(needle, "                    'B_tame_cubic_wild_exhaustion.tex',\n                    'B_tame_full_wild_projective.tex',\n                    'B_tame_full_wild_quadratic.tex']:")
if 'ROOT_SEARCH_LOG_22.md' not in s:
    s = s.replace('\\\\path{notes/ROOT_SEARCH_LOG_21.md}\nrecord',
                  '\\\\path{notes/ROOT_SEARCH_LOG_21.md}, and\n\\\\path{notes/ROOT_SEARCH_LOG_22.md}\nrecord')
p.write_text(s)

p = w / 'notes/root_references.bib'
s = p.read_text()
old = 'Section 2 Cartan descriptions were inspected.'
new = ('Section 2.1 normal forms and Propositions 2.9--2.10 read; '
       'Proposition 3.8 with its proof and Section 5 through Lemma 5.3, '
       'Theorem 5.5 and Corollary 5.6 with their complete proofs read. '
       'Corollary 5.6 applies in characteristic different from three and is '
       'used in characteristic two. Lemma 2.8 is restricted to characteristic '
       'zero and is not used. The normal-form polar action minors are '
       'independent calculations retained with exact code and output.')
assert old in s or new in s
s = s.replace(old, new)
p.write_text(s)

p = w / 'notes/late_source_census.json'
oldrows = json.loads(p.read_text())
removed = [r['key'] for r in oldrows if r['key'] in {'ColmezLocalFieldsNotes', 'Serre1961LocalClosed'}]
p.write_text(json.dumps([r for r in oldrows if r['key'] not in removed], indent=2)+'\n')

for oldname, newname in [('prepare_checkpoint21.py','prepare_checkpoint22.py'),
                         ('verify_program_paths21.py','verify_program_paths22.py')]:
    s = (w/'code'/oldname).read_text().replace('21','22')
    if oldname.startswith('prepare'):
        start=s.index('required=['); end=s.index('\nfor rel in required:',start)
        s=s[:start]+'required='+repr(promoted)+s[end:]
    (w/'code'/newname).write_text(s)

record = {'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'promoted_files':promoted,
          'source_census_aliases_superseded':removed,
          'source_census_replacements':['ColmezCorpsLocaux','Serre1961LocalClosed'],
          'reason':'These actual source reads are now included in the bibliography; the historical CP21 entries remain in that checkpoint.',
          'no_mathematical_program':True}
(w/'outputs/checkpoint22_setup.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
