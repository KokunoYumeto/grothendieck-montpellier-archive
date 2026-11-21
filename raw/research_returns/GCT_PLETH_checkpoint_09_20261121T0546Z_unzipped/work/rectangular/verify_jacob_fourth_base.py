"""Recheck Jacob's published Table 4.4; no orbital enumeration is claimed.

Source: https://publications.rwth-aachen.de/record/51990/files/Jacob_Juby.pdf
Juby Jacob, Representation Theory of Association Schemes (2004),
section 4.2, printed p.99 and Table 4.4, printed pp.104--106.
The three column blocks were extracted from the primary PDF text. The
page-header joins after the final entries 64 and 48 were removed.
"""
from pathlib import Path
from hashlib import sha256

HERE=Path(__file__).resolve().parent


def bareiss(matrix):
    a=[row[:] for row in matrix]; n=len(a); old=1; sg=1
    for k in range(n-1):
        j=next(j for j in range(k,n) if a[j][k])
        if j!=k:
            a[j],a[k]=a[k],a[j]
            sg=-sg
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=pivot*a[i][j]-a[i][k]*a[k][j]
                assert numerator%old==0
                a[i][j]=numerator//old
            a[i][k]=0
        old=pivot
    return sg*a[-1][-1]


def modular_det(matrix,p):
    a=[[x%p for x in row] for row in matrix]; value=1
    for k in range(len(a)):
        pivot=next(j for j in range(k,len(a)) if a[j][k])
        if pivot!=k:
            a[k],a[pivot]=a[pivot],a[k]
            value=-value
        v=a[k][k];value=value*v%p;vi=pow(v,-1,p)
        for i in range(k+1,len(a)):
            c=a[i][k]*vi%p
            for j in range(k+1,len(a)):
                a[i][j]=(a[i][j]-c*a[k][j])%p
    return value%p


def main():
    path=HERE/'JACOB_2004_TABLE_4_4.tsv'
    data=path.read_bytes()
    a=[list(map(int,line.split())) for line in data.decode().splitlines()]
    assert len(a)==43 and all(len(row)==43 for row in a)
    value=bareiss(a)
    assert value==2**223*3**67
    lines=['PASS 43x43 published matrix determinant = 2^223 * 3^67',
           'Matrix SHA256: '+sha256(data).hexdigest(),
           'All Bareiss divisions exact; original orbital enumeration was not rerun.']
    for p in (101,1009,10007):
        residue=modular_det(a,p)
        assert residue==value%p
        lines.append(f'PASS separate Gaussian determinant modulo {p}: {residue}')
    (HERE/'JACOB_FOURTH_BASE_DETERMINANT_CHECK.txt').write_text('\n'.join(lines)+'\n')
    print('\n'.join(lines))


if __name__=='__main__':main()
