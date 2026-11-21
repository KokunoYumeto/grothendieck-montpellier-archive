# Fresh full review of the actual plethysm ray algebra

Reviewer: `/root/grothendieck_dictionary`, GPT-6 Astra Pro; effort not exposed. Date: 21 November 2026 UTC.

Target: `agent_plethysm_ray_algebra.md`.

Target SHA256: `a9400e168226b08e985b36214712cb26bbc7c36082f9d63e9e82718602396c51`.

**Result: PASS for the full supplement, including all calculations (S1)–(S7), the actual highest-weight interpretation, and the stated scope.** I read the entire supplement and the companion F34 report to check that the ray is exactly the same stretched multiplicity family. No changes are required.

## Independent reconstruction

The divided basis has the asserted raising action: \(x\partial_y(x^{k-i}y^i/i!)=v_{i-1}\). Its interpretation as a basis of \(V\), whose symbols then become free generators of \(\operatorname{Sym}(V)\), is explicit and avoids incorrectly identifying this algebra with a subalgebra of \(\mathbf C[x,y]\). A degree-\(N\), index-\(r\) monomial has diagonal weight ((kN-r,r)). In the semisimple characteristic-zero \(\mathrm{GL}_2\) representation of that degree, the kernel of the raising operator in the dominant weight (((k-1)N,N)) has dimension exactly the stated irreducible multiplicity. The hypothesis \(k\ge2\) ensures dominance, including the determinant case at \(k=2\).

For \(t=v_1/v_0\), the localized derivation has \(D(t)=1\). Differentiating

\[
\sum_{j=0}^{i}\frac{(-t)^j}{j!}v_{i-j}
\]

gives cancellation between differentiation of the coefficient at index \(j+1\) and differentiation of the basis variable at index \(j\). The terminal variable \(v_0\) has zero derivative. Multiplying by \(v_0^{i-1}\) preserves invariance. Every resulting term is a polynomial: the only superficially negative exponent occurs at \(j=i\), where the final factor is \(v_0\), giving \((-1)^i v_1^i/i!\). Each term has degree and index \(i\). The displayed \(f_2\) and \(f_3\) expansions are correct.

The localization is an invertible triangular coordinate change. Starting with \(v_1=t v_0\), each \(v_i\) is solved from \(f_i\) using the unit coefficient \(v_0^{i-1}\). This proves both generation and algebraic independence of \(v_0,t,f_2,\ldots,f_k\) after inverting \(v_0\). In those coordinates \(D=\partial_t\). Characteristic zero ensures that its kernel consists exactly of polynomials independent of \(t\); the argument would fail in positive characteristic because of powers such as \(t^p\), which the note correctly excludes.

In the resulting Laurent polynomial invariant algebra, a monomial \(v_0^a\prod f_i^{x_i}\) has degree minus index \(a\). Independence and homogeneity imply that the full degree-equals-index subalgebra has \(a=0\). This is exactly \(\mathbf C[f_2,\ldots,f_k]\), already contained in the unlocalized polynomial algebra. Intersection with the original algebra therefore changes nothing. This proves the claimed global ray algebra without needing a presentation of the entire Weitzenböck invariant ring.

The products \(\prod f_i^{x_i}\) consequently form an actual independent spanning basis of the highest-weight ray, with \(\sum i x_i=N\). The count equals the companion F34 family by its definition, so the construction does not infer a basis merely from numerical equality. The affine and weighted projective interpretations and Hilbert series follow directly. The statements about monomial multiplication constants and numerical-\(k\) formula size are properly limited to this particular algebra; they do not identify a GCT VIII basis or yield a bound polynomial in \(\log k\).

## Source and review scope

The classical \(\mathrm{GL}_2\) highest-weight decomposition is background representation theory. The supplement's localized coordinate and invariant-algebra proof is fully explicit and was independently checked here. Its reference to PPS Lemma1.3 is only a compatibility statement with the already cited classical formula; the proof does not require an unverified new PPS assertion. This event is a full fresh mathematical review of the named supplement at the recorded hash, not a new review of every result in F34 or of a later generated LaTeX fragment.


## Direct generated-fragment match

I subsequently read all of finding_F34_ray.tex, SHA256 ad62fddde0f0801d9a48abe5ad85511a2ef29f402e3c7f6718dbf90915a573fa, including its separate Grothendieck paragraph. **PASS.** The free-algebra convention, dominant GL2 highest-weight identification, polynomial invariant generators, triangular localization, characteristic-zero derivative kernel, degree-minus-index extraction, actual monomial basis, and compact-input scope all match the reviewed source note. The scheme and Hilbert-series paragraph adds only direct consequences of the proved polynomial presentation.
