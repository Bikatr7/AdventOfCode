from aocd import get_data,submit

def prs(d):
    pts=d.strip().split('\n\n')
    rngs=[]
    for ln in pts[0].splitlines():
        if(ln.strip()):
            st,en=map(int,ln.split('-'))
            rngs.append((st,en))
    
    ids=[]
    for ln in pts[1].splitlines():
        if(ln.strip()):
            ids.append(int(ln))
    
    return rngs,ids

def is_frsh(id,rngs):
    for st,en in rngs:
        if(st<=id<=en):
            return True
    return False

def mrg_rngs(rngs):
    if(not rngs):
        return []
    
    srt=sorted(rngs)
    mrg=[srt[0]]
    
    for st,en in srt[1:]:
        lst_st,lst_en=mrg[-1]
        if(st<=lst_en+1):
            mrg[-1]=(lst_st,max(lst_en,en))
        else:
            mrg.append((st,en))
    
    return mrg

def slv1(d):
    rngs,ids=prs(d)
    cnt=0
    for id in ids:
        if(is_frsh(id,rngs)):
            cnt+=1
    return cnt

def slv2(d):
    rngs,_=prs(d)
    mrg=mrg_rngs(rngs)
    
    tot=0
    for st,en in mrg:
        tot+=en-st+1
    
    return tot

if(__name__=="__main__"):
    tst="""3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    
    tr=slv1(tst)
    print(f"Test result part 1: {tr}")
    assert tr==3
    
    dat=get_data(day=5,year=2025)
    
    a1=slv1(dat)
    print(f"Part 1: {a1}")
    submit(a1,part="a",day=5,year=2025)
    
    tr2=slv2(tst)
    print(f"Test result part 2: {tr2}")
    assert tr2==14
    
    a2=slv2(dat)
    print(f"Part 2: {a2}")
    submit(a2,part="b",day=5,year=2025)

