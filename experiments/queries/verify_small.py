"""Independent exhaustive recursion on explicit tuples (small examples only)."""
from itertools import combinations, permutations
from fractions import Fraction
from functools import lru_cache
from audit import optimize, fibers

def verify(words, pairs=False):
    n=len(words[0]); qs=[(j,) for j in range(n)]
    if pairs: qs+=list(combinations(range(n),2))
    def answer(w,q): return sum(int(w[j]) for j in q)%2
    @lru_cache(None)
    def rec(ws):
        if len(ws)==1:return (0,0)
        values=[]
        for q in qs:
            a=tuple(w for w in ws if answer(w,q)==0);b=tuple(w for w in ws if answer(w,q)==1)
            if not a or not b:continue
            x,y=rec(a),rec(b);values.append((len(ws)+x[0]+y[0],1+max(x[1],y[1])))
        return min(v[0] for v in values),min(v[1] for v in values)
    x,y=rec(tuple(words));return Fraction(x,len(words)),y

if __name__=='__main__':
    checked=0
    for n in (5,6,7,8):
        for k in (2,3):
            for ws in fibers(n,k):
                if not 2<=len(ws)<=8:continue
                for p in (False,True):
                    a,b=verify(ws,p);r=optimize(ws,p,False);assert abs(float(a)-r['optimal'])<1e-12 and b==r['worst'];checked+=1
    print('Independent checks:',checked)
