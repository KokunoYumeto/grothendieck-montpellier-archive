"""Normalize the audit ledger's categories while retaining original detail labels."""
from pathlib import Path
from collections import Counter
import csv

HERE=Path(__file__).resolve().parent
VALID={
    'targeted proof check','independent re-proof','computation or formal certificate',
    'used and rechecked in this run','carried as background without fault found',
    "refuted, with the refined statement's id",
}
SOURCE={
    'source statement check','primary source statement and full relevant proof read',
    'complete relevant source proof reread','primary theorem statement used and checked',
    'independent primary edge-case comparison','primary theorem and algorithm proof review',
    'complete primary propagation proof and scalar audit',
}
COMPUTATION={
    'independent character check','independent exact matrix entry check',
    'independent source-vector and modulus check','independent source-character check',
    'independent complete certificate recheck','independent finite coefficient check',
    'independent finite character check','independent finite support check',
    'independent exact finite character check','independent complete source-character comparison',
    'independent complete matrix-entry check','independent complete source characters',
    'independent exact matrix-entry check','independent complete numerical certificate check',
    'independent finite character checks','independent finite plethysm verification',
    'independent exact finite coefficient checks','independent complete low-degree plethysm verification',
    'independent finite arithmetic boundary check','independent actual plethysm computation',
    'independent exact matrices and fixed character table',
    'independent full finite-data and rational-extension audit',
    'independent literal determinant/cofactor coefficient audit',
    'independent full fixed rational and tensor-table audit',
    'independent literal integer cofactor coefficient audit',
}
PROOF={
    'new reformulation','new finite computational theorem','independent complete proof review',
    'known construction with exact normalization','proved corollary of known inequality and T025',
    'independent targeted morphism review','three finite exact kernel theorems',
    'exact kernel reformulation','complete proof and exact morphism check',
    'cutoff and source notation follow-up','complete proof and exact scalar check',
    'complete proof and exact preimage check','complete proof and exact annihilator morphism check',
    'complete exact prolongation proof check','exact support-envelope arithmetic proof',
    'parent-review typography repair','complete proof and exact intermediate-annihilator morphism check',
    'exact square-kernel endpoint proof','complete triangular-profile proof',
    'independent complete application proof and primary-source audit',
    'complete proof and exact normalization check','complete exact-morphism proof',
    'exact apolar endpoint proof and independent coefficient audit',
}


def main():
    path=HERE/'CHECK_EVENTS.tsv'
    with path.open() as inp:
        reader=csv.DictReader(inp,delimiter='\t');fields=reader.fieldnames;old=list(reader)
    if 'detail_type' in fields:
        assert all(row['type'] in VALID for row in old)
        print('already normalized',len(old),'events',dict(Counter(r['type'] for r in old)))
        return
    out=[]
    for source in old:
        row=dict(source);detail=row['type'];row['detail_type']=detail
        if detail in VALID:pass
        elif detail in SOURCE:row['type']='used and rechecked in this run'
        elif detail in COMPUTATION:row['type']='computation or formal certificate'
        elif detail in PROOF:row['type']='targeted proof check'
        else:raise AssertionError(('unclassified actual check label',detail))

        if row['statement_id']=='T-038' and detail=='independent complete proof review':
            before,after=row['how'].split(' Independent exact symbolic audit ',1)
            row['how']=before;row['source']='work/theta/outer5/five_point_resolution_report.md'
            out.append(row)
            extra=dict(row,type='computation or formal certificate',
                detail_type=detail+'; executed symbolic matrix audit',
                outcome='passed literal matrix identities and120 signed actions',
                how='Executed an independent exact symbolic audit that '+after,
                source='verify_five_point_matrices.py; FIVE_POINT_MATRIX_INDEPENDENT_CHECK.txt')
            out.append(extra);continue

        if row['statement_id']=='A-029' and detail=='independent complete application proof and primary-source audit':
            row['how']='Read complete application proof. Verified height3 Gorenstein/local generator hypotheses, exceptional q3 shift4, degree0 torsion, Tor passage to linear powers, saturation and H1 ranges. Older1992 complexes are used as attributed established input.'
            row['source']='work/archive/FIVE_POINT_POWERS.md'
            out.append(row)
            extra=dict(row,type='used and rechecked in this run',
                detail_type=detail+'; primary-source reading',
                how='Opened the publisher Kustin-Polini-Ulrich PDF and read formula(6.1.4), Lemma6.3, Corollary6.4 and their surrounding proofs on printedpp1509-1511. Checked their precise application to the actual ideal; older1992 complex construction retained as attributed input.',
                source='https://msp.org/ant/2017/11-7/ant-v11-n7-p01-p.pdf')
            out.append(extra);continue

        if row['statement_id']=='R-026' and detail=='exact apolar endpoint proof and independent coefficient audit':
            first,after=row['how'].split(' Independently expanded ',1)
            row['how']=first;row['source']='canonical_below_square_families.md BS24-BS31'
            row['outcome']='passed exact coefficient and apolar proof review'
            out.append(row)
            extra=dict(row,type='computation or formal certificate',
                detail_type=detail+'; executed exact coefficient calculations',
                outcome='passed5 expanded binary identities and2 finite-field matrix checks',
                how='Independently expanded '+after,
                source='verify_apolar_endpoint.py; APOLAR_ENDPOINT_BINARY_CHECK.txt; APOLAR_ENDPOINT_LITERAL_CHECK.tsv')
            out.append(extra);continue

        if row['statement_id']=='R-022' and detail=='complete proof and exact annihilator morphism check':
            row['how']=row['how'].removeprefix('Re-read full Sra§2.2 and Lemma2.1. ')
            out.append(row)
            extra=dict(row,statement_id='SRA-1.3-2.1',type='used and rechecked in this run',
                detail_type=detail+'; primary-source proof rereading',outcome='passed precise source range and lemma check',
                how='Re-read all of Sra section2.2 and Lemma2.1, checking the actual canonical lower map and the full stated range B>=(r-1)^2 used in the annihilator proof.',
                source='work/external/sra_qfoulkes3-v1.txt; https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1.pdf')
            out.append(extra);continue

        if detail=='parent-review typography repair':
            row['how']='Checked the two corrected displays against the intended formulas: K2 has its proper left delimiter; the split binary form before K17 reads (x^r+c t^r)Q. These are textual corrections with no mathematical change.'
        out.append(row)
    fields=['statement_id','date','who','type','detail_type','outcome','how','source']
    assert all(row['type'] in VALID for row in out)
    with path.open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields,delimiter='\t')
        writer.writeheader();writer.writerows(out)
    print('normalized',len(old),'original events into',len(out),'separate events')
    print(dict(Counter(row['type'] for row in out)))


if __name__=='__main__':main()
