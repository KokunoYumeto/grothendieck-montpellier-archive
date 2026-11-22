"""Retain two isolated exact reruns and the complete uniform-Q root audit."""
from pathlib import Path
import csv,datetime,json,hashlib,contextlib,io
w=Path(__file__).resolve().parents[1]
proof=w/'agents/monodromy/nonordinary_ppav_uniform_Q_inertia_candidate.tex'
runs=[]
for stem in ['ppav_theta_Q_pencil_pfaffians_complete','ppav_theta_equal_cubes_F8_witness']:
    source=w/'agents/monodromy/code'/f'{stem}.py'
    author=w/'agents/monodromy/outputs'/f'{stem}.json'
    before=hashlib.sha256(author.read_bytes()).hexdigest()
    old="Path(__file__).resolve().parents[1]/'outputs/"+stem+".json'"
    text=source.read_text();assert text.count(old)==1
    dest=w/'outputs'/f'root_{stem}.json';assert not dest.exists()
    executed=text.replace(old,'Path('+repr(str(dest))+')')
    snapshot=w/'code/audit_snapshots'/f'{stem}_at_root_audit.py';assert not snapshot.exists()
    snapshot.write_text(executed);out=io.StringIO()
    with contextlib.redirect_stdout(out):
        exec(compile(executed,str(snapshot),'exec'),{'__file__':str(source),'__name__':'__main__'})
    (w/'outputs'/f'root_{stem}_stdout.txt').write_text(out.getvalue())
    result=json.loads(dest.read_text());assert result['status']=='PASS'
    assert before==hashlib.sha256(author.read_bytes()).hexdigest()
    runs.append({'program':stem,'root_runtime_seconds':result.get('runtime_seconds',result.get('elapsed_seconds')),
                 'author_output_sha256_unchanged':before})
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checks={
'lem:nonordinary-uniform-Q-stable-loss-candidate':'Complete proof independently rederived. Smooth Fermat cubic Q is integral and no nonzero allowed q is proportional to it. At q!=0 onQ, the coherent linearization has kernelks and rank7; its second image has rank7 exactly when s^t*u^[2]!=0 for M(s)u=s^[2]. This follows directly from the annihilator of the squared first image and is independent of replacingu byu+cs. The universal four-coordinate isotropic pencil and both six-Pfaffian identities were rederived and exactly rerun. The coefficient-support case analysis reduces every failure of that pencil to four equal nonzero cubes, with the excluded one/three-support cases exactlyq=0. Quadratic mu3 phases have evaluation image the sum-zero hyperplane onfour directions; a scalar supplies the last direction, and the unitary basis change preserves the typed relative Frobenius. Nonzero tensor scaling preserves all iterated ranks. The exact GF8 normal-form witness, independently reconstructed, hasQ=0,q=7,Mu=s² andeta=7. Openness on integralQ gives generic stable rank7, determinant order1 and the identity projective coherent-kernel map.',
'cor:nonordinary-ppav-uniform-root-inertia-candidate':'Complete application independently checked. The actual nonordinary ppav tensor hasq!=0 by the earlier globally generated Frobenius-bundle simplicity argument. The Euler relative bundle embeds in the constant9-space on an affine chart. AlongQ its kernel map is the identity on a smooth7-dimensional cubic, so has differential rank7. Every hypothesis of the fully reread moving-kernel lemma holds; its seven independent Artin-Schreier classes give the full2^7 geometric inertia subgroup. Restriction to the dense smooth-member open preserves the finite image. No global irreducibility or fullGL8 conclusion is made.',
'rem:nonordinary-ppav-uniform-root-scope-candidate':'Full source-code and output scope checked. Universal polynomial identities and one exactly justified exceptional normal form are proof inputs; the finite exploratory searches and their failures are retained but are not extrapolated. Author outputs are unchanged under the two isolated root executions. The global nonzero Lang-cover exceptional incidence remains open.',
'lem:moving-kernel-full-root-inertia-candidate':'Entire earlier proof freshly reread. Strict henselian finite Lang sections frame the stable part; the remaining Frobenius column is(b,tc). In the constant ambient bundle, squared frame entries have zero differential, so the projective kernel differential has rank equal to the differentials ofb0. Each nonzero binary combination gives a nonsquare residue leading coefficient at pole order2, excluding an Artin-Schreier coboundary even over the imperfect separably closed residue field. The resulting full2^(r-1) group fixes the stable hyperplane and quotient. Prior primary finite-part/purity reads are reused; no fresh source image is claimed.',
'lem:DE-A3-theta-pfaffian':'Entire earlier four-parameter Pfaffian proof and relative determinant calculation freshly reread, along with the theta symmetrizer proof. Their already-proved factorizationq²Q is a dependency, not a newly claimed result. Oda simplicity is reused only with the already verified finite-isogeny hypotheses.'
}
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for label,detail in checks.items():writer.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root','full mathematical/source/code audit','PASS. '+detail])
record={'status':'FULL MATHEMATICAL AND CODE PASS','actual_utc':now,'events':len(checks),
        'new_assertions':3,'candidate_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
        'isolated_reruns':runs,'remaining_gate':'Global nonzero Lang-cover connectedness or another irreducibility proof on every fixed nonproduct nonordinary principal surface.'}
dest=w/'outputs/root_nonordinary_uniform_Q_audit.json';assert not dest.exists()
dest.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
