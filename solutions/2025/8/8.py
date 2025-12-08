from aocd import get_data,submit
import heapq
from collections import Counter

def dst(p1,p2):
    return sum((a-b)**2 for a,b in zip(p1,p2))**0.5

def fnd(p,x):
    if(p[x]!=x):p[x]=fnd(p,p[x])
    return p[x]

def uni(p,sz,x,y):
    rx,ry=fnd(p,x),fnd(p,y)
    if(rx!=ry):
        if(sz[rx]<sz[ry]):rx,ry=ry,rx
        p[ry]=rx
        sz[rx]+=sz[ry]
        return True
    return False

def slv(d,ncon=None):
    pts=[tuple(map(int,ln.split(','))) for ln in d.strip().splitlines()]
    n=len(pts)
    prs=[(dst(pts[i],pts[j]),i,j) for i in range(n) for j in range(i+1,n)]
    heapq.heapify(prs)
    par,siz={i:i for i in range(n)},{i:1 for i in range(n)}
    
    if(ncon):
        for _ in range(ncon):
            _,i,j=heapq.heappop(prs)
            uni(par,siz,i,j)
        cmp=Counter(fnd(par,i) for i in range(n))
        top3=sorted(cmp.values(),reverse=True)[:3]
        return top3[0]*top3[1]*top3[2]
    
    circs,lst=n,None
    while(circs>1):
        _,i,j=heapq.heappop(prs)
        if(uni(par,siz,i,j)):
            circs-=1
            lst=(i,j)
    return pts[lst[0]][0]*pts[lst[1]][0]

if(__name__=="__main__"):
    tst="""162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
    
    tr=slv(tst,10)
    print(f"Test part 1: {tr}")
    assert tr==40
    
    dat=get_data(day=8,year=2025)
    
    a1=slv(dat,1000)
    print(f"Part 1: {a1}")
    submit(a1,part="a",day=8,year=2025)
    
    tr2=slv(tst)
    print(f"Test part 2: {tr2}")
    assert tr2==25272
    
    a2=slv(dat)
    print(f"Part 2: {a2}")
    submit(a2,part="b",day=8,year=2025)
