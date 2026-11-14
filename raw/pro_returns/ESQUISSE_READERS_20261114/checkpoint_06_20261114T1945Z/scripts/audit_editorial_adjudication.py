#!/usr/bin/env python3
"""Publish explicit editorial decisions for checked wording-difference loci.

The manually supplied RETAIN reasons below record editorial consideration, not
new scan inspection. Unlisted loci remain pending; the script never infers a
visual confirmation or an editorial approval from source agreement.
"""
from pathlib import Path
import hashlib,json
from audit_inventory import read_tsv,write_tsv

EXTRA_EDITORIAL_IDS={
    'D1-003','D1-045','D1-049','D1-050','D1-053','D1-055','D1-058','D1-060',
    'D1-088','D1-094','D1-095','D1-114','D1-159','D1-193','D1-237','D1-248',
    'D1-250','D1-258','D1-260',
}

def needs_editorial(difference):
    """The wording classes plus individually identified lexical-normalization loci."""
    return difference['class'] in {'silent-correction','wording'} or difference['difference_id'] in EXTRA_EDITORIAL_IDS

RETAIN = {
    'D1-003': 'Retain Légo-Teichmüller with its checked accent. The spelling recurs throughout the discussion; no naming convention is substituted.',
    'D1-005': 'Retain the checked heading et corps finis. The alternative sur les corps finis changes the wording; no letter-level slip is established.',
    'D1-006': 'Retain bidimensionelle. The same single-n spelling recurs in the checked text, including pages 2 and 26; it is not treated as an isolated typing slip.',
    'D1-008': 'Retain astéristiques. No checked same-word parallel establishes an isolated corruption of this particular form.',
    'D1-010': 'Retain the checked attribution par A. Grothendieck. Editorial expansion or omission of the initials is unwarranted.',
    'D1-011': 'Retain illu-soires with its source line division. The flagged difference concerns source wording, not an established isolated letter error.',
    'D1-013': 'Retain thèmes de réflexion des as checked. No exact local omission is established by the alternative phrasing.',
    'D1-014': 'Retain bidimensionelles. The single-n stem recurs in the checked text and is preserved consistently.',
    'D1-017': 'Retain valables en toutes dimensions. The plural wording is explicit in the checked source; no isolated correction is established.',
    'D1-026': 'Retain savoir before the listed example. The source uses this construction elsewhere; insertion of à would change the wording without a demonstrated slip.',
    'D1-030': 'Retain points bases. The same plural phrase occurs again on page 8; no isolated change to the authorial usage is established.',
    'D1-037': 'Retain explicité. The relation to the preceding expression does not supply a checked same-form parallel establishing an isolated ending error.',
    'D1-041': 'Retain occurence. The same spelling recurs on pages 30 and 35; no isolated spelling correction is assigned.',
    'D1-044': 'Retain the checked quotation punctuation around jeu de Légo-Teichmüller (grande boite). The source does not supply a closing mark at the suggested position.',
    'D1-046': 'Retain points bases, also used on page 5. The repeated phrase is preserved.',
    'D1-047': 'Retain tels des twists. No unique referent or checked same-form parallel establishes an isolated agreement correction here.',
    'D1-054': 'Retain muni. No checked munie parallel yet establishes this occurrence as an isolated typing omission; recurring agreement forms are not changed wholesale.',
    'D1-057': 'Retain associées à des courbes. The plural wording is explicitly checked and no isolated error is established.',
    'D1-061': 'Retain dégagé and its line division. A proposed agreement change lacks a checked same-form parallel establishing an isolated omission.',
    'D1-062': 'Retain pendant quelque temps. The singular expression is the checked authorial wording.',
    'D1-068': 'Retain développé tant soit peu. The surrounding passage includes dictionnaire as well as existence, so no unique letter-level correction is established.',
    'D1-075': 'Retain de genre zéro. The wording is explicit in the checked source.',
    'D1-093': 'Retain trésaillir. The complete checked copy supplies no tressaillir parallel establishing an isolated accent error.',
    'D1-103': 'Retain correspondants. The passage refers to subgroups and Tate modules; no unique agreement correction is established from the checked wording.',
    'D1-104': 'Retain bien peu de choses. The plural wording is explicit in the checked source.',
    'D1-110': 'Retain sens pour des polyèdres réguliers. The alternative phrasing does not establish an isolated source slip.',
    'D1-111': 'Retain polygônes. The same circumflex spelling appears on page 26 and is preserved as recurring usage.',
    'D1-119': 'Retain sur les corps premiers. The plural wording is explicitly checked; no isolated omission or substitution is established.',
    'D1-124': 'Retain restreint. The complete checked copy supplies no restreints parallel; plural context alone is not used to regularize this agreement ending.',
    'D1-126': 'Retain arguments de spécialisation standards. The adjective agrees with the written plural arguments; no correction is warranted.',
    'D1-128': 'Retain crû. No checked occurrence of the corresponding unaccented form establishes an isolated typing error.',
    'D1-129': 'Retain réunisse. The alternative réussisse is not yet supported by a checked same-word parallel; do not infer a source correction from its presence in a draft.',
    'D1-135': 'Retain déduits. No checked déduites parallel establishes an isolated ending error, and recurring agreement forms are not globally changed.',
    'D1-137': 'Retain degénérescence. The complete checked copy supplies no dégénérescence parallel establishing an isolated accent omission.',
    'D1-139': 'Retain bidimensionelle. The single-n stem recurs on the contents page and page 2.',
    'D1-140': 'Retain the second bidimensionelle on this page for the same reason: it repeats the checked authorial spelling.',
    'D1-144': 'Retain polygônes, also written on page 20. The recurring circumflex is not corrected as an isolated slip.',
    'D1-145': 'Retain the explicit uncertainty crc isements|croisements. An editorial replacement must not erase the unresolved scan reading.',
    'D1-153': 'Retain homéomorphisme pending a checked homéomorphismes parallel. The plural context suggests an ending omission but is not used alone to normalize this form.',
    'D1-167': 'Retain développés. No checked feminine plural of the same participle establishes an isolated omission; related masculine agreement forms recur in this discussion.',
    'D1-168': 'Retain occurence, also written on pages 6 and 35. The recurring spelling is preserved.',
    'D1-189': 'Retain équisingularité convenables. The source accent is present and convenables qualifies the plural hypothèses.',
    'D1-194': 'Retain articielle. The complete checked copy supplies no exact artificielle parallel; the proposed missing letters have not met the evidence rule used for isolated slips.',
    'D1-195': 'Retain développé. This masculine form participates in recurring agreement choices in the discussion; no isolated same-form correction is established.',
    'D1-196': "Retain tout ce qu'il y a de plausible. The checked wording is a complete expression; the alternative plural is not required by the written construction.",
    'D1-198': 'Retain occurence, a spelling already checked on pages 6 and 30.',
    'D1-199': 'Retain dévissage général. Général can qualify the written masculine noun dévissage; no isolated correction is established.',
    'D1-200': 'Retain développé. The passage includes the masculine dévissage; no unique correction is established by the alternative agreement.',
    'D1-201': 'Retain révélé. The complete checked copy supplies no exact révélée parallel; the surrounding agreement forms are not silently regularized.',
    'D1-204': 'Retain the second occurence on this page as recurring checked spelling.',
    'D1-208': 'Retain topologies étale. The draft changes topologies to singular, while another possible intervention would change étale to plural; the checked evidence does not establish one unique isolated correction.',
    'D1-210': 'Retain progressées. The complete checked copy supplies no exact progressé parallel; the draft reading alone does not establish the correction.',
    'D1-214': 'Retain ils sont obtenus. The preceding explanation names both strates and espaces; no unique source pronoun correction is established.',
    'D1-219': 'Retain compactifications schématique pending a checked schématiques parallel. The plural context alone is not used to regularize all agreement endings.',
    'D1-226': 'Retain où with its visible accent. It introduces the cases in which the automorphism-group property holds; the unaccented draft form loses a source mark.',
    'D1-230': "Retain s'est agit pending a checked s'est agi parallel. The final t is explicitly confirmed in the scan; no editorial correction has yet been approved.",
    'D1-233': "Retain j'aie été amené. The relative clause follows le plus draconien and admits the subjunctive; the original DIFFERENCES note calling aie a typo does not establish a correction. Root explicitly retained it.",
    'D1-236': "Retain L'idée ici est d'introduire. The checked order is clear, and no isolated typing error supports moving ici.",
    'D1-242': 'Retain dans le cas de strates lisses. The checked indefinite construction is complete; adding s to de would change the wording without an established slip.',
    'D1-245': 'Retain les premiers dans une série. The checked construction is complete; substituting de changes the wording without an established typing slip.',
    'D1-247': 'Retain déserpoir. The complete checked copy supplies no exact désespoir parallel; the draft reading alone does not establish the correction.',
    'D1-252': 'Retain Histoire de Modèles in the singular. Both title mentions on the same page repeat Histoire, and the next page does too.',
    'D1-254': 'Retain Eilenberg-Maclane as written. No alternative spelling of this name occurs in the checked pages; the source naming is not replaced from external convention.',
    'D1-259': 'Retain chapître. No checked chapitre parallel establishes an isolated circumflex insertion in this source occurrence.',
    'D1-263': 'Retain serai. The future form can present the anticipated solitary work from the narrative viewpoint; the draft conditional alone does not prove an accidental missing s.',
    'D1-265': 'Retain répéré. The intended verb has not been established by an exact checked parallel; root explicitly rejected an automatic choice between repéré and répété.',
    'D1-266': 'Retain A. Campo with the checked period and space. No same-name parallel in the checked text establishes a source apostrophe; external naming convention is not substituted.',
    'D1-269': 'Retain occurence and its source line division. The same spelling is repeatedly checked on pages 6, 30 and 35.',
    'D1-271': 'Retain téléscopage. No checked télescopage parallel establishes an isolated accent insertion.',
    'D1-278': 'Retain métier de mathématiciens. The plural names the practitioners collectively; no unique accidental ending is established by the draft singular.',
    'D1-282': 'Retain aux dépens with the checked plural article. The draft removes a source letter; no correction is warranted.',
    'D1-283': 'Retain sibyllin with the checked order of i and y. The alternate draft spelling supplies no reason to alter the source.',
    'D1-045': 'Retain boite without a circumflex. This spelling repeats in the same discussion and was explicitly designated for preservation by root.',
    'D1-049': 'Retain boite without a circumflex, following the repeated checked spelling on this page.',
    'D1-050': 'Retain the same unaccented boite in La boite la plus petite; no isolated accent omission is established.',
    'D1-053': 'Retain the unaccented grande boite, matching the other source occurrences.',
    'D1-055': 'Retain arètes. Root explicitly designated this source spelling for preservation; the difference in accent is not silently regularized.',
    'D1-058': 'Retain petite boite without a circumflex, matching the repeated source usage on pages 8 and 9.',
    'D1-060': 'Retain grande boite without a circumflex, matching the repeated source usage on pages 8 and 9.',
    'D1-088': 'Retain grosso-modo with the source hyphen. The draft spacing is a normalization, not evidence of a unique typing slip.',
    'D1-094': 'Retain quelques 1 300 pages. No checked same-construction parallel establishes an isolated final-s error; the authorial approximate-quantity phrasing is preserved.',
    'D1-095': "Retain Assez vite il s'oriente in the source present tense. The retrospective narrative permits this change of viewpoint; replacing it with another tense would edit the wording.",
    'D1-114': 'Retain polygône with the circumflex. The same stem is written polygônes on pages 20 and 26; the existence of other spellings does not make this repeated form an isolated slip.',
    'D1-159': "Retain c'est à dire with the source spacing. No global hyphen standardization is applied.",
    'D1-193': 'Retain celà. The same page also has cela, but the coexistence of the two spellings does not by itself establish that the grave accent was accidental; no isolated correction has been approved.',
    'D1-237': 'Retain fonction de 0 variables. The source wording and numeral are explicit; no reformulation of the zero-variable case is made.',
    'D1-248': "Retain d'Illusie with the checked apostrophe and capitalization. The original difference concerns draft presentation, not a proven source slip.",
    'D1-250': 'Retain au delà with the source spacing. No global hyphen standardization is applied.',
    'D1-258': 'Retain van Kampen with the source capitalization. External naming style is not substituted for the checked source.',
    'D1-260': 'Retain terre à terre with the source spacing. The same phrase elsewhere has hyphens; this typographic variation is preserved.',
    'D1-289': "Retain que j'ai laissé passer. The source has laissé followed by an infinitive; the checked material does not establish this construction as an accidental omission of e. The alternate agreement is not imposed.",
    'D1-294': 'Retain impréssionné. The visible acute accent is confirmed, and the complete checked copy supplies no exact impressionné parallel establishing an isolated accidental accent.',
    'D1-297': "Retain s'est dégagé. The checked text supplies no exact dégagée parallel; the masculine participial endings already retained in related passages are not globally regularized.",
    'D1-301': 'Retain occurence. The single-r spelling recurs on pages 6, 30, 35 and 47 and is preserved throughout the French forms.',
    'D1-303': 'Retain en termes d\'un monde algébrique with its source quotation marks. The indefinite article is explicit and the passage supplies no evidence of an accidental added word.',
    'D1-315': 'Retain cartes de congruence. Congruence names the qualifying property in this phrase; adding a plural s is not an established correction of an isolated typing slip.',
    'D1-316': 'Retain les cartes de congruence. The definite article identifies the maps described in the parenthesis; the draft des does not establish an accidental letter substitution.',
    'D1-317': 'Retain ce système d\'espaces. The checked spelling système is complete; the draft sytème drops a source letter.',
    'D1-319': 'Retain the second prose arrow X_{i,j} to X_i as printed. The diagram gives the ordinary proper-fibration arrow to X_i and the hooked bordering-inclusion arrow to X_j. The discrepancy concerns the first prose target, which is also X_i; the guide records the actual map labels and targets. Mathematical source notation is unchanged.',
    'D1-320': 'Retain les strates d\'indice i et j. The singular indice can distribute over the two named strata; the source gives no evidence of an accidentally omitted s.',
    'D1-321': 'Retain les deux carrés de droite. Droite is the directional noun in de droite; the draft droites adds a source letter without an established typing correction.',
}


def main():
    edition=Path(__file__).resolve().parent.parent
    work=edition.parent
    checked={p.stem:p for p in (edition/'checked_pages').glob('*.tex')}
    candidates=read_tsv(edition/'records/EDITORIAL_CANDIDATES.tsv')
    by_diff={d:c for c in candidates for d in c.get('difference_ids','').split(';') if d}
    variants=json.loads((edition/'editorial_variants.json').read_text())
    variant_lookup={(v['key'],v['old'],v['new']):v for v in variants}
    scan_rows={r['difference_id']:r for r in read_tsv(edition/'DIFFERENCES_OUTCOMES.tsv')}
    rows=[]
    for key,path in sorted(checked.items()):
        packet=json.loads((work/'review_packets'/(key+'.json')).read_text())
        for d in packet['differences']:
            if not needs_editorial(d):continue
            did=d['difference_id'];candidate=by_diff.get(did);variant=None
            source_ids=[did]+[f'L-{key}-{n:03d}' for n in d['literal_matching_lines']]
            if candidate:
                variant=variant_lookup.get((key,candidate['page_reading'],candidate['proposed_reading']))
                outcome='approved isolated slip' if variant else 'retained after editorial consideration' if candidate['status'].startswith('retained') else 'proposed isolated slip; pending root decision'
                reason=candidate['reason_en']
                line_id=f"L-{key}-{int(candidate['line']):03d}"
                if line_id not in source_ids:source_ids.append(line_id)
            elif did in RETAIN:
                outcome='retained after editorial consideration'
                reason=RETAIN[did]
            else:
                outcome='pending editorial consideration'
                reason='This newly checked locus has not yet received an editorial decision; no correction or retention is inferred automatically.'
            rows.append(dict(adjudication_id='EA-'+did,difference_id=did,key=key,
                typescript_page=d['typescript_page'],source_class=d['class'],source_page_reading=d['page'],
                candidate_id=candidate['candidate_id'] if candidate else '',variant_id=variant['id'] if variant else '',
                editorial_outcome=outcome,reason=reason,source_ids=';'.join(source_ids),
                scan_decision_ids=scan_rows.get(did,{}).get('decision_ids',''),
                checked_sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    fields=['adjudication_id','difference_id','key','typescript_page','source_class','source_page_reading',
        'candidate_id','variant_id','editorial_outcome','reason','source_ids','scan_decision_ids','checked_sha256']
    path=edition/'records/EDITORIAL_ADJUDICATIONS.tsv'
    previous={r['difference_id']:r for r in read_tsv(path)} if path.exists() else {}
    history_path=edition/'records/EDITORIAL_ADJUDICATION_HISTORY.tsv'
    history=read_tsv(history_path) if history_path.exists() else []
    serials={}
    for h in history:serials[h['difference_id']]=serials.get(h['difference_id'],0)+1
    for r in rows:
        old=previous.get(r['difference_id'])
        if old and any(old.get(f)!=r.get(f) for f in ['candidate_id','variant_id','editorial_outcome','reason']):
            n=serials.get(r['difference_id'],0)+1;serials[r['difference_id']]=n
            history.append(dict(revision_id=f"{r['adjudication_id']}-H{n:03d}",**old,
                superseding_outcome=r['editorial_outcome'],superseding_reason=r['reason']))
    if history:write_tsv(history_path,history,['revision_id']+fields+['superseding_outcome','superseding_reason'])
    write_tsv(path,rows,fields)
    counts={v:sum(r['editorial_outcome']==v for r in rows) for v in sorted({r['editorial_outcome'] for r in rows})}
    print(json.dumps({'checked_pages_in_scope':len(checked),'wording_loci':len(rows),'outcomes':counts},ensure_ascii=False))


if __name__=='__main__':main()
