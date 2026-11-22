from pathlib import Path
import datetime,json,hashlib
r=Path(__file__).resolve().parent.parent
p=r/'nonordinary_five_theta_self_isogenies_candidate.tex'; s=p.read_text()
s=s.replace('\\status{Candidate; the finite census has an independent audit, while the complete geometric assembly awaits audit.}','\\status{Proved and independently checked.}')
for old in ['[Candidate; independent finite and function-theoretic checks passed.]','[Candidate; complete finite census independently rerun.]','[Candidate; exact kernel comparison passed.]']:
    s=s.replace(old,'[Proved; independent audits passed.]')
s=s.replace('\\path{code/nonordinary_five_theta_packet_probe.py}','\\path{code/monodromy/nonordinary_five_theta_packet_probe.py}').replace('\\path{code/nonordinary_five_theta_self_isogenies.py}','\\path{code/monodromy/nonordinary_five_theta_self_isogenies.py}')
s=s.replace('JSON outputs of the same stems in \\path{outputs/}.','JSON outputs of the same stems in \\path{agents/monodromy/outputs/}.')
s=s.replace('The full geometric proof above remains separately auditable.','The parent completed the full mathematical and source audit at 20:31:15 UTC and independently reran both complete programs, preserving the author outputs, in $0.334064817$ and $0.058760470$ seconds. The independent reduction/descent audit also checked the Weil functions and finite census; no broader geometric scope is attributed to that bounded audit.')
q=r/'nonordinary_five_theta_self_isogenies.tex';q.write_text(s)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['lem:five-theta-explicit-Weil-candidate','lem:five-theta-geometric-census-candidate','prop:five-theta-twenty-self-isogenies-candidate','rem:five-theta-self-isogeny-scope-candidate']
record={'status':'PROMOTED','actual_utc':now,'candidate':p.name,'candidate_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'canonical':q.name,'canonical_sha256':hashlib.sha256(q.read_bytes()).hexdigest(),'labels':labels,'root_audit':'../../outputs/root_five_theta_audit.json','scope':'Explicit fixed-source five-self-isogenies and nodal theta norms; no degree-five full monodromy or all-target theorem.'}
(r/'outputs/nonordinary_five_theta_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
with (r/'post_CP16_notes.md').open('a') as f:f.write('\n## '+now+' — Bounded fifth-torsion census promotion\n\nPromoted nonordinary_five_theta_self_isogenies.tex after full parent proof/source/code audit. Exact candidate retained. Four stable labels unchanged; only statuses, actual completed-check scope and exported code paths changed. This is a fixed-source geometric certificate, not a full-image theorem. Separate universal f0 nodality/four-value candidate remains unpromoted.\n')
with (r/'CHECK_EVENTS_post_CP16.tsv').open('a') as f:
    for label in labels:f.write('\t'.join([now,label,'promotion_after_parent_full_audit','PASS','Bounded fixed-source geometric theorem; two root output-preserving reruns; no full monodromy inference',q.name])+'\n')
bib=r/'references.bib'
if 'BoxallGrantLeprevost2001' not in bib.read_text():
    with bib.open('a') as f:f.write('''\n@article{BoxallGrantLeprevost2001,
 author={Boxall, John and Grant, David and Lepr{\\'e}vost, Franck},
 title={5-torsion points on curves of genus 2},
 journal={Journal of the London Mathematical Society},
 year={2001}, volume={64}, number={1}, pages={29--43},
 doi={10.1017/S0024610701002113},
 url={https://euclid.colorado.edu/~grant/publications/5torsion_points_on_curves_of_genus_2.pdf},
 note={Original author-hosted published PDF opened and Proposition1.1, Example1.2(ii), the following two-rank-zero paragraph, and Lemma2.1 with proof, printedpp30--32, read on19November2026. Parent independently reopened Example1.2(ii). Local originalPDF and extractedtext retained. The classification relative to a Weierstrass base point is not applied to arbitrary translated torsion packets.}
}
''')
print(json.dumps(record,indent=2))
