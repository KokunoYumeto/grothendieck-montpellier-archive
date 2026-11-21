"""Integrate three completely read and independently audited reductions.

Only status wording and collision-safe labels change in the frozen proofs.
This is an integration, not a scheduled substantive review.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re

R = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
frozen = {
 'agents/sixfolds/rm_free_summand_overlap_section.tex': 'f1dbe8bc05a87c0d07adf748f8c0b321fa0191685dba6a68de53201fce54bfee',
 'agents/imprimitive/odd_c2/finite_odd_c2_section.tex': '7eed128e6c5d4ad9835025a94f0a82e372abe6a0fb6fb335627e34ba8e88f343',
 'agents/imprimitive/odd_c2/odd_c2_all_fields_section.tex': '10d17b9a511c5acd80a026ad724517211448860224e81fce809039074bf2fc88',
 'research/exceptional_small_section.tex': 'eed92a30c4fb13b822ab967d3622eede628f381c45932d9805e0d7377f99f2da',
 'agents/g34_eightfolds/bireflection/heisenberg_carrier_section.tex': 'a29d62b414f69ff2d91113b75d0f4094038df64ac90ef48b13ea52b435b4b85f',
}
for n,h in frozen.items(): assert sha(R/n)==h, n
q=R/'QUESTIONS.tsv'
rows=list(csv.DictReader(q.open(),delimiter='\t'));fields=list(rows[0])
assert not {'Q5y','Q2bi','Q2bj'} & {r['id'] for r in rows}
(R/'research/gates_before_e825_c2_exceptional.json').write_text(json.dumps(
 {r['id']:r for r in rows if r['id'] in ('Q2i','Q5i')},indent=2)+'\n')

# Preserve the complete mathematical text; give the converted labels a namespace.
p=R/'agents/sixfolds/rm_free_summand_overlap_section.tex';s=p.read_text()
labels=re.findall(r'\\label\{([^}]+)\}',s)
assert len(labels)==10
for label in labels:
    s=s.replace('{'+label+'}', '{SF-E825:'+label+'}')
p.write_text(s)

p=R/'agents/imprimitive/odd_c2/finite_odd_c2_section.tex';s=p.read_text()
old=('D-OC2-F is a complete author derivation with an actually executed exact\n'
     'certificate, awaiting independent whole-proof review. Its limited coverage')
new=('D-OC2-F has passed complete author, root and independent peer proof\n'
     'readings, together with separate exact spectrum certificates. Its limited coverage')
assert old in s;p.write_text(s.replace(old,new))
p=R/'agents/imprimitive/odd_c2/odd_c2_all_fields_section.tex';s=p.read_text()
old=('This is a complete author derivation, with an executed exact certificate\n'
     'for the corrected unipotent input. Independent whole-proof review is\n'
     'pending. The core factors in the final theorem are permuted transitively;')
new=('This complete derivation and its cited input scopes have passed whole\n'
     'author, root and independent peer readings. The corrected unipotent\n'
     'input and finite spectra have separate exact certificates.\n'
     'The core factors in the final theorem are permuted transitively;')
assert old in s;p.write_text(s.replace(old,new))
p=R/'research/exceptional_small_section.tex';s=p.read_text()
old=('New complete root derivation. The full exact spectrum reconstruction has\n'
     'run successfully. Independent whole-proof and arithmetic review is pending.')
new=('New complete root derivation, read in full by the author and an\n'
     'independent reviewer with both mathematical audits passing. Full GAP\n'
     'orthogonality and spectrum checks, a separate root exact reconstruction,\n'
     'and an independent polynomial-Fourier reconstruction all passed.')
assert old in s;p.write_text(s.replace(old,new))
canonical={n:sha(R/n) for n in frozen}

p=R/'HODGE_DIVISION.tex';s=p.read_text()
anchor=r'\input{research/a7_cores/a7_section.tex}'
new_inputs=[
 'agents/g34_eightfolds/bireflection/heisenberg_carrier_section.tex',
 'agents/imprimitive/odd_c2/finite_odd_c2_section.tex',
 'agents/imprimitive/odd_c2/odd_c2_all_fields_section.tex',
 'research/exceptional_small_section.tex']
assert anchor in s and all(n not in s for n in new_inputs)
s=s.replace(anchor,anchor+'\n'+'\n'.join(r'\input{'+n+'}' for n in new_inputs))
anchor=r'\input{agents/sixfolds/rm_unit_derived_trace_section.tex}'
assert anchor in s and 'rm_free_summand_overlap_section.tex' not in s
s=s.replace(anchor,anchor+'\n'+r'\input{agents/sixfolds/rm_free_summand_overlap_section.tex}')
anchor=r'\input{research/a7_cores/a7_bibitems.tex}'
bibs=['agents/imprimitive/odd_c2/finite_odd_c2_bibitems.tex',
      'agents/imprimitive/odd_c2/odd_c2_all_fields_bibitems.tex',
      'research/exceptional_small_bibitems.tex']
assert anchor in s and all(n not in s for n in bibs)
s=s.replace(anchor,anchor+'\n'+'\n'.join(r'\input{'+n+'}' for n in bibs))
old=('not a separately refereed journal table. Other small-field higher-rank\n'
     'Lie representations remain outside these exclusions.')
new=r'''not a separately refereed journal table. D-OC2-01--04 now excludes every
transitive ordinary $\operatorname{PSp}_4(q)$ core with odd $q\ge5$
in the nonselfdual-original source problem, allowing all compatible
normalizers, larger inducing fields and either determinant. Its ordinary
unipotent restrictions, elementary shear and Heisenberg estimates, and
explicit field descent include the characteristic-equals-field-order case.
The complete universal $q=5$ endpoint is supplied by D-OC2-F; the separate
finite $q=7,9$ tables have only their stated center-positive coverage.
D-EXS-01--03 excludes arbitrary mixed products of the four simple types
$F_4(2)$, $F_4(3)$, $E_6(2)$ and ${}^2E_6(2)$, including all covers and
compatible normalizers. Complete exact spectra give common normalizer
support $e/5$ and force $e\le15$, below the minimum factor degree $52$.
Other small-field higher-rank Lie representations remain outside these
exclusions.'''
assert old in s;s=s.replace(old,new)
old=('isogeny is assumed. Added free summands, rank-deficient unit matrices,\n'
     'other unequal-degree extensions, other support classes, nonreduced or\n'
     'singular surface modules, and more general derived couplings remain open.')
new=r'''isogeny is assumed. SF-E825 treats arbitrary added locally free summands
and their off-diagonal mixing. It constructs the intrinsic defect bundle
$\widetilde Q$ on the first infinitesimal neighborhood and proves
$\Psi_{\pi_\pm}(\det\widetilde Q+rB)
=(7r/2)\Psi_{\pi_\pm}(\mathcal O_X(D))$ as a necessary condition.
An adjusted flat determinant extending from $X$ is therefore excluded.
Positive adjusted determinants satisfying this condition remain possible;
there is no universal added-free exclusion or balanced semiregular seed.
Rank-deficient unit matrices, other unequal-degree extensions, other
support classes, nonreduced or singular surface modules, and more general
derived couplings remain open.'''
assert old in s;s=s.replace(old,new);p.write_text(s)

for row in rows:
    if row['id']=='Q2i':
        old='Other small-field higher-rank Lie cores remain.'
        new=('D-OC2-01--04 excludes transitive ordinary PSp4(q) cores for every oddq>=5 in the nonselfdual-original source gate, with arbitrary compatible normalizers, either determinant and possibly larger inducing field. The q3 small endpoint remains as previously stated. D-OC2-F separately covers the full universal q5 and center-positive q7/q9 endpoints; no full universal q7/q9 table is assumed. D-EXS-01--03 excludes arbitrary mixed cores of types F4(2),F4(3),E6(2),2E6(2), all central covers and compatible normalizers:1639rows1007457spectra imply common supporte/5 and e<=15<52. Other small-field higher-rank Lie cores remain.')
        assert old in row['finding_ids_or_current_gate']
        row['finding_ids_or_current_gate']=row['finding_ids_or_current_gate'].replace(old,new)
    if row['id']=='Q5i':
        old='Remaining: unstable bundles'
        new=('SF-E825 now treats arbitrary added free summands and off-diagonal mixing: the intrinsic defect bundle Qtilde on S2 must obey Psi_pi(detQtilde+rB)=(7r/2)Psi_pi(L) for both RM bivectors. Flat adjusted determinants extending from X are excluded. Positive adjusted determinants meeting the simultaneous primitive/mixed-block condition remain possible; this is a necessary condition, not universal exclusion. Remaining: unstable bundles')
        assert old in row['finding_ids_or_current_gate']
        row['finding_ids_or_current_gate']=row['finding_ids_or_current_gate'].replace(old,new)
        row['finding_ids_or_current_gate']=row['finding_ids_or_current_gate'].replace(
         'outsideE818/E821/E822/E823/E824 (including added free summands,',
         'outsideE818/E821/E822/E823/E824/E825 (including added free summands with the required positive adjusted determinant,')
new_rows=[
 ['Q5y','Prompt target5; added-free unit-surface forms',
  'What first-overlap condition survives arbitrary locally free summands and off-diagonal gluing?',
  'proved',
  'SF-E825 constructs the intrinsic S2 defect bundle, proves the surviving cyclic Ext1 trace, and derives Psi_pi(detQtilde+rB)=(7r/2)Psi_pi(L) for both RM bivectors. This excludes flat adjusted determinants from X; when the determinant extends from X the corrected class must be primitive on both RM planes with all mixed entries zero. Positive adjusted determinants remain possible. Complete author/root/peer readings and independent exact local/exterior certificates PASS.'],
 ['Q2bi','Prompt target2; ordinary odd rank-two symplectic cores',
  'Can a transitive ordinary PSp4(q) core with odd q>=5 supply the nonselfdual-original rank-nine source?',
  'refuted',
  'D-OC2-01--04 and D-OC2-F exclude all q>=5 with full compatible scalar/outer/permutation actions and either determinant. Corrected published ordinary unipotent restrictions give258 all-q inequalities; elementary shears, D-HOS-01 and field descent cover all inner and compatible outer cases. The complete q5 finite endpoint and q7/q9 degree/Weil endpoints finish the proof. Transitivity and original nonselfduality are explicit; the inducing field may be larger. Whole author/root/peer proof/source checks PASS.'],
 ['Q2bj','Prompt target2; four exceptional small-field families',
  'Can mixed F4(2),F4(3),E6(2),2E6(2) quasisimple cores supply actual period rank nine?',
  'refuted',
  'D-EXS-01--03: all universal-cover nonlinear rows and compatible F4(2) outer rows,1639rows1007457spectra, prove the exact support ratios. A full-normalizer commutator estimate and weighted tensor cycles give common supporte/5; the actual Euler and Hurwitz-image bound forces e<=15<52. Covers arbitrary mixtures, all central quotients including the noncyclic universal center, all outers/scalars, and either determinant. Whole root/peer checks and independent complete polynomial spectra PASS.']]
rows.extend(dict(zip(fields,r)) for r in new_rows)
with q.open('w',newline='') as f:
    w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rows)

events=[
 ('SF-E825','targeted proof check',
  'Root completed the whole473-line canonical TeX reading, after whole initial draft reading and explicit variable-b amendment check; final reviewed draftSHA34af017d1f0c49a56b9924c68b923052afc003ba953e62e1ff55f6d811079783. Read entire independent audit and exact independent code. PASS unital ell map, cancellation of free-factor maps, surviving cyclic trace, unrestricted variable-row boundary terms, standard transition normalization,7/2 coefficient, first-overlap edge-map scope, ordinary-only rational-B transport, Koszul and simultaneous primitive/mixed kernel. Only ten label prefixes changed at integration. Positive adjusted determinants remain open.',
  'agents/sixfolds/rm_free_summand_overlap_section.tex; agents/g34_eightfolds/bireflection/FREE_SUMMAND_OVERLAP_PEER_AUDIT.md'),
 ('SF-E825 independent proof and certificate','independent re-proof',
  'Peer /root/g34_eightfolds completed whole proof/source/code audit at19:43:44UTC, PASS. Independently written exact certificate PASS0.601104s, all six bivector coefficients, arbitrary tangential/normal b derivatives, exact boundaries, generic determinant and16-variable kernel codimension10. Root read whole report and independent code; does not relabel peer execution as a root rerun.',
  'agents/g34_eightfolds/bireflection/audit_free_summand_overlap.py; agents/g34_eightfolds/bireflection/audit_free_summand_overlap.json'),
 ('Buchweitz--Flenner and Mumford in SF-E825','used and rechecked in this run',
  'Root reuses prior whole invoked BF2008 authorpp24--33 and Mumford Abelian Varieties section16 pp150--153 source readings, plus supplied DEG_L S-21. Peer freshly checked BF5.1.3,5.2.2 and Cor5.2.3 and reused previously checked remaining scopes. E825 proves its new local algebra, gluing and edge-map consequences; no fresh rereading of every BF page is claimed at integration.',
  'agents/sixfolds/rm_free_summand_overlap_section.tex; agents/g34_eightfolds/bireflection/FREE_SUMMAND_OVERLAP_PEER_AUDIT.md'),
 ('D-OC2-01--04 and D-OC2-F1--F2','targeted proof check',
  'Root read the entire473-line all-field proof and121-line finite proof, both bibliographies, full unipotent transcription/checker, finite exporter/checker and all-fields auxiliary checker. Read entire independent audit. PASS exhaustive projective-prime cases, involutions with square minus identity, shear/Heisenberg alternatives, no-isotropic centralizers, diagonal duality, characteristic-equals-field-order descent, tensor multiplier budget and finite/Weil endpoints. No arbitrary intransitive mixture theorem or full universal q7/q9 table is claimed. Status wording only changed.',
  'agents/imprimitive/odd_c2/odd_c2_all_fields_section.tex; agents/imprimitive/odd_c2/finite_odd_c2_section.tex; agents/g34_eightfolds/bireflection/ODD_C2_PEER_AUDIT.md'),
 ('D-OC2 independent proof and exact reconstruction','independent re-proof',
  'Peer /root/g34_eightfolds completed audit19:48:54UTC, PASS. Whole proof, cited scopes and all source/code inputs read. Independent Fraction reconstruction of43types258inequalities, finite485rows37502spectra/fivefusions and186-row finite Gauss comparison passed in1.602889s. Four conflicting indexed source identities are not used: direct Table2 rows are retained with the failed diagnostic. Author auxiliary531441-vector F27 test is distinguished from universal proof and from peer execution.',
  'agents/g34_eightfolds/bireflection/audit_odd_c2.py; agents/g34_eightfolds/bireflection/audit_odd_c2.json; agents/imprimitive/odd_c2/STATUS.md'),
 ('Dabbaghian-Abdoly2006 and Vinroot2004 in C2','used and rechecked in this run',
  'Root freshly read all invoked published pp620--624 on author-uploaded ResearchGate: full six-class Table2, six basis characters, all restriction coefficients and averaging proof. Four direct override rows were checked explicitly. This is complete ordinary-character restriction to unipotents, not unipotent characters only. Root freshly read Vinroot2004 Theorem1 authorp1 with characteristic-not-two hypothesis. No binary PDF rendering or fresh reconstruction of Wonenburger is claimed. Li--Xia section2.2.2 Table2.1 p14 and HHM ch5 Table1 p35 scopes reuse prior root readings; peer freshly reread them and official finite-table metadata.',
  'agents/imprimitive/odd_c2/odd_c2_all_fields_bibitems.tex; agents/imprimitive/odd_c2/finite_odd_c2_bibitems.tex'),
 ('D-HOS-01--02 inclusion','used and rechecked in this run',
  'Root previously read whole199-line elementary carrier and degree proof and recorded PASS19:37:07UTC on mathematicalSHA1e71929404f2a5420c308d6971c1327f79422909fe3ab409ee6a6dcbaaae3d7f. CurrentSHAa29d62b414f69ff2d91113b75d0f4094038df64ac90ef48b13ea52b435b4b85f changes status only, read at integration. C2 uses HOS01 with arbitrary multiplicity and no global scalar-power assumption. HOS02 alone is not counted as a new higher odd-rank exclusion.',
  'agents/g34_eightfolds/bireflection/heisenberg_carrier_section.tex'),
 ('D-EXS-01--03','targeted proof check',
  'Root author read and reread the entire221-line frozen proof and bibliography, and complete exporter/root checker; later read entire independent audit and independent code. PASS universal-cover lifting with noncyclic center, all cyclic extension relations without splitness, actual scalar commutators, full-normalizer fifth support, arbitrary mixed tensor cycles and actual Euler/Hurwitz rank-nine budget. Status wording only changed at integration.',
  'research/exceptional_small_section.tex; research/exceptional_small_bibitems.tex; agents/imprimitive/audit_exceptional_small/PEER_AUDIT.md'),
 ('D-EXS actual GAP and root exact certificates','computation or formal certificate',
  'Actual GAP probe completed all four full core row-orthogonality checks and all994643 core nonscalar spectra; the separate exporter completed outer orthogonality and12814 compatible outer spectra. COMPLETE EXCEPTIONAL PROBE observed after earlier long-running status; no runtime invented. Separate root rational-trace/Ramanujan checker passed all1639rows1007457spectra in47.790341917s. Full inputSHA625618617ad0b6268b8898cc39e7e04afb6ae55f8639686347a0b9cf8d244a21. Exact minima4/13,32/73,512/1241,8/19 and degrees52,6643,2482,1938.',
  'research/exceptional_small_probe.g; research/exceptional_small_probe.json; research/exceptional_small_export.g; research/check_exceptional_small.py; research/exceptional_small_checked.json'),
 ('D-EXS independent whole-proof and arithmetic audit','independent re-proof',
  'Peer /root/imprimitive completed whole proof/bibliography/author-code/source audit19:50:40UTC, PASS. Independently written polynomial-Fourier checker imports no root arithmetic, selected rows or outputs; all1639rows1007457spectra and124963distinct Fourier problems passed in41.376808s. Root read full report/code. Peer report truthfully predates later completion of the root GAP probe and is retained unchanged.',
  'agents/imprimitive/audit_exceptional_small/PEER_AUDIT.md; agents/imprimitive/audit_exceptional_small/independent_check.py; agents/imprimitive/audit_exceptional_small/independent_check.json'),
 ('Exceptional small-core original data and multipliers','used and rechecked in this run',
  'Root freshly read HHM ch5 complete Table1 and preceding paragraph p35; queried all four official extension metadata. Fresh official records read for2.F4(2),2.F4(2).2,F4(2).2,E6(2),(2^2x3).2E6(2). The old F4 outer square-map error and E6 Unger2016 order91 correction are explicit. F4(3) web open failed, so root read actual ctoexce1.tbl provenance and release-history p15; peer retrieved and read the official1281-byte HTML. F4(3) is OBrien/Magma2024, added1.3.10May2025, not ATLAS. Specific accepted CTblLib1.3.11 tables are cited inputs, not freshly reconstructed original tables.',
  'research/exceptional_small_bibitems.tex; agents/imprimitive/audit_exceptional_small/PEER_AUDIT.md')]
with (R/'research/root_check_events.tsv').open('a',newline='') as f:
    w=csv.writer(f,delimiter='\t')
    for sid,typ,out,ev in events:
        w.writerow([sid,now,'/root','GPT-6 Astra Pro','inherited; not externally exposed','HODGE_DIVISION',typ,out,ev])

(R/'research/e825_root_review_in_progress.md').write_text('''# Root whole-proof review of E825 — completed

The initial416-line draft was read in full, and the explicit variable-row amendment and final428-line draft changes were read. The complete473-line final canonical TeX was then read, with whole mathematical PASS. Its frozen hash and the label-only integrated hash are recorded in e825_c2_exceptional_integration.json. The independent G34 report and its entire exact code were read in full. Both whole-proof audits pass.

The review explicitly checks the unital endomorphism map to R/I² and all free-factor products; the cyclic trace surviving off-diagonal mixing; variable normal and tangential derivatives of the row b; exact boundary terms; standard F comparison before determinant gluing; the7/2 coefficient; the first-overlap edge map's kernel/image scope; Koszul nonvanishing; and the two-plane primitive/mixed-block condition. The rational B step transports ordinary obstruction vanishing, not semiregularity. The author/root constant-row certificate and the peer's independent unrestricted derivative/exterior certificate are distinguished in the events.

This theorem excludes the flat adjusted determinant subcase and gives an explicit necessary condition for all local F^r plus free forms. Positive adjusted determinants can satisfy it. No balanced semiregular seed or universal added-free exclusion is claimed.
''')

p=R/'agents/imprimitive/odd_c2/STATUS.md';s=p.read_text()
s=s.replace('independent root and peer reviews are\npending.',
 'complete root and independent peer reviews have\npassed. The peer report is ODD_C2_PEER_AUDIT.md; only status text changed after the frozen mathematical audit.')
s+='\nRoot integration and final hashes: research/e825_c2_exceptional_integration.json.\n'
p.write_text(s)
p=R/'agents/imprimitive/odd_c2/manifest.json';d=json.loads(p.read_text())
d['status']='Complete author, root and independent peer whole-proof/source audits PASS; integrated'
d['integrated_at_utc']=now
d['canonical_proof_sha256']=canonical['agents/imprimitive/odd_c2/odd_c2_all_fields_section.tex']
d['canonical_finite_proof_sha256']=canonical['agents/imprimitive/odd_c2/finite_odd_c2_section.tex']
p.write_text(json.dumps(d,indent=2)+'\n')

p=R/'research/frameworks.tex';s=p.read_text()
s=s.replace('D-C3-01--03, D-A7-01--03,',
 'D-C3-01--03, D-A7-01--03, D-HOS, D-OC2, D-OC2-F, D-EXS,')
s=s.replace('SF-E811--824 concern','SF-E811--825 concern')
p.write_text(s)
with (R/'LEDGER.md').open('a') as f:
    f.write('\n## Three completed reductions: added free summands, odd C2 and exceptional small fields\n\n'+now+' — Q5y proved, Q2bi and Q2bj refuted; both Q5i and Q2i strictly reduced. SF-E825 gives a necessary first-overlap determinant condition for arbitrary added free summands and gluing; it excludes adjusted flat determinants from X but leaves positive adjusted determinants open. D-OC2 closes transitive ordinary odd PSp4(q),q>=5, in the nonselfdual-original source gate with either determinant. D-EXS closes arbitrary mixed F4(2),F4(3),E6(2),2E6(2) cores, including covers and all compatible normalizers. Every included proof has been read in full by its author/root and independent peer, with exact source scopes and distinct executed certificates. This integration is not an hourly review.\n')
with (R/'IMPLICATIONS.md').open('a') as f:
    f.write('''
## Added locally free summands retain a determinant obstruction

SF-E825 makes the first infinitesimal defect bundle intrinsic even under arbitrary mixing with free summands. Its canonical first-overlap trace imposes the simultaneous RM determinant condition. In the actual local unit-surface family this removes all flat adjusted determinant repairs and confines every remaining possible seed to the explicitly nonzero determinant class. The equation can be satisfied by positive determinant data; the theorem does not construct a weakly semiregular seed or exclude every added-free repair.

This is an obstruction to actual coherent sheaves/perfect complexes in DEG_L S-14/S-21, with exact local derived deformation and K-theoretic Chern-character identities. It narrows the potential cycle-supplier gate for condition A, cote16 scan050. It supplies no new condition-I positivity argument, cycle, Cayley-Hamilton projector or motivic L-value bound. The precise EGA/SGA/weight placements are the ones in the paper's common framework section.

## Further ordinary symplectic and exceptional sources are excluded

D-OC2-01--04 removes all transitive ordinary PSp4(q), oddq>=5, from the nonselfdual-original sixfold gate, with arbitrary scalar/outer actions, either determinant and potentially larger inducing field. The q3 endpoint remains exactly as in D-SPW. The finite theorem's partial universal-cover coverage atq7/9 is never silently enlarged; the complete ordinary unipotent restriction proof handles the all-q conclusion.

D-EXS-01--03 removes arbitrary mixed cores from F4(2),F4(3),E6(2),2E6(2), with every universal-cover central character and full normalizer. The exact million-spectrum certificate and actual Euler/Hurwitz factorization force a degree ceiling below the smallest possible factor. Original character tables are cited inputs with their respective ATLAS, corrected, Magma and central-construction provenance. Neither table consistency nor a parameter count is presented as dominance.

Both are restrictions on actual finite-cover weight-one variations and their representation-ring operations. They strictly narrow the condition-A supplier gate; they do not prove a negative Hodge statement or identify a ghost. Markman, Severn and032 retain their conditional status, and no new assertion about schemes over all of Spec Z or about motivic L-functions follows from these restrictions.
''')
out={'date_utc':now,'integrated':['SF-E825','D-HOS-01--02','D-OC2-F1--F2','D-OC2-01--04','D-EXS-01--03'],
     'whole_reviewed_sha256':frozen,'canonical_sha256':canonical,
     'bib_sha256':{n:sha(R/n) for n in bibs},
     'new_rows':{'Q5y':'proved','Q2bi':'refuted','Q2bj':'refuted'},
     'strictly_reduced_main_gates':['Q2i','Q5i']}
(R/'research/e825_c2_exceptional_integration.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
