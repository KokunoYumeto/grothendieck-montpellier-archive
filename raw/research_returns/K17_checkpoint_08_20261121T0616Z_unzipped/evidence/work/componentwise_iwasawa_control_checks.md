# K17-COMPONENT-CONTROL: author whole-proof check

Date: 2026-11-21. Model: GPT-6 Astra Pro, run `/root/archive_kummer`.

**Author verdict: PASS, pending the requested independent root/tripod reviews.** The new consequence is conditional only on the already stated K-group/source inputs; the componentwise control proposition itself is classical and unconditional.

Reviewed the entire saved TeX and bibliography after writing them. TeX SHA-256: `b3ae47959cdbf1169dfe8dc3d0daf478c49038844daba505e2ceaabb30daad97`. Bibliography SHA-256: `46ceda04e0fbb979088089ae4de905881551d141881a1fd1bf446e983702d7eb`.

## Actual source reads

- Freshly read Sharifi, complete *Iwasawa Theory* PDF/text, Proposition 1.3.11 and its complete class-field proof, Corollaries 1.3.9 and 1.3.12, pp.17–18. Also read Theorem 1.3.16 and the relevant complete Proposition 3.2.11 proof, equation (3.2.1), and Remark 3.2.12, pp.80–81. Local source: `work/sharifi_full_iwasawa.pdf/.txt`; primary PDF: `https://www.math.ucla.edu/~sharifi/iwasawa.pdf`.
- Freshly opened the author's current Chapter 3 web version and found the exact Remark 3.2.12 statement at lines226–228: `https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch03.html`, retrieved reference `turn519620774view0`.
- Freshly read the entire Wake–Wang-Erickson ordinary paper setup §2.1 and Proposition2.2.6 with its complete proof, pp.2–4, in `work/wake_wang_erickson_ordinary.txt`. Checked theta even/nontrivial/primitive and not omega², chi=omega^-1 theta, and that the left module is fraktur X (p-ramified). The Tate twist and involution are both defined in that setup.
- Reread the earlier independently audited exceptional-character Coleman/Stickelberger paragraph of `work/greenberg_kernel_section.tex`. Its exceptional calculation is unconditional; it does not import Greenberg for the omega or omega^-1 component.
- Reread (K2), the zero trivial character proof, and the final nine-degree corollary supplying the finite base classes.

## Reconstruction

The finite norm map `(A_n)_{G_n} -> A_0` is an isomorphism because there is only one ramified prime and its inertia is all of the cyclic group G_n. The complete class-field proof is repeated in the TeX: cyclicity identifies the maximal abelian-over-base quotient with coinvariants, and the unique inertia subgroup supplies an actual direct complement. Its fixed field is exactly the base Hilbert p-class field.

The norm map is Delta-equivariant. Teichmuller Delta commutes with G_n, and p-1 is invertible over Z_p, so integral character projection commutes with coinvariants. Thus there is no character mixing. Vanishing of the coinvariants of a finite component forces its mod-p quotient V to satisfy both `V=(sigma-1)V` and `(sigma-1)^(p^n)V=0`; consequently V=0 and the whole finite p-group is zero. This proves vanishing separately at every layer and avoids any lim^1, infinite-level control kernel, or capitulation assumption.

The exact reflected character is `omega theta^-1`; setting theta=omega^(-2j) gives `omega^(2j+1)`. WWE gives integral rank-one freeness after the indicated ring automorphisms, hence integral rank-one freeness before them. In particular the entire Lambda-torsion component vanishes, a stronger statement than merely nonvanishing of a cubic residue.

## Precise scope

For all odd p, the new class conclusion is `A_n^[-2j]=X^[-2j]=0` for every n and j=0,...,9. For p>=5 the matching p-ramified odd components are integrally free of rank one, including exceptional residues by the earlier explicit calculation. This removes those characters from the actual odd companion list in the cubic theorem. Remaining characters and their actual Triple-NV condition are unchanged. No proof of Greenberg at a new entire prime, no ordinary triple-Massey identification, and no new numerical calculation is claimed.
