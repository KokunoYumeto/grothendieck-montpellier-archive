# Mathematical notes on scans 083–097

## What the pages do

**083–084. Products and addition.** A formula attributed to Jacobi expresses an elliptic function as a quotient of products of σ factors attached to its zeros and poles. Applying it to $pu-pv$ and taking logarithmic derivatives gives an addition relation for ζ. Putting $v=u$ gives the duplication relation. The next sheet gives the analogous addition and duplication formulas for $p$.

**084–085. The shifted sigma functions.** Two applications of Hermite’s formula relate $p(2u)$ and $pu-e_i$ to shifts by the half-periods. The notes name $\sigma_i$ and express the square root of $pu-e_i$ as $\sigma_i/\sigma$. A pair of shift identities gives the periods of each square root. The functions $\sigma_i$ are described as even and normalized at zero.

**085–086. Constructing theta.** Dividing σ by an exponential with the same multiplier under $u\mapsto u+2\omega_1$ produces a periodic quotient. The sheet expands it in a Fourier series. Translation by $2\omega_2$ then relates successive coefficients. Scan 086 gives the exponential and sine versions of the theta series, the conversion back to σ, the translation laws, and the zeros.

**087–089. Inverting the parameter.** The series is rewritten in powers of $h(t)$ and related to general quadratic exponential sums. Interchanging the two generating periods in the σ expression yields a transformation with $t\mapsto-1/t$. The heat equation determines the dependence on $t$ of the remaining multiplier. Scan 088 gives the boxed transformation and a formula for the derivative at zero. Scan 089 discusses its use in accelerating numerical evaluation.

**089–090. Three further theta functions.** Ratios involving $\sigma_i$ introduce three indexed theta functions. Their Fourier series are paired with differently shaped $\vartheta$ symbols in a second numbering. The sheets give expressions for the roots $e_i$, for $\eta_1\omega_1$ and for the derivative of the odd theta at zero.

**091. A sheet of conversion formulas.** The first rows collect the periods, the invariants, two coefficients and the three roots. Four groups then express them in terms of different starting data. They include reciprocal lattice sums, the roots of a cubic, period integrals and choices of their determinations. One such choice is rewritten above a cancelled sum.

**092–093. The modular function.** The ratio $J=g_2^3/\Delta$ is introduced as a function of $\tau=\omega_2/\omega_1$. The invariants depend on the period group and give invariance under determinant-one integral changes of basis. The discussion passes to local inversion, two classes of double points, their values, and a connection with Picard’s theorems.

**094. Legendre functions.** The inverse of an elliptic integral introduces sn. Two quadratic relations and the values at zero specify cn and dn. A three-row system gives the derivatives. Taylor expansions at zero, a parameter $\alpha$, two degenerations and the period integrals $K,K'$ follow.

**095. Periods, translations and values.** Three lists give periods and progressions of zeros and poles. The ruled right margin treats real arguments. The center gives translations by full multiples and half-periods, followed by the imaginary-argument formulas with complementary modulus. The table evaluates all three functions at the listed multiples of the periods.

**096–097. Converting between notations.** The real ordering $e_2<e_3<e_1$ gives a modulus $k$ and scale $M$. The sheets relate sn, cn and dn to σ quotients, $p$ to sn, and the three $K$’s to the $\omega$’s. The choice $M=1/2$ displays common periods. The last sheet writes the Legendre functions as theta quotients, then gives their three addition formulas.

## Statements left without proof

| Scan | Manuscript wording or displayed assertion | Treatment on the sheet |
|---|---|---|
| 083–084 | “le deuxième mb sera en effet elliptique”; “L’application de la formule d’Hermite … donne” | The periodicity condition and earlier formula are cited. Hermite’s formula is applied twice without being established here. |
| 084–085 | “La racine carrée de … fonction est analytique méromorphe”; “Les fonctions … sont paires” | The sigma quotient represents the root. The parity assertion and period lists are stated without a separate proof. |
| 086 | “est définie et holomorphe”; “Ces relations caractérisent … un facteur constant près” | The Fourier construction is invoked for the characterization. Holomorphy and the convergence rate are asserted. |
| 086–088 | “Notons aussi la formule (vérification immédiate)”; “vérification immédiate par la série” | The shifts of the parameter and the heat equation are left for direct verification. The computation of $H'/H$ is reported in words. |
| 089–090 | “et s’exprime par une série du type”; “Le calcul des $e_i$ par exemple donne”; “Enfin, on a les relations” | The series, the fourth-power formulas and the final derivative product are recorded without the coefficient computations. |
| 091 | “Expressions en fonction de”; “pour des déterminations convenables” | The sheet gives lattice sums and period integrals as reference formulas. The choices of paths and square-root branches are not worked out. |
| 092–093 | “peuvent être pris arbitraires”; “comme on vérifie très facilement”; “il y a exactement deux classes de points doubles”; “Le calcul donne respectivement” | The existence and classification assertions are used in the argument for $J$. The mentioned integral calculation is not displayed. |
| 094 | “On a les équations différentielles”; “Les développements de Taylor sont, en 0” | Derivatives and coefficients are listed. The two limiting rows are also given without calculation. |
| 095 | “pour leurs périodes propres, d’ordre 2; pour leurs périodes communes, d’ordre 4” | The orders, translation rules, imaginary-argument formulas and special values are stated in lists and a table. |
| 096–097 | “et on a les formules ci-dessus”; “Formules d’addition” | The quotient, period and addition identities are presented as formulas without accompanying proofs. |

## Questions and conjectures

Scan 091 L10 may query an index. The ink after $g$ in the formula for $c_1$ resembles a question mark with its own dot. The same sheet’s earlier box gives $g_2=20c_1$. I found no explicit conjecture or open mathematical question in the prose.

## Slips

The entries distinguish the manuscript reading from the proposed mathematical reading. Confidence applies to the proposed correction at the specified place. A doubtful stroke, a cancellation or an overwrite limits confidence to low.

| ID and place | Written statement | Proposed reading | Reason and confidence |
|---|---|---|---|
| **S00** · 083 L5 | f(z) or f(u) on the left of (17), with u in both products | **S00a** · A single argument on both sides if the formula is to be read as an identity of functions | The letter on the left is darkened. The u’s in the products are clear. **Low.** |
| **S01** · 083 L1 | $e^{2\eta_i(u+\omega_i)+2i\pi}$ | **S01a** · A constant exponent ±iπ | The factor on scan 85 for i=1 has a minus sign after exponentiation. The term 2iπ on this sheet gives a plus sign. **High.** |
| **S02** · 084 L18–21 | A period 2ωᵢ, then a sign change at 2ωᵢ | **S02a** · 2ωⱼ in the last clause | The same shift cannot both preserve a nonzero function and negate it. The two cases of (26) distinguish i from j. **High.** |
| **S03** · 085 L19 | $A_{n+1}=-h^n A_n$, with the base uncertain | **S03a** · $-h^{2n}A_n$ if the base is $h$ | The exponent of h on scan 87 increases by 2n between consecutive half-integer squares. The base of the recurrence is retraced. **Low.** |
| **S04** · 086 L5 and 089 L16–19 | A denominator resembling 1 in n−1/1 | **S04a** · n−1/2 | The exponential on scan 86 L1 has a clear half-shift. The lower strokes on the later copies are much straighter. **Low.** |
| **S05** · 088 L8–10 | At $t=i$ and apparent $v=0$, “on trouve $a=\sqrt i$”, followed by $i\sqrt{i/t}$ | **S05a** · Compare first derivatives at v=0, giving $a=i\sqrt i$ with the same choice of root | Both sides at zero vanish by oddness. The proposed constant would also lose the i in the next boxed line. The argument written after v= is uncertain. **Low.** |
| **S06** · 088 L17 | On the right of (12), no visible square after (n−1/2) | **S06a** · (n−1/2)²π/T with the preceding minus sign | The opposite side, (11), and the following derivative series keep a squared half-shift. Several neighbouring signs and digits are overwritten. **Low.** |
| **S06b** · 088 L18 | Possible i before πv in the last cosine | **S06ba** · $\cos((2n-1)\pi v)$ | The derivative of the sine in scan 86 (2) has the same argument. The sheet edge crowds the final letters. **Low.** |
| **S07** · 089 L4–8 | For Re T not greater than 1, one of Re T and Re(1/T) is said to be greater than 1 | **S07a** · An inversion-only bound works for positive real T, using a non-strict bound at T=1 | With T=1/2+2i the real parts are 1/2 and 2/17. The assertion needs an additional condition for complex T. The comparison is retraced. **Low.** |
| **S07b** · 089 L1–3 | The inverse-parameter theta is written with first argument v | **S07ba** · The general formula (10) uses v/t in the second theta | This could be shorthand in the numerical discussion. The full identity on scan 88 includes a prefactor as well. **Medium.** |
| **S08** · 089 L18–19 | No alternating sign in the cosine row for Θ₂, with a possible extra π in cos 2ππv | **S08a** · If the preceding factor is (−1)ⁿ, retain it in the paired series and use cos 2nπv | Pairing n with −n leaves that factor intact. The first sign and the angular letter after 2 are uncertain. **Low.** |
| **S09** · 090 L8 | $\Theta_i'''0/\Theta_i'0$ | **S09a** · Probably $\Theta_i''0/\Theta_i0$ | The indexed functions are even by the parity on scan 85 and (13). The displayed odd derivatives both vanish at zero. The proposed ratio uses their first nonconstant Taylor coefficient. **Medium.** |
| **S10** · 090 L9–11 | 1/2 before the expression for e₃ | **S10a** · 1/3, if the last subscript is 2 | With that index, the three fourth-power brackets cancel in the sum of the roots when all coefficients are 1/3. The last subscript is doubtful. **Low.** |
| **S11** · 091 L4, L16 | $g_2=4(e_2e_3+e_3e_1+e_1e_2)$ | **S11a** · $g_2=-4(e_2e_3+e_3e_1+e_1e_2)$ | The z coefficient of the displayed product is the positive symmetric sum times 4. On the other side it is −g₂. The disputed constant sign is immaterial to this coefficient. **High.** |
| **S12** · 091 L19–20 | g₁=20c₁ and a second coefficient 20 with uncertain indices | **S12a** · g₂=20c₁ and g₃=28c₂ | Compare the two explicit pairs at the head and in the first section of the same sheet. **Low.** |
| **S12b** · 091 L11 | The middle root can read e₃ in the list e₁,e₃,e₃ | **S12ba** · e₁,e₂,e₃ | The three distinct factors in the upper product name all three roots. **Low.** |
| **S13** · 092 L2–7 | “homogènes de degré 2 et 3” as functions of the periods | **S13a** · Degrees −4 and −6 under a common dilation of the periods | Scan 91 writes sums in reciprocal fourth and sixth powers. The relative weights 2 and 3 still give equal degree to g₂³ and g₃². **Medium.** |
| **S14** · 093 L14–21 | $J(i)$ and $J((1+i\sqrt3)/2)$ have respectively 0 and 1 | **S14a** · Respectively 1 and 0, with g₃=0 and g₂=0 | The lattice rotations by i and by (1+i√3)/2 force these vanishings using scan 91’s powers. The ordering here uses the clear first listing of the two points. **High.** |
| **S15** · 094 L17–18 | k=1, dn=1/th | **S15a** · dn=1/ch | At k=1, (1) gives dn²=cn² and both functions start at 1. The same row gives cn=1/ch. At zero 1/th has a pole. **High.** |
| **S15b** · 094 L19–20 | Apparent du in K, though the integrand uses x | **S15ba** · dx | The adjacent K′ formula has a much clearer x in its differential. **Low.** |
| **S15c** · 094 L21–22 | K″=−k−iK′, with the first k possibly a capital | **S15ca** · K″=−K−iK′ | The period identifications on scan 096 and the chosen zero sum of the half-periods on scan 091 give the latter reading. **Low.** |
| **S16** · 095 upper right beside sn | “n’a pas de zéros ni de pôles pour u réel” | **S16a** · No real poles in the stated real-modulus case; real zeros include 0 and 2mK | The table on this sheet and the normalization on scan 94 both give sn 0=0. The beginning of the written range of k is obscured. **Low.** |
| **S17** · 095 L5, L8 | The two cn and dn zero progressions end in 2m′iK | **S17a** · Apparently 2m′iK′ | On the same sheet both functions change sign under 2iK′, preserving their zero sets. The zero rows lack the final prime present in the neighbouring pole rows. **Medium.** |
| **S18** · 095 L17 | Possible 2K″ in the first argument of the last quotient row | **S18a** · K″, if the extra 2 was cancelled | Putting u=0 would otherwise conflict with the preceding rule for sn(2K″). The digit and the letter touch. **Low.** |
| **S19** · 096 L8 | dn proportional to $\sigma_3/\sigma_1$, with an isolated stroke before the quotient | **S19a** · $\sigma_3/\sigma_2$ | Squaring and using (24) and the definition of k gives (p−e₃)/(p−e₂). The theta version on scan 97 also has subscript 2 in its denominator. The isolated multiplier remains uncertain. **Low.** |
| **S20** · 097 L6 | The first factor after k² looks like on²u | **S20a** · sn²u | The parallel cn and dn denominators both have sn²u. The initial loop on this line is closed. **Low.** |

## Pointers

| Scan | Words on the page | Referent |
|---|---|---|
| 083 | “Formule de Jacobi”; “grace à (16)” with the accent uncertain | Jacobi’s product formula and this sheet’s σ transformation. |
| 084 | “L’application de la formule d’Hermite” | Hermite’s formula is invoked for both duplication and the shifted root functions. |
| 085 | “série de Fourier” | The series of the periodic quotient. |
| 086–089 | “comme on voit par le calcul qui avait donné”; “au deuxième membre de (8)”; “Comparant avec” the circled 8; “La formule” followed by the circled 10 | Internal references connect the characterization, the heat-equation calculation and numerical use of the inversion formula. |
| 090 | “fonctions de Weierstrass” | The parenthetical identification of the looped theta symbols. |
| 093 | “à la base des théorèmes de Picard sur les fonctions entières” | Picard is named at the end of the modular-function discussion. No particular publication is identified. |
| 094, 096–097 | “Fonctions elliptiques de Legendre”; “développements de Taylor”; “fonctions de Weierstrass et de Legendre”; “Fonctions de Legendre et fonctions” followed by Θ | These headings and names identify the notations being compared. |

No other archive cote, dated work or bibliographic title is specified on these leaves.

## Remarks of the model

- **R01. Model, high confidence, scan 095.** The minus before $ik'/k$ occurs in both the $K''$ and the $3K''$ cells of the cn row. The sheet’s own translation $\operatorname{cn}(u+2K'')=\operatorname{cn}u$ gives equal values in those two columns.
- **R02. Model, low confidence for the overwritten reading, scan 096.** Solving $e_1-e_2=M^2$, $e_3-e_2=k^2M^2$ and $e_1+e_2+e_3=0$ gives $3e_2=(-2+k'^2)M^2$. This supplies a reason to prefer the leading minus in the coefficients line. The ink at the parenthesis and the 2 still admits another reading.
- **R03. Model, high confidence on the notation, scan 091.** The lattice terms for $c_1,c_2$ and the line for $e_i$ share a starred index set. The first two sums use reciprocal fourth and sixth powers. The last uses reciprocal squares. The sheet gives no explicit summation order in that line.

