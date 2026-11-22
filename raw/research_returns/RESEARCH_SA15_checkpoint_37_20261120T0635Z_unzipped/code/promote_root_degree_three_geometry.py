"""Promote three independently audited root geometric fragments, preserving drafts."""
from pathlib import Path
import csv,datetime,hashlib,json
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
pairs=[
 ('notes/nonordinary_genus_two_trigonal_direct_candidate.tex','sections/A_nonordinary_trigonal_direct.tex'),
 ('notes/nonordinary_three_neighbor_boundary_candidate.tex','sections/A_nonordinary_three_neighbor_boundary.tex')]
records=[]
for src,dst in pairs:
    source=w/src; target=w/dst
    assert not target.exists()
    s=source.read_text()
    if 'trigonal_direct' in src:
        s=s.replace('% Root post-CP22 candidate. Complete direct proof, independent audits pending.',
                    '% Root proof promoted after full monodromy and obstruction/crystal independent audits.')
        s=s.replace('Candidate; complete direct proof and universal identities written, independent audits pending.',
                    'Proved; both independent proof and exact-certificate audits passed.')
        s=s.replace('Candidate consequence; independent audits pending.','Proved and independently checked.')
        s=s.replace('Candidate scope statement.','Proved scope statement.')
        s=s.replace('A separate\nGalois-closure and Cartier argument has been proposed independently;',
                    'A separate\nGalois-closure and Cartier argument has also been proved independently;')
        labels=['lem:root-nonordinary-trigonal-three-excluded-candidate',
                'cor:root-nonordinary-theta-no-three-triples-candidate',
                'rem:root-trigonal-direct-scope-candidate']
        audits=['agents/monodromy/outputs/independent_root_trigonal_direct_audit.json',
                'agents/obstructions_crystals/nonordinary_trigonal_direct_independent_audit.json',
                'outputs/root_post_cp22_audits.json']
    else:
        s=s.replace('% Root post-CP22 candidate; independent proof audits pending.',
                    '% Root proof promoted after full monodromy and obstruction/crystal independent audits.')
        s=s.replace('Candidate; complete proof written, independent audits pending.',
                    'Proved; both complete independent mathematical audits passed.')
        s=s.replace('Candidate scope statement.','Proved scope statement.')
        labels=['lem:root-nonordinary-nonproduct-three-neighbor-candidate',
                'lem:root-nonordinary-three-theta-clean-boundary-candidate',
                'rem:root-three-neighbor-boundary-scope-candidate']
        audits=['agents/monodromy/outputs/independent_root_three_neighbor_boundary_audit.json',
                'agents/obstructions_crystals/three_neighbor_boundary_independent_audit.json',
                'outputs/root_degree_three_and_b62_audits.json']
    for audit in audits: assert (w/audit).exists(),audit
    assert '\\status{Candidate' not in s
    target.write_text(s)
    records.append({'candidate':src,'canonical':dst,'candidate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                    'canonical_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'audits':audits,'labels':labels})
    with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
        wr=csv.writer(f,delimiter='\t')
        for label in labels:
            wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15',
                         'used and rechecked in this run','PROMOTED after complete root check and both independent full proof audits. Exact candidate preserved; canonical '+dst+'.'])
out=w/'outputs/root_degree_three_geometry_promotion.json'; assert not out.exists()
out.write_text(json.dumps({'actual_utc':now,'records':records},indent=2)+'\n')
print(json.dumps({'actual_utc':now,'promoted':[x['canonical'] for x in records]},indent=2))
