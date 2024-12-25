from aocd import get_data,submit

def prs(l):
    h=[]
    for c in range(5):
        ht=0
        for r in range(7):
            if(l[r][c]=="#"):
                ht+=1
        h.append(ht)
    return h

def prs_inp(d):
    lks=[]
    kys=[]
    
    cl=[]
    for ln in d.splitlines():
        if(not ln):
            if(cl):
                if(cl[0]=="#####"):
                    lks.append(prs(cl))
                else:
                    kys.append(prs(cl))
            cl=[]
            continue
        cl.append(ln)
    
    if(cl):
        if(cl[0]=="#####"):
            lks.append(prs(cl))
        else:
            kys.append(prs(cl))
    
    return lks,kys

def cmp(l,k):
    for x,y in zip(l,k):
        if(x+y>7):
            return False
    return True

def slv1(d):
    l,k=prs_inp(d)
    
    vp=0
    for lk in l:
        for ky in k:
            if(cmp(lk,ky)):
                vp+=1
    
    return vp

if(__name__=="__main__"):
    td="""#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""
    
    tr=slv1(td)
    print(f"Test result: {tr}")
    assert tr==3,f"Test failed: expected 3, got {tr}"
    
    inp=get_data(day=25,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(str(a1),part="a",day=25,year=2024) 