"""Promote the twice-audited proof and retain its provenance-only delta."""
from pathlib import Path
import hashlib,json,datetime,difflib,csv,re
w=Path(__file__).resolve().parents[1]
source=w/'notes/primitive_elliptic_double_cover_candidate.tex'
target=w/'notes/primitive_elliptic_double_cover.tex'
assert not target.exists()
old=source.read_text()
assert hashlib.sha256(source.read_bytes()).hexdigest()=='43b704d52a72fe1c4b7174746dfe34be30dd5f83dea521466e472d81b2829e17'
audits=['agents/monodromy/outputs/independent_primitive_elliptic_double_cover_audit.json','agents/obstructions_crystals/primitive_elliptic_double_cover_independent_audit.json','agents/obstructions_crystals/primitive_double_cover_certificate_independent_audit.json']
for p in audits:
    data=json.loads((w/p).read_text())
    assert 'PASS' in data.get('status',''),p
new=old.replace('% Root candidate, complete proof; independent written-proof audits pending.','% Complete proof: two independent written-proof audits and exact certificate audit passed.')
new=new.replace('\\status{Candidate; complete proof awaiting independent audits.}','\\status{Proved under the stated hypotheses; independently audited.}')
new=new.replace('\\status{Candidate scope; the general A.4 question remains open.}','\\status{Proved scope limitation; general A.4 remains open.}')
oldtail='''general A.4 gate. Its source and elementary numerical checks are
proved in the text; no finite experiment or new numerical
certificate is used.'''
newtail=r'''general A.4 gate.

The exact supplement
\path{code/verify_primitive_double_cover_counterexamples.py}
and its complete companion output
\path{code/verify_primitive_double_cover_counterexamples.output.json}
verify the homogeneous cubic and all its partials, the universal
intersection and Smith identities, every nonzero quotient vector
and every adjacent transposition for the six certified primes
including the separate type-\((1,3)\) control, and all
\(120^2=14400\) multiplication pairs of the faithful \(S_5\)
matrices. The author run passed on 20 November 2026 at
06:16:42 UTC in 0.404319353 seconds. The unchanged isolated
independent rerun passed at 06:17:43 UTC in 0.419799397 seconds,
with every mathematical output identical and author bytes
preserved. The complete written proof was independently audited
by both companion readers before promotion. These finite checks
supplement the geometric proof; ampleness, global generation,
the sheaf sequences and the identification of the actual
relative local system are established in the text. All audit
records, source readings and execution streams are retained.'''
assert old.count(oldtail)==1
new=new.replace(oldtail,newtail)
assert '\\status{Candidate' not in new
target.write_text(new)
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
diff=''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=str(source.relative_to(w)),tofile=str(target.relative_to(w))))
(w/'notes/primitive_double_cover_promotion.diff').write_text(diff)
labels=re.findall(r'\\label\{([^}]+)\}',new)
assert len(labels)==5
record={'status':'PROMOTED AFTER TWO COMPLETE WRITTEN AUDITS AND CERTIFICATE AUDIT','actual_utc':stamp,'candidate':str(source.relative_to(w)),'candidate_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'canonical':str(target.relative_to(w)),'canonical_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'labels':labels,'audits':audits,'delta':'Status and numerical-provenance paragraphs only; all mathematical statements and proofs unchanged.','scope':'Actual proper primitive image and disconnected nonzero Lang cover; no large-degree A.4 refutation or exact S_n claim.'}
(w/'notes/primitive_double_cover_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for label in labels:
        wr.writerow([label,stamp,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root and two independent companion readers','full independent proof and exact certificate audit','PASS: actual E:y^2+y=x^3, A=E^2 and L_m=mV+H+Gamma; complete construction and Galois-equivariant branch module. Complete written audits at06:10:57.649345 and06:15:28.815324; exact checker author0.4043193529942073s and unchanged independent0.41979939700104296s; all mathematical outputs identical. Canonical and exact status/provenance diff in notes/primitive_double_cover_promotion.json. No general A.4 closure.'])
print(json.dumps(record,indent=2))
