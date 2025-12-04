from aocd import get_data,submit

def cnt_nbr(g,r,c):
    h=len(g)
    w=len(g[0])
    cnt=0
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            if(dr==0 and dc==0):
                continue
            nr=r+dr
            nc=c+dc
            if(0<=nr<h and 0<=nc<w and g[nr][nc]=='@'):
                cnt+=1
    return cnt

def slv1(d):
    g=[ln.strip() for ln in d.splitlines() if ln.strip()]
    h=len(g)
    w=len(g[0])
    
    acc=0
    for r in range(h):
        for c in range(w):
            if(g[r][c]=='@'):
                if(cnt_nbr(g,r,c)<4):
                    acc+=1
    return acc

def slv2(d):
    g=[list(ln.strip()) for ln in d.splitlines() if ln.strip()]
    h=len(g)
    w=len(g[0])
    
    tot=0
    while(True):
        rem=[]
        for r in range(h):
            for c in range(w):
                if(g[r][c]=='@'):
                    if(cnt_nbr(g,r,c)<4):
                        rem.append((r,c))
        
        if(not rem):
            break
        
        for r,c in rem:
            g[r][c]='.'
        
        tot+=len(rem)
    
    return tot

if(__name__=="__main__"):
    tst="""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
    
    tr=slv1(tst)
    print(f"Test result part 1: {tr}")
    assert tr==13
    
    dat=get_data(day=4,year=2025)
    
    a1=slv1(dat)
    print(f"Part 1: {a1}")
    submit(a1,part="a",day=4,year=2025)
    
    tr2=slv2(tst)
    print(f"Test result part 2: {tr2}")
    assert tr2==43
    
    a2=slv2(dat)
    print(f"Part 2: {a2}")
    submit(a2,part="b",day=4,year=2025)

