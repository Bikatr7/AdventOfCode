from aocd import get_data,submit
from collections import Counter

def trf(s):
    if(s==0):
        return [1]
    
    ss=str(s)
    if(len(ss)%2==0):
        m=len(ss)//2
        l=int(ss[:m])
        r=int(ss[m:])
        return [l,r]
    
    return [s*2024]

def sim(c,b):
    for _ in range(b):
        n=Counter()
        for s,t in c.items():
            ns=trf(s)
            for x in ns:
                n[x]+=t
        c=n
    
    return sum(c.values())

def slv1(d):
    s=[int(x) for x in d.split()]
    c=Counter(s)
    return sim(c,25)

def slv2(d):
    s=[int(x) for x in d.split()]
    c=Counter(s)
    return sim(c,75)

if(__name__=="__main__"):
    inp=get_data(day=11,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(a1,part="a",day=11,year=2024)
    
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    submit(a2,part="b",day=11,year=2024) 