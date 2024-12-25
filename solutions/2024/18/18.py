from aocd import get_data,submit
from collections import deque

def gn(p,c,m):
    x,y=p
    for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx,ny=x+dx,y+dy
        if(0<=nx<=m and 0<=ny<=m and (nx,ny) not in c):
            yield (nx,ny)

def fsp(c,m):
    s=(0,0)
    e=(m,m)
    
    q=deque([(s,0)])
    sn={s}
    
    while(q):
        p,st=q.popleft()
        
        if(p==e):
            return st
            
        for n in gn(p,c,m):
            if(n not in sn):
                sn.add(n)
                q.append((n,st+1))
    
    return -1

def slv1(d,m=70,l=1024):
    cd=[tuple(map(int,l.split(','))) for l in d.splitlines()]
    c=set(cd[:l])  
    return fsp(c,m)

def slv2(d,m=70):
    cd=[tuple(map(int,l.split(','))) for l in d.splitlines()]
    c=set()
    
    for i,cd in enumerate(cd):
        c.add(cd)
        if(fsp(c,m)==-1):
            return f"{cd[0]},{cd[1]}"
    return "FUCK"

if(__name__=="__main__"):
    td="""5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,1
6,1"""
    
    print(slv1(td,6,12))
    assert slv1(td,6,12)==22
    
    print(slv2(td,6))
    assert slv2(td,6)=="6,1"

    inp=get_data(day=18,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(str(a1),part="a",day=18,year=2024)
    
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    submit(a2,part="b",day=18,year=2024) 