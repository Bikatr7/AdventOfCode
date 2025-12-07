from aocd import get_data,submit

def fnd_s(g):
    return next(c for c in range(len(g[0])) if g[0][c]=='S')

def slv1(d):
    g=[list(ln) for ln in d.splitlines()]
    h,w=len(g),len(g[0])
    bms,vis,splt=[(0,fnd_s(g))],set(),0
    
    while(bms):
        nb=[]
        for r,c in bms:
            if((r,c) in vis or r>=h):
                continue
            vis.add((r,c))
            if(g[r][c]=='^'):
                splt+=1
                if(c-1>=0):nb.append((r,c-1))
                if(c+1<w):nb.append((r,c+1))
            elif(r+1<h):
                nb.append((r+1,c))
        bms=nb
    return splt

def cnt(g,r,c,m,h,w):
    if(r>=h):return 1
    if((r,c) in m):return m[(r,c)]
    rs=0
    if(g[r][c]=='^'):
        if(c-1>=0):rs+=cnt(g,r,c-1,m,h,w)
        if(c+1<w):rs+=cnt(g,r,c+1,m,h,w)
    else:
        rs=cnt(g,r+1,c,m,h,w)
    m[(r,c)]=rs
    return rs

def slv2(d):
    g=[list(ln) for ln in d.splitlines()]
    return cnt(g,0,fnd_s(g),{},len(g),len(g[0]))

if(__name__=="__main__"):
    tst=""".......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
    
    tr=slv1(tst)
    print(f"Test part 1: {tr}")
    assert tr==21
    
    dat=get_data(day=7,year=2025)
    
    a1=slv1(dat)
    print(f"Part 1: {a1}")
    submit(a1,part="a",day=7,year=2025)
    
    tr2=slv2(tst)
    print(f"Test part 2: {tr2}")
    assert tr2==40
    
    a2=slv2(dat)
    print(f"Part 2: {a2}")
    submit(a2,part="b",day=7,year=2025)
