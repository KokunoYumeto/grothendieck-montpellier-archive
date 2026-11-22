"""Complete norm-eleven geometric proof audit after full universal reruns."""
from pathlib import Path
import datetime,hashlib,json,shutil,subprocess,sys
w=Path(__file__).resolve().parents[1]
agent=w/'agents/monodromy'
candidate=agent/'nonordinary_uniform_eleven_theta_geometry_candidate.tex'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(candidate)=='f240bd69cb86e8401c4896902faf709726852f4740b5d4455e0b1fec55b48cb9'
runs=json.loads((w/'outputs/root_eleven_independent_runs.json').read_text())
assert runs['status']=='PASS_ALL_SIX_UNIVERSAL_STAGES'
env=w/'outputs/root_eleven_independent_environment'
source=agent/'code/post_CP27_eleven_binary_bezout_check.py'
author=agent/'outputs/post_CP27_eleven_binary_bezout_check.json'
before=sha(author)
dest=env/'code'/source.name
assert not dest.exists();shutil.copy2(source,dest)
with (env/'binary_only.stdout.txt').open('w') as stdout, (env/'binary_only.stderr.txt').open('w') as stderr:
    run=subprocess.run([sys.executable,str(dest)],cwd=env,stdout=stdout,stderr=stderr)
assert run.returncode==0
a=json.loads(author.read_text());b=json.loads((env/'outputs'/author.name).read_text())
omit={'runtime_seconds','actual_utc'}
assert {k:v for k,v in a.items() if k not in omit}=={k:v for k,v in b.items() if k not in omit}
assert sha(source)==sha(dest) and sha(author)==before
data={
 'status':'FULL GEOMETRIC PROOF, DEPENDENCY AND UNIVERSAL CERTIFICATE PASS',
 'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'candidate_sha256':sha(candidate),
 'labels':[
  'lem:uniform-eleven-interpolation-candidate','lem:uniform-eleven-quintic-fibres-candidate',
  'lem:uniform-eleven-good-parameters-candidate','thm:uniform-eleven-nodal-self-isogeny-candidate',
  'cor:f0-odd-multiples-eleven-candidate','rem:uniform-eleven-verification-scope-candidate'],
 'checks':{
  'interpolation':'Complete norm-seven quaternion/normal-form argument freshly reread. Rosati norm of3+g+h is11, so the same-surface polarized isogeny is etale of degree121. All prescribed points are distinct, and the arbitrary H0(7W) section with a triple zero has exactly the displayed reversible linear equations. gamma nonzero prevents simultaneousY=Z=0, proving the unique nonspecial residual degree-two divisor and excluding every finite theta-kernel point. The complete universal interpolation rerun checks arbitrary-section rows, norm factorization and both residual coefficient identities.',
  'fibres':'Infinity is excluded by the actual theta-kernel argument. Equal-x points are hyperelliptic conjugates; a common image would be geometric2-torsion, hence zero in two-rank0, already excluded. AtZ=0 there are two distinct nonzeroY values and A3=Y squared/D is nonzero; the residual divisorW+R determines p uniquely for eachY. Those fibres cannot meet finite degree-two residual divisors. This also permits doubled finite residuals. AtZ nonzero the monic quintic is separable for EVERY finiteL because its derivativeZ squared cannot vanish at a root; the regular polynomialu identity is checked without dividing byY orL0.',
  'triple_value':'The quartic reduction gives A(L)p=B+J. AtA nonzero, distinct points in a common fibre give distinctY roots and a triple root of the P-characteristic polynomial. Ordinary and second Hasse derivatives yield precisely F1/F2, or c3=c2=0. Omitting the additional equation in the latter branch enlarges the bad locus, as the corrected wording states. AtA=0, distinctB-values determine at most oneY and the remaining quadratic has at most two p solutions, includingL0=0 orL=0. A triple therefore forces the separate repeated-B resultant.',
  'universal_certificate':'Both characteristic polynomials are universal over the explicit localized binary coefficient ring; no sampled surface substitutes for the calculation. Root recomputed the full Sylvester resultants of degrees121104,3944,3540 from the frozen inputs, then independently reran all factor products, G10 inclusion and the explicit five-polynomial Bezout sum. Nonzero resultants exclude common roots at every specialization, including leading-coefficient drops. Deleted factors lie only inF4, already excluded. Every denominator in the geometry is included or is forced nonzero by the parameter hypothesis.',
  'all_moduli':'The modulus numerator equation D12(V)^5+mu^5 H4(V)^12 is monic degree60 and has no F4 root becauseD12 equals1 there. Translation by1, reciprocal and multiplication by either nontrivialF4 unit preserve its ratio and stay outsideF4. If all five parameters were bad, both omega-components and the three other Bezout polynomials would vanish; the exact identity1 excludes this. The argument includesmu0 without an orbit-size assumption. Changing the fifth-root normalization realizes the prescribedmu rather than merelymu^5.',
  'geometry_and_transfer':'Complete odd-kernel theta-nodality proof and good-theta norm transfer reread. Triple-free fibres give only transverse nodes, with normalizationgenus2 and arithmeticgenus122, hence120 nodes. The isogeny is a self-isogeny, so its incoming direction is correct. The known degree-one source gives the complete |33Theta| degree-eleven group; arbitrary odd incoming nonproduct sources and the already audited cubic-component transfer with e11 give every odd multiple11 in the complete systems|3dTheta|. Products are covered by their separate all-degree theorem. Full geometric GL forces the same arithmetic GL over any perfect ground field. No two-rank-one extension or arbitrary-polarization conclusion is inferred.',
  'preservation_and_scope':'All six unchanged-source root reruns reproduce every mathematical author field; original worker entry points are run under a retained180-second yielding harness to avoid the exploratory60-second cap. All author sources/outputs remain unchanged. Prior timeouts, serialization errors and the incomplete finite-field inference are preserved and are not used. The main fixed-f0 odd gate strictly moves from11 to13; generalA4 and fixed-f1degree5/even8 remain open.'},
 'independent_runs':runs['stages'],
 'additional_binary_only_runtime_seconds':b['runtime_seconds'],
 'additional_binary_source_sha256':sha(source),
 'additional_binary_author_output_sha256':before,
 'all_author_mathematical_fields_equal':True,
 'source_scope':'Fresh complete internal norm-seven quaternion/interpolation, odd-kernel nodality and good-theta norm-transfer proofs read. Previously fully audited normal-form, incoming-neighbour and cubic-component source proofs are reused with their exact hypotheses. No new external theorem is imported.',
 'literature_scope':'Fresh two-engine targeted searches for supersingular genus-two norm11 nodal theta images recorded in ROOT_SEARCH_LOG_28.md. Returned complex/generic isogeny comparisons are not used as characteristic-two all-modulus theorems; no priority claim.'}
out=w/'outputs/root_uniform_eleven_theta_audit.json'
assert not out.exists();out.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({k:v for k,v in data.items() if k!='checks'},indent=2))
