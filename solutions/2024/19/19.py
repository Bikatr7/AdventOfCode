from aocd import get_data,submit

def prs(d):
    p,ds=d.split("\n\n")
    p=[p.strip() for p in p.split(", ")]
    ds=[d.strip() for d in ds.splitlines()]
    return p,ds

def cnt(d,p,m=None):
    if(m is None):m={}
        
    if(not d):
        return 1
        
    if(d in m):
        return m[d]
    
    t=0
    for pat in p:
        if(d.startswith(pat)):
            t+=cnt(d[len(pat):],p,m)
                
    m[d]=t
    return t

def slv1(d):
    p,ds=prs(d)
    ps=0
    
    for d in ds:
        if(cnt(d,p)>0):
            ps+=1
            
    return ps

def slv2(d):
    p,ds=prs(d)
    t=0
    
    for d in ds:
        w=cnt(d,p)
        t+=w
            
    return t

if(__name__=="__main__"):
    t="""r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

    assert slv1(t)==6
    assert slv2(t)==16

    inp=get_data(day=19,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(str(a1),part="a",day=19,year=2024)
    
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    submit(str(a2),part="b",day=19,year=2024) 