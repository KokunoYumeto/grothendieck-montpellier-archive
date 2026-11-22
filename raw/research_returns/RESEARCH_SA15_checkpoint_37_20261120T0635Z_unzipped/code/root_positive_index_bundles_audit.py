"""Retain root's independent proof/source audit of the three toral-bundle lemmas.
No finite probe is used to assert the remaining determinant nonvanishing.
"""
from pathlib import Path
import csv, datetime, json
w=Path(__file__).resolve().parents[1]
dest=w/'outputs/root_positive_index_bundles_audit.json'
assert not dest.exists()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
who='GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root; inherited effort'
events=[
('lem:DE-A3-positive-two-bundles','independent re-proof',
 'PASS: complete proof read and rederived over the now explicit algebraically closed characteristic-two base. The previously proved actual mu2 theta linearization descends M^d, since multiplying by3 does not change the ordinary2-index; thus H descends as a cube J. Factoring relative Frobenius into the mu2 and alpha2 quotients gives E0=nu_*J and E1=nu_*(JQ). Dual alpha2 kernel makes nu^* bijective on geometric Picard points; the unique preimage P of nontrivial2-torsion Q is again nontrivial2-torsion. Projection formula gives E1=E0P. Finite Frobenius duality and C(omega)=0 make the Cartier pairing perfect alternating; toral self-adjointness makes the two eigensummands orthogonal and therefore individually nondegenerate, with determinantL. Ample vanishing, Riemann-Roch and trivial tangent bundle give h0=b/2 and c2=b/2. Root reread the entire original EVGM Lemma7.19 proof p105: a nontrivial algebraically trivial line has H0=0, and its least nonzero higher cohomology would have identity factoring through zero by multiplication/Kunneth. This proves acyclicity of P. Cubes J and JQ are very ample and separate every length2 fibre of nu, giving global generation of the pushforwards.'),
('lem:DE-A3-positive-determinant-curve','independent re-proof',
 'PASS: complete geometric and local algebra proof independently rederived. Global generation and positive c2 give general finite regular-section zero schemes of length b/2. Simultaneous vanishing imposes4 conditions on the2-dimensional surface, so general Z0,Z1 are disjoint. Contraction is surjective and the cross-section P subbundle is nowhere zero, giving locally free rank2 quotient Q_s with determinantLP and identical cohomology to K. The wedge w is nonzero by independent evaluation. In a frame where s0 is nonzero, with P² trivialization unit u not assumed a square, quotient columns are (1,0) and (u f²,w). The other chart treats s1 nonzero. Therefore rank is exactly1 along D, and the cokernel is invertible on the Cartier divisor even if nonreduced. Adjunction gives genusb+1; the contraction sequence and acyclicP give chi(Q_s)=chi(R_s)=0, hence degR_s=b. At a sharp source full Cartier first rank is exactlyb-2 (stable lower bound and universal toral upper bound), so the contraction long exact sequence gives h0=h1=2,h2=0. No determinant nonvanishing follows from these calculations.'),
('lem:DE-A3-positive-torsor-boundary','independent re-proof',
 'PASS: entire Cech proof independently checked. A finite etale double algebra has exact trace sequence0→O→A→O→0, and H1(E_i)=0 gives global trace lifts of s_i. Trace of the contraction is beta(s_i,s_i)=0, so it descends to L and vanishes along the regular zero scheme Zi. Local trace-one generators differ by the representative c_ab of alpha. Writing q_i=z_a s_i+r_a gives v_i=beta(s_i,r_a) and r_b-r_a=c_ab s_i. The contraction connecting homomorphism is therefore precisely alpha, with the characteristic-two sign convention explicit.'),
('POSITIVE-INDEX-BUNDLE-SCOPE','targeted proof check',
 'PASS: these statements produce actual bundles, a Cartier curve and the torsor cohomology class, but do not identify the quadratic first-variation determinant with a nonzero residue pairing. Neither acyclicity ofP nor degreeR_s=b proves sharpness. No computation or source is claimed to settle the still-open common-kernel/common-image exclusion.')]
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
    wr=csv.writer(f,delimiter='\t')
    for sid,kind,result in events:wr.writerow([sid,now,who,kind,result])
with (w/'notes/ROOT_SEARCH_LOG_18.md').open('a') as f:
    f.write(f'''\n## {now}: positive-index toral-bundle source/proof audit\n\nRoot read all three proofs in post_CP17_positive_index_bundle_notes.tex, with the explicit algebraically closed base correction. Root actually read original Edixhoven–van der Geer–Moonen Lemma7.19 and its full proof, printedp105, from the retained original full-book extraction agents/obstructions_crystals/sources/edixhoven_geer_moonen_AV.txt (the associated original PDF is retained). This is a fresh content read of an already opened source, not a claim of a new network retrieval or new visual inspection. The proof's acyclicity conclusion is exactly the needed one for the nontrivial Picard line P. The prior actual theta descent and toral Cartier pairing arguments were rechecked at their uses. All three lemmas pass. The remaining residue formula and determinant nonvanishing are still unproved. No finite computation is substituted for this missing geometric step.\n''')
summary={'status':'PASS','actual_utc':now,'complete_mathematical_assertions':3,
         'events':len(events),'base':'Algebraically closed field of characteristic two',
         'source_read':'EVGM Lemma7.19 and entire proof, original printedp105',
         'remaining_gate':'Nonzero quadratic variation determinant; no residue nonvanishing proved.'}
dest.write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
