"""Promote the explicit bad-five-kernel counterexample after full independent audits."""
from pathlib import Path
import csv, datetime, hashlib, json
w=Path(__file__).resolve().parents[1]
candidate=w/'notes/root_f1_bad_five_kernel_candidate.tex'
expected='2d34f653d4911ad0a8c344a197bec30246326fd45249e86f503757c3364b7186'
assert hashlib.sha256(candidate.read_bytes()).hexdigest()==expected
audits=[
 'agents/monodromy/outputs/independent_root_f1_bad_five_kernel_audit.json',
 'agents/obstructions_crystals/root_bad_five_kernel_independent_audit.json']
for rel in audits:
    a=json.loads((w/rel).read_text())
    assert 'PASS' in a['status']
canonical=w/'agents/monodromy/nonordinary_rank_one_bad_five_kernel.tex'
assert not canonical.exists()
t=candidate.read_text()
t=t.replace('% Candidate retained after the CP25 paper freeze; independent audit requested.',
            '% Root proof promoted after two complete independent audits; exact candidate retained.')
t=t.replace('Candidate; explicit function proof and exact certificates supplied.',
            'Proved; the stronger every-kernel nodality claim is refuted.')
t=t.replace('Candidate scope statement; no existence theorem is refuted.',
            'Proved scope statement; no existence theorem is refuted.')
t=t.replace('The polarization descends through\neach such kernel to a principal polarization with multiplier five.',
            'Five times the source principal polarization descends through\neach such kernel to a principal polarization on the quotient.')
t=t.replace('The bounded search \\path{code/root_f1_five_packets.py}',
            'The norm-function method is consistent with\n\\citep[Proposition~1.1]{BoxallGrantLeprevost2001}; the full divisor\nverification is given above, without a novelty claim.\nThe bounded search \\path{code/root_f1_five_packets.py}')
canonical.write_text(t)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
labels=['prop:root-f1-bad-five-kernel','rem:root-f1-bad-five-kernel-scope']
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for lab in labels:
        wr.writerow([lab,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15',
                     'targeted proof check',
                     'PASS. Smooth genus-two f1 model, Cartier diagonal(1,0), exact norm (z+1)^5, '
                     'local zero5P and sole pole5Q prove nonzero order-five class. Its negative '
                     'and zero give a three-point theta fibre in all six maximal isotropic '
                     'planes through that line. Five times the source polarization descends. '
                     'Both independent complete proof audits and separate exact norm certificates '
                     'passed. The24-curve census is supplementary; no geometric absence or '
                     'good incoming-neighbour theorem follows. Stronger every-kernel shortcut '
                     'is refuted, with no main-gate closure counted.'])
record={'status':'PROVED COUNTEREXAMPLE','promotion_utc':now,'labels':labels,
        'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,
        'canonical':str(canonical.relative_to(w)),
        'canonical_sha256':hashlib.sha256(canonical.read_bytes()).hexdigest(),
        'independent_audits':audits,
        'canonical_precision_repair':'Explicitly five times the source principal polarization descends; mathematical meaning unchanged.',
        'source_read':'Boxall--Grant--Leprevost original printedpp30--31, Proposition1.1 and Example1.2, already recorded in ROOT_SEARCH_LOG_25.',
        'scope':'Refutes every-kernel nodality only; no universal existence question closed.'}
dest=w/'outputs/root_f1_bad_five_kernel_promotion.json'
assert not dest.exists();dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
