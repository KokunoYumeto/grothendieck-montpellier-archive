"""Consolidate B corrections with exact attached-source line locators."""
from pathlib import Path
import csv

root = Path(__file__).resolve().parents[1]
attached = "input/RESEARCH_SA08_study/study/"
trans = "input/RESEARCH_SA08_transcriptions/transcriptions/"
prompt = "upload/PROMPT(20261119-052153).md"
entries = [
("B-C01", "missing condition; prior correction independently verified",
 f"{trans}MPL_136_142-188_transcription.tex:634-689,736-765,1738-1742; {attached}STUDY.md:171-183; {prompt}:99-107",
 "Three displayed conditions, and the later unrestricted B_i list, classify all differential-ring maps.",
 "Add M: binom(i+j,i)B_(i+j)=A^[i]B_j+A^[j]B_i. The F2 data A=X,B2=1,others0 violate the (1,2) relation by X dX. Credit the attached Pro notes N029-N031 and reader2 for the prior discovery.",
 "B-01;B-02", "Refuted; exact replacement proved"),
("B-C02", "scope correction to a study inference",
 f"{attached}STUDY.md:184-186; {attached}readings/136_142-376.md:122-130; {prompt}:103-105; {trans}MPL_136_142-188_transcription.tex:637-638,767-774",
 "Over a Z-torsion-free target every such ring map preserves the full divided-power structure.",
 "Torsion-freeness plus M forces B_n=A^[n-1]B1 and hence the variable PD identities. Full scalar PD preservation additionally requires u to preserve the scalar PD ideal, or J=(t)_PD. The identity on Z[epsilon]/epsilon^2 with t=0, source ideal(epsilon), target ideal0 is a counterexample to the unrestricted assertion.",
 "B-02", "Refuted; exact qualification proved"),
("B-C03", "scope of the free B parameters",
 f"{attached}STUDY.md:184-186; {attached}readings/136_142-376.md:122-126; {prompt}:104-105",
 "Over an F_p-algebra the B values are free on B_(p^m).",
 "The p-power values freely parametrize derivations solving M; maps of the whole simplicial differential ring must still satisfy the independent coefficient-annihilator conditions. For automorphisms over odd characteristic those conditions force B=0.",
 "B-01;B-03", "Qualified statement proved"),
("B-C04", "margin correction and reducedness precision",
 f"{trans}MPL_136_142-188_transcription.tex:1017,1077,1115; {attached}STUDY.md:189-191; {attached}readings/136_142-376.md:133-139; {prompt}:108-109",
 "The condition on B disappears when 2 is invertible; the F3 witness is called reduced.",
 "For A=0,B3=T^[5],others0 over S=F3{T}, all required conditions hold and the map has a nonzero odd image. The ground ring F3 is reduced; S itself is not, since (T^[5])^2=252T^[10]=0. A regular element in the coefficient ideal together with invertible2 is a sufficient replacement forcing B=0.",
 "B-02", "Refuted; exact witness and sufficient replacement proved"),
("B-C05", "completed parameter and representability correction",
 f"{trans}MPL_136_142-188_transcription.tex:1327-1373; {attached}STUDY.md:192-195; {attached}readings/136_142-376.md:158-167; {attached}RESEARCH_PACKAGES.md:69-71; {prompt}:110-111",
 "The unrestricted arrays on scan178 give an affine automorphism scheme.",
 "For continuous maps and for natural coefficient-ring families, only c_m=B_(2^m) are free, they are2-torsion, and c_m tends to0 in total weight. The B functor is the product over output monomials of finite-support input rows, an ind-affine functor rather than an affine scheme. The A coefficients have no2-torsion restriction.",
 "B-03;B-04;B-17", "Refuted; exact functor and law proved"),
("B-C06", "completion interpretation made necessary",
 f"{trans}MPL_136_142-188_transcription.tex:1159-1194,1230-1275,1366-1373; {attached}readings/136_142-376.md:150-164; {prompt}:110-111",
 "A fixed-ring abstract automorphism of the completed algebra is implicitly determined by the same convergent one-variable data.",
 "Continuity is not automatic for abstract maps: the F2 ultrafilter automorphism fixes polynomial forms but is discontinuous, and its square is identity in dimension1 but not dimension2. Its degree-zero substitution is nevertheless automatically continuous. Natural families over all coefficient algebras are exactly the continuous automorphisms.",
 "B-15;B-16;B-17", "Abstract reading refuted; both precise categories distinguished"),
("B-C07", "determinant criterion completed",
 f"{trans}MPL_136_142-188_transcription.tex:1269-1275; {attached}STUDY.md:202-205; {attached}readings/136_142-376.md:151-155; {attached}RESEARCH_PACKAGES.md:70-71",
 "Only necessity of invertible determinant is proved on the page.",
 "Invertible Delta gives the inverse continuous substitution by the complete total-weight filtration, followed by a finite inverse in exterior degree. The converse also holds for abstract differential-algebra endomorphisms because their degree-zero parts are forced substitutions.",
 "B-03;B-16", "Missing converse proved"),
("B-C08", "determinant-only cohomology claim refuted",
 f"{trans}MPL_136_142-188_transcription.tex:1431-1440; {attached}HUNCHES.md:54-57; {attached}readings/136_142-376.md:171-175,430-434; {attached}RESEARCH_PACKAGES.md:72; {prompt}:150-151",
 "Omega acts on full completed cohomology only through Delta.",
 "The full action is coefficient substitution u=phi0 on product-weight cohomology and is u-semilinear. A=X+X^[2] overZ has Delta1 but acts nontrivially already on the point, T maps to T+T^[2]. Only the associated-weight action is Delta^w, with lowest weight Delta^i in cohomological degreei. All components changing exterior degree vanish.",
 "B-05;B-06;B-07", "Refuted; complete action proved"),
("B-C09", "incorrect sphere test",
 f"{attached}RESEARCH_PACKAGES.md:86-88; {attached}readings/136_142-376.md:451-453; {prompt}:221-222",
 "Each positive operation from H^i is decided by its value on Delta[i+1]/boundary.",
 "For i>0 that sphere has H^i=0, so it cannot test such an operation. Sq1 on the degree-one class of RP2 is nonzero, while this sphere test sees zero. Linear cycle-object maps, and finite skeleta of universal K(F2,i), give the valid proof and detection method.",
 "B-09;B-10", "Refuted; finite RP2 certificate and correct method supplied"),
("B-C10", "strict tau-omega scope",
 f"{trans}MPL_136_142-188_transcription.tex:1478-1507; {attached}STUDY.md:205-207; {attached}RESEARCH_PACKAGES.md:73-74; {attached}readings/136_142-376.md:176-190",
 "The tau-omega programme can be read without specifying the retained category or the uncertain completion hat.",
 "Use an explicit graded-S Serre quotient and strict natural differential-ring maps in that category; only exterior grading is forgotten. Completion has the same homogeneous pieces, whose graded direct sum is the quotient input. These automorphisms induce only identity overF2; no assertion classifies derived-only natural transformations. Original scan182 visually confirms the ambient category.",
 "B-10", "Precise manuscript-category statement proved"),
("B-C11", "G is a monoid, with its units determined separately",
 f"{trans}MPL_136_189-234_transcription.tex:557-579; {attached}STUDY.md:209-213; {attached}readings/136_142-376.md:253-260",
 "The rescaling parameter may be read as an additive or ordinary multiplicative group without the substitution law.",
 "The full object is S with lambda star mu=lambda(T)mu(Tlambda(T)); its polynomial units are exactly the ordinary ring units S^*. The completed units are precisely series with invertible constant coefficient. This respects the author's explicit correction from group to monoid.",
 "B-12", "Exact monoid and units proved"),
("B-C12", "intersection multiplication determined",
 f"{trans}MPL_136_189-234_transcription.tex:610-623,635; {attached}STUDY.md:211-213; {attached}readings/136_142-376.md:260-262",
 "The displayed coefficient list for G intersect H leaves its group law unspecified.",
 "G intersect H=1+Ann(T), with Ann(T)=direct sum of (i+1)-torsion k in weighti, and Ann(T)^2=0. Its law is addition. Use a product in the completion. The intersection is trivial exactly when k is additively torsion free.",
 "B-12", "Exact multiplication and torsion scope proved"),
("B-C13", "scan208 semidirect monoid diagrams refuted",
 f"{trans}MPL_136_189-234_transcription.tex:624-635; {attached}STUDY.md:209-213; {attached}readings/136_142-376.md:260-264; {prompt}:223-224",
 "The displayed semidirect decompositions of endomorphism monoids, including the torsion-free coefficient reading, hold.",
 "The coefficient image from G consists of f(T)=sum f_nT^[n] with f_n in nk; T+T^[2] overZ is omitted despite torsion-freeness. Even overQ the scalar-zero endomorphism A=X(T-X),B=0 cannot factor through the unique scalar-zero rescaling. The correct split statement is for automorphism groups using the coordinatewise section for a coefficient substitution.",
 "B-13", "Refuted; corrected split group extension proved"),
("B-C14", "exclusive Breen-versus-Steenrod inference refuted",
 f"{attached}HUNCHES.md:64-68; {attached}readings/136_282-376.md:415-418; {prompt}:155-157",
 "Operations induced by Omega lie in Breen's algebra and not in the Steenrod algebra.",
 "The coefficient-fixed action is identity, which is the unit in both algebras. Breen's P0 is Frobenius, distinct from its unit. Full weighted coefficient substitution is semilinear; lowest-weight Delta^i is not a stable operation when Delta is not1. No nontrivial positive operation is produced for exclusive placement.",
 "B-06;B-11", "Exclusive claim refuted; exact operation range proved"),
("B-C15", "documentary inference remains unproved",
 f"{attached}HUNCHES.md:39-42; {attached}STUDY.md:37-38; {attached}readings/136_142-376.md:34-37,408-415; {prompt}:158-159",
 "Adjacency to the16August1982 printout and parallels to Pursuing Stacks date scans144-212 to1982-83.",
 "The printout dates itself; same-sheet or contemporaneous-writing linkage to the later loose leaves is not established. Original scans142-145 and archive catalogue footnote137 do not supply that linkage; Pursuing Stacks date headings document parallels only. L7 remains undetermined, not refuted.",
 "B-14", "Undetermined; documentary limits stated"),
]

proof_files = [
    root / "sections/B_automorphisms.tex",
    root / "sections/B_abstract_completion.tex",
    root / "sections/B_dating.tex",
]
def proof_locator(ids):
    result=[]
    for sid in ids.split(";"):
        found=False
        for f in proof_files:
            for number,line in enumerate(f.read_text().splitlines(),1):
                if "\\paragraph{"+sid+"." in line:
                    result.append(str(f.relative_to(root))+":"+str(number)+" ["+sid+"]")
                    found=True
                    break
            if found: break
        if not found: result.append(sid)
    return "; ".join(result)

out=root/"notes/B_CORRECTIONS.tsv"
with out.open("w",newline="") as f:
    writer=csv.writer(f,delimiter="\t")
    writer.writerow(("id","kind","attached_file_line_locators","original_claim","correction","proof_file_line_locators","status","who","date_utc"))
    for key,kind,loc,claim,fix,proof,status in entries:
        writer.writerow((key,kind,loc,claim,fix,proof_locator(proof),status,
                         "GPT-6 Astra (OpenAI), automorphisms parallel agent","2026-11-19"))
print(f"Saved {len(entries)} corrections to {out}")
