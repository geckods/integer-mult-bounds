#!/usr/bin/env python3
"""Price a reduced bit row on #146's paired-cube assembly (atom 1/1000 default).

This is #147's price144.py with exactly one line changed to track the compose:
the #144 control constants are replaced by #146's (subset-optimal) control so the
reproducibility assert pins the composit base. Everything else — the assembly,
both moment grids, the next-grid rejection — is #144/#146's own code.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))
sys.path.insert(0, str(Path(__file__).resolve().parent))

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

# Reuse #147's pricing module from the bit-elim dir (identical assembly).
sys.path.insert(0, str(ROOT / 'research/bit-elim-144'))
import price144 as _p147  # pyright: ignore[reportMissingImports]

from fractions import Fraction as Q


def price(row):
    return _p147.price(row)


def price_atom_2000(row):
    import paired_cube_network as pcn  # pyright: ignore[reportMissingImports]
    pcn.ATOM = Q(1, 2000)
    return _p147.price(row)
