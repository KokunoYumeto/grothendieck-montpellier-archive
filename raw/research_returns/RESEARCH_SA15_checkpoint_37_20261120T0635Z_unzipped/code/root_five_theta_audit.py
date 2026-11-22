"""Retained independent reruns and full geometric audit for the C0 five-isogenies."""
from pathlib import Path
import csv, datetime, hashlib, json, subprocess, sys

w=Path(__file__).resolve().parents[1]
dest=w/'outputs/root_five_theta_audit.json'
assert not dest.exists()
candidate=w/'agents/monodromy/nonordinary_five_theta_self_isogenies_candidate.tex'
runroot=w/'outputs/root_five_theta_independent_run'
(runroot/'code').mkdir(parents=True,exist_ok=False)
(runroot/'outputs').mkdir()
records=[]
for stem in ['nonordinary_five_theta_packet_probe','nonordinary_five_theta_self_isogenies']:
    source=w/'agents/monodromy/code'/f'{stem}.py'
    authorout=w/'agents/monodromy/outputs'/f'{stem}.json'
    before=authorout.read_bytes()
    snap=runroot/'code'/source.name
    snap.write_bytes(source.read_bytes())
    p=subprocess.run([sys.executable,str(snap)],capture_output=True,text=True)
    (runroot/'outputs'/f'{stem}.stdout.txt').write_text(p.stdout)
    (runroot/'outputs'/f'{stem}.stderr.txt').write_text(p.stderr)
    assert p.returncode==0,(stem,p.stderr)
    result=json.loads((runroot/'outputs'/f'{stem}.json').read_text())
    original=json.loads(before)
    omit={'actual_utc','runtime_seconds','base_output_sha256'}
    assert {k:v for k,v in result.items() if k not in omit}=={k:v for k,v in original.items() if k not in omit}
    assert authorout.read_bytes()==before
    records.append({'program':str(source.relative_to(w)),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                    'retained_independent_copy':str(snap.relative_to(w)),'runtime_seconds':result['runtime_seconds'],
                    'actual_utc':result['actual_utc'],'all_mathematical_output_equals_author_output':True,
                    'author_output_unchanged':True})

checks={
 'lem:five-theta-explicit-Weil-candidate':'The genus-two Artin-Schreier basis dx,x dx has Cartier images0,dx, hence f0 and J[2](k)=0. For every a in F16, Tr(a^5)=0 gives two b. Directly fP^2+fP=(x+a)^5, fP(P)=0 and fP(iota P)=1; its unique pole has order5. The common local parameter z=x^2/y has z^5 fP tending to1. The stated tame-symbol moving-divisor computation was rederived: fP(div h-W)=h(P)^5/(cP d^5), and the Weil quotient becomes fP(Q)cQ/(fQ(P)cP). The exact nonsingular four-by-four pairing matrix therefore proves a rational basis of all J[5], without an assumed Jacobian group law. All finite code and actual exact rerun were checked.',
 'lem:five-theta-geometric-census-candidate':'Full geometric exhaustion rederived. A nonzero translate of the principal theta has intersection length2 and no common component. If P,P+g lie on theta, its two possible intersection points are P and -P-g, counted with multiplicity. A nonrational point of a rational length2 scheme must be interchanged with the other by Frob16; two distinct nonzero g,h in a triple yield contradiction. Thus every geometric triple is rational. Equality of tangent lines is exactly the canonical hyperelliptic pair P,-P. From2P in K and J[2](k)=0 one gets P in J[5] and then P in K; W,P,-P are distinct in one rational packet. The 156 maximal isotropic planes are completely enumerated with every basis and packet retained:20 have maximum2,80 maximum4,56 maximum5. Good planes have no geometric tangencies or higher packets. The etale quotient restricts immersively and birationally to theta because its translation stabilizer is trivial; transverse doubles are ordinary nodes. Numerical class5Theta gives genus26, hence24 nodes over the genus2 normalization.',
 'prop:five-theta-twenty-self-isogenies-candidate':'Direct substitution verifies every displayed automorphism; squaring adds alpha^10+alpha^5=1 and fixes W. Its induced polarized action has g^2=-1 and g dagger=-g, so(2-g)(2+g)=5. This proves a separable degree25 polarized isogeny, with maximal isotropic5-kernel. The exact supplement checks all actions on the four torsion basis vectors and all33 curve vectors, preservation of J5, twenty distinct25-element kernels, and equality with all twenty good census planes. The symmetric norm line has numerical class5Theta, so differs by a symmetric Pic0 class, which is2-torsion and zero since f0. Hence the images belong to the actual complete system. All claims are restricted to J(y^2+y=x^5).',
 'rem:five-theta-self-isogeny-scope-candidate':'No all-modulus or degree5 monodromy claim follows. In particular the exponent3 eigenmap argument cannot be transferred to a5-torsion translation of3Theta. The twenty explicit good self-neighbours are a bounded geometric input only; S18 and full gluing remain open.'}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for label,detail in checks.items():
        wr.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15','targeted proof check','PASS. '+detail])
result={'status':'FULL MATHEMATICAL PROOF AND EXACT RERUNS PASS','actual_utc':now,
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':hashlib.sha256(candidate.read_bytes()).hexdigest(),
 'independent_reruns':records,'checks':checks,
 'source_read':{'source':'Boxall, Grant, and Leprevost (2001), 5-torsion points on curves of genus2',
 'exact_locator':'Example1.2(ii), printed pp30-31; Proposition1.1 statement',
 'original_url':'https://euclid.colorado.edu/~grant/publications/5torsion_points_on_curves_of_genus_2.pdf',
 'root_browser_ref':'turn615687814view0',
 'scope':'Original author-hosted published PDF reopened and full Example1.2(ii) read; its fifth-order function calculation was independently proved here. No uninspected Igusa classification or other theorem is imported.'}}
dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
