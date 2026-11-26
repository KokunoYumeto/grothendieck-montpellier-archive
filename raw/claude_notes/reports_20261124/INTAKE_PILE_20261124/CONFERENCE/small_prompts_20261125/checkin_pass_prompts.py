"""The check-in pass over the waiting research prompts (25 Nov 2026, after the intakes of the night's returns).

Conference convener ae84c4aa (Claude Fable 5.2 at effort max), for the main session 329fb1e6. Sentences that the new
results make more precisely statable are replaced in Q03, Q04, Q06 and Q09; the texts they name are appended to the
ZIPs of Q03 and Q09. Backups go to TO_SEND/PRO/_backups_20261125/<folder>/before_checkin_pass_20261125/ first.
Nothing is sent.

usage: python -I -B checkin_pass_prompts.py --dry     show the match counts only
       python -I -B checkin_pass_prompts.py           back up, edit, append, lint
"""
import pathlib
import re
import shutil
import subprocess
import sys
import zipfile

sys.stdout.reconfigure(encoding="utf-8")
DRY = "--dry" in sys.argv
DOCS = pathlib.Path("<local>/Documents")
Q = DOCS / "TO_SEND/PRO/1_Archive_research_by_topic"
BAK = DOCS / "TO_SEND/PRO/_backups_20261125"
RR = DOCS / "grothendieck_archive_transcription_20261110/research_returns"
INT = DOCS / "field_experts/intake_20261121/intakes"
LINT = DOCS / "claude_tools/push_rule_pro_prompts.py"
Q03 = "Q03_INTAKE_A_ANABELIAN_SECTIONS"
Q04 = "Q04_29_SA32_Drivateurs"
Q06 = "Q06_30_SA31_Autour_de_La_Longue_Marche_travers_la_th_part4"
Q09 = "Q09_31_SA28_Autour_de_La_Longue_Marche_travers_la_th_part1"
Q03B = "Q03b_OBJ_H0A2-1_cote57_Picard_points"
Q05 = "Q05_28_SA30_Autour_de_La_Longue_Marche_travers_la_th_part3"
Q10 = "Q10_24_SA20_Autour_dEsquisse_dun_programme"
Q11 = "Q11_OBJ_H037_cote100_finite_normalization"
GT = "GPT-6 Astra (ChatGPT Pro mode)"
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import checkin_pass_bridges as BR  # noqa: E402


def flex(s):
    """regex for s with any whitespace run matching any whitespace run, and either kind of double quote"""
    out = []
    for part in re.split(r"(\s+)", s):
        if not part:
            continue
        if part.isspace():
            out.append(r"\s+")
        else:
            out.append(re.escape(part).replace('"', '["\u201c\u201d]'))
    return "".join(out)


EDITS = {
    Q03: [
        ("the next questions (GT with marked points)",
         flex('Your section 7 takes the next questions: does (III′) hold on GT̂, that is, is the Nakamura-Schneps group '
              'IΓ all of GT̂ (the note, "What remains open", item 1); and does the action of Λ₀ together with the Galois '
              'action form one action of GT̂ on the tower with marked points (Lochak-Nakamura-Schneps §8)?'),
         "Your section 7\n"
         "     takes the next question: does the action of Λ₀ together with the Galois action form one action of GT̂ on the\n"
         "     tower with marked points (Lochak-Nakamura-Schneps §8)? For zero or one marked point our run GT_AFTER_H17\n"
         "     (" + GT + ", checkpoint 07 of 25 November 2026, its question Q2.b) reports that the\n"
         "     Nakamura-Schneps and the Lochak-Nakamura-Schneps actions agree as outer actions, with an explicit inner\n"
         "     correction; no one outside that run has checked this. The note's other open question, whether (III′) holds on\n"
         "     all of GT̂, is closed: it does (see \"Settled on 24 and 25 November 2026\" below)."),
        ("Steklov's two steps and FERMAT_SECTIONS",
         r"Two steps of its proof fail:.*?his own Corollary 5\.6 says ℓ ≥ 11\.",
         "Two steps of its proof fail:\n"
         "     - Proposition 4.6 is false as stated. It needs the leading constant to be an e-th power, and at the Fermat cusp\n"
         "       q = 256⁻¹t^{2n}(1 + O(tⁿ)), where the class κ(256⁻¹) has 2-adic valuation −8 (LM8_PUSH D.22, FERMAT_SUCCESSOR\n"
         "       A.4, in INTAKE_B). The description of the splitting in the proof of Proposition 5.10 is false as well. The\n"
         "       conclusion of Proposition 5.10 holds, so his Theorem A stands for ℓ ≥ 11 once 5.10 is re-proved;\n"
         "     - \"Y₁(ℓ) and Y(μ_ℓ) have no Q-points for ℓ ≥ 7\" is false at ℓ = 7 (his own Corollary 5.6 says ℓ ≥ 11), so the\n"
         "       case ℓ = 7 is unproved as printed.\n\n"
         "     Our run FERMAT_SECTIONS (" + GT + ", checkpoint 13 of 25 November 2026) now proves the\n"
         "     Selmer statement for every odd n ≥ 3: every Selmer section of the open Fermat curve U_n over Q (the run's\n"
         "     notation) is cuspidal, and the Selmer sections form three disjoint packets of cuspidal sections, each a torsor\n"
         "     under H¹(Q, Ẑ(1)); no local section conjecture is an input. For all sections it proves the statement under\n"
         "     OpenAI's local theorem for proper curves (6 October 2026, unrefereed). The Selmer theorem is LM8_PUSH D.23 with\n"
         "     two repairs. Claude Opus 5.5 at effort max checked it (`ATTACK_D23.md` and the intake of 25 November, both in\n"
         "     `INTAKE_A_8_night_20261125/`), with two published inputs still to be opened at the statement used: Wiles 1995,\n"
         "     Theorem 2.14, and the real section theorem. No human has checked it. Where a row of your runs is a case of\n"
         "     this theorem, say so and compare the two proofs."),
        ("the Vandiver eigenspace for even r",
         flex("or r is even and the Vandiver eigenspace A(ω^{−r}) is nonzero."),
         "or r is even and the Vandiver eigenspace A(ω^{−r}) is nonzero.\n"
         "     - For even r ≤ 60 the second case does not occur at any ℓ if K_{4m}(Z) = 0 for 1 ≤ m ≤ 30, which Mok and Zheng\n"
         "       claim (hexagon:2611.00998, unrefereed). The transport K_{4m}(Z)/ℓ ≅ (Cl(Q(μ_ℓ))/ℓ)(ω^{−2m}) that this uses was\n"
         "       audited inside our run IHARA_AFTER_STEP17 (" + GT + ", checkpoint 09 of 25 November\n"
         "       2026, its row K-TRANSPORT) and by no one outside it. State the consequence of N3 in both forms: with no\n"
         "       hypothesis, and on that input."),
        ("N6: strictness of GT in GT_0",
         flex("The claim rests on our unrefereed runs (INTAKE_B, item 2). Read the note with this correction."),
         "The claim rested on our unrefereed runs (INTAKE_B, item 2).\n"
         "     Since 25 November 2026 one of our runs has a proof that was read outside the run: GT_AFTER_H17\n"
         "     (" + GT + ", checkpoint 07) constructs, for every prime p ≡ 5 (mod 12), a continuous\n"
         "     character ϑ_p : GT̂₀ → F₂ that vanishes on GT̂, and these are jointly onto ∏F₂; so GT̂ ⊊ GT̂₀, and GT̂₀ modulo the\n"
         "     normal closure of GT̂ has the quotient (Z/2)^ℕ (its paper on gentle characters, Theorem 11.5, with Theorem 8.1\n"
         "     and Lemma 8.2; in `INTAKE_A_8_night_20261125/`). Claude Opus 5.5 at effort max followed that chain line by\n"
         "     line on 25 November, apart from one published input it did not open (Ihara 1999, Proposition 1.6.1, as\n"
         "     recalled in Furusho 2003, §2.3). No printed proof is known to us, and no human has checked this one. Read the\n"
         "     note with this correction."),
        ("the folder of the night's records",
         r"\n## How to work\n",
         "\n### Results of our runs of the night of 24 to 25 November 2026\n\n"
         "Added on 25 November 2026 by Claude Fable 5.2 (Anthropic) at effort max. Three runs that returned that night are\n"
         "named above where they bear on a row: FERMAT_SECTIONS (Fermat for Selmer sections), GT_AFTER_H17 (GT̂ ⊊ GT̂₀; the\n"
         "action with marked points) and IHARA_AFTER_STEP17 (the transport behind N3). All three are runs of\n"
         "" + GT + ". The folder `INTAKE_A_8_night_20261125/` of the attached ZIP holds their intakes by\n"
         "Claude Opus 5.5 at effort max with the check events, the attack-read of LM8_PUSH D.23, and the LaTeX of the two\n"
         "papers named above (`FERMAT_SECTIONS_cp13_fermat/main.tex`, `GT_AFTER_H17_cp07_gentle_characters/`). These runs are\n"
         "not among the runs this intake takes in. Use them as the newest state of the questions they bear on, each with\n"
         "the check state its intake gives, and record each check named there in `CHECK_EVENTS.tsv` as an earlier event.\n"
         "The folder also holds the LaTeX of OpenAI's preprint on the p-adic section conjecture for proper curves\n"
         "(`OpenAI_p-adic_section_LaTeX/`, 6 October 2026). It is unrefereed, and none of ours has checked it; it enters\n"
         "the Fermat statement for all sections as a named hypothesis only.\n"
         + BR.BLOCK_Q03 +
         "\n## How to work\n"),
    ],
    Q04: [
        ("finite monoids: who proved and checked",
         flex("(our result of 12 November 2026 by Claude Fable 5.2 at effort max, re-derived by a second Claude Fable 5.2 "
              "at effort max; no reader of another model family yet)"),
         "(our result of 12 November 2026 by Claude Fable 5.2 at effort max; written up as\n"
         "  our paper D2, which Claude Opus 5.5 at effort max checked independently on 25 November 2026; re-proved by another\n"
         "  model family, " + GT + ", in our run FINMON_CP2, rows CP2:C-*, whose nilpotence lemma needs\n"
         "  no finite-type hypothesis)"),
        ("finite monoids: the minimum 23",
         flex("it is then simply connected."),
         "it is then simply connected. The least order of a finite monoid M with BM ≃ CP² is 23, attained by one monoid up to\n"
         "  isomorphism and anti-isomorphism (FINMON_CP2, A.6; the reduction was checked by Claude Opus 5.5 at effort max on\n"
         "  25 November 2026, the exclusion computations only inside the run)."),
    ],
    Q06: [
        ("leads on Selmer sections of Fermat curves",
         flex("Leads: our runs SECTIONS_OVER_Q and SECTION_GHOSTS (D.2: Conjecture A for ordinary tripod sections over Q, "
              "conditional on a pronilpotent finite-support statement)."),
         "Leads: our runs SECTIONS_OVER_Q and SECTION_GHOSTS (D.2: Conjecture A for ordinary tripod sections over Q, conditional\n"
         "  on a pronilpotent finite-support statement).\n"
         "  Lead: our run FERMAT_SECTIONS (" + GT + ", checkpoint 13 of 25 November 2026) proves that\n"
         "  every Selmer section of the open Fermat curve of every odd exponent n ≥ 3 over Q is cuspidal, with no local section\n"
         "  conjecture as input (after Steklov, arXiv:2602.17746v2, whose proof needs two repairs); Claude Opus 5.5 at effort\n"
         "  max checked the proof, with two published inputs still to be opened, and no human has. Its second paper states,\n"
         "  checked only inside the run, that for every odd n ≥ 5 a noncuspidal prosolvable Selmer section would have open\n"
         "  2-adic and 3-adic Frey images with common rational Frobenius polynomials on a set of primes of density one."),
        ("the gentle group: strictness",
         flex("Dolgushev-Guynee, arXiv:2401.06870 (attached), on the gentle group GT̂₀."),
         "Dolgushev-Guynee, arXiv:2401.06870 (attached), on the gentle group GT̂₀. Our run GT_AFTER_H17\n"
         "  (" + GT + ", checkpoint 07 of 25 November 2026) proves that GT̂ is a proper subgroup of GT̂₀,\n"
         "  by quadratic characters of GT̂₀ that vanish on GT̂ (its paper on gentle characters, Theorem 11.5; followed line by\n"
         "  line by Claude Opus 5.5 at effort max on 25 November, apart from one published input of Ihara; no human check)."),
    ],
    Q09: [
        ("the two cyclic equations: strictness proved in our run",
         r"- Leads: our runs LM8_PUSH C\.39 and GT_TOWER_CHECK A\.7 claim GT̂ ⊊ GT̂₀,.*?the profinite steps are\s+unchecked\.",
         "- Our runs: GT_AFTER_H17 (" + GT + ", checkpoint 07 of 25 November 2026) proves GT̂ ⊊ GT̂₀.\n"
         "    For every prime p ≡ 5 (mod 12) it constructs a continuous character ϑ_p : GT̂₀ → F₂ that vanishes on GT̂, and these\n"
         "    are jointly onto ∏F₂; so GT̂₀ modulo the normal closure of GT̂ has the quotient (Z/2)^ℕ (its paper on gentle\n"
         "    characters, Theorem 11.5, with Theorem 8.1 and Lemma 8.2; the LaTeX and the intake are attached under\n"
         "    `SA28_updates_20261125/ours_runs/`). Claude Opus 5.5 at effort max followed the chain line by line on\n"
         "    25 November, apart from one published input it did not open (Ihara 1999, Proposition 1.6.1, as recalled in\n"
         "    Furusho 2003, §2.3); no human has checked it. If it holds, the answer to the question is no: the two equations\n"
         "    do not determine the Grothendieck-Teichmüller group. Recheck the chain, open Ihara's proposition, and say what\n"
         "    his pages then assert. The same run claims quotients of order p^k for every prime p ≥ 5, on inputs that no one of\n"
         "    ours has opened (Brown's construction, an all-weight bound of OpenAI, Willwacher's proof of it). The earlier\n"
         "    leads LM8_PUSH C.39 and GT_TOWER_CHECK A.7 (characters of GT̂₀ to F₅, F₇, F₁₃ that vanish on GT̂; graded input\n"
         "    checked by Claude Opus 5.5 at effort high on 24 Nov, profinite steps unchecked) are cases of that claim."),
    ],
}

RULES = r"\n## Rules\n"
EDITS[Q04].append(("the Riemann hypothesis section", RULES, BR.SECTION_Q04 + "\n## Rules\n"))
EDITS[Q06].append(("the Riemann hypothesis section", RULES, BR.SECTION_LM + "\n## Rules\n"))
EDITS[Q09].append(("the Riemann hypothesis section", RULES, BR.SECTION_LM + "\n## Rules\n"))
EDITS[Q05] = [("the Riemann hypothesis section", RULES, BR.SECTION_LM + "\n## Rules\n")]
EDITS[Q10] = [("the Riemann hypothesis section", RULES, BR.SECTION_LM + "\n## Rules\n")]
EDITS[Q03B] = [("the Riemann hypothesis paragraph", re.escape("**Where the outcome goes.**"),
                BR.PARA_Q03B + "**Where the outcome goes.**")]
EDITS[Q11] = [("the Riemann hypothesis paragraph", re.escape("**Where the outcome goes.**"),
               BR.PARA_Q11 + "**Where the outcome goes.**")]
OPENAI_ZIP = Q / "SENT/100_FERMAT_SECTIONS_FOLLOWUP_ATTACHMENT_OpenAI_p-adic_section_LaTeX.zip"


def attachments(folder):
    """(arcname, path or bytes) to append to the ZIP of a prompt"""
    fermat = RR / "FERMAT_SECTIONS_checkpoint_13_20261125T1152Z_unzipped/workbench/papers/fermat/main.tex"
    gentle = RR / "GT_AFTER_H17_checkpoint_07_20261125T0716Z_unzipped/workbench/papers/gentle_characters"
    out = []
    if folder == Q03:
        base = "INTAKE_A_8_night_20261125/"
        for run in ("FERMAT_SECTIONS", "GT_AFTER_H17", "IHARA_AFTER_STEP17"):
            for name in ("INTAKE_%s_20261125.md" % run, "INTAKE_%s_20261125_CHECK_EVENTS.tsv" % run):
                p = INT / run / name
                if p.exists():
                    out.append((base + name, p))
        out.append((base + "ATTACK_D23.md", DOCS / "reports_20261124/INTAKE_PILE_20261124/CONFERENCE/ATTACK_D23.md"))
        out.append((base + "FERMAT_SECTIONS_cp13_fermat/main.tex", fermat))
        for p in sorted(gentle.glob("*.tex")):
            out.append((base + "GT_AFTER_H17_cp07_gentle_characters/" + p.name, p))
    if folder == Q09:
        base = "SA28_updates_20261125/ours_runs/"
        for name in ("INTAKE_GT_AFTER_H17_20261125.md", "INTAKE_GT_AFTER_H17_20261125_CHECK_EVENTS.tsv"):
            p = INT / "GT_AFTER_H17" / name
            if p.exists():
                out.append((base + name, p))
        for p in sorted(gentle.glob("*.tex")):
            out.append((base + "GT_AFTER_H17_cp07_gentle_characters/" + p.name, p))
    for arc, p in out:
        assert p.exists(), p
    if folder == Q03:
        with zipfile.ZipFile(OPENAI_ZIP) as z:
            for i in z.infolist():
                if not i.is_dir() and not i.filename.lower().endswith(".zip"):
                    out.append(("INTAKE_A_8_night_20261125/OpenAI_p-adic_section_LaTeX/" + i.filename, z.read(i.filename)))
    return out + BR.rh_attachments()


def main():
    ok = True
    for folder, edits in EDITS.items():
        pm = Q / folder / "PROMPT.md"
        raw = pm.read_bytes()
        crlf = b"\r\n" in raw
        text = raw.decode("utf-8").replace("\r\n", "\n")
        new = text
        print("==", folder)
        for what, pat, rep in edits:
            n = len(re.findall(pat, new, flags=re.S))
            print("   %-55s matches: %d" % (what, n))
            if n != 1:
                ok = False
                continue
            new = re.sub(pat, lambda m, rep=rep: rep, new, count=1, flags=re.S)
        att = attachments(folder)
        zips = [p for p in (Q / folder).iterdir() if p.suffix == ".zip"]
        assert len(zips) == 1, zips
        print("   attachments to append: %d (%d bytes) to %s"
              % (len(att), sum((len(p) if isinstance(p, bytes) else p.stat().st_size) for _, p in att), zips[0].name))
        if DRY or not ok:
            continue
        dest = BAK / folder / "before_checkin_pass_20261125"
        assert not dest.exists(), dest
        dest.mkdir(parents=True)
        shutil.copy2(pm, dest / "PROMPT.md")
        if att:
            shutil.copy2(zips[0], dest / zips[0].name)
        pm.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
        if att:
            with zipfile.ZipFile(zips[0], "a", zipfile.ZIP_DEFLATED) as z:
                have = set(z.namelist())
                for arc, p in att:
                    assert arc not in have, arc
                    if isinstance(p, bytes):
                        z.writestr(arc, p)
                    else:
                        z.write(p, arc)
            with zipfile.ZipFile(zips[0]) as z:
                assert z.testzip() is None
                assert not [n for n in z.namelist() if n.lower().endswith(".zip")]
                for arc, _ in att:
                    assert arc in z.namelist()
        names = sorted(p.name for p in (Q / folder).iterdir())
        assert len(names) == 2 and "PROMPT.md" in names, names
        for mode in ("--lint", "--lint-math"):
            r = subprocess.run([sys.executable, "-I", "-B", str(LINT), mode, str(pm)], capture_output=True, text=True,
                               encoding="utf-8")
            print("   %s: %s" % (mode, " | ".join((r.stdout + r.stderr).strip().splitlines())[:260]))
        for tool in (DOCS / "claude_tools/paper_completeness_lint.py", DOCS / "claude_tools/prompts/pack_one_zip.py"):
            arg = str(pm) if tool.name.startswith("paper") else str(Q / folder)
            r = subprocess.run([sys.executable, "-I", "-B", str(tool), arg], capture_output=True, text=True,
                               encoding="utf-8")
            print("   %s: %s" % (tool.name, " | ".join((r.stdout + r.stderr).strip().splitlines())[-2:].__str__()[:260]))
    print("all patterns matched once" if ok else "SOME PATTERN DID NOT MATCH ONCE: nothing was written for that prompt")


if __name__ == "__main__":
    main()
