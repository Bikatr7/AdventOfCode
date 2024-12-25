from aocd import get_data,submit
from collections import deque

def prs(d):
    mz=d.splitlines()
    st=ed=None
    
    for i,r in enumerate(mz):
        for j,c in enumerate(r):
            if(c=='S'):
                st=(i,j)
            elif(c=='E'):
                ed=(i,j)
                
    return mz,st,ed

def dst(mz,st):
    r,c=len(mz),len(mz[0])
    d={st:0}
    q=deque([st])
    
    while(q):
        p=q.popleft()
        cd=d[p]
        
        for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx,ny=p[0]+dx,p[1]+dy
            if(0<=nx<r and 0<=ny<c and 
               mz[nx][ny]!='#' and (nx,ny) not in d):
                d[(nx,ny)]=cd+1
                q.append((nx,ny))
                
    return d

def fnd(mz,st,ed,bt,mc):
    r,c=len(mz),len(mz[0])
    w={(i,j) for i in range(r) for j in range(c) if mz[i][j]=='#'}
    sd=dst(mz,st)
    ed=dst(mz,ed)
    ch={}
    
    for i in range(r):
        for j in range(c):
            if(mz[i][j]!='#'):
                v={(i,j)}
                q=deque([(i,j,0)])
                
                while(q):
                    ci,cj,d=q.popleft()
                    if(d>=mc):
                        continue
                        
                    for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
                        ni,nj=ci+di,cj+dj
                        if(0<=ni<r and 0<=nj<c and 
                           (ni,nj) not in v and d<mc):
                            if(mz[ni][nj]!='#'):
                                if((i,j) in sd and (ni,nj) in ed):
                                    tt=sd[(i,j)]+(d+1)+ed[(ni,nj)]
                                    ts=bt-tt
                                    if(ts>0):
                                        ch[ts]=ch.get(ts,0)+1
                                v.add((ni,nj))
                                q.append((ni,nj,d+1))
                            else:
                                v.add((ni,nj))
                                q.append((ni,nj,d+1))
    
    return ch

def slv1(d):
    mz,st,ed=prs(d)
    sd=dst(mz,st)
    bt=sd.get(ed,float('inf'))
    ch=fnd(mz,st,ed,bt,2)
    
    return sum(c for t,c in ch.items() if t>=100)

def slv2(d):
    mz,st,ed=prs(d)
    sd=dst(mz,st)
    bt=sd.get(ed,float('inf'))
    ch=fnd(mz,st,ed,bt,20)
    
    return sum(c for t,c in ch.items() if t>=100)

if(__name__=="__main__"):
    t="""###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
    
    tr=slv1(t)
    print(f"Test Result Part 1: {tr}")
    assert tr==0,f"Test failed: expected 0, got {tr}"
    
    tr2=slv2(t)
    print(f"Test Result Part 2: {tr2}")
    assert tr2==0,f"Test failed part 2: expected 0, got {tr2}"

    inp=get_data(day=20,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    if(a1 not in [1674,0,1395]):
        submit(a1,part="a",day=20,year=2024)
        
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    if(a2 not in [1674,0,1395]):
        submit(a2,part="b",day=20,year=2024) 