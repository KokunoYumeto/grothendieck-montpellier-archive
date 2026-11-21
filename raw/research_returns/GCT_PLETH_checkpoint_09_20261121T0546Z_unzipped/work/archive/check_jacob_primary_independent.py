"""Independent primary-table reconstruction and rational determinant check."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
HERE=Path(__file__).resolve().parent
p=HERE/"JACOB_TABLE_PRIMARY_RECONSTRUCTION.tsv"
a=[list(map(int,line.split())) for line in p.read_text().splitlines() if line.strip()]
b=[list(map(int,line.split())) for line in (HERE.parent/"rectangular/JACOB_2004_TABLE_4_4.tsv").read_text().splitlines()]
assert len(a)==43 and all(len(row)==43 for row in a)
assert a==b
matrix=[[Fraction(x) for x in row] for row in a]
value=Fraction(1)
swaps=0
for j in range(43):
    pivot=next(i for i in range(j,43) if matrix[i][j])
    if pivot!=j:
        matrix[j],matrix[pivot]=matrix[pivot],matrix[j]
        value=-value;swaps+=1
    diagonal=matrix[j][j]
    value*=diagonal
    matrix[j]=[x/diagonal for x in matrix[j]]
    for i in range(j+1,43):
        t=matrix[i][j]
        if t:
            matrix[i]=[x-t*y for x,y in zip(matrix[i],matrix[j])]
assert value.denominator==1
assert value==2**223*3**67
receipt=dict(statement="R031 primary fourth-square matrix",status="PASS",
 primary_url="https://publications.rwth-aachen.de/record/51990/files/Jacob_Juby.pdf",
 primary_locators="Definition1.1.11p9; Definition4.1.1p92; section4.2p99; Table4.4pp104-106",
 rows=43,entries_reconstructed_from_primary_web_pdf_text=1849,
 comparison_to_rectangular_transcription="all1849equal",
 determinant=str(value.numerator),determinant_factorization="2^223*3^67",
 independent_algorithm="ordinary rational Gaussian elimination with Fraction arithmetic",
 row_swaps=swaps,table_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
 scope="No original2,627,625-point orbital enumeration rerun; direct local PDF download gave HTML challenge; primary text was retrieved by web tool.")
(HERE/"JACOB_PRIMARY_INDEPENDENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt,indent=2))
