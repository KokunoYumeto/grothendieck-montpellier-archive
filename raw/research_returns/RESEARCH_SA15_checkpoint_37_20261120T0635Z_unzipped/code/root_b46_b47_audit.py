"""Independent full residual-branch audits with preserved author outputs."""
from pathlib import Path
from contextlib import redirect_stdout
import csv,datetime,io,json
w=Path(__file__).resolve().parents[1]
outputs=[]
for stem in ['verify_p2_residual_trivial_gate','verify_p2_residual_c2_gate']:
    program=w/'agents/reduction_descent/code'/f'{stem}.py'
    author=program.with_suffix('.output.json')
    dest=w/'outputs'/f'root_{stem}.json'
    assert not dest.exists()
    before=author.read_bytes();old_write=Path.write_text;capture=io.StringIO()
    def write(path,data,*args,**kwargs):
        assert path.resolve()==author.resolve()
        return old_write(dest,data,*args,**kwargs)
    try:
        Path.write_text=write
        with redirect_stdout(capture):
            exec(compile(program.read_text(),str(program),'exec'),{'__name__':'__main__','__file__':str(program)})
    finally:
        Path.write_text=old_write
        (w/'outputs'/f'root_{stem}.stdout.txt').write_text(capture.getvalue())
    assert author.read_bytes()==before
    out=json.loads(dest.read_text());assert out['status']=='PASS'
    outputs.append({'program':stem,'elapsed_seconds':out['elapsed_seconds'],'status':out['status']})
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
('lem:B-RD46-discriminant','independent re-proof','PASS: full proof rederived. Unramified completion preserves inertia and valuation; exact finite special groups have orders1,2,3,4,6,8,24. Scaling x=u²x0,y=u³y0 gives Delta=u^12 Delta0 and omega=u^-1 omega0, hence12v(c)=-m delta. The order3 tame cotangent character is primitive, and averaging a parameter proves an order3 elliptic automorphism with derivative1 would be identity. Thus3|m iff3 does not divide delta. The unique cubic tame quotient identifies characters as functions on inertia. The corrected differential sign is accepted; the failed earlier draft remains retained.'),
('prop:B-RD46','independent re-proof','PASS: entire Legendre/Kummer argument and exact program read. Permuting roots and quadratic twisting permits q=v(lambda)>=0,v(1-lambda)=0; potentially supersingular j forces q0,1,2,3. The discriminant table isolates q1. Halving points produce the full rho4=I+2(chi_d I+chi_-1 T+chi_lambda N+chi_1-lambda U), including dependent quadratic characters. The valuation functional supplies an actual element of each finite Kummer compositum. Scalar/nonscalar excludes q0/2; q1/3 forces centralization of N and preservation of the upper-right character, but1-lambda is nonsquare in the former case and square by Hensel in the latter. The normal wild2-subgroup and cyclic odd tame quotient exclude residualS3. No residualC3 existence claim.'),
('lem:B-RD47','independent re-proof','PASS: quotient equation and normalized differential independently derived; source and quotient2-fields are K(sqrt D),K(sqrt b). Over complete e1 with algebraically closed residue, z²+z=u lifts and gives1+4R inside squares. Twisting normalizes beta=v(b) to0or1 and changes discriminant valuation by6v(t), so preserves every stated invariant. All alpha<=0 cases force D square; beta0,alpha1,r>=2 forces b square. The four surviving rows give (beta,vD,delta,vj)=(0,2,6,6),(0,3,7,5),(1,2,8,7),(1,3,9,6). Thus cubic inertia is exactly differing valuation parities.'),
('prop:B-RD47','independent re-proof','PASS: unique invariant residualC2 vector identifies the rational2-kernels. The equivariant construction T={P in E8:4P in C}, T/C=E1[4] transfers an8-isomorphism to the quotient4-isomorphism, with no finite-flat integral lifting asserted. Trivial quotient residual invokes fully rechecked B46; otherwise equality of both nontrivial quadratic fields preserves both Kummer parities, hence the cubic special character. Isogeny preserves the rational special Dieudonne representation. Combined with B44/B46, only residualC3 can remain at16.'),
('B46-EXACT-CERTIFICATE','computation or formal certificate',f"PASS: entire program read and author-preserving rerun {outputs[0]['elapsed_seconds']}s. Exact polynomial halving/translation identities, all6 GL2(F2) conjugators,2 centralizers,32 upper-right-entry cases,8 scalar exclusions and4 valuation rows checked. Universal proofs were independently checked; no curve enumeration represented."),
('B47-EXACT-CERTIFICATE','computation or formal certificate',f"PASS: entire program read and author-preserving rerun {outputs[1]['elapsed_seconds']}s. Exact2-isogeny and differential, invariants and both torsion-field discriminants, all4 symbolic branches and181 sample excluded-square valuation cases checked. The branch exhaustion and finite-group-scheme quotient were separately rederived; no residualC3 comparison evaluated.")]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for sid,kind,result in events:writer.writerow([sid,now,who,kind,result])
with (w/'notes/ROOT_SEARCH_LOG_16.md').open('a') as f:
    f.write(f'''\n## {now}: B46 and B47 residual dyadic exclusions\n\nRoot fully read and independently rederived all four assertions and both exact programs. The Kummer representation, differential scaling, all valuation branches, and the8-to4 quotient construction passed. Author-preserving exact reruns took {outputs[0]['elapsed_seconds']}s and {outputs[1]['elapsed_seconds']}s. The proof uses the prior fully audited finite quaternionic inertia/elliptic realization and re-proves all Legendre and quotient identities; no new source theorem is imported. The general field scope was requested explicitly in both proposition statements. B46 and B47 narrow the open16-torsion gate to common residualC3 only, conditional on their independent companion audits and promotion. The least index remains undecided.\n''')
summary={'status':'PASS','actual_utc':now,'events':len(events),'reruns':outputs,'remaining_residual_gate':'C3 only after companion audits and promotion'}
(w/'outputs/root_b46_b47_audit.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
