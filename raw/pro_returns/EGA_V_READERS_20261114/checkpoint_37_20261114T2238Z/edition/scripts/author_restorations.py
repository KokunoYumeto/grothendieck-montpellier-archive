#!/usr/bin/env python3
"""Explicit author-directed restoration attested by cote 25 sites 21 and 22.

This transformation is deliberately narrow. It records the cancelled 4.5
passage as restored at the author's stated destination, 5.1. Proposition 4.6
remains cancelled. The checked source pages are never changed.
"""
from pathlib import Path
import json
from edition_core import Variant,arguments_at,write_tsv,extract_variants


def token(v):
    return r"\var{"+v["page_reading"]+"}{"+v["corrected_reading"]+"}{"+v["kind"]+"}{"+v["source_id"]+"}"


def translated_passage(master: str, donor_variants: list[dict]) -> str:
    """Copy the same reviewed restoration boundaries in a translated master."""
    donor="ega25_25_021"
    translated=extract_variants(master)
    outer=translated[donor+"-v0005"]
    payload=arguments_at(outer["page_reading"],0,"deleted")[0][0]
    passage=payload.split(token(translated[donor+"-v0022"]),1)[0]
    passage=passage.replace(token(translated[donor+"-v0006"]),"",1).strip()
    for v in donor_variants:
        sid=v["source_id"]
        if v["parent"]==outer["source_id"] and v["kind"]=="deletion" and sid in translated and token(translated[sid]) in passage:
            inner=arguments_at(translated[sid]["page_reading"],0,"deleted")[0][0]
            passage=passage.replace(token(translated[sid]),inner)
    return passage


DONOR_REASON = " The cancellation of paragraph 4.5 is revoked by the author's instruction on site 22 and the paragraph is restored under 5.1; Proposition 4.6 remains cancelled."
DONOR_REASON_FR = " La suppression du paragraphe 4.5 est révoquée par l'instruction de l'auteur au site 22, et ce paragraphe est rétabli sous 5.1 ; la proposition 4.6 reste biffée."


def donor_restoration_metadata(records: list[dict]) -> list[dict]:
    """Apply the donor apparatus explanation once, without writing any file."""
    vv=[dict(v) for v in records]
    donor="ega25_25_021";byid={v["source_id"]:v for v in vv}
    outer=byid[donor+"-v0005"];number=byid[donor+"-v0006"];boundary=byid[donor+"-v0022"]
    payload=arguments_at(outer["page_reading"],0,"deleted")[0][0]
    passage=payload.split(token(boundary),1)[0].replace(token(number),"",1).strip()
    affected={outer["source_id"],number["source_id"]}
    affected.update(v["source_id"] for v in vv
        if v["parent"]==outer["source_id"] and v["kind"]=="deletion" and token(v) in passage)
    for v in vv:
        v["reason"]=v["reason"].replace(DONOR_REASON,"")
        v["reason_fr"]=v["reason_fr"].replace(DONOR_REASON_FR,"")
        if v["source_id"] in affected:
            v["reason"]+=DONOR_REASON
            v["reason_fr"]+=DONOR_REASON_FR
    return vv


def restore_45_at_51(annotated: str, variants: list[Variant], target: Path, pages: dict,
                    *, write_records: bool=True) -> tuple[str,list[Variant]]:
    donor="ega25_25_021";recipient="ega25_25_022"
    metadata=target/"variant_records"/(donor+".json")
    if not metadata.is_file():
        raise ValueError("Author-directed restoration requires checked site 21 before site 22")
    vv=json.loads(metadata.read_text());byid={v["source_id"]:v for v in vv}
    outer=byid[donor+"-v0005"]
    if outer["macro"]!="deleted" or outer["parent"]:
        raise ValueError("Restoration donor cancellation no longer matches the reviewed source structure")
    payload=arguments_at(outer["page_reading"],0,"deleted")[0][0]
    number=byid[donor+"-v0006"]
    boundary=byid[donor+"-v0022"]
    if r"\hand{4.5.}" not in number["page_reading"] or r"\uline{Proposition} 4.6." not in boundary["page_reading"]:
        raise ValueError("Restoration boundaries require renewed review")
    if payload.count(token(boundary))!=1 or payload.count(token(number))!=1:
        raise ValueError("Restoration boundary is not unique")
    passage=payload.split(token(boundary),1)[0]
    passage=passage.replace(token(number),"",1).strip()
    revived=[]
    for v in vv:
        if v["parent"]==outer["source_id"] and v["kind"]=="deletion" and token(v) in passage:
            inner=arguments_at(v["page_reading"],0,"deleted")[0][0]
            passage=passage.replace(token(v),inner)
            revived.append(v["source_id"])
    if "Proposition} 4.6." in passage:
        raise ValueError("Restoration accidentally includes Proposition 4.6")
    prefix="\n5.1.\n"
    if annotated.count(prefix)!=1:
        raise ValueError("Restoration recipient heading is not unique")
    start=annotated.index(prefix)+len(prefix)
    end=annotated.index("\n\n5.2.",start)
    printed=annotated[start:end]
    if "texte barr\\'e par erreur" not in printed:
        raise ValueError("Recipient no longer contains the attested restoration instruction")
    ordinal=max((v.ordinal for v in variants),default=0)+1
    sid=f"{recipient}-v{ordinal:04d}"
    donorurl=pages[donor]["viewer"].replace("#",r"\#")
    corrected=r"\restoredfrom{25/21}{"+donorurl+"}{%\n"+passage+"\n}"
    reason=("Author-directed restoration and relocation of the cancelled paragraph 4.5 from cote 25/site 21 to the existing heading 5.1 on site 22. "
        "Site 21 says Passer au No 5.1; site 22 describes the preceding cancellation as texte barré par erreur. "
        "The source number 4.5 is retained in the site-21 apparatus; the destination heading 5.1 supplies the running-text number. "
        "The restored passage stops before Proposition 4.6. Earlier internal typewriter corrections and the insertion are applied once; their original site-21 variant IDs and apparatus entries are retained. "
        "Transferred doubt marks link to site 21. The exact abbreviated incipit and reference printed on site 22 remain the page-reading branch of this entry.")
    reason_fr=("Rétablissement et déplacement prescrits par l'auteur du paragraphe 4.5 biffé, de la cote 25/site 21 sous la rubrique 5.1 du site 22. "
        "Le site 21 porte Passer au No 5.1 ; le site 22 précise texte barré par erreur. "
        "Le numéro 4.5 de la source demeure dans l'apparat du site 21 ; la rubrique 5.1 donne le numéro du texte courant. "
        "Le passage rétabli s'arrête avant la proposition 4.6. Les corrections internes antérieures de machine et l'ajout sont appliqués une fois ; leurs identifiants et leurs entrées d'apparat du site 21 sont conservés. "
        "Les doutes transférés renvoient au site 21. L'incipit abrégé et le renvoi exacts imprimés au site 22 constituent la leçon de page de cette entrée.")
    variant=Variant(sid,recipient,25,22,annotated.count("\n",0,start)+1,ordinal,
        "author-directed restoration","restoration",printed,corrected,reason,reason_fr,False,"")
    replacement=r"\var{"+printed+"}{"+corrected+"}{"+variant.kind+"}{"+sid+"}"
    annotated=annotated[:start]+replacement+annotated[end:]
    variants.append(variant)
    # Each donor ID receives its one apparatus entry on the donor source page.
    # The restoration's body links to those entries rather than duplicating them.
    inherited=[v["source_id"] for v in vv if token(v) in passage]
    vv=donor_restoration_metadata(vv)
    if write_records:
        metadata.write_text(json.dumps(vv,ensure_ascii=False,indent=2)+"\n")
        write_tsv(target/"records/AUTHOR_RESTORATIONS.tsv",[dict(source_id=sid,donor_key=donor,recipient_key=recipient,
            donor_number="4.5",recipient_number="5.1",excluded="Proposition 4.6 and its continuation",
            revived_line_cancellation_ids=" ".join(revived),earlier_correction_ids_applied_once=" ".join(inherited),
            reason=reason,source_reading=printed,restored_reading=corrected)])
    return annotated,variants
