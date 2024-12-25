from aocd import get_data,submit
from collections import defaultdict

def prs(d):
    r,s=d.split("\n\n")
    
    rl=defaultdict(set)
    for x in r.split("\n"):
        if(not x): continue
        b,a=map(int,x.split("|"))
        rl[b].add(a)
    
    sq=[]
    for x in s.split("\n"):
        if(not x): continue
        sq.append([int(y) for y in x.split(",")])
    
    return rl,sq

def chk(s,r):
    for i,x in enumerate(s):
        if(x in r):
            m=r[x]
            rem=set(s[i+1:])
            for y in m:
                if(y in s and y not in rem):
                    return False
    return True

def srt(s,r):
    n=len(s)
    res=[]
    u=set()
    
    while(len(res)<n):
        for x in s:
            if(x in u): continue
            ok=True
            for b,a in r.items():
                if(b not in s or b in u): continue
                if(x in a and b not in u):
                    ok=False
                    break
            if(ok):
                res.append(x)
                u.add(x)
                break
    return res

def slv1(d):
    r,s=prs(d)
    ans=0
    for x in s:
        if(chk(x,r)):
            m=len(x)//2
            ans+=x[m]
    return ans

def slv2(d):
    r,s=prs(d)
    ans=0
    for x in s:
        if(not chk(x,r)):
            sx=srt(x,r)
            m=len(sx)//2
            ans+=sx[m]
    return ans

if(__name__=="__main__"):
    inp=get_data(day=5,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(a1,part="a",day=5,year=2024)
    
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    submit(a2,part="b",day=5,year=2024) 