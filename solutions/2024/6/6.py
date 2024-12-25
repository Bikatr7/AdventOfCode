from aocd import get_data,submit

def prs(d):
    g=[]
    s=None
    for i,l in enumerate(d.split("\n")):
        r=list(l)
        if("^" in l):
            s=(i,l.index("^"))
        g.append(r)
    return g,s

def nxt(d):
    dr=[(0,1),(1,0),(0,-1),(-1,0)]
    return dr[(dr.index(d)+1)%4]

def vld(p,g):
    return 0<=p[0]<len(g) and 0<=p[1]<len(g[0])

def pth(g,s):
    v=set()
    v.add(s)
    cp=s
    cd=(-1,0)
    
    while(True):
        np=(cp[0]+cd[0],cp[1]+cd[1])
        if(not vld(np,g)):
            break
        if(g[np[0]][np[1]]=="#"):
            cd=nxt(cd)
        else:
            cp=np
            v.add(cp)
    return v

def sim(g,s,o):
    vs=set()
    cp=s
    cd=(-1,0)
    
    while(True):
        st=(cp,cd)
        if(st in vs):
            return True
        vs.add(st)
        np=(cp[0]+cd[0],cp[1]+cd[1])
        if(not vld(np,g)):
            return False
        if(g[np[0]][np[1]]=="#" or np==o):
            cd=nxt(cd)
        else:
            cp=np

def slv1(d):
    g,s=prs(d)
    return len(pth(g,s))

def slv2(d):
    g,s=prs(d)
    p=pth(g,s)
    lp=0
    for i in range(len(g)):
        for j in range(len(g[0])):
            if(g[i][j]=="." and (i,j)!=s):
                if((i,j) in p or any((i+di,j+dj) in p for di,dj in [(0,1),(1,0),(0,-1),(-1,0)])):
                    if(sim(g,s,(i,j))):
                        lp+=1
    return lp

if(__name__=="__main__"):
    inp=get_data(day=6,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(a1,part="a",day=6,year=2024)
    
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    submit(a2,part="b",day=6,year=2024)
