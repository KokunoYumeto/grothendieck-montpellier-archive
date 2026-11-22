"""Uniform mixed thin-system proof audit and preserved symbolic rerun."""
from pathlib import Path
from contextlib import redirect_stdout
import csv,datetime,io,json
w=Path(__file__).resolve().parents[1]
program=w/'agents/obstructions_crystals/code/mixed_thin_residue_checks.py'
author=program.with_suffix('.output.json')
dest=w/'outputs/root_mixed_thin_residue_checks.json'
assert not dest.exists()
before=author.read_bytes();old_write=Path.write_text;old_exists=Path.exists;capture=io.StringIO()
def write(path,data,*args,**kwargs):
    assert path.resolve()==author.resolve()
    return old_write(dest,data,*args,**kwargs)
def exists(path):
    return False if path.resolve()==author.resolve() else old_exists(path)
try:
    Path.write_text=write;Path.exists=exists
    with redirect_stdout(capture):
        exec(compile(program.read_text(),str(program),'exec'),{'__name__':'__main__','__file__':str(program)})
finally:
    Path.write_text=old_write;Path.exists=old_exists
    (w/'outputs/root_mixed_thin_residue_checks.stdout.txt').write_text(capture.getvalue())
assert author.read_bytes()==before
out=json.loads(dest.read_text());assert out['status']=='PASS' and out['identity_count']==13
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
('lem:DE-A3-ordinary-two-pencils','independent re-proof','PASS: full proof rederived. Cartier on an ordinary invariant differential gives a normalized O-linear retraction tau(1)=1; local2-basis duality makes tau(uv) perfect. Its orthogonal line B has square in O, perfect pairing forces B²=O, and H0(F_*O)=k forces nontrivial degree0 B and H0B=H1B=0. Reduced disjoint divisors exist for degreeq>=3. The exact middle sequence has kernel B; both evaluation kernels are B, so all three displayed maps are isomorphisms. Illusie1979 original retained text at0, Theorem2.1.9 and local formulas2.1.12-13 p515 freshly read; oversized web fetch was not represented as a successful PDF fetch.'),
('lem:DE-A3-mixed-residue-determinant','independent re-proof','PASS: complete proof, every equation and symbolic code rederived. The supersingular pairing gives the three displayed equations; the middle map is an isomorphism and the two pencil maps have1-dimensional kernels/cokernels. Q is the bijective Frobenius-semilinear square-descent map, Q(a,b)=a²+mu b². The correct stability test is Q(kerT)->cokerT, giving matrix[t,u;v,t]. Root checked all regular residue remainders and both diagonal entries via global residues. The shift b1+lambda b2 fixes t and v and has u linear coefficient c1. Evaluation on A makes c1 a nonzero quadratic polynomial for every allowed a1; evaluation on D makes v a nonzero cubic polynomial for every allowed b1. These nonempty opens intersect in the irreducible pair space. Therefore det=t²+uv is nonzero for some shift, so image and kernel of Q^-1 T meet trivially and first rank6q-2 is stable. Tate1968 original Theorems2/3+cor pp155-156 and Section4 Theorem5+cor pp157-159 actually read, including complete residue-duality argument.'),
('thm:DE-A3-mixed-thin-all','independent re-proof','PASS: full proof checked with the entire prior even ordinary-factor upper bound and divisor-sequence argument reread. Nonzero stable-rank minor gives an open meeting the very-ample Bertini smooth open; no smoothness is claimed for the constructed algebraic witness. For every evenm>=6, genus3m+1, full rank3m-1 and relative rank3m-2 follow. Mixed ambient H2 has Frobenius zero and ambient H1 stable rank1; Serre duality identifies the computed Cartier stable rank with the relative Frobenius stable rank.'),
('cor:DE-A3-mixed-product-no-exception','independent re-proof','PASS: all previous degree cases and the remaining d=b=1,a even case checked. Substitution m=3a in the uniform thin-system theorem gives every positivea,b,d over every perfect characteristic2 field after geometric base change. Formula r=9abd²-1-epsilon(ad), coherent dimension9abd²-1. This closes all mixed elliptic product ranks and does not claim arbitrary nonproduct or arbitrary-X ranks.'),
('rem:DE-A3-mixed-thin-residue-checks','computation or formal certificate',f"PASS: full program read, exact13 universal identities rerun in {out['elapsed_seconds']}s, author output unchanged. The original output-existence guard and write were redirected only for the isolated rerun. Both kernel vectors, middle exact-sequence relation, residue remainders, cubic variation, and determinant coefficient v*c1 verified. No finite elliptic curves sampled; global existence proof independently audited.")]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for sid,kind,result in events:writer.writerow([sid,now,who,kind,result])
with (w/'notes/ROOT_SEARCH_LOG_16.md').open('a') as f:
    f.write(f'''\n## {now}: all mixed thin-product ranks by residues\n\nRoot fully read and independently rederived all four mathematical assertions and the verification remark of A3_mixed_thin_strip_residues.tex. Particular checks were the precise Frobenius-semilinear mapQ, the middle-equation isomorphism, all Cech residue substitutions, and independence of the two evaluation arguments giving nonzero c1 and v. The full prior mixed-even upper bound and divisor sequence were reread. The author-preserving symbolic rerun passed13 identities in {out['elapsed_seconds']}s. Tate1968, Residues of differentials on curves, original https://www.numdam.org/item/10.24033/asens.1162.pdf was opened; Theorems2/3+cor pp155-156 and Section4 Theorem5+cor pp157-159 were actually read. Illusie1979 original0, Theorem2.1.9 and local formulas2.1.12-13 p515 were freshly read from the retained original text after the web PDF fetch exceeded the size limit. RD's separate full proof/source/code audit also passed. This closes every mixed elliptic product rank, uniformly in the ordinary modulus, including4|a,b=d=1. General nonproduct mixed ranks and arbitrary-X structural ranks remain open.\n''')
summary={'status':'PASS','actual_utc':now,'events':len(events),'elapsed_seconds':out['elapsed_seconds'],'identities':out['identity_count'],'finite_curves_tested':0,'closed_gate':'All mixed elliptic product ranks, every degree and ordinary modulus'}
(w/'outputs/root_mixed_thin_residue_audit.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
