"""Promote only the twice independently audited odd-theta reduction."""
from pathlib import Path
import csv, datetime, hashlib, json

w = Path(__file__).resolve().parents[1]
candidate = w / 'notes/root_odd_theta_nodality_reduction_candidate.tex'
expected = '6e33c20395bcfc1e1fff6598142af1b9c08511df6d2714f660b35f6a340b1693'
assert hashlib.sha256(candidate.read_bytes()).hexdigest() == expected
audit_paths = [
    'agents/monodromy/outputs/independent_root_odd_theta_nodality_audit.json',
    'agents/obstructions_crystals/root_odd_theta_nodality_independent_audit.json',
]
audits = [json.loads((w / rel).read_text()) for rel in audit_paths]
assert all('PASS' in a['status'] for a in audits)
assert all(a.get('sha256', a.get('candidate_sha256')) == expected for a in audits)
canonical = w / 'agents/monodromy/nonordinary_odd_theta_nodality_reduction.tex'
assert not canonical.exists()
text = candidate.read_text()
text = text.replace('% Root candidate. No existence of a suitable odd-degree neighbour is asserted.',
                    '% Root proof promoted after two complete independent audits; exact candidate retained.')
text = text.replace('Candidate; submitted for independent proof audit.',
                    'Proved; two complete independent proof audits passed.')
text = text.replace('Candidate scope statement; no new degree is classified here.',
                    'Proved scope statement; no new degree is classified here.')
text = text.replace('two-rank-one normal form; here',
                    'two-rank-one normal form in Lemma~\\ref{lem:p-rank-one-genus-two-polar-stable-candidate}; here')
canonical.write_text(text)
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
labels = ['lem:root-nonordinary-odd-theta-nodality',
          'rem:root-nonordinary-odd-theta-nodality-scope']
detail = (
    'PASS. Full root derivation and two independent full mathematical audits. '
    'Finite translate intersections prove generic injectivity; the etale restriction is '
    'unramified and is the normalization of its integral image. Equal invariant tangent '
    'lines give a distinct hyperelliptic pair, whose common quotient image is geometric '
    'two-torsion. An odd isogeny induces a bijection on geometric two-torsion, every '
    'such class for f<=1 has a Weierstrass representative, and that representative '
    'gives a distinct third point. Thus at-most-two fibres are precisely the nodal '
    'case. The divisor pullback and adjunction give |K|-1 nodes. The root reread the '
    'complete f1 normal-form derivation and the f0 normal-form/Cartier derivation. '
    'Incoming-neighbour existence is explicitly retained; no new degree is classified. '
    'This is a mathematical proof check, not a finite numerical certificate.'
)
with (w / 'notes/root_check_events.tsv').open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for label in labels:
        writer.writerow([label, now, 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15',
                         'targeted proof check', detail])
record = {'status': 'PROVED', 'promotion_utc': now,
          'candidate': str(candidate.relative_to(w)), 'candidate_sha256': expected,
          'canonical': str(canonical.relative_to(w)),
          'canonical_sha256': hashlib.sha256(canonical.read_bytes()).hexdigest(),
          'independent_audits': audit_paths, 'labels': labels,
          'scope': 'Nodality equivalence only; existence and new-degree monodromy remain separate.'}
dest = w / 'outputs/root_odd_theta_nodality_promotion.json'
assert not dest.exists()
dest.write_text(json.dumps(record, indent=2) + '\n')
with (w / 'notes/checkpoint25_changes.md').open('a') as f:
    f.write('\n### Audited odd-theta nodality reduction\n\n'
            'The short odd-kernel lemma was subsequently promoted after complete independent '
            'monodromy and obstruction/crystal proof audits at21:17:20.478565 and21:18:55.331241UTC. '
            'For a smooth genus-two curve of two-rank at mostone and any odd kernelK, '
            'the theta image is nodal exactly when every geometric fibre has at mosttwo points; '
            'then it has |K|-1 nodes. Equal tangent lines give a hyperelliptic pair, and its '
            'common two-torsion image has a Weierstrass representative, producing a third point. '
            'No incoming-neighbour existence or new unconditional monodromy degree follows. '
            'The exact candidate, initial wording repair, both audit records and canonical '
            'promotion record are retained.\n')
print(json.dumps(record, indent=2))
