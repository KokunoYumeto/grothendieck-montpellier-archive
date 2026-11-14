#!/usr/bin/env python3
"""Write the edition README from the current documentary records.

The default mode requires a passing release audit. --working records the current
state without certifying unfinished translations, builds, or visual reviews.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from edition_core import read_tsv, write_tsv, mark_counts, extract_variants
from edition_render import CREDIT, RIGHTS_EN, RIGHTS_FR

EDITION = Path(__file__).resolve().parents[1]
SPECS = [
    ("EGA_V_FR_diplomatique", "French diplomatic reader", "FR", "fr", 0),
    ("EGA_V_FR_corrige_apparat", "French corrected reader with apparatus", "FR", "fr", 1),
    ("EGA_V_FR_texte_de_lecture", "French reading text", "FR", "fr", 2),
    ("EGA_V_FR_master_annotated", "French annotated master", "FR", "fr", 1),
    ("EGA_V_EN_corrected_translator_notes", "New English translation with apparatus and translator's notes", "EN", "en", 1),
    ("EGA_V_EN_reading", "New English reading text", "EN", "en", 2),
    ("EGA_V_EN_master_annotated", "New English annotated master", "EN", "en", 1),
    ("EGA_V24_EN_diplomatic", "Piotr Blass diplomatic reader", "EN", "blass", 0),
    ("EGA_V24_EN_corrected_apparatus", "Piotr Blass corrected reader with apparatus", "EN", "blass", 1),
    ("EGA_V24_EN_reading", "Piotr Blass reading text", "EN", "blass", 2),
    ("EGA_V24_EN_master_annotated", "Piotr Blass annotated master", "EN", "blass", 1),
    ("EGA_V_GUIDE", "English prose guide", "FR and EN", "guide", 2),
]


def rows(relative):
    path = EDITION / relative
    return read_tsv(path) if path.is_file() else []


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def md(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def table(headers, values):
    return ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)] + [
        "| " + " | ".join(md(x) for x in row) + " |" for row in values]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--working", action="store_true")
    args = parser.parse_args()
    audit_file = EDITION / "records/RELEASE_AUDIT.json"
    audit = json.loads(audit_file.read_text()) if audit_file.exists() else {}
    passed = audit.get("status") == "PASS"
    if not args.working and not passed:
        raise SystemExit("A passing release audit is required; use --working for an explicit progress record.")
    pages = rows("PAGES_CHECKED.tsv")
    decisions = rows("CHECK_DECISIONS.tsv")
    outcomes = Counter(r["decision"] for r in decisions)
    translations = rows("records/EN_TRANSLATION_STATUS.tsv")
    translated = {r["key"]: r for r in translations}
    omissions = rows("records/EN_VARIANT_OMISSIONS.tsv")
    translation_variant_notes = rows("records/EN_VARIANT_NOTES.tsv")
    guide = rows("records/GUIDE_PARTS.tsv")
    cleanup = rows("CLEANUP_LOG.tsv")
    fixes = rows("TYPESETTING_FIXES.tsv")
    changes = rows("CHANGES.tsv")
    marks = rows("records/SOURCE_MARK_COUNTS.tsv")
    visual = rows("records/PDF_VISUAL_REVIEW.tsv")
    inventory = {r["reader"]: r for suffix in ("fr", "en", "blass")
                 for r in rows("records/READER_INVENTORY_" + suffix + ".tsv")}
    marker_names = ("unsure", "illegible", "hand", "over", "inserted", "margin", "deleted", "xout", "uline", "uuline", "scanpage", "mspage", "diagram")
    source_totals = {}
    for cote in ("25", "24"):
        selected = [r for r in marks if r["cote"] == cote]
        source_totals[cote] = dict(pages=len(selected), counts={
            name: {phase: sum(int(r.get(phase + "_" + name, 0)) for r in selected)
                   for phase in ("before", "after")} for name in marker_names})
    translator_notes = sum(mark_counts(p.read_text())["tnote"]
                           for p in (EDITION / "master_pages/en").glob("*.tex"))
    reports = {}
    stats = []
    apparatus = []
    for name, label, package, family, mode in SPECS:
        path = EDITION / "build" / name / "audit/report.json"
        report = json.loads(path.read_text()) if path.exists() else {}
        reports[name] = report
        pdf = path.parents[1] / (name + ".pdf")
        pdf_hash = digest(pdf) if pdf.exists() else ""
        latest = {}
        for row in visual:
            if row["reader"] == name and row["pdf_sha256"] == pdf_hash:
                latest[int(row["pdf_page"])] = row
        reviewed = sorted(n for n, row in latest.items() if row["result"] == "layout inspection passed")
        required = report.get("required_visual_review_pages", [])
        boxes = report.get("overfull_boxes", [])
        inv = inventory.get(name, {})
        counts = Counter()
        if mode == 1:
            for key in inv.get("source_keys", "").split():
                variants = json.loads((EDITION / "variant_records" / (key + ".json")).read_text())
                if family == "en":
                    ids = extract_variants((EDITION / "master_pages/en" / (key + ".tex")).read_text())
                    variants = [v for v in variants if v["source_id"] in ids]
                counts.update(v["kind"] for v in variants)
        for kind, count in sorted(counts.items()):
            apparatus.append(dict(reader=name, kind=kind, entries=count))
        stats.append(dict(reader=name, label=label, package=package,
            source_pages=len(report.get("source_physical_pages", {})),
            pdf_pages=report.get("pdf_pages", 0), errors=len(report.get("latex_errors", [])),
            warnings=len(report.get("warnings", [])), missing_characters=len(report.get("missing_characters", [])),
            overfull_boxes=len(boxes), overfull_gt_2pt=sum(b["excess_pt"] > 2 for b in boxes),
            widest_pt=max((b["excess_pt"] for b in boxes), default=0),
            logical_links=report.get("logical_link_marks", {}),
            pdf_annotations=report.get("link_annotations", 0),
            archive_annotations=report.get("archive_link_annotations", 0),
            distinct_archive_pages=report.get("distinct_archive_pages", {}),
            apparatus_entries=sum(counts.values()),
            required_visual_pages=required, passed_visual_pages=reviewed,
            pending_visual_pages=sorted(set(required)-set(reviewed)), pdf_sha256=pdf_hash))
    stamp = datetime.now(timezone.utc).isoformat()
    status = "PASS: all release gates passed" if passed and not args.working else "WORK IN PROGRESS: final release not certified"
    text = ["# Nouveau EGA V: checked texts, readers, translation and guide", "",
        f"Status: **{status}**. Documentary counts generated {stamp}.", "",
        f"The checked source comprises {len(pages)} pages: {sum(r['key'].startswith('ega25_') for r in pages)} from cote 25 and {sum(r['key'].startswith('ega24_') for r in pages)} from cote 24. CHECK_DECISIONS.tsv contains {len(decisions):,} decision rows. The new English translation has {len(translated)} recorded source pages. The guide manifest contains {len(guide)} prose parts.", "",
        "Alexandre Grothendieck, *Nouveau EGA V*, Université de Montpellier, fonds Grothendieck, cote 25; and Piotr Blass's 1987 translation typescript, cote 24. Edition dated 14 November 2026. The archive describes cote 25 as '[à partir de 1967-1987]'.", "",
        "## The three packages", "",
        "EGA_V_READERS_FR.zip contains the three French forms, their annotated master and the guide. EGA_V_READERS_EN.zip contains the two new English forms, their annotated master, the three Blass forms, the Blass annotated master and the guide. Each named work is supplied as a standalone .tex file and a PDF. The guide and this README are repeated in both language packages. There are twelve distinct PDF editions in total.", "",
        "EGA_V_READERS_RECORDS.zip contains the checked pages, intermediate source representations, decision records, manifests, page observations, full-page PDF review images, build scripts and their documentary outputs. Its root is the edition directory referred to by the scripts. The supplied scans and original input archives remain the sources of record and are not duplicated in these packages.", ""]
    text += table(["File stem (.tex and .pdf)", "Contents", "Package"], [(n,l,p) for n,l,p,_,_ in SPECS])
    text += ["", "## Source and reading order", "",
        "The French diplomatic volume follows cote 25 sites 1–184 in archive order. The corrected and reading volumes, their annotated master, and the new English volumes use this exact site order: 139–157, 158–184, 1–96, 97–133, 136–138, 134–135. This places IV 16, IV 17.15–17.16, IV 20 and IV 21 in numerical order, retains the interleaved leaves, and ends with the letter to Dieudonné.", "",
        "The Blass diplomatic volume contains sites 1–76 in archive order. The corrected, reading and annotated-master PDFs contain sites 1–75. The handwritten French note at site 75 retains its language. The curriculum-vitae leaf at site 76 is marked as a stray sheet in the diplomatic volume; its checked page remains in checked_pages/. Blass's gaps, queries, English wording and notation remain in his text. CHECK_DECISIONS.tsv and the guide identify the checked French passages corresponding to his queries and gaps.", "",
        "## How the texts were established", "",
        "Both supplied manifests were checked against file sizes and SHA-256 hashes: 803 entries. Each source page was compared line by line with both supplied image halves, including unmarked typed text, formulas, indices, arrows, handwriting, cancellations and margins. PAGES_CHECKED.tsv records the start and end times and the number of decision rows. Its lines_read field counts nonblank lines in the checked LaTeX source, excluding comments and scan markers; it is not a count of physical manuscript baselines. The per-page review records preserve the definition and observations.", "",
        "The checked_pages/ files retain the supplied editorial macro vocabulary. A changed reading or physical-layer classification has a decision record. Remaining uncertainty stays in the source. A lower or higher count of doubt macros alone does not measure resolved readings: the review also split marks, expanded candidates, recovered canceled wording and introduced doubts where the original transcription was too definite.", "",
        f"Mechanical cleanup has {len(cleanup):,} recorded operations in CLEANUP_LOG.tsv. It repairs TeX syntax and encodings while retaining the visible reading. cleaned_pages/ is that intermediate representation. master_pages/fr/ and master_pages/blass/ attach a stable source ID and a kind to every editorial difference; variant_records/ and CHANGES.tsv preserve the page reading, corrected reading and reason. CHANGES.tsv contains {len(changes):,} entries. Resolving the diplomatic branch must reproduce the cleaned page exactly.", "",
        "The corrected branch incorporates the author's insertions and replacements, places marginal notes, and retains deleted or struck text in its apparatus. The reading form selects the same corrected branch and omits the apparatus reference marks. Source doubts and marginal notes remain. The author-directed transfer from cote 25 site 21 to site 22 is recorded in AUTHOR_RESTORATIONS.tsv: the donor text and its variants are retained and the reproduced passage links back to its donor scan.", "",
        "French spelling, abbreviations and notation remain those of the checked page, including préschéma, Module, systême, loc, rel, resp., sss and cqfd where written. The records preserve the particular source form. A mathematical discrepancy is discussed in the relevant guide paragraph; it supplies no unrecorded correction to the text.", "",
        "The disputed mark at cote 25 site 140 is recorded as the scan-supported handwritten comma after k. The later paired-glyph review of cote 24 revises several earlier baseline/subscript judgments; VISUAL_DECISION_SUPERSESSIONS.tsv identifies those superseded decisions. Earlier checkpoint versions remain separately accounted for.", "",
        "## New English translation", "",
        f"There are {len(translated)} recorded translations out of 184 source pages. The English master contains {translator_notes:,} translator-note macros; {len(translation_variant_notes):,} further variant-specific translation notes and {len(omissions):,} documented French-only variant omissions are recorded separately. Their counts have different units and should not be added as a single note total.", "",
        "The supplied unified SGA glossary governs the new English and editorial prose. Translation notes explain source abbreviations, puns, uncertain letterforms and grammatical repairs. Source explanations remain in the source's running text; new explanations are placed in notes. A French physical correction with identical English outcomes can have its variant omitted only with an explicit entry in EN_VARIANT_OMISSIONS.tsv.", "",
        "The validator compares every mathematical token string in both the page-reading and corrected branches of each French/English master pair. It also checks the ordered variant IDs, documented omissions, numerals outside explicit math, live uncertainty and illegibility counts, and hashes of the checked page and both masters. The restored site-21 passage in site 22 is checked against its donor translation. TRANSLATION_FORMULA_AUDIT.tsv, EN_TRANSLATION_STATUS.tsv and EN_TRANSLATION_HISTORY.tsv retain these results.", "",
        "## Counts from the checked sources", "",
        "These are macro occurrences in the original and checked page files, before reader selection and repeated apparatus quotations. Each illegible macro is one mark even when its argument denotes several unreadable words.", ""]
    text += table(["Cote", "Pages counted", "Macro", "Before", "After"], [
        (cote, source_totals[cote]["pages"], name,
         source_totals[cote]["counts"][name]["before"],source_totals[cote]["counts"][name]["after"])
        for cote in ("25","24") for name in marker_names])
    text += ["", "### Decision outcomes", "",
        "The labels below are the exact decision values in CHECK_DECISIONS.tsv. Composite labels remain composite and each row is counted once. Superseded decisions remain in the history and are identified in the supersession records.", ""]
    text += table(["Recorded outcome", "Rows"], sorted(outcomes.items(), key=lambda x:(-x[1],x[0])))
    text += ["", "### Apparatus entries", "",
        "Counts are per printed form. Nested physical corrections retain separate IDs. The diplomatic and reading forms print no apparatus entries. APPARATUS_COUNTS.md gives the per-kind counts for each volume.", ""]
    text += table(["Volume", "Source pages", "Printed apparatus entries"],
                  [(r["reader"],r["source_pages"],r["apparatus_entries"]) for r in stats if r["reader"]!="EGA_V_GUIDE"])
    text += ["", "## Compilation, links and visual review", "",
        f"TYPESETTING_FIXES.tsv contains {len(fixes):,} reader-specific repair records. Local repairs are applied to the generated page payloads and are recorded with their source location; the common mathematical master remains available for the translation token checks. LOCAL_DIAGRAM_SCALE_AUDIT.tsv records the measured local scaling. Every resulting PDF has its own compile report, source and PDF hashes, historical overflow list, link inventory and visual observations.", "",
        "The table reports the final log for each current PDF. The warning count includes warning messages collected by the compiler, separately from overfull boxes and missing glyphs. TYPESETTING_REPORT.md preserves the before/after compile history and every recorded page observation.", ""]
    text += table(["PDF", "Pages", "Errors", "Warnings", "Missing glyphs", "Overfull boxes", "Widest (pt)", "Over 2 pt", "Required / passed views"], [
        (r["reader"],r["pdf_pages"],r["errors"],r["warnings"],r["missing_characters"],r["overfull_boxes"],f"{r['widest_pt']:.5f}",r["overfull_gt_2pt"],f"{len(r['required_visual_pages'])} / {len(set(r['required_visual_pages']) & set(r['passed_visual_pages']))}") for r in stats])
    text += ["", "Every source-page scan marker and every printed uncertainty/illegibility mark has an archive link. Named logical destinations let the audit compare source-mark counts with the PDF and test the actual URI near each individual mark. Archive PDF pages equal site numbers plus one. A linked word or phrase can wrap across multiple PDF annotations, so the logical mark count and annotation count are reported separately.", ""]
    text += table(["PDF", "Logical scan", "Logical unsure", "Logical illegible", "Provenance", "All annotations", "Archive annotations", "Distinct archive pages"], [
        (r["reader"],r["logical_links"].get("scan",0),r["logical_links"].get("unsure",0),r["logical_links"].get("illegible",0),r["logical_links"].get("provenance",0),r["pdf_annotations"],r["archive_annotations"],json.dumps(r["distinct_archive_pages"],sort_keys=True)) for r in stats])
    text += ["", "For each PDF, the required visual set includes forty evenly spread pages (every page for a shorter work), all landscape pages, the final page ranges corresponding to historical overflows and local repairs, and all current text, vector and image geometry flags. A successful page observation is tied to the exact PDF SHA-256 and rendered-image SHA-256. Reuse of a previously viewed complete page requires byte-for-byte identity of its newly rendered PNG with the actually viewed image; PDF_VISUAL_EQUIVALENCE.tsv records both PDF hashes, both page numbers, the common image hash and the originating inspection. Every differing required image is inspected separately. PDF_GEOMETRY_REVIEW.tsv records the explicit visual disposition of each permitted single-letter overhang or conservative graphics bound. A real overflow or overlap requires a source repair and review of the changed page.", "",
        "Marginal-note placement uses the number of actual packed lines measured by LuaTeX. A note of at most three lines remains in the margin; a longer note appears as a labeled, ruled block at its attachment. MARGIN_LINE_AUDIT.tsv records the measured routes, and the PDF audit verifies that every queued marginal note and its attachment remain on the same physical page. The earlier height-only test admitted notes that occupied four lines and was replaced; those repairs and their superseded PDF observations remain documented.", "",
        "## Documentary file map", ""]
    text += table(["Path", "Purpose"], [
        ("checked_pages/", "All 260 checked diplomatic page sources."),
        ("CHECK_DECISIONS.tsv; PAGES_CHECKED.tsv", "Reading decisions and completed page-review records."),
        ("CHANGES.tsv; APPARATUS_COUNTS.md", "Every corrected/diplomatic difference, with kind and reason; counts by form."),
        ("CLEANUP_LOG.tsv; TYPESETTING_FIXES.tsv", "Mechanical TeX cleanup and local layout repairs."),
        ("TYPESETTING_REPORT.md", "PDF log results, geometry, link counts and actual visual findings."),
        ("cleaned_pages/; corrected_pages/; master_pages/; variant_records/", "Reproducible intermediate source representations and variants."),
        ("readers/", "Current standalone reader, master and guide TeX sources."),
        ("guide_parts/; records/GUIDE_PARTS.tsv", "The guide's prose and section manifest."),
        ("records/NOTES_COVERAGE.tsv", "Per-item cross-references from the supplied NOTES.tsv concerns to the decisions."),
        ("records/EN_*.tsv; records/TRANSLATION_FORMULA_AUDIT.tsv", "Translation coverage, source hashes, variant explanations and token comparisons."),
        ("records/PDF_*.tsv; build/visual_review/", "PDF freezes, actual inspection records, geometry dispositions, images and image manifests."),
        ("build/*/audit/; build/*/*.log", "Compile reports, sanitized logs, overfull-box history and individual PDF link audits."),
        ("review_work/", "Per-page review records, comparison notes and retained work documentation."),
        ("scripts/", "Build, checking, reporting, checkpoint and packaging programs."),
        ("records/CHECKPOINT_CATALOG.tsv; records/CHECKPOINT_MEMBER_ACCOUNT.tsv", "Immutable checkpoint catalogue and the disposition of every earlier file version."),
        ("records/RELEASE_AUDIT.json; records/RELEASE_AUDIT.md", "The final release gates and their evidence."),
        ("records/FINAL_FILE_MANIFEST.tsv", "Package-member byte counts and SHA-256 hashes; the manifest excludes its own self-hash."),
    ])
    text += ["", "## Rebuilding", "",
        "Each supplied reader .tex is self-contained and compiles with LuaLaTeX in a standard TeX Live installation. Run LuaLaTeX twice to settle page references. The sources use Latin Modern fonts and the standard packages fontspec, babel (English/French), geometry, amsmath, amssymb, mathtools, newunicodechar, xcolor, tikz-cd, lua-ul, marginnote, fancyhdr, pdflscape, microtype and hyperref.", "",
        "To regenerate the edition, extract the records ZIP into a directory named edition and the supplied EGA_V_TEXT.zip into its sibling source directory. For scan-based reinspection, extract EGA_V_SCANS.zip into the sibling scan_source directory. Python 3, PyMuPDF and pypdf support the build audits; LuaLaTeX supplies the typesetting. Commands are run from the parent of edition:", "",
        "```sh\npython edition/scripts/build_readers.py build --family all\npython edition/scripts/build_guide.py\npython edition/scripts/compile_readers.py edition/readers/*.tex\npython edition/scripts/generate_build_reports.py\npython edition/scripts/audit_release.py\npython edition/scripts/generate_readme.py\n```", "",
        "The preserved PDF freeze ledger intentionally prevents an accidental overwrite of a reviewed edition. A deliberate rebuild must first release the affected reader with pdf_review.py release and a concrete reason. New PDF bytes require their own freeze, rendered pages and explicit page observations; commands and the observation schema are in records/PDF_REVIEW_WORKFLOW.md. The release audit remains blocked until those requirements are fulfilled. Earlier review evidence remains in the ledger.", "",
        "Historical audit scripts document how the checked pages were established. Rebuilding the readers uses the checked_pages/ sources directly; it does not replay earlier reading decisions. In particular, the paired-glyph supersession record controls the later cote-24 index decisions.", "",
        "## Checkpoints and retained history", "",
        "CHECKPOINT_CATALOG.tsv identifies every numbered, immutable checkpoint by bytes, SHA-256 and saved-file identity. CHECKPOINT_MEMBER_ACCOUNT.tsv gives one row for every member of every checkpoint: original member path and SHA-256, retained destination or replacement path and hash, and the reason for supersession or omission. The final packages retain current deliverables and documentary work. Earlier development PDFs and TeX auxiliary products are accounted for individually; they are not included among the published PDFs.", "",
        "## Credits and rights", "", CREDIT + ".", "",
        "AI-translated by GPT-6 Astra (OpenAI, ChatGPT Pro mode).", "",
        "The translation in cote 24 is Piotr Blass's (1987); the rights in it belong to its translator or his heirs.", "",
        "The Grothendieck Circle scan EGA5.pdf, the P. and J. Blass translations (2004), J. C. Reinhold's web re-edition and the Centre for Grothendieckian Studies item L49d are named as published texts. They are not reproduced and were not consulted for any reading. Published EGA IV is cited in the guide by numbered results, with the verification method and limits recorded in records/PUBLISHED_REFERENCE_METHOD.md.", "",
        RIGHTS_EN, "", RIGHTS_FR, ""]
    (EDITION / "README.md").write_text("\n".join(text))
    summary = dict(generated_utc=stamp, status=status, checked_pages=len(pages), decisions=len(decisions),
        decision_outcomes=dict(outcomes), source_macro_counts=source_totals, translated_pages=len(translated),
        translator_note_macros=translator_notes, variant_translation_notes=len(translation_variant_notes),
        french_only_variant_omissions=len(omissions), guide_parts=len(guide), readers=stats)
    (EDITION / "records/README_COUNTS.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n")
    write_tsv(EDITION / "records/DECISION_OUTCOME_COUNTS.tsv",
              [dict(outcome=k, rows=v) for k,v in sorted(outcomes.items())], ["outcome","rows"])
    write_tsv(EDITION / "records/APPARATUS_COUNTS.tsv", apparatus, ["reader","kind","entries"])
    print(json.dumps(dict(status=status, readers=len(stats), checked_pages=len(pages), translated_pages=len(translated))))


if __name__ == "__main__":
    main()
