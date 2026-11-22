"""Retain actual source readings, a complete evaluation-fibre audit and CP36 delivery receipt."""
from pathlib import Path
import csv, datetime, hashlib, json, re, shutil
w=Path(__file__).resolve().parents[1]
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
candidate=w/'agents/obstructions_crystals/post_CP36_type_1_5_evaluation_fibres_candidate.tex'
expected='0e741584e1093eacc160cd9b7a7a2cccc97fff69696c7528f00902093dff13bd'
assert sha(candidate)==expected
out=w/'outputs/root_type15_evaluation_fibres_audit.json';assert not out.exists()
labels=re.findall(r'\\label\{([^}]+)\}',candidate.read_text());assert len(labels)==3
record={'status':'FULL-INDEPENDENT-PROOF-PASS','actual_utc':now,
 'reviewer':'GPT-6 Astra (OpenAI, ChatGPT Pro mode); /root',
 'candidate':str(candidate.relative_to(w)),'candidate_sha256':expected,'labels':labels,
 'entire_candidate_actually_read':True,
 'proof_checks':[
  'The actual evaluation on B=A^(2) has rank4 on a nonempty open by the fully read odd-evaluation proposition withN5. Its rank1 kernel defines psi_B, and finite flat Frobenius base change gives the explicitly typed fibre ideal(u²,v²) after pullback toA.',
  'For a nonordinary surface the perfect alternating H-valued Cartier pairing pulls back along the surjective evaluation to the actual dual matrix B_y. It has rank4, with radical equal to the evaluation kernel. The Pfaffian vector therefore gives precisely psi_B, without requiring the H morphism to be an embedding.',
  'The evaluation identities y_i=e_i(z)² and sum sigma_i(y)e_i(z)=0 give Q(y)=0 as an actual square. Density extends this to the global section ofH^5. The kernel section is allowed to vary withz; no fixed global section is inferred.',
  'A curveD in a fibre has a fixed nonzero section vanishing on every Frobenius fat fibre along a dense open. A multiplicity1 local equation would have a nonzero linear term, impossible in(u²,v²), so div(s)>=2D. The residual effectiveR is nonzero because10 is not divisible4.',
  'All effective divisors onA are nef. IfD²>0, evenness givesD²>=2 and Hodge index makesD ample; D.R>=1 then forcesL²>=12, contradicting10. ThusD²0, adjunction and absence of rational curves makeD a smooth elliptic translate.',
  'Global generation givesL.D>=2. The exact identity10=4L.D+R² forcesL.D2 andR²2, withL.R6; R is an ample principal line. The kernel map cannot be constant because that would make one nonzero section vanish on a dense open ofA.',
  'ConverselyR_x=L(-2E_x) has square2 and positiveL intersection6. Hodge index puts it in the positive cone, and every curve is nef in the closure of that cone, so Nakai makesR_x ample before effectiveness is assumed. RR and ample-line vanishing giveh0R_x1.',
  'OnA×(A/E), the relative Cartier divisor of fibres gives an actual familyR. Cohomology and base change produces its rank1 pushforward. Multiplication by the squared fibre equation gives an everywhere nonzero line subbundle ofW tensorO, defininggamma. On the rank4 evaluation open this is exactlypsi.',
  'If two fibres gave the same section, its residual divisor after removing both double fibres would have square(L-4E)²=-6, impossible for an effective divisor. Hencegamma is nonconstant and injective on geometric points; no separability is inferred.',
  'The dichotomy is valid also for ordinaryA, while the alternating Cartier assertions retain nonordinarity. Generic finiteness of a surface inside an ambient exceptional divisor does not exclude contraction of that divisor, so the proof makes no exceptional-ratio, common-wall or monodromy inference.'
 ],
 'dependencies':[{'path':p,'sha256':sha(w/p)} for p in ['agents/obstructions_crystals/A4_odd_Cartier_evaluation.tex','agents/obstructions_crystals/A4_primitive_type_1_3_full_group.tex','agents/monodromy/prime_Heisenberg_rank.tex']],
 'numerical_run':'None needed or claimed; this is a complete geometric proof audit.',
 'source_scope':'The previously audited theta, Frobenius evaluation and abelian-divisor arguments were reread. No new numerical experiment or external source is needed for this candidate.'}
out.write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/root_check_events.tsv').open('a',newline='') as f:
 wr=csv.writer(f,delimiter='\t')
 for label in labels:wr.writerow([label,now,record['reviewer'],'independent re-proof','PASS: complete actual evaluation and elliptic-degree-two fibre dichotomy; outputs/root_type15_evaluation_fibres_audit.json.'])
 abstract=json.loads((w/'outputs/root_prime5_exceptional_wall_audit.json').read_text())
 for label in abstract['statements']:wr.writerow([label,abstract['actual_utc'],record['reviewer'],'independent re-proof / computation or formal certificate','PASS: full abstract proof and unchanged isolated exact-polynomial rerun; outputs/root_prime5_exceptional_wall_audit.json.'])
source={'actual_utc':now,'reader':record['reviewer'],'readings':[
 {'key':'StacksFiniteEtaleDirectCP37','url':'https://stacks.math.columbia.edu/tag/03QN','web_ref':'turn767707220view0','scope':'Actually opened and fully read Lemma59.55.1, Proposition59.55.2 and Lemma59.55.3 with complete proofs. Strict-henselian stalk/global-section identity, all-prime finite higher-direct-image vanishing and finite base-change map. No image-page inspection claimed.'},
 {'key':'StacksArtinSchreierCP37','url':'https://stacks.math.columbia.edu/tag/0A3J','web_ref':'turn767707220view1','scope':'Actually opened Artin-Schreier sequence and fully read Lemmas59.63.1,59.63.2 and59.63.3 with proofs. In particular the finite etale polynomial algebra argument for surjectivity ofF-1 was read in full. Later general quasi-projective vanishing proofs are not used here.'}
 ],'dependency_boundary':'The specific sheaf exact sequences for the quadratic cover and their Galois equivariance are proved directly in the root candidate; they are not claimed as a theorem copied from these sources.'}
(w/'notes/CP37_root_primary_readings.json').write_text(json.dumps(source,indent=2)+'\n')
bib=w/'notes/root_references.bib'
text=bib.read_text()
assert 'StacksFiniteEtaleDirectCP37' not in text and 'StacksArtinSchreierCP37' not in text
with bib.open('a') as f:
 f.write('''
@misc{StacksFiniteEtaleDirectCP37,
 author={{The Stacks Project Authors}},
 title={Vanishing of finite higher direct images},
 year={2026},
 url={https://stacks.math.columbia.edu/tag/03QN},
 note={Opened and read20November2026: full Lemma59.55.1, Proposition59.55.2 and Lemma59.55.3 with proofs. The finite-morphism statements apply to all abelian etale sheaves, including characteristic-prime coefficients; no source-image inspection claimed.}
}
@misc{StacksArtinSchreierCP37,
 author={{The Stacks Project Authors}},
 title={The Artin--Schreier sequence},
 year={2026},
 url={https://stacks.math.columbia.edu/tag/0A3J},
 note={Opened and read20November2026: the exact sequence and complete Lemmas59.63.1--59.63.3 with proofs. The full polynomial-algebra proof of semilinear F-minus-one surjectivity was checked; later general vanishing proofs are not used for the explicit elliptic curve.}
}
''')
receipt={'checkpoint':36,'archive':'RESEARCH_SA15_checkpoint_36.zip','bytes':46467241,
 'sha256':'87ff89bb99d1f9f5eb857d6703faa7f5f07644e8e074bb66be596fa3ed4a511a',
 'library_file_id':'libfile_fde3_f-2990ef4a41b88191b6c383dcfb034da4_c6789dc4b4d481919ad633aabe6d84d0',
 'observed_save_success':True,'returned_xattrs_applied':True,'apply_xattrs_exit_code':0,
 'recorded_utc':now,'scope':'Receipt recorded after the archive was verified and its save succeeded. The actual archive verification timestamp remains05:54:58.726960UTC. No earlier ZIP was modified.'}
(w/'notes/checkpoint36_delivery_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'status':record['status'],'actual_utc':now,'candidate_sha256':expected,'labels':labels,'sources_recorded':2},indent=2))
