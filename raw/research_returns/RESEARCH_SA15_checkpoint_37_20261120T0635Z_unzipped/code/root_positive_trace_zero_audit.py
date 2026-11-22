"""Full geometric trace-zero audit and preserved local symbolic certificate."""
from pathlib import Path
import json,csv,datetime,hashlib,io,contextlib
w=Path(__file__).resolve().parents[1]
source=w/'agents/obstructions_crystals/code/post_CP20_trace_zero_factorization.py'
author=source.with_suffix('.output.json')
before=hashlib.sha256(author.read_bytes()).hexdigest()
program=source.read_text();needle="Path(__file__).with_suffix('.output.json').write_text"
assert program.count(needle)==1
target=w/'outputs/root_positive_trace_zero_factorization.json';assert not target.exists()
executed=program.replace(needle,'Path('+repr(str(target))+').write_text')
snapshot=w/'code/audit_snapshots/post_CP20_trace_zero_factorization_at_root_audit.py'
assert not snapshot.exists();snapshot.write_text(executed)
stream=io.StringIO()
with contextlib.redirect_stdout(stream):
    exec(compile(executed,str(snapshot),'exec'),{'__file__':str(source),'__name__':'__main__'})
(w/'outputs/root_positive_trace_zero_factorization_stdout.txt').write_text(stream.getvalue())
assert before==hashlib.sha256(author.read_bytes()).hexdigest()
run=json.loads(target.read_text());assert run['status']=='PASS'
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checks={
'lem:DE-A3-positive-acyclic-alternating-candidate': 'Entire geometric proof independently rederived after full fresh rereads of the earlier rank-two bundle, determinant-curve and norm-pencil proofs. End(V)P andP are acyclic. The locally surjective trace sequence and the scalar subbundle in trace-zero endomorphisms give an acyclic rank2 quotientG=(End^0(V)/O)P. Its descended trace form is perfect alternating. The map phi->(phi s1,phi s0) lies in the contraction kernel by the rank2 trace identity and takes scalars to the specifiedP subbundle, hence descends to f:G->Q. In the actual nonsquare-unit chart, a=[[1,u h²],[0,w]], f=diag(uw,1), and the G pairing is uJ, whose inverse is u^-1J. Thus aJ a^t=f(u^-1J)f^t=wJ exactly. Both are intrinsic bundle maps, so equality extends from the dense chart. The induced H1 map vanishes because it factors through acyclicG; no unjustified square root ofu is used.',
'prop:DE-A3-positive-cup-trace-zero-candidate': 'Entire proof and the actual Cech comparison independently rederived. Dualizing the surface two-section sequence gives0->Q^vee->O²->i_*A->0, with the squared pencil row up to the J-preserving interchange. At a sharp source beta cup is invertible. The kernel S of the ensuing H1 cup map is the graph alpha tensorv + beta tensorT_sv. Naturality of Serre duality identifies its tensor cup/J pairing with H1(aJ a^vee), zero by the acyclic factorization. Alpha andbeta are independent because Frobenius fixes the nonzero connected etale torsor class and kills the nonzero alpha2 torsor class; the latter cannot be zero over an algebraically closed base without making the torsor nonsmooth/trivial. Exterior-algebra cup on the abelian surface gives alpha cupbeta nonzero. Graph isotropy is JT_s+T_s^tJ=tr(T_s)J=0. For each trace lift q_i=z_j s_i+r_ij, the Cech transition of the associated G_s lift is c_jk a_i, yielding alpha cupa_i; the norm-section boundary is beta cupa_i. Thus the actual projection matrixA(u) is this cup ratio with the stated Frobenius transports. Its trace is zero, and the already audited derivative identity gives trace-zero Cartier-dual and coherent variations, with the coherent coefficient-square transpose retained.',
'cor:DE-A3-positive-tracezero-matrix-line-candidate': 'Entire algebraic proof independently rederived. A nonzero traceless singular2x2matrix is rank1 nilpotent. Conjugate it toE12. For another tracelessB=[[a,b],[c,a]], det(E12+tB)=tc+t²(a²+bc). Its identically vanishing polynomial forcesc=0 thena=0 over the stated field, soB is a multiple ofE12. Therefore an everywhere-singular variation space is zero or a single nilpotent line. Image dimensionatleast2 is sufficient for nonvanishing but is not asserted; a one-dimensional invertible line would also suffice.',
'rem:DE-A3-positive-tracezero-scope-candidate': 'Entire retained symbolic/finite certificate read and isolated rerun preserved. It checks20 universal scalar identities, the exact uJ inverse factor, all15 nonzero traceless nilpotents overF4 and90 independent pairs with invertible sum. The geometric conclusion comes from the bundle/duality proof, not the finite sample. The remaining uniform gate is exclusion of zero or a single nilpotent variation line; no image-dimension lower bound or general sharpness theorem is claimed.'
}
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for label,detail in checks.items():writer.writerow([label,now,'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root','full mathematical/source/code audit','PASS. '+detail])
record={'status':'FULL MATHEMATICAL AND CODE PASS','actual_utc':now,'events':len(checks),
 'root_rerun_seconds':run['elapsed_seconds'],'author_output_sha256_unchanged':before,
 'candidate_sha256':hashlib.sha256((w/'agents/obstructions_crystals/post_CP20_positive_index_trace_zero_candidate.tex').read_bytes()).hexdigest(),
 'counts':{k:run[k] for k in ['universal_scalar_identities','F4_nonzero_nilpotents','F4_independent_nilpotent_pairs']},
 'source_scope':'Entire current proof, code, earlier bundle and full norm-pencil proofs actually read. Original Edixhoven/van der Geer/MoonenAV freshly opened online; Proposition7.27 and its proof p108, Theorem6.12 statement p93 and complete Corollary6.13 proof p94 read in the retained original text. No new full proof of cited Borel structure theorem is claimed.',
 'remaining_gate':'Exclude a zero variation space or one line of rank1 nilpotents at a suitable sharp source; trace-zero is proved, determinant nonvanishing is not.'}
dest=w/'outputs/root_positive_trace_zero_audit.json';assert not dest.exists()
dest.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
