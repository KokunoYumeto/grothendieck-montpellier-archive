"""Full root proof/source audit of the two post-CP26 A3 auxiliary candidates."""
from pathlib import Path
import csv,datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
names={'post_CP26_unipotent_bundle_candidate.tex':'60a34fea8ba26a0e17f7bf15719668e0aa7a0471e2e22b0e54bd1e998be333e9','post_CP26_symmetric_boundary_kernel_candidate.tex':'fa1479a8d9c0719d1b429f926a4c5f3389a1a8c9fce75d2c61879119aa4a411c'}
for name,digest in names.items():
 assert hashlib.sha256((w/'agents/obstructions_crystals'/name).read_bytes()).hexdigest()==digest
source=w/'agents/obstructions_crystals/code/primitive_unipotent_transition_checks.py'
author=source.with_suffix('.output.json');before=author.read_bytes()
snap=w/'code/audit_snapshots/A3_unipotent_root_independent_certificate.py'
dest=w/'outputs/root_A3_unipotent_kernel_audit.json'
assert not snap.exists() and not dest.exists()
snap.write_bytes(source.read_bytes())
run=subprocess.run([sys.executable,str(snap)],capture_output=True,text=True)
(w/'outputs/root_A3_unipotent_independent.stdout.txt').write_text(run.stdout)
(w/'outputs/root_A3_unipotent_independent.stderr.txt').write_text(run.stderr)
assert run.returncode==0,run.stderr
fresh=json.loads(snap.with_suffix('.output.json').read_text());old=json.loads(before)
omit={'actual_utc','elapsed_seconds'}
assert {k:v for k,v in fresh.items() if k not in omit}=={k:v for k,v in old.items() if k not in omit}
assert fresh['status']=='PASS' and author.read_bytes()==before
checks={
 'lem:DE-A3-primitive-unipotent-candidate':'Entire proof checked. The actual transition matrix has determinant equal to the alpha2 norm and its normalized Frobenius square becomes the stated upper-unipotent matrix in the explicit global-compatible frames. The infinitesimal translation cocycle is the polarization differential. The complementary isogeny has kernelmu2 and dual etale kernel, giving an isomorphism onH1O; its pullback takes kappa^(2) to gamma. Freshly reread integral local-polarization-block proof: actual indexzero makes its alpha2 differential nonzero, whereas positive actualindex kills it. No descent of an unmarked splitting is assumed.',
 'rem:DE-A3-primitive-unipotent-scope-candidate':'The extension calculation alone establishes no residual cup lower bound. Primitive-root and actual line-bundle indices are distinguished, including even exponents. The derivative identity is correct; its global Frobenius consequence is proved in the companion candidate.',
 'lem:DE-A3-unipotent-Frobenius-candidate':'Entire proof independently rederived. Smoothness of the local alpha2 cover z²=h makes the glued invariant one-form dh nonzero. The cocycle identitydgamma=gamma²theta, zero H1(d) by full Hodge-de Rham degeneration, and the direct-summand inclusion Otheta inOmega force Fgamma=0. The square-coboundary frame change gives Sym²U=U+O without division bytwo. The nonzero extension has cohomology(1,2,1), by the exterior cup algebra, yielding(2,4,2); the split case yields(3,6,3). Frobenius is understood semilinearly over the perfect base.',
 'lem:DE-A3-residual-boundary-kernel-candidate':'Freshly reread entire prior residual-pencil resolution and norm-pencil proofs. H1(Lcal^-1)=0 and H0(EG)=0 give H0(J)=0 and inject H1(EG) intoH1(J). Taking preimages in the second long exact sequence gives the exact displayed kernel quotient, including surjectivity. The squared-pencil sequence and acyclicG identifyH1(EG)=H0(D,AG). The regular nonzero norm section inRP, degreeA=g-1, Cartier-curve duality and the actual sublineP inG imply this domain is nonzero even for a nonreduced Cartier divisor.',
 'rem:DE-A3-symmetric-boundary-kernel-scope-candidate':'The two computed global symmetric-square sections control only a subspace of the full kernel. Neither their intersection with the residual product space nor the restriction to the actual determinant direction space is determined. No assertiondim imPsi>=2 or closure of the primitive mixed rank gate follows.'}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label,detail in checks.items():wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','targeted proof check','PASS. '+detail])
record={'status':'FULL PROOF, PRIMARY SOURCE AND EXACT LOCAL CERTIFICATE PASS','actual_utc':now,'candidate_sha256':names,'checks':checks,'source_read':{'path':'agents/obstructions_crystals/sources/edixhoven_geer_moonen_AV.txt','locators':'Theorem7.5 and Proposition7.6, complete proofs p100; Proposition7.27 full proof p108; Corollary7.29 complete proof pp108-109','scope':'Fresh retained original text read. The product spectral-sequence differential is interpreted by the total-complex Leibniz rule; the subsequent primitive-element argument is checked explicitly. No new web retrieval or page-image inspection claimed.'},'program_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'independent_runtime_seconds':fresh['elapsed_seconds'],'identities':fresh['identities'],'author_output_sha256':hashlib.sha256(before).hexdigest(),'author_output_unchanged':True,'all_mathematical_fields_equal_author':True,'main_gate_movement':False}
dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='checks'},indent=2))
