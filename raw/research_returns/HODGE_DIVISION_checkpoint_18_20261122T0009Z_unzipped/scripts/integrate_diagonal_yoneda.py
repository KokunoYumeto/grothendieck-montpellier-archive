"""Integrate the whole-reviewed diagonal Yoneda strengthening of E826."""
from pathlib import Path
from datetime import datetime, timezone
import csv,hashlib,json
R=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
proof='agents/sixfolds/rm_diagonal_yoneda_obstruction_section.tex'
h='d8e80fbd6b0eb2648dd15750073057f5cb9c3757b79ed0afa43a578813d3d4b0'
assert hashlib.sha256((R/proof).read_bytes()).hexdigest()==h
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
assert all(r['id']!='Q5aa' for r in rows)
(R/'research/gates_before_diagonal_yoneda.json').write_text(json.dumps({r['id']:r for r in rows if r['id']=='Q5i'},indent=2)+'\n')
p=R/'HODGE_DIVISION.tex';s=p.read_text()
anchor=r'\input{agents/sixfolds/rm_two_slope_extension_obstruction_section.tex}'
assert anchor in s and proof not in s;s=s.replace(anchor,anchor+'\n'+r'\input{'+proof+'}')
old='has invariant middle Ext at least $192$ and is not a seed.\nRank-deficient unit matrices, other unequal-degree extensions, other'
new=r'''has invariant middle Ext at least $192$ and is not a seed.
SF-E827 then removes the global cross-$\operatorname{Ext}^3$
vanishing requirement in two precise settings. Actual diagonal Yoneda
classes give $\operatorname{ext}^2_\Gamma(E,E)\ge6u$ when every
cross-line difference is nondegenerate, and at least $4u$ for every
nonzero cross difference in the rational four-divisor Gaussian algebra,
including all degenerate cases. Thus $u\ge4$ or respectively $u\ge5$
is excluded; selected negative blocks contribute under their explicit
unit-block vanishing condition. The actual equivariant filtration and
blocks are essential hypotheses. Too few such blocks and more general
divisor or filtration types remain open.
Rank-deficient unit matrices, other unequal-degree extensions, other'''
assert old in s;s=s.replace(old,new);p.write_text(s)
for r in rows:
 if r['id']=='Q5i':
  old='Remaining: unstable bundles'
  new=('SF-E827 removes globalExt3(B,A)=0 in the actual equivariant two-slope architecture: each positive line block contributes6 invariant diagonalExt2 for all nondegenerate cross differences, or4 for all nonzero differences in the rational four-divisor Gaussian algebra including degenerate cases. Thresholdu>=4 oru>=5 excludes balancedcap18; selected negative blocks add only under explicitExt3(M_b,A0)=0. Too few positive/selected blocks, more general divisor directions or actual filtration types remain open. Remaining: unstable bundles')
  assert old in r['finding_ids_or_current_gate'];r['finding_ids_or_current_gate']=r['finding_ids_or_current_gate'].replace(old,new).replace('outsideE818/E821/E822/E823/E824/E825/E826','outsideE818/E821/E822/E823/E824/E825/E826/E827')
rows.append(dict(zip(fields,['Q5aa','Prompt target5; surviving diagonal Yoneda classes','Can nonzero opposite Ext3 or degenerate cross-line differences repair the actual two-slope architecture with at least4 nondegenerate positive blocks or5 blocks in the rational four-divisor algebra?','refuted','SF-E827: actual diagonal LES projections, normalized multiplicity trace and invariant averaging give ext2Gamma>18 without a global crossExt3 vanishing. Full nondegenerate index argument gives6 per positive block; actual product Kunneth gives4 in the rational four-divisor algebra, including all nonzero degeneracies and flat twists. Selected negative blocks require explicit unit Ext3 vanishing. Whole root/peer reviews PASS; no numerical premise or universal unstable-sheaf exclusion.'])))
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
events=[
 ('SF-E827','targeted proof check','Root read every265line of final clarified draftabe42293 and then every281line of canonical TeX atd8e80fbd, plus full independent report. PASS actual Hom(A,triangle) diagonal injection, Hom(-,E) next boundary, independent B-side lifts and quotient trace, all multiplicity matrices, finite-invariant averaging, every nondegenerate pair and every rational-four-divisor degenerate Kunneth case with flat twists. No globalExt3 vanishing or assumed spectral-sequence splitting enters. Conversion preserves all10equation tags and6namespaced labels.',proof+'; agents/sixfolds/rm_diagonal_yoneda_obstruction_conversion_check.json'),
 ('SF-E827 independent mathematical audit','independent re-proof','G34 entire265-line proof audit completed20:16:14UTC PASS. The only clarification repeats nonzero before E827.10, already forced by opposite slopes in applications; zero difference is explicitly not covered. Actual boundary and equivariance arguments, both surface-factor cases and caprank18 checked. No new finite computation or numerical premise is claimed.', 'agents/g34_eightfolds/bireflection/DIAGONAL_YONEDA_PEER_AUDIT.md'),
 ('SF-E827 source boundary','carried as background without fault found','Mumford original nondegenerate index theorem, Mukai Pic0 vanishing and BF evaluation/trace retain their previously complete source readings. E826 fresh root/peer S21 proof through8 and rationalB shear are reused. S21 supplied-source status remains explicit; no new Markman, Severn or032 premise is promoted. The new Yoneda/Kunneth argument is fully proved in this section.',proof)]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:
 f.write('\n## Diagonal classes remove the cross-Ext escape in a larger family\n\n'+now+' — Q5aa refuted and Q5i strictly reduced. SF-E827 excludes actual two-slope extensions with at least4 positive blocks and nondegenerate cross differences, or at least5 positive blocks in the rational four-divisor Gaussian algebra even with degeneracies, without globalExt3(B,A)=0. Actual equivariant filtration/block hypotheses remain. All new proof and canonical text read in full by root and independent peer; no new numeric test is needed. This is integration, not an hourly review.\n')
with (R/'IMPLICATIONS.md').open('a') as f:
 f.write('''\n## Actual diagonal Yoneda classes persist beyond the cross-Ext vanishing case\n\nSF-E827 follows selected diagonal classes through both actual triangle boundaries. It therefore strengthens the E826 architecture exclusion even when opposite crossExt3 groups exist. In the rational four-divisor Gaussian algebra the actual abelian-surface product decomposition leaves a four-dimensional mixed H2 subspace that survives every nonzero degenerate cross difference. The precise remaining gate requires fewer usable blocks, divisor directions outside that algebra, or an actual filtration not covered by the lemma. No successful seed follows from merely opening one of those possibilities.\n\nThis remains a necessary obstruction in the supplied DEG_L categorical cycle-supplier framework for condition A, cote16 scan050, with the common EGA/SGA and realization placement. It is not a general negative Hodge result and does not improve a detector bound without constructing a valid supplier. The condition-I division step, Cayley-Hamilton inversion and motivic/L-function scope are unchanged.\n''')
p=R/'research/frameworks.tex';s=p.read_text();assert 'SF-E811--826 concern' in s;p.write_text(s.replace('SF-E811--826 concern','SF-E811--827 concern'))
out={'date_utc':now,'integrated':['SF-E827'],'reviewed_draft_sha256':'abe42293fb48da62436bfe7fafd7ae19a2546a768ad294f6f89ed4ec451f8a27','canonical_sha256':h,'new_rows':{'Q5aa':'refuted'},'strictly_reduced_main_gates':['Q5i'],'new_computation':False}
(R/'research/diagonal_yoneda_integration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
