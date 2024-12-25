from aocd import get_data,submit
from itertools import product
from collections import defaultdict

def mp(n):
    n=n^(n*64)
    n=n%16777216
    n=n^(n//32)
    n=n%16777216
    n=n^(n*2048)
    n=n%16777216
    return n

def gps(i,n=2000):
    p=[]
    c=[]
    s=i
    lp=s%10
    p.append(lp)
    
    for _ in range(n):
        s=mp(s)
        pr=s%10
        p.append(pr)
        c.append(pr-lp)
        lp=pr
    return p,c

def fas(c,p):
    sm=defaultdict(list)
    for i in range(len(c)-3):
        sq=tuple(c[i:i+4])
        sm[sq].append(p[i+4])
    return sm

def slv1(d):
    t=0
    for l in d.splitlines():
        i=int(l)
        s=i
        for _ in range(2000):
            s=mp(s)
        t+=s
        print(f"Initial: {i}, 2000th: {s}")
    return t

def slv2(d):
    b=[int(x) for x in d.splitlines()]
    a=[]
    
    for b in b:
        p,c=gps(b)
        s=fas(c,p)
        a.append(s)
    
    bt=0
    bs=None
    
    pc=[-3,-2,-1,0,1,2,3]
    for sq in product(pc,repeat=4):
        t=0
        sq=tuple(sq)
        
        for s in a:
            if(sq in s):
                t+=s[sq][0]
                
        if(t>bt):
            bt=t
            bs=sq
            print(f"New best sequence {sq} with total {t}")
    
    return bt

if(__name__=="__main__"):
    td="""1
10
100
2024"""
    
    td2="""1
2
3
2024"""
    
    tr=slv1(td)
    print(f"Test result part 1: {tr}")
    assert tr==37327623,f"Test failed: expected 37327623, got {tr}"
    
    tr2=slv2(td2)
    print(f"Test result part 2: {tr2}")
    assert tr2==23,f"Test failed: expected 23, got {tr2}"
    
    inp=get_data(day=22,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(str(a1),part="a",day=22,year=2024)
    
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    submit(str(a2),part="b",day=22,year=2024) 