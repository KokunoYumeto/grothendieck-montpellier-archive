"""Record exact source access for the explicitly unpromoted primitive route."""
from pathlib import Path
import datetime,difflib,hashlib,json
w=Path(__file__).resolve().parents[1]
folder=w/'notes/CP35_primitive_source_scope';assert not folder.exists();folder.mkdir()
bib=w/'notes/root_references.bib';before=bib.read_text()
(folder/'root_references.before.bib').write_text(before)
entries=r'''
@misc{Sun2006FrobeniusFiltration,
 author={Sun, Xiaotao},
 title={Stability of direct images under {Frobenius} morphism},
 year={2006},
 eprint={math/0608043},
 archivePrefix={arXiv},
 url={https://arxiv.org/pdf/math/0608043},
 note={Opened: arXiv v2, 18 August 2006; complete higher-dimensional canonical-filtration proof, Definition 3.1, Lemmas 3.2, 3.3, 3.5, Definition 3.4 and Theorem 3.6, printed pp. 5--9. Used only in an explicitly unpromoted primitive-polarization research route. The curve stability theorem is not imported in dimension two.}
}
@misc{CataneseSernesi2022HesseScope,
 author={Catanese, Fabrizio and Sernesi, Edoardo},
 title={The {Hesse} pencil and polarizations of type $(1,3)$ on {Abelian} surfaces},
 year={2022},
 eprint={2212.14877},
 archivePrefix={arXiv},
 url={https://arxiv.org/pdf/2212.14877},
 note={Opened for scope only: v1 introduction, Theorem 0.1 statement and bibliography. No characteristic-two theorem or complete proof was imported; no whole-paper audit claimed.}
}
'''
for key in ['Sun2006FrobeniusFiltration','CataneseSernesi2022HesseScope']:
 assert key not in before
after=before+entries;bib.write_text(after)
(folder/'references.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before.bib',tofile='after.bib')))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={
 'actual_record_utc':now,
 'queries':[
  'Frobenius direct image line bundle abelian variety stable Euler characteristic coprime rank',
  'abelian surface type (1,3) characteristic 2 Cartier Hasse Witt monodromy',
  'Frobenius abelian line bundle stable direct image',
  'Frobenius abelian coprime Euler'],
 'query_scope':'First two queries used the routine search engine; stronger follow-up queries used the other search engine. The first batched result was partly truncated; only visible results informed follow-up. Search snippets alone were not used as proof.',
 'sun':{'url':'https://arxiv.org/pdf/math/0608043','version':'v2,18 August2006','read':'Introduction and complete higher-dimensional filtration proof: Definition3.1, Lemmas3.2,3.3,3.5, Definition3.4, Theorem3.6, printed pp5-9.','refs':['turn494745992view0','turn567682745view0','turn567682745view1'],'use':'Canonical Frobenius filtration in the explicitly unpromoted primitive type(1,3) route only. No dimension-two stability theorem is inferred from the curve theorem.'},
 'catanese_sernesi':{'url':'https://arxiv.org/pdf/2212.14877','version':'v1','read':'Introduction, Theorem0.1 statement, bibliography; a text search for characteristic returned no match.','refs':['turn494745992view1','turn567682745view2','turn567682745view3'],'use':'Search/scope record only; no characteristic-two result imported and no complete proof read.'},
 'research_note':'notes/ROOT_primitive_1_3_route.md',
 'gate_change':False,'novelty_claim':False,
 'before_sha256':hashlib.sha256(before.encode()).hexdigest(),
 'after_sha256':hashlib.sha256(after.encode()).hexdigest()}
(folder/'record.json').write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/ROOT_SEARCH_LOG_35.md').open('a') as f:
 f.write('\n## Primitive-polarization route: original filtration proof and scope search\n\nRecorded at '+now+'. The exact four queries and access locators are in notes/CP35_primitive_source_scope/record.json. Sun\'s complete higher-dimensional canonical-filtration proof (Definition3.1, Lemmas3.2/3.3/3.5, Theorem3.6, arXiv:math/0608043v2, printed pp5–9) was opened. It supplies the filtration used in the saved research route; its curve stability theorem is not applied to a surface. The proposed surface stability proof is written separately through saturated subquotients of a unipotent bundle.\n\nCatanese–Sernesi, arXiv:2212.14877v1, was opened only for its introduction, Theorem0.1 statement and bibliography. No characteristic2 theorem or proof was imported. The first query output was partly truncated; no claim is based on unread output. Both exact bibliography entries and their prior file/diff are retained. This source work and the unpromoted primitive-system outline change no current gate.\n')
with (w/'notes/checkpoint35_changes.md').open('a') as f:
 f.write('\n## Retained primitive-system route and source scope\n\nThe live primitive type(1,3) note contains the full candidate stability and nonzero-Cartier arguments, with generic separability separated from the still unresolved smooth-member/full-wall witness. Sun\'s original higher-dimensional filtration proof was opened completely; a type(1,3) discriminant paper was inspected for scope only. Exact queries, access limitations, bibliography changes and the unpromoted note are retained. No source-only or conditional-outline progress is counted as an hourly gate reduction.\n')
print(json.dumps({'status':'RECORDED','actual_utc':now,'new_entries':2,'gate_change':False},indent=2))
