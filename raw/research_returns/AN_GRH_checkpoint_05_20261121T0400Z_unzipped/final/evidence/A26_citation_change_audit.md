# A26: narrow final citation and split-fibre check

- Date: 2026-11-21.
- Reviewer: GPT-6 Astra Pro; reasoning effort not exposed; `/root/effective_galois`.
- Reviewed predecessor: `work/row_audit/A26_PREVIOUS_REVIEWED.tex`, SHA256 `8b780159d97aaaa3f64574cf4c306b0b85a2498b06b1305a4568c4467a9e3831`.
- Final source: `work/row_audit/A26_RANK_ONE_AUGMENTATION.tex`, SHA256 `e1985e61154e2eccab66a6e4a0cff1784c3d2dbb6700930326f1e330d2529bed`.
- Supplied exact diff: `work/row_audit/A26_CITATION_ONLY.patch`.
- Outcome: **PASS** for the narrow change.

The only changed paragraph replaces an implicit connectedness attribution to recovered A1 B.2 by an explicit invocation of A12's connected Lang-pullback argument, and spells out why the zero point in the fibre over [P-P]=0 makes the prescribed fibre split. I verified the exact predecessor and final hashes and read the complete final A26 text for context.

A12's proof of connectedness applies to the ordinary Abel embedding based at the rational point P, with translation zero. A quotient of the Lang isogeny has constant kernel G/H. Its zero point is rational and lies over zero; translation by each point of that constant kernel makes every point in that fibre rational. Thus the new paragraph supplies precisely the geometric connectedness and P-splitting assertions needed by A26.

I also read the complete recovered A1 B.1–B.3 block, including B.2's effective-divisor character criterion, so the unchanged use of B.2 immediately before the altered paragraph is consistent with the new attribution. This event does not substitute a new claim for the prior independent whole-proof review by `/root/gt_certificates`; it records the requested final-diff check.

No mathematical hypothesis, inequality, conclusion, or subsequent Fourier argument changed. No final or build files were edited.
