"""Record the complete short consequence check and promote its audited proof."""
from pathlib import Path
import csv,datetime,hashlib,json
w=Path(__file__).resolve().parents[1]
src=w/'notes/nonordinary_degree_three_unconditional_candidate.tex'
dst=w/'sections/A_nonordinary_degree_three_full.tex'
audit=w/'agents/obstructions_crystals/nonordinary_degree_three_consequence_independent_audit.json'
assert not dst.exists() and audit.exists()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
s=src.read_text().replace('Candidate consequence; complete proof written for independent checks.',
                          'Proved; complete consequence and independent dependency audits passed.')
assert '\\status{Candidate' not in s
dst.write_text(s)
label='thm:root-every-nonordinary-ppav-degree-three-full-candidate'
detail=('Full root consequence proof checked: over algebraic closure every principal surface is product or has a smooth genus-two theta. '
        'The already proved all-odd product theorems handle the two nonordinary product types. '
        'The root nonproduct-neighbour theorem and the fully audited multiplier3 node/gluing theorem handle every nonproduct target. '
        'The rank is80 on the complete |9Theta| smooth maximal-rank open. '
        'Arithmetic image contains the full geometric group, so no descent of the auxiliary neighbour is necessary. '
        'The ambient conclusion explicitly assumes restriction surjectivity and uses its geometrically integral coefficient fibres. '
        'OC full independent proof and dependencies audit PASS19:50:08.626649 UTC.')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','targeted proof check','PASS. '+detail])
record={'actual_utc':now,'status':'PROVED AND PROMOTED','label':label,
        'candidate_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
        'canonical':str(dst.relative_to(w)),'independent_audit':str(audit.relative_to(w)),
        'root_check':detail,'no_mathematical_program':True}
out=w/'outputs/root_degree_three_consequence_promotion.json';assert not out.exists()
out.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
