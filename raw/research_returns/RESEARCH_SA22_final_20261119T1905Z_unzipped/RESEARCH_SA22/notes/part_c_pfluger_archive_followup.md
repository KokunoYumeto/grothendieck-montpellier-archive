# Pfluger1960: independent public-archive follow-up

19 November2026, 13:55–13:57UTC. Reviewer: GPT-6 Astra Pro, OpenAI, ChatGPT Pro mode.

## Outcome

The historical publisher landing page and abstract were opened, but the mathematical article remains **not opened**. The public archive preserves the same subscription barrier: both captured galley routes redirect to a login URL whose query explicitly says payment.loginRequired.forArticle. Those redirects were recorded without following them. No current protected publisher endpoint was contacted.

This is a negative original-source retrieval audit, not a mathematical gap or a reason to weaken the separately proved welding results. The literal named-source delivery requirement remains open.

## Exact discovery and original publisher metadata

Six public Wayback CDX catalogue queries examined the known old OJS landing URL and its view/download descendants, with and without www. No guessed galley identifier or private filename was requested. The public catalogue actually advertised:

- Landing capture20171204062844: http://informaticsjournals.com/index.php/jims/article/view/16922, HTTP200, text/html.
- Galley view capture20180923020804: http://www.informaticsjournals.com:80/index.php/jims/article/view/16922/14139, HTTP302, text/html.
- Galley download capture20180923020034: http://www.informaticsjournals.com:80/index.php/jims/article/download/16922/14139, HTTP302, text/html.

The landing capture was actually downloaded through the public archive at:

https://web.archive.org/web/20171204062844id_/http://informaticsjournals.com/index.php/jims/article/view/16922

It is saved as sources/part_c_pfluger_landing_2017.html, 75,877bytes, SHA256 9c68cdd8c3424c461d45f1edce3e4e65d70b7ff42174c010440523035fcfb1e9. A separate web-tool open failed (turn388382871view0); that failure is not confused with the successful ordinary HTTP retrieval.

The actual publisher HTML identifies the title, author, volume24, issue3–4, pp401–412, September–December1960 and DOI10.18311/jims/1960/16922. It contains the short introductory abstract about constructing Riemann surfaces by polygon gluing. It does not expose the article's theorem statements or proofs. Exact local locators are lines41–51 for bibliographic metadata and advertised PDF URL;1343–1362 for issue/title/abstract;1375–1378 for the galley link and the explicit Restricted Access icon. The generic PDF icon has misleading Open Access alt text, but the immediately following access-status icon is restricted, and the actual archived response confirms the restriction. We do not infer access from the generic icon.

## Historical redirect evidence

The galley-view capture returns HTTP302 with Location:

https://web.archive.org/web/20180923020804id_/http://www.informaticsjournals.com/index.php/jims/login?source=%2Findex.php%2Fjims%2Farticle%2Fview%2F16922%2F14139&loginMessage=payment.loginRequired.forArticle

The galley-download capture returns HTTP302 with the corresponding download source path and the same payment.loginRequired.forArticle flag. Both bodies consist of one newline, not PDF bytes. The script deliberately disabled redirect following; no login page, credential operation, protected full text, or present publisher service was requested.

The current publisher restriction previously established by root is independently consistent with this older archived restriction. The archive route does not yield a public original article, and work on this route stops here.

## Program scope and runtimes

| Program | Scope | Requests | Runtime | Result |
|---|---|---:|---:|---|
| code/part_c_pfluger_public_cdx.py | Six public archive catalogue lookups | 6 | 13.074008558s | Actual landing and restricted galley captures discovered |
| code/part_c_pfluger_capture_audit.py | Only three advertised historical captures; redirects disabled | 3 | 9.217950619s | Landing HTML200; two archived login redirects302 |

Each program is saved with its exact stdout and complete JSON output. Start times are respectively2026-11-19T13:55:59.465496+00:00 and2026-11-19T13:56:39.605512+00:00. Per-request URLs, statuses, hashes, timings and redirects are preserved. These are source-access utilities, not proof-verification programs.
