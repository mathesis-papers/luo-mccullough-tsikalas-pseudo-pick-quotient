# A three-point negative answer to the pseudo-Pick quotient question

Haobo Ma (ChronoAI Pte Ltd, Singapore), followed by Wenlin Zhang (National University of Singapore; ChronoAI Pte Ltd, Singapore).

License: CC BY 4.0 (`cc-by-4.0`).

## Mathematical coverage

The note answers Question 9.3 of Luo, McCullough and Tsikalas, *Beurling Criteria for Reproducing Kernels*, arXiv:2607.25088v2, page 45. On `X={0,1,2}`, let `x=(1/10,1,2)`, `k(i,j)=1+x_i*x_j` and `ell(i,j)=1+delta_ij*x_i^2`. The pair is complete pseudo-Pick for every positive matrix size, including interpolation lists with repeated nodes, but its quotient has quadratic form `-10/33` at `(-2,1,1)`.

The source kernel has rank two; the target kernel is positive definite. Both three points and source rank two are minimal. More generally, let `ell_t(i,j)=ell(i,j)+t*delta_ij*k(i,i)`. For every real `0<=t<5/99`, the pair remains complete pseudo-Pick and has quotient `Q+t*I` with negative quadratic form `-10/33+6*t`. Every pair in this family fails the complete Pick, Beurling–Lax–Halmos and complete pseudo-Leech properties, and admits neither a weak nor a strong Agler decomposition. The source multiplier algebra consists of constants.

The finite separation is a partial contribution to Problem 9.4, not a full comparison. The source already establishes a separation in a diagonal holomorphic setting. The converse pseudo-Leech implication and the suggested unrestricted pseudo-Pick-to-BLH route are not assertions of the source. The note states their failure as obstructions, not as refuted conjectures. Strictly positive definite source kernels, holomorphic-domain variants and Questions 9.1, 9.5 and 9.6 are outside its coverage.

The earlier antecedent for separation is McCullough–Tsikalas, Proposition 7.4, present in the 25 May 2024 preprint and published in 2025; its quotient is positive. The two-point lower bound is also a consequence of Arcozzi–Rochberg–Sawyer–Wick's 2010 multiplier-distance estimate. Shimorin's 2005 necessary quotient factorization implies failure of mixed complete Pick for the family, alongside the explicit scalar obstruction given here. Hartz's Corollary 3.5 supplies an affirmative subclass when the source is irreducible complete Pick and both kernels are normalized at the same point. The contribution highlighted here is the minimal negative quotient answer, not priority for separation or these antecedent criteria.

## Files

- `note.tex`: complete proof and references.
- `note.pdf`: typeset note, supplied alongside the source archive.
- `metadata.json`: author, license, problem and scientific coverage metadata.
- `verify.py`: exact rational identities using the Python standard library.
- `checks.json`: the corresponding deterministic mathematical output.

The source archive contains the TeX, metadata, this README and the two checking files.

## Build

Build with Tectonic 0.17.0:

```sh
tectonic note.tex
```

Alternatively, use a LaTeX installation providing `amsmath`, `amssymb`, `amsthm`, `booktabs`, `array`, `geometry`, `fontenc` and `hyperref`:

```sh
pdflatex -interaction=nonstopmode -halt-on-error note.tex
pdflatex -interaction=nonstopmode -halt-on-error note.tex
```

The bibliography is in `note.tex`; no separate BibTeX file is needed.

## Reproduce the finite identities

```sh
python3 verify.py > recomputed.json
cmp checks.json recomputed.json
```

All arithmetic is rational. The identities include kernel ranks, the negative quotient form, the two source relations, three positive diagonal factorizations and the negative minor obstructing a mixed-space multiplier. They also establish the family's negative-witness coefficient and sufficient endpoint, the quartic mixed-multiplier obstruction, and positive factorizations for the rational interior parameter `t=1/100`. Written proofs establish the full real parameter interval, all interpolation sizes, repeated nodes, minimality, and the pseudo-Leech and Agler obstructions; the checker is not a scan over matrix sizes or real parameters.

## Formal scope and scientific sources

The declaration `D5.S3.HilbertOperators.ReproducingKernels.CompletePseudoPickQuotientRefutation.result` in the pinned Lean file below proves the negation of the universal quotient-positivity assertion `claim`, using the three-point example at `t=0` and interpolation for all positive sizes and repeated nodes. The parameter family, minimality, multiplier-algebra description and all property separations have written proofs in the note. The pseudo-Leech necessary condition follows the proof of the posing source's Proposition 4.3 on the entire target space; the weak-Agler necessary condition is its Remark 3.14.

- Posing source: https://arxiv.org/abs/2607.25088v2, Definition 9.2 and Question 9.3, page 45; multiplier criterion and Proposition 3.1, page 15; Definition 3.25, pages 22–23.
- Single-kernel interpolation background: https://arxiv.org/abs/1610.01997v1, Section 0.
- Mixed-space comparison: https://arxiv.org/abs/2405.16319v4, Theorem 1.4; its diagonal holomorphic factorization theorem is distinct from the finite same-target-space question here.
- Two-point multiplier-distance estimate: https://arxiv.org/abs/1010.0136v1, Proposition 4.
- Normalized complete-Pick-source subclass: https://arxiv.org/abs/1505.05108v1, Corollary 3.5.
- Pinned Lean statement and proof: https://github.com/the-omega-institute/trureturing/blob/8acf7efa41af7fc9ddbbd39571e7ef73462f4509/D5/S3/HilbertOperators/ReproducingKernels/CompletePseudoPickQuotientRefutation.lean.
