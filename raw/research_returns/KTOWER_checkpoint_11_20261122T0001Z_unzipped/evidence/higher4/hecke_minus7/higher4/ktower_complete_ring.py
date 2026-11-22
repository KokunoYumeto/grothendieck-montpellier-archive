"""Full model verification; exact native row elimination for the two determinants.

All frame reconstruction, complete kernel verification, input agreement, and
every identifying evaluation are the fully read archived independent verifier.
The determinant is evaluated by our GMP implementation with certified unit
pivots; no field or primality assumption is made. If an archived producer
result exists, every determinant is compared with it. Otherwise this is a new
complete computation, not an independently reproduced numerical result.
"""
from pathlib import Path
import subprocess, sys, json

HERE=Path(__file__).resolve().parent
source=(HERE/'verify_ring_schur_parallel.py').read_text()
source=source.replace('Independent, standard-library replay of the complete minus-seven U3 test.',
    'Complete exact minus-seven U3 test with native determinant evaluation.')
source=source.replace('No C++ code or\nprepared row-reduction routines are imported.',
    'Only the two determinants use the included GMP C++ implementation;\nall frame, kernel, and identifying-row calculations use Python integers.')
start=source.index('def determinant(matrix):')
end=source.index('\n\ndet_a=determinant(evaluations)',start)
replacement='''def determinant(matrix):
    import subprocess
    native=HERE.parent.parent/'ring_determinant'
    n=len(matrix)
    payload=str(Q)+' '+str(n)+chr(10)+''.join(
        str(a)+' '+str(b)+chr(10) for row in matrix for a,b in row)
    proc=subprocess.run([str(native)],input=payload,text=True,capture_output=True,check=True)
    a,b,pivots=map(int,proc.stdout.split())
    assert pivots==max(0,n-1)
    assert 0<=a<Q and 0<=b<Q
    return a,b
'''
source=source[:start]+replacement+source[end:]
start=source.index("result = json.loads((CASE / 'schur.json').read_text())")
end=source.index('\nreport={',start)
replacement='''common=gcd(norm(det_o),Q)
assert common==1
producer=CASE/'schur.json'
matched=False
if producer.exists():
    result=json.loads(producer.read_text())
    assert result['modulus']==Q and result['k']==K
    assert result['comparison_point']==E and result['dimension']==d
    assert det_a==tuple(result['det_evaluation'])
    assert det_s==tuple(result['det_schur_evaluations'])
    assert det_o==tuple(result['det_schur_operator'])
    assert result['gcd_norm_determinant_modulus']==1
    matched=True
'''
source=source[:start]+replacement+source[end:]
source=source.replace("'PASS: full independent exact quadratic-algebra unit certificate'",
    "'PASS: complete exact quadratic-algebra unit certificate'")
source=source.replace("'parallel_row_workers':workers,",
    "'parallel_row_workers':workers,'archived_producer_matched':matched,'determinant_method':'GMP row elimination with unit norms','native_source_sha256':sha256((HERE.parent.parent/'ring_determinant.cpp').read_bytes()).hexdigest(),'native_executable_sha256':sha256((HERE.parent.parent/'ring_determinant').read_bytes()).hexdigest(),")
source=source.replace("for name in ['model.json','model.txt','schur.json']",
    "for name in ['model.json','model.txt']+(['schur.json'] if matched else [])")
source=source.replace("CASE/'verify_ring_schur_parallel.json'","CASE/'ktower_complete_ring.json'")
generated=HERE/f'ktower_ring_verifier_{Path(sys.argv[1]).name}.py'
generated.write_text(source)
subprocess.run([sys.executable,str(generated),*sys.argv[1:]],check=True)
