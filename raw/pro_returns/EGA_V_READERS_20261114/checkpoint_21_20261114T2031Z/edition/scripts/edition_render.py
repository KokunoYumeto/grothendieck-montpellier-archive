#!/usr/bin/env python3
"""Standalone TeX rendering of the common annotated page masters."""
from __future__ import annotations
import json
import re
from pathlib import Path
from edition_core import tex_escape, KINDS_FR, resolve_variants, mark_counts, write_tsv, read_tsv, visible_link_marks, extract_variants, sha256

RIGHTS_EN = "The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights, in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it down."
RIGHTS_FR = "Les droits sur l'œuvre originale appartiennent à son auteur, à ses représentants ou à ses ayants droit. Dans la mesure où nous détenons des droits sur la transcription, la traduction, les corrections et la composition produites par l'IA, nous les consacrons au domaine public sous CC0 1.0. Cette édition est publiée à des fins éducatives et non lucratives, et nous ne revendiquons aucun droit que nous ne détenons pas. Si vous détenez des droits sur cette œuvre et vous opposez à sa publication ici, veuillez ouvrir une issue GitHub et nous la retirerons."
CREDIT = "AI-transcribed by Claude Opus 5.5 (Anthropic, effort high, Message Batches API); checked against the scans, and this edition built, by GPT-6 Astra (OpenAI, ChatGPT Pro mode); prompts and records by Claude (Anthropic)"

PREAMBLE = r'''\documentclass[10pt,a4paper]{article}
% A single-file reader generated from the common annotated page master.
% Compile with LuaLaTeX twice. Source IDs and archive links are retained.
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\setsansfont{Latin Modern Sans}
\setmonofont{Latin Modern Mono}
\usepackage[english]{babel}
\babelprovide[import]{french}
\usepackage[a4paper,left=21mm,right=43mm,top=22mm,bottom=22mm,
  marginparwidth=29mm,marginparsep=5mm,headheight=14pt,headsep=5mm]{geometry}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{newunicodechar}
\newunicodechar{∈}{\ensuremath{\in}}
\newunicodechar{⊗}{\ensuremath{\otimes}}
\newunicodechar{ø}{\ifmmode\text{\normalfont\itshape\char"00F8}\else\char"00F8\fi}
\newunicodechar{Ø}{\ifmmode\text{\normalfont\itshape\char"00D8}\else\char"00D8\fi}
\usepackage{xcolor}
\usepackage{tikz-cd}
\usetikzlibrary{shapes.geometric}
\usepackage{lua-ul}
\usepackage{marginnote}
\usepackage{fancyhdr}
\usepackage{pdflscape}
\usepackage{microtype}
\usepackage[unicode,breaklinks,colorlinks,linkcolor=blue!45!black,
  urlcolor=blue!45!black,pdfencoding=auto]{hyperref}
% Some transcribed symbols deliberately use the slashed-o letter. Select its
% actual text glyph even inside math; do not replace it by another math symbol.
% Install after package encoding declarations have initialized the text macros.
\AtBeginDocument{\RenewDocumentCommand{\o}{}{\ifmmode\text{\normalfont\itshape\char"00F8}\else\char"00F8\fi}}
\AtBeginDocument{\RenewDocumentCommand{\O}{}{\ifmmode\text{\normalfont\itshape\char"00D8}\else\char"00D8\fi}}
% Explicit maps also support minimal TeX Live installations.
\pdfextension mapfile{+cm.map}
\pdfextension mapfile{+symbols.map}
\pdfextension mapfile{+euler.map}
\pdfextension mapfile{+latxfont.map}
\pdfextension mapfile{+cmextra.map}
\pdfextension mapfile{+lm.map}
\setlength{\parindent}{0pt}
\setlength{\parskip}{4pt plus 1pt minus 1pt}
\setlength{\emergencystretch}{1.5em}
\setlength{\marginparpush}{3pt}
\raggedbottom
\definecolor{handblue}{RGB}{25,65,125}
\definecolor{deletedred}{RGB}{132,38,34}
\definecolor{strikegray}{RGB}{90,90,90}
\newcount\EditionMode
\EditionMode=@MODE@ % 0 diplomatic; 1 corrected apparatus; 2 reading
\tikzset{handwritten/.code={\ifnum\EditionMode=0
  \pgfkeysalso{/tikz/draw=handblue}\else\pgfkeysalso{/tikz/draw=black}\fi}}
\tikzcdset{handwritten/.style={/tikz/handwritten}}
\newif\ifInApparatus
\newif\ifEditionFrench
@FRENCH@
\newcommand{\EditionForm}{@FORM@}
\newcommand{\CurrentScanURL}{}
\newcommand{\CurrentScanLabel}{}
\newcommand{\CurrentPageKey}{}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\sffamily Nouveau EGA V}
\fancyhead[R]{\small\sffamily\CurrentScanLabel}
\fancyfoot[C]{\small\thepage}
\renewcommand{\headrulewidth}{0.2pt}
\newcommand{\ScanLink}[1]{\href{\CurrentScanURL}{#1}}
\newcount\SourceMarkSerial
\newcommand{\SourceHref}[2]{%
  \global\advance\SourceMarkSerial by 1
  \hypertarget{egamark:#1:\the\SourceMarkSerial}{\ScanLink{#2}}}
\newcommand{\scanpage}[1]{%
  \ifnum\EditionMode=2
    \marginnote{\scriptsize\sffamily\SourceHref{scan}{scan #1}}%
  \else
    \par\medskip\noindent{\small\sffamily\SourceHref{scan}{[scan #1]}}\par\smallskip
  \fi}
\newcommand{\mspage}[1]{%
  \ifnum\EditionMode=2
    \marginnote{\scriptsize\sffamily p.\,#1}%
  \else
    {\small\sffamily[p.\,#1]}%
  \fi}
\NewDocumentCommand{\hand}{+m}{\ifnum\EditionMode=0{\color{handblue}#1}\else#1\fi}
\let\over\relax
\NewDocumentCommand{\over}{+m +m}{%
  {\color{strikegray}#1}\ensuremath{{}^{\nearrow}}{\color{handblue}#2}}
\NewDocumentCommand{\inserted}{O{} +m}{%
  {\color{handblue}\ensuremath{\langle}#2\ensuremath{\rangle}}}
\NewDocumentCommand{\deleted}{+m}{%
  {\color{deletedred}\ifmmode\text{[del.:}\,#1\,\text{]}\else[\textsf{del.:} #1]\fi}}
\NewDocumentCommand{\xout}{+m}{%
  {\color{strikegray}\ifmmode\text{[x:}\,#1\,\text{]}\else[\textsf{x:} #1]\fi}}
\NewDocumentCommand{\uline}{+m}{\ifmmode\underline{#1}\else\underLine{#1}\fi}
\NewDocumentCommand{\uuline}{+m}{\ifmmode\underline{\underline{#1}}\else\underLine[top=-1.05ex,bottom=-1.15ex]{\underLine{#1}}\fi}
\NewDocumentCommand{\unsure}{+m}{\SourceHref{unsure}{[#1?]}}
\newcommand{\illegible}[1]{\SourceHref{illegible}{\ifmmode\text{[illeg. #1]}\else[\textsf{illeg.\ #1}]\fi}}
\newsavebox{\MarginMeasure}
\NewDocumentCommand{\MarginContent}{+m}{%
  \ifInApparatus
    {\small\textsf{\ifEditionFrench marg.\else marg.\fi:}\ #1}%
  \else
    \ifmmode
      \text{\scriptsize[\textsf{marg.:} #1]}%
    \else
      \sbox{\MarginMeasure}{\parbox[t]{\marginparwidth}{\footnotesize\raggedright #1}}%
      \ifdim\dimexpr\ht\MarginMeasure+\dp\MarginMeasure\relax<36pt
        \marginnote{\usebox{\MarginMeasure}}%
      \else
        \par\smallskip\noindent\rule{16mm}{0.3pt}\par\nobreak
        \begingroup\small\noindent\textsf{\ifEditionFrench Note marginale\else Marginal note\fi.}\ #1\par\endgroup
        \nobreak\smallskip\noindent\rule{16mm}{0.3pt}\par\smallskip
      \fi
    \fi
  \fi}
\NewDocumentCommand{\margin}{+m}{{\color{handblue}\MarginContent{#1}}}
\NewDocumentCommand{\placedmargin}{+m}{\MarginContent{#1}}
\NewDocumentCommand{\diagram}{+m}{\par\smallskip{\centering #1\par}\smallskip}
\newenvironment{diagramblock}{\par\begin{center}}{\end{center}\par}
\newcommand{\VariantNumber}[1]{\csname variantnumber@#1\endcsname}
\newcommand{\VariantMark}[1]{%
  \ifInApparatus\else
    \ifmmode\text{\textsuperscript{\tiny\hyperlink{app:#1}{[\VariantNumber{#1}]}}}%
    \else\textsuperscript{\tiny\hyperlink{app:#1}{[\VariantNumber{#1}]}}\fi
  \fi}
\NewDocumentCommand{\var}{+m +m m m}{%
  \ifnum\EditionMode=0#1\else#2\ifnum\EditionMode=1\VariantMark{#4}\fi\fi}
\NewDocumentCommand{\tnote}{m +m}{%
  \ifnum\EditionMode=1\footnote{\textsf{Translator's note (#1).} #2}\fi}
\NewDocumentCommand{\restoredfrom}{m m +m}{%
  \begingroup\def\CurrentScanURL{#2}%
  \ifInApparatus
    {\small\sffamily\SourceHref{provenance}{[scan #1]}}\par
  \else
    \marginnote{\scriptsize\sffamily\SourceHref{provenance}{scan #1}}%
  \fi
  #3\par\endgroup}
\NewDocumentCommand{\AppEntry}{m m m +m +m +m}{%
  \par\smallskip\noindent\hypertarget{app:#1}{\textbf{[#2]}}\quad
  \textit{#3}. #4\par
  \begingroup\InApparatustrue\small
  \ifEditionFrench\textsf{Page :}\else\textsf{Page:}\fi\ 
  {\EditionMode=0 #5}\par
  \ifEditionFrench\textsf{Texte retenu :}\else\textsf{Retained text:}\fi\ 
  {\EditionMode=2 #6}\par\endgroup}
\newcommand{\AbsentReading}{\ifEditionFrench[omis]\else[omitted]\fi}
\newcommand{\WordSpaceReading}{\ifEditionFrench[espace entre les mots]\else[word space]\fi}
\NewDocumentCommand{\RegisterPage}{m +m +m}{%
  \expandafter\long\expandafter\gdef\csname PageBody@#1\endcsname{#2}%
  \expandafter\long\expandafter\gdef\csname PageApparatus@#1\endcsname{#3}}
\newcommand{\PrintPage}[3]{%
  \clearpage
  \gdef\CurrentPageKey{#1}\gdef\CurrentScanLabel{#2}\gdef\CurrentScanURL{#3}%
  \typeout{EGA-SOURCE-BEGIN #1 PDF-PAGE \thepage}%
  \pdfbookmark[1]{Scan #2}{source:#1}%
  \csname PageBody@#1\endcsname\par
  \ifnum\EditionMode=1
    \csname PageApparatus@#1\endcsname
  \fi
  \typeout{EGA-SOURCE-END #1 PDF-PAGE \thepage}}
'''


def frontmatter(family: str, *, partial: bool, development: bool) -> str:
    french=family=="fr"
    title="Nouveau EGA V" if family!="blass" else "EGA V based on notes of Alexandre Grothendieck"
    cote="25" if family!="blass" else "24"
    subtitle="Prenotes françaises" if french else ("English translation of the corrected French prenotes" if family=="en" else "Piotr Blass's translation typescript (1987)")
    credit=CREDIT if not development else "AI-transcribed by Claude Opus 5.5 (Anthropic, effort high, Message Batches API). Unchecked development build prepared by GPT-6 Astra (OpenAI, ChatGPT Pro mode). This development build does not certify any page reading."
    label = "UNCHECKED DEVELOPMENT BUILD" if development else ("INCOMPLETE CHECKPOINT — REVIEW IN PROGRESS" if partial else "")
    front = r"\begin{document}"+"\n"
    front += (r"\selectlanguage{french}" if french else r"\selectlanguage{english}")+"\n"
    front += r"\hypersetup{pageanchor=false}\begin{titlepage}\thispagestyle{empty}\vspace*{20mm}"+"\n"
    front += r"{\Large Alexandre Grothendieck\par}\vspace{12mm}"+"\n"
    front += r"{\Huge\bfseries "+tex_escape(title)+r"\par}\vspace{8mm}"+"\n"
    front += r"{\Large "+tex_escape(subtitle)+r"\par}\vspace{7mm}"+"\n"
    front += r"{\large\EditionForm\par}\vspace{12mm}"+"\n"
    if label:front += r"{\large\bfseries\color{deletedred}"+tex_escape(label)+r"\par}\vspace{10mm}"+"\n"
    front += "Université de Montpellier, fonds Grothendieck\\\\ Cote "+cote+"\\\\\n14 November 2026\n"
    front += r"\vfill\end{titlepage}\clearpage\hypersetup{pageanchor=true}"+"\n"
    front += r"\section*{"+("Établissement du texte et droits" if french else "Text, provenance, and rights")+"}\n"
    front += tex_escape(credit)+".\n\n"
    if family=="en":front += "AI-translated by GPT-6 Astra (OpenAI, ChatGPT Pro mode).\n\n"
    if family=="blass":front += "The translation in cote 24 is Piotr Blass's (1987); the rights in it belong to its translator or his heirs.\n\n"
    front += ("Cote 25 is described in the archive as dated ``[à partir de 1967-1987]''. " if family!="blass" else "Cote 24 is the 1987 translation typescript, including its translator's queries and the French manuscript note at site 75. ")
    front += "The source of each reading is the attached Montpellier scan. The named published texts---the Grothendieck Circle scan EGA5.pdf, the P. and J. Blass translations (2004), J. C. Reinhold's web re-edition, and the Centre for Grothendieckian Studies item L49d---are not reproduced and have not been consulted for any reading.\n\n"
    front += tex_escape(RIGHTS_EN)+"\n\n"
    if french:front += tex_escape(RIGHTS_FR)+"\n\n"
    front += r"\clearpage\section*{"+("Mode de lecture" if french else "How to read this edition")+"}\n"
    if french:
        front += "Le lecteur diplomatique suit l'ordre des pages de la cote 25. Le texte corrigé et le texte de lecture présentent IV 16, IV 17.15--17.16, IV 20, puis IV 21 ; la lettre à Dieudonné constitue l'appendice. Les feuillets intercalaires sont conservés auprès des ensembles auxquels ils sont joints.\n\n"
        front += "La forme diplomatique distingue le texte dactylographié, l'écriture manuscrite en bleu, les suppressions manuscrites en rouge et les ratures de machine en gris. Les ajouts sont encadrés de chevrons ; une flèche signale les corrections suscrites. Le texte corrigé incorpore les ajouts et les corrections et renvoie chaque changement à l'apparat. Le texte de lecture laisse de côté cet apparat et les signes éditoriaux qui en assurent le repérage. Les notes marginales et les marques de doute sont conservées.\n\n"
        front += "Les graphies, les abréviations et les notations de la source demeurent celles du manuscrit : notamment préschéma, Module, systême lorsqu'il est ainsi écrit, loc, rel, resp., sss, cqfd, les lettres soulignées et les différentes formes des lettres et des flèches. Aucune harmonisation de vocabulaire ou de notation n'est appliquée au français. Une éventuelle coquille corrigée possède sa leçon de page et son motif dans l'apparat.\n\n"
        front += "Chaque indication de scan et chaque marque de doute ou d'illisibilité est un lien vers la page correspondante du visionneur de Montpellier. Les numéros de la source sont distingués de la pagination du présent volume.\n"
    else:
        front += "The diplomatic form follows archive order. The corrected and reading forms for cote 25 order the material as IV 16, IV 17.15--17.16, IV 20, and IV 21, followed by the letter to Dieudonné. Interleaved leaves are retained with the relevant groups. Cote 24 keeps its archive order; its stray curriculum-vitae leaf at site 76 appears in the diplomatic form only.\n\n"
        front += "Handwriting is blue in the diplomatic form, manuscript deletions red, and typewriter strike-outs gray. Angle brackets mark insertions, and a small rising arrow marks writing over typed text. The corrected form incorporates the additions and replacements and records each difference in the apparatus. The reading form omits the apparatus and its editorial reference marks. Source marginal notes, unresolved readings, and translator queries remain.\n\n"
        if family=="blass":
            front += "Blass's wording, abbreviations, spelling, and mathematical notation are retained. The French handwritten leaf at site 75 remains in its original language. English terminology rules apply to editorial prose and do not alter Blass's English.\n\n"
        else:
            front += "The new English translation follows the supplied unified glossary. The mathematical formulas retain the token strings of the mechanically cleaned corrected French text. Translation explanations are confined to translator's notes. The English annotated master preserves the French variant identifiers.\n\n"
        front += "Every scan mark and every uncertainty or illegibility mark links to the corresponding page in the Montpellier viewer. The original page numbers remain distinct from this volume's pagination.\n"
    front += r"\clearpage"+"\n"
    return front


def apparatus(variants: list[dict], french: bool) -> str:
    if not variants:return ""
    result = r"\par\medskip\noindent\rule{\linewidth}{0.3pt}\par"+"\n"
    result += r"{\small\sffamily\bfseries "+("Apparat de la page" if french else "Apparatus for this source page")+r"}\par"+"\n"
    for v in variants:
        raw=v["page_reading"]
        corrected=v["corrected_reading"] or r"\AbsentReading"
        if v["corrected_reading"].isspace():corrected=r"\WordSpaceReading"
        if v["math_mode"] == "true":
            raw="$"+raw+"$"
            if v["corrected_reading"]:corrected="$"+corrected+"$"
        kind=KINDS_FR.get(v["kind"],v["kind"]) if french else v["kind"]
        reason=v.get("reason_fr",v["reason"]) if french else v["reason"]
        result += r"\AppEntry{"+v["source_id"]+"}{"+v["source_id"].rsplit("v",1)[-1].lstrip("0")+"}{"+tex_escape(kind)+"}{"+tex_escape(reason)+"}{"+raw+"}{"+corrected+"}\n"
    return result


def order_keys(keys: list[str], family: str, mode: int) -> list[str]:
    if family=="blass":
        return [k for k in keys if mode==0 or not k.endswith("_076")]
    if mode==0:return keys
    sites=list(range(139,158))+list(range(158,185))+list(range(1,97))+list(range(97,134))+list(range(136,139))+[134,135]
    available=set(keys)
    return [f"ega25_25_{i:03d}" for i in sites if f"ega25_25_{i:03d}" in available]


def build_family(target: Path, family: str, pagekeys: list[str], pages: dict,
                 *, partial: bool=False, development: bool=False) -> list[Path]:
    french=family=="fr"
    data=[]
    pagelinks={}
    patchfile=Path(__file__).resolve().parents[1]/"records/TYPESETTING_PATCHES.json"
    patches=json.loads(patchfile.read_text()) if patchfile.exists() else []
    applied=[]
    input_hashes={}
    if not development:
        for rel in ("scripts/edition_render.py","scripts/edition_core.py","scripts/build_readers.py",
                "records/TYPESETTING_PATCHES.json","records/MECHANICAL_SYNTAX_PATCHES.json"):
            path=target/rel
            if path.is_file():input_hashes[rel]=sha256(path.read_text())
    declarations=[]
    notefile=Path(__file__).resolve().parents[1]/"records/EN_VARIANT_NOTES.tsv"
    translationnotes={r["source_id"]:r["note"] for r in read_tsv(notefile)} if notefile.is_file() else {}
    for key in pagekeys:
        body=(target/"master_pages"/family/(key+".tex")).read_text()
        for rel in (f"master_pages/{family}/{key}.tex",f"checked_pages/{key}.tex",f"variant_records/{key}.json"):
            path=target/rel
            if path.is_file():input_hashes[rel]=sha256(path.read_text())
        if family=="en":
            rel=f"master_pages/fr/{key}.tex"
            input_hashes[rel]=sha256((target/rel).read_text())
        variants=json.loads((target/"variant_records"/(key+".json")).read_text())
        if family=="en":
            # Translated apparatus side readings are contained in the English
            # master. Pull them by ID while retaining the French reasons/kinds.
            translated=extract_variants(body)
            for v in variants:
                if v["source_id"] in translated:
                    t=translated[v["source_id"]]
                    v["page_reading"],v["corrected_reading"]=t["page_reading"],t["corrected_reading"]
                    if v["source_id"] in translationnotes:
                        v["reason"]+=" "+translationnotes[v["source_id"]]
            variants=[v for v in variants if v["source_id"] in translated]
        for v in variants:
            ordinal=v["source_id"].rsplit("v",1)[-1].lstrip("0")
            declarations.append(r"\expandafter\def\csname variantnumber@"+v["source_id"]+r"\endcsname{"+ordinal+"}")
        pagelinks[key]={}
        for mode in (0,1,2):
            counts=visible_link_marks(body,mode)
            if mode==1:
                for v in variants:
                    for branch,branchmode in (("page_reading",0),("corrected_reading",2)):
                        for kind,n in visible_link_marks(v[branch],branchmode).items():
                            counts[kind]+=n
            pagelinks[key][mode]=counts
        page_data=r"\RegisterPage{"+key+"}{%\n"+body+"\n}{%\n"+apparatus(variants,french)+"}\n"
        for patch in patches:
            if patch["key"]!=key:continue
            count=page_data.count(patch["before"])
            if count:
                page_data=page_data.replace(patch["before"],patch["after"])
                applied.append(dict(page_key=key,source_line=patch["source_line"],issue=patch["issue"],repair=patch["repair"],before=patch["before"],after=patch["after"],occurrences=count))
        data.append(page_data)
    common_defs="\n".join(declarations)+"\n"+"\n".join(data)
    forms = {
        "fr":[("EGA_V_FR_master_annotated",1,"Maître annoté — texte corrigé avec apparat"),
              ("EGA_V_FR_diplomatique",0,"Transcription diplomatique"),
              ("EGA_V_FR_corrige_apparat",1,"Texte corrigé avec apparat"),
              ("EGA_V_FR_texte_de_lecture",2,"Texte de lecture")],
        "blass":[("EGA_V24_EN_master_annotated",1,"Annotated master — corrected text with apparatus"),
                 ("EGA_V24_EN_diplomatic",0,"Diplomatic transcription"),
                 ("EGA_V24_EN_corrected_apparatus",1,"Corrected text with apparatus"),
                 ("EGA_V24_EN_reading",2,"Reading text")],
        "en":[("EGA_V_EN_master_annotated",1,"Annotated English master"),
              ("EGA_V_EN_corrected_translator_notes",1,"Corrected translation with translator's notes"),
              ("EGA_V_EN_reading",2,"English reading text")],
    }[family]
    outdir=target/"readers";outdir.mkdir(parents=True,exist_ok=True)
    results=[]; inventory=[]
    for basename,mode,form in forms:
        pre=PREAMBLE.replace("@MODE@",str(mode)).replace("@FRENCH@",r"\EditionFrenchtrue" if french else r"\EditionFrenchfalse").replace("@FORM@",form)
        chosen=order_keys(pagekeys,family,mode)
        body=pre+"\n"+common_defs+frontmatter(family,partial=partial,development=development)
        for key in chosen:
            r=pages[key]
            if family=="blass" and key.endswith("_076"):
                body += r"\clearpage\section*{Stray sheet: final page of a curriculum vitae}"+"\n"
            body += r"\PrintPage{"+key+"}{"+r["cote"]+"/"+str(int(r["site"]))+"}{"+r["viewer"].replace("#",r"\#")+"}\n"
        body += r"\end{document}"+"\n"
        p=outdir/(basename+".tex");p.write_text(body);results.append(p)
        counts={kind:sum(pagelinks[k][mode][kind] for k in chosen) for kind in ("scan","unsure","illegible","provenance")}
        expected=dict(reader=basename,source_pages=len(chosen),logical_link_marks=counts,
            reader_sha256=sha256(body),source_files_sha256=input_hashes,
            typesetting_patch_source_keys=sorted({p["key"] for p in patches if p["key"] in chosen}),
            source_page_marks={k:pagelinks[k][mode] for k in chosen})
        expectation=target/"records"/("LINK_EXPECTATIONS_"+basename+".json")
        expectation.parent.mkdir(parents=True,exist_ok=True)
        expectation.write_text(json.dumps(expected,ensure_ascii=False,indent=2)+"\n")
        inventory.append(dict(reader=basename,family=family,mode=mode,source_pages=len(chosen),
                              source_keys=" ".join(chosen),status="UNCHECKED DEVELOPMENT" if development else "INCOMPLETE CHECKPOINT" if partial else "source-complete; compilation pending"))
    write_tsv(target/"records"/("READER_INVENTORY_"+family+".tsv"),inventory)
    fixrows=[dict(reader=name,**patch) for name,_,_ in forms for patch in applied]
    write_tsv(target/"records"/("TYPESETTING_FIXES_"+family+".tsv"),fixrows,["reader","page_key","source_line","issue","repair","before","after","occurrences"])
    return results
