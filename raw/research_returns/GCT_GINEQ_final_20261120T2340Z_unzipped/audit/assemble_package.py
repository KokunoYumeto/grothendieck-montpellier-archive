from pathlib import Path
import csv
import hashlib
import json
import re
import shutil
import subprocess
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / "work"
DEST = ROOT / "deliverable"
AUDIT = DEST / "audit"
CHECKS = DEST / "checks"
AUDIT.mkdir(exist_ok=True)
CHECKS.mkdir(exist_ok=True)
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
who_root = "GPT-6 Astra Pro; effort not exposed; run GCT_GINEQ-2026-11-20-R1; agent /root"

mapping = {
    "N-01":"F-01", "N-02":"F-05", "N-03":"F-06", "N-04":"F-07",
    "N-05":"F-08", "N-06a":"F-03", "N-06b":"F-04", "N-07":"F-05",
    "S-01":"F-09", "S-02":"F-10", "S-03":"F-02", "S-04":"F-11",
    "S-05":"F-11", "S-06":"F-07", "S-07":"F-05", "S-08":"F-10",
    "S-DICTIONARY":"B-03",
    "G-01":"F-15", "G-02":"F-16", "G-03":"F-17", "G-04":"F-19",
    "G-05":"F-20", "G-06":"F-21", "G-07":"F-22",
    "GI-01":"F-18", "GI-02":"F-13", "GI-03":"F-13",
    "I-01":"F-13", "I-02":"F-13", "I-03":"F-14", "I-04":"F-14",
    "I-05":"F-14", "I-06":"F-14", "I-07":"F-14", "I-08":"F-14",
    "QI-01":"F-23",
}

def final_id(original):
    if original.startswith("F-"):
        match = re.match(r"F-\d{2}", original)
        return match.group(0) if match else original
    for key in sorted(mapping, key=len, reverse=True):
        if original == key or original.startswith(key + " ") or original.startswith(key + "-"):
            return mapping[key]
    return original

events = []
for file in sorted(WORK.glob("agent*check_events.tsv")):
    shutil.copy2(file, AUDIT / file.name)
    with file.open(newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            event_type = row["type"]
            outcome = row["outcome"]
            if event_type == "final-draft whole-proof check":
                event_type = "targeted proof check"
                outcome = "Whole final-draft proof check. " + outcome
            elif event_type == "source and claim check":
                event_type = "carried as background without fault found"
                outcome = "Source statement and scope checked; not a full independent proof audit. " + outcome
            elif event_type == "targeted implication check":
                event_type = "targeted proof check"
                outcome = "Targeted implication/arithmetic check, not a new whole-proof event. " + outcome
            events.append({
                "statement_id":final_id(row["statement_id"]),
                "date_utc":row["date_utc"],
                "who_model_effort_run":row["who"],
                "type":event_type,
                "outcome":outcome,
                "original_id":row["statement_id"],
                "record":f"audit/{file.name}",
            })

# Background is deliberately not promoted to independent re-proof.
# These records consolidate the actual source-statement/locator checks
# described in the accompanying root and agent audits.
background = [
("B-01.FL-duality","Friedland-Lim arXiv1410.6072v3 section2 equations(5)-(8), duality discussion, Proposition3.1","Projective/injective duality and attainment; source statement and conventions checked."),
("B-01.FL-symmetry","Friedland-Lim section5 equation(23), Theorem5.1, Corollaries5.2-5.3","Banach symmetric spectral reduction and symmetric nuclear decomposition; used over R and C with scalar coefficients."),
("B-02.Der-M","Derksen arXiv1308.3860v2 Corollary1.10; section1.5 equation(4)","Exact matrix-multiplication nuclear norm; spectral/Frobenius conventions checked."),
("B-02.Der-P","Derksen Theorem1.14; section1.7","Exact row permanent nuclear/injective norms; real decompositions and complex lower bounds."),
("B-02.Der-D","Derksen Theorem1.15","Exact row determinant nuclear/injective norms."),
("B-02.CLL","Carlen-Lieb-Loss math/0508096v1 Theorem1.1 equation(1.1)","Sharp Hadamard-type permanent inequality with row Euclidean norms."),
("B-Strassen","Derksen section1.5 equation(5)","Seven-term identity; additionally executed exactly in checks/check_tensor_decompositions.py."),
("B-Glynn","Derksen section1.7 equation(8)","Row permanent decomposition with at most 2^(n-1) terms; coefficient conventions checked."),
("B-Der-D3-and-rank","Derksen section8 p23, five-term unnumbered display and final unnumbered display before Remark8.1","Five-term D3 identity and (5/6)^floor(n/3)n! upper bound; locator corrected from nonexistent equation labels."),
("B-FL-W","Friedland-Lim Lemma6.2 equations(34)-(37)","After rescaling epsilon(W)=2/sqrt(3), real pi(W)=3 and complex pi(W)=3sqrt(3)/2; field distinction checked."),
("B-FL9.4","Friedland-Lim Theorem9.4","The needed conclusion is re-proved in F-08 because two preceding source displays are defective."),
("B-03.GI","Pisier arXiv1101.4195v3 Theorem2.4 equations(2.4)-(2.5)","Real discrete Grothendieck inequality; exact norm direction checked."),
("B-03.Banach","Pisier Theorem3.1 equations(3.13)-(3.14)","ell_1 injective/sign norm and ell_infinity projective/gamma2 polar dictionary; not Hilbert tensor norms."),
("B-KG-dimension","Pisier equation(4.4)","Vector-dimension Grothendieck constants K_G(s); monotonicity and K_G(1)=1."),
("B-04.LO","Landsberg-Ottaviani Theory of Computing11(11), Theorem1.1 and Corollary1.2 p286","Complex matrix-multiplication lower bound 2n^2-n from restricted Koszul flattenings."),
("B-04.LM-bound","Landsberg-Michalek arXiv1608.07486v1 Theorem1.1","Complex matrix-multiplication border lower bound 2n^2-ceil(log2 n)-1; not a best-small-n claim."),
("B-LM-substitution","Landsberg-Michalek Proposition2.3 p3","Known border-substitution antecedent; arbitrary-order image form and norm consequence supplied in F-13."),
("B-04.HJK","Han-Ju-Kim arXiv2503.12032v1 Proposition3.2, Theorem4.2 p9, Theorem5.6","Recursive Koszul cost and row determinant/permanent bounds; large computations not rerun."),
("B-04.HJK4","Han-Ju-Kim arXiv2510.11051v2 Theorem1.1 p2","Row determinant4 CP border rank12; not the polynomial determinant tensor."),
("B-04.HS","Han-Song arXiv2608.09708v2 TheoremA p3, Proposition4.1 pp10-11","Row permanent5 ordinary CP rank16; central binomial plus1 border bound. No claim that permanent5 CP border16 is proved there."),
("B-04.Han","Han arXiv2609.09141v1 TheoremA p2","Waring border rank of squarefree monomial equals 2^(n-1); not a CP lower bound for general order."),
("B-04.Farn","Farnsworth arXiv1505.05079v2 Theorems1.3,1.6,1.8 and Corollary1.11","Historical symmetric polynomial bounds and explicit delta_n factors; CP and symmetric distinctions retained."),
("B-04.CHL","Conner-Harper-Landsberg Forum Math Pi11 e17 (2023), Theorems1.1-1.2, p4","M3 CP border lower bound17 and polynomial det3 CP border equality17; substantial apolarity proof not rerun."),
("B-04.CHuangL","Conner-Huang-Landsberg arXiv2009.11391v1 Theorem1.1 and following identification p3; CP convention p2; proof section5","Polynomial per3 CP border equality16; separate numerical caveat of Theorem1.3 does not apply."),
("B-05.EGOW","Efremenko-Garg-Oliveira-Wigderson ITCS2018 Theorem3 p1:10, Corollary4 p1:11","Linear-rank-method potency barrier 2^d N^floor(d/2), including8N for order3; precise scope checked."),
("B-05.Lovitz","Lovitz arXiv2610.08504v1 Theorem1.2, Corollary1.3 pp2-3","2026 primary preprint statement; potency between2N-2 and2N-2+2/(N+1), upper attained oddN. Whole proof not independently audited."),
("B-06.RS-hardness","Raghavendra-Steurer SODA2009 Theorem1.1","UGC NP-hardness below the real K_G approximation loss; P!=NP qualifier explicit for algorithm exclusion."),
("B-06.RS-algorithm","Raghavendra-Steurer section3.3 equations(3.5)-(3.7); Theorem1.3","Reciprocal guarantee1/K_G-eta and computability; printed Theorem1.2 direction discrepancy recorded, not propagated."),
("B-KG-real-lower","Heilman-Jones-Malavolta arXiv2610.10477v2 Theorem1.1","Source-reported lower bound1.773 and upper1.7799; computer-assisted certificate not rerun."),
("B-KG-real-upper","Peng arXiv2610.24417, Theorem1.1 and section6 equations(41)-(43), author full text https://hub.valency.io/works/W_uhkyapjd","Source-reported upper44496791/25000000=1.77987164; not an exhaustive best-bound claim; certificate not rerun."),
("B-KG-complex","Heilman-Jones-Malavolta arXiv2609.25462 Theorem1.1 equation(1.2)","Source-reported1.4<K_G^C<1.404898554746; computer-assisted certificate not rerun."),
("B-07.FL-real","Friedland-Lim Theorem8.1","Generic real tensor norm hardness for order>=3; exact source scope checked."),
("B-07.FL-complex","Friedland-Lim Theorem8.10","Complex result in this source is order>=4; source is not cited for complex order3."),
("B-08.AlonNaor","Alon-Naor Lemma2.1, Theorem4.3, section4.4","Cut-norm/sign approximation interpretation; no CP-rank equivalence."),
("B-08.Tsirelson","Pisier Theorem12.12 and section19","Real bipartite vector correlations and XOR-game interpretation; cited background."),
("B-09.BIP","Burgisser-Ikenmeyer-Panova arXiv1604.06431v3 Theorem1.4 p3; Corollary2.6 p7","Occurrence support inclusion for n>=m^25; not multiplicity or orbit-closure inclusion."),
("B-Landsberg-survey","Supplied Landsberg GCT survey sections2.2,2.3,2.9","Segre/Veronese and equation dictionary; nonnormality issue distinguished from BIP."),
("G53-N","Grothendieck Resume CSG17, section1 no1 Definition1/Theorem1 p8; USP scan leaf8","Original projective/injective norm construction; archive identifier is a published-work ID."),
("G53-D","Grothendieck Resume section1 no1 Theorem2 and corollary p8-prime; scan leaf9","Universal property and duality; original printed8-prime makes offsets nonconstant."),
("G53-G","Grothendieck Resume section4 no2 Theorems1-2 pp59-60; scan leaves60-61","Fundamental theorem; original scan checked."),
("G53-I","Grothendieck Resume section4 no2 Corollary1 after Theorem3, inequality(8), p61; scan leaf62","Original inequality locator checked."),
("G53-P","Grothendieck Resume section4 no3 opening p62; scan leaf63","Opening of proof, not an invented modern CP-rank theorem."),
("EGA-image","EGA I9.5.1-9.5.4 pp176-177; NUMDAM PMIHES_1960__4__5_0, scan leaves175-176","Scheme-theoretic images and closures; complex flat base change distinguished from nonflat prime reduction."),
("EGA-proper","EGA II Definition5.4.1 and Proposition5.4.2 p100 leaf97; Theorem5.5.3(i) p104 leaf101; NUMDAM PMIHES_1961__8__5_0","Properness, universal closedness, projective implies proper; agent visually verified original scans."),
("SGA3-G","SGA3 ExposeI sections4.5-4.6 p29, MSRI scan leaf42","General linear and module schemes."),
("SGA6-L","SGA6 ExposeV Definition2.1 p314 leaf321; Examples2.2(b), Lemma2.2.1 pp315-316 leaves322-323","lambda structures and exterior powers of locally free sheaves."),
("SGA6-R","SGA6 ExposeV representation-ring example p317 leaf324","K_0 of representation categories; source locator checked."),
("SGA6-G","SGA6 ExposeV Proposition3.2(ii) p325 leaf332; section3.10 equation(3.10.1) p331 leaf338","gamma operations and filtration; does not determine a bundle map's rank."),
("FGA-Q","Bourbaki Expose221, Theorems3.1-3.2 pp259-260, scan leaves12-13; CSG44 and NUMDAM SB_1960-1961__6__249_0","Quot representability used to supply Hilbert/Grassmann parameter spaces."),
("FGA-H","Same Expose221, Hilbert specialization after Proposition3.8 p265 leaf18; Remarks3.9 p266 leaf19","Projective Hilbert schemes; limiting span qualifications supplied in F-17."),
("SGA4-etale","SGA4 ExposeVII section1.2","Definition of etale site; no tensor-rank conclusion imported."),
("WII-purity","Deligne WeilII Definition1.2.2 p153, IAS scan leaf17","Weight/purity convention; F-21 uses only constant rational points and unit motives."),
]
for sid, locator, note in background:
    events.append({
        "statement_id":sid, "date_utc":now, "who_model_effort_run":who_root,
        "type":"carried as background without fault found",
        "outcome":note + " Consolidated against this run's actual source checks and audit notes; complete external proof not independently re-proved by this record.",
        "original_id":sid, "record":locator
    })

for old, corrected in [
("FL-v3-equation57","F-08: e tensor I_m refutes the operator denominator; nuclear denominator is required."),
("FL-v3-before60","F-08: I_m refutes nuclear<=sqrt(rank)*operator; Frobenius is the correct denominator."),
("Direct-rank-ratios","F-05 and F-06: M2 and explicit rank-two T_(1/100); every fixed constant also fails by grouped powers."),
]:
    events.append({"statement_id":old,"date_utc":now,"who_model_effort_run":who_root,
      "type":"refuted, with the refined statement's id","outcome":corrected,
      "original_id":old,"record":"GCT_GINEQ.tex; F-05,F-06,F-08"})

for file in sorted(WORK.glob("agent*.md")):
    shutil.copy2(file,AUDIT/file.name)
shutil.copy2(WORK/"START.md",AUDIT/"START.md")
for name in ["check_tensor_decompositions.py","agent_sdp_checks.py","agent_sdp_checks_result.json"]:
    shutil.copy2(WORK/name,CHECKS/name)

outputs={}
for name in ["check_tensor_decompositions.py","agent_sdp_checks.py"]:
    result=subprocess.run(["python",str(CHECKS/name)],capture_output=True,text=True,check=True,cwd=DEST)
    outputs[name]=result.stdout
    (CHECKS/(name.replace(".py","_output.txt"))).write_text(result.stdout)
    events.append({"statement_id":"F-05,F-06,F-23" if name.startswith("check_tensor") else "F-11",
      "date_utc":now,"who_model_effort_run":who_root,
      "type":"computation or formal certificate",
      "outcome":"PASS; executed exact finite computation only, not theorem-prover verification. " + ("Strassen M2, Derksen rowD3, rational W margin, and both quadratic determinants." if name.startswith("check_tensor") else "Rational unit Gram factor, primal14/5, all Boolean assignments give optimum2, SOS remainder0."),
      "original_id":"ROOT-EXACT-"+name,"record":"checks/"+name})

events.append({"statement_id":"F-18","date_utc":now,"who_model_effort_run":who_root,
 "type":"targeted proof check","outcome":"PASS; complete final incidence proof reread. Added explicit complex-tensor qualifier to the border assertion, retaining the algebraic closed-incidence construction and F-13 dependency; no characteristic-general analytic claim.",
 "original_id":"ROOT-F18-final","record":"GCT_GINEQ.tex"})
events.append({"statement_id":"F-23","date_utc":now,"who_model_effort_run":who_root,
 "type":"targeted proof check","outcome":"PASS; complete coordinate restriction proof and recursive applications reread; both cubic seeds are complex CP results, and only lower bounds transfer automatically to real Euclidean border rank.",
 "original_id":"ROOT-F23-final","record":"GCT_GINEQ.tex"})

with (DEST/"CHECK_EVENTS.tsv").open("w",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=["statement_id","date_utc","who_model_effort_run","type","outcome","original_id","record"],delimiter="\t")
    writer.writeheader();writer.writerows(events)
with (DEST/"ID_MAP.tsv").open("w",newline="") as f:
    writer=csv.writer(f,delimiter="\t");writer.writerow(["working_id","final_id","note"])
    for old,new in mapping.items():writer.writerow([old,new,"Raw notes preserve temporary IDs; final paper controls scope."])
    writer.writerow(["agent_F18_substitution_norms.md","F-13,F-14","Filename retained from earlier provisional numbering; not final F-18."])
    writer.writerow(["QI-01","F-23","Quadratic alternative proof checked; final uses general coordinate restriction."])
with (DEST/"SOURCES.sha256").open("w") as f:
    for file in sorted((ROOT/"upload").iterdir()):
        if file.is_file():
            f.write(hashlib.sha256(file.read_bytes()).hexdigest()+"  "+file.name+"\n")
covered={x["statement_id"] for x in events if x["type"]=="targeted proof check" and "PASS" in x["outcome"]}
missing={f"F-{i:02d}" for i in range(1,24)}-covered
assert not missing, missing
print(json.dumps({"events":len(events),"findings_with_passed_targeted_checks":23,"background_records":len(background),"audit_files":len(list(AUDIT.iterdir())),"exact_checks":"PASS","time_utc":now},indent=2))
