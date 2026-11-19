"""Serialize manually adjudicated cross-package identity decisions.

No mathematical matching is performed by the script. Lookups below only copy
the already-read source identifiers and coordinates into the recorded decisions.
"""
from pathlib import Path
import json, hashlib, datetime, csv
O=Path(__file__).resolve().parents[1]
P=O.parent
BASE=O.parents[2]/'sources'
BASE=Path('/workspace/scratch/c38eb4e8f07f/sources')
files={'agent16':O/'SA18_items.json','agent45':P/'agent45/items.json','agent46':P/'agent46/items.json'}
items={a:{x['id']:x for x in json.loads(p.read_text())} for a,p in files.items()}
index={r['entry_id']:r for r in csv.DictReader((BASE/'SA18_notes/NOTES_INDEX.tsv').open(),delimiter='\t')}
def entry(e):
 row=index[e];path=BASE/'SA18_notes/pro'/f"{row['package']}_notes.md"
 lines=path.read_text().splitlines();heading=row['heading']
 starts=[i for i,s in enumerate(lines,1) if s.lstrip('# ').strip()==heading]
 if not starts:raise ValueError((e,heading))
 start=starts[0];end=next((i-1 for i in range(start+1,len(lines)+1) if lines[i-1].startswith('### ')),len(lines))
 return {'entry_id':e,'heading':heading,'notes_file':str(path.relative_to(BASE)),'start':start,'end':end}
F='SA18_texts/pro/MPL_16+47+54+44_transcription.tex'
endpoint_fourier={'file':F,'cote':47,'scans':[7,8],'start':2333,'end':2394,'specific_unfinished_line':2394}
endpoint_oda={'file':F,'cote':54,'scans':[7],'start':2714,'end':2733,'question_lines':[2727,2730]}
full=[]
def merge(owner,src,dst,endpoint,reason,preserve):
 si=items[owner][src];di=items['agent16'][dst]
 full.append({'action':'merge_full_item','from_owner':owner,'from_item':src,'to_item':dst,'to_claim':'CL-'+dst,
 'source_entries_to_move':si['sources'],'source_entry_evidence':[entry(e) for e in si['sources']],
 'existing_target_source_entries':di['sources'],'same_authored_endpoint':endpoint,'identity_reason':reason,
 'preserve_in_occurrence_or_reconstruction':preserve,'confidence':'high','new_archival_witness':False})
merge('agent45','SA18-45002','SA18-16050',endpoint_fourier,
 'Both assess the same specifically constructed Poincare direct-image morphism and the same unit-fibre compatibility left open at c47:8. The c45 exterior identities are mentioned only as possible tools, not as another authored question.',
 ['The exact morphism must be checked; matching exterior-power cohomology objects does not check it.','Preserve the bounded statement that the c45 exterior formulas do not complete that check.','The perfect-cone strategy belongs to the earlier run.'])
merge('agent45','SA18-45003','SA18-16050',endpoint_fourier,
 'The item gives the exact later-literature fate of the very same comparison-map obligation, not a separate c45 theorem. It can be included as the publication-comparison occurrence of the canonical question.',
 ['Laumon1.2.4–1.2.5 retain the determinant line and shift.','The opened Laumon passage recalls the morphism construction but does not write the requested unit-fibre calculation.','A published theorem and a second independent manuscript proof witness are different evidence.'])
merge('agent45','SA18-45004','SA18-16069',endpoint_oda,
 'This entry quotes the identical c54:7 A[p]-reconstruction question and matches it to OdaCor5.11. The c45 Lie/orthogonal material is a non-solution comparison, not an additional theorem in this item.',
 ['Use a perfect field of characteristicp and the full finite group scheme A[p].','Record contravariant Dieudonne convention and the Hodge submodule; do not suppress variance or p-operation matching.','Oda does not supply the unrelated c47 Fourier-map check.'])
merge('agent46','SA18-46003','SA18-16050',endpoint_fourier,
 'Entry#3 pinpoints the same unfinished c47 morphism; entry#4 records its exact Mukai/Laumon fate. The cote46 EGA plan gives no independent mathematical statement that would be lost in this merge.',
 ['Preserve the limited no-second-proof observation for the reviewed cote46 material.','Mukai is the field theorem; Laumon is the relative theorem with determinant line and shift.','The draft map check remains unwritten in the cited comparison passage.'])
partial=[{
 'action':'move_only_one_source_entry_and_its_abelian_comparison',
 'from_owner':'agent46','from_item':'SA18-46030','to_item':'SA18-16069','to_claim':'CL-SA18-16069',
 'source_entries_to_move':['MPL_46_002-048#42'],
 'source_entry_evidence':[entry('MPL_46_002-048#42')],
 'same_authored_endpoint':endpoint_oda,
 'identity_reason':'N40 gives the exact OdaCor5.11 counterpart of the same c54:7 A[p]-extension question.',
 'retain_from_item':True,
 'source_entries_to_retain':['MPL_46_002-048#43','MPL_46_002-048#44','MPL_46_002-048#45'],
 'retained_entry_evidence':[entry(e) for e in ['MPL_46_002-048#43','MPL_46_002-048#44','MPL_46_002-048#45']],
 'do_not_absorb':['Cor5.12 for Picard_X[p] of a general proper smooth X with a k-point and its iterated-Cartier-stable subspace.','The proposed ordinary/supersingular elliptic diagnostic.','The documentary warning that Oda thesis/publication dates do not date the undated manuscript leaves.'],
 'preserve_in_occurrence_or_reconstruction':['Full finite group scheme, not rational p-torsion points.','Perfect-field and contravariance qualifications.'],
 'confidence':'high'
}]
distinct=[]
def keep(owner,sources,targets,why):
 distinct.append({'action':'retain_distinct_link_only','owner':owner,'items':sources,
 'source_entries':{s:items[owner][s]['sources'] for s in sources},'related_agent16_items':targets,'reason':why})
keep('agent45',['SA18-45001'],['SA18-16050'],'A bounded negative corpus search over c45 is a separate documentary assertion; do not erase its reviewed-corpus boundary by identifying it with the c47 authored gap.')
keep('agent45',['SA18-45005'],['SA18-16072','SA18-16073','SA18-16076','SA18-16077','SA18-16078','SA18-16113'],'This is the bounded absence of the whole seven-theorem programme in c45, not one of the seven mathematical claims.')
keep('agent45',['SA18-45006','SA18-45066','SA18-45067'],[],'Folder chronology, headings and scan counts are package-specific documentary observations.')
keep('agent45',['SA18-45007'],['SA18-16115','SA18-16116'],'Torus/Borel classification has a thematic connection to the cancelled root draft; it neither repeats nor repairs the coroot-integrality claim.')
keep('agent45',['SA18-45008'],['SA18-16008','SA18-16072'],'The distinction between base Picard groups and Pic0/Albanese is a comparative scope statement, not a common construction.')
keep('agent45',['SA18-45010','SA18-45011'],['SA18-16071'],'Finite-order distributions and recovery from augmentation completion differ from graded I-adic completion.')
keep('agent45',['SA18-45012','SA18-45013','SA18-45014','SA18-45015','SA18-45016','SA18-45017','SA18-45018'],['SA18-16068','SA18-16069'],'Adjoint Lie deformation, cohomology and characteristic2 semisimple examples differ from the abelian restricted Hodge extension.')
keep('agent45',['SA18-45027','SA18-45028','SA18-45029'],['SA18-16115','SA18-16116'],'Torus isomorphisms, based root data and lifting ambient forms are not the cancelled finite-root-vector integrality argument.')
keep('agent45',['SA18-45038'],['SA18-16068'],'Infinitesimal solutions in an orthogonal-group chart are not the Hodge extension or its restricted p-operation.')
keep('agent45',['SA18-45055','SA18-45056'],['SA18-16008','SA18-16105','SA18-16106'],'Finite Kummer Pic(A)/2 for a base ring, and an undefined quadratic-form kernel, are different from the proper-surface l-adic NS/Brauer comparisons.')
keep('agent45',['SA18-45064','SA18-45065'],['SA18-16002','SA18-16051'],'General module-dual separation and exterior contraction identities are tools; they are neither the normalization mismatch nor the specific derived zero-section Koszul calculation.')
keep('agent46',['SA18-46002','SA18-46033'],['SA18-16044','SA18-16065','SA18-16072'],'The EGA plan and cancelled headings are documentary topic lists, not the transform, deRham or intermediate-Jacobian statements.')
keep('agent46',['SA18-46004'],['SA18-16072','SA18-16073','SA18-16077'],'It combines same-cote edition provenance and a multi-theorem concordance. No single mathematical item can absorb both assertions; the numbered claims remain separately linked.')
keep('agent46',['SA18-46005'],['SA18-16076','SA18-16077'],'The independently dated16August1964 letter asks about the Hodge/Neron–Tate relationship. It is a distinct historical occurrence/comparison, not an exact proof or repetition of the manuscript pencil-height identity. Do not merge it with the8August reference.')
keep('agent46',['SA18-46006'],['SA18-16072','SA18-16073'],'The31August1964 Mumford letter is a dated multi-claim parallel. Preserve the independent-witness and chronology analysis rather than force it into one mathematical item.')
keep('agent46',['SA18-46007'],['SA18-16076','SA18-16078'],'The1968 authorial reassessment is external later correspondence, not a withdrawal within the c44 source and not the same statement as either original claim.')
keep('agent46',['SA18-46008'],['SA18-16078'],'The1962 divisor-case precursor has codimension-one scope; it is not the ambiguous all-cycle equality at c44:6.')
keep('agent46',['SA18-46009'],['SA18-16050','SA18-16072','SA18-16073','SA18-16076','SA18-16077'],'The proposed witness/date/proof register is a research-method entry, not a mathematical theorem or one authored question.')
keep('agent46',['SA18-46024','SA18-46025','SA18-46026'],['SA18-16008','SA18-16069'],'Picard p-torsion line-bundle classes, dlog and Cartier-fixed forms on a general X differ from prime-to-p Brauer Tate modules and the entire Dieudonne module of an abelian variety.')
keep('agent46',['SA18-46027','SA18-46028'],['SA18-16068'],'The general cotangent/restricted-Lie dictionary and variable-coefficient transpose question differ from the particular abelian Hodge extension and its zero p-operation on a specified subgroup.')
keep('agent46',['SA18-46029'],['SA18-16067'],'Construction of Verschiebung with VF=p is not the mutual-annihilator statement for Frobenius kernels of dual abelian varieties.')
keep('agent46',['SA18-46031','SA18-46032'],['SA18-16017'],'Absolute/relative Frobenius topos comparisons and their converse are different from invariance under nilpotent thickenings.')
keep('agent46',['SA18-46034','SA18-46036','SA18-46037'],['SA18-16011','SA18-16012'],'Brauer–Severi splitting and Picard lifting obstructions are not the local surface discriminant/linking-pairing comparison.')
keep('agent46',['SA18-46045'],['SA18-16079','SA18-16115','SA18-16116'],'Coxeter graph/conjugacy theorems at c46:42,44,46 differ from arbitrary affine hyperplane arrangements at c54:8 and the cancelled c44:5 root draft. C44:7 lines2948–2964 contain editorial graph/root terminology only, not a second occurrence of the c46 theorems.')
keep('agent46',['SA18-46046'],['SA18-16009','SA18-16010'],'Divisible modules over a PID and the Baer criterion differ from Matlis decomposition and a point-supported injective sheaf.')
keep('agent46',['SA18-46054'],['SA18-16008','SA18-16011','SA18-16012'],'Topological/analytic torsion Brauer representability and fixed-degree projective representations differ from the algebraic surface Kummer and discriminant questions.')
keep('agent46',['SA18-46055'],['SA18-16109'],'Restriction-of-scalars cohomology and purely inseparable norm groups are not the same as the particular face-map complex of Gm cohomology in the reused fragment.')
keep('agent46',['SA18-46063','SA18-46065'],['SA18-16067','SA18-16068'],'General Cartier/Hopf duality and full functional distributions provide background, but not the specific abelian Frobenius-kernel pairing or Hodge extension.')
snapshot={a:{'file':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'item_count':len(items[a])} for a,p in files.items()}
for r in full:
 assert all(e in items[r['from_owner']][r['from_item']]['sources'] for e in r['source_entries_to_move'])
assert all(e in items['agent46']['SA18-46030']['sources'] for e in partial[0]['source_entries_to_move']+partial[0]['source_entries_to_retain'])
out={
 'reviewer':'GPT-6 Astra Pro / inherited effort / agent16','date':'2026-11-19','recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'status':'Completed manual identity review; parent applies accepted changes. No other owner files edited.',
 'scope':'All67 agent45 and67 agent46 item statements/reconstructions screened against103 agent16 items. Candidate indexed entries and their exact shared manuscript endpoints read directly.',
 'input_snapshot':snapshot,'merge_rule':'Merge only the same authored question and its exact publication comparison. Preserve distinct corpus searches, chronology, broader theorems, different quantifiers and comparative constructions.',
 'accepted_full_item_merges':full,'accepted_partial_entry_merges':partial,'retain_distinct_decisions':distinct,
 'other_items':'Remaining screened items have no candidate same-claim identity in agent16; retain them. This is not a judgment about cross-duplicates with the root or between agent45 and agent46.',
 'owner_feedback':{'agent45':'Explicitly agreed to all three proposed merges and retained distinctions via collaboration message.','agent46':'Proposal sent; response, if any, is recorded separately by the parent.'},
 'counts':{'foreign_items_screened':134,'target_items_screened':103,'full_item_merges':len(full),'partial_entry_merges':len(partial),'foreign_source_entries_moved':sum(len(r['source_entries_to_move']) for r in full+partial),'distinct_candidate_groups':len(distinct),'net_item_reduction_if_applied':len(full)},
 'c44_scan7_limit':{'file':F,'start':2948,'end':2964,'result':'Editorial terminology commentary; no Coxeter conjugacy theorem, no assigned writer/date.'}
}
(O/'cross_package_merge_review.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
(O/'outputs/cross_package_merge_counts.json').write_text(json.dumps(out['counts'],ensure_ascii=False,indent=2)+'\n')
events=[]
for r in full+partial:
 events.append({'statement_id':r['from_item'],'date':'2026-11-19','who':out['reviewer'],'type':'cross-package identity review','outcome':r['action']+' to '+r['to_item']+'. '+r['identity_reason']})
for r in distinct:
 for sid in r['items']:
  events.append({'statement_id':sid,'date':'2026-11-19','who':out['reviewer'],'type':'cross-package identity review','outcome':'Retain distinct. '+r['reason']})
for sid in ['SA18-16050','SA18-16069']:
 events.append({'statement_id':sid,'date':'2026-11-19','who':out['reviewer'],'type':'cross-package identity review','outcome':'Canonical endpoint checked against the exact foreign indexed entries; source-entry provenance and restrictions retained in cross_package_merge_review.json.'})
with (O/'cross_merge_CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(events)
print(json.dumps(out['counts'],ensure_ascii=False,indent=2))
