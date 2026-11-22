# Memoir spectral continuity: alternative route audit

2026-11-20 UTC. Independent requested check by `crystalline_categories`.

Source actually inspected: `notes/geometry_PTT_1966_scan.pdf`, 382-page scan,
fourth printing1966 of the memoir first published1955. SHA256
`85b3ba9324fbadcd41c55090a20e7fdf3e886318c838aff2311ea78755ea2802`.
Public source URL: https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/PTT.pdf .
This note records its own printing, without inventing a requirement to collate
all printings. Page images and render commands are preserved by
`code/category_memoir_remark4_audit.py` and
`code/category_memoir_continuity_followup.py`, with corresponding logs.

## Exact checked passage

Memoir ChapterII, §1 no4, Remark4 begins on printedp20 (physical221), continues
onp21 (physical222), and ends with two lines onp22 (physical223). All three
pages were directly viewed, not merely OCR-searched.

The notation is consequential. Onp21, Sigma_(p) is the metric space of unordered
sequences with summable p-th powers. The separately defined Sigma_[p] is the
intersection of Sigma_(q) for q>p, the space of order at mostp. The stated
Hilbert continuity theorem has **Sigma_(p)** as target, not Sigma_[p]. It
therefore includes genuine unordered l1 continuity whenp=1.

The text first asserts Banach spectral continuity into Sigma_(r), where
1/r=1/p-1/2. Its proof sketch invokes Theorem1's common representation of
convergent tensor sequences and the reduction used in Proposition1, reducing
the matter to the finer Hilbert continuity assertion. It then states that
Hilbert assertion, supplies no proof of it in the remark, and deduces the
order-at-most analogue. Page22 immediately proceeds to no5 on magnitude.

## Consequence, proved in this audit

The stated Hilbert theorem atp=1 would prove the trace formula immediately.
Take finite-rank T_n converging to T in trace norm. For the unordered spectral
l1 metric d_1, finite-rank trace gives Tr(T_n)=sum(lambda(T_n)), and

  |sum(lambda(T_n))-sum(lambda(T))| <= d_1(lambda(T_n),lambda(T)).

Indeed, for any enumerations padded with zero, the absolute difference of
the two sums is at most the l1 distance; take the infimum over enumerations.
The spectral sums exist because the asserted target is Sigma_(1). Trace-norm
continuity of the trace gives Tr(T_n)→Tr(T), while the asserted spectral
continuity gives the right side→0. Thus Tr(T)=sum(lambda(T)). This is our
explicit implication, not an additional argument printed after Remark4.

## Dependencies and other locations actually inspected

- **II§1 no1, Theorem1, pp5–6** (physical206–207): common tensor
  representations for compact sets/convergent sequences. Read full OCR text
  with its definitions and proof-transfer explanation; it concerns tensor
  representations, not eigenvalue continuity.
- **II§1 no4, p13** (physical214): directly viewed. The memoir explicitly
  recalls the Hilbert eigenvalue p-summability bound, determinant order at mostp,
  and genuszero forp≤1, attributing these to Weyl1949. No proof of those
  Hilbert statements is printed in this introductory paragraph.
- **II§1 no4, Lemma1/Proposition1 and proof, pp14–16** (physical215–217):
  read full OCR text. These factor Banach operators through Hilbert matrices
  and use the recalled Hilbert statements; they do not prove those statements.
- **Appendix to ChapterI, pp194–195** (physical199–200): both directly viewed.
  Grothendieck explains that Hilbert eigenvalue results
  originally intended for reference[11] were removed after he found them
  essentially in Weyl1949, and acknowledges that the old references became
  inadequate. This is explicit evidence about the omission, not an inference
  from keyword counts.
- **II§2 no4, p65** (physical266): read full text and directly viewed. The continuity statement
  for operators on nuclear spaces explicitly uses Remark4; it does not supply
  the missing Hilbert proof.
- **Appended Résumé, p168** (physical378): directly viewed. It repeats Banach
  spectral continuity as a further assertion after the two-thirds trace
  corollary, without proving Hilbert trace-class continuity.

## Correct source-critical conclusion

The memoir does print a full Hilbert genuszero **statement** and a second
spectral-continuity statement strong enough to imply the full trace formula.
It is inaccurate to say that it contains only a two-thirds trace result.
The checked passages give reductions to Hilbert facts and citations, not a
printed proof of Hilbert l1 spectral continuity. Any claim that a complete
argument is printed must distinguish these assertions/references from their
proofs. Root's separate complete memoir/Weyl audit determines whether a proof
is supplied elsewhere; this targeted audit does not substitute a keyword
search for that whole-source judgment.
