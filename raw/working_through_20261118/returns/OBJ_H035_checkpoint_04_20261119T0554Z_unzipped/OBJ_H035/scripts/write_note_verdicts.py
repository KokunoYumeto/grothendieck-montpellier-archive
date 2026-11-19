"""Encode the individually checked claims of all six supplied entries."""
from pathlib import Path
import csv

root=Path(__file__).resolve().parents[1]
rows=[]
def add(n,anchor,math,placed,reason,right='H035'):
    rows.append([f'work:K94-01#{n}',anchor,math,placed,reason,right])

add(1,'94/002.1–15; cover','confirmed as a description; invariant not identifiable','H035.1; READINGS 002','The two programmes and raised 1 are visible. The final mark has no definition here; the precise augmented-algebra construction is explicitly ours.')
add(1,'94/003.2–13; change of rings and Lemme 1','confirmed','H035.2–3','Restriction is tensor–Hom adjunction; the faithful-flat descent equivalence retains left exactness and descends finite generation and finite presentation separately.')
add(1,'94/003.14–004.13; Lemme 2','confirmed with completed-module quantifier made explicit','H035.4','Tests include every finite module over the completed ring. Compatible quotient representers give a finite completed module; the product with A_f is faithfully flat.')
add(1,'94/004.14–005.12; Proposition 3','corrected anchor; corrected theorem proved','H035.5; READINGS 004','The note silently says nonzero quotient. The statement locus does not visibly exclude zero; the proof assumes A nonzero. Excluding the zero quotient repairs the literal boundary defect.')
add(1,'94/005.15–006.10; Proposition 4','confirmed, with weaker sufficient finite-value condition','H035.6; READINGS 005','The parenthesis says finite values on finite original A-modules suffice. The injective hulls of the artinian quotients are such test modules.')
add(1,'94/006.11–007.27; Lemme 5','corrected','H035.7–8; H035.10','Local representations and the support argument are proved; generic representation requires nonzero f in A/p. Allowing zero makes that hypothesis vacuous and the tensor counterexample refutes strict prorepresentation.')
add(1,'94/008.1–26; Remarque 5 bis','forward implication confirmed; unqualified converse refuted','H035.9–10','The note accurately describes the attempted converse but does not expose its missing finite-value assumption. L=sum_p (1/p)Z has constant local rank and no finite generic localization. Theorem 12(iv) supplies the repair.')
add(1,'94/009.1–19; Lemme 6','confirmed with coefficient notation repaired','H035.11–12; READINGS 009','The two graded objects can be made locally free on a dense open. The regular-sequence Tor claim follows through strict nilpotent filtrations; undefined M is a coefficient notation problem.')
add(1,'94/009.20–010.19; Corollaire 7','result confirmed; displayed proof corrected','H035.13–15','The Hom comparison is true on a dense open, but the complex writes P for Q and the stated Z^1 two-Tor criterion is false. Both failures have checked counterexamples and explicit repairs.')
add(1,'94/011.4–14; Lemme 8 and Corollaire 9','confirmed in the canonical-module interpretation','H035.16–18','Regular quotients of canonical modules are canonical; the artinian parameter quotient is the residue-field injective hull. The literal heading differentials is retained separately.')
add(1,'94/011.15–013.7; Corollaire 10','confirmed in main hypotheses; margin partly refuted','H035.19–21; H035.27','The split sentence indeed resumes on scan 13. Generic canonical modules exist under regular embedding and excellence. The CMU-only enlargement fails. All parameter-quotient Hom tests detect an isomorphism.')
add(1,'94/013.8–20; cancelled Corollaire 11','confirmed as a cancelled draft; reconstructed implication proved','H035.28; READINGS 013','Whole-block cancellation and local rewrites are retained. The proof uses the final Hom(R,M) definitions, not the uncertain cancelled tensor formulas.')
add(1,'94/012.5–23; absolute-value definition, criterion, characteristic p','corrected; off object','H035.22–24','The note describes the leaf but misses f(0)=0 in the literal definition and nonzero in the root-of-unity sentence. The normalized criterion and positive-characteristic corollary are proved.','Absolute values and valuations; no matching tag supplied')
add(1,'94/012.24–30; equivalence and classification on Q','corrected; off object','H035.25–26','The exponent must be positive; the trivial absolute value needs a separate class. The typescript stops mid-proof. Our completed proof is not attributed to the leaf.','Absolute values and valuations; no matching tag supplied')

add(2,'94/003.8–13; faithful-flat descent','confirmed as an omitted proof; theorem checked','H035.3','Effective module descent plus the equalizer for a faithfully flat algebra supplies the complete argument, including finite and finitely presented versions.')
add(2,'94/003–006; Necessite claire','confirmed as a proof-status description; boundary repaired','H035.4–6','Necessity follows from finite Hom and its limit properties. Proposition 3 must exclude the zero quotient; the note is not a certificate for the literal unqualified condition.')
add(2,'94/004; les P_n se recollent','confirmed; gluing proof supplied','H035.4','Yoneda gives the reductions and surjective transitions; compatible finite presentations identify P_n=P/f^nP. No false assertion about reduction of the kernel is used.')
add(2,'94/008; (v) implies (v bis)','confirmed','H035.9','Generic free representers on each integral closed subset give constructibility by noetherian induction. This checks only the forward implication.')
add(2,'94/009; assertion a and n=1','confirmed','H035.11–12','Generic freeness handles finitely many nilpotent graded pieces. The last nonzero graded piece detects a regular element on the reduction; strict filtrations prove the induction.')
add(2,'94/010.12–18; two-Tor criterion','refuted, not merely left unproved','H035.15','With A=k[x,y]/(xy), M=A/(x), and K=[A --y--> A], both written Tor_1 groups vanish but the H^0 comparison fails. Replace cycles Z^1 by boundaries B^1, or impose the stated Tor_2 repair.')
add(2,'94/011 and 013; Lemme 8 and parameter Hom tests','confirmed in reconstructed terminology','H035.16–20; H035.27','Koszul duality, artinian Matlis duality, generic canonical modules and Krull intersection provide the separate proofs. The false CMU margin is isolated as H035.21.')
add(2,'94/012.26–30; interrupted classification proof','confirmed as a description; corrected theorem proved','H035.26','The unlocated valuations-chapter pointer is not used as evidence. The proof in PROOFS.tex includes the missing trivial case and both nonarchimedean and archimedean arguments.','Absolute values and valuations; no matching tag supplied')
add(2,'94/013.8–20; cancelled Corollaire 11','confirmed as an omitted proof in a cancelled block','H035.28','For the final local definitions, base-change comparisons on Omega reduce the claim to Corollaire 10(c). Cancellation is not treated as a mathematical refutation.')

add(3,'94/007.21; mark after est representable','not checkable as a definite question mark','READINGS 007; H035.8','The enlarged locus admits punctuation or reworking. The entry is appropriately cautious; this is not counted as a securely stated conjecture.')
add(3,'94/013.16m; a expliciter dune autre facon','confirmed','READINGS 013; H035.28','The marginal phrase is legible beside a) of the cancelled corollary and requests reformulation.')
add(3,'94/002–013; no other explicit conjecture or hope','confirmed within its cited scope; later programme added','H035.1; H035.39–40','The claim concerns the supplied 2–13 page set. The targeted continuation search finds prospective composition and two-scheme language on scan 22, which is recorded separately.')

add(4,'S5.1; 94/005.7–8','agreement correction confirmed; expanded spelling uncertain','READINGS 005','The antecedent un f is singular, so editorial French uses tel. The contracted handwritten ending does not justify a high-confidence expanded spelling independently of the transcription.')
add(4,'S6.1; 94/006.22','agreement correction confirmed; expanded spelling uncertain','READINGS 006','One element f is quantified. Singular agreement is appropriate; this minor issue is separate from the mathematically necessary nonzero qualification.')
add(4,'S8.1; 94/008.11','not checkable as a definite grammatical slip','READINGS 008','The terminal curl permits egale or egal. The note itself assigns low confidence. No mathematical statement changes.')
add(4,'S9.1; 94/009.6,16','confirmed notation problem; repaired coefficient specified','H035.12; READINGS 009','The proof uses M without an uncancelled definition. The actual filtered argument is proved for the coherent coefficient module, labeled R in our proof.')
add(4,'S10.1; 94/010.9','confirmed correction','H035.14; READINGS 010','Applying Hom(-,Q) gives L_i dual tensor Q. The ink writes P. A field example gives different dimensions and refutes the literal complex.')
add(4,'S11.1; 94/011.18','not checkable as a definite cancellation','READINGS 011','The enlarged de has a strong horizontal baseline stroke. Cancellation remains uncertain; U subset X is used only as the precise mathematical formulation.')
add(4,'T12.1 and T12.1a; 94/012.21–23','literal sentence refuted; proposed nonzero repair confirmed','H035.24; READINGS 012','In characteristic p, n=p gives zero, never a root of unity. Every nonzero prime-field element has finite multiplicative order.','Absolute values and valuations; no matching tag supplied')

add(5,'94/004–007; Lemme 1, Lemme 2, Proposition 4','confirmed','H035.3–8','The cited internal dependencies are present and their hypotheses have been checked in the reconstructed proofs.')
add(5,'94/007.26; Nakayama','confirmed and used with hypotheses checked','H035.8','At a point of V(p), the ideal p is contained in the local maximal ideal and the quotient of the finite support module is finite; Nakayama applies.')
add(5,'94/008.1; notations of Lemme 5','confirmed, but converse needs repair','H035.9–10','The dependency is literal. The earlier five hypotheses do not include finite F(B), although the converse proof invokes it.')
add(5,'94/009–010; Koszul and Lemme 6(b)','confirmed use; false intermediate criterion isolated','H035.12–15','The Koszul resolution computes Tor for a regular-sequence quotient. The all-positive-Tor result proves Hom base change after correcting the two-term criterion.')
add(5,'94/011.17m; EGA IV 6.11.8','pointer confirmed; claimed enlargement refuted','H035.19–21; EGAIV2','Opened Proposition 6.11.8 p.162 and Remarques 6.11.9 pp.162–163 concern the CMU condition and CM loci. They do not provide generic canonical modules. The excellent clause remains valid.')
add(5,'94/012.24–30; Top. gen. IX and chapter on valuations','first pointer verified; second unidentified','H035.25–26; BourbakiTopIX','Opened Bourbaki IX section 3 no.2 Proposition 6, pp.TG IX.29–30, for equivalence by positive powers. The unspecified valuations chapter is not assigned a fabricated locator.','Absolute values and valuations; no matching tag supplied')
add(5,'94/013.8–10; comme dans Cor. 10','confirmed','H035.28','The cancelled draft reuses U and Omega. The modern implication is proved under the parameter-injective property established in Corollaire 10.')

add(6,'R4.1; 94/004–005; upward arrow','confirmed as a reading of proof order','H035.5; READINGS 004','The completion condition and the generic quotient condition are reordered; the proof uses the latter to choose its nonnilpotent f. The arrow is not a new mathematical implication.')
add(6,'R9.1; 94/009–010; reuse of positive Tor','confirmed, with a false intervening criterion corrected','H035.12–15','The same regular-sequence quotient is the tensor factor. The explicit Lemme 6(b) pointer is valid, but the Z^1 criterion does not follow merely from its displayed two vanishings.')
add(6,'R10.1; 94/010.2; final parameter index','confirmed as a reading uncertainty','READINGS 010; H035.13','The enlarged final index has a tight s-like loop. Mathematics requires the same parameter list; that requirement is not used to overwrite the doubtful ink.')
add(6,'R13.1; 94/013.13–14; cancelled Hom definitions','confirmed caution; no convention change inferred','READINGS 013; H035.28','The overwritten coefficient and operation are not secure. Only the final Hom(R,M) and Hom(R prime,M) formulas are used in the reconstruction.')

with (root/'NOTES_VERDICTS.tsv').open('w') as stream:
    writer=csv.writer(stream,delimiter='\t')
    writer.writerow(['entry_id','anchor','mathematics','placed','reason','right_object'])
    writer.writerows(rows)
print('Wrote',len(rows),'subclaim verdicts across',len(set(r[0] for r in rows)),'entries.')
with (root/'LINKS.tsv').open('w') as stream:
    csv.writer(stream,delimiter='\t').writerow(['tag','other_tag','relation','evidence'])
print('LINKS.tsv has no asserted cross-object links: the nearby catalogue alone is not passage evidence.')
