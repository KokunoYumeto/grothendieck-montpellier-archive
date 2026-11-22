"""Retain the complete root proof audit of the residual-pencil boundary."""
from pathlib import Path
import csv, datetime, hashlib, json

w = Path(__file__).resolve().parents[1]
candidate = w / 'agents/obstructions_crystals/post_CP24_residual_pencil_boundary_candidate.tex'
dest = w / 'outputs/root_residual_pencil_boundary_audit.json'
assert not dest.exists()
checks = {
    'lem:DE-A3-residual-pencil-boundary-candidate': (
        'Complete proof rederived after fresh complete reads of the two-bundle construction, '
        'determinant curve, norm pencil and contraction, acyclic alternating factorization, '
        'symplectic monad, and restricted cup pairing. The actual f:g->Q has Smith form '
        'diag(uw,1), with w a nonzerodivisor even for nonreduced D. Cartier-divisor duality '
        'identifies Ext^1(i_*A,O_T) with i_*(A^-1 Lcal|D)=i_*R, without a smoothness '
        'assumption on D. G=g^dual is acyclic, using its perfect alternating identification, '
        'so H0(R)->H1(Q^dual) is an isomorphism. For phi(e1)=w f1, phi(e2)=f2, the four '
        'symmetric-square images are w f1^2,w f1 f2,f1 f2,f2^2. Their sole relation is '
        'e1 tensor f2-w e2 tensor f1, giving an injective det(E)=Lcal^-1 term and '
        'cokernel R^2. This proves exactness on every local ring. For local lifts u_i,v_i '
        'and boundary cocycles x,y, z_ij=x_ij tensor v_j+y_ij tensor u_i lifts the first '
        'Cech difference. Its next difference is -d2(x_ij wedge y_jk). The sign is positive '
        'in characteristic two. Thus the two-step boundary of the ordinary product equals '
        'the cup-wedge map, including equal factors. No division by two or identification '
        'of symmetric and divided powers is used.'
    ),
    'cor:DE-A3-residual-pencil-restriction-candidate': (
        'At a sharp source h0(R)=2 follows from the fully reread contraction sequence and '
        'Serre duality. On integral D the ratio of two independent residual sections is '
        'nonconstant; a quadratic relation over the algebraically closed base would make '
        'it constant. Hence Sym^2 H0(R) has a three-dimensional injective multiplication '
        'image W_s. The independently reread Serre-duality identity DE-PT5 identifies '
        'the dual variation family with the cup-wedge pairing restricted to the ACTUAL '
        'determinant image Delta_s. Substitution of the proved boundary identity yields '
        'exactly DE-RB4. Neither replacing Delta_s by all H0(LP) nor inferring a '
        'nonzero restricted boundary is permitted.'
    ),
    'rem:DE-A3-residual-pencil-boundary-scope-candidate': (
        'The statement is an exact identification only. The unresolved kernel is the '
        'kernel of the two-step boundary followed by restriction to Delta_s. Acyclicity '
        'of G and injectivity of residual-pencil multiplication give no lower bound on '
        'that composite. The ordinary A-times-R Petri multiplication is a different map. '
        'The primitive positive-index gate therefore remains open, and this refinement '
        'by itself is not counted as a strict gate reduction at a progress review.'
    ),
}
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
with (w / 'notes/root_check_events.tsv').open('a', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    for label, detail in checks.items():
        writer.writerow([label, now, 'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; RESEARCH_SA15',
                         'targeted proof check', 'PASS. ' + detail])
record = {
    'status': 'FULL MATHEMATICAL AND TYPED DEPENDENCY PROOF PASS',
    'actual_utc': now,
    'candidate': str(candidate.relative_to(w)),
    'candidate_sha256': hashlib.sha256(candidate.read_bytes()).hexdigest(),
    'checks': checks,
    'fresh_dependency_reads': [
        'A3_mixed_positive_index_bundles.tex (complete)',
        'A3_mixed_positive_index_pencil.tex (complete)',
        'A3_mixed_positive_index_trace_zero.tex (acyclic factorization, trace theorem and matrix-line proof)',
        'A3_mixed_positive_index_monad.tex (complete)',
        'A3_mixed_positive_index_Petri.tex (complete)',
    ],
    'scope': 'Symbolic full proof audit; no new finite computation or fresh external theorem invoked.',
}
dest.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
