"""Integrate the independently audited small orthogonal and two-slope obstructions."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json
R=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).isoformat()
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
proofs={
 'research/orthogonal_small_section.tex':'44c6d392c14925b173191439b3668d3b75e42f1358bad411749033e92b842d21',
 'agents/sixfolds/rm_two_slope_extension_obstruction_section.tex':'5391995f71c99eeaaae500e2ab3446df062ab8a8f1b35175761265ff3df5c458'}
for n,h in proofs.items():assert sha(n)==h,n
bib='research/orthogonal_small_bibitems.tex'
assert sha(bib)=='7401537dc18dad4b38297cabdda235684a1553ec35b2f3b238eebfe966f27650'
q=R/'QUESTIONS.tsv';rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
assert not {'Q2bm','Q5z'}&{r['id'] for r in rows}
(R/'research/gates_before_orthogonal_two_slope.json').write_text(json.dumps({r['id']:r for r in rows if r['id'] in ('Q2i','Q5i')},indent=2)+'\n')
p=R/'research/orthogonal_small_section.tex';s=p.read_text()
old='New root derivation. The full mathematical proof is given below;\nindependent whole-proof review is pending.'
new='New root derivation. Complete author and independent peer proof and\nsource reviews have passed, together with separate full exact spectrum\nreconstructions and the retained GAP orthogonality checks.'
assert old in s;p.write_text(s.replace(old,new))

p=R/'HODGE_DIVISION.tex';s=p.read_text()
for anchor,n in [(r'\input{research/exceptional_small_section.tex}',list(proofs)[0]),(r'\input{agents/sixfolds/rm_free_summand_overlap_section.tex}',list(proofs)[1])]:
 assert anchor in s and n not in s;s=s.replace(anchor,anchor+'\n'+r'\input{'+n+'}')
anchor=r'\input{research/exceptional_small_bibitems.tex}'
assert anchor in s and bib not in s;s=s.replace(anchor,anchor+'\n'+r'\input{'+bib+'}')
old='ranges finite but does not enumerate or settle them. Other small-field\nhigher-rank Lie representations remain outside these exclusions.'
new=r'''ranges finite but does not enumerate or settle them.
D-OSM-01--04 excludes arbitrary mixed cores from the eight types
$\Omega_7(3)$, $\Omega_8^-(2)$, $\mathrm{P}\Omega_8^\pm(3)$,
$\Omega_{10}^\pm(2)$ and $\Omega_{12}^\pm(2)$, with all covers and
compatible normalizers. Fifteen complete tables give common support
$e/5$ and force $e\le15<27$. The ninth type $\Omega_9(3)$ is
excluded under transitivity and the nonselfdual-original hypothesis:
its two nonselfdual characters have quarter normalizer support, while
the other case uses the nontrivial form multiplier and gives
$e\le41/4<780$. This ninth conclusion is not enlarged to arbitrary
mixtures. The small $\Omega_8^+(2)$ representations retain their
separate gates. Other small-field higher-rank Lie representations
remain outside these exclusions.'''
assert old in s;s=s.replace(old,new)
old='there is no universal added-free exclusion or balanced semiregular seed.\nRank-deficient unit matrices, other unequal-degree extensions, other'
new=r'''there is no universal added-free exclusion or balanced semiregular seed.
SF-E826 excludes every actual two-slope extension in its specified
unit-plus-line architecture with $\operatorname{Ext}^3(B,A)=0$
and at least four distinct line-class blocks. The actual invariant
triangle maps give $\operatorname{ext}^2_\Gamma(E,E)\ge6(u+v)>18$.
It also constructs an actual indecomposable object of full balanced
character and positive defect determinant, using a proved rectangular
matrix construction and a checked 33-vertex tree. That object still
has invariant middle Ext at least $192$ and is not a seed.
Rank-deficient unit matrices, other unequal-degree extensions, other'''
assert old in s;s=s.replace(old,new);p.write_text(s)

for r in rows:
 if r['id']=='Q2i':
  old='Other small-field higher-rank Lie cores remain.'
  new=('D-OSM-01--04 excludes arbitrary mixed cores of eight types Omega7(3),Omega8-(2),POmega8+(3),POmega8-(3),Omega10+/-(2),Omega12+/-(2), all central covers and normalizers:15tables2938rows778260spectra give support1/5 and e<=15<27. The ninth Omega9(3) is excluded only with transitivity and nonselfdual original: two nonselfdual core characters have quarter normalizer support; selfdual case uses nontrivial form multiplier to force e<=41/4<780. Arbitrary mixes involving ninth not claimed. Omega8+(2) small representations retain separate gates. Other small-field higher-rank Lie cores remain.')
  assert old in r['finding_ids_or_current_gate'];r['finding_ids_or_current_gate']=r['finding_ids_or_current_gate'].replace(old,new)
 if r['id']=='Q5i':
  old='Remaining: unstable bundles'
  new=('SF-E826 excludes the whole actual two-slope unit-plus-line extension architecture with Ext3(B,A)=0 and u+v>=4 distinct line-class blocks, using invariant ext2>=6(u+v)>18. Its exact full-character example has rank10923384225792 and an actual33-vertex matrix gluing with local endomorphism quotientC and square-zero kernel; it is indecomposable but ext2Gamma>=192, hence not semiregular. Positive adjusted determinant by itself therefore does not repair this family. Remaining: unstable bundles')
  assert old in r['finding_ids_or_current_gate'];r['finding_ids_or_current_gate']=r['finding_ids_or_current_gate'].replace(old,new)
  r['finding_ids_or_current_gate']=r['finding_ids_or_current_gate'].replace('outsideE818/E821/E822/E823/E824/E825','outsideE818/E821/E822/E823/E824/E825/E826')
rows.extend([
 dict(zip(fields,['Q2bm','Prompt target2; nine small orthogonal core families','Can the eight listed arbitrary mixed orthogonal types, or a transitive Omega9(3) core in the nonselfdual-original problem, supply actual period rank nine?','refuted','D-OSM-01--04: complete15table exact spectra,3141indicators and6normalfusions. Eight-type support1/5 forces e<=15<27. Ninth-type nonreal quarter-support or selfdual form-multiplier case forces e<=6 or41/4<780. No general intransitive ninth-type mixture is claimed. Full author and independent peer proof/source checks PASS, separate arithmetic reconstructions PASS.'])),
 dict(zip(fields,['Q5z','Prompt target5; actual two-slope coupled unit/line extensions','Can an actual two-slope unit-plus-line extension satisfying Ext3(B,A)=0 and u+v>=4 line-class blocks be a balanced weakly semiregular seed?','refuted','SF-E826: actual three-LES inequality and intrinsic torsion/HN/block equivariance give ext2Gamma>=6(u+v)>18. Full positive integral rank10923384225792 example is actually indecomposable by explicit rectangular bricks on a checked33-vertex tree, yet ext2Gamma>=192. Entire architecture excluded, not every positive-determinant form. Full root/peer proof/source reviews and independent exact16coordinate240pair148edge certificate PASS.']))])
with q.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)
events=[
 ('D-OSM-01--04','targeted proof check','Root author reread entire frozen248-line proof and whole bibliography after editorial fixes, then entire independent report. PASS all universal central quotients, six actual order-two extension relations, complete-normalizer commutator for noncyclic outer groups, mixed tensor cycles, eighth-family support and separate transitive ninth-family selfdual/nonselfdual argument. Only review-status text changes at integration.',list(proofs)[0]+'; '+bib+'; agents/imprimitive/audit_orthogonal_small/PEER_AUDIT.md'),
 ('D-OSM root exact spectra and orthogonality','computation or formal certificate','Actual GAP export full orthogonality of all15tables PASS3.830861454s, separate spectrum probe completed2938rows778260spectra. Root exact rational-trace checker PASS59.481014833s on all2938rows778260spectra,3141indicators,6normalfusions. InputSHA5236207618c2564af7ed4871c0f92a667664255d2e60be87f037257356669b79. Includes all extension rows with irreducible core restriction and all nonfaithful central characters. Original table correctness is cited, not inferred solely from consistency.', 'research/orthogonal_small_export.g; research/orthogonal_small_export_run.json; research/orthogonal_small_probe.json; research/check_orthogonal_small.py; research/orthogonal_small_checked.json'),
 ('D-OSM independent full reconstruction','independent re-proof','Peer whole-proof/source/code review completed20:15:28UTC PASS. Independent polynomial-Fourier/Galois-substitution reconstruction, importing neither root arithmetic nor selected rows, passed39.612917s:15tables2938rows778260spectra3141indicators6fusions and241074distinct Fourier problems. Separate metadata checker confirms all9multiplier/outer records and6genuine outer actions. Root read entire report; no fresh root peer-code execution claimed.', 'agents/imprimitive/audit_orthogonal_small/PEER_AUDIT.md; agents/imprimitive/audit_orthogonal_small/independent_check.py; agents/imprimitive/audit_orthogonal_small/independent_checked.json'),
 ('D-OSM original data provenance','used and rechecked in this run','Root freshly opened/read all15official CTblLib information pages, complete manual3.7-3 definition and universal-cover naming, and HHM ch5p35 complete exceptional multiplier table. Eight ATLAS-associated core/outer records are distinguished from Spin8+3 V4G construction, Neunhoeffer2008 two covers, Magma2018 O12cores and Frame1986/Frame-Pahlings1987 outer tables. Officialweb1.3.10 versus executed1.3.11 is recorded. Peer independently reread all15records/manual and matching source metadata.',bib+'; agents/imprimitive/audit_orthogonal_small/source_log.json'),
 ('SF-E826 whole proof and canonical conversion','targeted proof check','Root read entire473-line frozen draft and both full author programs, then every521line of final canonical TeX and full conversion record, and entire independent peer report. PASS actual3LES inequality, finite invariants, intrinsic torsion/HN filtration, block Hom orthogonality, caprank6/18, all16character coordinates, resolution Ext3 vanishings and actual Ext1 capacities, all-size rectangular bricks, actual Cech gluing and square-zero endomorphism kernel. Canonical labels SF-E826; no proof premise changes in conversion and no TeX compilation.',list(proofs)[1]+'; agents/sixfolds/rm_two_slope_extension_obstruction_conversion_check.json; agents/g34_eightfolds/bireflection/TWO_SLOPE_EXTENSION_PEER_AUDIT.md'),
 ('SF-E826 distinct actual certificates','computation or formal certificate','Author coupling exact run PASS0.221079061s on full16coordinates,240linepairs,20unitcases,148qualifiededges and33vertex32edgetree; separate36rectangular matrix systems PASS0.011185307s. Independent G34 checker PASS0.04080446s reconstructs all those data and capranks18/6. Its initial unnecessary nondegeneracy assertion on unused auxiliary terms was repaired and failure retained; no author mathematical defect. Root read both full author programs and full peer report, not a new root rerun.', 'agents/sixfolds/rm_two_slope_coupling_certificate.py; agents/sixfolds/rm_rectangular_brick_certificate.py; agents/g34_eightfolds/bireflection/audit_two_slope_extension.py; agents/g34_eightfolds/bireflection/audit_two_slope_extension.json'),
 ('SF-E826 invariant source boundary','used and rechecked in this run','Root freshly reread the complete supplied S21 proof from nonidentity sector vanishings through invariant Serre duality, forgetting/induction comparison, full(S21.8) evaluation adjunction and rationalB shear. Supplied status retained. Original Mumfordsection16pp150--153,162--163 and BF2008 exact evaluation/trace locators retain earlier full root readings; peer freshly reread Mumford and S21 for E826. No new Markman, Severn or032 premise is promoted.', 'DEG_L.tex supplied S21; agents/g34_eightfolds/bireflection/TWO_SLOPE_EXTENSION_PEER_AUDIT.md')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 for sid,typ,out,ev in events:w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])
with (R/'LEDGER.md').open('a') as f:
 f.write('\n## Nine small orthogonal reductions and an actual extension obstruction\n\n'+now+' — Q2bm and Q5z refuted; Q2i and Q5i strictly reduced. D-OSM excludes eight orthogonal types in arbitrary mixtures and a ninth with explicit transitivity/nonselfdual-original hypotheses. SF-E826 excludes the whole specified actual two-slope architecture and proves indecomposability of a large exact balanced object that still fails semiregularity. Complete root/peer reviews and separate actual arithmetic certificates passed. This is integration, not an hourly review.\n')
with (R/'IMPLICATIONS.md').open('a') as f:
 f.write('''\n## Small orthogonal finite-cover sources\n\nD-OSM strictly removes eight complete small orthogonal families with all covers and compatible normalizers, plus transitive Omega9(3) in the nonselfdual-original scope. The ninth scope is intentionally separate: its weaker general support cannot be silently combined with arbitrary other factors. These restrictions concern the actual polarized weight-one Hurwitz supplier for condition A, cote16 scan050, with the exact EGA/SGA interpretation recorded in the framework section. Complete ordinary tables are cited mathematical inputs with their distinct provenance; full spectrum reconstruction does not replace their group-theoretic construction.\n\n## An actual indecomposable balanced object still fails semiregularity\n\nSF-E826 proves an actual extension and its indecomposability by explicit ordinary matrix arrows and Cech gluing. It has the full balanced character and the positive determinant required by SF-E825. Its invariant middle Ext nevertheless has dimension at least192, versus cap rank18; the entire specified two-slope family is excluded by the same actual triangle argument. Thus connectedness of an Ext graph or positive determinant does not alone resolve the seed gate. This is an obstruction in the supplied DEG_L semiregularity framework, with exact source status, not a negative Hodge statement. It supplies neither a cycle nor condition-I positivity, a new Cayley-Hamilton projector, or a motivic L-value bound.\n''')
p=R/'research/frameworks.tex';s=p.read_text();s=s.replace('D-OC2-F, D-EXS,','D-OC2-F, D-EXS, D-OSM,').replace('SF-E811--825 concern','SF-E811--826 concern');p.write_text(s)
out={'date_utc':now,'integrated':['D-OSM-01--04','SF-E826'],'whole_reviewed_sha256':proofs,'canonical_sha256':{n:sha(n) for n in proofs},'bib_sha256':{bib:sha(bib)},'new_rows':{'Q2bm':'refuted','Q5z':'refuted'},'strictly_reduced_main_gates':['Q2i','Q5i']}
(R/'research/orthogonal_two_slope_integration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
