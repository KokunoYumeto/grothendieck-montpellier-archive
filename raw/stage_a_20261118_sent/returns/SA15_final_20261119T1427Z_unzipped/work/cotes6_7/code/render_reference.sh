#!/bin/sh
# Used to inspect the scanned primary theorem, PDF pages 1–3.
pdftoppm -f 1 -l 3 -scale-to 1600 -png work/cotes6_7/outputs/lenstra_oort1974.pdf work/cotes6_7/outputs/lenstra_oort1974
