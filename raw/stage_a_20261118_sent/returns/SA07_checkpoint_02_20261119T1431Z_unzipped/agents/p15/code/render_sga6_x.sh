#!/bin/sh
set -eu
pdftoppm -f 589 -l 598 -r 90 -png agents/p15/evidence/SGA6_original.pdf agents/p15/evidence/pdf_pages/SGA6X
pdftoppm -f 577 -l 586 -r 100 -png agents/p15/evidence/SGA6_original.pdf agents/p15/evidence/pdf_pages/SGA6X
pdftoppm -f 587 -l 588 -r 120 -png agents/p15/evidence/SGA6_original.pdf agents/p15/evidence/pdf_pages/SGA6X
