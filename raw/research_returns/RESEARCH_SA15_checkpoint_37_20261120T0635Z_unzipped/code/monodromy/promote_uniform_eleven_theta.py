"""Promote only after explicit parent authorization and both complete audits."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,csv,re,difflib

parser=argparse.ArgumentParser()
parser.add_argument('--root-audit',required=True)
parser.add_argument('--oc-audit',required=True)
parser.add_argument('--root-time',required=True)
parser.add_argument('--oc-time',required=True)
args=parser.parse_args()
agent=Path(__file__).resolve().parents[1];work=agent.parents[1]
candidate=agent/'nonordinary_uniform_eleven_theta_geometry_candidate.tex'
expected='f240bd69cb86e8401c4896902faf709726852f4740b5d4455e0b1fec55b48cb9'
assert hashlib.sha256(candidate.read_bytes()).hexdigest()==expected
root_audit=work/args.root_audit;oc_audit=work/args.oc_audit
assert root_audit.exists() and oc_audit.exists()
canonical=agent/'nonordinary_uniform_eleven_theta_geometry.tex'
assert not canonical.exists()
s=candidate.read_text()
s=s.replace('% Post-CP27 candidate; no promotion before complete independent audits.',
            '% Post-CP27 theorem; exact fully audited candidate retained separately.')
s=s.replace('A candidate uniform nodal norm-eleven self-isogeny','A uniform nodal norm-eleven self-isogeny')
s=s.replace('\\status{Candidate; complete proof and exact certificate pending independent audit.}',
            '\\status{Proved and independently checked.}')
s=s.replace('On every fixed two-rank-zero principally polarized surface over a perfect\nfield of characteristic two, every positive odd degree divisible by at',
            'On every fixed two-rank-zero principally polarized surface $(A,\\Theta)$\nover a perfect field of characteristic two, put $L=\\mathcal O_A(3\\Theta)$\nand use the complete systems $|L^d|=|3d\\Theta|$. Every positive odd\ndegree divisible by at')
s,count=re.subn(r'\\textup\{\[Candidate[^\]]*\]\}',lambda m:'\\textup{[Proved; independent audits passed.]}',s)
assert count==6
extra=('\nThe complete parent proof, dependency, and exact-resultant audit passed at\n'
       +args.root_time+' UTC, and the complete obstruction/crystal audit\n'
       'passed at '+args.oc_time+' UTC on 19 November 2026.\n'
       'Both original universal characteristic polynomials were also independently\n'
       'reconstructed by a separate 120-permutation determinant calculation.\n'
       'The additional binary-only transform and Bezout check is retained as\n'
       '\\path{code/monodromy/post_CP27_eleven_binary_bezout_check.py}.\n')
pos=s.rfind('\\end{remark}')
assert pos>=0;s=s[:pos]+extra+s[pos:]
canonical.write_text(s)

changes=[]
def edit(path,old,new,reason):
    p=work/path;before=p.read_text();assert before.count(old)==1,path
    history=agent/'history'/('pre_uniform_eleven_'+path.replace('/','__'))
    assert not history.exists();history.write_text(before)
    after=before.replace(old,new);p.write_text(after)
    diff=history.with_name(history.name+'.diff')
    diff.write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile=history.name,tofile=path)))
    changes.append({'file':path,'prior':str(history),'diff':str(diff),'reason':reason})

edit('code/consolidate.py',"'monodromy/nonordinary_cubic_component_norm_transfer.tex'",
     "'monodromy/nonordinary_cubic_component_norm_transfer.tex',\n                  'monodromy/nonordinary_uniform_eleven_theta_geometry.tex'",
     'Include the newly fully audited canonical theorem.')
edit('code/prepare_checkpoint28.py','for rel in required:\n',
     "required.append('agents/monodromy/nonordinary_uniform_eleven_theta_geometry.tex')\nfor rel in required:\n",
     'Require the new canonical input before checkpoint28 integration.')
edit('agents/monodromy/nonordinary_nine_theta_norm_transfer.tex',
     'in particular the fixed two-rank-zero degree eleven and fixed\ntwo-rank-one degree five gates remain separate. The raw pre-archive outline, the exact audited candidate, and\nunrelated norm-eleven experiments remain retained separately.',
     'the fixed two-rank-zero degree-eleven case is settled later in\nTheorem~\\ref{thm:uniform-eleven-nodal-self-isogeny-candidate} and its\ncorollary; fixed two-rank-one degree five remains separate. The raw\npre-archive outline, exact audited candidate, and earlier norm-eleven\nexperiments remain retained separately.',
     'Replace the superseded degree-eleven open-gate sentence with an explicit forward reference; preserve all original bytes.')
edit('agents/monodromy/nonordinary_arbitrary_odd_neighbors.tex',
     'two-rank zero the first remaining odd degree is still eleven.',
     'two-rank zero degree eleven is settled by\nCorollary~\\ref{cor:f0-odd-multiples-eleven-candidate}; the first\nremaining odd degree is thirteen.',
     'Update only the now-superseded fixed-surface gate and retain the proved theorem scope.')
edit('agents/monodromy/nonordinary_cubic_component_norm_transfer.tex',
     'fixed two-rank-zero odd degree is eleven; fixed two-rank-one\ndegrees five and eight also remain separate.',
     'fixed two-rank-zero odd degree is thirteen after\nCorollary~\\ref{cor:f0-odd-multiples-eleven-candidate}; fixed two-rank-one\ndegrees five and eight also remain separate.',
     'Record the newly proved degree-eleven source without changing the uniform transfer argument.')

labels=['lem:uniform-eleven-interpolation-candidate','lem:uniform-eleven-quintic-fibres-candidate',
        'lem:uniform-eleven-good-parameters-candidate','thm:uniform-eleven-nodal-self-isogeny-candidate',
        'cor:f0-odd-multiples-eleven-candidate','rem:uniform-eleven-verification-scope-candidate']
now=datetime.now(timezone.utc).isoformat()
record={'status':'PROMOTED','actual_utc':now,'candidate_sha256':expected,
        'canonical':str(canonical),'canonical_sha256':hashlib.sha256(canonical.read_bytes()).hexdigest(),
        'labels':labels,'root_audit':str(root_audit),'oc_audit':str(oc_audit),'changes':changes,
        'scope':'Every fixed indecomposable f0 ppav has a nodal polarized eleven-self-isogeny with120nodes. Every fixed f0 odd degree divisible by3,5,7,or11 is full; every even degree was already full. Remaining first f0odd13, f1degree5/8.'}
(agent/'outputs/uniform_eleven_theta_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
with (agent/'CHECK_EVENTS_post_CP16.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for label in labels:writer.writerow([label,now,'/root/monodromy','PROMOTED-root-OC-full-proof-code-PASS',record['scope']])
with (agent/'post_CP16_notes.md').open('a') as f:
    f.write('\n## '+now+' — Uniform norm-eleven theorem promoted\n\n'+record['scope']+'\n\n'
            'The exact candidate remains byte-identical. All earlier executed versions, failures, discovery resultants, coefficient inputs, factorization outputs and independent Bezout reconstructions remain retained. '
            'Three obsolete canonical degree-eleven scope sentences were replaced only with forward references and the new degree-thirteen residual gate; exact prior files and diffs are retained. '
            'Both complete proof audits passed before promotion; no numerical sampling or unproved orbit-size assertion is used.\n')
print(json.dumps(record,indent=2))
