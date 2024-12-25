from aocd import get_data,submit
from collections import Counter

def pos(r,t,w,h):
    px,py,vx,vy=r
    return ((px+vx*t)%w,(py+vy*t)%h)

def adj(ps):
    s=set(ps)
    a=0
    for x in range(100):
        for y in range(103):
            if((x,y) in s and (x+1,y) in s):
                a+=1
    return a

def qdr(p,w,h):
    px,py=p
    if(px==w//2 or py==h//2):
        return None
    return (px<w//2,py<h//2)

def prs(d):
    return [(int(l.split()[0].split('=')[1].split(',')[0]),int(l.split()[0].split('=')[1].split(',')[1]),int(l.split()[1].split('=')[1].split(',')[0]),int(l.split()[1].split('=')[1].split(',')[1])) for l in d.splitlines()]

def slv2(d):
    w,h=101,103
    r=prs(d)
    
    for t in range(10000):
        ps=[pos(rb,t,w,h) for rb in r]
        if(adj(ps)>200):
            return t
    return -1

def slv1(d):
    w,h=101,103
    r=prs(d)
    q=Counter()
    
    for rb in r:
        p=pos(rb,100,w,h)
        qd=qdr(p,w,h)
        if(qd):
            q[qd]+=1
    
    s=1
    for v in q.values():
        s*=v
    return s

if(__name__=="__main__"):   
    inp=get_data(day=14,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(str(a1),part="a",day=14,year=2024)
    
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    submit(str(a2),part="b",day=14,year=2024)