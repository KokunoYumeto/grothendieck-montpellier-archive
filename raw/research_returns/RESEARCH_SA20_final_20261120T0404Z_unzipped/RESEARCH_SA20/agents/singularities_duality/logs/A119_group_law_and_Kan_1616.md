# A.119 audit additions, 2026-11-19 16:16 UTC

This note is separate from the included manuscript during checkpoint07 freeze. The existing A119_draft.tex retains its n >= 9 scope. Replace its unsupported short group-law sentence by the argument below after freeze. Also replace `\N` by `\mathbb N` in that draft: the shared preamble does not define `\N`.

## Composition is the group law computed by the cycle presentation

For a simplicial group C, the natural isomorphism pi_0 C -> pi_1 BC sends a component represented by g to its bar edge. The bar 2-simplex (g,h) identifies the product edge with the concatenated edges. Choose the bar convention in which this identifies the given order of composition; the opposite convention differs by inversion and gives the same final abelian group.

Waldhausen--Jahren--Rognes, 166-page author PDF, Remark 1.1.11 and (1.1.12), printed p.12, identify the component of the trivial h-cobordism in H(M) with BC(M). They do this through the actual simplicial automorphism group CAT(M x I rel M x 0), into which the side-fixed concordance group C(M) includes by a group homomorphism and weak equivalence. Thus

    pi_0 C(M) -> pi_1 BC(M) -> pi_1 H(M)_0

is an isomorphism of groups, with the left side carrying ordinary composition. The stabilization functor sends W to W x J and each automorphism g to g x id_J; it preserves composition. Consequently these isomorphisms are compatible with stabilization on components (even if one realizes the side-fixed stabilization only after the usual boundary adjustment).

Take the direct limit of these group isomorphisms. The simplicial stabilization maps for H are cofibrations, by WJR Definition 1.1.3, printed p.8, so pi_1 of their colimit is the direct limit of pi_1. Applying pi_1 to the based stable h-cobordism equivalence of WJR Theorem 0.1 yields

    colim_k pi_0 C(M x J^k)
      = pi_1 H^st(M)_0
      = pi_1 Omega Wh^Diff(M)
      = pi_2 Wh^Diff(M)

as groups. A based weak equivalence always induces a homomorphism on pi_1. No preservation of an unlooped H-space multiplication is being presumed. The subsequent maps induced by the split unit and by Hurewicz are homomorphisms. Therefore ordinary pseudo-isotopy composition is precisely the addition of cycle classes in A.119.3.

Opened source: https://www.mn.uio.no/math/personer/vit/rognes/papers/plmf.pdf . Current-version tool refs turn904108561view0 (full), turn870041195view1 and turn870041195view2 (Remark 1.1.11, p.12), turn914762336view1 (Theorem 1.4.1, p.21 and delooping statement immediately following). Root independently opened p.12 and agrees.

## Explicit Kan-loop-group data

Let X be the reduced finite simplicial set obtained by collapsing a maximal tree of K. Define

    G(X)_n = F(X_{n+1}) / < [s_0 x] = 1 : x in X_n >.

The face and degeneracy homomorphisms on generators are

    d_0[x] = [d_1 x] [d_0 x]^{-1},
    d_i[x] = [d_{i+1} x]       (i > 0),
    s_i[x] = [s_{i+1} x].

All are extended multiplicatively to words. The displayed s_0 relations are respected; the simplicial identities follow from the identities in X (the only nontrivial cancellation in d_0d_0=d_0d_1 uses d_0d_1=d_0d_0 in X). This is the convention of Goerss--Jardine, V.5, (5.1), printed p.276. Their formula for arbitrary ordinal maps simultaneously proves functoriality. The loop-group theorem in that section identifies BG(X) with X for reduced X; hence the construction is the required loop model.

Opened book: Paul G. Goerss and John F. Jardine, Simplicial Homotopy Theory, original 1999, uncorrected Modern Birkhaeuser Classics reprint 2009. https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Goerss-Jardine2.pdf . Tool refs turn870041195view0 (full) and turn914762336view0 (V.5 pp.275--279). Exact formula (5.1), p.276. Add the book bibliography entry only after checkpoint release.
