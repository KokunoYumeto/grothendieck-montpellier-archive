# VK-37-NORM: corrected source normalization, unchanged certificate

Reviewer: /root/vandiver_k, GPT-6 Astra Pro; effort not exposed. Date: 2026-11-21 UTC.

Hart--Harvey--Ong, *Irregular primes to two billion*, arXiv:1605.02398, section 7, printed p.13, explicitly corrects the exponent inside the Vandiver product printed in Buhler--Harvey section 4: the factors are zeta^(c/2)-zeta^(-c/2), where halves are interpreted modulo p. The correction was freshly read in the primary source at https://arxiv.org/pdf/1605.02398 . The authors state that this printed error was not propagated to the programs used for their cited computations.

The existing p=37 computation used s=16 modulo q=149 and factors s^c-s^(-c). It is exactly the corrected formula with zeta=s^2=107 modulo149. Both s and zeta have exact order37. The inverse of2 modulo37 is19, and

    zeta^(19c)=(s^2)^(19c)=s^(38c)=s^c,

for every integer c. Thus every factor, the product V=48, and the certificate V^4=142 !=1 modulo149 are unchanged. This is a change of the named primitive root/prime embedding, not an unverified numerical adjustment. The existence criterion is invariant under this reparametrization because squaring permutes the primitive odd-p roots.

The script now states the corrected criterion, defines zeta=107 and half=19 explicitly, and checks every half-exponent factor against the earlier square-root factor. Its two independent Bernoulli calculations and two modular-product evaluations still pass. The output was regenerated and read; the owned TeX section was changed to the corrected formula and retains the same V and fourth power. Historical completed archives were not changed.

This note and the corrected criterion application were read in full. The correction concerns accurate attribution of the displayed formula; it does not change the established Vandiver37 result.
