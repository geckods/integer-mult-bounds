# Composed bit-branch witness: #146's exact min-cut subset + #147's terminal elimination + #148's tightened adapter toll

Under #144's retained interfaces this package certifies

    T(n) = O(n (log n)^(1 - kappa)),
    kappa = 4649897/10000000000 = 4.649897e-4   (atom 1/2000, #148's tightened table)
    kappa = 929553/2000000000 = 4.647765e-4      (atom 1/1000, the inherited table)

Both are +3,264 / +1,132 grid points (denominator 10^10) over #147's
4646633/10000000000, the furthest published value at the time of this
branch. The next 10^-10 grid point is rejected under both tables.

## What this is

No new mathematical machinery. This is the composition of three already
published, independently certified bit-branch improvements to #144's
paired-cube shared-core word, which compose because they touch disjoint
parts of the same word's certification:

- **#146 (Thomas Marchand):** the entrance-gauge subset S* chosen by exact
  telescoping interval s-t min-cut, certified globally optimal over all
  2^11565 subsets (this branch inherits S* via the pinned
  `references/paired-cube/pr97-subset/selection.json` and its
  `verify_global_mincut` certificate in `scripts/paired_cube_bit.py`).
  R 28,866, W 32,408, kappa 4.61028508707e-4 / 4.61239827139e-4 alone.
- **#147 (William Porter):** 1,549 terminal accumulator eliminations on
  #144's selection (SovereignSteak's #122 operation): delete each
  never-a-source deferred output slot, read, output read, inverse writes
  and V^-1; apply its forward writes to the target at the same time and
  frame; every modified target chain re-certified exactly nested over Q;
  literal replay over Z and F2 with both tamper controls rejected.
  Alone: kappa 4.646633e-4 on #144's subset.
- **#148 (Rohan Gupta):** the tightened subordinate adapter exponent
  beta_atom = 1/2000, which raises the effective bit saving
  eco: this branch inherits both atom tables via #146's frozen
  `certificates/paired-cube-network.json`.

This branch applies #147's elimination to **#146's min-cut-optimal
subset** (9,730 selected gauges rather than #144's 9,543) — the two PRs
were published against different subsets of the same word and had not been
composed — and prices the reduced row under **both** atom tables. The
elimination search, plan regeneration, row regeneration and replay are run
unmodified from #147's own `research/bit-elim-144` tooling; the row is
priced by #144's own `price144`/`paired_cube_network.py` assembly exactly
as in #147, with ATOM set by the pinned table.

| | roles R | W per vertex | coarse bit (1/1000) | stopped bit (1/1000) | kappa |
|---|---|---|---|---|---|
| #146 alone | 28,866 | 32,408 | 461877426979/10^15 | 4613422943/10^13... (subset) | 4.61239827139e-4 |
| this branch | 27,317 | 30,859 | 2328181/5*10^9 | 4652090237/10^13 (row) | **4.649897e-4** |

The deficit per vertex is unchanged; the complex side retains its 4.5%
headroom; the bit side binds.

## Verify

From the repository root (Python 3.10+ standard library, about 4 minutes;
do not use `-O`):

    python3 research/subset-elim-compose/verify.py

The script runs these checks:

1. It reproduces #146's published kappas 461028508707/10^15 (atom 1/1000)
   and 461239827139/10^15 (atom 1/2000) from the pinned network file.
2. It rebuilds the exact frames from the pinned PR97 witness with Swapnil
   Jain's `check_lifted.py` machinery (no cache).
3. It regenerates the elimination plan on #146's selection: every accepted
   target chain must be nested exactly over Q; the result equals the
   frozen `plan.json` (1,549 eliminated).
4. It regenerates the reduced row and equals the frozen `row-elim.json`
   (R 27,317, W 30,859).
5. It replays the reduced word literally over Z and over F2 with arbitrary
   scratch and data; both tamper controls (a missing redirected update, a
   sign-flipped one) are rejected.
6. `price_compose.py` prices the frozen row with #144's own assembly under
   both atom tables: kappa 929553/2000000000 at atom 1/1000 and
   4649897/10000000000 at atom 1/2000, each with the next grid point
   rejected.

## Credits

- icekylinx: #144, #130 (paired-cube and three-stage cover framework,
  selected gauges, pricing and assembly) and #104.
- Thomas Marchand: #146 (exact telescoping min-cut subset optimality).
- William Porter: #147 (terminal accumulator elimination on the bit word;
  this branch reuses his `frames144.py`, `elim144.py`, `row144.py`,
  `replay144.py` and `price144.py` verbatim).
- Rohan Gupta: #148 (tightened adapter toll, beta_atom = 1/2000).
- SovereignSteak: #122 (terminal accumulator elimination operation).
- Swapnil Jain: the round-seven deferred bit word and its exact frame
  tools; Zhihao Chen: the PR97 ledger.

The composition itself — running the elimination on the min-cut subset and
pricing under both atom tables — was prepared by Abhinav Ramachandran with
Hermes (Nous Research) assistance.

## Scope

All inherited written proof dependencies of #144/#146/#147/#148 remain
explicit: the shared-core execution theorem, the eliminated-chain nesting
arguments of #147, the min-cut optimality certificate of #146 (which is
itself machine-verified inside this verify), and the inherited
analytic/tape interfaces. This package certifies the finite arithmetic of
the composed witness only; it does not upgrade any of those dependencies.
