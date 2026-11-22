"""Record newly read primary passages and consolidate the duplicate source row."""
from pathlib import Path
import datetime,difflib,hashlib,json,re
w=Path(__file__).resolve().parents[1]
snap=w/'notes/sources30_before_update';assert not snap.exists();snap.mkdir()
bib=w/'notes/root_references.bib';before=bib.read_text()
late=w/'notes/late_source_census.json';late_before=late.read_text()
(snap/bib.name).write_text(before);(snap/late.name).write_text(late_before)
entries=re.split(r'(?=^@)',before,flags=re.M)
replacement=r'''@article{KnutsenLelliChiesa2020GenusTwo,
 author={Knutsen, Andreas Leopold and Lelli-Chiesa, Margherita},
 title={Genus two curves on abelian surfaces},
 journal={Annales Scientifiques de l'Ecole Normale Superieure},
 volume={55}, number={4}, pages={905--918}, year={2022},
 doi={10.24033/asens.2508}, eprint={1901.07603}, archivePrefix={arXiv},
 url={https://arxiv.org/pdf/1901.07603},
 note={Opened original arXiv v3, 6 July 2020, 12 pages; final journal metadata checked separately. Read the introduction through Theorems 1.1--1.4, complete Section 2.1 setup, Section 2.2 odd reduction, and complete Lemma 2.1 proof in Section 2.3. Section 3 and its full main proof were not newly audited. These are general complex-surface results, not every fixed nonordinary characteristic-two surface; no theorem is imported into that gate. Earlier institutional 403 and JavaScript-wall failures are retained in the logs; the original arXiv text was subsequently obtained.}
}

'''
matches=[i for i,x in enumerate(entries) if x.startswith('@misc{KnutsenLelliChiesa2020GenusTwo,')]
assert len(matches)==1,matches
entries[matches[0]]=replacement
new=''.join(entries)
assert 'RainsSam2019LateLead,' not in new and 'OzmanPries2017Prym,' not in new
new+=r'''
@article{RainsSam2019LateLead,
 author={Rains, Eric M. and Sam, Steven V.},
 title={Vector bundles on genus 2 curves and trivectors},
 journal={Algebraic Geometry}, volume={6}, number={3}, pages={328--345},
 year={2019}, doi={10.14231/AG-2019-016},
 url={https://content.algebraicgeometry.nl/2019-3/2019-3-016.pdf},
 note={Opened original 18-page publisher PDF. Latest root reading: introduction pp.328--329; Proposition 2.5 and proof p.330; Lemma 2.6, Proposition 2.7 and Corollary 2.8 p.331; Lemma 2.9 and Proposition 2.10 p.332; complete Lemma 5.7 and Remark 5.8 pp.341--342; Appendix A setup, Theorem A.1 and its full proof, and full Lemmas A.3, A.5, A.6 pp.342--344. The short Theorem 5.4 proof was read but explicitly excludes characteristic two; its dependencies 4.3/4.4 were not fully audited in this pass. Earlier read scopes are retained in the source logs. No identification with the higher-theta Cartier pairing or nonproduct twisted cross determinant is asserted; no theorem from this paper is imported into that monodromy route.}
}

@misc{OzmanPries2017Prym,
 author={Ozman, Ekin and Pries, Rachel},
 title={Ordinary and almost ordinary Prym varieties},
 year={2017}, eprint={1502.05959}, archivePrefix={arXiv},
 doi={10.48550/arXiv.1502.05959},
 url={https://arxiv.org/pdf/1502.05959},
 note={Opened original arXiv v3, 28 April 2017, 21 pages. Read the introduction and Theorem 1.1; complete Lemma 3.7 proof pp.6--7; complete Propositions 4.3, 4.4 and Theorem 4.5 proofs pp.10--11; and Section 8 pp.17--18. The cited moduli/monodromy and Raynaud dependencies were not all independently read. The generic p-rank-stratum theorem does not establish the needed statement for the linear system on a fixed abelian surface; no theorem is imported into that gate. Journal metadata are not asserted for this inspected preprint version.}
}
'''
bib.write_text(new)
rows=json.loads(late_before)
removed=[r for r in rows if r['key']=='KnutsenLelliChiesa2022LateLead']
assert len(removed)==1
rows=[r for r in rows if r['key']!='KnutsenLelliChiesa2022LateLead']
late.write_text(json.dumps(rows,indent=2)+'\n')
(snap/'root_references.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),new.splitlines(True),fromfile='before',tofile='after')))
record={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Bibliographic/access recording only; no mathematical claim promoted.',
 'root_bibliography_sha256':hashlib.sha256(bib.read_bytes()).hexdigest(),
 'new_primary_entries':['RainsSam2019LateLead','OzmanPries2017Prym'],
 'updated_primary_entry':'KnutsenLelliChiesa2020GenusTwo',
 'removed_duplicate_census_row':removed,
 'removal_reason':'The historical Knutsen lead duplicated the now precisely updated canonical bibliographic row. Its original wording is preserved in sources30_before_update/late_source_census.json and earlier checkpoints; failed retrieval history and exact new reading scope are preserved in the canonical entry and root logs.'}
(w/'outputs/sources30_update.json').write_text(json.dumps(record,indent=2)+'\n')
with(w/'notes/checkpoint30_changes.md').open('a') as f:
 f.write('\n### Exact source-record update\n\n'
  'The Rains--Sam2019 and Ozman--Pries2017 primary reading scopes are now explicit bibliography entries. '
  'The Knutsen--Lelli-Chiesa entry now uses the verified2022 publication metadata while identifying '
  'the inspected2020 arXiv version and the exact Section2 proof scope. Its duplicate late-lead '
  'census row is consolidated into that canonical entry; the original row, all failed retrieval '
  'history and the exact bibliography diff are retained in notes/sources30_before_update. '
  'No theorem is imported from these comparison readings.\n')
print(json.dumps(record,indent=2))
