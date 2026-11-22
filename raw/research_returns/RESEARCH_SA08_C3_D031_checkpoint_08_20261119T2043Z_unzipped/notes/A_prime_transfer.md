# AT23: torsion at a new prime after a genuine primary repair

The full proof is in `sections/A_prime_transfer.tex`.

The source has an actual order-p class y in the free even-to-odd complex dx=p y on D(3). Its actual AT14 repair adds du=y and dv=p u−x. The integral PD change x′=x−p u gives a split even identity disk and an odd unit disk. The latter has the exact arity-n differential v γ_(n−1)(x′)↦−n γ_n(x′). This produces order-r cohomology in form2r at weight rw for every prime r.

The construction has actual split target maps to G, unchanged simplex degrees zero and one, horizontal row retractions to G, rational coefficient comparison, and H0/H1 as stated. Since H1 is already zero, the entire based degree-one saturation adds no element. An increasing-weight graded tensor over all odd p retains split detectors for order-two classes in unbounded form-four weights.

The refuted invariant is specifically that a p-primary repair can create only p-primary torsion. A stronger weight reserve may still allow a subsequent r-primary repair at weight rw, and this example does not rule it out. It also does not refute common-source existence or terminality of the localization.

Root and lifting_recheck independently passed the full proof. The independent program code/B_prime_transfer_certificate.py and its JSON log record 144 exact checks, including the complete variable-change matrices and the full arity-two H4 lattice, for p=2,3,5 and arities 0 through 8. Its runtime was 0.09705105099419598 seconds. These finite checks supplement the all-index proof. The standalone two-page syntax build passes without an overfull box.
