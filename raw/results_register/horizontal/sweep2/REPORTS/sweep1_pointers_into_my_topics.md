# The four sweep-1 pointers into SA05 and SA19

Claude Opus 5.5 at effort max (agent a28ea31fa17dd65e1), sweep 2 part 2, 18 Nov 2026. Source: the AUTO section of my
inbox (built by the broad agent's script `_broad_tools/build_global.py`, 18 Nov 15:33 UTC) and the four items' rows in
`sweep1/SA20`, `SA23`, `SA31` OBJECTS.tsv.

| Pointer | The item | Why the script pointed it at my topic | Decision |
|---|---|---|---|
| SA20-10 (H0CI) -> SA05 [cote 12] | are his tame-topology axioms M0-M11 those of an o-minimal structure? (cotes 120-121) | its cross_topic reads "SA20-12/13/15"; "12" was taken for cote 12, which is SA05's | no link: a parse of an item number as a cote |
| SA20-12 (H00K) -> SA05 [cote 13] | the axioms of a tame topology on cote 120 | its cross_topic reads "SA20-13/14/15 (cote 121)"; "13" was taken for cote 13 | no link: same cause |
| SA23-24 (H0DD) -> SA19 [cote 43] | connections on fibre products; regular rings in characteristic p with non-free Omega^1 (cote 23, scans 33-50) | its cross_topic reads "cote 93 (connections, SA23-43/44)"; "43" was taken for cote 43, which is SA19's | no link to SA19; a theme only with SA14-2 (connections on the Picard scheme) and SA15-1 (connections and stratifications) |
| SA31-13 (H0IP) -> SA05 [cote 15] | the maquette of a normal-crossings compactification (cote 149) | its cross_topic reads "SA29-Q4, SA30-15/17"; "15" was taken for cote 15 | no link: same cause |

All four come from one parsing error: an item suffix after a slash or hyphen ("SA20-12/13", "SA23-43/44", "SA30-15/17")
read as a cote number. None of the four objects is on cotes 12, 13, 15 or 43, and none is the same mathematical object as
an item of SA05 or SA19. I add no cross_topic for them; SA23-24's theme link (connections) is noted in the introduction
of SA14's WHAT_IS_WHERE.md as a theme only, with no dependency. For the broad agent: the script's cote pattern should not match digits that follow
"SA<nn>-" or a slash.
