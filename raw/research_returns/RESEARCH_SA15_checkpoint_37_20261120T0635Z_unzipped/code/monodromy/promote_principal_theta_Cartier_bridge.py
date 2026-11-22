"""Promote only the fully audited principal theta/Cartier bridge."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re,difflib,csv

agent=Path(__file__).resolve().parents[1];work=agent.parents[1]
candidate=agent/'principal_theta_Cartier_bridge_candidate.tex'
expected='2f37d09805d4b0fff3d5b95f682b926ccb98dd128e7a6318dce61a5fb1405a7e'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(candidate)==expected
root_audit=work/'outputs/root_principal_theta_bridge_audit.json'
oc_audit=work/'agents/obstructions_crystals/principal_theta_Cartier_bridge_independent_audit.json'
assert root_audit.exists() and oc_audit.exists()
canonical=agent/'principal_theta_Cartier_bridge.tex';assert not canonical.exists()
text,count=re.subn(r'\\status\{Candidate[^}]*\}',lambda m:'\\status{Proved; independent audits passed.}',candidate.read_text())
assert count==5
old='All assertions await independent\nproof audit.'
assert old in text
text=text.replace(old,'The full parent proof and source audit passed at 01:27:55.333447 UTC\non 20 November 2026.  The full obstruction/crystal proof and source\naudit passed at 01:33:13.137653 UTC.  Both independently checked every\ngroup-scheme, descent, trace and representation step and freshly read\nthe stated primary sources.  No numerical experiment was required.\nThe exact candidate and both audit records remain retained.')
canonical.write_text(text)
changes=[]
def save_change(path,after,reason):
    before=path.read_text();assert before!=after
    stem='pre_principal_theta_Cartier_'+str(path.relative_to(work)).replace('/','__')
    saved=agent/'history'/stem;assert not saved.exists();saved.write_text(before)
    diff=saved.with_name(saved.name+'.diff')
    diff.write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile=str(saved.relative_to(work)),tofile=str(path.relative_to(work)))))
    path.write_text(after)
    changes.append({'path':str(path.relative_to(work)),'before':str(saved.relative_to(work)),'diff':str(diff.relative_to(work)),'reason':reason})
consolidate=work/'code/consolidate.py';before=consolidate.read_text()
anchor="   out.write('\\n\\\\input{sections/A_nonordinary_ppav_covectors}\\n')"
assert before.count(anchor)==1
addition="   principal_bridge=a/'monodromy/principal_theta_Cartier_bridge.tex'\n   if principal_bridge.exists() and '\\\\status{Candidate' not in principal_bridge.read_text():\n    out.write('\\n'+principal_bridge.read_text()+'\\n')\n"
save_change(consolidate,before.replace(anchor,addition+anchor),'Insert the independently audited principal Cartier bridge after the product calculation and before the general covector section.')
bib=agent/'references.bib';before=bib.read_text();after=before
def append_note(source,key,sentence):
    start=source.index('{'+key+',');end=source.index('\n}',start)
    segment=source[start:end];pos=segment.index('note={')+len('note={')
    depth=1;i=pos
    while depth:
        if segment[i]=='{':depth+=1
        elif segment[i]=='}':depth-=1
        i+=1
    return source[:start]+segment[:i-1]+' '+sentence+segment[i-1:]+source[end:]
after=append_note(after,'EdixhovenVanDerGeerMoonenAV','For the principal theta Cartier bridge on 20 November 2026, monodromy reread the retained original Theorem8.10 and Corollary8.14 with proofs pp116--117, Corollary8.20 p119, full discussion8.30--8.32 with proofs pp124--125, Theorem9.14 p133 and Corollary9.17 pp133--134. Parent and obstruction/crystal agents independently freshly opened and read these full original passages. The geometric-character basis sentence in Lemma8.31 is not used for local-local groups; the text supplies its universal-character and Hopf-ideal correction. No new numerical program or image-view claim is made.')
after=append_note(after,'BrionKumar2005','For the principal theta Cartier bridge, parent and obstruction/crystal agents freshly read the original passages1.3.4 and1.3.6--1.3.8 with their complete proofs on 20 November2026; monodromy reused the previously audited finite-Frobenius duality and coefficient-trace formulas. The proof uses relative duality trace, not the zero ordinary field trace of a purely inseparable extension.')
save_change(bib,after,'Append only exact newly completed primary-source access and the printed-character correction; preserve every earlier access statement.')
now=datetime.now(timezone.utc).isoformat()
labels=re.findall(r'\\label\{([^}]+)\}',candidate.read_text())
record={'status':'PROMOTED','actual_utc':now,'candidate':str(candidate.relative_to(work)),'candidate_sha256':expected,'canonical':str(canonical.relative_to(work)),'canonical_sha256':sha(canonical),'labels':labels,'root_audit':str(root_audit.relative_to(work)),'oc_audit':str(oc_audit.relative_to(work)),'changes':changes,'scope':'Principal f0 theta-square Cartier coefficient and conditional auxiliary-cover dual rank only; no full monodromy theorem or fixed-target conclusion.'}
(agent/'outputs/principal_theta_Cartier_bridge_promotion.json').write_text(json.dumps(record,indent=2)+'\n')
(agent/'outputs/checkpoint31_required_principal_bridge.json').write_text(json.dumps({'required':str(canonical.relative_to(work)),'canonical_sha256':sha(canonical),'note':'Parent creates CP31 preparer; no earlier preparer edited.'},indent=2)+'\n')
with (agent/'CHECK_EVENTS_post_CP16.tsv').open('a',newline='') as f:
    writer=csv.writer(f,delimiter='\t')
    for label in labels:writer.writerow([label,now,'/root/monodromy','PROMOTED-root-OC-full-proof-source-PASS',record['scope']])
with (agent/'post_CP16_notes.md').open('a') as f:
    f.write('\n## '+now+' — Principal theta Cartier bridge promoted\n\n'+record['scope']+' The exact candidate remains byte-identical. The canonical status and completed-audit paragraph are the only proof-text changes. Narrow consolidation and bibliography changes have exact prior files and diffs. The printed local-local character sentence is replaced by an explicit universal-character argument, not silently imported.\n')
assert sha(candidate)==expected
print(json.dumps(record,indent=2))
