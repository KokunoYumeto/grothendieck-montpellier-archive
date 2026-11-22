# Visual PDF verification

Second scheduled checkpoint, 20 November 2026. We rendered and visually inspected pages 1, 20, 40, 60, 76 of the 76-page current PDF. Body text, formulas, headings and bibliography fit the page; no clipping or overlaps were found. The final build had zero warnings and zero overfull boxes (0 exceeding 2pt, maximum 0pt). Before/after counts in both checkpoint builds were 0/0; no overflow pages required separate rendering.

PDF SHA256: 3c1ae59fcdbbd1e28f9a3f37b513d40a99f428412abc0464503999de39c570ca

Inspection completed 2026-11-20T01:42:41.953890+00:00.


## Third scheduled checkpoint

Completed 2026-11-20T02:27:10.155221+00:00. We rendered and directly inspected pages 1, 20, 40,
60 and 82 of the 82-page PDF. Headings, body text, mathematical displays,
footers and bibliography fit their pages, without clipping or overlap.
PDF SHA256: 4fa8689f698d0f8f45bc62834c2164860bcd07bda491f541473a733eb29b9af9.

The first attempt had one fatal bibliography typesetting error from two
unescaped underscores in agent names, and zero overfull boxes. We replaced
those metadata names by plain prose and rebuilt through LuaLaTeX/BibTeX/
LuaLaTeX/LuaLaTeX. All four commands returned zero. The successful build
had zero warnings, zero overfull boxes, zero overflows above 2pt, and a
maximum overflow of 0pt. Thus overfull counts before/after were 0/0;
there were no overflow pages requiring separate inspection. The failed
attempt's diagnostic and log are preserved under distinct names.
