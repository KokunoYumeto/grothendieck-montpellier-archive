"""Full original-source audit of the final dyadic branch and exact rerun."""
from pathlib import Path
from contextlib import redirect_stdout
import csv,datetime,io,json
w=Path(__file__).resolve().parents[1]
program=w/'agents/reduction_descent/code/verify_p2_residual_c3_gate.py'
author=program.with_suffix('.output.json')
dest=w/'outputs/root_verify_p2_residual_c3_gate.json'
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
    (w/'outputs/root_verify_p2_residual_c3_gate.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes()==before
out=json.loads(dest.read_text());assert out['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
('lem:B-RD48-models','independent re-proof','PASS: entire proof and exact program read. Root opened Chen arXiv1405.6385v3 original and read Theorems1.1-1.4 pp2-3, all Sections2-6 pp3-16 including Cor3.4, Lemmas5.1-5.5/6.1-6.3 and their actual finite-group cocycle proofs, and Appendix p21. Coefficient comparison gives q with minus linear sign and scalings1,D,D/gamma,gamma; inverse versus product changes only a square. The opposite sign printed in Lemma3.2 is expressly not imported. The universal Appendix discriminant identity uses exactly the same t. Root additionally opened Fisher original via cached author PDF and arXiv math/0610403v2, reading Lemma8.4 pp19-20, eq8.1/Remark8.6, and complete Theorem13.2 pp29-30 plus pp30-31 scope discussion/reverse4 twist. The Hesse family is exhaustive over arbitrary characteristic0 K including j0/1728; its basis matrix has determinant6T nonzero on smooth elliptic curves. Full4 marking has no nonidentity stabilizer. All finite-group cocycles restrict to any G_K, so the actual marked8 necessity, not an unmarked j-family, is used.'),
('prop:B-RD48','independent re-proof','PASS: full local argument rederived. After unramified completion, residue is algebraically closed, units are cubes and the residualC3 field is the unique tame cubic F=K(alpha),alpha³=2. Every trace-zero root is a alpha+b alpha², yielding A=-6ab,B=-2a³-4b³ and Delta=-1728(a³-2b³)². No cubic special inertia forces the first valuation to dominate; a common twist gives u=b/a integral and theta=alpha+u alpha². Scaling valuations are0,6,4,2. The q-term valuations6k,4+3k,5,3+3v(u) have the stated unique minimum: if k>=1 or t0 it is odd3or5, excluding every8 multiplier; if k<=0, norm valuation6k makes discriminant6+24k divisible3. Infinity and reversed discriminant twists preserve the character. The possibilities a0,b0,u0,t0 and negative k have all been checked symbolically.'),
('thm:B-RD48','independent re-proof','PASS: residual images1,C2,C3 exhaust height-two supersingular elliptic comparisons after unramified completion. B46/B47 and the fully audited C3 exclusion prove eight-torsion suffices within that subclass. B44 reduces every allowed height-two sixteen-torsion comparison to it. The actual B43 e1 eight-torsion counterexample gives the strict lower bound. With M(nu)=ker2^(nu+1), the exact least index is3. No claim for larger height or ramification follows.'),
('B48-EXACT-CERTIFICATE','computation or formal certificate',f"PASS: full program read and author-preserving rerun {out['elapsed_seconds']}s. All8 universal polynomial identities, the resultant norm and full Appendix discriminant, power3/7 scaling identities, trace-zero normal form and20301 valuation plus3721 normalization cases checked. Necessity/exhaustiveness is justified by the separately audited original marked-moduli proof; no finite curve sample substitutes for it.")]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for sid,kind,result in events:writer.writerow([sid,now,who,kind,result])
with (w/'notes/ROOT_SEARCH_LOG_16.md').open('a') as f:
    f.write(f'''\n## {now}: final dyadic residualC3 audit\n\nRoot fully rederived the three B48 assertions and read the entire exact certificate; the author-preserving rerun passed in {out['elapsed_seconds']}s. Chen original https://arxiv.org/pdf/1405.6385 (v3,2014) was opened and Theorems1.1-1.4, Sections2-6, Cor3.4, all cocycle/scaling proofs and Appendix actually read. The source's Lemma3.2 cusp-sum sign disagrees with its main models; the proof consistently uses the main-model sign, verified against the universal discriminant. To check the universal field scope and special j-values, root searched Fisher's Hessian paper, opened https://arxiv.org/pdf/math/0610403 and the cached original https://www.dpmms.cam.ac.uk/~taf1000/papers/g1hessians.pdf after a direct-URL timeout, and read Lemma8.4/eq8.1/Remark8.6 pp19-20, Theorem13.2 with proof pp29-30 and the exact pp30-31 j0/1728 and reverse4 discussions. The marked-moduli argument applies to arbitrary characteristic-zero fields and no alternate-coordinate exception was imported. Root full PASS gives nu_min(2,1,2)=3 once the companion audit passes and the candidate is promoted. The general B4 least-index question remains open.\n''')
summary={'status':'PASS','actual_utc':now,'elapsed_seconds':out['elapsed_seconds'],'events':len(events),'proved_after_companion_promotion':'nu_min(2,1,2)=3','source_sign_discrepancy_recorded':True}
(w/'outputs/root_b48_audit.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
