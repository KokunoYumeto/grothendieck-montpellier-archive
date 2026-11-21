"""Build the granular bridge-dependency audit from manually checked scopes.
Every row distinguishes the original statement from an appended estimate.
"""
from pathlib import Path
import csv

root = Path(__file__).resolve().parent
rows=[]
def add(run, ids, source, locator, claim, premise, verdict, conclusion, finding):
    for row_id in ids:
        rows.append(dict(audit_id=f"COND-{len(rows)+1:03d}",run=run,row_id=row_id,
            source=source,locator=locator,claim_audited=claim,premise=premise,
            verdict=verdict,corrected_conclusion=conclusion,finding_id=finding))

s6="INTAKE_RESEARCH_SA06_20261120.md"
s7="INTAKE_RESEARCH_SA07_20261120.md"
s20="INTAKE_RESEARCH_SA20_20261120.md"
sr="INTAKE_REVLOC_20261120.md"
add("SA06",["A.8a"],s6,"lines 52,374,381; archive cote15 scan70 (reported)",
    "F_p-rational supersingular j-count Littlewood bounds","Dirichlet quadratic GRH","A",
    "Exact positive constants are c_p sqrt(D_p)/(pi V(D_p)) and c_p sqrt(D_p)U(D_p)/pi for D_p>=1e10. The exact count identity was already unconditional.","IA02;IA03")
add("SA06",["A.8c"],s6,"lines 54,374,382; archive cote15 scan70 (reported)",
    "Littlewood estimate claimed for unspecified maximal-order class number h(R)","R and counting convention missing","SOURCE_GATE",
    "Neighboring A.1f suggests R is a maximal quadratic order. If R has imaginary quadratic discriminant -D, IA02 applies directly to h(R); for Q(sqrt(-p)), use D=p if p=3 mod4 and 4p otherwise. Original R identification still requires missing proof. No quaternion interpretation asserted.","IA03")
for ids in [["B.4a","B.4b","B.4c","B.4d","B.4e"]]:
    add("SA06",ids,s6,"lines 60-64,374,388-392",
        "Appended class-number--regulator bound for abelian CM field L","Dirichlet GRH","A",
        "Apply exact abelian residue-product bounds. Only h_L R_L is bounded at this step. A lower regulator bound is needed for h_L in the B.4e exponent. Original B.4c remains refuted.","IA02")
    add("SA06",ids,s6,"lines 60-64,374,388-392",
        "Appended full-GRH estimate for general nonabelian CM field L","Dedekind/Hecke GRH over general fields","M",
        "Masullo's stipulated general Hecke claim includes zeta_L and removes a full-GRH hypothesis. The intake supplies no precise generic numerical inequality to transfer. The lower no-Siegel-zero gate can be smaller (IA05); regulator control still matters.","IA02;IA05")
add("SA06",["A.7a","D.0a","D.3b","E.6a"],s6,"lines 368,380,429,439,488",
    "Artin-Tate gerbes, local decomposition data, H^2 classes","no zero hypothesis in these rows","U0",
    "Associated abelian Artin-Tate L-functions have A zero-location statements; zeros do not determine the gerbe or local H^2 class. Original row status unchanged.","IA01")
add("SA06",[f"E.4{x}" for x in "abcdefghijklmnop"],s6,"lines 362,465-480",
    "Weil-etale special values, K-groups and orders at integers","no analytic GRH premise in stated special-value identities","U0",
    "No exact special-value or integral K-group formula is supplied by zero location. GRH can give estimates of L-values; the intake's absolute statement that it says nothing about values is too strong. Original special-value gates unchanged.","IA02;IA07;IA08")
add("SA06",["B.1a","B.1b","B.2a","B.3a","B.3b"],s6,"lines 348,383-387",
    "Finite-field Frobenius purity and Weil-number realizations","finite-field Weil RH, not analytic global RH","U0",
    "Deligne/Weil purity is prior background. Neither A nor M is needed to discharge this finite-field zero bound; original realization claims are not independently re-proved here.","IA01")

add("SA07",["D.3.2"],s7,"lines 461-463",
    "Serre open-image theorem","none","U",
    "The qualitative theorem already is unconditional; no status change.","IA01")
add("SA07",["D.3.2"],s7,"lines 461-463",
    "Effective version via division-field Chebotarev","GRH for nonabelian division-field Dedekind zeta functions","M",
    "Masullo removes this analytic input; Alpoge only covers the cyclotomic subfield part. The intake does not state a fully quantified effectivity theorem or its constants, so no numerical Serre bound is invented.","IA01")
artin_ids=["E.2.1","E.2.2","E.2.3","E.2.4","E.2.5","E.2.6","E.2.10","E.2.11","E.2.12","E.2.13","E.2.14","E.2.18","E.2.22","E.2.23","E.2.24","E.2.26","E.2.27","E.3.2","E.3.3","E.3.4"]
add("SA07",artin_ids,s7,"lines 430-445",
    "New zeta RH associated to field Artin motives in integral-Betti rows","Dirichlet GRH for abelian fields; general Hecke GRH for nonabelian ring-class fields","A/M",
    "A for abelian fields and M for generalized-dihedral ring-class fields. These original geometric/place-separation statements use no zero hypothesis, so their source verdicts do not change.","IA01")
period_ids=["A.4.2","A.4.3","A.4.5","A.4.9","A.4.11","A.4.13","A.4.34"]
add("SA07",period_ids,s7,"lines 420-429",
    "RH for algebraic-Hecke L-functions associated to CM values","general Hecke GRH","M",
    "Hecke zero location is conditionally supplied by Masullo. Algebraicity, period identities, and transcendence remain separate; no upgrade of the period row follows.","IA01;IA04;IA06")

add("PROMPT",["SA07-height-CM-elliptic"],"PROMPT(20261120-235024).md","The task 2; no corresponding height row found in SA07 intake",
    "Effective CM elliptic Faltings-height error","Dirichlet quadratic GRH","A",
    "IA04 gives an explicit R_-(D)/2 error in the Deligne normalization for D>e^6, including the order-conductor correction. The exact height identity is U.","IA04")
add("PROMPT",["SA07-Colmez-Qzeta5"],"PROMPT(20261120-235024).md","The task 2; no corresponding Colmez row found in SA07 intake",
    "Colmez formula for CM by Q(zeta5)","none: abelian Colmez is known","U",
    "IA06 evaluates the exact gamma expression. Q(zeta5) has no imaginary quadratic subfield, so Wei Theorem1.4's qualitative height bound is already U.","IA06")
add("LITERATURE",["Wei-1.1","Wei-1.3-abelian"],"Wei arXiv:2111.00617","Conjecture1.1 p3; Theorem1.3 p4; Corollary4.3 eq13 p14; Theorem4.8 p18",
    "No-Siegel-zero hypothesis and abelian-CM root-discriminant bound","quadratic Dirichlet no-Siegel-zero conjecture; known abelian Colmez","A",
    "C_zero=4 works. Stark descent removes the CM exceptional-zero gate. Explicit C1(g)=75g((2g)!)^2/4 and C2(g)=-g(gamma+log4pi)/4, all CM endomorphisms defined over K.","IA05")
add("LITERATURE",["Wei-1.3-general"],"Wei arXiv:2111.00617","Theorem1.3 p4; proof p18",
    "General individual-CM root-discriminant height bound","individual Colmez formula plus no Siegel zeros","B",
    "A removes the no-Siegel-zero condition already; remaining gate is individual Colmez, not Masullo. The exact explicit implication is IA05.","IA05")
add("LITERATURE",["Wei-1.2"],"Wei arXiv:2111.00617","Conjecture1.2 p4; Stark Lemma9 as used p21",
    "No generalized CM Siegel zeros","quadratic Dirichlet no-Siegel-zero hypothesis plus Stark descent","A",
    "General CM exceptional-zero exclusion follows from A via Stark; it need not await full Hecke GRH. This does not imply full GRH for CM Hecke functions.","IA05")

add("SA20",["A5.011"],s20,"lines 284-291; cote121, exact scan not supplied for this row",
    "Ktilde_0(Z[C23]) and cyclotomic class number","none","U",
    "Rim identification plus h-=3 exact certificate and unconditional h+=1 gives cyclic group of order3. Bernoulli arithmetic alone computes the minus part. Topological application carried from intake.","IA07")
add("SA20",["A5.011-family-estimate"],s20,"line289",
    "Claim L(1,chi) asymp loglog q","Dirichlet GRH","REFUTED_AS_STATED",
    "Replace with 1/V(q)<=|L(1,chi)|<=U(q); complex values require absolute values. IA09 gives for every odd prime an odd primitive character with bounded |L(1,chi)|, refuting the asserted uniform lower asymptotic.","IA02;IA07;IA09")
add("SA20",["A.103"],s20,"lines293-299",
    "K2(Z), K3(Z), and zeta(-1)","none","U0",
    "Integral K-theory identities and Euler's Bernoulli value are separate unconditional inputs, not consequences of RH.","IA07")
for rid in ["I.5","I.8b"]:
    add("REVLOC",[rid],sr,"lines95-100",
        "Existence of a nontrivial cyclotomic group-ring unit","none","U",
        "The arithmetic unit-existence use is unconditional; original I.5 remains refuted as worded (intake status table). IA08 verifies L(1,chi5)=2log(phi)/sqrt5 and phi^4=(7+3sqrt5)/2. The actual group-ring unit is omitted, so its generator status is not newly certified.","IA08")
    add("REVLOC",[rid+"-family-estimate"],sr,"lines97-100",
        "Littlewood estimates for quadratic class-number--regulator products","Dirichlet GRH","A",
        "IA02 gives effective L-value bounds. Such bounds concern hR; an independent class number or regulator statement is needed to isolate R.","IA02;IA08")
add("LITERATURE",["LLS-1.5","LLS-Cor1.3","LLS-Cor1.1","LLS-Cor1.2"],"LLS arXiv:1309.3595v3","Theorem1.5 pp3-4; Corollary1.3 p4; Corollary1.1 p2; Corollary1.2 p3",
    "Explicit values/class numbers/least non-residues/least progression primes","Dirichlet GRH","A",
    "Precise constants and ranges in IA02. Use corrected v3, not obsolete asymptotic constants.","IA02")
add("BRIDGE_FLAGS",["S6_SERIES_GRIND/maps:src:F.2.36"],"BRIDGE_FLAGS.tsv","line280",
    "GRH keyword flag","explicit GRH=false","U0",
    "False positive for analytic conditional dependence in supplied context. Original computation certificates are not attached.","IA01")
add("BRIDGE_FLAGS",["LM8_PUSH/A.69"],"BRIDGE_FLAGS.tsv","line533",
    "DS/RH abbreviation","full proof not attached","SOURCE_GATE",
    "Natural curve-theoretic reading is Deuring-Shafarevich/Riemann-Hurwitz; cannot certify expansion from truncated metadata. No analytic-RH upgrade claimed.","IA01")

fields=list(rows[0])
with (root/'intake_conditional_audit.tsv').open('w') as f:
    w=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
print('Wrote',len(rows),'granular scope records to intake_conditional_audit.tsv')
