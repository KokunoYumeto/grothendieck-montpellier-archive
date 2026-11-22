# Distinct public IHES archive route for Fujiwara

19 November 2026,16:56–16:59UTC. The root checked the public IHES Item/File catalogue using the ordinary GET form previously observed and saved during the Gabber work. No endpoint, file name or credential was guessed.

Two new queries were made concurrently: `Fujiwara` returned two records, and `tubular` returned zero. Both responses were HTTP200. The complete utility took6.920292277005501seconds; individual requests took6.917198251001537 and6.91060863599705seconds. Exact URLs, byte counts, response hashes, displayed counts and actual record links are in `code/root_fujiwara_ihes_public_output.json`; raw catalogue HTML/text are reproducible reading caches under `sources/`.

The two actual record links were then opened, in one measured1.014-second web call. Despite their `.pdf` suffixes, both returned HTML catalogue descriptions. The root read both identities: Laurent Lafforgue's *Chtoucas de Drinfeld et correspondance de Langlands*, October2000, M/00/70, and his Tata lectures on the same subject, June2002, M/02/45. Fujiwara appears among their keywords; neither record is his1995 article or1992 preprint. The exact commands and compact output are retained as `code/root_fujiwara_ihes_open.js` and its output JSON.

This establishes only a bounded negative result for the inspected public catalogue and the two returned records. It does not establish that no public original exists elsewhere. No target theorem was read, no further article-file request was made, and the Fujiwara original-source requirement remains open. The lookup changes no theorem, bibliography status or progress-review gate.
