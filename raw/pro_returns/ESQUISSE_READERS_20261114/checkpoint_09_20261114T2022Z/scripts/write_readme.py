#!/usr/bin/env python3
"""Generate the edition README from current sources and recorded audits.

This script writes only README.md. It does not approve a reading, run a build,
set release status, or turn a rendered page into a visual-review observation.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import re
import tempfile

from edition_core import annotate, clean_latex, macros
from build_edition import (
    FORMS, PREFACES, attach_copy2, link_notes, make_document,
)


TICK = chr(96)
FENCE = TICK * 3
PACKAGES = [
    ("ESQUISSE_READERS_FR.zip", "FR/; README.md",
     "Three French readers and the French annotated master, each as standalone .tex and PDF."),
    ("ESQUISSE_READERS_EN.zip", "EN/; GUIDE/; README.md",
     "Two English readers, the English annotated master, and the guide, each as standalone .tex and PDF."),
    ("ESQUISSE_READERS_RECORDS.zip",
     "All remaining edition-root paths; README.md",
     "Checked and annotated page files, translations, guide fragments, scripts, templates, review records, build logs, tables, JSON files and reports."),
]
DOCUMENTS = [
    ("FR/ESQUISSE_FR_diplomatique", "French diplomatic reader",
     "Copy 1 followed by copy 2, with their checked typed and handwritten readings."),
    ("FR/ESQUISSE_FR_corrige_apparat", "French corrected reader",
     "The corrected copy 1 text, with the French apparatus and separately identified copy 2 annotations."),
    ("FR/ESQUISSE_FR_texte_de_lecture", "French reading text",
     "The same corrected text with editorial apparatus and correction markers suppressed; authorial notes and doubts remain."),
    ("FR/ESQUISSE_FR_master_annotated", "French annotated master",
     "The shared French variant-bearing source; its PDF displays the corrected apparatus projection."),
    ("EN/ESQUISSE_EN_corrected_translator_notes", "English corrected reader",
     "The complete English translation with shared variant IDs, French-source apparatus, copy 2 annotations and translator's notes."),
    ("EN/ESQUISSE_EN_reading", "English reading text",
     "The same English translation with editorial apparatus and translator's notes suppressed; authorial notes and doubts remain."),
    ("EN/ESQUISSE_EN_master_annotated", "English annotated master",
     "The shared English variant-bearing source; its PDF displays the corrected apparatus projection."),
    ("GUIDE/ESQUISSE_GUIDE", "Guide",
     "A collation preface and one commentary paragraph for the sommaire, each of sections 1–10, and each of notes 1–7."),
]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def code(value):
    return TICK + str(value).replace(TICK, "'") + TICK


def link(path, label=None):
    return f"[{label or path}]({path})"


def cell(value):
    return str(value).replace("|", r"\|").replace("\n", " ")


def table(headers, rows):
    return "\n".join([
        "| " + " | ".join(headers) + " |",
        "|" + "|".join("---" for _ in headers) + "|",
        *["| " + " | ".join(cell(x) for x in row) + " |" for row in rows],
    ])


def page_list(values):
    values = sorted(set(int(n) for n in values))
    return ", ".join(map(str, values)) if values else "none"


def yes(value):
    return "yes" if value else "no"


class Snapshot:
    """Read every input once and reject a snapshot changed while being read."""

    def __init__(self, root):
        self.root = root
        self.data = {}
        self.directories = {}

    def read(self, relative):
        relative = str(relative)
        if relative not in self.data:
            p = self.root / relative
            self.data[relative] = p.read_bytes() if p.exists() else None
        return self.data[relative]

    def text(self, relative, default=""):
        data = self.read(relative)
        return data.decode("utf-8") if data is not None else default

    def json(self, relative, default=None):
        data = self.read(relative)
        return json.loads(data) if data is not None else default

    def tsv(self, relative):
        text = self.text(relative)
        return list(csv.DictReader(io.StringIO(text), delimiter="\t")) if text else []

    def files(self, folder, pattern):
        paths = sorted(p.relative_to(self.root).as_posix()
                       for p in (self.root / folder).glob(pattern))
        self.directories[(folder, pattern)] = paths
        return paths

    def sha(self, relative):
        data = self.read(relative)
        return digest(data) if data is not None else None

    def stable(self):
        for relative, data in self.data.items():
            p = self.root / relative
            current = p.read_bytes() if p.exists() else None
            if current != data:
                return False
        for (folder, pattern), paths in self.directories.items():
            current = sorted(p.relative_to(self.root).as_posix()
                             for p in (self.root / folder).glob(pattern))
            if current != paths:
                return False
        return True


def project_sources(s, checked, english, editorial, annotations, guide_paths):
    """Use the generator's pure functions without writing any generated file."""
    metadata = {r["key"]: r for r in s.tsv("records/PAGE_MAP.tsv")}
    for name in [
        "templates/preamble.tex", "templates/frontmatter.tex",
        "templates/hand_renderer.tex", "templates/source_glyphs.tex",
        "templates/retained_usages_fr.tex", "RELEASE_STATUS.json",
        "scripts/build_edition.py", "scripts/edition_core.py",
    ]:
        s.read(name)
    marked, frvars, pending = {}, [], []
    for key in sorted(checked, key=lambda k: (k.startswith("esq119"), int(k.rsplit("_", 1)[1]))):
        cleaned, events = clean_latex(checked[key])
        pending.extend({"key": key, **event} for event in events)
        if key.startswith("esq_"):
            marked[key], variants = annotate(cleaned, key, editorial)
            frvars.extend(variants)
        else:
            marked[key] = cleaned
    frpages, frnotes, frnote_status = link_notes(marked, metadata)
    frpages = attach_copy2(frpages, annotations, "FR", metadata)
    fr_by_id = {v["id"]: v for v in frvars}
    enpages, envars, ensource = {}, [], []
    for key, text in english.items():
        text, events = clean_latex(text)
        pending.extend({"key": key, "language": "EN", **event} for event in events)
        for m in macros(text, {"var"}):
            old, new, kind, ident = m.arguments
            if ident not in fr_by_id:
                raise ValueError("English variant has no French variant: " + ident)
            v = dict(fr_by_id[ident])
            v.update(page_reading=old, corrected_reading=new, kind=kind)
            envars.append(v)
        for m in macros(text, {"frapparatus"}):
            ident = m.arguments[0]
            if ident not in fr_by_id:
                raise ValueError("French-source apparatus ID has no French variant: " + ident)
            v = dict(fr_by_id[ident])
            v["source_apparatus"] = True
            ensource.append(v)
        enpages[key] = text
    enpages, ennotes, ennote_status = link_notes(enpages, metadata)
    enpages = attach_copy2(enpages, annotations, "EN", metadata)
    documents = {}
    for form, (language, name, _, _, _) in FORMS.items():
        pages, variants, notes = ((frpages, frvars, frnotes) if language == "FR"
                                  else (enpages, envars + ensource, ennotes))
        documents[f"{language}/{name}.tex"] = make_document(
            s.root, form, metadata, pages, variants, notes)
    for language, form in [
        ("FR", "FR_corrige_apparat"), ("EN", "EN_corrected_translator_notes"),
    ]:
        pages, variants, notes = ((frpages, frvars, frnotes) if language == "FR"
                                  else (enpages, envars + ensource, ennotes))
        documents[f"{language}/ESQUISSE_{language}_master_annotated.tex"] = make_document(
            s.root, form, metadata, pages, variants, notes, master=True)
    if guide_paths:
        document = make_document(
            s.root, "EN_corrected_translator_notes", metadata, {}, [], "", guide=True)
        end = document.index(r"\end{document}")
        document = document[:end] + "\n\n".join(s.text(p) for p in guide_paths) + "\n" + document[end:]
        document = document.replace(
            r"\newcommand{\EditionTitle}{Sketch of a Program}",
            r"\newcommand{\EditionTitle}{A Guide to the Esquisse}")
        document = document.replace(
            r"\newcommand{\EditionForm}{Corrected text with translator’s notes}",
            r"\newcommand{\EditionForm}{Commentary for a mathematical reader}")
        document = document.replace(
            PREFACES["EN_corrected_translator_notes"],
            "This guide follows the sommaire, sections 1–10 and notes (1)–(7) in the order of the typescript. Page references give the original typescript pagination and link to the archive. The guide is based on the checked text and collation; it does not change the text’s mathematics.")
        document = document.replace(
            "AI-translated by GPT-6 Astra (OpenAI, ChatGPT Pro mode).", "")
        documents["GUIDE/ESQUISSE_GUIDE.tex"] = document
    return {
        "documents": documents, "frvars": frvars, "envars": envars,
        "ensource": ensource, "pending_cleanup": pending,
        "note_status": {"FR": frnote_status, "EN": ennote_status},
    }


def pdf_records(s, projection):
    checks = s.json("PDF_CHECKS.json", {})
    audits = s.json("FINAL_PDF_AUDIT.json", {})
    observations = s.tsv("VISUAL_QA.tsv")
    output = []
    for stem, role, purpose in DOCUMENTS:
        name = stem.rsplit("/", 1)[1]
        tex = stem + ".tex"
        pdf = stem + ".pdf"
        build = s.json("build_logs/" + name + ".json", checks.get(name, {}))
        audit = audits.get(name, {})
        source_sha = s.sha(tex)
        pdf_sha = s.sha(pdf)
        compiled = bool(source_sha and build.get("source_sha256") == source_sha)
        compiled_pdf = bool(pdf_sha and build.get("pdf_sha256") == pdf_sha
                            and build.get("pdf_compilation_succeeded") is True)
        current = bool(pdf_sha and audit.get("pdf_sha256") == pdf_sha
                       and audit.get("source_sha256") == source_sha
                       and audit.get("compiled_source_matches")
                       and audit.get("compiled_pdf_matches")
                       and not audit.get("upstream_input_mismatches"))
        seen = sorted({int(r["pdf_page"]) for r in observations
                       if r["reader"] == name and r["pdf_sha256"] == pdf_sha
                       and r["status"] == "visually inspected"})
        required = audit.get("required_visual_pages", []) if current else []
        fresh = s.text(tex) == projection["documents"].get(tex, object())
        source_status = s.text(tex).splitlines()
        source_status = source_status[0].removeprefix("% ") if source_status else "source absent"
        clean = all(not build.get(k) for k in [
            "errors", "missing_characters",
            "ink_outside_sheet", "ink_outside_type_area",
        ]) and not any(float(box.get("points", 0)) > 2 for box in build.get("overfull", []))
        passes = bool(build.get("runs")) and all(x.get("exit_code") == 0 for x in build["runs"])
        links = current and not audit.get("link_count_mismatches")
        apparatus = (current and "apparatus_entry_mismatches" in audit
                     and not audit["apparatus_entry_mismatches"])
        notes = current and audit.get("endnote_link_audit", {}).get("problems") == 0
        footnotes = current and all(x.get("same_physical_page") for x in audit.get("author_footnote_placements", []))
        visual = current and bool(required) and set(required) <= set(seen)
        ready = fresh and compiled and compiled_pdf and passes and clean and links and apparatus and notes and footnotes and visual
        output.append({
            "name": name, "stem": stem, "role": role, "purpose": purpose,
            "tex": tex, "pdf": pdf, "source_sha": source_sha, "pdf_sha": pdf_sha,
            "build": build, "audit": audit, "audit_current": current,
            "compiled_current": compiled, "source_current": fresh,
            "compiled_pdf_current": compiled_pdf,
            "seen": seen, "required": required,
            "remaining": sorted(set(required) - set(seen)),
            "status": source_status, "ready": ready,
            "build_ready": fresh and compiled and compiled_pdf and passes and clean,
        })
    return output


def generate(s):
    checked_paths = s.files("checked_pages", "*.tex")
    english_paths = s.files("translated_pages", "*.tex")
    guide_paths = s.files("guide_fragments", "*.tex")
    checked = {Path(p).stem: s.text(p) for p in checked_paths}
    english = {Path(p).stem: s.text(p) for p in english_paths}
    units = [p for p in guide_paths if "preface" not in Path(p).stem.lower()]
    prefatory = [p for p in guide_paths if p not in units]
    decisions = s.tsv("CHECK_DECISIONS.tsv")
    differences = s.tsv("DIFFERENCES_OUTCOMES.tsv")
    collation = s.tsv("COLLATION.tsv")
    pairs = s.tsv("records/COLLATION_PAGE_COVERAGE.tsv")
    adjudications = s.tsv("records/EDITORIAL_ADJUDICATIONS.tsv")
    editorial = s.json("editorial_variants.json", [])
    annotations = s.json("copy2_annotations.json", [])
    separate = [a for a in annotations if not a.get("merged_into_variant")]
    merged = [a for a in annotations if a.get("merged_into_variant")]
    inventory = s.tsv("records/SOURCE_PAGE_INVENTORY.tsv")
    integrity = s.json("records/SOURCE_INTEGRITY.json", {})
    progress = s.json("records/AUDIT_PROGRESS.json", {})
    index = s.json("translated_pages/TRANSLATION_INDEX.json", [])
    build_inputs = s.json("BUILD_INPUTS.json", {})
    release = s.json("RELEASE_STATUS.json", {})
    release_validation = s.json("records/RELEASE_VALIDATION.json", {})
    projection = project_sources(s, checked, english, editorial, annotations, guide_paths)
    pdfs = pdf_records(s, projection)
    checked_counts = Counter(2 if k.startswith("esq119") else 1 for k in checked)
    validated = []
    for key in checked:
        status = s.json("reviews/" + key + "_status.json", {})
        review = s.json("reviews/" + key + ".json", {})
        if (status.get("finalized") and status.get("checked_sha256") == s.sha("checked_pages/" + key + ".tex")
                and len(review.get("inspected_images", [])) == 2
                and review.get("full_text_confirmation")):
            validated.append(key)
    index_current = (
        len(index) == 58 and {r["key"] for r in index} == set(english)
        and all(r.get("source_sha256") == s.sha(r["source"])
                and r.get("translation_sha256") == s.sha(r["translation"]) for r in index)
    )
    pair_current = all(
        all(r.get(f"copy{n}_checked_sha256") == s.sha("checked_pages/" + r[f"copy{n}_key"] + ".tex")
            for n in [1, 2])
        and r.get("full_inspection") and r.get("original_transcription_comparison")
        for r in pairs)
    progress_current = (
        progress.get("checked_pages") == len(checked)
        and progress.get("decision_rows") == len(decisions)
        and progress.get("difference_outcomes") == len(differences)
        and progress.get("collation_rows") == len(collation)
        and progress.get("collated_page_pairs") == len(pairs)
        and progress.get("editorial_wording_loci") == len(adjudications)
        and {p["key"] for p in progress.get("pages", [])} == set(checked)
        and all(p.get("sha256") == s.sha("checked_pages/" + p["key"] + ".tex")
                for p in progress.get("pages", []))
    )
    fr_ids = {v["id"] for v in projection["frvars"]}
    en_ids = [v["id"] for v in projection["envars"] + projection["ensource"]]
    aligned = fr_ids == set(en_ids) and len(en_ids) == len(set(en_ids))
    tnotes = sum(len(list(macros(t, {"tnote"}))) for t in english.values())
    math_count = sum(len(x.get("math_fragments", [])) for x in index)
    diagram_count = sum(len(x.get("diagram_fragments", [])) for x in index)
    unique_differences = len({r["difference_id"] for r in differences})
    source_current = sum(p["source_current"] for p in pdfs)
    validation_current = bool(release_validation.get("passed")) and all(
        release_validation.get("documents", {}).get(p["name"], {}).get("source_sha256") == p["source_sha"]
        and release_validation.get("documents", {}).get(p["name"], {}).get("pdf_sha256") == p["pdf_sha"]
        for p in pdfs)
    final_preface = bool(prefatory) and not any(
        "WORKING COLLATION PREFACE" in s.text(p) for p in prefatory)
    gates = [
        ("Both supplied manifests verified", set(integrity) == {"ESQUISSE_TEXT.zip", "ESQUISSE_SCANS.zip"}
         and len(integrity.get("ESQUISSE_TEXT.zip", [])) == 143
         and len(integrity.get("ESQUISSE_SCANS.zip", [])) == 232
         and all(r.get("verified") for rows in integrity.values() for r in rows),
         "; ".join(f"{name}: {sum(bool(r.get('verified')) for r in rows)}/{len(rows)}" for name, rows in integrity.items())),
        ("All 116 scan pages explicitly reviewed", len(validated) == 116 and len(checked) == 116,
         f"{len(validated)} current finalized review declarations; copy 1 {checked_counts[1]}/58, copy 2 {checked_counts[2]}/58"),
        ("All 468 original differences decided", unique_differences == 468
         and not any(r["outcome"].startswith(("pending", "proposed")) for r in differences),
         f"{unique_differences}/468 unique outcome rows"),
        ("All 58 page pairs collated against current files", len(pairs) == 58 and pair_current,
         f"{len(pairs)}/58 pair declarations; recorded hashes current: {yes(pair_current)}"),
        ("Complete source and editorial validator current", progress_current
         and progress.get("status") == "complete" and not progress.get("errors"),
         f"validator status: {progress.get('status', 'absent')}; snapshot current: {yes(progress_current)}"),
        ("Complete English translation and exact formula index current", index_current,
         f"{len(english)}/58 pages; {math_count} math fragments and {diagram_count} complete diagram; index current: {yes(index_current)}"),
        ("French IDs aligned with the English apparatus", aligned,
         f"{len(fr_ids)} French IDs; {len(projection['envars'])} English wording variants and {len(projection['ensource'])} French-source notes"),
        ("Guide units and completed collation preface present", len(units) == 18 and final_preface,
         f"{len(units)}/18 commentary units; completed collation preface: {yes(final_preface)}"),
        ("No unintegrated mechanical TeX repairs", not projection["pending_cleanup"],
         f"{len(projection['pending_cleanup'])} current projection repairs awaiting integration"),
        ("All standalone sources regenerated from current inputs", source_current == len(DOCUMENTS),
         f"{source_current}/{len(DOCUMENTS)} files match the generator's current projection"),
        ("All eight PDFs have current successful builds", all(p["build_ready"] for p in pdfs),
         f"{sum(p['build_ready'] for p in pdfs)}/{len(pdfs)} current builds without recorded errors, boxes exceeding 2 pt, missing glyphs or geometry violations"),
        ("All eight PDFs pass recorded links and visual QA", all(p["ready"] for p in pdfs),
         f"{sum(p['ready'] for p in pdfs)}/{len(pdfs)} pass all current-hash checks"),
        ("Release status explicitly final", bool(release.get("final")),
         f"RELEASE_STATUS.json final: {yes(release.get('final'))}"),
        ("Authoritative release validator passes for the current PDFs", validation_current,
         f"records/RELEASE_VALIDATION.json passed: {yes(release_validation.get('passed'))}; current document hashes: {yes(validation_current)}"),
    ]
    complete = all(ok for _, ok, _ in gates)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    lines = [
        "# Esquisse d'un programme — readers and review records",
        "",
        ("**FINAL EDITION — the recorded release gates below pass.**" if complete else
         "**INCOMPLETE WORKING EDITION — this snapshot has not passed all release gates.**"),
        "",
        f"README snapshot generated {now} by {link('scripts/write_readme.py')}. "
        "Counts below describe the files read for this snapshot. Earlier checkpoints and earlier PDFs retain their own histories. "
        "A full translation source or a successful partial compilation does not establish completion of the two-copy collation or the final visual review.",
        "",
        "## Scope and source coordinates",
        "",
        "The edition concerns Alexander Grothendieck's January 1984 "
        "*Esquisse d'un programme*, Université de Montpellier, fonds Grothendieck, cote 119. "
        "Copy 1 comprises the sommaire and typescript pages 1–57 at archive sites 2–59; "
        "copy 2 comprises the corresponding 58 pages at sites 78–135. "
        "The archive viewer's PDF page is the site number plus one. "
        "Every source-page link is taken from " + link("records/PAGE_MAP.tsv") + ".",
        "",
        "The supplied text and scan manifests are retained as verified inventory outcomes in "
        + link("records/SOURCE_INTEGRITY.json") + " and summarized in "
        + link("records/SOURCE_INVENTORY.md") + ". Each source page was supplied as two overlapping image halves. "
        "A checked page requires an explicit observation of both halves; file presence and prior transcription alone do not constitute inspection. "
        "The source readings in this edition are decided from those scans. Published editions supply no replacement readings.",
        "",
        "## Three ZIP layouts",
        "",
        table(["Archive", "Paths retained at its root", "Contents"], PACKAGES),
        "",
        "The same README accompanies all three archives. Paths below are relative to their combined edition root. "
        "Extract the three delivery ZIPs into one directory, preserving FR/, EN/, GUIDE/ and the shared paths. "
        "For the complete source-validation workflow, extract the two supplied input archives separately as follows, "
        "from the directory containing the ZIP files:",
        "",
        FENCE + "sh",
        "mkdir -p work/edition work/source work/images",
        "unzip -o ESQUISSE_READERS_FR.zip -d work/edition",
        "unzip -o ESQUISSE_READERS_EN.zip -d work/edition",
        "unzip -o ESQUISSE_READERS_RECORDS.zip -d work/edition",
        "unzip -o ESQUISSE_TEXT.zip -d work/source",
        "unzip -o ESQUISSE_SCANS.zip -d work/images",
        FENCE,
        "",
        "The scan files then lie under work/images/scans/. The supplied archives are inputs and are not repackaged inside the delivery ZIPs. "
        "A standalone reader .tex can be compiled independently of the records ZIP and the supplied scan images.",
        "",
        "## Documents",
        "",
        table(["Role", "Files", "Purpose"], [
            (role, link(stem + ".tex", ".tex") + " · " + link(stem + ".pdf", "PDF"), purpose)
            for stem, role, purpose in DOCUMENTS
        ]),
        "",
        "The diplomatic reader contains both copies in order. The corrected French and English forms use copy 1 as the base. "
        "The guide keeps the eighteen requested commentary paragraphs in source order; its additional collation preface is counted separately. "
        "The annotated masters and their compiled PDFs expose the reusable apparatus-bearing sources.",
        "",
        "## Form generation and variant policy",
        "",
        "The source of record is " + code("checked_pages/") + ". "
        + code("editorial_variants.json") + " contains only explicitly approved editorial changes with exact old/new TeX strings, bilingual reasons and stable evidence IDs. "
        + code("annotated_pages/") + " is generated without overwriting those checked files. "
        + code("scripts/build_edition.py") + " then embeds the common macros, font/glyph definitions, page bodies, variant declarations and note links into each standalone source.",
        "",
        "A changed reading is represented by "
        + code(r"\var{page reading}{corrected reading}{kind}{id}") + ". "
        "The diplomatic projection selects the first argument. The corrected projections select the second; "
        "the apparatus projection also prints the reason under that ID. The reading projection suppresses the apparatus marker and note. "
        "Unchanged handwriting retains its source macro and receives no variant merely for being handwritten.",
        "",
        table(["Form", "Text selected", "Apparatus and source marks"], [
            ("FR diplomatic", "Checked readings of copy 1 and copy 2", "Typed/handwritten distinctions, deletions, insertions, overwriting, marginal material, underlining, foliation and doubts remain."),
            ("FR corrected with apparatus", "Corrected copy 1", "Approved variants and separately identified copy 2 annotations are printed; the author's notes and doubts remain."),
            ("FR reading", "The same corrected copy 1", "Editorial apparatus is suppressed; authorial notes and doubts remain; scan and source-page labels move to the margin."),
            ("EN corrected with translator's notes", "Translation of corrected copy 1", "Meaningful English variants use the corresponding French IDs; unchanged English clauses carry French-source notes; translator's notes and copy 2 notes remain distinct."),
            ("EN reading", "The same English translation", "Editorial apparatus and translator's notes are suppressed; authorial notes, doubts, and marginal scan/page labels remain."),
        ]),
        "",
        "An isolated French typing slip is corrected only through an approved evidence record. "
        "Its English clause receives an English wording variant only when the correction changes the English wording. "
        "Otherwise " + code(r"\frapparatus{French-id}") + " prints the French old/new readings and their English explanation at the corresponding clause, "
        "without creating an English wording variant. "
        + code(r"\tnote{TN-site-number}{English explanation}") + " identifies translator's notes separately. "
        "The shared French IDs, including Ladegraillerie → Ladegaillerie and the English wording change hyperquadratic → hyperquadric, are aligned in "
        + link("translated_pages/FRENCH_APPARATUS_ALIGNMENT.tsv") + " and "
        + link("translated_pages/TRANSLATION_INDEX.json") + ".",
        "",
        "Copy 2 revisions are recorded in the collation and in "
        + code("copy2_annotations.json") + ". A copy 2 correction enters the corrected copy 1 text only when explicitly approved as correcting a typing slip shared by the two copies. "
        "The source annotation then names its " + code("merged_into_variant") + " ID; its evidence remains in the records, while its printed explanation is merged into that one shared variant. "
        "Other copy 2 deletions, additions, move marks and marginal marks remain identified as copy 2 evidence. "
        "Common handwriting is recorded under the explicitly approved collation kind “handwriting in both copies”, with both readings and evidence links; "
        + link("records/COLLATION_COMMON_MARKS.tsv") + " is a verbatim companion subset of the full collation.",
        "",
        "Stable IDs distinguish original differences (D1-001–D1-327; D2-001–D2-141), "
        "source lines (L-page-key-line), macros (M-page-key-occurrence), original note items (N-page-key-item), "
        "scan decisions (C-page-key-number), collation loci (COL-119-site-number), "
        "French slips (V-FR-site-number), copy 2 notes (A2-119-site-number), and translator's notes (TN-site-number). "
        "Automatic authorial deletion/insertion/overwriting variants use V-page-key-kind-number. "
        "The exact schemas are in " + link("records/AUDIT_SCHEMA.md") + ".",
        "",
        "## Retained source usages, doubts and mathematical content",
        "",
        "The French forms retain recurring usages including Légo-Teichmüller, bidimensionelle/bidimensionelles, "
        "boite, arètes, polygône/polygônes, occurence, résidual and points bases. "
        "They also retain checked source naming such as the singular title Histoire de Modèles. "
        "On typescript p. 36, the diplomatic form preserves pro-gressées; the corrected forms print pro-gressée, "
        "following copy 2's deletion of the terminal s and retaining the preceding e and source line division. "
        "The individual retention reasons, as well as the approved isolated slips, are recorded in "
        + link("records/EDITORIAL_ADJUDICATIONS.tsv") + "; superseded decisions remain in its history table. "
        "A spelling or agreement rule alone does not silently replace a source reading.",
        "",
        "Uncertain readings retain " + code(r"\unsure{...}") + " and illegibility retains "
        + code(r"\illegible{...}") + ", with links to their particular scans in every reader. "
        "Doubtful dots and unresolved alternatives are retained at the translated anchors and explained where necessary. "
        "The rounded open mathematical glyph recorded as "
        + code(r"\unsure{\sourceglyph{119A}}") + " preserves an individually inspected contour without assigning a conventional alphabet. "
        "Its vector, coordinate transformation and provenance are documented in "
        + link("records/SOURCE_GLYPHS.md") + ", "
        + link("records/SOURCE_GLYPH_119A.json") + " and "
        + link("records/SOURCE_GLYPH_USAGE.tsv") + ". The vector definition is embedded in each standalone source.",
        "",
        "The English formulas preserve the exact checked French TeX fragments, including source peculiarities and the complete diagram. "
        "The translation index compares their ordered strings and records both source hashes. "
        "The guide discusses identified mathematical difficulties using explicit maps or calculations and exact source references; "
        "those discussions do not alter the readers' formulas. "
        "The source's authorial notes (1)–(7) remain at the end, with every call linked to its note and every note linked back to its calls. "
        "Local (*) and (**) authorial notes remain associated with their source-page text. "
        "Marginal content of more than three rendered lines is set as a labeled block; shorter content uses the reserved margin. "
        "Handwritten archive foliation is preserved without attributing its hand to the author.",
        "",
        "English terminology follows the supplied unified glossary and standardization instructions. "
        "The guide's references to later literature are named and sourced without borrowing their readings of the Esquisse. "
        "Checked external reference details are in " + link("guide_fragments/EXTERNAL_REFERENCES.tsv") + ".",
        "",
        "## Current source and apparatus counts",
        "",
        table(["Measure", "Current value", "Evidence"], [
            ("Checked copy 1 pages", f"{checked_counts[1]}/58", "checked_pages/ and reviews/"),
            ("Checked copy 2 pages", f"{checked_counts[2]}/58", "checked_pages/ and reviews/"),
            ("Current finalized page declarations", f"{len(validated)}/116", "Matching checked hashes and explicit two-image/full-text declarations"),
            ("Scan-decision rows", len(decisions), "CHECK_DECISIONS.tsv"),
            ("Original difference outcomes", f"{unique_differences}/468", "DIFFERENCES_OUTCOMES.tsv"),
            ("Collated page pairs", f"{len(pairs)}/58", "records/COLLATION_PAGE_COVERAGE.tsv"),
            ("Individual collation loci", len(collation), "COLLATION.tsv"),
            ("Editorial wording-locus adjudications", len(adjudications), "records/EDITORIAL_ADJUDICATIONS.tsv"),
            ("Approved isolated French slips", len(editorial), "editorial_variants.json"),
            ("English source pages", f"{len(english)}/58", "translated_pages/"),
            ("Exact math fragments in translation index", math_count, "TRANSLATION_INDEX.json; current hashes: " + yes(index_current)),
            ("Complete diagrams in translation index", diagram_count, "TRANSLATION_INDEX.json"),
            ("Translator's notes", tnotes, "tnote markers in translated_pages/"),
            ("Guide commentary units", f"{len(units)}/18", "guide_fragments/ excluding filenames containing preface"),
            ("Additional guide prefatory units", len(prefatory), "guide_fragments/"),
            ("Copy 2 annotation records", len(annotations), "copy2_annotations.json"),
            ("Copy 2 notes printed separately", len(separate), "Records without merged_into_variant"),
            ("Copy 2 records merged into shared variants", len(merged), "Records with merged_into_variant"),
        ]),
        "",
        "These are current input counts. The last generated build records report "
        f"{build_inputs.get('checked_pages', 'unrecorded')} checked pages, "
        f"{build_inputs.get('translated_pages', 'unrecorded')} translated pages and "
        f"{build_inputs.get('french_variants', 'unrecorded')} French variants. "
        "Any difference from the current inputs requires regeneration; the per-document freshness checks below also detect content changes that leave counts unchanged.",
        "",
        "### Decision and collation outcomes",
        "",
        table(["Record", "Outcome or kind", "Count"], [
            *[("Scan decisions", k, n) for k, n in sorted(Counter(r["decision"] for r in decisions).items())],
            *[("Original differences", k, n) for k, n in sorted(Counter(r["outcome"] for r in differences).items())],
            *[("Collation", k, n) for k, n in sorted(Counter(r["kind"] for r in collation).items())],
            *[("Editorial consideration", k, n) for k, n in sorted(Counter(r["editorial_outcome"] for r in adjudications).items())],
        ]),
        "",
        "### Doubt marks before and after review",
        "",
    ]
    doubt_rows = []
    for copy in [1, 2]:
        all_original = [r for r in inventory if int(r["copy"]) == copy]
        reviewed_original = [r for r in all_original if r["key"] in checked]
        current = Counter(m.name for k, t in checked.items()
                          if (2 if k.startswith("esq119") else 1) == copy
                          for m in macros(t, {"unsure", "illegible"}, recursive=True))
        for label, rows in [("original complete copy", all_original), ("original pages now checked", reviewed_original)]:
            doubt_rows.append((copy, label, len(rows),
                               sum(int(r.get("unsure", 0)) for r in rows),
                               sum(int(r.get("illegible", 0)) for r in rows)))
        doubt_rows.append((copy, "current checked pages", checked_counts[copy],
                           current["unsure"], current["illegible"]))
    lines += [
        table(["Copy", "Scope", "Pages", "unsure", "illegible"], doubt_rows),
        "",
        "The original counts come from the supplied-source inventory; current counts parse the checked pages, including nested doubt macros. "
        "Review can add a newly observed doubt as well as resolve an earlier one, so subtraction of these totals is not a count of resolved loci. "
        "Each decision and its prior state remain traceable in the review records.",
        "",
        "### Apparatus entries by form and kind, cote 119",
        "",
    ]
    apparatus_rows = [
        ("FR diplomatic", "editorial apparatus", 0),
        ("FR reading", "editorial apparatus", 0),
        ("EN reading", "editorial apparatus and translator's notes", 0),
    ]
    for label, variants in [
        ("FR corrected", projection["frvars"]),
        ("EN corrected: English wording", projection["envars"]),
        ("EN corrected: French-source note", projection["ensource"]),
    ]:
        apparatus_rows += [(label, kind, n) for kind, n in sorted(Counter(v["kind"] for v in variants).items())]
    for label in ["FR corrected", "EN corrected"]:
        apparatus_rows += [(label, "copy 2: " + kind, n)
                          for kind, n in sorted(Counter(a["kind"] for a in separate).items())]
    apparatus_rows.append(("EN corrected", "translator's note", tnotes))
    lines += [
        table(["Form or entry class", "Kind", "Current input count"], apparatus_rows),
        "",
        "French-source notes explain the French correction at an unchanged English clause and are counted separately from English wording variants. "
        "Merged copy 2 evidence is counted once under its shared variant. "
        "The generator's last emitted apparatus table is " + link("APPARATUS_COUNTS.md")
        + "; actual printed-entry IDs and counts are checked against the PDF build log in the final audit.",
        "",
        "## Per-PDF build, link and visual-review status",
        "",
        "The build columns report the latest sanitized build record for each named file. "
        "A PDF is current only after its standalone source matches the current inputs, its compiled-source hash matches that source, "
        "and the final audit records the exact current PDF hash. A row with a stale or absent audit does not certify current links or geometry.",
        "",
        table(["Document", "PDF pages", "Errors", "Warnings", "Overfull / widest pt", "Missing glyphs", "Source / compiled source / compiled PDF current"], [
            (p["role"], p["build"].get("pdf_pages", "—"),
             len(p["build"].get("errors", [])), len(p["build"].get("warnings", [])),
             f"{len(p['build'].get('overfull', []))} / {max((x.get('points', 0) for x in p['build'].get('overfull', [])), default=0):g}",
             len(p["build"].get("missing_characters", [])),
             yes(p["source_current"]) + " / " + yes(p["compiled_current"]) + " / " + yes(p["compiled_pdf_current"]))
            for p in pdfs
        ]),
        "",
        table(["Document", "Archive / all external / internal link annotations", "Final audit current", "Required pages inspected for exact PDF", "Outside sheet / text area"], [
            (p["role"],
             f"{p['build'].get('archive_link_annotations', '—')} / {p['build'].get('external_link_annotations', '—')} / {p['build'].get('internal_link_annotations', '—')}",
             yes(p["audit_current"]),
             f"{len(set(p['seen']) & set(p['required']))}/{len(p['required'])}" if p["audit_current"] else "current audit required",
             f"{len(p['build'].get('ink_outside_sheet', []))} / {len(p['build'].get('ink_outside_type_area', []))}")
            for p in pdfs
        ]),
        "",
        "The required visual sample consists of forty pages spread through each reader and annotated master, or every page of a shorter document, "
        "plus every mandatory overflow/repair, landscape and special-glyph/diagram page identified by the audit. "
        "Rendering alone adds no inspection credit. "
        + link("VISUAL_QA.tsv") + " records actual page observations against the exact PDF SHA-256; observations for older PDF hashes remain as history. "
        "Permitted isolated glyph overhangs are reported separately from text-line, vector or image violations.",
        "",
    ]
    for p in pdfs:
        b, a = p["build"], p["audit"]
        lines += [
            "### " + p["role"],
            "",
            link(p["pdf"]) + " · " + link(p["tex"]),
            "",
            p["status"] + ".",
            "",
            "- PDF SHA-256: " + code(p["pdf_sha"] or "PDF absent") + ".",
            "- Standalone-source SHA-256: " + code(p["source_sha"] or "source absent") + ".",
            "- Last recorded compilation: " + str(b.get("compiled_at", "absent")) + ".",
            "- Current input projection matches source: " + yes(p["source_current"])
            + "; compiled-source hash matches source: " + yes(p["compiled_current"])
            + "; successful compilation PDF hash matches current PDF: " + yes(p["compiled_pdf_current"])
            + "; final audit matches current PDF and source: " + yes(p["audit_current"]) + ".",
        ]
        if p["audit_current"]:
            lines += [
                f"- Logical external links expected: {a.get('expected_link_count', 'unrecorded')}; PDF external annotations: {a.get('pdf_external_link_annotations', 'unrecorded')}; target-count discrepancies: {len(a.get('link_count_mismatches', []))}.",
                f"- Projected apparatus entries: {a.get('source_apparatus_entries', 'unrecorded')}; executed: {a.get('executed_apparatus_entries', 'unrecorded')}; printed: {a.get('printed_apparatus_entries', 'unrecorded')}; ID discrepancies: {len(a.get('apparatus_entry_mismatches', [])) if 'apparatus_entry_mismatches' in a else 'audit required'}.",
                f"- Authorial endnote-link problems: {a.get('endnote_link_audit', {}).get('problems', 'audit required')}; local-footnote placement problems: {sum(not x.get('same_physical_page') for x in a.get('author_footnote_placements', []))}.",
                "- Required pages: " + page_list(p["required"]) + ".",
                "- Required pages still uninspected: " + page_list(p["remaining"]) + ".",
            ]
        else:
            lines.append("- Link targets, printed apparatus, footnote placement and required-page coverage await an audit of the current file.")
        lines.append("- Pages with actual observations for this PDF hash: " + page_list(p["seen"]) + ".")
        for field, label in [("errors", "Error"), ("warnings", "Warning"), ("missing_characters", "Missing character")]:
            for item in b.get(field, []):
                rendered = item if isinstance(item, str) else json.dumps(item, ensure_ascii=False)
                lines.append("- " + label + ": " + rendered.replace("\n", " "))
        lines.append("")
    lines += [
        "## Release gates",
        "",
        table(["Gate", "Status", "Current evidence"], [
            (name, "PASS" if ok else "OPEN", detail) for name, ok, detail in gates
        ]),
        "",
        "This README never changes " + code("RELEASE_STATUS.json")
        + " and never supplies missing review observations. Final release status must agree with completed source validation, "
        "current generated files, successful PDF audits and recorded visual inspection. "
        "Changing any source or macro can change a PDF hash and therefore requires the corresponding fresh PDF audit and visual record.",
        "The authoritative release gate is " + link("scripts/validate_release.py")
        + "; its machine-readable result is " + link("records/RELEASE_VALIDATION.json") + ". "
        "It replays complete scan and collation validation, verifies original input integrity, current generation and PDF hashes, exact mathematics, shared master bodies, credits, standalone sources, every required visual page and checkpoint reconciliation. "
        "The README summarizes the available records; the guarded packaging command reruns the authoritative gate.",
        "",
        "## Reproducible compilation and full rebuild",
        "",
        "### Compile one standalone document",
        "",
        "Use a working TeX Live installation with LuaLaTeX, Latin Modern, French and English babel support, "
        "fontspec, amsmath/amssymb, ulem, xcolor, graphicx, TikZ/tikz-cd, marginnote, etoolbox, microtype and hyperref. "
        "From the combined edition root, the following example runs three passes for stable cross-references:",
        "",
        FENCE + "sh",
        "cd EN",
        "lualatex -interaction=nonstopmode -halt-on-error -file-line-error ESQUISSE_EN_reading.tex",
        "lualatex -interaction=nonstopmode -halt-on-error -file-line-error ESQUISSE_EN_reading.tex",
        "lualatex -interaction=nonstopmode -halt-on-error -file-line-error ESQUISSE_EN_reading.tex",
        "cd ..",
        FENCE,
        "",
        "Substitute another .tex filename in FR/, EN/ or GUIDE/ to compile that document. "
        "Each source embeds its required edition macros and source-glyph contour; it has no external page-file or image dependency. "
        "A new TeX environment can change pagination or PDF bytes, so a locally rebuilt PDF needs its own recorded audit and visual inspection.",
        "",
        "### Regenerate all forms from the review records",
        "",
        "Python 3 is required for generation and record processing. PyMuPDF is required for PDF link and geometry measurements; "
        "Pillow is used for the rendered review sheets. The optional source-glyph tracing helper also uses NumPy and Matplotlib. "
        "With all three delivery archives combined in work/edition and the inputs extracted as above, run from that edition root:",
        "",
        FENCE + "sh",
        "python scripts/audit_validate.py --complete",
        "python translated_pages/attach_fr_apparatus.py",
        "python translated_pages/refresh_index.py",
        "python scripts/build_edition.py generate",
        "python scripts/compile_readers.py --passes 3",
        "python scripts/pdf_final_audit.py --render",
        FENCE,
        "",
        "The complete validator intentionally reports failure while any of the 116 pages, 468 differences or 58 page pairs remains unchecked. "
        "Without " + code("--complete") + ", it validates the current reviewed subset and records its incomplete scope. "
        "The generation command refreshes annotated pages, both masters, every reader, the guide, coverage tables, variant register, note links and apparatus counts. "
        "The compiler writes sanitized logs and measured results; " + code("--names") + " selects particular document stems. "
        "The final-audit command compares projected scan/doubt links, apparatus IDs, authorial note links, physical note placement and required visual-page coverage.",
        "",
        "Open and inspect the rendered page images before recording observations. The locking helper accepts a JSON list containing "
        + code("reader") + ", " + code("pdf_sha256") + ", " + code("pdf_page") + ", "
        + code("observation") + " and " + code("phase") + ". It rejects an observation when the PDF hash has changed. "
        "With actual observations saved in records/visual_observations.json, the remaining commands are:",
        "",
        FENCE + "sh",
        "python scripts/record_visual_qa.py records/visual_observations.json",
        "python scripts/pdf_final_audit.py",
        "python scripts/write_readme.py",
        FENCE,
        "",
        "After the completed collation preface, final source status, builds and visual records are in place, reconcile the checkpoints and run the authoritative gate. "
        "The package command repeats validation and reconciliation, requires unchanged passing evidence, and refuses to overwrite an existing final package:",
        "",
        FENCE + "sh",
        "python scripts/release_bundle.py reconcile",
        "python scripts/validate_release.py",
        "python scripts/write_readme.py",
        "python scripts/release_bundle.py package",
        FENCE,
        "",
        "The execution environment used an isolated support tree because its installed TeX file databases, font support and French files were incomplete. "
        "That fallback is documented in " + link("scripts/ENVIRONMENT.md") + " and "
        + link("scripts/bootstrap_tex.py") + ". On a standard working TeX Live installation it is unnecessary. "
        "To reproduce that fallback from the edition root, run "
        + code("python scripts/bootstrap_tex.py ../tex-runtime") + " before the compile command. "
        "The helper downloads its explicitly listed archived TeX Live packages into the private runtime directory and does not alter the system installation.",
        "",
        "Standalone compilation and regeneration preserve source strings. Syntax-only repairs, such as removing redundant nested math delimiters or "
        "using TikZ's ampersand replacement inside the diagram macro, have exact before/after records. "
        + code("scripts/apply_mechanical_cleanup.py") + " is the controlled integration helper for such already-defined repairs; it records hash transitions and history. "
        "It is not a spelling or mathematical correction operation. "
        "The source review records and original attachments are required to replay their validation.",
        "",
        "## Record and helper inventory",
        "",
        table(["Path", "Role"], [
            ("CHECK_DECISIONS.tsv; reviews/; reviews/history/", "Every explicit scan decision, complete-page declaration and superseded observation."),
            ("DIFFERENCES_OUTCOMES.tsv", "Every original draft/transcription difference retained with its final scan outcome and stable decision links."),
            ("COLLATION.tsv; collation_reviews/; records/COLLATION_PAGE_COVERAGE.tsv", "Both readings at each collated locus, full four-image declarations and current checked-source hashes."),
            ("records/COLLATION_COMMON_MARKS.tsv", "Shared-handwriting rows reproduced from the complete collation."),
            ("editorial_variants.json; records/EDITORIAL_CANDIDATES.tsv; records/EDITORIAL_ADJUDICATIONS.tsv", "Approved corrections, their candidate evidence, and explicit correction/retention decisions."),
            ("copy2_annotations.json", "Bilingual copy 2 apparatus text and links, including records merged into a shared correction."),
            ("checked_pages/; annotated_pages/", "Checked diplomatic source files and the generated variant-bearing versions."),
            ("translated_pages/; guide_fragments/", "Complete English page translations, translator review history, math index, apparatus alignment and ordered guide prose."),
            ("guide_fragments/GUIDE_MATH_REVIEW.tsv; guide_fragments/verify_icosahedron_graph.py; guide_fragments/ICOSAHEDRON_GRAPH_CHECK.tsv", "Independent source-and-mathematics review of all 18 commentary units and seven explicit arguments, with a reproducible exact arithmetic check of the displayed 12-vertex graph."),
            ("VARIANTS.json; CHANGES.tsv; APPARATUS_COUNTS.md", "Generated variant register, old/new readings, stable IDs, reasons and counts by language/form/kind."),
            ("SOURCE_COVERAGE.tsv; TRANSLATION_COVERAGE.tsv; NOTE_LINKS.json", "Source hash recovery, literal math comparison, and every authorial endnote definition/call/return."),
            ("CLEANUP_LOG.tsv; MECHANICAL_CLEANUP.json; REVIEW_STAGE_CLEANUP.json; records/MECHANICAL_PATCHES.json", "Exact syntax-only repairs and their source IDs, replay order and hash transitions."),
            ("TYPESETTING_FIXES.tsv; TYPESETTING_REPORT.md", "Source locations, reasons and measured outcomes of typography repairs and PDF validation."),
            ("BUILD_INPUTS.json; BUILD_HISTORY.jsonl; PDF_CHECKS.json; build_logs/", "Actual generation scope, compilation history, sanitized logs and measured PDF properties."),
            ("FINAL_PDF_AUDIT.json; VISUAL_QA.tsv", "Exact-PDF link/apparatus/geometry and required-page audits, plus actual human/model visual observations."),
            ("MASTER_FORM_EQUIVALENCE.json; records/RELEASE_VALIDATION.json", "Shared-body equivalence of each language's forms and the authoritative complete release-gate outcome."),
            ("records/RELEASE_GATE_REVIEW.md", "Independent review of final content checks, evidence freshness and index/README/reconciliation sequencing, with the accepted remedies."),
            ("records/INDEPENDENT_TEXT_REVIEW.tsv; records/SECOND_READINGS.tsv", "Independent FR/EN/guide reading and targeted visual comparisons, with hashes and observations."),
            ("records/SOURCE_INTEGRITY.json; records/SOURCE_PAGE_INVENTORY.tsv; records/PAGE_MAP.tsv; packets/", "Manifest integrity, complete inventories, archive coordinates and source-review packets."),
            ("records/SOURCE_GLYPHS.md; records/SOURCE_GLYPH_119A.json; glyphs/", "Observed special-glyph provenance, vector transformations and inspected rendering probes."),
            ("scripts/; templates/", "Reproducible review, collation, generation, compilation, audit and rendering code plus reusable TeX definitions."),
            ("records/CHECKPOINTS.tsv; records/OMITTED_CHECKPOINT_FILES.tsv", "Earlier checkpoint identities and explicit reconciliation of files not repeated in the final archives."),
            ("records/CHECKPOINT_RECONCILIATION.tsv; records/CHECKPOINT_RECONCILIATION.md; records/FINAL_CONTENTS.tsv", "Every checkpoint member's final disposition, exact replacement diffs and the final three-archive content manifest."),
        ]),
        "",
        "The records ZIP retains the authored review history and reproducibility files. "
        "Unmodified input-table duplicates removed from earlier checkpoints are identified in "
        + link("records/OMITTED_CHECKPOINT_FILES.tsv") + " with their original archive location and reason. "
        "Runtime downloads, font caches, temporary TeX outputs and duplicate intermediate diagnostic renderings are reproducible intermediates; "
        "they are excluded from publication while sanitized logs, source hashes, measured results and actual review observations are retained. "
        "The diagnostic build baseline is recorded in " + link("ORIGINAL_BUILD_BASELINE.json") + "; its unchecked PDFs are not readers.",
        "",
        "## Credits and rights",
        "",
        "AI-transcribed by Claude Opus 5.5 (Anthropic, effort high, Message Batches API); checked against the scans, "
        "and this edition built, by GPT-6 Astra (OpenAI, ChatGPT Pro mode); prompts and records by Claude (Anthropic). "
        "AI-translated by GPT-6 Astra (OpenAI, ChatGPT Pro mode).",
        "",
        "The transcription of copy 1 was made with the text layer of the Grothendieck Circle's typeset *Esquisse* "
        "(" + code("EsquisseFr.pdf") + ") given to the transcribing model as a draft, to compare with after it had transcribed each page; "
        "every reading of this edition was decided on the scans.",
        "",
        "The published French text and English translation in *Geometric Galois Actions 1*, edited by L. Schneps and P. Lochak "
        "(Cambridge University Press, 1997), the Grothendieck Circle's typeset " + code("EsquisseFr.pdf") + ", "
        "and the Centre for Grothendieckian Studies' draft transcription G94d are named as published texts. They are not reproduced here.",
        "",
        "The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights, "
        "in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain under CC0 1.0. "
        "This edition is published for educational, non-profit purposes, and we claim no rights we do not hold. "
        "If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it down.",
        "",
    ]
    return "\n".join(lines), {
        "complete": complete, "checked_pages": len(checked),
        "translated_pages": len(english), "guide_units": len(units),
        "source_current": source_current, "documents": len(pdfs),
        "open_gates": [name for name, ok, _ in gates if not ok],
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument("--strict", action="store_true",
                   help="Write the README, then return failure while any release gate is open.")
    args = p.parse_args()
    root = args.root.resolve()
    for attempt in range(3):
        snapshot = Snapshot(root)
        text, status = generate(snapshot)
        if snapshot.stable():
            break
    else:
        raise RuntimeError("Inputs changed during all three README snapshots; rerun after the current write completes.")
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=root,
                                     prefix=".README-", delete=False) as out:
        out.write(text)
        temporary = Path(out.name)
    temporary.replace(root / "README.md")
    print(json.dumps(status, ensure_ascii=False))
    raise SystemExit(1 if args.strict and not status["complete"] else 0)


if __name__ == "__main__":
    main()
