#!/usr/bin/env python3
"""Record editorial candidates with checked-text evidence; apply no correction."""
from pathlib import Path
import csv,json
from audit_inventory import read_tsv,write_tsv

def main():
    edition=Path(__file__).resolve().parent.parent
    work=edition.parent
    sources={p.stem:p.read_text() for p in (edition/"checked_pages").glob("*.tex")}
    decisions=read_tsv(edition/"CHECK_DECISIONS.tsv") if (edition/"CHECK_DECISIONS.tsv").exists() else []
    specs=[
      ("EC-001","esq_119_004","inadéquante","inadéquate","","",
       "Lecture de la copie 1 établie; attendre l'examen de la correction portée dans la copie 2 avant de décider cette correction éditoriale.",
       "The copy 1 reading is established; the reported correction in copy 2 remains to be examined before this editorial change is decided.","await copy 2 review"),
      ("EC-002","esq_119_006","des surface.","des surfaces.","esq_119_005","surfaces",
       "Le pluriel est imposé localement par « des »; le même substantif est écrit « surfaces » à la page 3. La correction ajoute le s final manquant.",
       "The local article des requires the plural; the same noun is written surfaces on page 3. The proposed correction supplies the missing final s.","proposed; root review required"),
      ("EC-003","esq_119_007","voir indispensable","voire indispensable","esq_119_004","voire conformes",
       "La progression « bien plus élégant, voire indispensable » appelle l'adverbe d'enchérissement; la forme « voire » figure à la page 2 (« voire conformes ») et à la page 3. Le e final a été omis ici.",
       "The progression from more elegant to indispensable uses the intensifying adverb; voire occurs on page 2 (voire conformes) and page 3. The proposed correction supplies its omitted final e here.","proposed; root review required"),
      ("EC-004","esq_119_009","convenanble","convenable","esq_119_007","convenable",
       "Un n supplémentaire est intercalé dans le mot; « convenable » figure dans le même développement à la page 5.",
       "An extra n is interposed in the word; convenable occurs in the same discussion on page 5.","proposed; root review required"),
      ("EC-005","esq_119_010","Ladegraillerie","Ladegaillerie","esq_119_010","Yves Ladegaillerie.",
       "Le nom « Yves Ladegaillerie » figure à la ligne précédente pour le même participant; le second emploi intercale un r.",
       "The preceding line gives Yves Ladegaillerie for the same participant; the second occurrence interposes an r.","proposed; root review required"),
      ("EC-006","esq_119_014","ramifié seulement on","ramifié seulement en","esq_119_013","ramifiés au plus en les",
       "La préposition « en » introduit les points de ramification; la même construction est écrite « ramifiés au plus en les points » à la page 11. Le o de « on » remplace ici le e.",
       "The preposition en introduces the ramification points; page 11 has the same construction, ramifiés au plus en les points. The o in on replaces e here.","proposed; root review required"),
      ("EC-007","esq_119_016","une directions","une direction","esq_119_027","dans une direction toute",
       "L'article « une » et l'adjectif « conceptuelle » commandent le singulier; la page 25 écrit « dans une direction toute différente ». Le s est ajouté par erreur ici.",
       "The article une and adjective conceptuelle require the singular; page 25 has dans une direction toute différente. The s is added in error here.","proposed; root review required"),
      ("EC-008","esq_119_017","dingueen effet","dingue en effet","esq_119_021","fournit en effet",
       "L'adjectif « dingue » qualifie « la supposition »; « en effet » suit comme locution adverbiale. La séparation « en effet » est explicitement écrite à la page 19. Le blanc manque après « dingue ».",
       "The adjective dingue qualifies la supposition; en effet follows as an adverbial phrase. Page 19 explicitly separates en effet. A space is missing after dingue.","proposed; root review required"),
      ("EC-009","esq_119_012","Iladmet","Il admet","esq_119_012","admet une description",
       "Le pronom « Il » et le verbe « admet » sont soudés dans la frappe. La même page écrit séparément « Il va » et « admet une description »; le groupe cartographique est le sujet de cette phrase.",
       "The pronoun Il and verb admet are run together in the typing. The same page separately writes Il va and admet une description; the cartographic group is the subject of this sentence.","proposed; root review required"),
      ("EC-010","esq_119_013","les trois point 0, 1","les trois points 0, 1","esq_119_013","de trois points, numérotés",
       "Le nombre « trois » impose le pluriel; la même page écrit plus haut « de trois points, numérotés ». Le s final manque au second emploi.",
       "The number trois requires the plural; the same page earlier has de trois points, numérotés. The final s is missing in the second occurrence.","proposed; root review required"),
      ("EC-011","esq_119_006","d'automorphisme d'un groupe profini","d'automorphismes d'un groupe profini","esq_119_009","un groupe d'automorphismes",
       "Le texte parle d'un groupe dont les éléments sont des automorphismes. La construction « un groupe d'automorphismes » figure à la page 7; ici le s final manque dans le même syntagme.",
       "The text speaks of a group whose elements are automorphisms. Page 7 has the construction un groupe d'automorphismes; the final s is absent here in the same phrase.","proposed; root review required"),
      ("EC-012","esq_119_024","nouveau ;","nouveaux ;","esq_119_022","nouveaux",
       "« Des charmes » est au pluriel; la forme « nouveaux » figure à la page 20. Le x final manque dans cette occurrence.",
       "Des charmes is plural; the form nouveaux occurs on page 20. The final x is missing in this occurrence.","proposed; root review required"),
      ("EC-013","esq_119_024","l'isosaèdre","l'icosaèdre","esq_119_024","un icosaèdre",
       "La suite immédiate donne « un icosaèdre » pour le même polyèdre. Le premier emploi porte un s à la place du c.",
       "The immediately following text gives un icosaèdre for the same polyhedron. The first occurrence has s in place of c.","proposed; root review required"),
      ("EC-014","esq_119_025","les caractéristique 2 et 5","les caractéristiques 2 et 5","esq_119_025","l'une des caractéristiques",
       "L'article « les » et les deux caractéristiques énumérées imposent le pluriel; la ligne précédente comporte déjà « l'une des caractéristiques ». Le s final manque ici.",
       "The article les and the two listed characteristics require the plural; the preceding line already has l'une des caractéristiques. The final s is absent here.","proposed; root review required"),
      ("EC-015","esq_119_027","variété algèbrique","variété algébrique","esq_119_027","géométrie algébrique moderne",
       "Cette page donne deux fois « géométrie algébrique » avec un accent aigu, ainsi que « courbes algébriques ». L'accent grave isolé de « variété algèbrique » paraît être une faute de frappe; la proposition vise cette occurrence seule.",
       "This page twice has géométrie algébrique with an acute accent, and also courbes algébriques. The isolated grave accent in variété algèbrique appears to be a typing slip; this proposal concerns that occurrence alone.","proposed; root review required"),
    ]
    approved_path=edition/"editorial_variants.json"
    approved=json.loads(approved_path.read_text()) if approved_path.exists() else []
    approval_set={(v["key"],v["old"],v["new"]) for v in approved}
    rows=[]
    for cid,key,old,new,evkey,ev,fr,en,status in specs:
        if key not in sources or old not in sources[key]:continue
        if evkey and (evkey not in sources or ev not in sources[evkey]):continue
        packet=json.loads((work/"review_packets"/(key+".json")).read_text())
        oldline=next((l["line"] for l in packet["source_lines"] if old in l["text"]),"")
        if not oldline:
            oldline=next((int(d['line']) for d in decisions if d['key']==key and old in d['image_reading'] and d['line'].isdigit()),'')
        ids=[r["decision_id"] for r in decisions if r["key"]==key and r["source_item_id"]==f"L-{key}-{oldline:03d}"] if isinstance(oldline,int) else []
        evline=""
        if evkey:
            ep=json.loads((work/"review_packets"/(evkey+".json")).read_text())
            evline=next((l["line"] for l in ep["source_lines"] if ev in l["text"]),"")
        if (key,old,new) in approval_set:status="approved by root for corrected master; diplomatic source unchanged"
        rows.append(dict(candidate_id=cid,key=key,cote="119",site=packet["metadata"]["site"],
            typescript_page=packet["metadata"]["ts_page"],line=oldline,page_reading=old,proposed_reading=new,
            kind="slip corrected",reason_fr=fr,reason_en=en,evidence_key=evkey,evidence_line=evline,
            evidence_reading=ev,decision_ids=";".join(ids),status=status))
    fields=["candidate_id","key","cote","site","typescript_page","line","page_reading","proposed_reading","kind","reason_fr","reason_en","evidence_key","evidence_line","evidence_reading","decision_ids","status"]
    write_tsv(edition/"records/EDITORIAL_CANDIDATES.tsv",rows,fields)
    print(json.dumps({"candidates":len(rows),"approved_for_master":sum(r['status'].startswith('approved') for r in rows),"applied_to_checked_pages":0,"remaining":"unapproved candidates await root decision"}))

if __name__=="__main__":main()
