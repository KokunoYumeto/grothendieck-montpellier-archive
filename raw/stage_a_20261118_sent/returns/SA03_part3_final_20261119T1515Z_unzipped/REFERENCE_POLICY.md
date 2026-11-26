# Reference and verification policy

The bibliography records works, not proof certificates. Each entry has exactly
`note = {verified}` or `note = {unverified}`. “Verified” means that the described
URL, DOI landing page or primary text was actually opened. The accompanying
scope/annotation and check event say whether this was metadata, an abstract,
a theorem statement, a selected proof passage or a full argument. A metadata-only
opening never licenses an exact theorem match.

Different prefixes preserve the inspecting part's evidence. Two keys can denote
the same work while recording different access: one inspector may have opened
only a publisher record, another the book passage itself. These are deliberately
not silently coalesced into the stronger verification claim. Citation locators
in the claim map identify the passage actually used. No inference of independent
proof review follows from the `verified` flag alone.

The search logs preserve negative retrieval results and backward-reference
routes. Historical first circulation, lecture date, publication date and checked
revision date are distinguished whenever the sources establish them. A DOI
containing a year need not be the journal-volume year. An undated archive sheet
does not establish priority relative to a matching published text.

No newly downloaded complete third-party books or articles are included in the
ZIP. Programs can retrieve the public URLs again. Their included outputs record
locators, computations and access status rather than republishing full sources.
Excerpts from the user's supplied transcriptions are retained where needed for
the passage audit. The supplied input files themselves are not duplicated.

Two failed accesses particularly matter. Faltings's publisher URL returned a
LibLynx access notice; Theorem 17 was checked in the public MPIM preprint instead.
The proposed Huff attribution was checked only against publisher front matter;
its missing theorem is not treated as retrieved. Messing's original monograph
was initially available only through later references; a public copy was then
opened and the specified passages checked directly. That changed access is
recorded in the search and event logs. Other inaccessible original theorem
passages remain explicitly unverified even where later primary texts cite them.

Class C is not a synonym for a currently open mathematical problem. It can mark
an exact historical category still unidentified, a stronger quantifier not
covered by an opened theorem, or a reconstruction with a stated remaining proof
obligation. Present-status fields identify which kind of gap applies. Class F
means the fragment cannot securely identify an exact statement. Neither class
asserts novelty.
