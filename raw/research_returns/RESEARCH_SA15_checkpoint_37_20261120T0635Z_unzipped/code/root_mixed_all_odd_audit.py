"""Retain an isolated graph rerun and the completed root all-odd proof audit."""
from pathlib import Path
import json,csv,datetime,hashlib,io,contextlib
w=Path(__file__).resolve().parents[1]
source=w/'agents/monodromy/code/mixed_odd_common_graph_checks.py'
author=w/'agents/monodromy/outputs/mixed_odd_common_graph_checks.json'
before=hashlib.sha256(author.read_bytes()).hexdigest()
text=source.read_text();needle="dest=Path(__file__).resolve().parents[1]/'outputs/mixed_odd_common_graph_checks.json'"
assert text.count(needle)==1
target=w/'outputs/root_mixed_odd_common_graph_checks.json';assert not target.exists()
executed=text.replace(needle,'dest=Path('+repr(str(target))+')')
snapshot=w/'code/audit_snapshots/mixed_odd_common_graph_checks_at_root_audit.py'
snapshot.parent.mkdir(exist_ok=True);assert not snapshot.exists();snapshot.write_text(executed)
stream=io.StringIO()
with contextlib.redirect_stdout(stream):
    exec(compile(executed,str(snapshot),'exec'),{'__file__':str(source),'__name__':'__main__'})
(w/'outputs/root_mixed_odd_common_graph_stdout.txt').write_text(stream.getvalue())
assert before==hashlib.sha256(author.read_bytes()).hexdigest()
run=json.loads(target.read_text());assert run['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checks={
'lem:mixed-odd-all-translated-small-source-candidate':'Complete proof independently rederived: every nonzero odd translation has a birational separable degree6 chord map; multiple pairs or triples require finite3Q conditions. A general projective transform meets all finitely many sextics transversely and avoids all triple lines. Four independent simultaneous branch conditions against three parameters give disjoint supports for every shift.',
'lem:mixed-odd-node-product-candidate':'Complete proof independently rederived: sharp source boundary exists in each fixed twist; two-node value incidences give double transitivity. All four/three/two-second-coordinate contact strata and every triple/singular exception have codimension>=2. The genuinely new one-overlap triple case has rank7 generically and at least6 against at most4parameters. Kunneth proves smooth-source connectedness; finite odd translation eigenspaces cannot contain the contact system. Independent local constant/linear jets supply a transposition in exactly one node type, hence the full product of symmetric groups.',
'lem:mixed-odd-normalization-block-hearts-candidate':'Complete proof independently rederived: exact normalization sequence, odd-isogeny ambient isomorphism, sourceGL_(9d-1), explicit order inequality distinguishing every alternating factor, Goursat and natural-dualH1 actual-block extraction. Shifted covers retain full individual images on the connected prescribed-sum fibres, and their disjoint single-factor inertia gives the full product. Pure shifted torsor labels annihilating the ambient line fix all source cohomology and other type nodes, yielding actual type-specific shears and everyHom(U,sumhearts).',
'lem:mixed-odd-common-graph-candidate':'Both uniform graph assertions fully rederived for arbitrary odd finite abelianK. Fixed loops anchor the annihilator constants; varying selected lifts and the odd3d-star relation force all coefficients zero, so the hearts span all graph cohomology. In the puregraph branch a pair vector violates a newly selected triple; remaining type constants define an additiveK-to-F2function and vanish. The exact nine-case program was read fully before an isolated rerun; it does not prove the geometric claims.',
'prop:mixed-odd-balanced-irreducibility-candidate':'Complete proof independently rederived: u>t separates the zero-projection and surjective-projection dimension ranges uniformly across source twists. All common targets have full unit rankr, so one actual fibreS_Y is used. In the zero branch the graph lemma givesS_Y=0; in the surjective branch its entire graph containsT_r and surjectivity toU_r givesS_Y=V_Y. No covector shortcut or rank-drop specialization is used.',
'thm:mixed-every-fixed-modulus-all-odd-candidate':'Complete proof independently rederived: restriction to normal transvection closure is semisimple. The unique naturalGL_u constituent and everytypeheart lie in one simple summand of dimension>=r-t>r/2; its conjugates must coincide, hence irreducibility makes it allV. Exact Kantor-Seress3.6 proper alternatives are excluded by the actual natural block. Perfect-field geometric and arithmetic images both equalGL_(9d²-1).',
'rem:mixed-all-odd-norm-scope-candidate':'Scope checked: all odd balanced mixed-product degrees, including every fixed ordinary modulus; even degrees and general ambient classification remain separate. Universal graph proof is not inferred from finitely many examples. Prior strip, H1, original classification and jet proofs were reread; no new external theorem or priority assertion is imported.'}
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for label,detail in checks.items():writer.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root','full mathematical/source/code audit','PASS. '+detail])
record={'status':'FULL MATHEMATICAL AND CODE PASS','actual_utc':now,'events':len(checks),
        'root_rerun_seconds':run['runtime_seconds'],'graph_cases':len(run['cases']),
        'author_output_sha256_unchanged':before,
        'source_scope':'Complete current candidate including all clarification repairs, full supporting code and prior small-degree jet, strip lifted-cover, H1 and finite-Lang dependency proofs read. Retained original Kantor-Seress3.6 text reread in the immediately preceding degree3audit; its earlier actual page-image audit is reused without a fresh image claim.',
        'remaining_gate':'Even balanced fixed mixed-product degrees>=4 and arbitrary-X structural groups.'}
dest=w/'outputs/root_mixed_all_odd_audit.json';assert not dest.exists()
dest.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
