# Pfluger1960: bounded article-level zbMATH / EuDML route

Date: 2026-11-19, 17:47–17:50 UTC. Researcher: GPT-6 Astra Pro, OpenAI, agent part_a567.

## Outcome and evidence limit

No actual target record in zbMATH Open or EuDML was read, and no independently advertised original full-text link was obtained. The official zbMATH entry point returned a403 Forbidden response and was not retried. The EuDML entry point timed out; no catalogue/form reading is claimed from that response. Pfluger1960 remains **unread**, with no mathematical status change and no progress movement.

An indexed later EMS bibliography identifies the paper as **Zbl0112.05303**, **MR0132827**. That is a bibliographic discovery lead from the returned search text, not a reading of a zbMATH review, an actual target registry record, or the original1960 theorem. No review or abstract is substituted for the requested original.

## Prior-route check

Searched the retained authored notes and source bibliography for zbMATH, Zentralblatt and EuDML, then inspected only matching contexts in saved Pfluger metadata. The only prior Pfluger-related EuDML occurrence was an unrelated row in the Bielefeld serial registry output, not an article-level target record. Earlier Fujiwara/Gabber references to zbMATH concern other works. This article-level route was therefore distinct from the already completed Mathdoc serial/physical-holdings audit.

The known publisher subscription route, Mathdoc holdings, IA/TDL, Hathi, ETH and other earlier source attempts were not requested again.

## Exact queries and actually observed links

### Search batch1: system2,17:47:58 UTC

- site:zbmath.org "Pfluger" "Verheftung"
- site:eudml.org "Pfluger" "Konstruktion"

The returned response was explicitly empty. This is only a negative search-engine response for those strings, not an exhaustive registry search.

### Search batch2: system1,17:48:06 UTC

- "Pfluger" "Konstruktion Riemannscher" zbMATH
- site:eudml.org "Verheftung" "Pfluger"

Ten source blocks returned. The useful metadata lead is the EMS paper *On removable sets for holomorphic functions*, EMS Surveys in Mathematical Sciences2(2015),219–254. Its indexed printedp253 reference[49] gives the exact Pfluger title, J.Indian Math.Soc.(N.S.)24(1960),401–412, Zbl0112.05303 and MR0132827. Actual returned URL: https://ems.press/content/serial-article-files/36977, ref turn177681311search5. Its complete PDF was not requested or represented as newly read in this task.

The same search advertised the Math-Net bibliography URL https://www.mathnet.ru/links/41a1060803bc9da8a5ac2018c94b1047/rm_9919_refs_eng.htm. An actual open at17:48:29 UTC redirected to https://www.mathnet.ru/, returning the general homepage (turn665567850view0). Consequently this open did not provide a target-reference link or the expected bibliography page. No alternate Math-Net path was inferred.

### Search batch3: system1,17:48:39 UTC

- "0112.05303"
- "Ueber die Konstruktion" "eudml"

Four source blocks returned: the same EMS indexed reference (turn439480796search3) and unrelated algebraic-number-theory records. No actual target registry URL was returned. Those unrelated original works were not opened.

### Official public entry points,17:49:05 UTC

- https://zbmath.org/: tool ref turn939692856view0, reported403 Forbidden. Stopped; no ordinary-HTTP retry, alternative API, challenge handling or constructed target URL.
- https://eudml.org/: tool ref turn939692856view1, reported "(400) Timeout fetching." This is a tool access failure, not a successfully read remote catalogue or an empty result set. Stopped without a retry.

The two homepage requests were normal public registry entry points; no hidden or inferred article-content URL was used. Since no target record was actually obtained, there were no independently advertised original full-text links to inspect.

## Exact operations, times and compact provenance

Five web-tool calls executed6 queries in3 batches and3 open commands in2 batches. Tool-internal network/cache counts are unknown. No separate ordinary HTTP request or article-file retrieval occurred.

| Cached operation | StartUTC | Measured tool-call seconds | Returned source blocks |
|---|---|---:|---:|
|search1|17:47:58|0.317|0|
|search2|17:48:06|1.098|10|
|refs open|17:48:29|1.117|1|
|id_search|17:48:39|0.803|4|
|homes open|17:49:05|0.617|2|

These are actual Date.now intervals around the awaited calls, excluding following clock reads. The counts describe returned source blocks, not search-engine hit totals.

Complete raw search/open bodies reside exclusively in /workspace/scratch/9c53b536a97f/source_reading/recorded_web_search/part_a567_pfluger_article_registry_*_raw.json. Compact counterparts under code/part_a567_pfluger_article_registry_*_metadata.json retain exact commands, original timestamps/times, source headings, URLs, refs, redirects/failures and bounded outcomes. code/part_a567_pfluger_article_registry_metadata_output.json records raw-cache and compact-file SHA256s/byte counts.

The local summarization utility code/part_a567_pfluger_article_registry_metadata.py made zero network calls and took0.004282533998775762seconds to read the already cached results, parse metadata and write the compact records, excluding final output serialization. No mathematical program, finite certificate or numerical test ran. No TeX, bibliography or aggregate was edited. This bounded route is stopped with the named-original gate unchanged.

