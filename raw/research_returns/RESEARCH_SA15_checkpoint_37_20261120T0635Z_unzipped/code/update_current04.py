"""Update current findings without creating or dating a progress review early."""
from pathlib import Path
import json,re,datetime
w=Path(__file__).resolve().parents[1]
rows=json.loads((w/'notes/item_status.json').read_text())
changes={
'A.3':('OPEN: ordinarity refuted; positivity and effective rank computation proved','thm:all-X-explicit-positive-rank; prop:effective-generic-rank; thm:relative-ordinarity-fails-smooth','Eventual positivity and the generic Hodge parenthesis have explicit bounds. A finite exact matrix algorithm determines each specified finite-field generic rank. A uniform structural rank formula for arbitrary X remains; the characteristic-two alpha4 surface refutes relative ordinarity.'),
'A.4':('OPEN: all projective spaces and all determinant images determined','thm:pn-odd-full-groups; thm:pn-char2-all-groups; prop:exact-general-determinant-image','Every projective-space degree and characteristic is classified, geometrically and arithmetically. General geometric and arithmetic determinant images are exact Kummer images computable from the stable Hasse determinant. An explicit characteristic-two adjunction-square bound produces a fixed covector on every smooth section. The complete nonabelian image and irreducibility classification for arbitrary ambient X remain.'),
'A.5':('PROVED for every ambient X with explicit degree bound','thm:all-X-residue-density; cor:pn-all-p-sharp-residue-threshold','Every residue modulo p occurs in every nonempty open over a suitable finite extension, for every d at least the explicit d_res from Hilbert/regularity/Koszul data. Geometric connectedness is unnecessary. The sharp projective-space threshold is d=n+2.'),
'B.4':('OPEN: finite explicit upper and lower bounds proved','thm:B-RD17; prop:B-RD18; cor:B-RD18; prop:B-RD5','A finite universal truncation bound is proved in every height and every prime. Height1 has least index0. For every h>=2 and admissible e, M(0) fails to determine the prime-to-p character; higher lower bounds are explicit. The least index between the bounds remains.'),
'C.1':('PROVED: proposed iff refuted; exact essential image determined','thm:C-RD13; cor:C-RD14; thm:C-RD12; thm:C-RD11; prop:C-RD5','The exact necessary and sufficient criterion specifies closed-locus realization, algebraization of its Serre–Tate tower, actual punctured-completion comparison, and a compatible quasi-affine atlas. The two effectivity conditions disappear for elliptic schemes and when a reduced realization is already specified. No excellence or finite-normalization hypothesis is used.'),
'E.2':('OPEN: coherent characteristic-zero and F-pure positive-characteristic cases proved','prop:DE-E2-coherent; lem:DE-crystal-Fdiv; prop:DE-E2-Fpure','Every quasi-coherent infinitesimal crystal over a finite-type perfect-field scheme is F-divided. For F-pure such schemes, arbitrary quasi-coherent stratifications and crystals agree. The general flat relative assertion, including arbitrary sheaves, remains. The manuscript itself inserts a coherent locally noetherian qualification.'),
'F.1':('COMPLETE for the current results, with open obligations retained','RESEARCH_SA15_results.csv; paper Part F','Every numbered theorem-like environment has a stable label, visible status, proof location and manuscript-page mapping. Short French quotations distinguish the absent scans from the supplied transcription witnesses; R7–R10 have fresh numbered audits.'),
'F.2':('COMPLETE source census with explicit access limitations','notes/SOURCE_CENSUS.tsv; references.bib; source logs','Every named or used bibliographic source has a current access/locator record, including not-obtained originals. Failed attempts and successful later retrieval are distinguished. The topic-specific query record and all three agent source logs are retained.'),
'Lead A':('REFUTED as full-GL/ordinarity prediction; point-count consequence PROVED','thm:pn-char2-all-groups; thm:relative-ordinarity-fails-smooth; thm:all-X-residue-density','The full-linear prediction fails in infinitely many characteristic-two degrees, and relative ordinarity fails for a smooth fixed ambient surface. Eventual positivity and every-open point-count residues are proved for all X; exact arbitrary-X monodromy remains the separate A4 obligation.')
}
for row in rows:
 if row['item'] in changes:row['status'],row['where'],row['gate']=changes[row['item']]
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
root=json.loads((w/'notes/root_results.json').read_text())
for r in root:
 if r['id'].startswith('A6-'):r['manuscript_pages_settled']='4:10--11'
(w/'notes/root_results.json').write_text(json.dumps(root,indent=2)+'\n')
aux=(w/'RESEARCH_SA15_paper.aux').read_text()
nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux))
idmap={r['id']:r['label'] for r in root}
def where(text):
 out=[]
 for x in text.split('; '):
  lab=idmap.get(x,x);out.append(x+(f' (no. {nums[lab]})' if lab in nums else ''))
 return '; '.join(out)
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'+'\n'.join('| '+' | '.join([r['item'],r['status'],where(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
p=w/'RESEARCH_SA15_report.md';old=p.read_text();body=old[old.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 04: current findings and access record\n'
if marker in body:body=body.split(marker)[0]
new=marker+'''
A.5 is now proved in the stated generality, with an explicit degree bound for every smooth projective connected ambient variety over a finite field. The proof independently realizes many node-permutation factors, lifts the finite part of the boundary Lang kernel through a henselian pair, bounds all discarded and newly appearing cohomology, and isolates a single alternating factor acting trivially on the error spaces. Its traces exhaust F_p. The point-count conclusion uses the exact constant-field/Chebotarev direction. This does not identify the full arbitrary-X monodromy group.

B.4 now has a finite universal upper bound, using the opened Kisin rational classification (including p=2), a bounded good-reduction extension, and the Vasiu–Zink finite-flat Hom-loss bound. Honda height-two formal groups give explicit lower bounds at every admissible ramification index. The sharp least general-height truncation is still open. The proposed p=2 height-one full-inertia calculation was rejected because the requested character is restricted to prime-to-p elements; the correct least height-one index is zero for every prime.

C.1 now has an absolute necessary and sufficient essential-image criterion on every locally noetherian base. It separately retains formal algebraization, actual punctured-completion comparison and compatible quasi-affine charts; it does not assume the desired global extension. In relative dimension one, canonical polarized algebraization removes the algebraization and atlas conditions. The additional nilpotent-overlap criterion is also exact once the reduced triple is realized. E.2 now includes all quasi-coherent modules on F-pure finite-type perfect-field schemes, while the general relative assertion remains open. The transcription's coherent/locally-noetherian insertion at6:7 is explicitly quoted and distinguished from the broader prompt.

The numbered statement register now covers all numbered environments, including previously unlabelled remarks and the new manuscript companion. The source census is passage-specific: Kisin, Messing, Mazur–Messing, Serre and Fontaine originals were obtained after earlier failed attempts. Original BBMII, Sah and the cotangent-complex books remain marked not obtained. The full SGA4½ target was not obtained; the trace formula used is the independently opened Katz SGA7II statement. No original scan reading is claimed.

### Additional computations and their precise scope

The retained `agents/obstructions_crystals/code/R7_R10_checks.py` ran in 0.146205 seconds and performs exact integer and symbolic calculations for the all-prime elliptic obstruction audit. Its output `R7_R10_checks_output.json` verifies the Legendre discriminant, the characteristic-two equation y²+txy+y=x³ with discriminant t³+1 and c4=t4, the characteristic-three Hasse polynomial t, and the integer binomial coefficient identity for p=3,5,7,11,13,17,19. The general-prime proof is the binomial argument in the text, not an extrapolation from those checks. Other computations, inputs, outputs and timings remain recorded in the preceding report and their per-program JSON records.

### Corrections, superseded passages and retained limitations

Earlier checkpoint statements that general A.5 is open, that the Kisin originals were unavailable, or that E.2 has only the coherent characteristic-zero subcase are superseded by the current table and census. Earlier mathematical constructions and independent projective-space proofs are retained. No unresolved proof has been silently upgraded by the statement-numbering script: each promotion listed here follows a targeted independent audit. The blank manuscript reference at100:11 is only plausibly identified with the matching Grothendieck1966 pp75–76; the text does not claim direct evidence of the intended citation. Rendering images, source PDFs, TeX runtime and older ZIPs remain intentionally excluded.

'''
new+=(w/'notes/ROOT_SEARCH_LOG_04.md').read_text()+'\n\n'+(w/'notes/SOURCE_CENSUS.md').read_text()
p.write_text('INCOMPLETE\n\n'+table+'\n'+body+new)
events=w/'notes/root_check_events.tsv';existing=events.read_text()
descs={
'A5-GENERAL-X':'Independent audit passed: Entin product criterion; full jets in characteristic2; henselian finite Lang subgroup and full boundary finite images; Cech incoming differential bounds; Koszul/Hilbert explicit constants; alternating-factor isolation; Chebotarev and constant-field transfer.',
'A4-GENERAL-DETERMINANT':'Independent audit passed: exact finite stable-rank matrix product over imperfect parameter function field; divisor-valuation Kummer gcd; geometric and arithmetic determinant image, including constant-extension factor and Frobenius inversion.',
'B-RD17-ROOT':'Independent audit of filtered finite-flat bifiltration eigenlength comparison, bounded inertia extension, original Kisin2.2.6 all-prime rational classification and VasiuZinkCor2 quantitative bound; least-index question retained.',
'B-RD18-ROOT':'Independent recheck of Drinfeld full-level formal construction for Honda height2 tame orderp+1 includingp2; determinant/cyclotomic containment and exact lower-bound indexing.',
'B-RD4-DICTIONARY-ROOT':'Independent comparison convention check Dcov(G)=Dcontra(GD)=Dcris(TpG)(-1); opened Fontaine exactness and WD inertia formulas; extra potential semistability hypothesis retained.',
'C-RD13-ROOT':'Independent audit of the complete formal-model and paired-chart essential-image criterion, local-to-global compatibility, BT faithfulness and elliptic polarized algebraization. Original MoretBailly0.3/1.1/1.2 and EGAIII1 Theorems5.4.1/5.4.5 opened with exact hypotheses.',
'A4-ADJUNCTION-ROOT':'Independent audit of relative Frobenius duality, square-root adjunction covector, regularity and ambient restriction bounds, and nonvanishing on vanishing cohomology; original BrionKumar1.3.6-1.3.8 opened.',
'C-RD12-ROOT':'Independent complete-base SerreTate lifting and formal-overlap descent audit; ArtinRees and MoretBailly0.3 source hypotheses checked; reduced realization is expressly an additional datum.',
'E2-FPURE-ROOT':'Independent audit of quasi-coherent infinitesimal crystal/F-divided equivalence via ambient Frobenius neighbourhoods and fpqc descent; pure Frobenius effective module descent opened; full relative scope remains unresolved.',
'R7-R10-ROOT':'Independent proof check of all four supplied-background audits: display complement determinant, covariant stable rank, Dieudonne bimodule actions and corrected W_(n+1) indices, all-prime elliptic F² obstruction, nilpotent-PD hypotheses, integral no-PD cohomology vanishing.'}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with events.open('a') as f:
 for sid,desc in descs.items():
  if sid+'\t' not in existing:f.write('\t'.join([sid,now,'GPT-6 Astra (OpenAI); /root; inherited effort','independent re-proof',desc])+'\n')
print('Current table, manuscript mappings, source census report and root audit events updated; no progress review recorded yet.')
