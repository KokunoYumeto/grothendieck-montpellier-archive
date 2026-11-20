# The doubt marks of the Montpellier archive transcription

Generated 20 Nov 2026, 10:45 UTC by `build_report.py` (Claude Opus 5.5 at effort max), from the returns filed by then: the newest return of each Pro second pass (partial returns included), DM01's newest checkpoint (checkpoint 10, 20 Nov 05:37 UTC), the Claude block pass of 13 Nov, and the text of record. Every number is computed from the files.

- [Summary](#summary)
- [1. The doubt marks: types and where they are](#1-the-doubt-marks-types-and-where-they-are)
- [2. What the second passes did with the doubt marks](#2-what-the-second-passes-did-with-the-doubt-marks)
- [3. The Pro workflows compared](#3-the-pro-workflows-compared)
- [4. Deep zoom: what the data says](#4-deep-zoom-what-the-data-says)
- [5. DM01, the doubt-marks-only run](#5-dm01-the-doubt-marks-only-run)
- [6. Pro's own methods, and whether the prompts carry them](#6-pros-own-methods-and-whether-the-prompts-carry-them)
- [7. The pilots](#7-the-pilots)
- [8. Every way suggested to settle the doubt marks](#8-every-way-suggested-to-settle-the-doubt-marks)
- [9. The intakes: what each return did](#9-the-intakes-what-each-return-did)
- [10. Next steps](#10-next-steps)
- [11. Method, data and limits](#11-method-data-and-limits)

<div id="summary" class="section">

## Summary

<div class="lede">

**128,310 doubt marks** stand open in the text of record today, on 12,518 of its 13,553 pages: 71,321 single readings marked doubtful (`\unsure{a}`), 54,180 choices between readings (`\unsure{a|b}`) and 2,809 illegible places (`\illegible{n}`). Every route marks its doubts the same way. 55,116 of the marks (43.0 %) sit inside struck-out text.

**5,786 of the open marks (4.5 %) have been checked against the scan and stayed doubtful** (4,989 on Pro second passes, 797 on the pages DM01 finished); **122,524 (95.5 %) have not been checked yet**: 114,325 on pages with only a first reading and 8,199 on the pages of the 13 Nov Claude pass. The text itself does not tell the two apart; a way to mark a checked doubt is proposed in section 10.

**Mathematics, per word.** 27.2 % of the words of the text of record are mathematics and 36.8 % of the open marks sit there: per 100 words, 4.76 marks in mathematics against 3.77 in prose (in live text, 3.25 against 2.19; section 1).

**The second passes leave most of the first reading's doubt marks in place.** On the 1,345 pages they have finished (15,987 marks of witness C), the Pro second passes settled 38.5 % of C's marks, the Claude block pass of 13 Nov 10.4 %, and the doubt-marks-only run DM01 45.8 %. Where a mark was settled, C's first reading was wrong 14.4 % of the time in the Pro passes and 14.0 % in DM01.

**DM01 did real work and built its own method.** In 443 minutes it recorded a decision on each of the 1447 marks of 67 pages: it settled 682, changed C's reading at 98 of them, left 765 undecided (573 of these in struck-out text), and found 11 errors outside the marks. It kept a timed record of its workflow (48 entries), with the measured effect of each change (section 5). At its measured pace the remaining 1,237 marks of cote 1 take about 6 hours.

**Hua's text, at the same place, is a strong sign only when it agrees with C.** Where Hua has C's first reading and a Pro pass settled the mark, the pass confirmed C at 719 of 795 (90.4 %). Where Hua has C's other alternative, the Pro passes still kept C's first reading at 191 of 274 (69.7 %) and chose Hua's at 50 (18.2 %); the Claude pass of 13 Nov, which settled far fewer marks, went the other way (48 of 69 for Hua's alternative). No scan has decided between them yet. This bears on 6,070 open marks, the head of the fix queue; Hua is uncertain at the same place at 27,518 more.

**55,116 open marks (43.0 %) are inside struck-out text,** and every pass settles those less often than marks in live text: at 16-60 % of the live-text rate, depending on the pass (section 2).

**Deep zoom:** the data so far cannot separate the effect of zoom depth from the page and the design (section 4); the deep-zoom pieces with fresh readers (SP36, SP37, SP38, SP57) have 62 finished pages between them.

</div>

</div>

<div id="inventory" class="section">

## 1. The doubt marks: types and where they are

Every reading route writes its doubts with the same two commands, defined in each route's preamble: `\unsure{...}` and `\illegible{n}`. A `|` at the top level of `\unsure` separates alternatives (`\unsure{a|b}`, a *choice*); without it the one reading is marked doubtful (`\unsure{a}`, a *single* mark). A `|` that leaves an empty side, as in `\unsure{g=|f|}`, is an absolute value, not a choice. The question marks `??` and `(?)` that also occur in the texts are not counted: many are Grothendieck's own. The counts are over the text of record (`text_of_record/`, the best reading of each of 13,553 pages, La Longue Marche excluded: its edition is its text).

### By route

<div class="tw">

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th>Base reading of the page (its route)</th>
<th class="n">Pages</th>
<th class="n">Pages with a mark</th>
<th class="n">Single</th>
<th class="n">Choice</th>
<th class="n">Illegible</th>
<th class="n">All marks</th>
<th class="n">Marks a page</th>
</tr>
</thead>
<tbody>
<tr>
<td>Work<br />
<span class="small">GPT-6.2 Astra at reasoning effort max in ChatGPT Work</span></td>
<td class="n">5,751</td>
<td class="n">5,610</td>
<td class="n">30,706</td>
<td class="n">29,435</td>
<td class="n">802</td>
<td class="n">60,943</td>
<td class="n">10.6</td>
</tr>
<tr>
<td>Pro first reading<br />
<span class="small">GPT-6 Astra (ChatGPT Pro mode)</span></td>
<td class="n">4,103</td>
<td class="n">3,652</td>
<td class="n">24,448</td>
<td class="n">10,626</td>
<td class="n">625</td>
<td class="n">35,699</td>
<td class="n">8.7</td>
</tr>
<tr>
<td>Codex web<br />
<span class="small">GPT-6 Astra at reasoning effort max in Codex web</span></td>
<td class="n">903</td>
<td class="n">894</td>
<td class="n">5,133</td>
<td class="n">7,026</td>
<td class="n">107</td>
<td class="n">12,266</td>
<td class="n">13.6</td>
</tr>
<tr>
<td>Claude second pass<br />
<span class="small">Claude Opus 5.5 at effort max (13 Nov second pass)</span></td>
<td class="n">898</td>
<td class="n">851</td>
<td class="n">5,032</td>
<td class="n">2,993</td>
<td class="n">174</td>
<td class="n">8,199</td>
<td class="n">9.1</td>
</tr>
<tr>
<td>API (typescripts)<br />
<span class="small">Claude Opus 5.5 at effort high (Message Batches API), typed pages</span></td>
<td class="n">1,361</td>
<td class="n">992</td>
<td class="n">3,784</td>
<td class="n">698</td>
<td class="n">935</td>
<td class="n">5,417</td>
<td class="n">4.0</td>
</tr>
<tr>
<td>Pro second pass<br />
<span class="small">GPT-6 Astra (ChatGPT Pro mode), second pass</span></td>
<td class="n">470</td>
<td class="n">452</td>
<td class="n">1,635</td>
<td class="n">3,273</td>
<td class="n">81</td>
<td class="n">4,989</td>
<td class="n">10.6</td>
</tr>
<tr>
<td>doubt marks settled (DM run)<br />
<span class="small"></span></td>
<td class="n">67</td>
<td class="n">67</td>
<td class="n">583</td>
<td class="n">129</td>
<td class="n">85</td>
<td class="n">797</td>
<td class="n">11.9</td>
</tr>
<tr>
<td>All</td>
<td class="n">13,553</td>
<td class="n">12,518</td>
<td class="n">71,321</td>
<td class="n">54,180</td>
<td class="n">2,809</td>
<td class="n">128,310</td>
<td class="n">9.5</td>
</tr>
</tbody>
</table>

</div>

### By where the page stands

<div class="tw">

| Where the page stands (STATE/PAGE_STATE.tsv) | Pages | Single | Choice | Illegible | All marks |
|----|----|----|----|----|----|
| nothing prepared | 9,191 | 47,979 | 37,961 | 1,935 | 87,875 |
| in a piece ready to send | 2,976 | 17,315 | 8,489 | 580 | 26,384 |
| second pass done | 470 | 1,635 | 3,273 | 81 | 4,989 |
| in a sent second pass | 323 | 1,352 | 2,473 | 43 | 3,868 |
| nothing prepared (Claude pass of 13 Nov only, doubt marks open); doubt marks in DM03 (built, nothing back yet) | 199 | 1,055 | 665 | 19 | 1,739 |
| nothing prepared; doubt marks in DM06 (built, nothing back yet) | 71 | 689 | 442 | 52 | 1,183 |
| doubt marks settled by DM01 (no full second pass) | 67 | 583 | 129 | 85 | 797 |
| nothing prepared (Claude pass of 13 Nov only, doubt marks open); doubt marks in DM04 (built, nothing back yet) | 100 | 314 | 285 | 8 | 607 |
| nothing prepared (Claude pass of 13 Nov only, doubt marks open); doubt marks in DM02 (built, nothing back yet) | 48 | 162 | 288 | 1 | 451 |
| nothing prepared (Claude pass of 13 Nov only, doubt marks open); doubt marks in DM05 (built, nothing back yet) | 32 | 153 | 151 | 3 | 307 |
| nothing prepared (Claude pass of 13 Nov only, doubt marks open) | 39 | 47 | 10 | 0 | 57 |
| nothing prepared; doubt marks in DM01 (the run ended before this page) | 4 | 37 | 14 | 2 | 53 |

</div>

### Checked and still doubtful, or not yet checked

<div class="tw">

| The mark | Pages with such a mark | In live text | In struck-out text | Single | Choice | Illegible | All | Share |
|----|----|----|----|----|----|----|----|----|
| **checked against the scan, still doubtful**: Pro second pass | 452 | 2,712 | 2,277 | 1,635 | 3,273 | 81 | 4,989 | 3.9 % |
| **checked against the scan, still doubtful**: doubt-mark run | 67 | 185 | 612 | 583 | 129 | 85 | 797 | 0.6 % |
| **not yet checked**: Claude pass of 13 Nov only | 851 | 5,051 | 3,148 | 5,032 | 2,993 | 174 | 8,199 | 6.4 % |
| **not yet checked**: first reading only | 11,148 | 65,246 | 49,079 | 64,071 | 47,785 | 2,469 | 114,325 | 89.1 % |
| All | 12,518 | 73,194 | 55,116 | 71,321 | 54,180 | 2,809 | 128,310 | 100.0 % |

</div>

Checked: the page's text of record is a Pro second pass or a doubt-mark run, so a reader has looked at the place on the scan and left the doubt. DM01 took every mark of its pages; the later doubt-mark prompts take the live-text marks only. The pages of the 13 Nov Claude pass count as not second-passed (the decision of 20 Nov), so their marks count as not yet checked.

### By where the mark sits

<div class="tw">

| Where the mark sits | Single | Choice | Illegible | All | Share of all marks |
|----|----|----|----|----|----|
| inside struck-out text (\deleted) | 42,704 | 10,804 | 1,608 | 55,116 | 43.0 % |
| in a margin note (\margin) | 8,137 | 4,320 | 419 | 12,876 | 10.0 % |
| in an insertion (\inserted) | 3,442 | 2,847 | 73 | 6,362 | 5.0 % |
| in mathematics | 24,163 | 31,458 | 151 | 55,772 | 43.5 % |
| in a drawing or diagram | 4,860 | 4,397 | 29 | 9,286 | 7.2 % |

</div>

A mark can sit in several of these at once (a struck formula in a margin note).

### Marks per 100 words: mathematics, prose, drawings

<div class="tw">

| Text | Zone | Words | Share of all words | Open marks | Share of all marks | Marks per 100 words | per 100 words, not yet checked | per 100 words, after a check | Marks per 1,000 letters |
|----|----|----|----|----|----|----|----|----|----|
| **live text** | prose | 1,747,729 | 48.0 % | 38,244 | 29.8 % | 2.19 | 2.20 | 2.04 | 4.61 |
|  | mathematics | 889,785 | 24.4 % | 28,910 | 22.5 % | 3.25 | 3.28 | 2.53 | 7.50 |
|  | drawings and diagrams | 722,401 | 19.8 % | 6,040 | 4.7 % | 0.84 | 0.84 | 0.87 | 1.26 |
| **struck-out text** | prose | 155,082 | 4.3 % | 33,581 | 26.2 % | 21.65 | 22.06 | 16.38 | 48.27 |
|  | mathematics | 101,767 | 2.8 % | 18,289 | 14.3 % | 17.97 | 18.23 | 13.93 | 45.27 |
|  | drawings and diagrams | 23,730 | 0.7 % | 3,246 | 2.5 % | 13.68 | 14.83 | 6.27 | 23.52 |
| **all text** | prose | 1,902,811 | 52.3 % | 71,825 | 56.0 % | 3.77 | 3.77 | 3.78 | 7.99 |
|  | mathematics | 991,552 | 27.2 % | 47,199 | 36.8 % | 4.76 | 4.80 | 4.01 | 11.09 |
|  | drawings and diagrams | 746,131 | 20.5 % | 9,286 | 7.2 % | 1.24 | 1.23 | 1.50 | 1.88 |

</div>

Words are counted the way the alignment counts them: the whitespace-separated pieces of the text with its LaTeX commands written out and each doubt mark written with its first reading, so a formula counts as its symbols and commands (`$f\colon X\to Y$` is five words). Letters are the characters of those words. Mathematics is whatever is inside `$...$`, `\[...\]`, `\(...\)` or a display environment; drawings are `tikzcd` and `tikzpicture`. 'After a check': pages whose text of record is a Pro second pass or a doubt-mark run. In drawings most words are drawing code (coordinates, `\draw`, `node`), so their rate does not compare with the other two. The zones hold 1.1 % more words than the alignment counts, because a word glued to a formula (`d'$X$`) counts once on each side.

### By shape

<div class="tw">

| Shape                            | Marks  |
|----------------------------------|--------|
| choice between 2 readings        | 49,147 |
| choice between 3 readings        | 4,652  |
| choice between 4 or more         | 381    |
| first reading of 1 word          | 88,965 |
| first reading of 2-3 words       | 31,497 |
| first reading of 4 words or more | 5,039  |

</div>

### The 30 cotes with the most open marks

<div class="tw">

| Cote | Pages in the text of record | Open marks | Marks a page | On pages with nothing prepared |
|----|----|----|----|----|
| 157-2 | 440 | 5,183 | 11.8 | 5,183 |
| 157-4 | 404 | 4,778 | 11.8 | 4,778 |
| 157-5 | 345 | 3,972 | 11.5 | 3,972 |
| 157-3 | 355 | 3,729 | 10.5 | 3,729 |
| 157-1 | 266 | 3,539 | 13.3 | 3,539 |
| 136 | 317 | 3,001 | 9.5 | 746 |
| 34 | 203 | 2,750 | 13.5 | 2,602 |
| 43 | 195 | 2,656 | 13.6 | 2,150 |
| 57 | 301 | 2,560 | 8.5 | 2,044 |
| 79 | 294 | 2,560 | 8.7 | 2,560 |
| 154 | 174 | 2,102 | 12.1 | 973 |
| 84 | 190 | 2,057 | 10.8 | 889 |
| 1 | 142 | 2,033 | 14.3 | 0 |
| 156-9 | 138 | 1,995 | 14.5 | 1,995 |
| 156-7 | 113 | 1,955 | 17.3 | 1,828 |
| 83 | 213 | 1,947 | 9.1 | 1,947 |
| 29 | 213 | 1,935 | 9.1 | 1,534 |
| 10 | 187 | 1,833 | 9.8 | 983 |
| 156-8 | 126 | 1,801 | 14.3 | 1,801 |
| 156-6 | 93 | 1,758 | 18.9 | 1,204 |
| 15 | 185 | 1,553 | 8.4 | 415 |
| 161-2 | 99 | 1,474 | 14.9 | 1,474 |
| 25 | 184 | 1,463 | 8.0 | 1,463 |
| 91 | 129 | 1,314 | 10.2 | 743 |
| 137 | 84 | 1,307 | 15.6 | 1,307 |
| 77 | 157 | 1,295 | 8.2 | 1,295 |
| 12 | 144 | 1,289 | 9.0 | 1,174 |
| 134-2 | 180 | 1,289 | 7.2 | 958 |
| 93 | 185 | 1,284 | 6.9 | 1,141 |
| 74 | 125 | 1,259 | 10.1 | 1,259 |

</div>

### Against Hua's text at the same place

<div class="tw">

| What Hua's text has at the same place (matched word by word) | Single | Choice | Illegible | All | Share |
|----|----|----|----|----|----|
| Hua = C's first reading | 5,321 | 6,720 | 0 | 12,041 | 9.4 % |
| Hua = C up to accents/case | 109 | 195 | 0 | 304 | 0.2 % |
| Hua = C's other alternative | 0 | 6,070 | 0 | 6,070 | 4.7 % |
| Hua has a third reading | 14,668 | 11,897 | 0 | 26,565 | 20.7 % |
| Hua also uncertain here | 18,995 | 7,833 | 690 | 27,518 | 21.4 % |
| Hua has nothing here | 4,742 | 1,777 | 218 | 6,737 | 5.3 % |
| Hua has a reading | 0 | 0 | 157 | 157 | 0.1 % |
| Hua not aligned here | 7,822 | 4,156 | 421 | 12,399 | 9.7 % |
| Hua's page does not match (ratio \< 0.25) | 4,137 | 2,877 | 260 | 7,274 | 5.7 % |
| no Hua text for the page | 15,527 | 12,655 | 1,063 | 29,245 | 22.8 % |

</div>

The page-wide match of STATE/doubts_vs_hua.py (a word anywhere on the page), over the pages with nothing prepared, had: Hua has the same reading 31,225; Hua differs 29,394; no Hua text 22,775; Hua has another of the alternatives 5,430. The positional match here is stricter: 'Hua = C's first reading' now means the same word at the same place.

On 869 pages Hua's page aligns with ours under 25 %. Trying his pages three either side of the usual one (his page *n* is our scan *n* + 1) matched 0 of them, so these are not numbering errors: his text of those pages is laid out or worded differently (`data/hua_offsets.tsv`).

</div>

<div id="passes" class="section">

## 2. What the second passes did with the doubt marks

**How this was measured.** For each page a second pass has finished (only the pages its `progress.log` marks done, so partial returns count), three texts are lined up word by word: witness C as the pass received it, the pass's final page, and Hua's page. Each of C's marks is looked up in the final text between the nearest words the two share, and the final reading there is compared with C's alternatives. Whether a pass was right is not measured here: no scan was read for this report. The method was checked against DM01, which records its own decision for every mark: of its 1447 marks the script classifies 1407 the same way (97.2 %). The others are marks glued into one word with a neighbouring mark that stayed doubtful (`data/dm01_check.tsv`).

The runs covered: the newest return of every Pro second pass in `second_pass_returns/` (finals and checkpoints), DM01's newest checkpoint (checkpoint 10, 20 Nov 05:37 UTC), and the Claude block pass of 13 Nov (`second_pass/out/`, whose C is the Pro first reading).

<div class="legend">

C's first reading confirmedanother of C's alternativesa reading C did not listremoved / illegible readstill doubtful (same reading)still doubtful (reading changed)still illegiblenot aligned

</div>

### By design

<div class="tw">

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th>Second pass</th>
<th>C (the first reading) by</th>
<th class="n">Pages finished</th>
<th class="n">C's marks</th>
<th>What happened to them</th>
<th class="n">Settled</th>
<th class="n">C's first reading wrong, where settled</th>
<th class="n">Still doubtful</th>
</tr>
</thead>
<tbody>
<tr>
<td>Claude Opus 5.5 at effort max, block second pass (13 Nov)</td>
<td>Pro first reading</td>
<td class="n">808</td>
<td class="n">7,362</td>
<td><div class="bar">
<span style="width:6.33%;background:#3b8f5a" title="C&#39;s first reading confirmed: 466 (6.3 %)"></span><span style="width:1.89%;background:#d08a1e" title="another of C&#39;s alternatives: 139 (1.9 %)"></span><span style="width:1.86%;background:#c0392b" title="a reading C did not list: 137 (1.9 %)"></span><span style="width:0.35%;background:#8e44ad" title="removed / illegible read: 26 (0.4 %)"></span><span style="width:81.27%;background:#9aa5b1" title="still doubtful (same reading): 5983 (81.3 %)"></span><span style="width:6.56%;background:#c3cbd3" title="still doubtful (reading changed): 483 (6.6 %)"></span><span style="width:1.74%;background:#6c7a89" title="still illegible: 128 (1.7 %)"></span>
</div></td>
<td class="n">10.4 %</td>
<td class="n">39.3 %</td>
<td class="n">89.6 %</td>
</tr>
<tr>
<td>GPT-6 Astra (ChatGPT Pro mode), one reader, large piece (SP02, SP04, SP12, SP14; sent 14-17 Nov)</td>
<td>Codex web</td>
<td class="n">328</td>
<td class="n">4,682</td>
<td><div class="bar">
<span style="width:35.60%;background:#3b8f5a" title="C&#39;s first reading confirmed: 1667 (35.6 %)"></span><span style="width:2.67%;background:#d08a1e" title="another of C&#39;s alternatives: 125 (2.7 %)"></span><span style="width:3.55%;background:#c0392b" title="a reading C did not list: 166 (3.5 %)"></span><span style="width:0.23%;background:#8e44ad" title="removed / illegible read: 11 (0.2 %)"></span><span style="width:44.70%;background:#9aa5b1" title="still doubtful (same reading): 2093 (44.7 %)"></span><span style="width:9.95%;background:#c3cbd3" title="still doubtful (reading changed): 466 (10.0 %)"></span><span style="width:1.13%;background:#6c7a89" title="still illegible: 53 (1.1 %)"></span><span style="width:2.16%;background:#e9e3d5" title="not aligned: 101 (2.2 %)"></span>
</div></td>
<td class="n">42.1 %</td>
<td class="n">15.3 %</td>
<td class="n">55.8 %</td>
</tr>
<tr>
<td>GPT-6 Astra (ChatGPT Pro mode), one reader, piece of 16-24 pages (SP31-SP33; sent 19 Nov)</td>
<td>Codex web</td>
<td class="n">64</td>
<td class="n">1,352</td>
<td><div class="bar">
<span style="width:29.59%;background:#3b8f5a" title="C&#39;s first reading confirmed: 400 (29.6 %)"></span><span style="width:1.41%;background:#d08a1e" title="another of C&#39;s alternatives: 19 (1.4 %)"></span><span style="width:1.55%;background:#c0392b" title="a reading C did not list: 21 (1.6 %)"></span><span style="width:0.22%;background:#8e44ad" title="removed / illegible read: 3 (0.2 %)"></span><span style="width:57.99%;background:#9aa5b1" title="still doubtful (same reading): 784 (58.0 %)"></span><span style="width:8.28%;background:#c3cbd3" title="still doubtful (reading changed): 112 (8.3 %)"></span><span style="width:0.81%;background:#6c7a89" title="still illegible: 11 (0.8 %)"></span><span style="width:0.15%;background:#e9e3d5" title="not aligned: 2 (0.1 %)"></span>
</div></td>
<td class="n">32.8 %</td>
<td class="n">9.7 %</td>
<td class="n">67.1 %</td>
</tr>
<tr>
<td>GPT-6 Astra (ChatGPT Pro mode), three readers and a main reader (SP34)</td>
<td>Codex web</td>
<td class="n">8</td>
<td class="n">159</td>
<td><div class="bar">
<span style="width:30.19%;background:#3b8f5a" title="C&#39;s first reading confirmed: 48 (30.2 %)"></span><span style="width:3.14%;background:#c0392b" title="a reading C did not list: 5 (3.1 %)"></span><span style="width:0.63%;background:#8e44ad" title="removed / illegible read: 1 (0.6 %)"></span><span style="width:48.43%;background:#9aa5b1" title="still doubtful (same reading): 77 (48.4 %)"></span><span style="width:14.47%;background:#c3cbd3" title="still doubtful (reading changed): 23 (14.5 %)"></span><span style="width:3.14%;background:#e9e3d5" title="not aligned: 5 (3.1 %)"></span>
</div></td>
<td class="n">34.0 %</td>
<td class="n">11.1 %</td>
<td class="n">62.9 %</td>
</tr>
<tr>
<td>GPT-6 Astra (ChatGPT Pro mode), three readers and the reading workflow of 21:07 UTC (SP35)</td>
<td>Codex web</td>
<td class="n">8</td>
<td class="n">196</td>
<td><div class="bar">
<span style="width:31.63%;background:#3b8f5a" title="C&#39;s first reading confirmed: 62 (31.6 %)"></span><span style="width:1.53%;background:#d08a1e" title="another of C&#39;s alternatives: 3 (1.5 %)"></span><span style="width:2.55%;background:#c0392b" title="a reading C did not list: 5 (2.6 %)"></span><span style="width:0.51%;background:#8e44ad" title="removed / illegible read: 1 (0.5 %)"></span><span style="width:49.49%;background:#9aa5b1" title="still doubtful (same reading): 97 (49.5 %)"></span><span style="width:9.69%;background:#c3cbd3" title="still doubtful (reading changed): 19 (9.7 %)"></span><span style="width:0.51%;background:#6c7a89" title="still illegible: 1 (0.5 %)"></span><span style="width:4.08%;background:#e9e3d5" title="not aligned: 8 (4.1 %)"></span>
</div></td>
<td class="n">36.2 %</td>
<td class="n">12.7 %</td>
<td class="n">59.7 %</td>
</tr>
<tr>
<td>GPT-6 Astra (ChatGPT Pro mode), three fresh readers per page, deep zoom (SP36 on)</td>
<td>Codex web</td>
<td class="n">62</td>
<td class="n">791</td>
<td><div class="bar">
<span style="width:24.02%;background:#3b8f5a" title="C&#39;s first reading confirmed: 190 (24.0 %)"></span><span style="width:1.64%;background:#d08a1e" title="another of C&#39;s alternatives: 13 (1.6 %)"></span><span style="width:3.03%;background:#c0392b" title="a reading C did not list: 24 (3.0 %)"></span><span style="width:0.25%;background:#8e44ad" title="removed / illegible read: 2 (0.3 %)"></span><span style="width:41.97%;background:#9aa5b1" title="still doubtful (same reading): 332 (42.0 %)"></span><span style="width:15.80%;background:#c3cbd3" title="still doubtful (reading changed): 125 (15.8 %)"></span><span style="width:1.14%;background:#6c7a89" title="still illegible: 9 (1.1 %)"></span><span style="width:12.14%;background:#e9e3d5" title="not aligned: 96 (12.1 %)"></span>
</div></td>
<td class="n">29.0 %</td>
<td class="n">17.0 %</td>
<td class="n">58.9 %</td>
</tr>
<tr>
<td>GPT-6 Astra (ChatGPT Pro mode), doubt marks only, its own workflow (DM01)</td>
<td>Pro first reading</td>
<td class="n">67</td>
<td class="n">1,445</td>
<td><div class="bar">
<span style="width:39.38%;background:#3b8f5a" title="C&#39;s first reading confirmed: 569 (39.4 %)"></span><span style="width:2.84%;background:#d08a1e" title="another of C&#39;s alternatives: 41 (2.8 %)"></span><span style="width:3.32%;background:#c0392b" title="a reading C did not list: 48 (3.3 %)"></span><span style="width:0.28%;background:#8e44ad" title="removed / illegible read: 4 (0.3 %)"></span><span style="width:43.74%;background:#9aa5b1" title="still doubtful (same reading): 632 (43.7 %)"></span><span style="width:4.64%;background:#c3cbd3" title="still doubtful (reading changed): 67 (4.6 %)"></span><span style="width:5.81%;background:#6c7a89" title="still illegible: 84 (5.8 %)"></span>
</div></td>
<td class="n">45.8 %</td>
<td class="n">14.0 %</td>
<td class="n">54.2 %</td>
</tr>
<tr>
<td>GPT-6 Astra (ChatGPT Pro mode), live-text doubt marks only, DM01's workflow (DM02 on)</td>
<td>Claude second pass</td>
<td class="n">0</td>
<td class="n">0</td>
<td></td>
<td class="n">–</td>
<td class="n">–</td>
<td class="n">–</td>
</tr>
</tbody>
</table>

</div>

### By run

<div class="tw">

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th>Run</th>
<th>Newest return</th>
<th class="n">Pages</th>
<th class="n">Marks</th>
<th>Outcome</th>
<th class="n">Settled</th>
<th class="n">First reading wrong</th>
<th class="n">Confirmed</th>
<th class="n">Other alternative</th>
<th class="n">Unlisted reading</th>
<th class="n">Still doubtful</th>
</tr>
</thead>
<tbody>
<tr>
<td>CLAUDE13</td>
<td>13 Nov blocks</td>
<td class="n">808</td>
<td class="n">7,362</td>
<td><div class="bar">
<span style="width:6.33%;background:#3b8f5a" title="C&#39;s first reading confirmed: 466 (6.3 %)"></span><span style="width:1.89%;background:#d08a1e" title="another of C&#39;s alternatives: 139 (1.9 %)"></span><span style="width:1.86%;background:#c0392b" title="a reading C did not list: 137 (1.9 %)"></span><span style="width:0.35%;background:#8e44ad" title="removed / illegible read: 26 (0.4 %)"></span><span style="width:81.27%;background:#9aa5b1" title="still doubtful (same reading): 5983 (81.3 %)"></span><span style="width:6.56%;background:#c3cbd3" title="still doubtful (reading changed): 483 (6.6 %)"></span><span style="width:1.74%;background:#6c7a89" title="still illegible: 128 (1.7 %)"></span>
</div></td>
<td class="n">10.4 %</td>
<td class="n">39.3 %</td>
<td class="n">462</td>
<td class="n">139</td>
<td class="n">137</td>
<td class="n">6,594</td>
</tr>
<tr>
<td>DM01</td>
<td>checkpoint_10</td>
<td class="n">67</td>
<td class="n">1,445</td>
<td><div class="bar">
<span style="width:39.38%;background:#3b8f5a" title="C&#39;s first reading confirmed: 569 (39.4 %)"></span><span style="width:2.84%;background:#d08a1e" title="another of C&#39;s alternatives: 41 (2.8 %)"></span><span style="width:3.32%;background:#c0392b" title="a reading C did not list: 48 (3.3 %)"></span><span style="width:0.28%;background:#8e44ad" title="removed / illegible read: 4 (0.3 %)"></span><span style="width:43.74%;background:#9aa5b1" title="still doubtful (same reading): 632 (43.7 %)"></span><span style="width:4.64%;background:#c3cbd3" title="still doubtful (reading changed): 67 (4.6 %)"></span><span style="width:5.81%;background:#6c7a89" title="still illegible: 84 (5.8 %)"></span>
</div></td>
<td class="n">45.8 %</td>
<td class="n">14.0 %</td>
<td class="n">566</td>
<td class="n">41</td>
<td class="n">48</td>
<td class="n">783</td>
</tr>
<tr>
<td>SP02</td>
<td>checkpoint_23</td>
<td class="n">106</td>
<td class="n">906</td>
<td><div class="bar">
<span style="width:23.29%;background:#3b8f5a" title="C&#39;s first reading confirmed: 211 (23.3 %)"></span><span style="width:1.77%;background:#d08a1e" title="another of C&#39;s alternatives: 16 (1.8 %)"></span><span style="width:6.84%;background:#c0392b" title="a reading C did not list: 62 (6.8 %)"></span><span style="width:0.22%;background:#8e44ad" title="removed / illegible read: 2 (0.2 %)"></span><span style="width:38.19%;background:#9aa5b1" title="still doubtful (same reading): 346 (38.2 %)"></span><span style="width:21.96%;background:#c3cbd3" title="still doubtful (reading changed): 199 (22.0 %)"></span><span style="width:1.43%;background:#6c7a89" title="still illegible: 13 (1.4 %)"></span><span style="width:6.29%;background:#e9e3d5" title="not aligned: 57 (6.3 %)"></span>
</div></td>
<td class="n">32.1 %</td>
<td class="n">27.5 %</td>
<td class="n">209</td>
<td class="n">16</td>
<td class="n">62</td>
<td class="n">558</td>
</tr>
<tr>
<td>SP04</td>
<td>checkpoint_05</td>
<td class="n">63</td>
<td class="n">1,321</td>
<td><div class="bar">
<span style="width:44.21%;background:#3b8f5a" title="C&#39;s first reading confirmed: 584 (44.2 %)"></span><span style="width:3.33%;background:#d08a1e" title="another of C&#39;s alternatives: 44 (3.3 %)"></span><span style="width:1.29%;background:#c0392b" title="a reading C did not list: 17 (1.3 %)"></span><span style="width:0.08%;background:#8e44ad" title="removed / illegible read: 1 (0.1 %)"></span><span style="width:43.91%;background:#9aa5b1" title="still doubtful (same reading): 580 (43.9 %)"></span><span style="width:5.60%;background:#c3cbd3" title="still doubtful (reading changed): 74 (5.6 %)"></span><span style="width:1.06%;background:#6c7a89" title="still illegible: 14 (1.1 %)"></span><span style="width:0.53%;background:#e9e3d5" title="not aligned: 7 (0.5 %)"></span>
</div></td>
<td class="n">48.9 %</td>
<td class="n">9.6 %</td>
<td class="n">582</td>
<td class="n">44</td>
<td class="n">17</td>
<td class="n">668</td>
</tr>
<tr>
<td>SP12</td>
<td>checkpoint_11</td>
<td class="n">59</td>
<td class="n">996</td>
<td><div class="bar">
<span style="width:34.74%;background:#3b8f5a" title="C&#39;s first reading confirmed: 346 (34.7 %)"></span><span style="width:2.61%;background:#d08a1e" title="another of C&#39;s alternatives: 26 (2.6 %)"></span><span style="width:4.72%;background:#c0392b" title="a reading C did not list: 47 (4.7 %)"></span><span style="width:0.20%;background:#8e44ad" title="removed / illegible read: 2 (0.2 %)"></span><span style="width:45.38%;background:#9aa5b1" title="still doubtful (same reading): 452 (45.4 %)"></span><span style="width:8.73%;background:#c3cbd3" title="still doubtful (reading changed): 87 (8.7 %)"></span><span style="width:1.20%;background:#6c7a89" title="still illegible: 12 (1.2 %)"></span><span style="width:2.41%;background:#e9e3d5" title="not aligned: 24 (2.4 %)"></span>
</div></td>
<td class="n">42.3 %</td>
<td class="n">17.8 %</td>
<td class="n">344</td>
<td class="n">26</td>
<td class="n">47</td>
<td class="n">551</td>
</tr>
<tr>
<td>SP14</td>
<td>checkpoint_13</td>
<td class="n">100</td>
<td class="n">1,459</td>
<td><div class="bar">
<span style="width:36.05%;background:#3b8f5a" title="C&#39;s first reading confirmed: 526 (36.1 %)"></span><span style="width:2.67%;background:#d08a1e" title="another of C&#39;s alternatives: 39 (2.7 %)"></span><span style="width:2.74%;background:#c0392b" title="a reading C did not list: 40 (2.7 %)"></span><span style="width:0.41%;background:#8e44ad" title="removed / illegible read: 6 (0.4 %)"></span><span style="width:49.01%;background:#9aa5b1" title="still doubtful (same reading): 715 (49.0 %)"></span><span style="width:7.27%;background:#c3cbd3" title="still doubtful (reading changed): 106 (7.3 %)"></span><span style="width:0.96%;background:#6c7a89" title="still illegible: 14 (1.0 %)"></span><span style="width:0.89%;background:#e9e3d5" title="not aligned: 13 (0.9 %)"></span>
</div></td>
<td class="n">41.9 %</td>
<td class="n">13.9 %</td>
<td class="n">525</td>
<td class="n">39</td>
<td class="n">40</td>
<td class="n">835</td>
</tr>
<tr>
<td>SP31</td>
<td>final</td>
<td class="n">24</td>
<td class="n">525</td>
<td><div class="bar">
<span style="width:29.14%;background:#3b8f5a" title="C&#39;s first reading confirmed: 153 (29.1 %)"></span><span style="width:1.90%;background:#d08a1e" title="another of C&#39;s alternatives: 10 (1.9 %)"></span><span style="width:2.67%;background:#c0392b" title="a reading C did not list: 14 (2.7 %)"></span><span style="width:0.19%;background:#8e44ad" title="removed / illegible read: 1 (0.2 %)"></span><span style="width:53.52%;background:#9aa5b1" title="still doubtful (same reading): 281 (53.5 %)"></span><span style="width:10.86%;background:#c3cbd3" title="still doubtful (reading changed): 57 (10.9 %)"></span><span style="width:1.33%;background:#6c7a89" title="still illegible: 7 (1.3 %)"></span><span style="width:0.38%;background:#e9e3d5" title="not aligned: 2 (0.4 %)"></span>
</div></td>
<td class="n">33.9 %</td>
<td class="n">14.0 %</td>
<td class="n">152</td>
<td class="n">10</td>
<td class="n">14</td>
<td class="n">345</td>
</tr>
<tr>
<td>SP32</td>
<td>final</td>
<td class="n">16</td>
<td class="n">312</td>
<td><div class="bar">
<span style="width:37.18%;background:#3b8f5a" title="C&#39;s first reading confirmed: 116 (37.2 %)"></span><span style="width:0.96%;background:#d08a1e" title="another of C&#39;s alternatives: 3 (1.0 %)"></span><span style="width:2.24%;background:#c0392b" title="a reading C did not list: 7 (2.2 %)"></span><span style="width:52.56%;background:#9aa5b1" title="still doubtful (same reading): 164 (52.6 %)"></span><span style="width:6.73%;background:#c3cbd3" title="still doubtful (reading changed): 21 (6.7 %)"></span><span style="width:0.32%;background:#6c7a89" title="still illegible: 1 (0.3 %)"></span>
</div></td>
<td class="n">40.4 %</td>
<td class="n">7.9 %</td>
<td class="n">116</td>
<td class="n">3</td>
<td class="n">7</td>
<td class="n">186</td>
</tr>
<tr>
<td>SP33</td>
<td>final</td>
<td class="n">24</td>
<td class="n">515</td>
<td><div class="bar">
<span style="width:25.44%;background:#3b8f5a" title="C&#39;s first reading confirmed: 131 (25.4 %)"></span><span style="width:1.17%;background:#d08a1e" title="another of C&#39;s alternatives: 6 (1.2 %)"></span><span style="width:0.39%;background:#8e44ad" title="removed / illegible read: 2 (0.4 %)"></span><span style="width:65.83%;background:#9aa5b1" title="still doubtful (same reading): 339 (65.8 %)"></span><span style="width:6.60%;background:#c3cbd3" title="still doubtful (reading changed): 34 (6.6 %)"></span><span style="width:0.58%;background:#6c7a89" title="still illegible: 3 (0.6 %)"></span>
</div></td>
<td class="n">27.0 %</td>
<td class="n">5.8 %</td>
<td class="n">131</td>
<td class="n">6</td>
<td class="n">0</td>
<td class="n">376</td>
</tr>
<tr>
<td>SP34</td>
<td>checkpoint_03</td>
<td class="n">8</td>
<td class="n">159</td>
<td><div class="bar">
<span style="width:30.19%;background:#3b8f5a" title="C&#39;s first reading confirmed: 48 (30.2 %)"></span><span style="width:3.14%;background:#c0392b" title="a reading C did not list: 5 (3.1 %)"></span><span style="width:0.63%;background:#8e44ad" title="removed / illegible read: 1 (0.6 %)"></span><span style="width:48.43%;background:#9aa5b1" title="still doubtful (same reading): 77 (48.4 %)"></span><span style="width:14.47%;background:#c3cbd3" title="still doubtful (reading changed): 23 (14.5 %)"></span><span style="width:3.14%;background:#e9e3d5" title="not aligned: 5 (3.1 %)"></span>
</div></td>
<td class="n">34.0 %</td>
<td class="n">11.1 %</td>
<td class="n">48</td>
<td class="n">0</td>
<td class="n">5</td>
<td class="n">100</td>
</tr>
<tr>
<td>SP35</td>
<td>final</td>
<td class="n">8</td>
<td class="n">196</td>
<td><div class="bar">
<span style="width:31.63%;background:#3b8f5a" title="C&#39;s first reading confirmed: 62 (31.6 %)"></span><span style="width:1.53%;background:#d08a1e" title="another of C&#39;s alternatives: 3 (1.5 %)"></span><span style="width:2.55%;background:#c0392b" title="a reading C did not list: 5 (2.6 %)"></span><span style="width:0.51%;background:#8e44ad" title="removed / illegible read: 1 (0.5 %)"></span><span style="width:49.49%;background:#9aa5b1" title="still doubtful (same reading): 97 (49.5 %)"></span><span style="width:9.69%;background:#c3cbd3" title="still doubtful (reading changed): 19 (9.7 %)"></span><span style="width:0.51%;background:#6c7a89" title="still illegible: 1 (0.5 %)"></span><span style="width:4.08%;background:#e9e3d5" title="not aligned: 8 (4.1 %)"></span>
</div></td>
<td class="n">36.2 %</td>
<td class="n">12.7 %</td>
<td class="n">62</td>
<td class="n">3</td>
<td class="n">5</td>
<td class="n">117</td>
</tr>
<tr>
<td>SP36</td>
<td>checkpoint_01</td>
<td class="n">3</td>
<td class="n">38</td>
<td><div class="bar">
<span style="width:44.74%;background:#3b8f5a" title="C&#39;s first reading confirmed: 17 (44.7 %)"></span><span style="width:50.00%;background:#9aa5b1" title="still doubtful (same reading): 19 (50.0 %)"></span><span style="width:2.63%;background:#c3cbd3" title="still doubtful (reading changed): 1 (2.6 %)"></span><span style="width:2.63%;background:#e9e3d5" title="not aligned: 1 (2.6 %)"></span>
</div></td>
<td class="n">44.7 %</td>
<td class="n">0.0 %</td>
<td class="n">17</td>
<td class="n">0</td>
<td class="n">0</td>
<td class="n">20</td>
</tr>
<tr>
<td>SP37</td>
<td>checkpoint_01</td>
<td class="n">2</td>
<td class="n">37</td>
<td><div class="bar">
<span style="width:21.62%;background:#3b8f5a" title="C&#39;s first reading confirmed: 8 (21.6 %)"></span><span style="width:2.70%;background:#c0392b" title="a reading C did not list: 1 (2.7 %)"></span><span style="width:48.65%;background:#9aa5b1" title="still doubtful (same reading): 18 (48.6 %)"></span><span style="width:16.22%;background:#c3cbd3" title="still doubtful (reading changed): 6 (16.2 %)"></span><span style="width:5.41%;background:#6c7a89" title="still illegible: 2 (5.4 %)"></span><span style="width:5.41%;background:#e9e3d5" title="not aligned: 2 (5.4 %)"></span>
</div></td>
<td class="n">24.3 %</td>
<td class="n">11.1 %</td>
<td class="n">8</td>
<td class="n">0</td>
<td class="n">1</td>
<td class="n">26</td>
</tr>
<tr>
<td>SP38</td>
<td>checkpoint_08</td>
<td class="n">14</td>
<td class="n">219</td>
<td><div class="bar">
<span style="width:20.55%;background:#3b8f5a" title="C&#39;s first reading confirmed: 45 (20.5 %)"></span><span style="width:2.28%;background:#d08a1e" title="another of C&#39;s alternatives: 5 (2.3 %)"></span><span style="width:0.91%;background:#c0392b" title="a reading C did not list: 2 (0.9 %)"></span><span style="width:50.23%;background:#9aa5b1" title="still doubtful (same reading): 110 (50.2 %)"></span><span style="width:18.72%;background:#c3cbd3" title="still doubtful (reading changed): 41 (18.7 %)"></span><span style="width:0.46%;background:#6c7a89" title="still illegible: 1 (0.5 %)"></span><span style="width:6.85%;background:#e9e3d5" title="not aligned: 15 (6.8 %)"></span>
</div></td>
<td class="n">23.7 %</td>
<td class="n">13.5 %</td>
<td class="n">44</td>
<td class="n">5</td>
<td class="n">2</td>
<td class="n">152</td>
</tr>
<tr>
<td>SP39</td>
<td>checkpoint_01</td>
<td class="n">2</td>
<td class="n">42</td>
<td><div class="bar">
<span style="width:38.10%;background:#3b8f5a" title="C&#39;s first reading confirmed: 16 (38.1 %)"></span><span style="width:2.38%;background:#c0392b" title="a reading C did not list: 1 (2.4 %)"></span><span style="width:42.86%;background:#9aa5b1" title="still doubtful (same reading): 18 (42.9 %)"></span><span style="width:16.67%;background:#c3cbd3" title="still doubtful (reading changed): 7 (16.7 %)"></span>
</div></td>
<td class="n">40.5 %</td>
<td class="n">5.9 %</td>
<td class="n">16</td>
<td class="n">0</td>
<td class="n">1</td>
<td class="n">25</td>
</tr>
<tr>
<td>SP40</td>
<td>checkpoint_01</td>
<td class="n">2</td>
<td class="n">28</td>
<td><div class="bar">
<span style="width:35.71%;background:#3b8f5a" title="C&#39;s first reading confirmed: 10 (35.7 %)"></span><span style="width:3.57%;background:#c0392b" title="a reading C did not list: 1 (3.6 %)"></span><span style="width:3.57%;background:#8e44ad" title="removed / illegible read: 1 (3.6 %)"></span><span style="width:53.57%;background:#9aa5b1" title="still doubtful (same reading): 15 (53.6 %)"></span><span style="width:3.57%;background:#6c7a89" title="still illegible: 1 (3.6 %)"></span>
</div></td>
<td class="n">42.9 %</td>
<td class="n">16.7 %</td>
<td class="n">10</td>
<td class="n">0</td>
<td class="n">1</td>
<td class="n">16</td>
</tr>
<tr>
<td>SP41</td>
<td>checkpoint_01</td>
<td class="n">2</td>
<td class="n">71</td>
<td><div class="bar">
<span style="width:42.25%;background:#3b8f5a" title="C&#39;s first reading confirmed: 30 (42.3 %)"></span><span style="width:1.41%;background:#d08a1e" title="another of C&#39;s alternatives: 1 (1.4 %)"></span><span style="width:4.23%;background:#c0392b" title="a reading C did not list: 3 (4.2 %)"></span><span style="width:40.85%;background:#9aa5b1" title="still doubtful (same reading): 29 (40.8 %)"></span><span style="width:9.86%;background:#c3cbd3" title="still doubtful (reading changed): 7 (9.9 %)"></span><span style="width:1.41%;background:#e9e3d5" title="not aligned: 1 (1.4 %)"></span>
</div></td>
<td class="n">47.9 %</td>
<td class="n">11.8 %</td>
<td class="n">30</td>
<td class="n">1</td>
<td class="n">3</td>
<td class="n">36</td>
</tr>
<tr>
<td>SP44</td>
<td>checkpoint_01</td>
<td class="n">2</td>
<td class="n">18</td>
<td><div class="bar">
<span style="width:44.44%;background:#9aa5b1" title="still doubtful (same reading): 8 (44.4 %)"></span><span style="width:50.00%;background:#c3cbd3" title="still doubtful (reading changed): 9 (50.0 %)"></span><span style="width:5.56%;background:#e9e3d5" title="not aligned: 1 (5.6 %)"></span>
</div></td>
<td class="n">0.0 %</td>
<td class="n">–</td>
<td class="n">0</td>
<td class="n">0</td>
<td class="n">0</td>
<td class="n">17</td>
</tr>
<tr>
<td>SP45</td>
<td>checkpoint_01</td>
<td class="n">6</td>
<td class="n">23</td>
<td><div class="bar">
<span style="width:39.13%;background:#3b8f5a" title="C&#39;s first reading confirmed: 9 (39.1 %)"></span><span style="width:4.35%;background:#d08a1e" title="another of C&#39;s alternatives: 1 (4.3 %)"></span><span style="width:34.78%;background:#9aa5b1" title="still doubtful (same reading): 8 (34.8 %)"></span><span style="width:21.74%;background:#c3cbd3" title="still doubtful (reading changed): 5 (21.7 %)"></span>
</div></td>
<td class="n">43.5 %</td>
<td class="n">10.0 %</td>
<td class="n">9</td>
<td class="n">1</td>
<td class="n">0</td>
<td class="n">13</td>
</tr>
<tr>
<td>SP46</td>
<td>checkpoint_01</td>
<td class="n">2</td>
<td class="n">22</td>
<td><div class="bar">
<span style="width:13.64%;background:#3b8f5a" title="C&#39;s first reading confirmed: 3 (13.6 %)"></span><span style="width:9.09%;background:#c0392b" title="a reading C did not list: 2 (9.1 %)"></span><span style="width:45.45%;background:#9aa5b1" title="still doubtful (same reading): 10 (45.5 %)"></span><span style="width:22.73%;background:#c3cbd3" title="still doubtful (reading changed): 5 (22.7 %)"></span><span style="width:4.55%;background:#6c7a89" title="still illegible: 1 (4.5 %)"></span><span style="width:4.55%;background:#e9e3d5" title="not aligned: 1 (4.5 %)"></span>
</div></td>
<td class="n">22.7 %</td>
<td class="n">40.0 %</td>
<td class="n">3</td>
<td class="n">0</td>
<td class="n">2</td>
<td class="n">16</td>
</tr>
<tr>
<td>SP47</td>
<td>checkpoint_01</td>
<td class="n">2</td>
<td class="n">32</td>
<td><div class="bar">
<span style="width:25.00%;background:#3b8f5a" title="C&#39;s first reading confirmed: 8 (25.0 %)"></span><span style="width:3.12%;background:#c0392b" title="a reading C did not list: 1 (3.1 %)"></span><span style="width:62.50%;background:#9aa5b1" title="still doubtful (same reading): 20 (62.5 %)"></span><span style="width:6.25%;background:#c3cbd3" title="still doubtful (reading changed): 2 (6.2 %)"></span><span style="width:3.12%;background:#6c7a89" title="still illegible: 1 (3.1 %)"></span>
</div></td>
<td class="n">28.1 %</td>
<td class="n">11.1 %</td>
<td class="n">8</td>
<td class="n">0</td>
<td class="n">1</td>
<td class="n">23</td>
</tr>
<tr>
<td>SP48</td>
<td>checkpoint_01</td>
<td class="n">1</td>
<td class="n">9</td>
<td><div class="bar">
<span style="width:22.22%;background:#3b8f5a" title="C&#39;s first reading confirmed: 2 (22.2 %)"></span><span style="width:11.11%;background:#d08a1e" title="another of C&#39;s alternatives: 1 (11.1 %)"></span><span style="width:11.11%;background:#c0392b" title="a reading C did not list: 1 (11.1 %)"></span><span style="width:33.33%;background:#9aa5b1" title="still doubtful (same reading): 3 (33.3 %)"></span><span style="width:11.11%;background:#c3cbd3" title="still doubtful (reading changed): 1 (11.1 %)"></span><span style="width:11.11%;background:#e9e3d5" title="not aligned: 1 (11.1 %)"></span>
</div></td>
<td class="n">44.4 %</td>
<td class="n">50.0 %</td>
<td class="n">2</td>
<td class="n">1</td>
<td class="n">1</td>
<td class="n">4</td>
</tr>
<tr>
<td>SP49</td>
<td>checkpoint_01</td>
<td class="n">6</td>
<td class="n">19</td>
<td><div class="bar">
<span style="width:63.16%;background:#3b8f5a" title="C&#39;s first reading confirmed: 12 (63.2 %)"></span><span style="width:36.84%;background:#9aa5b1" title="still doubtful (same reading): 7 (36.8 %)"></span>
</div></td>
<td class="n">63.2 %</td>
<td class="n">0.0 %</td>
<td class="n">12</td>
<td class="n">0</td>
<td class="n">0</td>
<td class="n">7</td>
</tr>
<tr>
<td>SP50</td>
<td>checkpoint_01</td>
<td class="n">3</td>
<td class="n">29</td>
<td><div class="bar">
<span style="width:27.59%;background:#3b8f5a" title="C&#39;s first reading confirmed: 8 (27.6 %)"></span><span style="width:62.07%;background:#9aa5b1" title="still doubtful (same reading): 18 (62.1 %)"></span><span style="width:10.34%;background:#c3cbd3" title="still doubtful (reading changed): 3 (10.3 %)"></span>
</div></td>
<td class="n">27.6 %</td>
<td class="n">0.0 %</td>
<td class="n">8</td>
<td class="n">0</td>
<td class="n">0</td>
<td class="n">21</td>
</tr>
<tr>
<td>SP57</td>
<td>checkpoint_09</td>
<td class="n">15</td>
<td class="n">204</td>
<td><div class="bar">
<span style="width:10.78%;background:#3b8f5a" title="C&#39;s first reading confirmed: 22 (10.8 %)"></span><span style="width:2.45%;background:#d08a1e" title="another of C&#39;s alternatives: 5 (2.5 %)"></span><span style="width:5.88%;background:#c0392b" title="a reading C did not list: 12 (5.9 %)"></span><span style="width:0.49%;background:#8e44ad" title="removed / illegible read: 1 (0.5 %)"></span><span style="width:24.02%;background:#9aa5b1" title="still doubtful (same reading): 49 (24.0 %)"></span><span style="width:18.63%;background:#c3cbd3" title="still doubtful (reading changed): 38 (18.6 %)"></span><span style="width:1.47%;background:#6c7a89" title="still illegible: 3 (1.5 %)"></span><span style="width:36.27%;background:#e9e3d5" title="not aligned: 74 (36.3 %)"></span>
</div></td>
<td class="n">19.6 %</td>
<td class="n">45.0 %</td>
<td class="n">22</td>
<td class="n">5</td>
<td class="n">12</td>
<td class="n">90</td>
</tr>
</tbody>
</table>

</div>

### By kind of mark

<div class="tw">

| Second pass | Kind of mark | Marks | Settled | First reading wrong, where settled |
|----|----|----|----|----|
| Claude Opus 5.5 at effort max, block second pass (13 Nov) | choice | 2,412 | 22.2 % | 40.7 % |
|  | single | 4,822 | 4.8 % | 36.1 % |
|  | illegible | 128 | 0.0 % | – |
| GPT-6 Astra (ChatGPT Pro mode), one reader, large piece (SP02, SP04, SP12, SP14; sent 14-17 Nov) | choice | 2,937 | 41.8 % | 20.9 % |
|  | single | 1,685 | 43.9 % | 6.1 % |
|  | illegible | 60 | 0.0 % | – |
| GPT-6 Astra (ChatGPT Pro mode), one reader, piece of 16-24 pages (SP31-SP33; sent 19 Nov) | choice | 726 | 33.5 % | 13.2 % |
|  | single | 614 | 32.6 % | 5.5 % |
|  | illegible | 12 | 0.0 % | – |
| GPT-6 Astra (ChatGPT Pro mode), three readers and a main reader (SP34) | choice | 75 | 20.0 % | 6.7 % |
|  | single | 84 | 46.4 % | 12.8 % |
| GPT-6 Astra (ChatGPT Pro mode), three readers and the reading workflow of 21:07 UTC (SP35) | choice | 108 | 41.7 % | 15.6 % |
|  | single | 87 | 29.9 % | 7.7 % |
|  | illegible | 1 | 0.0 % | – |
| GPT-6 Astra (ChatGPT Pro mode), three fresh readers per page, deep zoom (SP36 on) | choice | 492 | 28.5 % | 20.7 % |
|  | single | 288 | 30.9 % | 11.2 % |
|  | illegible | 11 | 0.0 % | – |
| GPT-6 Astra (ChatGPT Pro mode), doubt marks only, its own workflow (DM01) | choice | 292 | 63.0 % | 25.5 % |
|  | single | 1,065 | 44.6 % | 9.1 % |
|  | illegible | 88 | 3.4 % | 100.0 % |

</div>

### Struck text, mathematics, margins

<div class="tw">

| Second pass | Context | Marks there | Settled there | Marks elsewhere | Settled elsewhere |
|----|----|----|----|----|----|
| Claude Opus 5.5 at effort max, block second pass (13 Nov) | in struck-out text | 2,717 | 2.5 % | 4,645 | 15.1 % |
|  | in mathematics | 3,808 | 12.2 % | 3,554 | 8.5 % |
|  | in a margin note | 1,132 | 6.5 % | 6,230 | 11.1 % |
| GPT-6 Astra (ChatGPT Pro mode), one reader, large piece (SP02, SP04, SP12, SP14; sent 14-17 Nov) | in struck-out text | 1,950 | 30.1 % | 2,732 | 50.6 % |
|  | in mathematics | 1,644 | 39.1 % | 3,038 | 43.6 % |
|  | in a margin note | 523 | 46.1 % | 4,159 | 41.5 % |
| GPT-6 Astra (ChatGPT Pro mode), one reader, piece of 16-24 pages (SP31-SP33; sent 19 Nov) | in struck-out text | 597 | 16.2 % | 755 | 45.8 % |
|  | in mathematics | 524 | 26.1 % | 828 | 37.0 % |
|  | in a margin note | 197 | 26.4 % | 1,155 | 33.9 % |
| GPT-6 Astra (ChatGPT Pro mode), three readers and a main reader (SP34) | in struck-out text | 71 | 22.5 % | 88 | 43.2 % |
|  | in mathematics | 54 | 29.6 % | 105 | 36.2 % |
|  | in a margin note | 25 | 36.0 % | 134 | 33.6 % |
| GPT-6 Astra (ChatGPT Pro mode), three readers and the reading workflow of 21:07 UTC (SP35) | in struck-out text | 83 | 21.7 % | 113 | 46.9 % |
|  | in mathematics | 84 | 32.1 % | 112 | 39.3 % |
|  | in a margin note | 37 | 32.4 % | 159 | 37.1 % |
| GPT-6 Astra (ChatGPT Pro mode), three fresh readers per page, deep zoom (SP36 on) | in struck-out text | 305 | 15.4 % | 486 | 37.4 % |
|  | in mathematics | 294 | 28.6 % | 497 | 29.2 % |
|  | in a margin note | 109 | 36.7 % | 682 | 27.7 % |
| GPT-6 Astra (ChatGPT Pro mode), doubt marks only, its own workflow (DM01) | in struck-out text | 857 | 30.9 % | 588 | 67.5 % |
|  | in mathematics | 418 | 59.1 % | 1,027 | 40.4 % |
|  | in a margin note | 165 | 49.1 % | 1,280 | 45.4 % |

</div>

### Hua's text at the mark, against what the pass did

Hua's text is an independent reading of the same page. Where it agrees with C's first reading, the Pro passes confirmed C at 90.4 % of the settled marks. Where it has C's other alternative, they still kept C's first reading at 69.7 %, while the Claude pass of 13 Nov chose Hua's alternative at 69.6 % of the few such marks it settled. Either C's first reading is mostly right there and the Claude pass changed readings it should not have, or the Pro passes lean towards witness C. The two populations also differ (different first readers, different cotes). Only the scan at a sample of these places can say which.

#### Pro second passes and DM01

<div class="tw">

| What Hua has at the mark | Marks | Settled | of these: C's first | C's other alternative | a reading C did not list | the pass's reading = Hua's |
|----|----|----|----|----|----|----|
| Hua = C's first reading | 1,445 | 55.0 % | 90.4 % | 4.8 % | 4.8 % | 66.9 % |
| Hua = C up to accents/case | 44 | 52.3 % | 73.9 % | 17.4 % | 8.7 % | 69.6 % |
| Hua = C's other alternative | 547 | 50.1 % | 69.7 % | 18.2 % | 12.0 % | 23.7 % |
| Hua has a third reading | 2,232 | 33.3 % | 82.7 % | 3.8 % | 13.6 % | 1.7 % |
| Hua also uncertain here | 2,158 | 37.7 % | 88.5 % | 5.8 % | 5.8 % | 3.6 % |
| Hua has nothing here | 609 | 34.3 % | 87.6 % | 2.9 % | 9.6 % | 0.0 % |
| Hua has a reading | 18 | 0.0 % | – | – | – | – |
| Hua not aligned here | 1,204 | 37.0 % | 87.2 % | 5.6 % | 7.2 % | 1.8 % |
| Hua's page does not match (ratio \< 0.25) | 154 | 21.4 % | 81.8 % | 3.0 % | 15.2 % | 0.0 % |
| no Hua text for the page | 214 | 42.5 % | 83.5 % | 2.2 % | 14.3 % | 0.0 % |

</div>

#### Claude block pass of 13 Nov

<div class="tw">

| What Hua has at the mark | Marks | Settled | of these: C's first | C's other alternative | a reading C did not list | the pass's reading = Hua's |
|----|----|----|----|----|----|----|
| Hua = C's first reading | 945 | 21.0 % | 83.3 % | 13.6 % | 3.0 % | 65.7 % |
| Hua = C up to accents/case | 16 | 6.2 % | 100.0 % | 0.0 % | 0.0 % | 100.0 % |
| Hua = C's other alternative | 292 | 23.6 % | 30.4 % | 69.6 % | 0.0 % | 59.4 % |
| Hua has a third reading | 2,001 | 9.6 % | 58.5 % | 13.0 % | 28.5 % | 9.3 % |
| Hua also uncertain here | 1,622 | 4.3 % | 65.7 % | 10.0 % | 24.3 % | 7.1 % |
| Hua has nothing here | 491 | 5.3 % | 50.0 % | 3.8 % | 46.2 % | 0.0 % |
| Hua has a reading | 1 | 0.0 % | – | – | – | – |
| Hua not aligned here | 1,299 | 8.2 % | 39.6 % | 2.8 % | 57.5 % | 3.8 % |
| Hua's page does not match (ratio \< 0.25) | 590 | 14.1 % | 54.2 % | 31.3 % | 14.5 % | 0.0 % |
| no Hua text for the page | 105 | 21.0 % | 90.9 % | 9.1 % | 0.0 % | 0.0 % |

</div>

The last column compares the pass's reading at the mark with Hua's, word for word, ignoring accents and case: Hua's conventions differ from ours in places, so it undercounts agreement.

### Every correction the Pro passes logged, and what pointed at it

This uses the passes' own changes logs (`STATE/second_pass_yield.py`), not the alignment: 7,974 corrections of C, 43.1 % at one of C's doubt marks, 39.6 % where Hua's text differs from C, and 17.3 % that only a full correcting pass found.

<div class="tw">

| Run | Places ruled in its changes log | C corrected | of which high confidence | at C's own doubt mark | where Hua differs from C | neither (only a full pass) |
|----|----|----|----|----|----|----|
| SP02 | 3,507 | 1,830 | 780 | 473 | 664 | 693 |
| SP04 | 2,522 | 1,198 | 183 | 495 | 622 | 81 |
| SP12 | 2,275 | 1,858 | 1,237 | 620 | 1,006 | 232 |
| SP14 | 2,591 | 1,140 | 283 | 803 | 184 | 153 |
| SP31 | 283 | 154 | 69 | 50 | 81 | 23 |
| SP32 | 517 | 215 | 62 | 159 | 52 | 4 |
| SP33 | 614 | 320 | 68 | 253 | 62 | 5 |
| SP34 | 344 | 124 | 47 | 50 | 57 | 17 |
| SP35 | 444 | 228 | 60 | 126 | 80 | 22 |
| SP36 | 76 | 12 | 7 | 6 | 2 | 4 |
| SP37 | 59 | 32 | 20 | 12 | 19 | 1 |
| SP38 | 581 | 323 | 77 | 166 | 108 | 49 |
| SP39 | 86 | 32 | 13 | 18 | 5 | 9 |
| SP40 | 69 | 17 | 5 | 12 | 4 | 1 |
| SP41 | 97 | 21 | 7 | 14 | 7 | 0 |
| SP44 | 56 | 28 | 2 | 11 | 8 | 9 |
| SP45 | 39 | 25 | 10 | 14 | 11 | 0 |
| SP46 | 65 | 19 | 3 | 12 | 4 | 3 |
| SP47 | 77 | 7 | 3 | 4 | 2 | 1 |
| SP48 | 27 | 27 | 21 | 0 | 26 | 1 |
| SP49 | 65 | 5 | 3 | 5 | 0 | 0 |
| SP50 | 62 | 8 | 1 | 4 | 2 | 2 |
| SP57 | 643 | 351 | 208 | 132 | 151 | 68 |
| All | 15,099 | 7,974 | 3,169 | 3,439 | 3,157 | 1,378 |

</div>

### How much each pass rewrote

<div class="tw">

| Second pass | Pages | Words a page (C) | C's marks a page | Marks a page after the pass | New marks a page | Changes outside the marks a page | per 100 words |
|----|----|----|----|----|----|----|----|
| Claude Opus 5.5 at effort max, block second pass (13 Nov) | 808 | 228 | 9.1 | 8.9 | 0.7 | 0.7 | 0.29 |
| GPT-6 Astra (ChatGPT Pro mode), one reader, large piece (SP02, SP04, SP12, SP14; sent 14-17 Nov) | 328 | 277 | 14.3 | 9.6 | 1.5 | 2.7 | 0.99 |
| GPT-6 Astra (ChatGPT Pro mode), one reader, piece of 16-24 pages (SP31-SP33; sent 19 Nov) | 64 | 216 | 21.1 | 14.4 | 0.7 | 1.7 | 0.80 |
| GPT-6 Astra (ChatGPT Pro mode), three readers and a main reader (SP34) | 8 | 274 | 19.9 | 13.1 | 1.4 | 0.6 | 0.23 |
| GPT-6 Astra (ChatGPT Pro mode), three readers and the reading workflow of 21:07 UTC (SP35) | 8 | 373 | 24.5 | 15.9 | 1.6 | 3.9 | 1.04 |
| GPT-6 Astra (ChatGPT Pro mode), three fresh readers per page, deep zoom (SP36 on) | 62 | 263 | 12.8 | 11.2 | 1.6 | 3.1 | 1.19 |
| GPT-6 Astra (ChatGPT Pro mode), doubt marks only, its own workflow (DM01) | 67 | 282 | 21.6 | 11.9 | 0.1 | 0.1 | 0.04 |

</div>

Changes outside the marks: blocks of words that differ between C and the final text where neither has a doubt mark, drawings left out, and leaving out blocks that differ only in accents, case or punctuation. They include notation changes as well as misreadings: they measure how much a pass rewrote, not how many errors it caught.

</div>

<div id="workflows" class="section">

## 3. The Pro workflows compared

Every Pro second pass so far worked on pages first read in Codex web, so witness C comes from one route throughout. The pieces still differ in cote, handwriting and density, and the newer designs have few pages, so differences between runs are not effects of the design alone. The fairest comparisons are on the same cote:

### Cote 156-5: one reader (SP33) against three readers (SP34)

<div class="tw">

| Run | Pages | C's marks | Settled | First reading wrong, where settled | Readings changed at marks, a page |
|----|----|----|----|----|----|
| SP33 | 24 | 515 | 27.0 % | 5.8 % | 0.3 |
| SP34 | 8 | 159 | 34.0 % | 11.1 % | 0.8 |

</div>

### Cote 156-3: two one-reader pieces (SP31, SP32)

<div class="tw">

| Run | Pages | C's marks | Settled | First reading wrong, where settled | Readings changed at marks, a page |
|----|----|----|----|----|----|
| SP31 | 24 | 525 | 33.9 % | 14.0 % | 1.0 |
| SP32 | 16 | 312 | 40.4 % | 7.9 % | 0.6 |

</div>

### Cote 71: the deep-zoom pieces with fresh readers (SP36, SP37)

<div class="tw">

| Run | Pages | C's marks | Settled | First reading wrong, where settled | Readings changed at marks, a page |
|----|----|----|----|----|----|
| SP36 | 3 | 38 | 44.7 % | 0.0 % | 0.0 |
| SP37 | 2 | 37 | 24.3 % | 11.1 % | 0.5 |

</div>

### All runs

<div class="tw">

| Run | Design | Cotes | Pages | Pages an hour | C's marks a page | Marks settled | C's reading changed at a mark, a page | Other changes a page | Crops a page | Median zoom | Crops at 4x or more | Crop record |
|----|----|----|----|----|----|----|----|----|----|----|----|----|
| DM01 | doubt marks only, its own workflow (DM01) | 1 | 67 | 9.1 | 21.6 | 45.8 % | 1.4 | 0.1 | 69.7 | 4.0 | 57.1 % | log |
| SP02 | one reader, large piece (SP02, SP04, SP12, SP14; sent 14-17 Nov) | 10, 12 | 106 | 6.3 | 8.5 | 32.1 % | 0.8 | 3.8 | 66.9 | 14.0 | 92.8 % | log |
| SP04 | one reader, large piece (SP02, SP04, SP12, SP14; sent 14-17 Nov) | 156-4, 156-6 | 63 | 12.5 | 21.0 | 48.9 % | 1.0 | 0.9 | 10.5 | 3.0 | 38.7 % | log |
| SP12 | one reader, large piece (SP02, SP04, SP12, SP14; sent 14-17 Nov) | 45, 46, 53, 57, 63 | 59 | 10.2 | 16.9 | 42.3 % | 1.3 | 4.1 | 0.0 | – | – | none |
| SP14 | one reader, large piece (SP02, SP04, SP12, SP14; sent 14-17 Nov) | 123, 13, 15, 162-1, 162-6, 26, 35, 48, 66, 97 | 100 | 17.7 | 14.6 | 41.9 % | 0.8 | 1.9 | 58.5 | 6.0 | 75.5 % | manifest |
| SP31 | one reader, piece of 16-24 pages (SP31-SP33; sent 19 Nov) | 156-3 | 24 | 22.9 | 21.9 | 33.9 % | 1.0 | 1.0 | 6.4 | – | – | image |
| SP32 | one reader, piece of 16-24 pages (SP31-SP33; sent 19 Nov) | 156-3 | 16 | 20.2 | 19.5 | 40.4 % | 0.6 | 0.8 | 6.1 | – | – | image |
| SP33 | one reader, piece of 16-24 pages (SP31-SP33; sent 19 Nov) | 156-5 | 24 | 28.8 | 21.5 | 27.0 % | 0.3 | 3.0 | 6.5 | 2.0 | 10.8 % | log |
| SP34 | three readers and a main reader (SP34) | 156-5 | 8 | 3.9 | 19.9 | 34.0 % | 0.8 | 0.6 | 89.2 | 3.0 | 48.4 % | log |
| SP35 | three readers and the reading workflow of 21:07 UTC (SP35) | 156-7 | 8 | 3.7 | 24.5 | 36.2 % | 1.1 | 3.9 | 59.5 | 3.0 | 0.0 % | log |
| SP36 | three fresh readers per page, deep zoom (SP36 on) | 71 | 3 | 4.9 | 12.7 | 44.7 % | 0.0 | 2.0 | 30.3 | 10.1 | 93.8 % | log |
| SP37 | three fresh readers per page, deep zoom (SP36 on) | 71 | 2 | 3.5 | 18.5 | 24.3 % | 0.5 | 4.5 | 98.0 | 9.4 | 76.9 % | log |
| SP38 | three fresh readers per page, deep zoom (SP36 on) | 75 | 14 | 2.4 | 15.6 | 23.7 % | 0.5 | 5.6 | 85.2 | 5.4 | 80.5 % | log |
| SP39 | three fresh readers per page, deep zoom (SP36 on) | 75 | 2 | 3.6 | 21.0 | 40.5 % | 0.5 | 2.5 | 7.0 | – | – | log |
| SP40 | three fresh readers per page, deep zoom (SP36 on) | 81 | 2 | 3.0 | 14.0 | 42.9 % | 1.0 | 0.0 | 17.5 | – | – | log |
| SP41 | three fresh readers per page, deep zoom (SP36 on) | 81 | 2 | 2.7 | 35.5 | 47.9 % | 2.0 | 0.0 | 110.0 | 11.6 | 83.3 % | log |
| SP44 | three fresh readers per page, deep zoom (SP36 on) | 36 | 2 | 3.3 | 9.0 | 0.0 % | 0.0 | 5.5 | 41.0 | 7.1 | 92.7 % | log |
| SP45 | three fresh readers per page, deep zoom (SP36 on) | 37 | 6 | 9.4 | 3.8 | 43.5 % | 0.2 | 0.7 | 22.7 | 11.1 | 83.3 % | log |
| SP46 | three fresh readers per page, deep zoom (SP36 on) | 37 | 2 | 2.7 | 11.0 | 22.7 % | 1.0 | 4.5 | 82.0 | – | – | log |
| SP47 | three fresh readers per page, deep zoom (SP36 on) | 103 | 2 | 3.6 | 16.0 | 28.1 % | 0.5 | 0.5 | 61.0 | 3.0 | 50.0 % | log |
| SP48 | three fresh readers per page, deep zoom (SP36 on) | 104 | 1 | 2.6 | 9.0 | 44.4 % | 2.0 | 0.0 | 34.0 | 9.4 | 100.0 % | log |
| SP49 | three fresh readers per page, deep zoom (SP36 on) | 109 | 6 | 9.2 | 3.2 | 63.2 % | 0.0 | 0.0 | 63.7 | 7.3 | 83.9 % | log |
| SP50 | three fresh readers per page, deep zoom (SP36 on) | 134-1, 134-2 | 3 | 4.6 | 9.7 | 27.6 % | 0.0 | 0.0 | 41.0 | 7.8 | 94.0 % | log |
| SP57 | three fresh readers per page, deep zoom (SP36 on) | 123, 162-1, 162-6, 97 | 15 | 2.2 | 13.6 | 19.6 % | 1.2 | 4.7 | 124.0 | 7.3 | 88.4 % | log |

</div>

Pages an hour: from the run's progress.log, its first line to its last page done. Zoom: output pixels over source pixels, from the crop logs (SP31 and SP32 logged only their crop images, so their zoom is unknown; SP12 kept no crop record).

</div>

<div id="zoom" class="section">

## 4. Deep zoom: what the data says

The guess to test: fewer but deeper zooms catch more. Two kinds of evidence exist so far, and neither is a controlled test.

**Between runs.** The median zoom of a run against the share of C's marks it settled, over 18 runs with zoom data: Spearman +0.15 (SP33 2.0x: 27 %, SP47 3.0x: 28 %, SP34 3.0x: 34 %, SP35 3.0x: 36 %, SP04 3.0x: 49 %, DM01 4.0x: 46 %, SP38 5.4x: 24 %, SP14 6.0x: 42 %, SP44 7.1x: 0 %, SP49 7.3x: 63 %, SP57 7.3x: 20 %, SP50 7.8x: 28 %, SP37 9.4x: 24 %, SP48 9.4x: 44 %, SP36 10.1x: 45 %, SP45 11.1x: 43 %, SP41 11.6x: 48 %, SP02 14.0x: 32 %). The runs differ in cote, design and size, so this cannot isolate the zoom.

**Within runs, page by page.** Pages that got deeper or more crops are the harder pages, so a correlation here runs both ways: a hard page draws deep crops and also keeps more doubts.

<div class="tw">

| Run | Pages with crop data and 3+ marks | Median zoom | Median crops a page | Zoom vs share settled | Crops vs share settled | Zoom vs readings changed |
|----|----|----|----|----|----|----|
| DM01 | 67 | 4.0 | 66 | -0.39 | +0.05 | +0.09 |
| SP02 | 92 | 9.0 | 52 | +0.17 | +0.19 | +0.35 |
| SP04 | 56 | 2.5 | 11 | +0.20 | -0.11 | +0.10 |
| SP14 | 84 | 5.0 | 49 | +0.08 | +0.13 | -0.13 |
| SP33 | 24 | 2.0 | 6 | -0.11 | -0.30 | +0.10 |
| SP34 | 8 | 3.0 | 74 | -0.01 | +0.36 | +0.79 |
| SP35 | 8 | 3.0 | 56 | – | -0.52 | – |
| SP38 | 12 | 6.5 | 98 | -0.25 | -0.26 | -0.28 |
| SP57 | 13 | 7.0 | 94 | +0.02 | -0.07 | -0.26 |

</div>

Spearman rank correlations between pages of the same run. +1: always rises together; 0: no relation; -1: opposite.

**DM01, mark by mark.** The crop box each decision cites is 196 px wide (median) for the 678 decided marks and 255 px for the 758 undecided ones. DM01 also reported that grouping neighbouring marks into one shared band crop, with a tight detail crop only for a feature still open, cut its crops per mark from 1.75 (scan 7) to 0.97 (scan 8) (section 5; its pages differ, so it is not a controlled measure).

**What would settle it.** The same pages read twice by the same design, once with crops capped at about 2-3x and once with tight crops at 8-10x, scored mark by mark against each other and against the scan at the places they disagree. Nothing like this has run yet; SP36 and SP37 (deep zoom, fresh readers) are the first returns with the deep setting, on cote 71, which no other design has read.

</div>

<div id="dm01" class="section">

## 5. DM01, the doubt-marks-only run

DM01 is the run we proposed on 19 Nov at 21:58 UTC: one long Pro run on the doubt marks of one cote only, with full freedom to design its own workflow, record it, change it as it goes and measure each change. It covers cote 1 (2,684 marks on its pages). Its newest checkpoint (checkpoint 10, 20 Nov 05:37 UTC) holds 67 pages, scans 3-72, done between 22:06 and 05:30 UTC.

### Its decisions

<div class="tw">

| Decision    | High | Medium | Low | All |
|-------------|------|--------|-----|-----|
| first       | 201  | 383    | 0   | 584 |
| alternative | 27   | 15     | 0   | 42  |
| other       | 19   | 37     | 0   | 56  |
| undecided   | 0    | 0      | 765 | 765 |

</div>

Where it decided, C's first reading held at 584 marks and was wrong at 98: 42 times another of C's alternatives, 56 times a reading C had not listed:

<div class="tw">

| Mark | Scan | C has | Decision | DM01 reads | Confidence | What the ink shows (its words, shortened) |
|----|----|----|----|----|----|----|
| M0035 | 5 | `\unsure{\wedge}` | other | `\uparrow` | high | Above C, the pointed cap has two outer sloping sides and a third stroke descending centrally from its apex. The central shaft makes this an upward arrow rather than the t |
| M0036 | 5 | `\unsure{\wedge}` | other | `\uparrow` | high | The mark below x-to-1 has a sloping left arm, a curved right arm and a separate central downstroke that reaches below the left arm. This is an upward-pointing arrow with |
| M0040 | 5 | `\unsure{\wedge}` | other | `\uparrow` | high | The sign above C has an arched pointed cap, two outer downward arms and an additional central descending shaft, with a white gap separating the shaft from the left arm. T |
| M0056 | 6 | `\unsure{\psi|\varphi}` | alternative | `\varphi` | high | The left curved arm joins a long vertical descender, while the upper-right stroke forms a closed oval with a small light counter. It has no separate upright central prong |
| M0057 | 6 | `\unsure{\psi|\varphi}` | alternative | `\varphi` | high | The left hooked arm meets a downward-curving stem; its right lobe is an enclosed, ink-filled oval. The stem does not rise independently between open arms as it does in th |
| M0059 | 6 | `\unsure{\psi|\varphi}` | alternative | `\varphi` | high | The glyph has a curled left arm, a short curved descender and an elongated closed right oval with a visible light center. That enclosed right lobe is the same varphi cons |
| M0065 | 7 | `\unsure{l}` | other |  | high | A second inspection of the rotated source crop confirms only an opening parenthesis, the M with two long strokes, a closing parenthesis and a comma. Blank paper separates |
| M0071 | 7 | `\unsure{\{\ne0\}|\complement\{0\}}` | alternative | `\complement\{0\}` | high | Inside the inverse-image parentheses there is a tall, looped complement sign followed by a separate small left brace, a rounded zero and a right brace. No pair of horizon |
| M0075 | 7 | `\unsure{continuité}` | other | `condition` | medium | The upper pencil word starts with open c/o and a low n join. Its next prominent stroke has a low rounded bowl leading into a taller ascender, supporting d; a later uprigh |
| M0076 | 7 | `\unsure{à gauche}` | other | `technique` | medium | The lower pencil word has an initial tall t-like stroke, low e/c joins and a medial tall h ascender. Farther right, the conspicuous descending loop belongs to a late q fo |
| M0082 | 8 | `\unsure{\nu|t}` | alternative | `t` | high | The isolated glyph after pour has an upright ascender crossed by a short horizontal bar, with a small lower continuation. It is a crossed t, unlike the uncrossed V-shaped |
| M0086 | 8 | `\unsure{déterminée|déterminé}` | alternative | `déterminé` | medium | The final letter is a small open e form with an acute accent above it. The ink ends immediately after that accented e, with clear paper to its right; no second terminal e |
| M0095 | 8 | `\unsure{\varphi_f(t)}` | other | `\varphi(t)` | medium | The deleted expression retains a broad phi loop, its long downward stem, and separate parentheses around the crossed t. The paper immediately below and to the right of th |
| M0113 | 8 | `\unsure{\varphi_{\alpha(f)}}` | other | `\varphi_{f^\alpha}` | medium | The insertion has a closed phi head with a long stem. At its lower right is a narrow f-like tall stroke descending below the small alpha; the alpha's loop/crossing sits a |
| M0121 | 9 | `\unsure{\mu_f}` | other | `\nu_f` | high | The cancelled main glyph forms a pointed V-like body with its left stroke descending well below the cancellation and its right arm rising to it. The adjacent lower f has |
| M0125 | 9 | `\unsure{concave}` | other | `continue` | medium | The insertion above the crossed-out décroissante begins with a small open c, then a compressed on connection, a tall crossed t-like stroke followed by a separate i dot, a |
| M0131 | 9 | `\unsure{+\infty}` | other | `f^{-1}` | high | The marked mathematical fragment has a tall f-shaped stem with a small upper loop and hooked descending foot. To its upper right are a separate raised horizontal minus an |
| M0154 | 10 | `\unsure{s|u}` | alternative | `u` | medium | Inside the parentheses the letter makes a tall left entry, a rounded bottom trough, and a right-hand rise followed by a short downstroke. That open trough and right stem |
| M0156 | 10 | `\unsure{R_*}` | other | `R_*^+` | high | The cancelled domain retains the loop and diagonal leg of R, a separate star below to its right, and a distinct raised plus with its own vertical stroke and horizontal cr |
| M0158 | 10 | `\unsure{\nu|\mu}` | alternative | `\mu` | high | After the equals sign the letter has a long descending left stroke, an ascending connection across its middle, and a separate right shoulder ending to the right. That des |
| M0206 | 12 | `\unsure{K|k}` | alternative | `k` | high | Inside the final parentheses the letter is narrow, with a short nearly vertical stem and two small right arms attached low on it. It lacks the tall broad upper-right diag |
| M0228 | 13 | `\unsure{Supposons|Donnons}` | alternative | `Donnons` | high | The initial capital is a tall closed D loop returning to a horizontal exit stroke, followed by a low rounded o and paired n-like valleys; the later small o/n forms and te |
| M0244 | 14 | `\unsure{e^s|\exp s}` | alternative | `\exp s` | high | Within the alpha parentheses the e/x cluster is followed by a separate p-shaped downstroke and then s on the same writing line. The s is not raised as an exponent; severa |
| M0249 | 14 | `\unsure{\infty\infty|0}` | other | `\infty` | high | The superscript has one continuous horizontal figure-eight: exactly two adjacent enclosed eyes with a crossing waist. There is no second figure-eight and no separate oval |
| M0252 | 14 | `\unsure{(\varphi_g)}` | other | `\deleted{(f)}(\varphi_g)` | medium | After W there is a cancelled parenthesized f: a small left curve, tall looped stem with a descending hooked foot and low right loop, crossed by cancellation strokes, foll |
| M0259 | 15 | `\unsure{1|\infty}` | alternative | `\infty` | high | The superscript immediately right of the heavily overwritten first L is a horizontally joined pair of rounded lobes with a central waist, clearly an infinity sign. It is |
| M0299 | 18 | `\unsure{Corollaire}` | other | `Corollaire 2` | medium | Under the heavy cancellation, the large opening C and paired tall ll ascenders identify Corollaire, matching the corresponding shapes in this page’s upper heading. To the |
| M0310 | 19 | `\unsure{de}` | other | `le` | medium | The surviving beginning has a single narrow tall loop rising directly from its entry stroke, followed by a separate lower upright/hump. There is no low oval preceding the |
| M0334 | 20 | `\unsure{uniformt}` | other | `unift` | medium | The abbreviation begins with a small upturned entry and a long, low, compressed connecting stroke, then rises into the prominent f-stroke, which drops below the line and |
| M0335 | 21 | `\unsure{uniformt}` | other | `unift` | medium | After the underlined commutative, the word has a shallow initial hook and long connected low prefix leading into a tall descending f with an upward return. The next separ |
| M0346 | 21 | `\unsure{C_{i_0}|D_{i_0}}` | other | `C_i` | medium | A heavy outer stroke rises into a right-facing upper hook and rounds into a lower right tip, forming C over a thinner old closed/diagonal loop. At the lower right, one sm |
| M0352 | 21 | `\unsure{$M$}` | other | `$\Omega$` | medium | Between de and the period is one tall rounded arch with a left baseline foot and a right outward foot. The arch survives above the cancellation and contains no second pea |
| M0358 | 22 | `\unsure{est}` | other | `$=$` | high | Between et and dans are exactly two separate heavy, nearly horizontal parallel strokes, with no connecting curve, e loop, s, or upright terminal t. This is an equals sign |
| M0362 | 22 | `\unsure{\underline a|\underline c}` | alternative | `\underline c` | high | The underlined letter after où is a small open curve with upper and lower rightward ends and a clear gap on the right; it has no closing right downstroke. The underlined |
| M0369 | 23 | `\unsure{uniformt}` | other | `unift` | medium | A compressed nearly horizontal prefix is followed by a tall descending f-like stroke whose upward diagonal goes directly into a small raised terminal t/hook. There is no |
| M0370 | 23 | `\unsure{\mu|\rho}` | alternative | `\rho` | medium | The glyph above the end of the measure line has a long left upright/descender and a single rounded upper hook bending over to its right, with a pale interior. It does not |
| M0377 | 23 | `\unsure{uniformt}` | other | `unift` | medium | After the compressed low initial run, the f rises to a sharp upper turn and drops deeply below the marginal baseline. A small raised angular t follows immediately. There |
| M0382 | 23 | `\unsure{T|\varphi}` | alternative | `\varphi` | high | The unstruck symbol has a broad curved bowl, open at the upper left and closing into a small right loop, with a long stem descending from the bowl junction. These curved |
| M0401 | 24 | `\unsure{\varphi}` | other | `\varphi_{1+f}` | medium | The upper cancelled phi has an oval loop with a long descending stem. Beneath its right side there are a separate upright 1, a plus formed by crossing short strokes, and |
| M0416 | 24 | `\unsure{A|\underline b}` | other | `A\ \underline b` | high | The targeted sequence view shows two successive canceled glyphs before the separate current A. The first has a pointed capital apex, two sloping legs and a crossbar, with |
| M0461 | 25 | `\unsure{1|2}` | alternative | `2` | medium | The subscript has a broad upper hook, a thick descending middle and a distinct rightward lower foot. That stepped outline favors 2 over the short triangular 1 in the foll |
| M0462 | 25 | `\unsure{muni|ayant}` | alternative | `ayant` | medium | After the low initial body, an isolated middle stroke descends deeply below the writing line and the final rising run ends in a crossed t. Those features favor ayant over |
| M0497 | 25 | `\unsure{soient|sont}` | alternative | `sont` | medium | The word has a separated s curve, a low o/n connection and a sharply raised terminal t. There is no separate i dot or extra e body in the clear space before that terminal |
| M0501 | 26 | `\unsure{Breifr|Breifm}` | other | `Breifn` | high | The typewritten sequence visibly reads B-r-e-i-f, followed by a letter with one rounded arch and a right upright. That final n has neither the short shoulder of r nor the |
| M0502 | 26 | `\unsure{minimale}` | other | `minimal` | medium | The final letter is a tall l with a short right-curving foot; a clear white gap separates it from the round following period. The targeted enlargement shows no intervenin |
| M0508 | 26 | `\unsure{d'une algèbre sans atomes}` | other | `d'une algèbre de von Neumann` | medium | After d'une and the looped g/ascenders of algèbre, the insertion has a narrow de, a short low von group, and a conspicuous capital N with an extended joined ending. Those |
| M0524 | 26 | `\unsure{\theta|A}` | alternative | `A` | high | The character is pointed and triangular, with a crossbar and a hooked lower-left foot; it has the angular outline of A rather than a rounded theta. |
| M0527 | 26 | `\unsure{que continuons}` | other | `en question` | high | The first word has a looped e and n hump with no q descender. The next has a descending initial q, a medial crossed t and following i dot, supporting en question rather t |
| M0537 | 27 | `\unsure{\Downarrow}` | other | `\downarrow` | high | One vertical shaft descends from the horizontal line to a dark downward arrowhead. The curved incoming arrow at upper left is separate, leaving no second downward shaft t |
| M0572 | 28 | `\unsure{\underline b|\underline\Phi}` | alternative | `\underline\Phi` | high | A central vertical stroke projects above and below a loop drawn on both sides of it; a short separate underline lies underneath. The bilateral loop distinguishes Phi from |
| M0584 | 29 | `\unsure{\sigma|s}` | alternative | `s` | high | The isolated letter after E= has two compact opposing bends and a lower leftward foot. It has neither an oval sigma bowl nor a rightward top arm. |
| M0598 | 30 | `\unsure{1+|A+}` | alternative | `A+` | high | The first sign has two sloping sides and a visible low crossbar, forming A rather than a single upright 1; a separate plus follows it. |
| M0633 | 32 | `\unsure{E,E|E,F}` | alternative | `E,F` | high | The first raised letter has the lower return of E; the second has a descending stem with top and middle bars but no lower return, matching the clear F in the adjacent E,F |
| M0660 | 34 | `\unsure{op.}` | other | `proj.` | medium | A narrow initial down/up stroke is followed by two distinct medial lobes, then a separate long left-hooked descender and period. The nearby proj. has the same four-part s |
| M0706 | 35 | `\unsure{\underline a|a}` | alternative | `a` | high | The upper a after A and the membership sign is a compact low oval with a rightward exit and no separate stroke beneath it. The nearby crossed-out lower a visibly has a di |
| M0790 | 39 | `\unsure{les}` | other | `, $\ldots$` | medium | A separate comma is followed by an elongated low continuation stroke with several darker points. There is no tall l or a separable es body; the unit is punctuation and a |
| M0791 | 39 | `\unsure{premiers}` | other | `$\lambda_n(u)$` | medium | There is one baseline lambda with a separate lower-right n, followed by a curved opening parenthesis and one baseline u. The crowded terminal strokes form the closing-par |
| M0795 | 39 | `\unsure{\rho_n(u)}` | other | `\rho_1(u)` | medium | The crossed rho retains its upper loop and descending stem; the low index is a short upright, like the clear 1 directly below. The horizontal return farther right belongs |
| M0796 | 39 | `\unsure{\lambda_n(u)}` | other | `\lambda_1(u)` | medium | The lambda has its tall slant and two lower legs. Its separate low index is a single short downstroke, matching the boxed lambda_1 below rather than the long horizontal n |
| M0815 | 39 | `\unsure{Ky-Fan|ky-Fan}` | alternative | `ky-Fan` | medium | The first letter has a straight ascender and a small rounded shoulder at its foot, the minuscule k form. The following y descends well below it; F has two separate rightw |
| M0856 | 40 | `\unsure{\text{---}}` | other | `\text{-- --}` | high | Between the parentheses are two separate horizontal strokes on the same level, with a visible gap between them and no letter bodies. |
| M0866 | 40 | `\unsure{Comme les particuliers en un corollaire, on a}` | other | `Comme cas particulier de ce corollaire, on a` | medium | The short second word has a low open c curve, compact a hump and trailing s; the longer word retains a p descent, crossed t, two i dots and a terminal er run without an a |
| M0888 | 42 | `\unsure{la propriété}` | other | `propriété` | medium | After the canceled est ends, a clear gap leads directly to the first descending p of propriété; there is no intervening la. A second p descender and the final tall t with |
| M0889 | 42 | `\unsure{précédent}` | other | `précédente` | medium | The initial descending p and compressed ré carry a visible acute accent; the middle strokes are closely joined. The ending has a tall looped t-like stroke followed by an |
| M0895 | 42 | `\unsure{2}` | other | `(2)` | high | Above the baseline L are three separate components: a curved left parenthesis, a capped descending 2, and a curved right parenthesis. The central numeral matches the smal |
| M0898 | 44 | `\unsure{Opérateurs Fredholm}` | other | `Op. de Fredholm` | medium | Before the clear capital F of Fredholm, the surviving ink shows a short Op. cluster and a separate small looped de; there is no readable continuous -érateurs sequence. A |
| M0903 | 44 | `\unsure{symétrique}` | other | `algébrique` | medium | The initial low a-like loop is followed by a tall l upright and then a separate small g descender; this ascender/descender sequence supports alg- rather than sym-. The co |
| M0909 | 44 | `\unsure{elle est}` | other | `est` | medium | The word is one connected low unit ending in a short upright t. The enlarged context has no pair of l ascenders and no second separated word, supporting est alone rather |
| M0911 | 44 | `\unsure{de l'espace de Banach}` | other | `d'espace de Banach` | medium | A single hooked d and adjacent apostrophe precede the low espace group and its p descender; there is no separate e followed by tall l before espace. The following de and |
| M0921 | 44 | `\unsure{deux}` | other | `trois` | high | The inserted word above the cancelled baseline begins with a short cross-stroke and tall t, continues with a small r/o join, and ends in a dotted i and hooked s. There is |
| M0923 | 44 | `\unsure{$L^h$}` | other | `$L'L'$` | medium | After rotation, both tall stem-and-hook bodies have their feet on the same baseline, and each bears a separate raised short oblique prime. The second lateral stroke start |
| M0942 | 45 | `\illegible{1}` | other |  | high | The last prose line ends with the shallow final stroke of d'espaces and remains blank to the margin edge; the diagonal strokes crossing that blank are cancellation lines, |
| M0993 | 50 | `\unsure{Th|Prop}` | other | `Th 1` | medium | The underlined title has a T crossbar and descending stem, followed by an h-like ascending stem and low hump. A separate short vertical stroke at x318–329,y231–257 follow |
| M1000 | 50 | `\unsure{linéairement|linéarité}` | alternative | `linéarité` | medium | The end has a short crossing/downward stroke before the final low hooked letter and a detached rising accent over that last letter. This supports the final té of linéarit |
| M1026 | 52 | `\illegible{1}` | other | `$l^2$` | medium | One tall narrow loop continues below the cancellation into a rightward lower hook, supporting baseline l. A separate smaller upper-right mark has a curved cap and descend |
| M1038 | 53 | `\unsure{mettre le (\# 2)}` | other | `mettre le (Th. 2)` | medium | The crossed first line shows mettre followed by a tall l and small e. On the next line, parentheses enclose a tall left stem and a right h-shaped curved foot, followed by |
| M1053 | 53 | `\unsure{(\mathrm{v.s.})^2\,h|(\mathrm{v.s.})^2}` | alternative | `(\mathrm{v.s.})^2` | medium | The compact parenthesized abbreviation has a small elevated 2. The nearby tall h is attached to the deleted line above: its ascender crosses that cancellation and its bow |
| M1081 | 54 | `\unsure{effet}` | other | `fait` | medium | One tall looped f is followed by a low rounded a body, a short stroke with its own detached dot, and a crossed terminal t. The dot lies below the upper insertion and alig |
| M1099 | 55 | `\unsure{parties en italiques|petites corrections}` | alternative | `petites corrections` | high | The underlined phrase has two word groups. The first has a p descender, crossed t strokes and an i dot; the second starts with an open c and ends in a crowded crossed gro |
| M1102 | 55 | `\unsure{1|' }` | alternative | `' ` | high | Above the tensor sign is one short, isolated curved oblique stroke. It has neither the length nor a baseline foot of a numeral 1, and reads as a prime. |
| M1132 | 57 | `\unsure{$\forall$}` | other | `(` | medium | The small independent stroke before A descends and curves right at its foot, forming an opening parenthesis. Its hooked outline matches the opening parenthesis before G o |
| M1159 | 58 | `\unsure{\|u\||\|u\|_1}` | alternative | `\|u\|_1` | high | Inside the inserted radical are two left bars and one baseline u. At the right are two taller bar strokes followed by a separate third, lower hooked upright before the cl |
| M1162 | 59 | `\unsure{à|:}` | alternative | `:` | high | Two separate dark dots lie one above the other after Applications; there is no connected oval body or grave-accented a. |
| M1169 | 59 | `\unsure{est un|on a un}` | alternative | `on a un` | medium | Three separated groups are visible: a low linked opening group, a separate rounded a, and the joined low strokes of un. The separate middle a and absence of a tall t favo |
| M1228 | 62 | `\unsure{donc|d'où}` | alternative | `d'où` | medium | The deleted word has a looped d, a separate raised apostrophe immediately after it, a small o bowl, and a low u-shaped ending with a separate raised grave-like mark. The |
| M1242 | 63 | `\unsure{donc|d'où}` | alternative | `d'où` | medium | The crossed word has a looped initial d, a separate raised apostrophe, a small o loop and a following low vowel body with a detached accent above it. These separated uppe |
| M1274 | 65 | `\illegible{1}` | other | `De` | medium | A separate cancelled group after the left remnant has a tall D upright with a rounded right bowl, followed by a small open e loop. The D/e group is spatially distinct fro |
| M1280 | 66 | `\unsure{comme|carré}` | alternative | `carré` | medium | An open c is followed by a compact low a and compressed r joins; a detached rising acute stands above the final short e stroke. The acute and the low middle strokes suppo |
| M1318 | 67 | `\unsure{\sigma_i(u)}` | other | `\|u\|` | high | The final member has two distinct opening vertical bars, one baseline u with two stems joined by a bowl, and two distinct closing vertical bars. There is no sigma loop, i |
| M1327 | 67 | `\unsure{(2)|(1)}` | alternative | `(1)` | high | The raised group has a curved opening parenthesis, one thick straight upright 1, and a curved closing parenthesis. The central stroke lacks the bent head and lower return |
| M1338 | 67 | `\unsure{conserve|invarie}` | alternative | `invarie` | high | The underlined word begins with a dotted i, then low n/v forms, a rounded a and r shoulder, a second dotted i and terminal e. Its dotted initial and lack of an opening co |
| M1341 | 67 | `\unsure{$E$|$F$|$\Lambda E$}` | alternative | `$\Lambda E$` | high | The canceled group contains two oblique arms meeting in a Λ apex, followed by a separate upright E with top, middle and bottom bars. Both baseline symbols are visible ben |
| M1405 | 70 | `\unsure{cpt|cpct}` | alternative | `cpct` | medium | Four letter events follow op.: a small initial open c, a descending p-shaped stroke, a separate broad open c bowl, and the terminal taller t with a rightward foot. The se |
| M1410 | 70 | `\unsure{uv|vu}` | alternative | `vu` | medium | The first of the two baseline letters is tall and filled, with a closed narrow lower turn and high right return; the second is lower, with an open rounded trough, rising |
| M1430 | 71 | `\unsure{mnemotechnique|mnémotechnique}` | alternative | `mnémotechnique` | high | The low joined mnemo body has a short detached rising accent above its first e. The rest shows the tall crossed t, low e/c join, tall h, joined n, dotted i, descending q |
| M1443 | 72 | `\unsure{n|\text{--}}` | alternative | `\text{--}` | high | The subscript under the right sigma is one low horizontal stroke with a tiny upward entry at its left. The nearby n under the preceding sigma has a tall entry, raised arc |

</div>

Most undecided marks are in struck-out text:

<div class="tw">

| Decision    | Mark in struck-out text | Mark in live text |
|-------------|-------------------------|-------------------|
| first       | 239                     | 336               |
| alternative | 7                       | 35                |
| other       | 22                      | 32                |
| undecided   | 573                     | 170               |

</div>

### Errors it found outside the marks

11 places.

- scan 3: N° 6, cancelled clause between dans les and d’opérateurs: C has `espaces`; The visible letters form anneaux: a followed by repeated low n/e arches and a final x. The original page is left unchanged outside marks. Independently confirmed; second inspected crop (210,305,1640,485). Both original reports remain in the audit.
- scan 5: Before f in on a pour \\\forall f\in R\_\*\\, source pixels 1115,1305,1280,1385: C has `\forall`; The horizontal word before f has a tall initial t-like stroke, a low interior dot/run and a right terminal t. A heavy diagonal crosses the whole group. The scan therefore shows a cancelled word, apparently tout, while the source prints an uncancelled forall sy
- scan 5: After ce qui prouve, the unmarked \deleted{que}; source pixels 675,1690,835,1775: C has `\deleted{que}`; The cancelled group has a looped phi with a long descender, followed by a psi with two raised arms and its own long descender. A horizontal strike passes through both. These are the same mathematical letter shapes used elsewhere on this page, rather than the l
- scan 8: First marginal integral, above the N_p equality; source bounds \[115,1550,315,1750\]: C has `\int f\,dm=\int s\,d\mu_f(s)`; The integrand reads s d\nu(s): after the looped d there is a single narrow descending-and-rising nu, then an opening parenthesis and s; no separate lowered f occurs between nu and the parenthesis. Thus the visible correction is \int f\\dm=\int s\\d\nu(s).
- scan 19: Inserted fidelity sentence, immediately after si and before the deleted A∈𝒜+ (approximately x945–1040, y2155–2198).: C has `si \deleted{$\unsure{A\in\mathcal A^+}$} $A\geq0$`; There is an additional separately crossed cluster immediately before the marked formula. It begins with a broad curved top and vertical downstroke, continues through an open curved/intersecting group, and ends with an upright stroke. I do not securely identify
- scan 27: Unmarked words between M0538 and (5), source pixels \[1055,1125,1330,1195\].: C has `dans (5)`; Two distinct d-start words are visible: donc dans (5). The first has a low oval d, a long joined middle, and a detached shallow open c-like terminal; the second has looped d, detached low dot, long baseline and comma-like terminal s, matching the earlier dans
- scan 39: Unmarked \$\lambda_n(u)\$ immediately before M0790 in the Si la dim paragraph; source pixels approximately \[1040,438,1135,483\].: C has `$\lambda_n(u)$`; The first formula has a small simple vertical subscript 1 under lambda, unlike the broad n-shaped lower index in the second formula at \[1250,448,1430,495\]. The visible first reading is lambda_1(u); the source formula is outside every page-39 mark and was not c
- scan 40: Immediately after the canceled M0835 expression, before the surviving \|Tr p_nu\|; source box \[612,686,745,739\].: C has `\deleted{\unsure{|\operatorname{Tr}p_nup_n|=}}\quad`; The same crossed-out line continues with an additional \|\operatorname{Tr}w\|: two upright bars enclose a clear T crossbar/stem, low r and rounded w body. This canceled term is omitted from the existing source; it lies outside the marked M0835 span.
- scan 42: Unmarked vérifie immediately before M0888, around source pixels \[900,1305,1125,1370\].: C has `vérifie`; The gap after canceled est leads directly into the single word propriété, followed by de v. Its two p descenders and final té leave no separate vérifie token in that position; the unmarked source word appears unsupported by the ink and is not changed here.
- scan 44: Unmarked \$E,F\$ immediately before M0920/M0921; source box (310,1355,495,1410).: C has `$E,F$`; A third capital G follows the comma after F: its open round body and short inward bar are visible at x430–460, y1370–1398. The sequence is E,F,G; it lies outside every listed mark and is not edited.
- scan 46: Canceled line after the unstruck qui and immediately before M0954; source insertion boundary outside every listed mark.: C has `qui \deleted{`; A further short canceled word at \[305,830,400,895\] precedes the tall-f fait of M0954. Its hooked initial, flat low join and final dot resemble the uncanceled qui at \[775,1400,855,1450\], while an additional qui is visibly present at the previous line end \[1545,

### Its pace

<div class="tw">

| Scan | Marks | Minutes (reader start to commit) | Marks an hour | Page views | Crop views | Crops a mark |
|----|----|----|----|----|----|----|
| 3 | 16 | 3.4 | 280 | 1 | 9 | 0.56 |
| 4 | 13 | 5.1 | 153 | 1 | 26 | 2.00 |
| 5 | 25 | 4.1 | 366 | 2 | 32 | 1.28 |
| 6 | 10 | 7.2 | 83 | 1 | 29 | 2.90 |
| 7 | 16 | 7.1 | 135 | 2 | 28 | 1.75 |
| 8 | 34 | 9.4 | 218 | 2 | 33 | 0.97 |
| 9 | 20 | 6.3 | 189 | 2 | 27 | 1.35 |
| 10 | 31 | 6.4 | 292 | 3 | 36 | 1.16 |
| 11 | 4 | 2.8 | 85 | 1 | 13 | 3.25 |
| 12 | 37 | 5.4 | 412 | 3 | 37 | 1.00 |
| 13 | 34 | 7.0 | 291 | 3 | 38 | 1.12 |
| 14 | 15 | 6.0 | 150 | 1 | 25 | 1.67 |
| 15 | 17 | 6.0 | 169 | 2 | 25 | 1.47 |
| 16 | 14 | 4.3 | 197 | 2 | 24 | 1.71 |
| 17 | 4 | 1.2 | 202 | 1 | 7 | 1.75 |
| 18 | 9 | 3.3 | 165 | 2 | 24 | 2.67 |
| 19 | 16 | 3.2 | 297 | 2 | 28 | 1.75 |
| 20 | 19 | 2.5 | 453 | 3 | 22 | 1.16 |
| 21 | 19 | 5.0 | 226 | 3 | 34 | 1.79 |
| 22 | 15 | 16.3 | 55 | 2 | 29 | 1.93 |
| 23 | 21 | 6.8 | 184 | 3 | 35 | 1.67 |
| 24 | 66 | 10.6 | 373 | 3 | 56 | 0.85 |
| 25 | 42 | 9.1 | 277 | 2 | 65 | 1.55 |
| 26 | 33 | 7.1 | 279 | 3 | 38 | 1.15 |
| 27 | 14 | 8.6 | 98 | 2 | 20 | 1.43 |
| 28 | 29 | 5.8 | 301 | 3 | 35 | 1.21 |
| 29 | 18 | 4.2 | 257 | 3 | 24 | 1.33 |
| 30 | 17 | 5.5 | 186 | 2 | 17 | 1.00 |
| 31 | 13 | 4.0 | 194 | 2 | 24 | 1.85 |
| 32 | 24 | 5.8 | 248 | 3 | 36 | 1.50 |
| 33 | 6 | 1.5 | 235 | 2 | 12 | 2.00 |
| 34 | 20 | 8.0 | 150 | 3 | 34 | 1.70 |
| 35 | 41 | 5.6 | 439 | 3 | 53 | 1.29 |
| 36 | 35 | 5.5 | 384 | 3 | 36 | 1.03 |
| 38 | 33 | 6.4 | 310 | 3 | 48 | 1.45 |
| 39 | 38 | 9.8 | 233 | 3 | 58 | 1.53 |
| 40 | 50 | 21.0 | 143 | 3 | 83 | 1.66 |
| 41 | 5 | 2.7 | 113 | 1 | 7 | 1.40 |
| 42 | 22 | 6.8 | 193 | 3 | 37 | 1.68 |
| 44 | 31 | 7.6 | 243 | 3 | 54 | 1.74 |
| 45 | 21 | 6.0 | 211 | 3 | 38 | 1.81 |
| 46 | 18 | 7.4 | 147 | 3 | 33 | 1.83 |
| 48 | 12 | 5.7 | 126 | 2 | 21 | 1.75 |
| 49 | 14 | 7.3 | 115 | 2 | 24 | 1.71 |
| 50 | 9 | 5.4 | 100 | 2 | 24 | 2.67 |
| 51 | 10 | 2.2 | 270 | 2 | 22 | 2.20 |
| 52 | 20 | 3.9 | 312 | 3 | 27 | 1.35 |
| 53 | 25 | 5.3 | 282 | 3 | 44 | 1.76 |
| 54 | 29 | 6.3 | 278 | 3 | 45 | 1.55 |
| 55 | 18 | 9.4 | 115 | 3 | 29 | 1.61 |
| 56 | 19 | 7.4 | 154 | 3 | 44 | 2.32 |
| 57 | 23 | 7.9 | 175 | 3 | 33 | 1.43 |
| 58 | 17 | 5.7 | 180 | 2 | 37 | 2.18 |
| 59 | 19 | 5.7 | 201 | 3 | 38 | 2.00 |
| 60 | 16 | 5.6 | 173 | 2 | 28 | 1.75 |
| 61 | 11 | 4.2 | 157 | 2 | 21 | 1.91 |
| 62 | 25 | 8.8 | 170 | 3 | 42 | 1.68 |
| 63 | 15 | 11.6 | 77 | 2 | 31 | 2.07 |
| 64 | 12 | 2.7 | 263 | 2 | 16 | 1.33 |
| 65 | 20 | 4.6 | 261 | 3 | 30 | 1.50 |
| 66 | 14 | 2.5 | 342 | 1 | 25 | 1.79 |
| 67 | 49 | 9.6 | 308 | 3 | 107 | 2.18 |
| 68 | 26 | 5.4 | 289 | 3 | 46 | 1.77 |
| 69 | 36 | 7.9 | 272 | 3 | 71 | 1.97 |
| 70 | 11 | 8.6 | 77 | 2 | 28 | 2.55 |
| 71 | 15 | 5.2 | 174 | 2 | 41 | 2.73 |
| 72 | 17 | 5.3 | 193 | 2 | 32 | 1.88 |

</div>

1447 marks in 443 minutes from its first line to its last page: about 196 marks an hour. The 1,237 marks left on cote 1 would take about 6 hours at that pace, about 8 checkpoints.

### Its workflow record (WORKFLOW.md), entry by entry

1.  **22:09 UTC**: source geometry and indexing (logged)
2.  **22:11 UTC**: sequential page coordinator and fresh reader contexts
3.  **22:16 UTC**: first fresh-context page measured; same-page splitting begins next
4.  **22:20 UTC**: first split-page measurements
5.  **22:29 UTC**: deletion stopping criterion and lower splitting threshold
6.  **22:36 UTC**: first page below the old split threshold; shared crops next
7.  **22:46 UTC**: shared-band measurements and coordinator handoff
8.  **22:53 UTC**: first timed checkpoint confirmed
9.  **23:00 UTC**: first three-reader page measured
10. **23:16 UTC**: staged coordinator phases
11. **23:20 UTC**: concurrent spare-slot peer on scan 014
12. **23:22 UTC**: duplicate error-list entry consolidated
13. **23:22 UTC**: first completed staged-coordination page measured
14. **23:25 UTC**: checkpoint timer separated from visual coordination
15. **23:28 UTC**: root-direct visual dispatch
16. **23:30 UTC**: allocation thresholds broadened for fresh visual contexts
17. **23:33 UTC**: scan 016 supports the uncertainty stopping rule
18. **23:35 UTC**: direct root completion of a small page
19. **23:37 UTC**: timed checkpoint 02 confirmed
20. **23:39 UTC**: first page under the lower two-reader threshold measured
21. **23:39 UTC**: checkpoint timer outcome
22. **23:45 UTC**: first page under the lower three-reader threshold measured
23. **23:51 UTC**: supplemental primary timing made explicit
24. **23:58 UTC**: checkpoint process monitor strengthened
25. **00:01 UTC**: heartbeat verified; detached attempt did not start
26. **00:05 UTC**: audited amendment A0001_unift_020_021
27. **00:22 UTC**: timed checkpoint 03 confirmed
28. **00:25 UTC**: dense-page measurements and concise annotations
29. **00:36 UTC**: scan025 annotation measurements
30. **00:36 UTC**: include prefixed reader scripts in timed packages
31. **00:51 UTC**: independent unmarked-error provenance
32. **01:07 UTC**: timed checkpoint 04 confirmed
33. **01:07 UTC**: count baseline letters before accepting a power reading
34. **01:12 UTC**: first page after explicit formula-letter accounting
35. **01:40 UTC**: preserve source candidate metadata
36. **01:46 UTC**: explicit empty replacement for absent marked ink
37. **01:52 UTC**: timed checkpoint 05 confirmed
38. **01:57 UTC**: refresh final coordination counts
39. **02:00 UTC**: measured follow-up through scan039
40. **02:03 UTC**: resumed readers and checkpoint service after interruption
41. **02:37 UTC**: timed checkpoint 06 confirmed
42. **03:22 UTC**: timed checkpoint 07 confirmed
43. **03:59 UTC**: completed reminder comparison through scan058
44. **04:07 UTC**: timed checkpoint 08 confirmed
45. **04:15 UTC**: incremental pattern synthesis through scan060
46. **04:52 UTC**: timed checkpoint 09 confirmed
47. **04:56 UTC**: Scan 067 inspection cost and reconciliation
48. **05:16 UTC**: Text-only pattern index through scan 069

What it changed, in its own measured terms (WORKFLOW.md):

- **A fresh reader for every page** from scan 4, so that earlier images do not stay in a reader's context.
- **A page's marks split between readers** by their number. Its last thresholds (from 19 Nov 23:30 UTC): three readers at 18 marks or more, two at 6-17, one below 6. Its first were 24, then 30 and 10.
- **Neighbouring marks on one band crop**, with a tight crop only for a feature still open.
- **A stopping rule for struck text**: once enlarged views and one independent look show no distinguishing stroke, the doubt stays. On scan 16 four independent re-checks of obscured ink settled nothing more.
- **Independent re-checks only where a plausible competing reading has a visible feature.** The abbreviation "unift" on scans 20-21 was recovered this way.
- **Count the baseline letters before accepting a power or an index** (scan 30: A^2 was A^\*A).
- **Evidence in one or two sentences a mark** (from scan 25), a due-only checkpoint timer, and a staged coordinator that keeps reader slots free.

It marks every comparison between pages as observed, not controlled: pages differ in density and cancellation. The full intake of this and the other recent returns is in `INTAKES_20261120.md`.

### The recurring patterns it recorded (PATTERNS.md)

- Long connective strokes in compressed French cursive
- Deletion and overwriting can genuinely destroy distinctions
- Compact fblt abbreviation
- Heavy deletions preserve only partial readings
- Abbreviated text preserved without expansion
- Upward arrow beneath a limit variable
- fbt abbreviation with variable joining
- Joined opening parenthesis and rounded v
- Cancellation can leave no recoverable interior
- Closed right oval in varphi, separate central prong in psi
- Horizontal cancellation hides low letter bodies
- Raised infinity in the margin
- Faint pencil compression
- Cancellation hides identifying strokes
- Crossed t and pointed nu
- Surviving text around heavy cancellation
- Repeated N_p with lowered p
- Narrow nu shape
- Raised alpha beside a low f
- Pointed nu compared with shoulder-shaped mu
- Small looped phi
- Thick equals sign with visible central separation
- Same-page concave comparison for insertion
- Open Psi versus looped phi
- Separate 1 and branched lambda
- Branched lambda in formula (14) and formula (15)
- mu left descender
- Overstrikes conceal low letter bodies
- Compact fblt abbreviation
- Tall stems survive cancellation more often than word bodies
- Compressed fblt abbreviation
- Distinct capital K and lower-case k
- Dotted si and open omega
- Cancellation obscures bodies and operators
- Heavy cancellation obscures baseline letters
- Contracted low letters with separate dots
- Open c versus closed a coefficients
- Single compact xi following an integral
- Tall angular Alors opening
- Dense cancellation obscures interior letters
- Compressed fblt abbreviation
- Compact les before φ_i
- Ascenders surviving deletion
- Compressed marginal word endings
- Deletion masks different parts of writing
- Flattened letter runs with retained dots
- Surviving lower contours under a single deletion stroke
- Cancellation preserves isolated vertical features
- Same-page heading comparison
- Ascenders, dots and descenders survive single cancellation lines
- Overdrawing masks complete word sequences
- Repeated abbreviated s. finie
- Surviving descenders distinguish support from an obliterated word
- Raised terminal t in abbreviated adverb
- Cancellation preserves separated dots and lower joins unevenly
- Heavy C correction over a thinner closed letter
- Omega retains one arch and baseline feet
- Short unift abbreviation with raised terminal t
- Literal symbolic and abbreviated writing
- Open underlined c contrasted with closed underlined a
- Long lower-return measure glyph
- Low open replacement and support measure glyphs
- Local mu with deep left stem and right shoulder
- Short written abbreviation before fermée
- Fidelity phi bowls
- Short unift in marginal insertion
- Mu descending left stem and raised right arm
- Separate phi layers in first marginal note
- Cancellation hides low letter bodies
- Crossings preserve upper features while merging bodies
- Local underlined b structure
- Masked lower word bodies
- Compressed low connecting strokes
- Cancellation preserves stems but hides bodies
- Low compressed groups with distinctive high or low strokes
- Dotted braced i with curled base
- Compressed finie(s)
- Absolute-value bar versus numeral 1
- Measure-symbol stem and shoulder
- Pen lifts inside words
- Intersected prefix
- Superscript E lower return versus F stem
- Compressed less-than-or-equal sign
- Cancellation obscures word bodies
- Contracted proj. abbreviation
- Compressed anneau lettering
- Open bowl in inserted phi candidates
- Separate underline versus heavy glyph base
- Open measure-letter shoulder
- Separated prime versus rounded unprimed B
- Compressed cursive and raised signs
- Overtraced formula capitals
- Angular argument s versus crossed t
- Looped rho with descending stem
- Central damaged strip
- flattened terminal handwriting
- cancelled indexed f
- Scan038 reconciliation: written abbreviation and formula components
- Compressed inserted prose
- Compact raised star versus open numeral 2
- Compressed subscript separator ambiguity
- Compressed hermitien ending
- Detached prime versus crowded label
- Cancellation removes small letter bodies
- Dotted i versus descending j on this page
- Flattened cursive and cancellation limit letter recovery
- Looped rho coefficients
- Descending p forms in propriété
- Parenthesized operator-class superscript
- vectoriel form
- Cancellation across letter bodies
- Raised insertion replaces cancelled baseline word
- Two marginal L-prime bodies
- Legible words with unresolved source placement
- Heavy local correction and cancellation
- Marginal cancellation layers
- An illegibility placeholder without a written token
- Dense raised strokes over conjugation bars
- Baseline obliteration by double cancellation
- Local corrections inside a globally cancelled line
- Raised numeral versus cancellation curl
- Cancellation through baseline
- Cancelled spans retain distinct local strokes
- Heavy horizontal cancellations
- Final component check limits a proposed formula
- Cancellation absorbs baseline bodies
- Literal abbreviation
- Raised numeral 2
- Separate deletion and surviving letter strokes
- Overlapping cancellation layers
- upper-line h beside summand
- Certainty must cover the retained word sequence
- Different shape of question-like lower mark and numeral 2
- Compact adverb endings
- Deletion lines absorb low letter bodies
- Low e followed by tall terminal t
- Full-height capital U versus shallow lowercase u
- Separated dot in a nearby summation index
- Undotted index and unallocated prefix remain uncertain
- Compact superscript 2
- Scan057: local shape comparison and cancellation junctions
- Cancelled repeated parenthetical E
- Lower-right index separated from paired norm bars
- Scan058: word certainty within a partly resolved phrase
- Scan060: abbreviated ending and unallocated textual groups
- Cancelled and inserted Si
- Scan062: correction layers and word-body limits
- Compressed continue with crossed t and dotted i
- Distinct raised 1 and 2 on this page
- Compressed p-bearing word
- Dense cancellation can leave a recognisable fragment without settling a word
- Looped rho versus forked lambda
- Separate v and u shapes in (24)
- Cursive heading numeral 4
- Scan 071: damage, symbol layers and punctuation count
- Compressed n and double-shouldered m
- Full n versus low dash in neighboring subscripts
- Scan 072: cancelled structure and separate layers

</div>

<div id="methods" class="section">

## 6. Pro's own methods, and whether the prompts carry them

The methods of the second-pass prompts and the ones Pro invented on its own in its returns, with where each came from and which prompts carry it, by their wording. Three findings:

- **What Pro invented is in no prompt.** The per-reader JSON records with crop coordinates and a verdict on each doubt mark, the decisions applied by a script per page, and the extra independent readings for places still open (SP34, SP35), and DM01's shared band crops, stopping rule for struck text and splitting of a page's marks between readers: the prompts carry none of these. The public METHODOLOGY.md described the first three as the design; it is corrected to say they are what the returns did.
- **The pieces forbid what DM01 does with its readers.** The unsent second-pass prompts say "never split the pages among readers": every page is read three times, independently. DM01 gives each mark one reader and a second only where a new reading competes. The two answer different questions (three independent readings of everything, against throughput on the marks).
- **The deep zoom, fresh readers, tight crops and the workflow record are in every unsent piece** (13 prompts).

<div class="tw">

| Method | Proposed | In the sent prompts | In the unsent prompts | In DM01's prompt |
|----|----|----|----|----|
| Three independent readers of every page, and a main reader who decides | 19 Nov ~20:26 UTC (SP34 on) | 21 of 24 | 13 of 13 | no |
| Fresh readers for every page (no reader carries an earlier page's images) | 19 Nov 21:11 UTC; DM01 on its own from scan 4 | 19 of 24 | 13 of 13 | no |
| The readers' brief improved from their disagreements, each version kept | the 21:10 UTC rewrite | 19 of 24 | 8 of 13 | no |
| A workflow record for the next runs (brief versions, crops a page, what worked) | the 21:10 UTC rewrite; DM01 | 19 of 24 | 13 of 13 | yes |
| Page once, halves once, then one tight crop per open place, never re-cropped | the reading workflow, 19 Nov 21:07 UTC | 20 of 24 | 8 of 13 | no |
| Deep zoom: a few thousand pixels across, contrast raised | 19 Nov 21:10 UTC | 19 of 24 | 3 of 13 | yes |
| C's doubt marks listed as places to decide on the ink | the two-witness prompts (14 Nov on) | 24 of 24 | 8 of 13 | no |
| Evidence as the visible strokes, with the crop | the two-witness prompts | 24 of 24 | 8 of 13 | no |
| All three readings listed where the readers differ | the three-reader rewrite | 21 of 24 | 8 of 13 | no |
| One notation table kept across the pages, and recurring signs made to agree | the three-reader rewrite | 24 of 24 | 8 of 13 | no |
| The transcription frozen by hash (SP31-SP33: before the mathematical context; three-reader prompts: when every page is decided) | SP31-SP33; the three-reader prompts | 24 of 24 | 8 of 13 | no |
| Witness S: the readings the sweeps decided on the scan | the 20:5x UTC build | 14 of 24 | 3 of 13 | no |
| Per-reader structured records (JSON: differences, strokes, crop coordinates, a verdict per doubt mark) | Pro's own, in the SP34 and SP35 returns | 0 of 24 | 0 of 13 | no |
| Decisions applied to the text by a script per page (decide_NNN.py) | Pro's own, in the SP34 return | 0 of 24 | 5 of 13 | yes |
| Further independent readings where a place stays open, instead of re-cropping | Pro's own, in the SP34 and SP35 returns | 0 of 24 | 0 of 13 | no |
| Neighbouring marks read on one shared band crop, a tight crop only for a feature still open | Pro's own, DM01, 22:36 UTC | 0 of 24 | 5 of 13 | no |
| A stopping rule for struck text (no distinguishing stroke left: keep the doubt, no more crops) | Pro's own, DM01, 22:29 UTC | 0 of 24 | 0 of 13 | no |
| A page's marks split between readers by their number (1, 2 or 3 readers) | Pro's own, DM01, 22:16 UTC | 0 of 24 | 0 of 13 | no |
| The first readers' recurring misreadings listed for script checks (PATTERNS.md) | the DM design, 19 Nov 21:58 UTC | 0 of 24 | 5 of 13 | yes |

</div>

Unsent: the second-pass pieces in TO_SEND/PRO/2_Archive_second_passes (SP55, SP56, SP57, DM02, DM03, DM04, DM05, SP58, SP59, SP60, SP61, DM06, SP62); sent: the pieces in its .SENT folder (SP31, SP32, SP33, SP34, SP35, SP36, SP37, SP38, SP39, SP40, SP41, SP42, SP43, SP44, SP45, SP46, SP47, SP48, SP49, SP50, SP51, SP52, SP53, SP54). A method counts as present when the prompt carries its wording (the pattern in build_report.py); a 'no' for witness S on a piece means its pages had no sweep row.

</div>

<div id="pilots" class="section">

## 7. The pilots

Six pilots ran on 19 Nov, all Claude Opus 5.5; A-E read cote 156-7 scans 2-6, the pages of Pro's SP35. A: a lead at effort max with three readers at effort high. B: one reader at max. C: two readers at max who debate. D: two readers at high who debate. E: two readers at high capped at 10 crops, one page. They were stopped at 21:00 UTC at our decision, after about 5.5 % of the weekly Claude usage limit; the lead of A and the debates of C and D had decided nothing by then, so most readers' pages are intermediate (they kept doubts for the debate). F: one reader at high checking only where C and Hua disagree, cote 156-4 scans 2-9.

### What they cost

<div class="tw">

| Pilot | Agent | Effort | Tool calls | Output | Cache write | Cache read | Weighted (output 1, cache write 0.25, read 0.02, input 0.2) |
|----|----|----|----|----|----|----|----|
| A | lead | max | 12 | 26k | 133k | 1.1M | 0.08M |
| A | reader R1 | high | 199 | 140k | 951k | 44.0M | 1.26M |
| A | reader R2 | high | 157 | 139k | 835k | 36.2M | 1.07M |
| A | reader R3 | high | 124 | 129k | 1279k | 24.1M | 0.93M |
| B | single reader | max | 201 | 147k | 452k | 61.5M | 1.49M |
| C | coordinator | medium | 4 | 4k | 53k | 0.3M | 0.02M |
| C | reader R1 | max | 202 | 133k | 972k | 54.4M | 1.46M |
| C | reader R2 | max | 177 | 138k | 952k | 48.1M | 1.34M |
| D | coordinator | medium | 14 | 10k | 117k | 1.1M | 0.06M |
| D | reader R1 | high | 226 | 124k | 1249k | 51.6M | 1.47M |
| D | reader R2 | high | 184 | 142k | 1377k | 44.4M | 1.37M |
| E | reader 4d06 | high | 34 | 24k | 137k | 3.6M | 0.13M |
| E | reader 3803 | high | 21 | 24k | 137k | 2.1M | 0.10M |

</div>

### At C's doubt marks, against SP35 on the same pages

<div class="tw">

| Claude reader (Claude Opus 5.5) | Scans | C's marks | Settled by the reader | Settled by SP35 | Same reading as SP35 | Same, where both settled |
|----|----|----|----|----|----|----|
| A R1 (high) | 2, 3, 4, 5 | 83 | 22 | 32 | 68 | 11 of 14 |
| A R2 (high) | 2, 3, 4, 5 | 83 | 11 | 32 | 67 | 5 of 8 |
| A R3 (high) | 2, 3 | 33 | 5 | 20 | 29 | 3 of 4 |
| B (max) | 2, 3 | 33 | 9 | 20 | 29 | 6 of 7 |
| C R1 (max) | 2 | 13 | 5 | 11 | 9 | 1 of 4 |
| C R2 (max) | 2 | 13 | 7 | 11 | 11 | 5 of 6 |
| D R1 (high) | 2, 3, 4, 5, 6 | 115 | 5 | 41 | 91 | 2 of 3 |
| D R2 (high) | 2, 3, 4, 5, 6 | 115 | 8 | 41 | 94 | 3 of 4 |
| E1a (high, 10 crops) | 2 | 13 | 4 | 11 | 9 | 2 of 4 |
| E1b (high, 10 crops) | 2 | 13 | 1 | 11 | 9 | 0 of 1 |

</div>

SP35 is Pro's three-reader pass with the reading workflow of 21:07 UTC. "Same reading" counts marks where the reader's text and SP35's agree, settled or not. Agreement is not accuracy: neither has been checked on the scan at these places.

### Pilot F against SP04

Of 162 places where C and Hua differ that F decided, 136 (84.0 %) agree with Pro's SP04. SP04 changed C at 13 of them; F decided 104 for C, 24 for Hua, 5 neither, 29 notation only and 8 undecidable.

### The API route: pilots 1 and 2 (20 Nov, Message Batches API)

On 19 Nov at 21:54 UTC the main session had estimated that checking the doubt marks through the API "would come to over \$1,000", at about a cent a place. That figure was an extrapolation from a text-only placement run (Claude Opus 5.5 at effort high, 136 requests, about \$3, standard endpoint), not a test of reading doubt marks. The pilots below are that test, run through the Message Batches API at half price.

#### Set 'full_v2': 96 of DM01's marks (27 where Hua has C's other alternative), 576 requests, \$2.54

<div class="tw">

| Model | Image | Prompt | Marks | Same as DM01 | Different | Abstained | Same as DM01, where Hua has C's other alternative | Cost per mark |
|----|----|----|----|----|----|----|----|----|
| Claude Haiku 5.5 at effort high | the line and the word crop | readings offered | 96 | 61.5 % | 32.3 % | 3.1 % | 16 of 24 | \$0.00036 |
| Claude Haiku 5.5 at effort high | the line and the word crop | free reading | 96 | 22.9 % | 62.5 % | 1.0 % | 7 of 24 | \$0.00041 |
| Claude Sonnet 5.5 at effort medium | the line and the word crop | readings offered | 96 | 62.5 % | 31.2 % | 3.1 % | 15 of 24 | \$0.00390 |
| Claude Sonnet 5.5 at effort medium | the line and the word crop | free reading | 96 | 30.2 % | 54.2 % | 0.0 % | 8 of 24 | \$0.00390 |
| Claude Opus 5.5 at effort high | the line and the word crop | readings offered | 96 | 64.6 % | 29.2 % | 0.0 % | 17 of 24 | \$0.00903 |
| Claude Opus 5.5 at effort high | the line and the word crop | free reading | 96 | 44.8 % | 40.6 % | 2.1 % | 17 of 24 | \$0.00890 |

</div>

#### Set 'full_v3': 96 of DM01's marks (27 where Hua has C's other alternative), 96 requests, \$0.35

<div class="tw">

| Model | Image | Prompt | Marks | Same as DM01 | Different | Abstained | Same as DM01, where Hua has C's other alternative | Cost per mark |
|----|----|----|----|----|----|----|----|----|
| Claude Haiku 5.5 at effort max | the line and the word crop | readings offered | 96 | 18.8 % | 4.2 % | 0.0 % | 8 of 24 | \$0.00362 |

</div>

#### Set 'small': 10 of DM01's marks (5 where Hua has C's other alternative), 120 requests, \$0.44

<div class="tw">

| Model | Image | Prompt | Marks | Same as DM01 | Different | Abstained | Same as DM01, where Hua has C's other alternative | Cost per mark |
|----|----|----|----|----|----|----|----|----|
| Claude Haiku 5.5 at effort medium | the word crop | readings offered | 10 | 70.0 % | 20.0 % | 10.0 % | 4 of 5 | \$0.00026 |
| Claude Haiku 5.5 at effort medium | the word crop | free reading | 10 | 10.0 % | 80.0 % | 0.0 % | 1 of 5 | \$0.00034 |
| Claude Haiku 5.5 at effort medium | the line | readings offered | 10 | 40.0 % | 50.0 % | 10.0 % | 3 of 5 | \$0.00022 |
| Claude Haiku 5.5 at effort medium | the line | free reading | 10 | 10.0 % | 80.0 % | 0.0 % | 1 of 5 | \$0.00023 |
| Claude Sonnet 5.5 at effort medium | the word crop | readings offered | 10 | 60.0 % | 30.0 % | 10.0 % | 3 of 5 | \$0.00386 |
| Claude Sonnet 5.5 at effort medium | the word crop | free reading | 10 | 10.0 % | 80.0 % | 0.0 % | 1 of 5 | \$0.00386 |
| Claude Sonnet 5.5 at effort medium | the line | readings offered | 10 | 40.0 % | 40.0 % | 20.0 % | 3 of 5 | \$0.00273 |
| Claude Sonnet 5.5 at effort medium | the line | free reading | 10 | 30.0 % | 60.0 % | 0.0 % | 2 of 5 | \$0.00297 |
| Claude Opus 5.5 at effort high | the word crop | readings offered | 10 | 50.0 % | 40.0 % | 10.0 % | 2 of 5 | \$0.00811 |
| Claude Opus 5.5 at effort high | the word crop | free reading | 10 | 50.0 % | 40.0 % | 0.0 % | 4 of 5 | \$0.00931 |
| Claude Opus 5.5 at effort high | the line | readings offered | 10 | 50.0 % | 30.0 % | 20.0 % | 3 of 5 | \$0.00580 |
| Claude Opus 5.5 at effort high | the line | free reading | 10 | 40.0 % | 50.0 % | 0.0 % | 3 of 5 | \$0.00628 |

</div>

#### Set 'sol_full': 96 of DM01's marks (27 where Hua has C's other alternative), 192 requests, \$0.57

<div class="tw">

| Model | Image | Prompt | Marks | Same as DM01 | Different | Abstained | Same as DM01, where Hua has C's other alternative | Cost per mark |
|----|----|----|----|----|----|----|----|----|
| GPT-6.2 Sol at reasoning effort medium | the line and the word crop | readings offered | 96 | 80.2 % | 14.6 % | 2.1 % | 21 of 24 | \$0.00220 |
| GPT-6.2 Sol at reasoning effort high | the line and the word crop | readings offered | 96 | 82.3 % | 13.5 % | 1.0 % | 21 of 24 | \$0.00379 |

</div>

#### Set 'sol_small': 10 of DM01's marks (5 where Hua has C's other alternative), 30 requests, \$0.15

<div class="tw">

| Model | Image | Prompt | Marks | Same as DM01 | Different | Abstained | Same as DM01, where Hua has C's other alternative | Cost per mark |
|----|----|----|----|----|----|----|----|----|
| GPT-6.2 Sol at reasoning effort medium | the line and the word crop | readings offered | 10 | 70.0 % | 30.0 % | 0.0 % | 4 of 5 | \$0.00178 |
| GPT-6.2 Sol at reasoning effort high | the line and the word crop | readings offered | 10 | 80.0 % | 20.0 % | 0.0 % | 5 of 5 | \$0.00278 |
| GPT-6.2 Sol at reasoning effort max | the line and the word crop | readings offered | 10 | 90.0 % | 10.0 % | 0.0 % | 5 of 5 | \$0.01052 |

</div>

#### What the sets show (20 Nov 2026)

- **Offering the readings works; asking for a free reading does not.** With the readings offered (in random order, no witness named), the three Claude models agree with DM01 on 59 to 62 of the 96 marks of set full_v2. Asked for a free reading, they agree on 22 to 43: they often read a neighbouring word, because the text around ⟦?⟧ alone does not locate the place in the image. Sending the whole line together with the magnified crop raised the free readings (Claude Opus 5.5 at effort high: 43 of 96) but left them well below the offered readings.
- **The magnified word beats the line** for the cheaper models (set small: Claude Haiku 5.5 7 against 4 of 10, Claude Sonnet 5.5 6 against 4); Claude Opus 5.5 read both equally (5 and 5).
- **DM01 is not a reliable reference where Hua has C's other alternative.** The main session (Claude Opus 5.5 at effort max) checked the 9 contested marks of that class on the crops and against the mathematics around them (full_v2/ADJUDICATION.tsv). Hua's alternative was right at 6 of the 7 it could decide. DM01 had kept C's reading at 4 of those 6: u (the formula is u ↦ Λ<sup>n</sup>u), t, + (the same expression reads 1+A further on) and p (α<sub>p</sub>(\|u\|) α<sub>n−p</sub>(\|v\|)). DM01 and C are both GPT-6 Astra, so their agreement there is not independent evidence. Claude Opus 5.5 at effort high matched the checked reading at 6 of the 7, Claude Sonnet 5.5 at 4, Claude Haiku 5.5 at 2. The checker is itself a Claude model; the mathematical checks are the independent part of this evidence.
- **GPT-6.2 Sol** (OpenAI Batch API, half price; readings offered, both images) agreed with DM01 on 77 of the 96 marks at reasoning effort medium (\$0.0022 a mark) and 79 at high (\$0.0038), against 59 to 62 for the Claude models; on 10 of the marks, 9 at max (\$0.0105). Sol, DM01 and C are all OpenAI models, so some of that agreement may be shared blind spots. On the 7 hand-checked contested marks, the checked reading was matched by Claude Opus 5.5 at effort high at 6, GPT-6.2 Sol at medium at 5, Sol at high and Claude Sonnet 5.5 at 4, Claude Haiku 5.5 at 2.
- **Claude Haiku 5.5 at effort max** (set full_v3) answered only 22 of the 96 marks: on 74 it used its whole 16,000-token allowance thinking and gave no answer. It was dropped.
- **Cost per mark** through the Message Batches API at half price: Claude Haiku 5.5 about \$0.0004, Claude Sonnet 5.5 about \$0.004, Claude Opus 5.5 about \$0.009. For the 70,502 live-text marks not yet checked that is about \$25, \$275 and \$635; for the 6,068 open marks where Hua has C's other alternative, about \$2, \$24 and \$55.

</div>

<div id="ways" class="section">

## 8. Every way suggested to settle the doubt marks

Each way, who proposed it and when, how far it has gone, and what this report measured for it.

<div class="tw">

| Way | Suggested | State | What it reached (measured here) | Cost |
|----|----|----|----|----|
| Settle C's doubt marks in a full second pass by Claude agents, one block of 15-18 scans each | 13 Nov plan | run 13 Nov: 887 pages | settled 10.4 % of C's marks on 808 pages; first reading wrong 39.3 % where settled | about 0.03-0.05 % of the weekly Claude usage limit a scan |
| Pro second pass, one reader per piece, settling C's marks among everything else | 14 Nov plan | SP02-SP33 run | settled 42.1 % (large pieces) and 32.8 % (pieces of 19 Nov) | Pro run-hours (flat plan) |
| Pro three readers and a main reader | 19 Nov ~20:26 UTC | SP34 run; in the pieces SP35-SP57 | settled 34.0 % on 8 pages so far | 5-7 pages an hour |
| The reading workflow: page once, halves once, list what is open, one tight crop per open place | 19 Nov 21:07 UTC | SP35 on; in SP36-SP57 | SP35 settled 36.2 % on 8 pages | Pro run-hours |
| Deep zoom and fresh readers per page | 19 Nov 21:10-21:11 UTC | SP36-SP62 (14 of them back) | settled 29.0 % on 62 pages so far | Pro run-hours |
| A long Pro run on the doubt marks only, designing its own workflow | 19 Nov 21:58 UTC | DM01 ended at checkpoint 10, 20 Nov 05:37 UTC (cote 1, 67 pages); DM06 takes the rest | settled 45.8 %; 196 marks an hour; 11 errors outside the marks | Pro run-hours |
| Hua's text as the pointer: settle first the marks where Hua has the other alternative | the fix lists, 19 Nov 21:58 UTC | listed (STATE/DOUBTS_VS_HUA.tsv); positional list in this report | where Hua had the other alternative, the passes chose it 18.2 % of the time (274 marks); 6,070 such open marks | a targeted check per mark |
| Diff C against Hua and check only the differences (pilot F) | 19 Nov | pilot F run; in the pieces as witness H | 39.6 % of the logged corrections were at such places; F agreed with SP04 at 84.0 % | about 0.014 % of the weekly Claude usage limit a page (F) |
| Give the pieces the lists as places to check first (doubt marks, Hua disagreements, his-error claims, sweep rows) | our proposal, 19 Nov | witness C's doubt marks and witness S are in the pieces; the his-error list is not | the cheap lists point at 82.7 % of the logged corrections | script edit, free |
| Check the listed places through the batch APIs, each image once (pilot G) | 19 Nov | not run | not measured | API dollars (Batch only) |
| Claude agents reading whole pages (pilots A-E) | 19 Nov 20:31 UTC | stopped 21:00 UTC | on SP35's pages they settled far fewer of C's marks than SP35 (section 7) | 0.15-0.5 % of the weekly Claude usage limit a page |
| A fresh Work reading (GPT-6.2 Astra at reasoning effort max) and a diff | 18 Nov plan | 229 folders built, held | not measured | about 286 Work-hours |
| Work correcting the first reading against the scan | 19 Nov | needs a pilot | not measured | Work time |
| Script checks of the first readers' recurring misreadings across the archive | DM01's PATTERNS.md (the DM design) | 158 patterns so far, none applied | not measured | script, free |
| A local open-weights model trained on our errors and their fixes, on a local GPU | 19 Nov 22:57 UTC | an idea; not built | not measured | GPU time |

</div>

</div>

<div id="intakes" class="section">

## 9. The intakes: what each return did

The returns themselves are the pilots: each design ran on real pages, and each recorded its own method. Their intake (each return's workflow file, README and progress log, with the measurements of this report) is in `INTAKES_20261120.md`. A run whose newest return is 3 hours old or more counts as ended (20 Nov).

Split by where the mark sits, the doubt-marks-only run settles by far the most live-text marks, and struck-out text resists every design:

<div class="tw">

| Run | Newest return | Pages done | Live-text marks | settled | first reading wrong | Struck-text marks | settled | first reading wrong |
|----|----|----|----|----|----|----|----|----|
| DM01 | checkpoint_10 | 67 | 588 | 67.5 % | 16.4 % | 857 | 30.9 % | 10.6 % |
| SP02 | checkpoint_23 | 106 | 471 | 30.1 % | 37.3 % | 435 | 34.3 % | 18.1 % |
| SP04 | checkpoint_05 | 63 | 781 | 58.8 % | 11.3 % | 540 | 34.6 % | 5.3 % |
| SP12 | checkpoint_11 | 59 | 530 | 55.1 % | 20.5 % | 466 | 27.7 % | 11.6 % |
| SP14 | checkpoint_13 | 100 | 950 | 51.5 % | 15.3 % | 509 | 24.0 % | 8.2 % |
| SP31 | final | 24 | 301 | 49.5 % | 14.1 % | 224 | 12.9 % | 13.8 % |
| SP32 | final | 16 | 173 | 52.0 % | 7.8 % | 139 | 25.9 % | 8.3 % |
| SP33 | final | 24 | 281 | 38.1 % | 6.5 % | 234 | 13.7 % | 3.1 % |
| SP34 | checkpoint_03 | 8 | 88 | 43.2 % | 7.9 % | 71 | 22.5 % | 18.8 % |
| SP35 | final | 8 | 113 | 46.9 % | 11.3 % | 83 | 21.7 % | 16.7 % |
| SP36 | checkpoint_01 | 3 | 28 | 53.6 % | 0.0 % | 10 | 20.0 % | 0.0 % |
| SP37 | checkpoint_01 | 2 | 27 | 33.3 % | 11.1 % | 10 | 0.0 % | – |
| SP38 | checkpoint_08 | 14 | 140 | 30.0 % | 11.9 % | 79 | 12.7 % | 20.0 % |
| SP39 | checkpoint_01 | 2 | 30 | 46.7 % | 7.1 % | 12 | 25.0 % | 0.0 % |
| SP40 | checkpoint_01 | 2 | 18 | 55.6 % | 10.0 % | 10 | 20.0 % | 50.0 % |
| SP41 | checkpoint_01 | 2 | 52 | 55.8 % | 10.3 % | 19 | 26.3 % | 20.0 % |
| SP44 | checkpoint_01 | 2 | 8 | 0.0 % | – | 10 | 0.0 % | – |
| SP45 | checkpoint_01 | 6 | 19 | 36.8 % | 14.3 % | 4 | 75.0 % | 0.0 % |
| SP46 | checkpoint_01 | 2 | 20 | 20.0 % | 25.0 % | 2 | 50.0 % | 100.0 % |
| SP47 | checkpoint_01 | 2 | 12 | 8.3 % | 0.0 % | 20 | 40.0 % | 12.5 % |
| SP48 | checkpoint_01 | 1 | 5 | 60.0 % | 33.3 % | 4 | 25.0 % | 100.0 % |
| SP49 | checkpoint_01 | 6 | 13 | 76.9 % | 0.0 % | 6 | 33.3 % | 0.0 % |
| SP50 | checkpoint_01 | 3 | 25 | 32.0 % | 0.0 % | 4 | 0.0 % | – |
| SP57 | checkpoint_09 | 15 | 89 | 33.7 % | 46.7 % | 115 | 8.7 % | 40.0 % |
| CLAUDE13 | 13 Nov blocks | 777 | 4,645 | 15.1 % | 38.9 % | 2,717 | 2.5 % | 43.3 % |

</div>

</div>

<div id="next" class="section">

## 10. Next steps

These follow from the measurements above. None is done yet.

1.  **Mark a checked doubt in the text itself** (a change of convention, not yet decided). Today `\unsure{a|b}` means both "not yet checked" and "checked, still doubtful": the split in section 1 is inferred from where a page's text of record came from, and is lost once pages are merged or edited. Proposal: an optional argument naming the check, `\unsure[DM01]{a|b}` ("DM01 looked at this place on the scan and could not decide"), written by every second pass and doubt-mark run on each mark it leaves; a mark without it has not been checked. The preamble's definition becomes `\newcommand{\unsure}[2][]{...}`, so every existing text compiles unchanged, and the readers can show checked doubts in their own colour; the scripts (alignment, inventory, STATE) read the argument. Alternatives: a new command such as `\doubtful{...}` (does not say who checked), or the decisions kept only in each run's `MARKS.tsv` (no change to the text, but the link to the mark breaks when the page is edited).
2.  **Decide who is right where Hua has the other alternative** (approved, 20 Nov). Where they settled such a mark, the Pro passes kept C at 69.7 %; the 13 Nov Claude pass went with Hua at 69.6 % (48 of 69). A scan check of a random sample of these marks (60-100 of the 6,070 open ones, a doubt-marks run like DM01 or pilot G on the batch APIs) would say which, and so how to treat the whole class.
3.  **Struck-out text** (decided 20 Nov: live-text marks first, struck-out text after). 55,116 of the open marks (43.0 %) are inside deletions. Every pass settles them at 16-60 % of the rate of live text, and DM01 left 573 of its 765 undecided marks there. The prompts could let a reader keep a doubt in struck text after one look (DM01's stopping rule) and spend the time on live text.
4.  **Carry DM01's own methods into the next DM prompts** (shared band crops, the stopping rule, a page's marks split by their number), and Pro's SP34/SP35 inventions (per-reader records, decisions applied by script) into the unsent pieces, if wanted: a script edit of the prompts.
5.  **The pages of the 13 Nov Claude pass no longer count as second-passed** (decided 20 Nov): 89.6 % of C's marks on them are still open (8,199 marks on 851 pages). A doubt-marks run on those pages would settle them.
6.  **Test deep zoom properly** (approved, cheaply, 20 Nov): the same pages read twice by the same design, crops capped at 2-3x against tight crops at 8-10x, scored mark by mark (section 4).

</div>

<div id="method" class="section">

## 11. Method, data and limits

- **Scripts** (in `reports_20261120/doubt_marks/scripts/`): `texalign.py` (tokens, marks, alignment), `dm_followup.py` (the second passes), `dm_inventory.py` (the open marks), `pilots_vs_sp35.py`, `hua_offsets.py`, `build_report.py` (this page). Data in `data/`: `marks.tsv` (one row per mark of C on a finished page), `pages.tsv`, `runs.json`, `inventory_marks.tsv` (one row per open mark), `inventory_pages.tsv`, `dm01_check.tsv`, `pilots_vs_sp35.tsv`, `hua_offsets.tsv`.
- **Validated** against DM01's own decisions: 1407 of 1447 marks classified the same way.
- **Mathematics** is decided by the delimiters before a mark. Fixed on 20 Nov: a delimiter counts only after an even run of backslashes, so the line break with spacing `\\[2pt]` (1,025 times on 582 pages) no longer opens a display, and `$$...$$` counts as a display. Before the fix, marks after such a line break counted as mathematics; every count on this page uses the fixed rule.
- **Not measured:** whether a pass's reading is right. That needs the scan at the places where readings disagree, or a reference text.
- **Hua's conventions** differ from ours in places, so exact agreement with Hua is undercounted.
- **Small samples:** SP34-SP37 and DM01 have 88 finished pages between them.
- **Pages an hour** come from each run's progress.log and include its reading of the research notes where the prompt asks for them.

</div>
