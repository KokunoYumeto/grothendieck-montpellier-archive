"""Root complete uniform-seven audit with isolated, output-preserving reruns."""
from pathlib import Path
import csv,datetime,hashlib,json,subprocess,sys
w=Path(__file__).resolve().parents[1]
candidate=w/'agents/monodromy/nonordinary_uniform_seven_theta_geometry_candidate.tex'
assert hashlib.sha256(candidate.read_bytes()).hexdigest()=='c671846e4b3b64d066003ed6d63af5b8e96c11c936e68fcff62c3b60e6e96cef'
dest=w/'outputs/root_uniform_seven_audit.json'; assert not dest.exists()
snap=w/'code/audit_snapshots/uniform_seven'
(snap/'code').mkdir(parents=True,exist_ok=True); (snap/'outputs').mkdir(exist_ok=True)
runs=[]
for stem in ('verify_nonordinary_seven_good_parameters','nonordinary_seven_q8_interpolation'):
    source=w/f'agents/monodromy/code/{stem}.py'
    author=w/f'agents/monodromy/outputs/{stem}.json'; before=author.read_bytes()
    copy=snap/f'code/{stem}.py'; assert not copy.exists(); copy.write_bytes(source.read_bytes())
    run=subprocess.run([sys.executable,str(copy)],capture_output=True,text=True)
    (snap/f'outputs/{stem}.stdout.txt').write_text(run.stdout)
    (snap/f'outputs/{stem}.stderr.txt').write_text(run.stderr)
    assert run.returncode==0,run.stderr
    fresh=json.loads((snap/f'outputs/{stem}.json').read_text()); old=json.loads(before)
    omit={'actual_utc','actual_timestamp_utc','runtime_seconds'}
    assert {k:v for k,v in fresh.items() if k not in omit}=={k:v for k,v in old.items() if k not in omit}
    assert fresh['status'].startswith('PASS') and author.read_bytes()==before
    runs.append({'source':str(source.relative_to(w)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                 'independent_copy':str(copy.relative_to(w)),'runtime_seconds':fresh['runtime_seconds'],
                 'author_output_sha256':hashlib.sha256(before).hexdigest(),'author_output_unchanged':True,
                 'all_mathematical_output_agrees':True})
subprocess.run([sys.executable,str(w/'code/root_uniform_seven_symbolic_rederivation.py')],cwd=w,check=True)
extra=json.loads((w/'outputs/root_uniform_seven_symbolic_rederivation.json').read_text())
checks={
 'lem:uniform-seven-interpolation-candidate':
 'Complete proof and all18-identity program read. Rechecked the Q8 curve identities, Rosati product7 and degree49. Independently rederived both arbitrary-section value rows in a retained exact program. The nonzero Dc_g gives a unique section for every finiteP includingZ=0, hence nonspecial degree2 residual divisor and no nonzero kernel-theta point.',
 'lem:uniform-seven-triple-obstruction-candidate':
 'Checked W, conjugate pairs, and all four distinct Z=0 roots before affine elimination. AtZ=0 the pole drops6 and residual x(R)=p+aD^2/c_g^2 is distinct. ForZ nonzero the cubic has nonzero constant and derivativeZ^2. Rederived both global quadratic coefficients and A(L)p=B(Z). Independently calculated P1 andP2 from the generic remainder, without Q8 specialization. A nonzero requires three distinctZ; A zero requires two distinct quadratic roots and gives exactlyT. Repeated roots andL=0 are covered without division byL.',
 'lem:uniform-seven-parameter-certificate-candidate':
 'Entire final universal certificate read, including the earlier exploratory provenance. Pseudo-division uses no leading-coefficient inverse, so its necessary obstruction survives degree drops. The separate monic cubic determinant coversA=0. Exact isolated rerun reproduces both norms, displayed squarefree radicaldegree97, c_g norm, and coefficient gcdz^3+z^2+1; r andz denominators have the stated excluded support. The three-r cover is separable and the coefficient specialization implication is valid.',
 'thm:uniform-seven-nodal-self-isogeny-candidate':
 'Freshly reread the full normal-form and odd-kernel nodality proofs. The degree10 presentation polynomial has ten distinct nonzero roots for nonzero modulus and hence avoids the three badz; moduluszero has two order3 roots, neither bad. Fifth-root scaling preserves the prescribed modulus. Thus an actual self-isogeny of the fixed surface has no triple fibre. The exact odd-kernel criterion gives integral nodal image and48nodes.',
 'cor:f0-three-five-seven-degree-groups-candidate':
 'Freshly reread the complete good-theta norm-step theorem and prior fixed3/5degree corollary. The incoming direction is satisfied by the SELF-isogeny; the fixed Pic0 discrepancy is already corrected by target translation. Iterate multipliers5and7 from3powers, then apply the proved even-addition theorem. Exact ambient covector bounds give arithmetic equality over each perfect base. Product surfaces already satisfy all degrees.',
 'rem:uniform-seven-scope-candidate':
 'No universal all-kernel or all-positive-degree assertion follows. Fixed-curve finite Groebner explorations and failures remain retained but are not proof inputs. These are universal algebra identities combined with the complete geometric argument, not extrapolation from a finite census. No fresh external-original read or priority claim is made.'}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for label,detail in checks.items():
        writer.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','targeted proof check','PASS. '+detail])
record={'status':'FULL PROOF AND UNIVERSAL CERTIFICATE PASS','actual_utc':now,
        'candidate':str(candidate.relative_to(w)),'candidate_sha256':hashlib.sha256(candidate.read_bytes()).hexdigest(),
        'checks':checks,'isolated_runs':runs,'independent_symbolic_rederivation':extra,
        'source_scope':'Previously source-audited complete normal-form, odd-theta, and norm-transfer proofs rechecked; no new external source retrieval claimed.'}
dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='checks'},indent=2))
