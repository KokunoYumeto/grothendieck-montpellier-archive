# Search coverage and limits

Every one of the 82 late-package claims has its own row in `search_log.tsv`. Claims with the same precise dependency share searches, but each row retains its own formulation, matched results and bounded outcome. Raw requests and responses are retained in `outputs/web_*.json`; some early result-only captures have no saved request object and are never assigned invented query strings.

## Channels actually used

Searches used both available web engines, arXiv full texts and records, Numdam, primary author pages, SGA 1, Grothendieck’s Esquisse, publisher records, bibliographies and backward references. MathOverflow was searched and opened for context, not substituted for primary theorem evidence. zbMATH Open was searched by site queries and direct title-query URL; direct access failed and did not supply an exact usable mathematical result. EGA/SGA and finite-étale-moduli searches led to the opened SGA 1 and Stacks results; no EGA theorem with the literal raw pinned-functor hypotheses was identified, and unverified modern translation hits were not used.

## Access limitations

Asada’s original article and the Diaz–Donagi–Harbater original were not successfully opened. Their historical priority is explicitly reported from McReynolds’s primary reproof. Girondo–González-Diez Example 4.58 was not opened; only its publisher record was checked. The 1992 catalogue’s formula GIFs could not be rendered; the exact 1993 PDF calculation was opened instead. The Lando–Zvonkin exact book section was read in a full-text mirror, with publisher record and author errata checked. No missing project context file is treated as an opened result.

## Backward chronology

The exact sextic first appeared in the located material in the spring-1992 catalogue (as dated by the authors in 1993), then in Bétréma–Zvonkin (1993), §4.3, pp.607–608. The 2003/2004 book and Jones’s 2013 example are later confirmations, not assigned priority. Ellenberg’s source circulated in 2000 and was published in 2002; Wood’s circulated in 2003 and was published in 2006. Guillot’s first arXiv circulation was 2013, its journal volume is 2014, and its actual release was 2015. The Adrianov et al. catalogue circulated in 2007 and appeared in a journal in 2009.

## Meaning of a negative outcome

“No exact result located” refers only to these searches. It does not establish that a theorem is unknown worldwide, and is never alone used to assign class D. Class F is reserved for an unidentified object, formula or topology; class C distinguishes a refuted broad statement from the narrower established framework or proposed repair.
