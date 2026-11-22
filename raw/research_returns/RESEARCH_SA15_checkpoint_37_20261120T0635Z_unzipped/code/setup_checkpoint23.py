"""Wire fully audited CP23 fragments into the reproducible paper build."""
from pathlib import Path
import datetime,json
w=Path(__file__).resolve().parents[1]
p=w/'code/consolidate.py';s=p.read_text()
needle="                 'obstructions_crystals/A3_mixed_positive_index_monad.tex',"
assert needle in s
for rel in ['obstructions_crystals/A3_mixed_positive_index_Petri.tex',
            'obstructions_crystals/A3_mixed_common_polarization_power.tex']:
    if repr(rel) not in s:s=s.replace(needle,needle+'\n                 '+repr(rel)+',')
needle="                 'monodromy/nonordinary_ppav_odd_natural_blocks.tex']:"
assert needle in s or "'monodromy/nonordinary_ppav_degree_three_node_gluing.tex'" in s
if "'monodromy/nonordinary_ppav_degree_three_node_gluing.tex'" not in s:
    s=s.replace(needle,"                 'monodromy/nonordinary_ppav_odd_natural_blocks.tex',\n                 'monodromy/nonordinary_three_theta_graph_reduction.tex',\n                 'monodromy/nonordinary_genus_two_triple_ramification.tex',\n                 'monodromy/nonordinary_ppav_degree_three_node_gluing.tex']:")
needle="   out.write('\\n\\\\input{sections/A_nonordinary_ppav_covectors}\\n')"
assert needle in s
if 'sections/A_nonordinary_trigonal_direct' not in s:
    s=s.replace(needle,"   for root_section in ['A_nonordinary_trigonal_direct', 'A_nonordinary_three_neighbor_boundary', 'A_nonordinary_degree_three_full']:\n    rp=s/(root_section+'.tex')\n    if rp.exists() and '\\\\status{Candidate' not in rp.read_text():\n     out.write('\\n\\\\input{sections/'+root_section+'}\\n')\n"+needle)
needle="                    'B_tame_reducible_recovery.tex']:"
assert needle in s or "'B_tame_cyclic_level_counterexamples.tex'" in s
if "'B_tame_cyclic_level_counterexamples.tex'" not in s:
    s=s.replace(needle,"                    'B_tame_reducible_recovery.tex',\n                    'B_tame_cyclic_level_counterexamples.tex']:")
if 'ROOT_SEARCH_LOG_23.md' not in s:
    s=s.replace('\\\\path{notes/ROOT_SEARCH_LOG_22.md}\nrecord',
                '\\\\path{notes/ROOT_SEARCH_LOG_22.md}, and\n\\\\path{notes/ROOT_SEARCH_LOG_23.md}\nrecord')
p.write_text(s)
required=[
 'agents/obstructions_crystals/A3_mixed_positive_index_Petri.tex',
 'agents/obstructions_crystals/A3_mixed_common_polarization_power.tex',
 'agents/monodromy/nonordinary_three_theta_graph_reduction.tex',
 'agents/monodromy/nonordinary_genus_two_triple_ramification.tex',
 'agents/monodromy/nonordinary_ppav_degree_three_node_gluing.tex',
 'agents/reduction_descent/B_tame_cyclic_level_counterexamples.tex',
 'sections/A_nonordinary_trigonal_direct.tex',
 'sections/A_nonordinary_three_neighbor_boundary.tex',
 'sections/A_nonordinary_degree_three_full.tex']
source=(w/'code/prepare_checkpoint22.py').read_text().replace('22','23')
start=source.index('required=[');end=source.index('\nfor rel in required:',start)
source=source[:start]+'required='+repr(required)+source[end:]
(w/'code/prepare_checkpoint23.py').write_text(source)
(w/'code/verify_program_paths23.py').write_text((w/'code/verify_program_paths22.py').read_text().replace('22','23'))
record={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'required_audited_fragments':required,'no_mathematical_program':True}
(w/'outputs/checkpoint23_setup.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
