# Direct publication check: Brauer III §8

**19 November 2026, 13:47 UTC.** Root downloaded the primary scanned *Dix exposés* volume from the Grothendieck Circle. Its text layer was empty. This worker rendered PDF pages 117–126 (printed pp.143–152), read their OCR, and visually inspected printed pp.146,148,150,151. These are **published-book images**, not the unavailable Montpellier manuscript scans. No manuscript reading was adjudicated.

The exact local hypotheses omitted from cote16/19 are on printed p.148: a complete normal local ring A of dimension two, algebraically closed residue field k, a chosen coefficient field k⊂A, and a proper birational regular resolution isomorphic away from the closed point. The local Picard construction is cited to SGA2 XIII §5. Printed p.149 matches the exceptional-lattice cokernel and discriminant self-duality in cote16/19.

Printed p.145 matches cote16/21, equation (8.7), with the finite-generation/divisibility and finite-cohomology assumptions. Printed p.146 matches cote16/23. The printed finite-Brauer-quotient formulas also suppress the ell-primary qualifier; this qualification is therefore not a new guess about handwritten ink.

Printed p.150 asks for verification that the two terms in the Kummer/NS sequences annihilate one another and that the induced quotient pairing equals the exceptional-lattice pairing (8.16). Printed p.151, Remark 8.5, says **“Le rédacteur avoue qu'il ne l'a pas faite”**. This is explicit evidence that the published argument retains the comparison gap. It initially assumes characteristic zero for local duality and points to cohomological purity as the then unresolved obstacle to removing that restriction. It also proposes the case of non-algebraically-closed residue fields, including finite fields.

The publication does **not** by itself settle the compatibility question. This run does not infer that the theorem remains open today: its exact later fate requires a later proof matching the pairing maps, twists and signs. The independently checked inverse-matrix pairing and blowup congruence are strictly separate.

Executable reading record: `scripts/ocr_primary.py`. OCR and page images: `research/primary_pages/DixExp/page_117` through `page_126` (txt/png). The downloaded primary PDF belongs to root's research folder and need not be duplicated in this worker folder.
