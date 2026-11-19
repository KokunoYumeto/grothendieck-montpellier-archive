# Early-package literature search log

Audit date: 19 November 2026. Every substantive web call is saved in logs/early_search_*.json, including failed routes and irrelevant results. The exact queries and opens below are mechanically indexed from those records; the mathematical outcomes were written after reading the sources.

## Outcomes and limits

- Cartan/Miller: title and bibliography searches led to Cartan’s full original §§1–7, Garvín et al.1998, and the exact Cenkl–Porter1982/1984 sources. Cartan is the exact weighted match. Miller metadata and its prepublication existence are verified, but the early analysis does not claim an independently checked full Miller proof.
- Shadows: French ombres and English divided-power/tail/fully-faithful/localization/Ext searches, including zbMATH, arXiv and MathOverflow targeting, located Nagpal–Snowden. Its complete-noetherian/finitely-presented scope and D/(x) counterexample target differ from the induced-target manuscript claim. Absence of an exact all-module source is not evidence of novelty.
- Integral models: author/arXiv/journal sources for Mandell, Ekedahl and Horel were opened. Their nilpotent finite-type hypotheses, E∞/numerical/binomial targets, and faithfulness/fullness conclusions are retained separately. No equivalence with the manuscript PD category was found.
- Arithmetic and negative maps: original Lucas pp51–52 supplies the digit congruence; the infinite-height MathOverflow presentation was checked directly. Exact saved proofs, rather than search results, settle the stated binomial-family and negative-map refinements.
- Coefficients/topoi: searches on local-coefficient de Rham models, category cohomology, flasque PD algebras and Grothendieck’s later accounts led to official Stacks pages, Cartan’s hypotheses, and actual Pursuing Stacks passages. No source licenses the literal arbitrary-presheaf tensor resolution; it is refuted here.
- Donors: Sullivan’s author bibliography and exact original PDF identify the English minimal-model leaves. SGA7 original scans identify the reused French typescripts. Exact original pages, not later AI translations surfaced by search, control the donor collation.
- Earlier analytic history: primary de Rham metadata, Cartan’s Stein exposé, Grothendieck1966 and DGMS1975 were opened. References not independently proved are explicitly carried as background. EGA IV theorem references were followed through the original SGA argument, not represented as full independent EGA proof checks.
- Access limitations: several Garvín, journal, zbMATH and EGA PDF routes failed. Successful alternate downloads and their paths are preserved. A failure to retrieve a source is never a negative mathematical result.

## Exact saved calls

### early_search_arithmetic_history.json

```json
{
  "system1_search_query": [
    {
      "q": "Lucas 1878 Théorie fonctions numériques binomial coefficients Numdam"
    },
    {
      "q": "Kummer 1852 binomial coefficient carries theorem original paper"
    },
    {
      "q": "\"de Rham\" 1931 \"Cartan\" \"thèse\""
    }
  ],
  "response_length": "long"
}
```

### early_search_arxiv_zbmath.json

```json
{
  "open": [
    {
      "ref_id": "https://arxiv.org/abs/1606.03431"
    },
    {
      "ref_id": "https://arxiv.org/abs/2211.02349"
    },
    {
      "ref_id": "https://arxiv.org/abs/math/0107004"
    },
    {
      "ref_id": "https://zbmath.org/?q=an%3A0379.55002"
    }
  ],
  "response_length": "long"
}
```

### early_search_bib_author_follow.json

```json
{
  "open": [
    {
      "ref_id": "https://www.mat.ucm.es/~vmunozve/articles.html"
    },
    {
      "ref_id": "https://sites.google.com/view/antonio-viruel/research/publications"
    },
    {
      "ref_id": "https://msp.org/pjm/1984/112-1/pjm-v112-n1-p02-p.pdf"
    },
    {
      "ref_id": "https://www.numdam.org/item/PMIHES_1967__32__5_0.pdf"
    }
  ],
  "response_length": "long"
}
```

### early_search_bib_corrections.json

Recheck bibliography titles and original Hodge source

```json
[
  "open author bibliography https://websites.umich.edu/asnowden/papers.html",
  "open arXiv:1606.03431",
  "open DGMS author PDF"
]
```

### early_search_cartan_miller.json

```json
{
  "system2_search_query": [
    {
      "q": "\"Edward Y. Miller\" \"de Rham cohomology with arbitrary coefficients\""
    },
    {
      "q": "\"Théories cohomologiques\" Cartan 1976 Grothendieck"
    },
    {
      "q": "site.zbmath.org Grothendieck Cartan Miller de Rham divided powers"
    }
  ],
  "response_length": "long"
}
```

### early_search_cenkl_final.json

Close exact Cenkl-Porter source gaps after middle-agent full downloads

The raw result preserves the opened source, command and source reference; see the named JSON record.

### early_search_classical_open.json

```json
{
  "open": [
    {
      "ref_id": "https://www.numdam.org/item/BSMF_1878__6__49_1.pdf"
    },
    {
      "ref_id": "https://mathoverflow.net/questions/422317/how-far-is-a-countably-infinite-reduced-abelian-p-group-from-being-an-infinite"
    },
    {
      "ref_id": "https://websites.umich.edu/asnowden/papers.html"
    },
    {
      "ref_id": "https://doi.org/10.1215/ijm/1534924829"
    }
  ],
  "response_length": "long"
}
```

### early_search_cochain_obstruction_find.json

```json
{
  "find": [
    {
      "ref_id": "turn878524008view3",
      "pattern": "THEOREM 2"
    },
    {
      "ref_id": "turn878524008view3",
      "pattern": "5."
    },
    {
      "ref_id": "turn878524008view0",
      "pattern": "Grothendieck"
    }
  ],
  "response_length": "long"
}
```

### early_search_cohomology_classics.json

```json
{
  "system1_search_query": [
    {
      "q": "site:numdam.org Grothendieck \"On the de Rham cohomology of algebraic varieties\""
    },
    {
      "q": "site:numdam.org \"Sur l’Analysis situs\" \"Rham\""
    },
    {
      "q": "site:numdam.org \"Théorèmes fondamentaux\" \"Stein\" \"Cartan\""
    }
  ],
  "response_length": "long"
}
```

### early_search_exact_donor_open.json

```json
{
  "open": [
    {
      "ref_id": "https://www.math.stonybrook.edu/~dennis/publications/PDF/DS-pub-0017.pdf"
    },
    {
      "ref_id": "https://www.math.stonybrook.edu/~dennis/publications/"
    },
    {
      "ref_id": "https://www.numdam.org/article/PMIHES_1966__29__95_0.pdf"
    },
    {
      "ref_id": "https://www.numdam.org/item/JMPA_1931_9_10__115_0/"
    }
  ],
  "response_length": "long"
}
```

### early_search_exact_primary.json

```json
{
  "system1_search_query": [
    {
      "q": "\"de Rham cohomology with arbitrary coefficients\" Miller"
    },
    {
      "q": "Horel binomial rings integral homotopy theorem 5.4"
    },
    {
      "q": "Cenkl cohomology operations higher products de Rham complex 1989 pdf"
    }
  ],
  "response_length": "long"
}
```

### early_search_final_reference_routes.json

```json
{
  "click": [
    {
      "ref_id": "turn257047279view1",
      "id": 207
    },
    {
      "ref_id": "turn257047279view1",
      "id": 206
    }
  ],
  "open": [
    {
      "ref_id": "https://msp.org/pjm/1984/112-1/p03.xhtml"
    },
    {
      "ref_id": "https://www.numdam.org/article/ASENS_1963_3_80_3_213_0.pdf"
    }
  ],
  "response_length": "long"
}
```

### early_search_follow_reference_gaps.json

```json
{
  "find": [
    {
      "ref_id": "turn780343542view0",
      "pattern": "Garvín"
    },
    {
      "ref_id": "turn780343542view2",
      "pattern": "Théorème B"
    }
  ],
  "system2_search_query": [
    {
      "q": "Cenkl Porter 1984 de Rham theorem cubical complexes Pacific 112 35 48 pdf"
    },
    {
      "q": "Cenkl Porter 1982 de Rham theorem simplicial sets Publ Mat 26 337 353"
    }
  ],
  "response_length": "long"
}
```

### early_search_garvin_alternates.json

```json
{
  "system1_search_query": [
    {
      "q": "\"An extension of Miller’s version\" de Rham 1998 pdf"
    },
    {
      "q": "\"An extension of Miller\" \"Theorem\" Garvin"
    },
    {
      "q": "\"Miller\" \"q-extendability\" \"1998\""
    }
  ],
  "response_length": "long"
}
```

### early_search_integral_models.json

```json
{
  "system2_search_query": [
    {
      "q": "\"Horel\" \"binomial\" \"integral\" homotopy 2024"
    },
    {
      "q": "\"Ekedahl\" \"numerical\" \"homotopy\" 2002"
    },
    {
      "q": "\"Cenkl\" \"cohomology operations\" \"de Rham\" 1989"
    }
  ],
  "response_length": "long"
}
```

### early_search_local_cochains.json

```json
{
  "system2_search_query": [
    {
      "q": "\"Cartan\" \"Swan\" \"cohomology\" \"1975\" \"simplicial\""
    },
    {
      "q": "site:stacks.math.columbia.edu simplicial sheaves cohomology presheaf acyclic"
    },
    {
      "q": "\"Deligne\" \"cosimplicial\" \"divided powers\""
    }
  ],
  "response_length": "long"
}
```

### early_search_nagpal_metadata.json

Correct final Nagpal–Snowden title and confirm exact author-verified journal metadata

```json
{
  "find": [
    {
      "url": "https://websites.umich.edu/asnowden/papers.html",
      "pattern": "divided power"
    },
    {
      "url": "https://websites.umich.edu/asnowden/papers.html",
      "pattern": "Illinois"
    }
  ]
}
```

### early_search_negative_hom_search.json

```json
{
  "system2_search_query": [
    {
      "q": "\"divided power\" \"negative degree\" \"Hom\""
    },
    {
      "q": "\"infinite height\" \"divisible\" abelian group example"
    },
    {
      "q": "site:zbmath.org \"divided power\" \"homomorphisms\""
    },
    {
      "q": "site:mathoverflow.net \"infinite height\" divisible group"
    }
  ],
  "response_length": "long"
}
```

### early_search_other_primary_open.json

```json
{
  "open": [
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/08RY"
    },
    {
      "ref_id": "https://stacks.math.columbia.edu/tag/07GK"
    },
    {
      "ref_id": "https://arxiv.org/pdf/math/0107004"
    },
    {
      "ref_id": "https://arxiv.org/pdf/2111.01000"
    }
  ],
  "response_length": "long"
}
```

### early_search_primary_gaps_open.json

```json
{
  "click": [
    {
      "ref_id": "turn780343542view0",
      "id": 91
    }
  ],
  "open": [
    {
      "ref_id": "https://mat.uab.cat/~pubmat/fitxers/download/FileType%3Apdf/FolderName%3Av26%283%29/FileName%3A26382_01.pdf"
    },
    {
      "ref_id": "https://msp.org/pjm/1984/112-1/pjm-v112-n1-p04-p.pdf"
    },
    {
      "ref_id": "https://www.numdam.org/item/PMIHES_1967__32__5_0/"
    }
  ],
  "screenshot": [
    {
      "ref_id": "turn780343542view2",
      "pageno": 7
    }
  ],
  "response_length": "long"
}
```

### early_search_primary_open1.json

```json
{
  "open": [
    {
      "ref_id": "https://websites.umich.edu/~asnowden/papers/dp-061016.pdf"
    },
    {
      "ref_id": "https://matwbn.icm.edu.pl/ksiazki/bcp/bcp45/bcp45112.pdf"
    },
    {
      "ref_id": "https://geoffroy.horel.org/binomial.pdf"
    },
    {
      "ref_id": "https://msp.org/pjm/1989/140-1/pjm-v140-n1-p02-p.pdf"
    }
  ],
  "response_length": "long"
}
```

### early_search_reference_gaps.json

```json
{
  "open": [
    {
      "ref_id": "https://www.impan.pl/en/publishing-house/banach-center-publications/all/45"
    },
    {
      "ref_id": "https://www.numdam.org/article/BSMF_1878__6__49_1.pdf"
    },
    {
      "ref_id": "https://www.numdam.org/item/SHC_1951-1952__4__A18_0.pdf"
    },
    {
      "ref_id": "https://msp.org/pjm/1984/112-1/pjm-v112-n1-p03-p.pdf"
    }
  ],
  "response_length": "long"
}
```

### early_search_sga_donor_exact.json

```json
{
  "open": [
    {
      "ref_id": "https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf"
    },
    {
      "ref_id": "https://link.springer.com/book/10.1007/BFb0068688"
    },
    {
      "ref_id": "https://numdam.org/articles/10.24033/asens.1124/"
    }
  ],
  "response_length": "short"
}
```

### early_search_sga_hodge_picard_search.json

```json
{
  "system1_search_query": [
    {
      "q": "\"SGA 7\" \"12.3.10\" graph Picard I J"
    },
    {
      "q": "\"SGA 7\" \"13.4\" Hodge abeloid"
    },
    {
      "q": "site:zbmath.org \"Modèles de Néron et monodromie\""
    },
    {
      "q": "\"EGA\" \"21.8.5\" Picard curve"
    }
  ],
  "response_length": "long"
}
```

### early_search_shadow_exact2.json

```json
{
  "system1_search_query": [
    {
      "q": "Grothendieck ombres modules puissances divisées"
    },
    {
      "q": "\"divided power algebra\" \"tails\" \"modules\""
    },
    {
      "q": "site:arxiv.org \"Grothendieck\" \"shadows\" \"modules\""
    }
  ],
  "response_length": "long"
}
```

### early_search_shadow_fate.json

```json
{
  "system2_search_query": [
    {
      "q": "Grothendieck \"ombres\" \"modules\" \"puissances divisées\""
    },
    {
      "q": "\"divided power\" \"shadows\" modules Grothendieck"
    },
    {
      "q": "site:mathoverflow.net \"Grothendieck\" \"divided powers\" \"de Rham\""
    }
  ],
  "response_length": "long"
}
```

### early_search_shadow_hom_search.json

```json
{
  "system2_search_query": [
    {
      "q": "\"divided power algebra\" \"fully faithful\" modules"
    },
    {
      "q": "\"divided power\" \"Hom\" \"truncation\" Nagpal Snowden"
    },
    {
      "q": "site:zbmath.org \"divided power\" \"modules\" Grothendieck"
    },
    {
      "q": "site:arxiv.org \"divided power algebra\" \"localization\" \"torsion\""
    }
  ],
  "response_length": "long"
}
```

### early_search_shadow_refs_follow.json

```json
{
  "system2_search_query": [
    {
      "q": "\"The module theory of divided power algebras\" journal 2019 Nagpal Snowden"
    },
    {
      "q": "site:zbmath.org \"The module theory of divided power algebras\""
    },
    {
      "q": "site:mathoverflow.net \"divided power algebra\" \"torsion\""
    },
    {
      "q": "site:numdam.org \"ombres\" \"Grothendieck\""
    }
  ],
  "response_length": "long"
}
```

### early_search_sullivan_donor.json

```json
{
  "system1_search_query": [
    {
      "q": "\"Sullivan\" \"Theorem B\" \"rank of the Hurewicz\""
    },
    {
      "q": "\"Theorem B\" \"beautifully simple\" \"Hirsch\""
    },
    {
      "q": "\"Sullivan\" \"Continuing in this way we construct the minimal model\""
    }
  ],
  "response_length": "long"
}
```

### early_search_topos_comparison_search.json

```json
{
  "system2_search_query": [
    {
      "q": "\"Grothendieck\" \"condition de De Rham\""
    },
    {
      "q": "\"de Rham\" \"topos\" \"flasque\" \"Cartan\""
    },
    {
      "q": "site:mathoverflow.net \"de Rham\" \"cosimplicial\" \"integral\""
    },
    {
      "q": "site:numdam.org \"formes différentielles\" \"topos\""
    }
  ],
  "response_length": "long"
}
```

## Claim-to-search audit

| Claim | Saved raw search logs |
|---|---|
| SA08-C001 | logs/early_search_cartan_miller.json; logs/early_search_cohomology_classics.json; logs/early_search_exact_donor_open.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_primary_open1.json |
| SA08-C002 | logs/early_search_cohomology_classics.json; logs/early_search_sullivan_donor.json |
| SA08-C003 | logs/early_search_cohomology_classics.json; logs/early_search_exact_donor_open.json |
| SA08-C004 | logs/early_search_cohomology_classics.json; logs/early_search_other_primary_open.json; logs/early_search_topos_comparison_search.json |
| SA08-C005 | logs/early_search_cohomology_classics.json; logs/early_search_exact_donor_open.json |
| SA08-C006 | logs/early_search_arxiv_zbmath.json; logs/early_search_exact_donor_open.json; logs/early_search_exact_primary.json; logs/early_search_integral_models.json; logs/early_search_other_primary_open.json; logs/early_search_sullivan_donor.json |
| SA08-C007 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_primary_open1.json |
| SA08-C008 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json |
| SA08-C009 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json; logs/early_search_topos_comparison_search.json |
| SA08-C010 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_primary_open1.json |
| SA08-C011 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json |
| SA08-C012 | logs/early_search_bib_author_follow.json; logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_garvin_alternates.json; logs/early_search_local_cochains.json; logs/early_search_primary_open1.json |
| SA08-C013 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_primary_open1.json |
| SA08-C014 | logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C015 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_primary_open1.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C016 | logs/early_search_other_primary_open.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C017 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_primary_open1.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C018 | logs/early_search_arxiv_zbmath.json; logs/early_search_exact_primary.json; logs/early_search_integral_models.json; logs/early_search_other_primary_open.json |
| SA08-C019 | logs/early_search_arxiv_zbmath.json; logs/early_search_exact_primary.json; logs/early_search_integral_models.json; logs/early_search_other_primary_open.json |
| SA08-C020 | logs/early_search_arxiv_zbmath.json; logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_integral_models.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C021 | logs/early_search_arxiv_zbmath.json; logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_integral_models.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json; logs/early_search_topos_comparison_search.json |
| SA08-C022 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json; logs/early_search_topos_comparison_search.json |
| SA08-C023 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json; logs/early_search_topos_comparison_search.json |
| SA08-C024 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json; logs/early_search_topos_comparison_search.json |
| SA08-C025 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_primary_open1.json |
| SA08-C026 | logs/early_search_arxiv_zbmath.json; logs/early_search_cartan_miller.json; logs/early_search_cenkl_final.json; logs/early_search_cochain_obstruction_find.json; logs/early_search_exact_primary.json; logs/early_search_integral_models.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json |
| SA08-C027 | logs/early_search_arithmetic_history.json; logs/early_search_classical_open.json; logs/early_search_shadow_hom_search.json |
| SA08-C028 | logs/early_search_arithmetic_history.json; logs/early_search_classical_open.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C029 | logs/early_search_arithmetic_history.json; logs/early_search_classical_open.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C030 | logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json; logs/early_search_topos_comparison_search.json |
| SA08-C031 | logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json; logs/early_search_topos_comparison_search.json |
| SA08-C032 | logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C033 | logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C034 | logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C035 | logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C036 | logs/early_search_arithmetic_history.json; logs/early_search_classical_open.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C037 | logs/early_search_arithmetic_history.json; logs/early_search_classical_open.json; logs/early_search_shadow_hom_search.json |
| SA08-C038 | logs/early_search_arithmetic_history.json; logs/early_search_classical_open.json; logs/early_search_shadow_hom_search.json |
| SA08-C039 | logs/early_search_arithmetic_history.json; logs/early_search_classical_open.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C040 | logs/early_search_negative_hom_search.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C041 | logs/early_search_negative_hom_search.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C042 | logs/early_search_negative_hom_search.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C043 | logs/early_search_arithmetic_history.json; logs/early_search_classical_open.json; logs/early_search_other_primary_open.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C044 | logs/early_search_negative_hom_search.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C045 | logs/early_search_negative_hom_search.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C046 | logs/early_search_negative_hom_search.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C047 | logs/early_search_negative_hom_search.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
| SA08-C048 | logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_topos_comparison_search.json |
| SA08-C049 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json; logs/early_search_topos_comparison_search.json |
| SA08-C050 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_primary_open1.json |
| SA08-C051 | logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_topos_comparison_search.json |
| SA08-C052 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json; logs/early_search_topos_comparison_search.json |
| SA08-C053 | logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_topos_comparison_search.json |
| SA08-C054 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_primary_open1.json |
| SA08-C055 | logs/early_search_cartan_miller.json; logs/early_search_cochain_obstruction_find.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_primary_open1.json |
| SA08-C056 | logs/early_search_cartan_miller.json; logs/early_search_cenkl_final.json; logs/early_search_exact_primary.json; logs/early_search_final_reference_routes.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json; logs/early_search_reference_gaps.json; logs/early_search_topos_comparison_search.json |
| SA08-C057 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_primary_open1.json |
| SA08-C058 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_primary_open1.json |
| SA08-C059 | logs/early_search_arxiv_zbmath.json; logs/early_search_cartan_miller.json; logs/early_search_cochain_obstruction_find.json; logs/early_search_exact_primary.json; logs/early_search_integral_models.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json |
| SA08-C060 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json; logs/early_search_topos_comparison_search.json |
| SA08-C061 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json; logs/early_search_topos_comparison_search.json |
| SA08-C062 | logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_topos_comparison_search.json |
| SA08-C063 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json; logs/early_search_topos_comparison_search.json |
| SA08-C064 | logs/early_search_arxiv_zbmath.json; logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_integral_models.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json; logs/early_search_topos_comparison_search.json |
| SA08-C065 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json; logs/early_search_topos_comparison_search.json |
| SA08-C066 | logs/early_search_arxiv_zbmath.json; logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_integral_models.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json; logs/early_search_topos_comparison_search.json |
| SA08-C067 | logs/early_search_exact_donor_open.json; logs/early_search_sullivan_donor.json |
| SA08-C068 | logs/early_search_exact_donor_open.json; logs/early_search_sullivan_donor.json |
| SA08-C069 | logs/early_search_sga_donor_exact.json; logs/early_search_sga_hodge_picard_search.json |
| SA08-C070 | logs/early_search_sga_donor_exact.json; logs/early_search_sga_hodge_picard_search.json |
| SA08-C071 | logs/early_search_sga_donor_exact.json; logs/early_search_sga_hodge_picard_search.json |
| SA08-C072 | logs/early_search_sga_donor_exact.json; logs/early_search_sga_hodge_picard_search.json |
| SA08-C073 | logs/early_search_sga_donor_exact.json; logs/early_search_sga_hodge_picard_search.json |
| SA08-C074 | logs/early_search_sga_donor_exact.json; logs/early_search_sga_hodge_picard_search.json |
| SA08-C075 | logs/early_search_sga_donor_exact.json; logs/early_search_sga_hodge_picard_search.json |
| SA08-C076 | logs/early_search_sga_donor_exact.json; logs/early_search_sga_hodge_picard_search.json |
| SA08-C077 | logs/early_search_sga_donor_exact.json; logs/early_search_sga_hodge_picard_search.json |
| SA08-C078 | logs/early_search_arxiv_zbmath.json; logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_integral_models.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json |
| SA08-C079 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json; logs/early_search_topos_comparison_search.json |
| SA08-C080 | logs/early_search_cartan_miller.json; logs/early_search_exact_primary.json; logs/early_search_local_cochains.json; logs/early_search_other_primary_open.json; logs/early_search_primary_open1.json |
| SA08-C081 | logs/early_search_arithmetic_history.json; logs/early_search_classical_open.json; logs/early_search_shadow_exact2.json; logs/early_search_shadow_fate.json; logs/early_search_shadow_hom_search.json; logs/early_search_shadow_refs_follow.json |
