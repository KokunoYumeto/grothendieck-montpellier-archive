#!/usr/bin/env python3
"""Source-preserving editorial parsing for the Nouveau EGA V readers.

This module does not certify a reading. It consumes files certified by the
visual review and records every mechanical change independently of that review.
All paths written into records are edition-relative or input-ZIP-relative.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

EDITORIAL = {
    "hand": 1, "over": 2, "inserted": 1, "margin": 1, "deleted": 1,
    "xout": 1, "uline": 1, "uuline": 1, "unsure": 1, "illegible": 1,
    "scanpage": 1, "mspage": 1, "diagram": 1, "var": 4,
    "tnote": 2, "restoredfrom": 3,
}
CHANGES = {"over", "inserted", "margin", "deleted", "xout"}
TEXT_ARGUMENTS = {"text", "textrm", "textsf", "texttt", "textnormal", "mbox"}
KINDS = {
    "over": "writing over", "inserted": "insertion", "margin": "marginal note placed",
    "deleted": "deletion", "xout": "typewriter strike-out",
}
REASONS = {
    "over": "The handwritten replacement is adopted; the overwritten reading is retained in the apparatus.",
    "inserted": "The insertion is incorporated at the position recorded by the checked transcription.",
    "margin": "The marginal note is retained and placed at its recorded source position.",
    "deleted": "The text struck through by hand is omitted from the running text and retained in the apparatus.",
    "xout": "The text struck on the typewriter is omitted from the running text and retained in the apparatus.",
}
REASONS_FR = {
    "over": "La correction manuscrite est retenue ; la leçon recouverte est conservée dans l'apparat.",
    "inserted": "L'ajout est incorporé à l'emplacement relevé dans la transcription vérifiée.",
    "margin": "La note marginale est conservée et placée à son emplacement dans la source.",
    "deleted": "Le texte biffé à la main quitte le texte courant et reste dans l'apparat.",
    "xout": "Le texte barré à la machine quitte le texte courant et reste dans l'apparat.",
}
KINDS_FR = {
    "writing over": "correction suscrite", "insertion": "insertion",
    "marginal note placed": "note marginale placée", "deletion": "suppression manuscrite",
    "typewriter strike-out": "rature à la machine", "slip corrected": "coquille corrigée",
    "author-directed restoration": "rétablissement prescrit par l'auteur",
}


class ParseError(ValueError):
    pass


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_tsv(path: Path, rows: list[dict], fields: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = fields or (list(rows[0]) if rows else [])
    pending = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="", dir=path.parent,
                prefix=path.name+".", suffix=".tmp", delete=False) as f:
            pending = Path(f.name)
            w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
        os.replace(pending,path)
    finally:
        if pending is not None and pending.exists():
            pending.unlink()


def read_tsv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def escaped(s: str, i: int) -> bool:
    n = 0
    while i > 0 and s[i-1] == "\\":
        n += 1
        i -= 1
    return n % 2 == 1


def command_at(s: str, i: int) -> tuple[str, int]:
    m = re.match(r"\\([A-Za-z@]+|.)", s[i:], re.S)
    if not m:
        return "", i + 1
    return m[1], i + len(m[0])


def group_at(s: str, i: int, opening: str = "{", closing: str = "}") -> tuple[str, int]:
    if i >= len(s) or s[i] != opening:
        raise ParseError(f"Expected {opening!r} at character {i}")
    depth = 1
    j = i + 1
    while j < len(s):
        if s[j] == "%" and not escaped(s, j):
            k = s.find("\n", j)
            j = len(s) if k < 0 else k + 1
            continue
        if s[j] == "\\":
            _, j = command_at(s, j)
            continue
        if s[j] == opening:
            depth += 1
        elif s[j] == closing:
            depth -= 1
            if depth == 0:
                return s[i+1:j], j + 1
        j += 1
    raise ParseError(f"Unclosed {opening!r} at character {i}")


def arguments_at(s: str, i: int, name: str) -> tuple[list[str], str, int, list[int]]:
    """Read only declared editorial commands; whitespace is not semantic here."""
    _, j = command_at(s, i)
    while j < len(s) and s[j].isspace():
        j += 1
    option = ""
    if name == "inserted" and j < len(s) and s[j] == "[":
        option, j = group_at(s, j, "[", "]")
        while j < len(s) and s[j].isspace():
            j += 1
    args, offsets = [], []
    for _ in range(EDITORIAL[name]):
        offsets.append(j + 1)
        arg, j = group_at(s, j)
        args.append(arg)
        while j < len(s) and s[j].isspace() and len(args) < EDITORIAL[name]:
            j += 1
    return args, option, j, offsets


def no_comments(s: str) -> str:
    return re.sub(r"(?<!\\)%[^\n]*(?:\n|$)", "", s)


def cleanup_page(s: str, key: str) -> tuple[str, list[dict]]:
    """Repair parseable syntax only; no spelling, reading, or notation changes."""
    if re.search(r"\\hand\{\\in\}serted(?:\[typed\])?\{", no_comments(s)):
        raise ParseError("An insertion macro name is split by a hand-wrapped membership prefix; review and record the checked-source encoding repair before building.")
    records: list[dict] = []
    lines = s.splitlines(keepends=True)
    for n, line in enumerate(lines, 1):
        m = re.search(r"(?<!\\)%([}]+)([ \t]*)(\r?\n)?$", line)
        if m:
            fixed = line[:m.start()] + m[1] + "%" + m[2] + (m[3] or "")
            records.append(dict(key=key, line=n, before=line.rstrip(), after=fixed.rstrip(),
                action="brace-before-comment", reason="Move closing braces before the line-end comment marker; the braces print no glyph."))
            lines[n-1] = fixed
    s = "".join(lines)
    syntax_file=Path(__file__).resolve().parents[1]/"records/MECHANICAL_SYNTAX_PATCHES.json"
    for patch in (json.loads(syntax_file.read_text()) if syntax_file.exists() else []):
        if patch["key"]!=key:
            continue
        count=s.count(patch["before"])
        if not count:
            continue
        if count!=patch.get("expected_occurrences",1):
            raise ParseError(f"Mechanical syntax patch has an unexpected occurrence count in {key}: {count}")
        start=s.index(patch["before"])
        records.append(dict(key=key,line=s.count("\n",0,start)+1,
            before=patch["before"],after=patch["after"],action=patch["action"],reason=patch["reason"]))
        s=s.replace(patch["before"],patch["after"])
    # Five malformed insertions use square brackets for the required content
    # argument. The only defined optional value is the literal word 'typed'.
    position = 0
    while True:
        m = re.search(r"\\inserted\[", s[position:])
        if not m:
            break
        start = position + m.start()
        arg_start = start + len(r"\inserted")
        option, end = group_at(s, arg_start, "[", "]")
        if option != "typed":
            before = s[start:end]
            after = r"\inserted{" + option + "}"
            records.append(dict(key=key, line=s.count("\n", 0, start)+1,
                before=before, after=after, action="required-argument-braces",
                reason="Restore braces around insertion content; square brackets are reserved for the literal optional value typed."))
            s = s[:start] + after + s[end:]
            position = start + len(after)
        else:
            position = end
    # tikz-cd is stored inside page and editorial macros. Explicit alignment
    # tokens retain the same matrix cells after macro argument tokenization.
    pat = re.compile(r"\\begin\{tikzcd\}(\[[^\]]*\])?([\s\S]*?)\\end\{tikzcd\}")
    def repair_diagram(m):
        options = (m[1] or "")[1:-1]
        original_options = options
        options = options.replace("arrows={blue}","arrows={handwritten}")
        body = m[2]
        align = "ampersand replacement" not in options
        if align:
            options = (options + "," if options else "") + r"ampersand replacement=\&,nodes in empty cells"
            body = re.sub(r"(?<!\\)&", r"\\&", body)
        after = r"\begin{tikzcd}[" + options + "]" + body + r"\end{tikzcd}"
        if after == m[0]:
            return m[0]
        reason = ("Use explicit alignment tokens so the unchanged diagram matrix survives storage inside a macro argument; invisible anchors in empty cells preserve any recorded arrow ending at an otherwise unnamed cell." if align else "")
        if "arrows={blue}" in original_options:
            reason += (" " if reason else "") + "Use the named handwritten arrow style: its diplomatic ink remains blue, while the corrected forms use their prescribed ink color."
        records.append(dict(key=key,line=s.count("\n",0,m.start())+1,before=m[0],after=after,
            action="explicit-diagram-alignment" if align else "diagram-handwriting-style",reason=reason))
        return after
    s = pat.sub(repair_diagram,s)

    def clean(part: str, mode: bool = False, base: int = 0, inherited: bool = False) -> str:
        out: list[str] = []
        i = 0
        while i < len(part):
            ch = part[i]
            if ch == "%" and not escaped(part, i):
                end = part.find("\n", i)
                end = len(part) if end < 0 else end + 1
                out.append(part[i:end]); i = end; continue
            if ch == "$" and not escaped(part, i):
                # Editorial arguments within math must not open a second math list.
                # This removes only explicit dollar delimiters, never math content.
                if inherited:
                    line = s.count("\n", 0, base+i) + 1
                    records.append(dict(key=key, line=line, before="$", after="",
                        action="nested-math-delimiter", reason="Remove a dollar delimiter nested in an editorial argument already in math mode; keep all enclosed tokens."))
                else:
                    out.append(ch); mode = not mode
                i += 1; continue
            if ch == "\\":
                name, cmdend = command_at(part, i)
                if name in ("[", "("):
                    mode = True; out.append(part[i:cmdend]); i = cmdend; continue
                if name in ("]", ")"):
                    mode = False; out.append(part[i:cmdend]); i = cmdend; continue
                if name in EDITORIAL:
                    args, option, end, offsets = arguments_at(part, i, name)
                    if name == "diagram" and re.match(r"\s*\\begin\{array\}", args[0]):
                        # A checked transcription can supply an array as its
                        # entire diagram. Array is a math-only environment;
                        # add only the missing, nonprinting delimiters.
                        before = args[0]
                        args[0] = r"\[" + before + r"\]"
                        records.append(dict(key=key,line=s.count("\n",0,base+i)+1,
                            before=before,after=args[0],action="array-math-delimiters",
                            reason="Enclose a bare array diagram in display-math delimiters; all array entries, arrows, alignment tokens and annotations are unchanged."))
                    cleaned = [clean(a, mode, base+o, mode) for a, o in zip(args, offsets)]
                    out.append("\\" + name + ("["+option+"]" if option else "") + "".join("{"+a+"}" for a in cleaned))
                    i = end; continue
                if name in TEXT_ARGUMENTS:
                    j = cmdend
                    while j < len(part) and part[j].isspace(): j += 1
                    if j < len(part) and part[j] == "{":
                        a, end = group_at(part, j)
                        out.append(part[i:j] + "{" + clean(a, False, base+j+1, False) + "}")
                        i = end; continue
                if name == "begin" and part.startswith("{tikzcd}", cmdend):
                    start = cmdend + len("{tikzcd}")
                    end = part.find(r"\end{tikzcd}", start)
                    if end < 0: raise ParseError("Unclosed tikzcd")
                    # All diagram cells are math; text commands reset that mode.
                    out.append(part[i:start] + clean(part[start:end], True, base+start, True) + r"\end{tikzcd}")
                    i = end + len(r"\end{tikzcd}"); continue
                out.append(part[i:cmdend]); i = cmdend; continue
            if ch == "{":
                a, end = group_at(part, i)
                out.append("{" + clean(a, mode, base+i+1, inherited) + "}")
                i = end; continue
            if ch == "}":
                raise ParseError(f"Unmatched closing brace in {key} at line {s.count(chr(10), 0, base+i)+1}")
            out.append(ch); i += 1
        return "".join(out)
    return clean(s), records


@dataclass
class Variant:
    source_id: str
    key: str
    cote: int
    site: int
    line: int
    ordinal: int
    kind: str
    macro: str
    page_reading: str
    corrected_reading: str
    reason: str
    reason_fr: str
    math_mode: bool
    parent: str = ""

    def as_record(self) -> dict:
        return dict(source_id=self.source_id, key=self.key, cote=self.cote, site=self.site,
            place=f"line {self.line}, variant {self.ordinal}", line=self.line,
            page_reading=self.page_reading, corrected_reading=self.corrected_reading,
            kind=self.kind, reason=self.reason, reason_fr=self.reason_fr,
            math_mode=str(self.math_mode).lower(), parent=self.parent, macro=self.macro)


def annotate_page(s: str, key: str) -> tuple[str, list[Variant]]:
    variants: list[Variant] = []
    cote, site = map(int, key.split("_")[1:])
    serial = 0

    def visit(part: str, mode: bool = False, base: int = 0, parent: str = "") -> str:
        nonlocal serial
        out: list[str] = []
        i = 0
        while i < len(part):
            ch = part[i]
            if ch == "%" and not escaped(part, i):
                end = part.find("\n", i)
                end = len(part) if end < 0 else end + 1
                out.append(part[i:end]); i = end; continue
            if ch == "$" and not escaped(part, i):
                mode = not mode; out.append(ch); i += 1; continue
            if ch == "\\":
                name, cmdend = command_at(part, i)
                if name in ("[", "("):
                    mode = True; out.append(part[i:cmdend]); i = cmdend; continue
                if name in ("]", ")"):
                    mode = False; out.append(part[i:cmdend]); i = cmdend; continue
                if name in EDITORIAL:
                    args, option, end, offsets = arguments_at(part, i, name)
                    sid = parent
                    ordinal = 0
                    if name in CHANGES:
                        serial += 1; ordinal = serial
                        sid = f"{key}-v{serial:04d}"
                    aa = [visit(a, mode, base+o, sid) for a, o in zip(args, offsets)]
                    raw = "\\" + name + ("["+option+"]" if option else "") + "".join("{"+a+"}" for a in aa)
                    if name in CHANGES:
                        corr = aa[-1] if name in ("over", "inserted") else ""
                        if name == "margin": corr = r"\placedmargin{" + aa[0] + "}"
                        v = Variant(sid, key, cote, site, s.count("\n", 0, base+i)+1,
                            ordinal, KINDS[name], name, raw, corr, REASONS[name], REASONS_FR[name], mode, parent)
                        variants.append(v)
                        out.append(r"\var{" + raw + "}{" + corr + "}{" + KINDS[name] + "}{" + sid + "}")
                    else:
                        out.append(raw)
                    i = end; continue
                if name in TEXT_ARGUMENTS:
                    j = cmdend
                    while j < len(part) and part[j].isspace(): j += 1
                    if j < len(part) and part[j] == "{":
                        a, end = group_at(part, j)
                        out.append(part[i:j] + "{" + visit(a, False, base+j+1, parent) + "}")
                        i = end; continue
                if name == "begin" and part.startswith("{tikzcd}", cmdend):
                    start = cmdend + len("{tikzcd}"); end = part.find(r"\end{tikzcd}", start)
                    if end < 0: raise ParseError("Unclosed tikzcd")
                    out.append(part[i:start] + visit(part[start:end], True, base+start, parent) + r"\end{tikzcd}")
                    i = end + len(r"\end{tikzcd}"); continue
                out.append(part[i:cmdend]); i = cmdend; continue
            if ch == "{":
                a, end = group_at(part, i)
                out.append("{" + visit(a, mode, base+i+1, parent) + "}")
                i = end; continue
            out.append(ch); i += 1
        return "".join(out)
    annotated = visit(s)
    return annotated, sorted(variants, key=lambda v: v.ordinal)


def resolve_variants(s: str, side: int = 1) -> str:
    """Resolve annotated choices without changing any other token."""
    out, i = [], 0
    while i < len(s):
        if s[i] == "%" and not escaped(s, i):
            end = s.find("\n", i); end = len(s) if end < 0 else end+1
            out.append(s[i:end]); i = end; continue
        if s[i] == "\\":
            name, end = command_at(s, i)
            if name == "var":
                args, _, end, _ = arguments_at(s, i, name)
                out.append(resolve_variants(args[side], side)); i = end; continue
            out.append(s[i:end]); i = end; continue
        out.append(s[i]); i += 1
    return "".join(out)


def extract_variants(s: str) -> dict[str,dict]:
    """Read all variant definitions, including nested and repeated branches."""
    result={};i=0
    while i<len(s):
        if s[i]=="%" and not escaped(s,i):
            j=s.find("\n",i);i=len(s) if j<0 else j+1;continue
        if s[i]=="\\":
            name,end=command_at(s,i)
            if name=="var":
                args,_,_,_=arguments_at(s,i,name)
                row=dict(page_reading=args[0],corrected_reading=args[1],kind=args[2],source_id=args[3])
                if args[3] in result and result[args[3]]!=row:
                    raise ParseError("Inconsistent repeated variant "+args[3])
                result[args[3]]=row
            i=end
        else:i+=1
    return result


def without_translator_notes(s: str) -> str:
    """Exclude explanatory notes from comparison of the translated source."""
    out=[];i=0
    while i<len(s):
        if s[i]=="%" and not escaped(s,i):
            j=s.find("\n",i);j=len(s) if j<0 else j+1
            out.append(s[i:j]);i=j;continue
        if s[i]=="\\":
            name,end=command_at(s,i)
            if name=="tnote":
                _,_,i,_=arguments_at(s,i,name);continue
            out.append(s[i:end]);i=end;continue
        out.append(s[i]);i+=1
    return "".join(out)


def apply_variant_overrides(annotated: str, variants: list[Variant], overrides: list[dict]) -> str:
    """Apply explicit reviewed corrected-branch decisions; never alter page text."""
    byid={v.source_id:v for v in variants}
    for row in overrides:
        sid=row["source_id"]
        if sid not in byid:continue
        v=byid[sid]
        if v.corrected_reading!=row["expected_corrected"]:
            raise ParseError(f"Stale corrected-branch override {sid}")
        old=r"\var{"+v.page_reading+"}{"+v.corrected_reading+"}{"+v.kind+"}{"+v.source_id+"}"
        new=r"\var{"+v.page_reading+"}{"+row["corrected_reading"]+"}{"+v.kind+"}{"+v.source_id+"}"
        if old not in annotated:raise ParseError(f"Override target missing: {sid}")
        annotated=annotated.replace(old,new)
        for other in variants:
            other.page_reading=other.page_reading.replace(old,new)
            other.corrected_reading=other.corrected_reading.replace(old,new)
        v.corrected_reading=row["corrected_reading"]
        v.reason += " " + row["reason"]
        v.reason_fr += " " + row["reason_fr"]
    return annotated


def math_fragments(s: str) -> list[str]:
    """Extract formula token strings, including delimiters, without expansion."""
    s = no_comments(s)
    out, i = [], 0
    while i < len(s):
        if s[i] == "$" and not escaped(s, i):
            close = "$$" if s.startswith("$$", i) else "$"
            j = i+len(close)
            while j < len(s):
                if s.startswith(close, j) and not escaped(s, j):
                    j += len(close); break
                j += 1
            out.append(s[i:j]); i = j; continue
        if s.startswith(r"\[", i) or s.startswith(r"\(", i):
            enddelim = r"\]" if s[i+1] == "[" else r"\)"
            j = s.find(enddelim, i+2)
            if j < 0: raise ParseError("Unterminated math")
            j += 2; out.append(s[i:j]); i = j; continue
        if s.startswith(r"\begin{tikzcd}", i):
            j = s.find(r"\end{tikzcd}", i)
            if j < 0: raise ParseError("Unterminated diagram")
            j += len(r"\end{tikzcd}"); out.append(s[i:j]); i = j; continue
        if s[i] == "\\":
            _, i = command_at(s, i)
        else:
            i += 1
    return out


def mark_counts(s: str) -> dict[str, int]:
    s = no_comments(s)
    return {n: len(re.findall(r"\\"+n+r"\b", s)) for n in EDITORIAL}


def bare_numerals(s: str) -> list[str]:
    """Screen literal numerals outside explicit formulas without rewriting them.

    This supplements exact formula comparison: the transcription also contains
    plain-text dimensions, bounds and numbered references. It does not infer
    mathematical structure from surrounding prose.
    """
    s=no_comments(s)
    for fragment in math_fragments(s):
        s=s.replace(fragment," ",1)
    return re.findall(r"(?<![A-Za-z0-9])\d+(?:\.\d+)*(?![A-Za-z0-9])",s)


def visible_link_marks(s: str, mode: int) -> dict[str, int]:
    """Count the links of the branch that will actually be printed.

    Each unsure/illegible/scan mark is one logical link. A multiline link can
    become several PDF annotations. Restoration provenance is separately named.
    """
    result = dict(scan=0, unsure=0, illegible=0, provenance=0)
    def visit(part: str) -> None:
        i=0
        while i<len(part):
            if part[i]=="%" and not escaped(part,i):
                j=part.find("\n",i);i=len(part) if j<0 else j+1;continue
            if part[i]!="\\":
                i+=1;continue
            name,end=command_at(part,i)
            if name in EDITORIAL:
                args,_,end,_=arguments_at(part,i,name)
                if name=="var":
                    visit(args[0 if mode==0 else 1])
                elif name=="tnote":
                    if mode==1:visit(args[1])
                elif name=="restoredfrom":
                    result["provenance"]+=1;visit(args[2])
                else:
                    if name in ("unsure","illegible"):result[name]+=1
                    if name=="scanpage":result["scan"]+=1
                    for arg in args:visit(arg)
            i=end
    visit(s)
    return result


def tex_escape(s: str) -> str:
    trans = {"\\": r"\textbackslash{}", "{": r"\{", "}": r"\}",
        "$": r"\$", "&": r"\&", "#": r"\#", "_": r"\_", "%": r"\%",
        "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(trans.get(c, c) for c in s)
