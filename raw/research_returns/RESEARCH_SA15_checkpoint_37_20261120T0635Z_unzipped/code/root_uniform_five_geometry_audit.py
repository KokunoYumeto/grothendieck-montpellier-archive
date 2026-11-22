"""Retained full proof audit and exact universal-identity rerun."""
from pathlib import Path
import csv,datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/root_uniform_five_geometry_audit.json';assert not dest.exists()
candidate=w/'agents/monodromy/nonordinary_uniform_five_theta_geometry_candidate.tex'
source=w/'agents/monodromy/code/nonordinary_uniform_five_self_isogeny_identities.py'
author=w/'agents/monodromy/outputs/nonordinary_uniform_five_self_isogeny_identities.json'
before=author.read_bytes();run=w/'outputs/root_uniform_five_geometry_independent_run'
(run/'code').mkdir(parents=True,exist_ok=False);(run/'outputs').mkdir()
snap=run/'code'/source.name;snap.write_bytes(source.read_bytes())
p=subprocess.run([sys.executable,str(snap)],capture_output=True,text=True)
(run/'outputs/stdout.txt').write_text(p.stdout);(run/'outputs/stderr.txt').write_text(p.stderr)
assert p.returncode==0,p.stderr
data=json.loads((run/'outputs'/author.name).read_text());old=json.loads(before)
omit={'actual_utc','runtime_seconds'}
assert {k:v for k,v in data.items() if k not in omit}=={k:v for k,v in old.items() if k not in omit}
assert before==author.read_bytes()
checks={
 'lem:uniform-f0-order-four-presentation-candidate':'The previously fully proved Cartier normal form was freshly reread: its triangular Cartier matrix forces constant nonzero hyperelliptic coefficient in f0. Starting from x^5+mu x^3+nu x, the stated separable degree16 equation for t gives A^2=t and B=t^4+mu t^2+nu with B^2=mu t+A; the AS shift removes all degree4,2,1 terms, and the explicitly added constant shift removes the new constant. The degree10 covering equation in z has constant1 and hence a nonzero root; a fifth-root scaling and its mu5 adjustment give a=z²,b=z²+z+1. Direct q²+q=F(x+1)+F(x) and q(x+1)+q(x)=1 prove the order4 automorphism. The original BGL normal-form remark was read, but no uninspected Igusa classification is imported.',
 'thm:uniform-f0-five-self-isogeny-nodal-candidate':'Complete proof rederived. The polarized automorphism has Rosati adjoint-g, so(2-g)(2+g)=5 gives separable degree25. The basepointW of |3W| excludes any finite theta point in its kernel. Exact interpolation of y at2P+gP yields the displayed residual quadratic U_P and an effective finite degree2 divisor E_P, even with overlapping multiplicities. The function y+v cannot vanish at both points over a finite x, so E_P is nonspecial and its degree2 linear system has dimension0. Equality of phi images therefore identifies E_P and U_P; their coefficients imply(p+q)(a(p+q)+ell)=0 and at most2 x values. A same-x hyperelliptic pair in a fibre would map to geometric2-torsion, hence0 in f0, already excluded. W has a singleton fibre. The etale isogeny gives an immersion; trivial theta translation stabilizer gives birational normalization; the canonical Gauss map then excludes equal tangents at distinct pairs. Thus only ordinary nodes occur. Symmetry and absence of geometric Pic0[2] put the image in actual |5Theta|, and genus26 minus2 gives24 nodes.',
 'lem:nonproduct-three-theta-four-values-candidate':'Full theta-product argument checked, including the repaired three-value bridge. Any three distinct points impose independent conditions: select theta factors through the first two, avoid their finite forbidden sets at the third, then use dominant addition Theta²->A to keep the remaining factor away. For t=sum of three points outsideTheta, Z_t inTheta² is a nonempty proper divisor. A constant projection or constant sum on a component would force respectivelyu=t,v=t,orsum0, hence t inTheta, contradiction. All three finite forbidden sets can therefore be avoided to isolate the fourth point. Together with the already proved three-value rank this forces rank4; the contrapositive gives all four triple sums inTheta. For P,P+h,Q,Q+k the two sum variables lie in finite theta intersections, and their linear map has determinant-3, a finite etale isogeny in characteristic2. Thus the four-value exceptional locus is finite for all fixed nonzero h,k. All Picard twists follow by translation of3Theta.',
 'rem:uniform-five-theta-geometry-scope-candidate':'Nine universal identities were read and exactly rerun, preserving the original output; all mathematical results match. The initial coefficient-domain setup failure remains retained and is not described as a failed identity. This theorem removes the good theta-five-self-neighbour prerequisite for every fixed f0 Jacobian and supplies the stated four-value incidence geometry. It does not prove isolated node-cover inertia, full gluing, degree5 full monodromy, or the f1 analogue.'}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label,detail in checks.items():wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','targeted proof check','PASS. '+detail])
result={'status':'FULL MATHEMATICAL PROOF AND UNIVERSAL CERTIFICATE PASS','actual_utc':now,
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':hashlib.sha256(candidate.read_bytes()).hexdigest(),
 'program_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'author_output_unchanged':True,
 'independent_runtime_seconds':data['runtime_seconds'],'all_mathematical_output_equals_author_output':True,
 'checks':checks,'source_scope':'Freshly reread the full already proved Cartier normal-form paragraph. BGL original Example1.2(ii), pp30-31, was freshly read in this session. No new external theorem is claimed from an unread source.'}
dest.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
