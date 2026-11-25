#!/usr/bin/env python3
"""Independent verifier of RGO XVII, using SciPy MILP rather than fixed-list subset search."""
import itertools as it
import json
import math
from functools import lru_cache
from pathlib import Path
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

def verify(row):
    n = row["n"]
    queries = list(it.combinations(range(n), 3))
    orders = [p for p in it.permutations(range(n)) if p[0] < p[-1]]
    sig = np.array([[sorted(q, key=p.index)[1] for q in queries] for p in orders])
    N, m = sig.shape
    assert (N, m) == (row["candidates"], row["allQueries"])
    diff = {sum(1 << j for j, x in enumerate(v) if x)
            for i in range(N - 1) for v in sig[i + 1:] != sig[i]}
    assert min(map(int.bit_count, diff)) == row["minimumDistance"] == n - 2
    minimal = []
    for d in sorted(diff, key=int.bit_count):
        if not any(x & d == x for x in minimal):
            minimal.append(d)
    A = np.array([[(d >> j) & 1 for j in range(m)] for d in minimal])
    for fixed in row["fixed"]:
        h = fixed["h"]
        res = milp(np.ones(m), integrality=np.ones(m), bounds=Bounds(0, 1),
                   constraints=LinearConstraint(A, h, np.inf))
        assert res.success and round(res.fun) == fixed["count"]
        assert round(res.mip_dual_bound) == fixed["count"]
        chosen = [queries.index(tuple(q)) for q in fixed["queries"]]
        assert len(set(chosen)) == fixed["count"]
        assert min(np.count_nonzero(sig[i+1:, chosen] != sig[i, chosen], axis=1).min()
                   for i in range(N-1)) >= h
    masks = [[sum(1 << i for i, s in enumerate(sig) if s[j] == a) for a in q]
             for j, q in enumerate(queries)]
    @lru_cache(None)
    def solve(S, depth):
        k = S.bit_count()
        if k <= 1:
            return True
        if not depth or k > 3**depth:
            return False
        options = []
        for mm in masks:
            parts = [S & M for M in mm]
            sizes = [x.bit_count() for x in parts]
            if max(sizes) == k or max(sizes) > 3**(depth-1):
                continue
            options.append((max(sizes), sum(x*x for x in sizes), parts))
        return any(all(solve(p, depth-1) for p in sorted(parts, key=int.bit_count, reverse=True))
                   for _, _, parts in sorted(options, key=lambda x: (x[0], x[1])))
    depth = math.ceil(math.log(N, 3)-1e-12)
    full = (1 << N) - 1
    while not solve(full, depth):
        depth += 1
    assert depth == row["adaptive"]["depth"]
    cert = row["certificate"]
    for k in range(1, cert["count"] + 1):
        found = any(np.all(np.any((sig[1:] != sig[0])[:, q], axis=1))
                    for q in it.combinations(range(m), k))
        if found:
            assert k == cert["count"]
            break
    else:
        raise AssertionError("missing certificate")
    return {"n": n, "minimum_distance": n-2, "fixed": {f["h"]:f["count"] for f in row["fixed"]},
            "adaptive": depth, "certificate": cert["count"]}

if __name__ == "__main__":
    filename = Path(__file__).resolve().parents[1] / "results" / "rgo_fase17_resultados.json"
    result = json.loads(filename.read_text())
    for row in result["rows"]:
        print(json.dumps(verify(row)))
    print("All ordinal minima and witnesses verified.")
