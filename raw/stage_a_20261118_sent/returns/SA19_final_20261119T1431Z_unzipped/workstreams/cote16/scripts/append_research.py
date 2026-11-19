"""Append actual later searches and primary reads to the existing research ledger."""
import csv
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rows=[
('CL-SA19-222','arXiv;Algebraic Geometry journal;backward Lipman/Saito bibliography','Suzuki2210.01396;2024Propositions11.2,11.10;Theorem1.6','Exact p-primary pairing comparison found for mixed-characteristic complete normal dimension2 rings with perfect residue field; no unproved equal-characteristic transfer','Primary PDF introduction,§11.2 and full11.10proof pp500–501 read; first arXiv4October2022,publication2024'),
('CL-SA19-204;CL-SA19-243;CL-SA19-247;CL-SA19-284','Katz author bibliography;Princeton primary PDF;backward Deligne lecture citation','KatzMessing1974Theorems1,2;Corollary1;D3;reference1','Finite-field cycle/correspondence theorem exactly identified. Deligne hard Lefschetz documented by Cambridge4–11July1973 and submission8August1973, not first1980','All printed73–77 OCR-read; pp76–77 visually checked; download/OCR scripts and outputs saved'),
('CL-SA19-257–261','MSP;Gabriel Numdam/Edinburgh;Hartshorne Springer/GDZ;Murfet author notes;EMS journal;MathOverflow leads','HartshorneII7.5–7.6,7.9,7.14,7.16–7.18;GabrielIV2Theorem2,VI2Theorem1;Murfet67–68;LuntsSchnuerer2.1','Exact original locally-noetherian sheaf theorem and proof found. QCoh category convention in Gabriel kept separate. Exact detached prepublication typescript still not attributed','Hartshorne original1966scan downloaded, printed120–136 read; main theorem/proof pages rendered. Gabriel downloaded text read. Modern pointers read before following originals'),
('CL-SA19-269–270','Stacks;MIT author teaching notes;Stanford local-field notes search','Totally tamely ramified uniformizer;Sutherland2021Lecture11Theorem11.10','Exact complete-DVR finite total-tame statement and Hensel proof found. No Galois/canonical-generator conclusion without roots of unity','Primary MIT notes Theorem11.10 pp3 and proof read'),
('CL-SA19-271;CL-SA19-277–278','Stacks official reference','033C;025L41.19.5,41.19.7;04HN41.18.3;0BL6;00U0','Normal/reduced ascent and finite-étale local splitting verified with exact hypotheses. Connectedness is constant-rank qualification','Statements and indicated proofs opened/read'),
('CL-SA19-282–283','Kleiman primary;Picard/Albanese appendix;modern standard-conjecture author paper','Kleiman2A9(5)–(6),2A10;2.13;letter low-dimensional dictionary','Degree-one inverse and outer projector claims retain ℓ-adic H¹ comparison. Char0 cycle A in dim≤4 distinguished from inverse-correspondence B','Primary2A9proof and2A10read; exact source letter re-read'),
('CL-SA19-227','Exact four-form reconstruction and earlier source search','Q from C=[[0,1,2],[1,0,3],[2,3,0]],xi=(1,1,−1/5)','Counterexample to automatic norm-one rescaling satisfies nondegenerate Q and nondegenerate alternating phi, with Q(xi,xi)=0','Own exact15×15 certificate and checked rational determinants saved; no literature novelty claimed'),
('CL-SA19-258','MathOverflow;arXiv search correction','Accidental arXiv1601.00944 opening','Unrelated subtree paper; excluded from every claim and bibliography','No mathematical result used'),
]
path=root/'research_log.tsv'
with path.open(newline='') as f:old=list(csv.reader(f,delimiter='\t'))
existing={tuple(x) for x in old[1:]}
with path.open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for row in rows:
        line=('2026-11-19',)+row
        if line not in existing:writer.writerow(line)
print(f'Added up to {len(rows)} later actual research events; duplicate-safe.')
