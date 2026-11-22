"""Retain a separate general-source candidate; never change the earlier file."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, difflib, re

root=Path(__file__).resolve().parents[3]
own=root/'agents/obstructions_crystals'
src=own/'post_CP33_odd_source_twisted_Cartier_candidate.tex'
dst=own/'post_CP33_general_odd_source_Cartier_candidate.tex'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(src)=='23d71c99b04ca054522b645d2d7c0eae0a3375ba660220d854d0dbca2c9c6599'
assert not dst.exists()
old=src.read_text()
s=old
replacements=[
('% Isolated post-CP33 candidate. No canonical or checkpoint-input mutation.',
 '% Separate arbitrary odd-source generalization; earlier narrower candidate retained.'),
(r'\subsection{Odd-source twisted Cartier blocks and the residual quotient}',
 r'\subsection{Twisted Cartier blocks for arbitrary odd cubic pullbacks}'),
(r'\begin{lemma}[Twisted blocks on every odd principal-cube source]',
 r'\begin{lemma}[Twisted blocks on an arbitrary odd cubic pullback]'),
('Let \\((B,\\Theta_B)\\) be a nonordinary principally polarized abelian\nsurface, let \\(e\\) be a positive odd integer, and set \\(M=\\mathcal O_B(3e\\Theta_B)\\),\n\\(h=9e^2\\). For any nontrivial odd-order \\(P\\in\\operatorname{Pic}^0(B)\\),',
 'Let \\((C,\\Theta_C)\\) be a nonordinary principally polarized abelian\nsurface and set \\(N=\\mathcal O_C(3\\Theta_C)\\). Let\n\\(\\eta:B\\to C\\) be an etale isogeny of positive odd degree \\(a\\),\nand put \\(M=\\eta^*N\\), \\(h=9a\\). The surface \\(B\\) need not\ncarry a principal polarization. For every nontrivial odd-order\n\\(P\\in\\operatorname{Pic}^0(B)\\),'),
('More precisely, choose an outgoing etale quotient\n\\(\\eta:B\\to C\\) of degree \\(e^2\\) with\n\\(M=\\eta^*N\\), \\(N=\\mathcal O_C(3\\Theta_C)\\).\nFor any finite collection of such \\(P\\), all the determinants in',
 'More precisely, for any finite collection of such \\(P\\), all the\ndeterminants in'),
('The outgoing quotient and symmetric descent are exactly those of\nCorollary~\\ref{cor:fixed-ppav-all-odd-maximal-dual-Cartier}.\nWrite',
 'Use the isogeny and cubic principal line bundle in the hypotheses.\nWrite'),
('where this finite group has odd order \\(e^2\\).',
 'where this finite group has odd order \\(a\\).'),
('In the notation of the lemma, suppose the degree-\\(e\\) relative\ngeometric image on \\(|M|\\) is',
 'In the notation of the lemma, suppose the relative geometric image\non the complete system \\(|M|\\) is'),
('The preceding proposition applies with \\(h=9e^2\\) and \\(n=m^2\\),\nand proves (DE-OS7).',
 'Apply the outgoing quotient theorem also to the positive odd\nsource degree \\(e\\) on \\(B\\): it writes\n\\(\\mathcal O_B(3e\\Theta_B)=\\eta^*N\\) with \\(N\\) cubic principal\nand \\(\\deg\\eta=e^2\\). The preceding proposition then applies\nwith \\(a=e^2\\), \\(h=9e^2\\), and \\(n=m^2\\), proving (DE-OS7).'),
]
for x,y in replacements:
    assert s.count(x)==1, x
    s=s.replace(x,y)
for x,y in [
 ('lem:DE-odd-source-twisted-blocks','lem:DE-general-odd-source-twisted-blocks'),
 ('prop:DE-full-odd-source-quotient-bound','prop:DE-general-odd-source-quotient-bound'),
 ('cor:DE-known-odd-divisor-quotient-bound','cor:DE-general-source-principal-divisor-bound'),
 ('rem:DE-odd-source-restriction-scope','rem:DE-general-odd-source-scope'),
 ('DE-OS','DE-GOS'),
]:
    s=s.replace(x,y)
assert 'degree-\\(e\\) relative' not in s
assert 'order \\(e^2\\)' not in s
with dst.open('x') as f:f.write(s)
h=own/'notes/CP34_general_odd_source_derivation'
h.mkdir(exist_ok=False)
(h/'narrower_source.tex').write_bytes(src.read_bytes())
(h/'generalization.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),s.splitlines(True),fromfile=src.name,tofile=dst.name)))
labels=re.findall(r'\\label\{((?:lem|prop|cor|rem):[^}]+)\}',s)
assert len(labels)==4
now=datetime.now(timezone.utc).isoformat()
record={'status':'COMPLETE GENERAL CANDIDATE; full independent audits pending',
        'actual_utc':now,'candidate':str(dst.relative_to(root)),'candidate_sha256':sha(dst),
        'labels':labels,'narrower_candidate':str(src.relative_to(root)),'narrower_sha256':sha(src),
        'scope':'Any odd etale cubic pullback source eta:B→C of degree a, with C principal nonordinary. Exact twisted blocks and common central Fermat wall; conditional full source gives quotient dimension at least9a−1. No full image for the new nonprincipal source is inferred.',
        'direct_dependencies':['agents/obstructions_crystals/A4_Lang_deck_slice_bound.tex','agents/obstructions_crystals/A4_common_Cartier_incidence.tex','agents/monodromy/ppav_all_odd_full_root_inertia.tex','agents/monodromy/ppav_twisted_Cartier_Moore.tex'],
        'computation':'No numerical computation needed; this retained program only produces the precisely scoped separate draft.'}
with (own/'general_odd_source_Cartier_candidate_record.json').open('x') as f:json.dump(record,f,indent=2);f.write('\n')
print(json.dumps(record,indent=2))
