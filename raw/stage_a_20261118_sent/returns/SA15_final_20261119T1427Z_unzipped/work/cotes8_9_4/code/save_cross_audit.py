"""Record the completed independent targeted review of the root proof audit."""
import csv
import hashlib
import json
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
ROOT=BASE.parent/'root_review'
who='GPT-6 Astra Pro; effort setting not exposed; SA15-20261119/cotes8_9_4'
checks={
 'P78-C001': ('§1', 'The cartesian coefficient condition gives quotient transition maps on affine sections and hence a countable surjective Mittag–Leffler system. The local algebra is checked; the whole site comparison is not independently re-proved.'),
 'P78-C002': ('§1', 'The distinction between levelwise acyclicity and totalization is correct. The stated boundedness or derived-totalization qualification is necessary; this is a scope check, not an independent proof of the global comparison.'),
 'P78-C004': ('§1', 'For I⊂J with J/I nilpotent, J^a⊂I gives J^(an)⊂I^n⊂J^n. The completions agree by cofinality. This checks only the completion lemma, not the entire equivalence of infinitesimal topoi.'),
 'P78-C012': ('§2', 'The closed-disc series has coefficients tending to zero, while its forced antiderivative has infinitely many coefficients equal to one. The failure of global surjectivity is valid. It does not decide a Poincaré lemma in an unspecified finer topology.'),
 'P78-C014': ('§3', 'The cohomology modules alone do not specify the attaching Ext² class of a two-term object. The proof correctly declines to reconstruct the proposed general functor from its two cohomology sheaves.'),
 'P78-C016': ('§3', 'Matching cohomology objects and separate distinguished triangles does not automatically supply compatibility of the maps between them. The audit retains this missing datum.'),
 'P78-C017': ('§3', 'The consecutive-composition axiom applies within one distinguished triangle. It does not force a Yoneda product of connecting maps from different triangles to vanish. No numerical value is assigned to the unidentified product.'),
 'P78-C022': ('§3', 'For α_p, F=V=0 gives ker F of dimension one and im V=0, so the BT1 restriction matters. Multiplication by ε over k[ε]/ε² is nonzero but its ordinary Frobenius pullback is zero. The latter example is correctly limited to the ordinary pullback functor.'),
 'P78-C023': ('§4', 'The relative fiber complex and its shift convention separate automorphisms, deformations and obstructions. Merely naming Ext⁰ does not establish its vanishing. No counterexample to an undefined geometric functor is claimed.'),
 'P78-C027': ('§5', 'Under the specified global-to-finite-local Kummer interpretation, even valuations reduce a locally square rational number to ±r², and the negative sign is excluded at Q₃. The homotopy-fiber conclusion is conditional on that interpretation, as stated.'),
 'P78-C028': ('§6', 'Scalarization proves the Banach-valued Schwarz bound; the Cauchy radius gives 2M/ρ and coordinate segments give the factor p. The proof is valid with the stated containment and does not resolve the glyph.'),
 'P78-C029': ('§6', 'Lifting paths to the universal cover of C× proves homotopy invariance, additivity and reversal. The approximation argument stays away from zero by compactness. No historical edition is identified.'),
 'P78-C031': ('§7', 'Using the displayed column convention gives Φ′=Φ+pL−σL and ω′=ω−dL. Expanding D₁D₀ cancels exactly because d commutes with Frobenius pullback, including its action on differentials.'),
 'P78-C032': ('§7', 'For square matrices, ΨΦ=p^iI gives invertibility after inverting p, and p-torsion-freeness descends ΦΨ=p^iI. The curvature convention dA+A∧A and the graded-commutator factor two are correctly distinguished. The isolated arithmetic is i+2p.'),
 'P78-C033': ('§7', 'The gauge rule φ′=uφ/σu with ω′=ω−dlog u preserves dlog φ=σω−ω. The competing positive sign does not preserve that equation. This checks the mathematical sign while leaving the ink undecided.'),
 'P78-C035': ('§8', 'In characteristic zero, finite-order unipotent operators are trivial. Passing to a finite-index subgroup preserves the connected unipotent Zariski closure and the rational filtration condition. The argument is restricted to ℓ≠p and does not identify extension of BT groups with trivial p-adic inertia.'),
 'P78-C036': ('§9', 'The f components each have W-rank e times their A-rank. Frobenius gives equal component ranks. With the chosen contravariant convention, the lengths sum to Σrν; dimension one gives slope 1/(ef). The perfect-field equivalence is an input.'),
 'P78-C037': ('§9', 'The intertwining recurrence propagates scalars by π^(s_j−s′_j). Its exact integrality condition is vπ(a₀)≥max_j(s′_j−s_j), including j=0. The one-dimensional ordering consequence follows. The general recurrence, not only finite tests, supports the bound.'),
 'P78-C038': ('§9', 'Commuting integral operators generate a finite A-algebra. Saturating a lattice under that algebra and finitely many F,V translates gives a finite stable lattice because FV=p reduces mixed words. The proof does not legitimize tensoring over Qp with W.'),
 'P78-C039': ('§10', 'For Ω free of A-rank one, Ω/pΩ has residue-field length e, whereas Ω/πΩ has length one. This detects the literal dimension mismatch at e>1 without choosing a replacement glyph.'),
 'P78-C041': ('§10', 'Legendre’s formula gives vπ(π^n/n!)=n−e(n−s_p(n))/(p−1). Stability holds exactly for e≤p−1; at e=p−1 and n=p^r the valuation is one, so divided-power nilpotence fails. The all-prime argument is valid.'),
 'P78-C043': ('§11', 'The line with φ=1 and sole Hodge weight one has t_N=0 and t_H=1. It fails weak admissibility and refutes unrestricted reconstruction. The equivalence theorem itself remains an external input.'),
 'P78-C054': ('§11', 'A lattice stable under φ=p has dual Frobenius p⁻¹, which preserves no lattice p^aZp. The proposed effective category is therefore not rigid without additional structure.'),
 'P78-C064': ('§11', 'For φ=diag(1,p) and Fil¹=span(e₀+e₁), total Hodge and Newton numbers agree and both eigenline inequalities hold. Fil¹ is nevertheless not φ-stable. The distinction between horizontality and filtration preservation is correct.'),
 'P78-C046': ('§12', 'The quotient of two nonzero solutions of the same eigen-equation is Galois-fixed. Conditional on Tate’s invariant-field theorem, it belongs to K×; multiplication by π disproves uniqueness modulo A× without an integral normalization.'),
 'P78-C047': ('§12', 'J={1} refutes the literal every-subgroup claim. The revised open-inertia argument explicitly passes through the completed maximal unramified extension and a nonzero cyclotomic weight. This implication is checked conditional on Tate’s precisely stated Theorem 2; that theorem is not independently re-proved or newly opened by this reviewer.'),
 'P78-C048': ('§13', 'Truncated substitution is associative; invertibility is solved degree by degree from the linear term for k≥1. Contact is chart invariant, truncation is surjective, and the top section symbol has the stated symmetric-power form in the differentiable characteristic-zero setting. The k=0 exception is retained.'),
 'P78-C049': ('§13', 'Pointed jets exclude the constant monomial, giving q(binomial(p+k,k)−1). The test p=q=k=1 gives dimension one, not two. Coordinate changes act by b∘c∘a⁻¹ with the stated source and target.'),
 'P78-C050': ('§13', 'An O-multilinear operation is determined by its coefficients on a local frame; changes of frame agree by multilinearity. This proves the local-to-global fiber map with the specified conventions.'),
 'P78-C051': ('§13', 'The implicit-function argument establishes the local transverse fiber-product dimension and tangent kernel. The global orbit and metric assertions remain limited by their stated hypotheses; this check does not certify a missing definition of the manifold category.'),
 'P78-C055': ('§14', 'For SL₂ and its Borel in characteristic zero, only Sym⁰ has B-invariants; applying this to U∨⊗V proves full faithfulness of restriction. The standard B-stable line witnesses failure of closure under subobjects. The additional observable-subgroup image argument is formally valid given the stated embedding/quotient property; André’s arithmetic theorem is not independently source-checked here.'),
 'P78-C057': ('§15', 'Rescaling a weight-i period changes the comparison by u⁻ⁱ with the fixed right-action convention. The rank-one expression u_g=g(a)/(aχ(g)) obeys u_gh=u_g·g(u_h) by direct cancellation.'),
 'P78-C059': ('§15', 'From φ(q)=qb, replacing q by qg gives b′=g⁻¹bσ(g). Ordinary conjugacy would omit semilinearity. A σ lift on a ramified coefficient field remains an explicit additional choice.'),
 'P78-C060': ('§15', 'Under the written compatibility and c_B²=1, the transported involution squares to one and is fixed by complex conjugation. This is a conditional identity, not construction of all realizations.'),
 'P78-C067': ('§16', 'The local Kummer class has codimension-one degree two and Tate twist one; composing such classes adds degrees and twists. Thus untwisted exceptional pullback has the negative twist and shift. This checks the algebra and does not re-prove global purity.'),
 'P78-C068': ('§17', 'Minkowski gives the conditional weighted convolution bound. Density and local translation bounds give strong continuity for finite p and the stated norm closure at p=∞. The half-line indicator refutes all-L∞ continuity. The abelian Fubini identity does not certify absent nonunimodular conventions.'),
 'P78-C069': ('§18', 'A finite free resolution of the character module gives the two-term co-Lie complex; μ_n gives [O --n→O]. The independent proof is correctly limited to finitely generated characters. The wider arbitrary-character statement is separately attributed to the opened Bergh–Rydh proof.'),
 'P78-C070': ('§18', 'Associativity follows by flat resolutions, preserving both derived tensors until the field hypothesis. The computation agrees with the directly read continuation at cote 8:79.'),
}
valid=set()
for filename in ['claims_c7.json','claims_c8.json']:
    valid.update(c['id'] for c in json.loads((ROOT/filename).read_text()))
assert set(checks)<=valid
with (BASE/'root_cross_events.tsv').open('w',newline='') as f:
    writer=csv.writer(f,delimiter='\t',lineterminator='\n')
    writer.writerow(['statement_id','date','who','type','outcome'])
    for claim,(section,result) in checks.items():
        writer.writerow([claim,'2026-11-19',who,'targeted proof check',
            f'Independent review of proof_audit_root.md {section}: {result}'])

# No fabricated project endpoint is added for an empty result.
with (BASE/'project_leads.tsv').open('w',newline='') as f:
    csv.writer(f,delimiter='\t',lineterminator='\n').writerow(
        ['kind','from','to','what','evidence','note_ids'])
(BASE/'project_leads_audit.md').write_text('''# Context-project lead audit

All 148 in-scope notes `MPL_8_079-081+9+4+100##1` through `MPL_8_079-081+9+4+100##148`, and all provided K4-01, K8-01, K9-01 and K9-02 Codex notes, were read. They name no La Longue Marche, Les Dérivateurs, S6, or identifiable research-run endpoint. Targeted searches for the project names, their spelling variants and mentions of runs or projects corroborated that full reading. The occurrence of “marche” in `MPL_8_079-081+9+4+100##139` is the ordinary verb inside the quoted mathematical assertion, not the name of La Longue Marche.

Consequently `project_leads.tsv` has its required header and zero data rows. This is an audited zero, not missing work. No new project was accessed and no unavailable endpoint was invented.

Two earlier-note ideas refer to a different archive folder: `MPL_8_079-081+9+4+100##5` points from cote 8:80 to cote 100:37; `MPL_8_079-081+9+4+100##73` points from cote 9:23 to cote 100:3. Both endpoint passages were read and these links are retained in `links.tsv` as folder links. Neither note supplies a named research run. Cote 100 remains outside TOPIC and outside the SA15 claim census.

The Codex material is used solely as textual leads and corroboration; it has no Stage 1 verdict rows.
''')

report={'root_targeted_cross_audit_events':len(checks),
        'context_project_leads':0,
        'reason':'No named project or research-run endpoint in the in-scope notes.',
        'reviewed_root_proof_sha256':hashlib.sha256((ROOT/'proof_audit_root.md').read_bytes()).hexdigest(),
        'root_proof_path':'work/root_review/proof_audit_root.md',
        'type':'targeted proof check; not wholesale re-proof of cited theorems'}
(BASE/'outputs/root_cross_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
