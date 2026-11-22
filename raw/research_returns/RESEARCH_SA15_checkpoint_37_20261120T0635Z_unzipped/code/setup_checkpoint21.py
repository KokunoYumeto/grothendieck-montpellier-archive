"""Preserve audited candidate and prepare CP21 integrations; no mathematical rerun."""
from pathlib import Path
import datetime, json, hashlib, csv
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
candidate=w/'notes/nonordinary_ppav_coble_rank_strata_candidate.tex'
text=candidate.read_text()
assert hashlib.sha256(candidate.read_bytes()).hexdigest()=='4f9e033cb52e1bb421618edb21e560d913ecf661759004cc115824ad82d4cea1'
audits=['agents/monodromy/outputs/independent_root_Coble_rank_strata_audit.json','agents/reduction_descent/nonordinary_coble_rank_independent_audit.json']
for rel in audits: assert 'PASS' in (w/rel).read_text()
text=text.replace('% Root post-CP20 candidate. Independent full audit required before promotion.','% Root result promoted after two independent complete proof/source audits; original candidate preserved.')
text=text.replace('Candidate; complete proof written, independent audits pending.','Proved under the stated nonproduct, nonordinary, characteristic-two hypotheses.')
text=text.replace('over the algebraically closed field. In the same complete\n$3\\Theta$ embedding, the construction of', 'over the algebraically closed field. Translating the Weierstrass-point\nrepresentative of the principal theta divisor identifies its complete\n$3\\Theta$ embedding with the fixed complete embedding above; the induced\nlinear isomorphism transports the theta group and the tensor together.\nIn this identified embedding, the construction of')
(w/'sections/A_nonordinary_ppav_Coble_ranks.tex').write_text(text)
labels=['lem:root-nonordinary-Coble-identification-candidate','lem:root-nonordinary-Cartier-stability-candidate','cor:root-nonordinary-Lang-rank-four-excluded-candidate']
record={'actual_utc':now,'status':'PROMOTED','candidate':str(candidate.relative_to(w)),'candidate_sha256':hashlib.sha256(candidate.read_bytes()).hexdigest(),'canonical':'sections/A_nonordinary_ppav_Coble_ranks.tex','labels':labels,'independent_audits':audits,'post_audit_change':'Explicit translation of the Weierstrass theta representative, as requested by the first audit; no changed mathematical assertion.','no_mathematical_program':True}
(w/'outputs/root_Coble_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for lab in labels:writer.writerow([lab,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','targeted proof check','Promoted after two full independent proof/source passes, at18:10:50.580066UTC and18:14:02.595889UTC. Original candidate retained. Translation clarification included. Rank-six Lang compatibility remains open; no full group claimed.'])
p=w/'code/consolidate.py';s=p.read_text()
s=s.replace("'obstructions_crystals/A3_mixed_positive_index_pencil.tex',", "'obstructions_crystals/A3_mixed_positive_index_pencil.tex',\n                 'obstructions_crystals/A3_mixed_positive_index_cup_derivative.tex',\n                 'obstructions_crystals/A3_mixed_positive_index_trace_zero.tex',")
s=s.replace("'monodromy/mixed_all_even_groups.tex']:","'monodromy/mixed_all_even_groups.tex',\n                 'monodromy/nonordinary_ppav_uniform_Q_inertia.tex']:")
s=s.replace("   out.write('\\n\\\\input{sections/A_nonordinary_ppav_covectors}\\n')", "   out.write('\\n\\\\input{sections/A_nonordinary_ppav_Coble_ranks}\\n')\n   out.write('\\n\\\\input{sections/A_nonordinary_ppav_covectors}\\n')")
s=s.replace("'B_tame_minimal_wild_layer.tex']:","'B_tame_minimal_wild_layer.tex',\n                    'B_tame_cubic_wild_layer.tex',\n                    'B_tame_cubic_wild_exhaustion.tex']:")
s=s.replace('\\\\path{notes/ROOT_SEARCH_LOG_20.md}\nrecord','\\\\path{notes/ROOT_SEARCH_LOG_20.md}, and\n\\\\path{notes/ROOT_SEARCH_LOG_21.md}\nrecord')
p.write_text(s)
old=json.loads((w/'notes/late_source_census.json').read_text())
old=[r for r in old if r['key']!='RainsSam2017Followup']
for r in old:
    if r['key']=='RainsSam2019LateLead':
        r['locators_and_limits']+=' After CP20, Remarks5.5--5.8 and AppendixA.1 proof with LemmasA.3/A.5/A.6 were inspected as further leads. The 2018 follow-up is now actually opened and used under its final journal citation RainsSam2018Trivectors. No theorem from this 2019 paper is needed in the Coble proof. The earlier no-identification statement describes only the frozen CP20 state.'
(w/'notes/late_source_census.json').write_text(json.dumps(old,indent=2)+'\n')
for oldname,newname in [('prepare_checkpoint20.py','prepare_checkpoint21.py'),('verify_program_paths20.py','verify_program_paths21.py')]:
    s=(w/'code'/oldname).read_text().replace('20','21')
    if oldname.startswith('prepare'):
        start=s.index('required=[');end=s.index('\nfor rel in required:',start)
        s=s[:start]+"required=['agents/monodromy/nonordinary_ppav_uniform_Q_inertia.tex',\n          'sections/A_nonordinary_ppav_Coble_ranks.tex',\n          'agents/obstructions_crystals/A3_mixed_positive_index_cup_derivative.tex',\n          'agents/obstructions_crystals/A3_mixed_positive_index_trace_zero.tex',\n          'agents/reduction_descent/B_tame_cubic_wild_layer.tex',\n          'agents/reduction_descent/B_tame_cubic_wild_exhaustion.tex']"+s[end:]
    (w/'code'/newname).write_text(s)
print(json.dumps(record,indent=2))
