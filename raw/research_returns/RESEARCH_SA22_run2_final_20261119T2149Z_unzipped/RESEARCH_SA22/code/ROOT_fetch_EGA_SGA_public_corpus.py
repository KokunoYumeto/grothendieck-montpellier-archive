#!/usr/bin/env python3
"""Read the independently discovered public repository's original-volume files."""
from ROOT_fetch_ring_sources import main
main([
 ('ROOT_EGAI_newedition.pdf', 'https://raw.githubusercontent.com/xhc144/algebraic-geometry-corpus/5e1bb75b9be3670f883e24e61ba77424344eb8be/EGA/EGA-1-Le-langage-des-schemas.pdf'),
 ('ROOT_SGA7I.pdf','https://raw.githubusercontent.com/xhc144/algebraic-geometry-corpus/main/SGA/SGA-7-1-Groupes-de-monodromie.pdf'),
], 'ROOT_EGA_SGA_public_corpus_fetch.json',
 'Read original-volume scans from independently discovered public GitHub corpus; verify edition, exact pages and typography before importing any claim. This is not an authentication or format workaround for the failed other hosts.')
