"""Retain actual Moore/Pfaffian search and original-source reading scope."""
from pathlib import Path
import datetime,difflib,hashlib,json
w=Path(__file__).resolve().parents[1]
folder=w/'notes/CP36_Moore_source_scope';assert not folder.exists();folder.mkdir()
p=w/'notes/root_references.bib';before=p.read_text()
entries=r'''
@misc{GrossPopescu1997MooreScope,
 author={Gross, Mark and Popescu, Sorin},
 title={Equations of $(1,d)$-polarized Abelian Surfaces},
 year={1997}, howpublished={arXiv:alg-geom/9609001v2},
 url={https://arxiv.org/pdf/alg-geom/9609001},
 note={Opened original version2,5March1997: introduction and complex-field scope; full Corollary2.8 and its proof, Corollary2.9, and Example2.10, printed pp17--19. Used only as a literature lead for Moore matrices; no arbitrary-parameter or characteristic-two maximal-rank conclusion is imported.}
}
@misc{Fisher2008PfaffianScope,
 author={Fisher, Tom}, title={Pfaffian presentations of elliptic normal curves},
 year={2008}, howpublished={Author preprint, revised January2008},
 url={https://www.dpmms.cam.ac.uk/~taf1000/papers/pfaffians.pdf},
 note={Opened cached author original after two direct retrieval failures. Read introduction, Definition1.6 and Theorems1.5/1.7 statements; complete Lemmas3.1,3.3--3.5, Proposition3.7 and Lemma3.8 proofs, printed pp7--10. Its elliptic-curve Klein matrix is not identified with an arbitrary Cartier tensor here; no such transfer is claimed.}
}
'''
assert 'GrossPopescu1997MooreScope' not in before and 'Fisher2008PfaffianScope' not in before
after=before+entries
(folder/'root_references.before.bib').write_text(before)
(folder/'root_references.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before',tofile='after')))
p.write_text(after)
r={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'queries':['skew Moore matrix Heisenberg alternating matrix generic rank prime polarization','Heisenberg invariant space alternating matrices constant bounded rank Pfaffian odd prime characteristic two','"Moore matrices" "Heisenberg" Gross Popescu','"skew" "Moore" "matrix" "abelian" Pfaffians','Tom Fisher Pfaffian presentations elliptic normal curves theorem 1.7 arxiv'],
 'query_scope':'Routine search followed by stronger primary-source search; no secondary-source theorem is used.',
 'Gross_Popescu':{'url':'https://arxiv.org/pdf/alg-geom/9609001','refs':['turn684370758view0','turn586465940view1','turn457004200view1'],'actually_read':'Introduction and complex-field setup; complete Corollary2.8 proof, Corollary2.9 and Example2.10, printed pp17-19.','use':'Literature comparison only; no characteristic2 transfer.'},
 'Fisher':{'url':'https://www.dpmms.cam.ac.uk/~taf1000/papers/pfaffians.pdf','refs':['turn472321284view0','turn415345994view0','turn415345994view1'],'actually_read':'Introduction, Definition1.6, Theorems1.5/1.7 statements; complete Lemmas3.1,3.3-3.5, Proposition3.7 and Lemma3.8 proofs, pp7-10.','use':'Klein-matrix source lead only; arbitrary Cartier coefficients are not supplied by its elliptic-curve hypothesis.'},
 'retrieval_failures':[
  {'ref':'turn235169109view0','url':'https://www.dpmms.cam.ac.uk/~taf1000/papers/pfaffians.pdf','outcome':'400 timeout'},
  {'ref':'turn684370758view1','url':'https://www.dpmms.cam.ac.uk/~taf1000/papers/pfaffians.pdf','outcome':'502 bad gateway'},
  {'ref':'turn586465940view0','url':'https://www.dpmms.cam.ac.uk/~taf1000/papers/pfaffenc.pdf','outcome':'400 timeout'},
  {'ref':'turn457004200view0','url':'https://www.dpmms.cam.ac.uk/~taf1000/research.html','outcome':'400 timeout'}],
 'successful_fallback':'Opening indexed original ref turn227719054search12 succeeded.',
 'no_new_theorem_imported':True,'no_gate_change':True,'no_novelty_claim':True,
 'before_sha256':hashlib.sha256(before.encode()).hexdigest(),'after_sha256':hashlib.sha256(after.encode()).hexdigest(),
 'nonmathematical_edit_failure':'Initial combined apply_patch was rejected before mutation because it both deleted and added update_current36.py. Reissued as separate add/update operations; no mathematical program was run in that failed call.'}
(folder/'record.json').write_text(json.dumps(r,indent=2)+'\n')
with (w/'notes/ROOT_SEARCH_LOG_36.md').open('a') as f:
 f.write('\n## Moore and Klein matrix literature\n\nRoot searched both engines for Heisenberg alternating tensors, generic prime-size rank and Moore matrices. Gross--Popescu original version2 and the Fisher cached author preprint were opened. Exact theorem and proof read scopes, URLs and failed retrievals are in notes/CP36_Moore_source_scope/record.json and the marked bibliography entries. Neither source supplies the arbitrary-coefficient characteristic-two multiplication-rank assertion being investigated. No gate changes from this search.\n')
print(json.dumps({'status':'PASS','actual_utc':r['actual_utc'],'sources_added':2,'scope':'Actual original-source read scope; no new theorem imported'},indent=2))
