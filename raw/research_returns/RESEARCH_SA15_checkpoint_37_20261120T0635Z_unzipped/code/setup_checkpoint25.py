"""Create the immutable CP25 preparation workflow; no mathematical calculation."""
from pathlib import Path
w = Path(__file__).resolve().parents[1]
required = [
    'agents/obstructions_crystals/A3_mixed_positive_index_residual_boundary.tex',
    'agents/monodromy/nonordinary_good_theta_norm_transfer.tex',
    'agents/reduction_descent/B_middle_tame_quotient.tex',
    'agents/reduction_descent/B_tame_irreducible_arbitrary_index.tex',
    'agents/reduction_descent/B_initial_tame_sector.tex',
]
p = w / 'code/consolidate.py'
s = p.read_text()
needle = "                 'obstructions_crystals/A3_mixed_positive_index_smooth_pencil.tex',"
assert needle in s
s = s.replace(needle, needle + "\n                 'obstructions_crystals/A3_mixed_positive_index_residual_boundary.tex',")
needle = "                  'monodromy/nonordinary_uniform_five_theta_geometry.tex']:"
assert needle in s
s = s.replace(needle, "                  'monodromy/nonordinary_uniform_five_theta_geometry.tex',\n                  'monodromy/nonordinary_good_theta_norm_transfer.tex']:")
needle = "                    'B_p5_e12_high_quotient.tex']:"
assert needle in s
s = s.replace(needle, "                    'B_p5_e12_high_quotient.tex',\n                    'B_middle_tame_quotient.tex',\n                    'B_tame_irreducible_arbitrary_index.tex',\n                    'B_initial_tame_sector.tex']:")
s = s.replace('\\\\path{notes/ROOT_SEARCH_LOG_24.md}\nrecord',
              '\\\\path{notes/ROOT_SEARCH_LOG_24.md}, and\n\\\\path{notes/ROOT_SEARCH_LOG_25.md}\nrecord')
p.write_text(s)
for name in ['prepare_checkpoint', 'finalize_checkpoint', 'archive_checkpoint', 'verify_program_paths']:
    src = w / 'code' / f'{name}24.py'
    dest = w / 'code' / f'{name}25.py'
    assert not dest.exists()
    t = src.read_text().replace('checkpoint24', 'checkpoint25').replace('checkpoint_24', 'checkpoint_25')
    t = t.replace('Checkpoint24', 'Checkpoint25').replace('CP24', 'CP25')
    t = t.replace('qa24', 'qa25').replace('current24', 'current25').replace('paths24', 'paths25')
    if name == 'prepare_checkpoint':
        a = t.index('required=')
        b = t.index('for rel in required:', a)
        t = t[:a] + 'required=' + repr(required) + '\n' + t[b:]
    elif name == 'archive_checkpoint':
        t = t.replace('20:50:40', '21:35:40').replace("'24'", "'25'")
        t = t.replace('after final QA and actual review16', 'after final QA; actual review16 already recorded')
    elif name == 'finalize_checkpoint':
        t = t.replace('checkpoint_23.zip', 'checkpoint_24.zip').replace("'checkpoint':24", "'checkpoint':25")
        t = t.replace('since checkpoint23', 'since checkpoint24')
        t = t.replace(
            'Checkpoint25 is archived only at or after20:50:40UTC and only after actual hourly review16 has been recorded. Review16 must execute at or after its scheduled20:50:40UTC time. The following hourly review is due21:50:40UTC and checkpoint25 is due21:35:40UTC. No early review or early archive is represented as completed.',
            'Checkpoint25 is archived only at or after21:35:40UTC. Actual review16 was recorded20:50:41.784886UTC, with movement and zero no-movement streak. The next actual review17 is due21:50:40UTC and checkpoint26 is due22:20:40UTC. No early review or early archive is represented as completed.')
        t = t.replace(
            'The current proved additions are the even sum-of-two-odd-degree theorem, the bounded nodal five-self-isogeny construction, the exact mixed cyclic threshold and the newly closed height-two inertia indices. General A.3/A.4, the primitive mixed rank gate, higher-dimensional B.3 and other exact B.4 indices stay open. Actual review16 is recorded separately at or after20:50:40UTC.',
            'The current proved additions include arbitrary good-theta odd norm transfer, every fixed f0 degree3^i5^j and two-term even sum, the exact middle ramification index, arbitrary p-prime irreducible-residual recovery, and the exact initial tame height-two sector. The residual-pencil boundary is an exact identification, without a nonvanishing theorem. General A.3/A.4, the primitive mixed rank gate, higher-dimensional B.3 and other exact B.4 indices stay open. Actual review17 remains due21:50:40UTC; this snapshot is not that review.')
    dest.write_text(t)
src = w / 'code/render_qa24.py'
dest = w / 'code/render_qa25.py'
assert not dest.exists()
dest.write_text(src.read_text().replace('CP24', 'CP25').replace('checkpoint24', 'checkpoint25').replace('qa24', 'qa25'))
bib = w / 'notes/root_references.bib'
b = bib.read_text()
assert 'KnutsenLelliChiesa2020GenusTwo' not in b and 'DolgachevLehavi2008Isogenous' not in b
b += r'''
@misc{KnutsenLelliChiesa2020GenusTwo,
 author={Knutsen, Andreas Leopold and Lelli-Chiesa, Margherita},
 title={Genus two curves on abelian surfaces},year={2020},
 eprint={1901.07603},archivePrefix={arXiv},
 url={https://arxiv.org/pdf/1901.07603},
 note={Opened original arXiv v3, 6 July 2020. Theorems 1.1--1.4 and Section 2 scope/reduction read. These are general complex-surface results; not applied to the fixed characteristic-two neighbour gate. No complete new audit of Section 3 is claimed. Initial institutional PDF access failed with 403; arXiv original succeeded.}
}
@misc{DolgachevLehavi2008Isogenous,
 author={Dolgachev, Igor and Lehavi, David},
 title={On isogenous principally polarized abelian surfaces},year={2008},
 eprint={0710.1298},archivePrefix={arXiv},
 url={https://arxiv.org/pdf/0710.1298},
 note={Opened original arXiv v3, 8 March 2008. Introduction and Theorem 1.1 read for applicability. The ground characteristic is explicitly different from two, so no theorem is imported into the present characteristic-two gate. Author-site attempts failed with redirected 500 and direct 404 before arXiv succeeded.}
}
'''
bib.write_text(b)
print('Prepared CP25 workflow and five audited-file inclusion slots. Archive time gate is21:35:40UTC.')
