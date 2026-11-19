"""Serialize manual duplicate decisions after reading the notes and both witnesses.

No heading similarity, keyword score or automatic mathematical verdict is used.
The integration script applies only these explicitly authored decisions.
"""
import json
from pathlib import Path

D=Path(__file__).resolve().parents[1]
decisions=[]
def merge(target,others,reason,statement,reconstruction,check,check_reason,locations,kind=None):
    decisions.append(dict(target=target,merge=others,reason=reason,statement=statement,
      reconstruction=reconstruction,check=check,check_reason=check_reason,locations=locations,
      kind=kind,reader='GPT-6 Astra Pro; effort not exposed; SA07-part3/root',date='2026-11-19'))

merge('SA07-1',['SA07-224','SA07-460'],
 'The three notes explicitly repeat the same operational dictionary for cote16; the p15 item already incorporates its repeated note#81.',
 'In cote16/044–049, manuscript A concerns hard Lefschetz on algebraic classes and manuscript C concerns algebraicity of inverse Lefschetz, matching printed A and B. The proposed manuscript B→printed D and manuscript D→printed C remain contextual identifications, because the supplied leaves do not provide their independent definitions. C(X) also denotes a cycle-class vector space in the same letter.',
 'The modern dictionary is editorial. Cotes15 and18 invoke the categories or conjectures without adding the missing definitions. No global substitution of letters is licensed.',
 'agrees','All notes retain the uncertainty; direct reading of16:1723–1756 and1803–1829 verifies the operator evidence. The p18 location is the place where its note invokes the comparison, not where the dictionary is written.',
 ['MPL_16+47+54+44_transcription.tex:1717–1756;1785–1832 (16/044–049)',
  'MPL_15_195-228+18_002-017_transcription.tex:475–481 (15/215)',
  'MPL_18_018-062_transcription.tex:133–161;186–199 (18/025,027)'], 'reading question')

merge('SA07-10',['SA07-410'],
 'The later cote18 notes explicitly supply the calculation for the same two-conjugation identity marked à vérifier at15/203.',
 'For a real motive with compatible Betti and algebraic de Rham realizations, let σ be coefficient conjugation on V_C and f∞ the rational Betti action of geometric complex conjugation. Then de Rham descent is τ=f∞σ=σf∞, so the two semilinear involutions commute and have linear product f∞. Its de Rham real form is V_R^+⊕iV_R^−.',
 'The common notation σ,τ,f∞ is editorial. Semilinearity alone does not imply commutativity: the geometric comparison is used. The separate finite-prime compatibility remains SA07-11.',
 'agrees','15/203 explicitly requests verification;18/033 and037 identify the geometric action, and18/035 computes the fixed space. This merge retains the change from a flagged identity to its later explanation.',
 ['MPL_15_195-228+18_002-017_transcription.tex:162–177 (15/203)',
  'MPL_18_018-062_transcription.tex:292;340–344;406–415 (18/033,035,037)'], 'self-flagged step')

merge('SA07-48',['SA07-424'],
 'Both notes invoke precisely Oda Corollary5.11 and the same characteristic-p Hodge-sequence comparison as a later answer to the p-torsion question.',
 'For an abelian variety A over a perfect field of characteristic p, the contravariant Dieudonné module of A[p] identifies with H¹_dR(A), with its Frobenius, Verschiebung and Hodge submodule H⁰(A,Ω¹). This is the precise Oda comparison; it does not solve every local-field or integral realization question listed on18/005 and043.',
 'This is a later-literature comparison made by the earlier notes. The more specific manuscript question at54/007 remains SA07-269 and is linked; the general crystalline-point programme is not merged into this theorem.',
 'not on the page','The cited18 leaves state programmes and comparison objects, not Oda’s theorem. The notes accurately delimit the later result; the published statement and attribution are separately checked.',
 ['MPL_15_195-228+18_002-017_transcription.tex:966–976;1081–1084 (18/005,011)',
  'MPL_18_018-062_transcription.tex:589–591 (18/043)',
  'MPL_16+47+54+44_transcription.tex:2714–2733 (54/007; linked question)'], 'unpursued implication')

merge('SA07-71',['SA07-401'],
 'The later explicit σ(2πi)^−p formula is the same cycle-class normalization established locally on18/015–017.',
 'For a smooth complex variety, compatible orientation and residue conventions give cl_dR(Y)=(2πi)^p cl_B(Y) for a codimension-p algebraic cycle. Over a field k abstractly isomorphic to C with chosen σ:C→k, the transported Betti class is σ(2πi)^−p times the algebraic de Rham class. Integral cohomology maps to the complex space through its quotient by torsion.',
 'The local residue integral is explicit; its multiplicative and global use requires compatibility of supports, products and trace. The later global formula does not retrospectively fill every proof gap. The transverse-dimension reading alarm and global Gysin-degree problem remain distinct items.',
 'agrees','18/015–017 supplies ∮dz/z=2πi and the proposed codimension-p factor;18/019 writes that factor explicitly, and18/021 tracks it under direct image. Both source layers were read.',
 ['MPL_15_195-228+18_002-017_transcription.tex:1207–1229;1262–1284 (18/015,017)',
  'MPL_18_018-062_transcription.tex:14–31;55–74 (18/019,021)'], 'unproved claim')

merge('SA07-79',['SA07-459'],
 'Both earlier-run notes give the same degree-range test distinguishing the period/Hodge SL₂ from the Lefschetz action on an elliptic curve.',
 'On H¹(E) of a smooth elliptic curve, cup-product L and lowering Λ vanish because H³(E)=H^−1(E)=0; the Lefschetz sl₂ therefore acts trivially. A non-CM Mumford–Tate derived SL₂ acts by its nontrivial two-dimensional standard representation. These are different actions; the two-elliptic product claim has its own nonisogeny hypotheses.',
 'This is an earlier-run comparison, not a new assertion attributed to Grothendieck. The18/012 period draft is cancelled;18/045 is a separate live group calculation.',
 'not on the page','The archive supplies the elliptic group contexts. The elementary degree test in the notes is correct but is not itself written on those leaves.',
 ['MPL_15_195-228+18_002-017_transcription.tex:1172–1188 (18/012,013)',
  'MPL_18_018-062_transcription.tex:617–649 (18/045)'], 'idea of the earlier run')

merge('SA07-82',['SA07-461'],
 'The p18 note expressly restates the p15 comparison and the same withdrawn16/047 reduction, with the same missing cote14 endpoint.',
 'At16/047 the proposed reduction through smooth hypersurfaces is withdrawn after Serre’s simply-connectedness objection. The replacement proposal is to formulate the standard conjectures for singular varieties. The smooth-projective conjugate-variety witness sought at15/223 serves a different problem, separation of archimedean fibre functors.',
 'No supplied cote14 transcription verifies implementation of the singular-variety programme. The anonymous singularity passage on18/044 does not establish that connection.',
 'agrees','The withdrawal and new proposal are explicit at16:1791; the two notes correctly separate them from place separation and do not claim the missing cote14 proof.',
 ['MPL_16+47+54+44_transcription.tex:1785–1796 (16/047)',
  'MPL_15_195-228+18_002-017_transcription.tex:795–796;877–879 (15/223,227)',
  'MPL_18_018-062_transcription.tex:133–161;186–199 (18/025,027; contextual note anchors)'], 'withdrawn in the same text')

merge('SA07-84',['SA07-463'],
 'Both notes identify the same Nori/Ayoub Hopf-algebra comparison and rational pure Nori/André comparison, with the same algebraicity qualification.',
 'For the chosen complex embedding and PID coefficient setup, Choudhury–Gallauer identify Nori’s and Ayoub’s motivic Hopf algebras. Arapura’s rational pure comparison uses André’s motivated correspondences. These constructions do not prove that all motivated projectors or inverse Lefschetz operators are algebraic cycles.',
 'A modern comparison supplied by the earlier runs; the manuscript invokes tensor automorphism groups and comparison torsors. The exact category, coefficients and embedding remain part of each theorem’s hypotheses.',
 'not on the page','The archive group formulas do not state the later comparison theorem. The notes’ warning against replacing motivated correspondences by algebraic correspondences is retained.',
 ['MPL_15_195-228+18_002-017_transcription.tex:420–431;1081–1088 (15/213;18/011)',
  'MPL_18_018-062_transcription.tex:399;879 (18/037,055)'], 'unpursued implication')

merge('SA07-87',['SA07-238','SA07-465'],
 'All three notes make the same exact qualification of Jannsen’s theorem and the quotient from homological to numerical correspondences.',
 'Numerical pure motives over any field, with characteristic-zero coefficients, form a semisimple abelian category. The natural quotient from homological to numerical correspondences does not identify those equivalence relations; a chosen Weil realization factors through that quotient only when numerically zero correspondences have zero cohomological action. The manuscript’s homological semisimplicity uses separate Lefschetz and positivity hypotheses.',
 'Jannsen’s theorem is a later comparison, not an unconditional theorem on the manuscript’s cohomological category. The distinct conditional original claim remains SA07-236.',
 'not on the page','The statement at16:1829 is conditional on C(X) and I(X×X). The later numerical theorem is absent from the archive; the notes correctly preserve the coefficient and equivalence-relation boundary.',
 ['MPL_16+47+54+44_transcription.tex:1819–1832 (16/049)',
  'MPL_15_195-228+18_002-017_transcription.tex:420–438 (15/213)',
  'MPL_18_018-062_transcription.tex:133–161;399 (18/025,037)'], 'unpursued implication')

merge('SA07-90',['SA07-467'],
 'Both earlier-run notes use exactly Rep_Q(G_m) and its conjugation kernel to block the same centre-free inference.',
 'Semisimplicity of rational representations does not imply a trivial group centre: Rep_Q(G_m) splits into characters, while G_m→Inn(G_m) is trivial with kernel G_m. Any comparison with a centre-free geometric fundamental group is a separate theorem with its own hypotheses.',
 'This is an earlier-run cross-project test, not a refutation of a sentence in the manuscript. External anabelian leads are retained only in the separate project-link table.',
 'not on the page','The archive supplies Tate objects and tensor automorphism groups but never asserts that semisimplicity implies centre-freeness. The character calculation is valid and its origin remains explicit.',
 ['MPL_15_195-228+18_002-017_transcription.tex:420–438 (15/213)',
  'MPL_16+47+54+44_transcription.tex:1829 (16/049)',
  'MPL_18_018-062_transcription.tex:197–199;399 (18/027,037)'], 'idea of the earlier run')

merge('SA07-226',['SA07-456'],
 'Both earlier-run notes construct the same algebra of normalized unit-shift Lefschetz strings by explicit matrix units; the p18 note adds a rational Casimir comparison.',
 'For one free normalized string S_i with positions0≤a≤n−i in degrees i+2a, raising L and unit-step lowering Λ generate the product of full matrix algebras Mat_(n−i+1)(Z). Bottom-string projectors are obtained by subtracting consecutive endpoint tests, and L^b e_i Λ^a are matrix units. After tensoring with Q, interpolation in the sl₂ Casimir with eigenvalues m(m+2), and in its Cartan operator, recovers the same rational operator image. This does not identify the ordinary integral exterior-algebra order with the normalized model.',
 'Both explicit constructions are earlier-run repairs/comparisons. The integral normalized-string model and the rational sl₂ interpolation have different coefficient requirements. The manuscript’s integral exterior claim remains refuted separately in SA07-201; the conversion of F and Λ is SA07-455.',
 'not on the page','16/014–015 asks for relations and gives candidate matrix units but uses a defective integral exterior model. The notes supply the normalized model explicitly and do not infer integral equality from rational divisions. The18/027 anchor is a comparison lead, not a manuscript proof of the matrix formula.',
 ['MPL_16+47+54+44_transcription.tex:482–596 (16/014–015), with supplied second-pass changes',
  'MPL_18_018-062_transcription.tex:186–199 (18/027; note anchor)'], 'idea of the earlier run')

out=D/'evidence'/'manual_merge_decisions.json'
out.write_text(json.dumps(decisions,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'merge_families':len(decisions),'item_records_absorbed':sum(len(x['merge']) for x in decisions),
 'method':'Individually authored after reading the source notes and cited manuscript passages. The script serializes decisions only.'},indent=2))
