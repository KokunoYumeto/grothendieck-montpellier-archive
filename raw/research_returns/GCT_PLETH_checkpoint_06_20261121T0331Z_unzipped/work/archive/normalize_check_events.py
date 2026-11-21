"""Preserve actual check history while using the six requested event types."""
from pathlib import Path
from collections import Counter
import csv

HERE=Path(__file__).resolve().parent
VALID={
    "targeted proof check","independent re-proof","computation or formal certificate",
    "used and rechecked in this run","carried as background without fault found",
    "refuted, with the refined statement's id",
}
MIXED={
    "A-026":(
        "PASS complete T037 A19-A31 read and checked: Elliott character identity, harmonic and S3 formulas, tensor decomposition, tag bijections, all parity and zero endpoints.",
        "PASS executed check_outer4_fixed_tables.py: five harmonic and three S3 rational identities,75 tensor entries, exact6/12/18 and12/24/36 tag counts, scalar N=-12..120 and310 intervals. The other agent's1980 sweep was not rerun."),
    "A-030":(
        "PASS complete T038 5R1-20 read and checked: reduced saturated five-point scheme, full minimal resolution, exact equivariant labels, Pfaffian presentation, irreducible cubic kernel, signed six-coordinate map.",
        "PASS executed check_outer5_fixed_data.py: two complex products, five Pfaffians, seven rational resolution identities, and exact Sylow-indexed intertwining for four group generators."),
    "A-031":(
        "PASS complete T039 read and checked: flag pushforward with the nonflat ideal, exterior determinant twists, all cohomology sequences, actual averaged positive split, all parity, zero and support endpoints.",
        "PASS executed check_outer5_fixed_data.py: independently enumerated26 tableaux, checked seven symmetric-power rational identities,49 tensor entries and exact tag counts6,24,30,36,30,24,6."),
    "A-032":(
        "PASS complete G017 Q1-26 read and checked: theta section and relation action, adjugate torsion-free injection, generic rank3, all cohomology endpoints, complete presentation, parameter regular sequence, averaged multiplication and support.",
        "PASS executed check_outer5_fixed_data.py: both matrix factorizations,20 substitution identities, seven rational characters,140 table entries and241 residue-count values. OUTER5_FIXED_DATA_RECEIPT.json saved."),
    "A-033":(
        "PASS complete G019 SQ1-16 read and checked: ideal-tensored symmetric quotient sequence, all endpoints, determinant parity, residue and zero cases, and bounded nine-variable lattice bijection.",
        "PASS independently executed check_symmetric_quotient_by_jets.py: reconstructed all403200 fixed Newton coefficients by an E-only recurrence and separable differences; every entry,28 rational bounds and44 zeros agree. SYMMETRIC_QUOTIENT_JET_RECEIPT.json saved."),
    "A-034":(
        "PASS complete T040 QP1-23 read and checked: ordinary/saturated Rees strands, full B-kernel and quotient-module resolution, equivariant averaged lift, all degree-zero endpoints, residue interpolation and support.",
        "PASS independently executed check_q_plus_by_jets.py: five signed maximal minors, rank3 minor, seven rational characters, all1680 Newton constants, maximum197280 and all zero sets agree."),
    "A-035":(
        "PASS complete T041 5H1-17 read and checked: relative complementary-column and determinant maps, exact hook differential, top Cech delta_ij map, acyclicity including a1, actual multiplication isomorphism, dimension, parity and support.",
        "PASS executed check_hook_fixed_tables.py: seven rational identities, exact cancellation5H15, and tag counts15,60,78,90,75,60,15."),
    "A-036":(
        "PASS complete T042 OS1-20 read and checked: ideal-tensored quotient sequence, every endpoint and determinant parity, initial interpolation, absent(3,3) term, eight-variable polytopes,27 zeros and both support-propagating injections.",
        "PASS independently executed check_q_plus_symmetric_by_presentation.py: reconstructed all403200 coefficients using the B(T) presentation and Newton characteristic identities, all28 rational bounds and every extremum926/607840200 agree."),
}


def main():
    path=HERE/"CHECK_EVENTS.tsv"
    with path.open(newline="") as stream:
        reader=csv.DictReader(stream,delimiter="\t")
        fields=reader.fieldnames
        old=list(reader)
    if "detail_type" in fields:
        assert all(row["type"] in VALID for row in old)
        print("already normalized",len(old),dict(Counter(r["type"] for r in old)))
        return
    output=[]
    for oldrow in old:
        row=dict(oldrow)
        detail=row["type"]
        row["detail_type"]=detail
        sid=row["statement_id"]
        if sid in MIXED and detail not in VALID:
            proof,computation=MIXED[sid]
            output.append(dict(row,type="targeted proof check",outcome=proof))
            output.append(dict(row,type="computation or formal certificate",outcome=computation))
            if sid=="A-033":
                output.append(dict(row,type="independent re-proof",outcome=
                    "PASS independently derived the actual affine five-point jet map and Q trivialization, with canonical ell_i and alpha_i, establishing the E-only jet character and twist-independent finite-group action. FIVE_POINT_JET_REVIEW.md saved."))
            continue
        if detail in VALID:
            pass
        elif detail=="computation":
            row["type"]="computation or formal certificate"
        elif detail=="targeted source check":
            row["type"]="used and rechecked in this run"
        elif detail in ("independent full proof review","independent exact algebra check"):
            row["type"]="targeted proof check"
        elif detail=="full applied primary-source proof check":
            row["type"]="targeted proof check"
            row["outcome"]=(
                "PASS complete applied A029 proof: d4,n5,D1,G4 and global bound, alternating presentation, "
                "fiber-type Rees map, m-annihilated torsion, linear powers k>=2, saturation, "
                "and root quotient-bundle dimension/Hilbert endpoints checked.")
            output.append(dict(row,type="used and rechecked in this run",outcome=
                "Read KPU published formula6.1.4 p1509, Lemma6.3/Cor6.4 p1510, Prop7.5 pp1514-15 and Thm9.1 pp1520-21, checking exact local hypotheses and stated conclusions. Local primary PDF saved."))
            output.append(dict(row,type="computation or formal certificate",outcome=
                "PASS independently executed the polynomial matrix certificate BQ=F I4 used in A029 and G017; FIVE_POINT_TORSION_CERTIFICATE.txt saved."))
        elif detail=="full map proof and primary-source check":
            row["type"]="targeted proof check"
            row["outcome"]=(
                "PASS complete A028 Cox map: p_i6=e_i and p_ij=(q_i-q_j)/exceptional product; "
                "Ga quotient, SL2 sixth-column slice, normal valuations, Picard degrees, "
                "actual S5 restriction U=[33]|S5=[32], and Rees inclusion checked.")
            output.append(dict(row,type="used and rechecked in this run",outcome=
                "Opened and read CT Remark3.9 p1487 and DFL Table1p10/Remark2.4p13. Recorded the dimensional typo and precise equivariant restriction. No positive flag-module decomposition is inferred."))
        else:
            raise AssertionError(("unclassified event",detail))
        if sid=="G-015" and detail=="independent full proof review":
            output.append(dict(row,type="used and rechecked in this run",outcome=
                "Independently opened and read Magyar Proposition1 pp5-6, determinant bundle p7 and Proposition4(a-c) p10; checked the actual dual Schur and full-flag pullback conventions."))
        output.append(row)
    assert all(row["type"] in VALID for row in output)
    fields=["statement_id","date","who_model_effort_run","type","detail_type","outcome"]
    with path.open("w",newline="") as stream:
        writer=csv.DictWriter(stream,fieldnames=fields,delimiter="\t")
        writer.writeheader()
        writer.writerows(output)
    print("normalized",len(old),"original records into",len(output),"actual events")
    print(dict(Counter(row["type"] for row in output)))


if __name__=="__main__":
    main()
