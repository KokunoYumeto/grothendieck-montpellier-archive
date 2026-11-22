# L1: the maximal-open argument

Current state at 2026-11-19T16:15:59Z: complete written proof in sections/A_finish_L1_general.tex; descent_groups full written audit PASS; root full audit requested.

The original route needed actual local F-models at every later specialization, so uniform Artin-Rees only gave a conditional theorem. That need is removed by defining E(T,eta) to mean Artinian formal etaleness and U its largest open subset.

## Four steps

1. If C is an open of a flat base change X_Aprime and C→X is fpqc, formal etaleness of C→F_Aprime implies formal etaleness of X→F. For a nilpotent test, pull back the open on the reduction and lift that open to the whole test; it is an fpqc cover. On the overlap compare both X-maps using the FIRST Aprime-structure. Both land in the same C because their reductions agree. This proves descent of existence and uniqueness.
2. An actual modular x forces quasi-finiteness atx via the represented Artinian residue fiber. Over the completion of O_S,s isolate the finite local branch C throughx. Actual7 makes it modular (or etale) at every point. The proved etale corollary makes C→F a representable etale chart. C→SpecO_T,x is flat local and hence ff, so step1 proves formal etaleness on the entire local test. Every generization ofx is therefore inE. This is weaker than actual-generization and avoids the false claim that actual modularity is fpqc-local.
3. If an irreducible closed stratum has genericpointc inE, isolate a finite source module C_R and choose its uniform Artin-Rees exponentN. The generic base (R/I^N)_I is Artinian, so condition5 plus comparison makesF actually represented there. A finite etale residue splitting makes the generic branch actually modular, so8 applies. At laterw the finite COMPLETE pro-hull D_w supplied by4+5 maps to C_w, the completed source local ring. ModI^N they are isomorphic (or become so after the finite etale residue lift D'_w). UniformAR givesD_w=C_w (orD'_w=C_w), hence w∈E. Only pro-hulls are used atw.
4. If actualx were outsideU, takec genericcomponent of the closed complement throughx. Step2 givesc∈E, andstep3 givesrelativeopenW inthatcomponent containedinE. Remove the other complement components and shrinkaroundc; everypoint of the newopen lies either inU orW, henceinE. This contradicts maximalityofU. OnU the etale corollary represents all chartbasechanges; its open image inF is an algebraicspace. Finite-fiber relation bounds plus6 make it separated locallyquasifinite, henceascheme. Thus actualM is the usual open local-isomorphism locus insideU.

## Exact correction of earlier failed approaches

- Modularity after a closed base change is never identified with original modularity. The finite-thickening step proves only E.
- A pro-hull is never called an actual local model.
- Actual modularity is not descended through completion. Formal lifting is descended explicitly on nilpotent tests.
- The maximal-open argument is necessary: E need not be stable under generization globally; P=henselizedalpha_p has pro-modular closed points but no actual modular points there. The only propagation needed starts at an ACTUAL point and uses7.
- In the weaker-etale8 paragraph, complete local pro-hulls are identified through their local Artinian quotients. A closed-point lifting property is not promoted to a global lifting property at unrelated primes.

## Sources and checks

Reopened Stacks04GH(10.153.4),06DD(10.153.6),04GK(10.153.7) and02HM(37.8.10). The newfiniteetaleresidue lift uses04GK. Existing independently audited A:uniform-AR, A:artinian-base, A:etale-corollary, finite-fiberetaleqc and Stacks0417 supply the other named ingredients. Primary search for Artinian formal-etale criteria returned these Stacks sources; no novelty or priority claim. This does not change the main criterion's counterexample: openness of existing modular points does not guarantee their existence.
