"""Exact source locations for the Part A corrections and scope refinements."""
import csv
from pathlib import Path
root=Path(__file__).resolve().parents[1]
source=root.parent/'SA21_input'
prompt=root.parent/'upload'/'PROMPT(20261119-110210).md'
rows=[]
def add(key,file,lines,kind,correction,evidence):
 p=prompt if file=='upload/PROMPT(20261119-110210).md' else source/file
 text=p.read_text().splitlines()
 for part in lines.replace('-', ';').split(';'):
  if part.isdigit():assert 1<=int(part)<=len(text),(file,part)
 rows.append([key,file,lines,kind,correction,evidence])
def pline(needle):
 hits=[i for i,l in enumerate(prompt.read_text().splitlines(),1) if needle in l]
 assert len(hits)==1,(needle,hits)
 return str(hits[0])
tr='RESEARCH_SA21_transcriptions/transcriptions/156_Codex_web/'
st='RESEARCH_SA21_study/study/'
pf='upload/PROMPT(20261119-110210).md'
add('SA21-A-K01',tr+'J156-9-15_transcription.tex','106','Transcription correction','The second ordinary-powerset condition has i and i-prime both outside E, not j and i-prime.','Original scan156-9/113 formula visually inspected; A11.')
add('SA21-A-K02',tr+'J156-9-15_transcription.tex','48','Diagram correction','The heavy c-to-C construction stroke is not a cover of the announced ten-element ortholattice; retain exactly the fourteen cover edges reconstructed from its set model.','A11; Figure1; all100 lattice-operation pairs and1000 associativity triples checked.')
add('SA21-A-K03',tr+'J156-9-15_transcription.tex','104','Doubtful powerset notation, both readings','Ordinary powerset gives the stated ten-element ortholattice. Reading the apparent superscript3 as three-element subsets selects only three incomparable sets and is not a lattice.','A11; explicit alternate-reading calculation in check_supports.py.')
add('SA21-A-K04',tr+'J156-9-15_transcription.tex','37;114','Ambiguous vertex label','The lower-right handwritten label has an ambiguous extra stroke. The reconstructed vertex is labelled b={j}; changing the label does not change the model.','Original scan113 inspected; A11 set table.')
add('SA21-A-K05',pf,pline('**L2 (replaces'),'Lead refuted, exact replacement','Sumner normality is not equivalent to orthomodularity, even for comparability graphs. The eight-symbol positional crown is normal but has20nonorthomodular supports. The exact arbitrary-poset condition is the explicit maximal-chain neighbourhood test.','A03,A07,A08; Sumner1974 p492 and opened Jenča theorem3.3.')
add('SA21-A-K06',st+'HUNCHES.md','347-350;362','Dacey terminology corrected','Distinguish the modern Dacey basis property from Sumner1974 two-neighbourhood normality. The purported identification is false; induced-fence repair wording alone supplies no exact equivalent.','A03,A07,A08; complete eight-vertex comparability certificate.')
add('SA21-A-K07',st+'HUNCHES.md','312','Cograph equivalence refuted, sufficiency retained','Cographs have orthomodular support lattices, but the converse fails even with Boolean supports; a five-vertex comparability example has an induced four-vertex path and8supports.','A25; self-contained recursive product/horizontal-sum proof and finite certificate.')
add('SA21-A-K08',pf,pline('**L3.**'),'Lead refuted without separation, positive connected case','Nondisjoint distinct lieux can have Boolean supports. Exact general Booleanity uses the neighbourhood criterion; with singleton-separated lieux it is equivalent to all distinct lieux being disjoint. In connected interval magasins it is equivalent to totality of the underlying order.','A04,A06,A15; twin model and divisible Q disjoint-union isolated-point interval model.')
add('SA21-A-K09',st+'HUNCHES.md','288','Cords/strands inference qualified','The unqualified nondisjoint-lieu criterion fails, including a genuine divisible interval magasin on Q plus an isolated point. Its connected ordered-set interpretation is true by the nonisolated-core theorem.','A06,A15, complete proofs; all hypotheses of the infinite interval example checked directly.')
add('SA21-A-K10',st+'readings/156-9.md','54','Atomicity versus point separation','An atomic singleton-generated support need not distinguish its lieu from another lieu. The exact atom test is N(x) subset N(y) implies N(x)=N(y); the stronger point-separation test requires y=x.','A14,A14a,A15; two twins have the same atom.')
add('SA21-A-K11',st+'HUNCHES.md','67','Atom question qualified','The separation property is stronger than atomicity unless distinct lieu supports are separately required.','A14,A15.')
add('SA21-A-K12',st+'readings/156-9_rest_INTEGRATION.md','12;67;76','Finite versus infinite support axiom','Every finite interval prefigure satisfies the support axiom for every base poset. An unrestricted infinitary version is false; the Q-with-two-one-sided-cut-points example has an incidence-closed infinite figure with failed complement formula.','A09,A10; direct proof for every symbol type. The original finite computation is not extrapolated.')
add('SA21-A-K13',st+'readings/156-9_rest.md','45-47;169','Finite theorem and infinitary qualification','The flag proof extends to all finite prefigures by an explicit endpoint-completed flag comparison. It does not prove the law for arbitrary infinite figures.','A09,A10; original IDs SA21-R9b-06 and SA21-R9b-28 retained.')
add('SA21-A-K14',pf,pline('**R13 ('),'Prefigures distinguished from figures','Positional chains are prefigures. Actual figures must also contain both endpoints of each interval they contain; this applies separately to the finite and full atlases.','A05,A05a,C11; endpoint closure proof.')
add('SA21-A-K15',st+'readings/156-9.md','118','Flag wording completed','Add incidence closure to the positional-flag description. A singleton interval is a prefigure and not a figure.','A05,A05a,C11.')
add('SA21-A-K16',tr+'J156-7-12_transcription.tex','7','Empty-infimum qualification','Arbitrary nonempty meets are preserved under the exact support criterion. The empty meet is preserved into [0,S_F]; preservation into the ambient support lattice additionally requires S_F=1.','A16, complete arbitrary-family proof.')
add('SA21-A-K17',tr+'J156-7-12_transcription.tex','7-19','Exact replacement for every theorem clause','Clauses(a)-(c) are characterized by the two-neighbourhood condition. Clause(d), recovering full support for an incidence-closed subfigure, is automatic under the old hypotheses; without them it has the separate exact incidence-coverage polar criterion.','A16; original scan87/90 open sets compared with open-lieu representatives; all20figures of oldR5 satisfy(d).')
add('SA21-A-K18',pf,pline('**L7.**'),'Morphisms distinguished from correspondences','Remove the universal self-orthogonal radical to compare objects with orthosets. Saturated correspondences correspond to all complete join maps; ordinary orthogonality-preserving functions form a different category.','A21,A22; typed inverse maps, composition and dagger; two finite relation/function separations.')
add('SA21-A-K19',st+'HUNCHES.md','318','Bibliographic correction','The thesis author is J.C.Dacey (James Charles Dacey Jr.), not J.R.Dacey. The full thesis was not retrieved, and no unopened theorem is invoked.','Opened Jenča and Paseka-Vetterlein bibliographies; references.bib access note.')
add('SA21-A-K20',pf,pline('J. R. Dacey, *Orthomodular spaces*'),'Bibliographic correction','Use J.C.Dacey rather than J.R.Dacey.','Opened primary bibliographies; references.bib.')
add('SA21-A-K21',pf,pline('**Other work.**'),'Prior-attention search, not a priority claim','An official Montpellier notice documents Jean Malgoire introductory seminar of3October2002 on this manuscript. This establishes prior attention, but does not by itself settle whether a published full study exists. No priority claim is made.','Opened official seminar abstract; Malgoire2002 bibliography entry.')
with (root/'parts/supports/CORRECTIONS.tsv').open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['id','file','line_or_locator','kind','correction','evidence']);w.writerows(rows)
print(f'{len(rows)} Part A corrections with verified attachment paths and line ranges')
