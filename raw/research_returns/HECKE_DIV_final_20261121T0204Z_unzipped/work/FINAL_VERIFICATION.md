# Final document verification

Run: HECKE_DIV_20261121. Recorded 2026-11-21T02:03:56.379638+00:00.

The complete mathematical reading and independent checks are recorded in CHECK_EVENTS.tsv. The final extension R24E–R24F was independently re-proved and fully read after the earlier integration audit; the earlier audit hashes identify that earlier source state. Later layout and locator changes do not silently replace those historical hashes.

The current paper has 54 pages and 39 explicit proof environments, with additional fully checked proofs embedded in numbered finding paragraphs. Nine source modules were flattened. The clean build used three pdfTeX passes and ended without warnings or overfull boxes. All 54 final pages were rendered and visually inspected. These are document checks, not formal mathematical certificates.

## Final document hashes

```text
feac90dcdcc86cf414ea36fb2105305ef3dfa112a04f846c26815bf2b5323bc1  HECKE_DIV.tex
1d45f7bc5bd91b4fc0ea4205c71bfb9558ab43a96538b365fee60d0c4a75534c  HECKE_DIV.pdf
b2323f64e281cb6c399fac987b8ee92ee973d59d38802460fec7d340cd89702a  source_tex/HECKE_DIV.tex
5bcd24711a3c4833c2559efc8033c4d43598ed3af77b7f88d9b949499ff5be09  source_tex/archive_section.tex
6ba9ecbaf3b6d16f7eefe248e61ffaa28cb78fa6946ac8389a6278a25a2b255b  source_tex/eightfold_quantitative.tex
7a5fa8695718eb70af598949bbdea6e235ddbe7df97d786c519aa9b664d603cf  source_tex/integral_seeds.tex
54d2f1035c83fb454ee456f76fe06d1c183cb48e21d7aafccb04c106466b6769  source_tex/markman_quantitative.tex
64205d2bd47358a590e3462a22ad6393fd05cae5ade0161031d7f4563655b661  source_tex/open_and_bibliography.tex
07a163259e510668c121047041ab3c493881664adb40441aa2480e6ff3bfe220  source_tex/prime_section.tex
a5441046794fd3c21f592fb4423581e17d84893f20b7e8a3cdf9a28d3e7d5e9f  source_tex/regularity_section.tex
9bb9d6c42675a6a96c0ded89ae00c8291e3bd38d4621dcdac870a62a5091f50d  source_tex/sections_remaining.tex
```

The final archive's MANIFEST.sha256 separately covers all delivered files. The original twelve-input checksums remain in SOURCE_MANIFEST.tsv. No earlier checkpoint archive is included.
