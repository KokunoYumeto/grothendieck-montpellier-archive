"""Retain only selected explicit vectors, evaluation points and square minors."""
from pathlib import Path
import sys

def compact(stem):
    path=Path(stem)
    lines=iter(Path(str(path)+'_CERTIFICATES.txt').read_text().splitlines())
    assert next(lines)=='prime 1000003';next(lines)
    points={};blocks={}
    for line in lines:
        z=line.split()
        if z[0]=='point':points[int(z[1])]=list(map(int,z[2:]))
        elif z[0]=='partition':
            lam=tuple(map(int,z[1].split(',')));m=int(z[3]);rank=int(z[5])
            assert m==rank
            chosen=list(map(int,next(lines).split()[1:]));rows=list(map(int,next(lines).split()[1:]))
            matrix=[list(map(int,next(lines).split())) for _ in range(m)]
            d=int(next(lines).split()[1]);assert d
            blocks[lam]=(m,chosen,rows,matrix,d)
    outfile=Path(str(path)+'.compact')
    with Path(str(path)+'.input').open() as src,outfile.open('w') as out:
        L,b,n=map(int,next(src).split());assert n==len(blocks)
        print(L,b,n,1000003,len(points),file=out)
        for i in range(len(points)):print(*points[i],file=out)
        for _ in range(n):
            head=list(map(int,next(src).split()));lam=tuple(head[:4]);m,ncand=head[4:]
            bm,chosen,rows,matrix,d=blocks[lam];assert bm==m
            keep={}
            for ci in range(ncand):
                nt=int(next(src));terms=[next(src).strip() for _ in range(nt)]
                if ci in chosen:keep[ci]=terms
            print(*lam,m,file=out)
            for ci in chosen:
                print(ci,len(keep[ci]),file=out)
                for term in keep[ci]:print(term,file=out)
            print(*rows,file=out)
            for row in matrix:print(*row,file=out)
            print(d,file=out)
    print(outfile,'bytes',outfile.stat().st_size)

if __name__=='__main__':
    for stem in sys.argv[1:]:compact(stem)
