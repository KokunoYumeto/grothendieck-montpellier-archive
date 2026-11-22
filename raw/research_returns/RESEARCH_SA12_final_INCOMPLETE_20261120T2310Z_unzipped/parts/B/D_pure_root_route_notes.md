# Pure-root modification route: verified reductions and remaining obstruction

## Scope, 2026-11-20 06:30 UTC

We investigate a possible extension to a sole smooth exceptional curve C of genus g with 0 < d = -C² < 2g-2. This note does not prove finite generation or finite exceptional wild image in that class.

Adjoining a p-th root of a rational function whose residue at C is not a p-th power gives a fixed purely inseparable extension with radial ramification index one and residue extension the curve Frobenius. The normalization Y' of a smooth surface Y in this extension is finite and Q-factorial. Indeed each prime divisor D' has a unique image divisor D; the Cartier pullback of D is eD', where e is a p-power. A common fixed p-power makes every local Weil divisor Cartier.

Every exceptional divisorial valuation over a point of Y' restricts to a divisorial valuation over a point of the smooth surface Y. Its residue field downstairs is rational, by factorization through point blowups. The upstairs residue extension is purely inseparable, so the normalized exceptional curve is rational as well. This controls the genera of potential new tails. It does not show that covers of the complement of the entire exceptional fibre extend across those tails.

## Explicit local obstruction to filling a rational tail

Let k be algebraically closed of characteristic two. Put Y = Spec k[x,t] and C = (t=0). In the pure degree-two extension

    z² = t + x³,

the normalization is the smooth plane Y' = Spec k[x,z]. The inverse image of C is the cusp C' : z² = x³. Its normalization is x=w², z=w³. At the cusp the element w=z/x is not in k[[w²,w³]], so there is no morphism C' -> C'^normal inverse to normalization. Thus a retraction onto the smooth normalized main curve cannot already be defined on the reduced main curve of this retained Q-factorial model.

Blow up the origin and use the chart x=s, z=sy. Then

    t = s²(y²+s).

The exceptional divisor R=(s=0) is rational. The strict transform of C' is y²+s=0 and meets R only at y=0. On the complement Y\C there is the connected finite étale Artin–Schreier cover

    u²+u = 1/t.

The derivative with respect to u is one. Connectedness follows from the odd pole of 1/t at the DVR t=0: a nonzero element b²+b of negative valuation has an even pole order.

After pure pullback and this blowup, put v=u+1/(sy). An exact identity in characteristic two gives

    v²+v = (1+y³+sy)/(s y²(y²+s)).

At the generic point of R the right side has valuation -1, since its leading coefficient is (1+y³)/y⁴ != 0 in k(y). If v were in the base field, its negative valuation would give an even pole order for v²+v. More precisely, in the extension the valuation of v is -1/2, so its ramification index is two. The cover is therefore wild at R, including on the part of R away from the strict transform of C'. Further embedded resolution does not change this divisorial valuation.

Consequently a pulled-back cover that is étale away from the *whole* pulled-back exceptional fibre need not extend étale after rational tails are filled in. This example is a local counterexample to that extension inference. Its affine curve C is not the proper exceptional curve of a global singularity, so it is not a counterexample to any D.1/D.2(ii) statement.

## Exact finite verification

The program code/check_pure_root_tail.py checks the polynomial source normalization description, cusp parametrization, blowup substitution, Artin–Schreier derivative and the rational-function identity. The valuation and geometric scope arguments are the written proofs above. The output is output/pure_root_tail.json.

## Remaining gate

To use the pure-root route globally, one would need a construction that either keeps the main exceptional curve smooth with a controlled formal neighborhood, or controls the ramification along every rational tail meeting it. Q-factoriality and rationality alone do not supply either condition. Applying the smooth single-curve cone theorem after discarding those tails is invalid.

## Automatic regularization loses the normal-degree gain

The chosen height-one pure extension is contained in K(Y)^(1/p). Normalizing Y in the latter gives its regular Frobenius twist Y^(-1), which maps finitely to the intermediate normalization. The total degree over Y is p² and the ramification index of the main curve is p. Since pullback(C)=p C_new, the finite intersection formula gives p² C_new²=p² C². Hence the normal degree returns to d. This automatic regularization does make the main curve smooth, but it does not supply the high negative degree sought in the intermediate index-one pure extension.
