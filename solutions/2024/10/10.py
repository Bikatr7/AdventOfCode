from aocd import get_data,submit
from collections import deque

def prs(d):
    return [[int(c) for c in l] for l in d.splitlines()]

def nbr(x,y,h,w):
    d=[(0,1),(1,0),(0,-1),(-1,0)]
    n=[]
    for dx,dy in d:
        nx,ny=x+dx,y+dy
        if(0<=nx<w and 0<=ny<h):
            n.append((nx,ny))
    return n

def fnd(g):
    t=[]
    for y in range(len(g)):
        for x in range(len(g[0])):
            if(g[y][x]==0):
                t.append((x,y))
    return t

def cnt(g,sx,sy):
    h=len(g)
    w=len(g[0])
    v=set()
    r=set()
    q=deque([(sx,sy,0)])
    
    while(q):
        x,y,c=q.popleft()
        
        if((x,y,c) in v):
            continue
            
        v.add((x,y,c))
        
        if(g[y][x]==9):
            r.add((x,y))
            continue
            
        for nx,ny in nbr(x,y,h,w):
            if(g[ny][nx]==c+1):
                q.append((nx,ny,c+1))
    
    return len(r)

def pth(g,sx,sy,m=None,p=None):
    if(m is None):m={}
    if(p is None):p=set()
    
    h=len(g)
    w=len(g[0])
    cp=(sx,sy)
    ch=g[sy][sx]
    
    if(ch==9):
        return 1
        
    if(cp in p):
        return 0
        
    if(cp in m):
        return m[cp]
    
    p.add(cp)
    t=0
    
    for nx,ny in nbr(sx,sy,h,w):
        if(g[ny][nx]==ch+1):
            t+=pth(g,nx,ny,m,p.copy())
    
    m[cp]=t
    return t

def slv1(d):
    g=prs(d)
    t=fnd(g)
    s=0
    
    for x,y in t:
        s+=cnt(g,x,y)
    
    return s

def slv2(d):
    g=prs(d)
    t=fnd(g)
    s=0
    
    for x,y in t:
        s+=pth(g,x,y)
    
    return s

if(__name__=="__main__"):
    inp=get_data(day=10,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(a1,part="a",day=10,year=2024)
    
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    submit(a2,part="b",day=10,year=2024) 