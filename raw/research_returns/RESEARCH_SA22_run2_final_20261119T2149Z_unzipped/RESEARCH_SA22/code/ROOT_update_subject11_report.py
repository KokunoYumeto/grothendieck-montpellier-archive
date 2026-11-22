#!/usr/bin/env python3
"""Update report mappings after the audited subject11 integration."""
from pathlib import Path
from datetime import datetime, timezone
import json
root=Path(__file__).resolve().parents[1]
p=root/'code/update_report.py';text=p.read_text()
lines=text.splitlines()
new=('B.3;28 subjects and Pour mémoire',
 'Strongest proved catalogue statements supplied for all entries; two original-source obligations remain separately',
 'B:nori-finite-flat,B:nori-base-change-counterexample,B:Lie-comparison-counterexample,B:Lie-comparison-integral-counterexample,B:integral-affinization,B:unipotent-homotopy,B:formal-homotopy,C:piecewise-graph-category,C:piecewise-group-fullness,C:piecewise-group-algebraization,C:absolute-flat-piecewise,C:absolute-flat-group-algebraization,B:finite-Greenberg-piecewise,B:uniform-partition-obstruction,B:finite-cover-partition-obstruction,B:complete-Greenberg-points,B:perfect-Greenberg-cohomology,B:Witt-localization-witness',
 'Subject11 now has full finite-piecewise category/group-object comparisons, exact finite Greenberg realization, an explicit infinite partition obstruction persisting under finite-surjective additive sheafification, complete Greenberg points for arbitrary schemes, and perfect-test relative cohomology with smooth/finite-flat calculations. The modern sites, perfection, bounded-output and acyclicity hypotheses are explicit. These answer the permitted strongest-statement alternative; no equality of all historical sites or lexical identity of morcelés is asserted. The ordinary BLR functor alone is not equated with the archival partition functor. Subject15 likewise has precise Toën/Nori/Mondal–Reinecke statements and later-candidate refutations. Both original Gabber/Fujiwara source obligations remain in the next row. All28subjects and Pour-mémoire entries have exact locators and stated scopes.')
replaced=0
for i,line in enumerate(lines):
 if line.startswith("('B.3;28 subjects and Pour mémoire'"):
  lines[i]=repr(new)+',';replaced+=1
assert replaced==1,replaced
text='\n'.join(lines)+'\n'
old="extra={15:"
newextra="extra={11:',C:piecewise-graph-category,C:piecewise-group-fullness,C:piecewise-group-algebraization,C:absolute-flat-piecewise,C:absolute-flat-group-algebraization,B:finite-Greenberg-piecewise,B:uniform-partition-obstruction,B:finite-cover-partition-obstruction,B:complete-Greenberg-points,B:perfect-Greenberg-cohomology,B:Witt-localization-witness',15:"
if old in text:text=text.replace(old,newextra,1)
anchor="'- `notes/C_report.md`: algebra, inequalities and original-scan reading audit.',"
addition="'- `notes/ROOT_subject11_integration_audit.md` and the B/C Greenberg audits: exact category, partition, complete-point, relative-cohomology and source-coordinate checks; all historical limits retained.',"
if addition not in text:
 assert anchor in text
 text=text.replace(anchor,anchor+addition)
anchor="'Detailed A567 and PartC corrections retain every additional source file and line locator in the appended reports."
correction="'7. Corrected primary source arXiv1311.0051v6, Section2.3 pp8–9 and Remark18.3 pp99–100: the printed Witt tuple lies in the localization under the source\'s standard coordinates. B:Witt-localization-witness supplies a correct excluded tuple and full universal proof. The valid strict-localization assertion and corrected infinite Greenberg theorem remain intact. The source-specific note and147-check certificate are retained.','', "
# Keep the apostrophe inside a Python string literal properly escaped.
correction=repr("7. Corrected primary source arXiv1311.0051v6, Section2.3 pp8–9 and Remark18.3 pp99–100: the printed Witt tuple lies in the localization under the source's standard coordinates. B:Witt-localization-witness supplies a correct excluded tuple and full universal proof. The valid strict-localization assertion and corrected infinite Greenberg theorem remain intact. The source-specific note and147-check certificate are retained.")+",'', "
if '7. Corrected primary source arXiv1311.0051v6' not in text:
 assert anchor in text
 text=text.replace(anchor,correction+anchor)
p.write_text(text)
compile(text,str(p),'exec')
out={'updated_utc':datetime.now(timezone.utc).isoformat(),'outcome_mapping_updated':True,'subject11_extra_statement_labels':11,'remaining_required_original_sources':2}
(root/'logs/ROOT_update_subject11_report.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
