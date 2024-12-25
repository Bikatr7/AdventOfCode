from aocd import get_data,submit
from heapq import heappush,heappop

def nxt(p,d,g):
    x,y=p
    m=[]
    
    for nd in [(0,1),(1,0),(0,-1),(-1,0)]:
        if(nd==d):
            nx,ny=x+nd[0],y+nd[1]
            if(0<=nx<len(g) and 0<=ny<len(g[0]) and g[nx][ny]!='#'):
                m.append((1,nd,(nx,ny)))
        else:
            dx1,dy1=d
            dx2,dy2=nd
            if(dx1*dy2-dx2*dy1 in [-1,1]):
                nx,ny=x+nd[0],y+nd[1]
                if(0<=nx<len(g) and 0<=ny<len(g[0]) and g[nx][ny]!='#'):
                    m.append((1001,nd,(nx,ny)))
    
    return m

def fnd(g):
    st=None
    ed=None
    
    for i in range(len(g)):
        for j in range(len(g[0])):
            if(g[i][j]=='S'):
                st=(i,j)
            elif(g[i][j]=='E'):
                ed=(i,j)
    
    h=[(0,(0,1),st,{st})]
    v={}
    mc=float('inf')
    ot=set()
    
    while(h):
        c,d,p,pt=heappop(h)
        
        if(c>mc):
            break
            
        if(p==ed):
            mc=c
            ot.update(pt)
            continue
            
        s=(p,d)
        if(s in v and v[s]<c):
            continue
            
        v[s]=c
        
        for nc,nd,np in nxt(p,d,g):
            tc=c+nc
            if((np,nd) not in v or v[(np,nd)]>=tc):
                tp=pt|{np}
                heappush(h,(tc,nd,np,tp))
    
    return mc,len(ot)

def slv1(d):
    g=[list(l) for l in d.splitlines()]
    mc,_=fnd(g)
    return mc

def slv2(d):
    g=[list(l) for l in d.splitlines()]
    _,tc=fnd(g)
    return tc

if(__name__=="__main__"):
    t1="""###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

    t2="""#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

    assert slv1(t1)==7036
    assert slv1(t2)==11048
    assert slv2(t1)==45
    assert slv2(t2)==64

    inp=get_data(day=16,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(str(a1),part="a",day=16,year=2024)
    
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    submit(str(a2),part="b",day=16,year=2024) 