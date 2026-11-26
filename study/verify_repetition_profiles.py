from collections import Counter, defaultdict
from itertools import product

def spectrum(s,k): return Counter(s[i:i+k] for i in range(len(s)-k+1))
def sig(s,k): return (s[:k-1],s[len(s)-k+1:],tuple(sorted(spectrum(s,k).items())))
def profile(s): return tuple(tuple(sorted(Counter(spectrum(s,k).values()).items())) for k in range(1,len(s)+1))
def switching(s,k):
    z=k-1; n=len(s)-z
    p=defaultdict(list)
    for i in range(n+1): p[s[i:i+z]].append(i)
    for I in p.values():
        for ai,i in enumerate(I):
            for l in I[ai+1:]:
                for j in range(i+1,l+1):
                    for m in p[s[j:j+z]]:
                        if m>l:
                            t=s[:i]+s[l:m]+s[j:l]+s[i:j]+s[m:]
                            if t!=s: return t
    return None

if __name__=='__main__':
    checks=0
    for n in range(2,13):
        words=[''.join(w) for w in product('01',repeat=n)]
        for k in range(1,n+1):
            c=Counter(sig(s,k) for s in words)
            for s in words:
                assert (switching(s,k) is not None)==(c[sig(s,k)]>1)
                checks+=1
    a,b='0000101','0001001'
    assert sig(a,2)==sig(b,2) and profile(a)==profile(b)
    words=[''.join(w) for w in product('01',repeat=7)]
    for s in (a,b):
        print(s,[sum(sig(s,k)==sig(t,k) for t in words) for k in range(1,8)])
    print('Checks:',checks)
