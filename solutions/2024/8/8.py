from aocd import get_data,submit

def prs(d):
    g=[list(l) for l in d.splitlines()]
    a={}
    for y in range(len(g)):
        for x in range(len(g[0])):
            if(g[y][x]!='.'):
                if(g[y][x] not in a):
                    a[g[y][x]]=[]
                a[g[y][x]].append((x,y))
    return a,len(g),len(g[0])

def col(p1,p2,p3):
    x1,y1=p1
    x2,y2=p2
    x3,y3=p3
    return (y2-y1)*(x3-x1)==(y3-y1)*(x2-x1)

def slv1(d):
    a,h,w=prs(d)
    n=set()
    
    for f in a:
        p=a[f]
        if(len(p)<2):
            continue
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                x1,y1=p[i]
                x2,y2=p[j]
                
                if(x1==x2):
                    dy=y2-y1
                    n1=(x1,y1-dy)
                    n2=(x1,y2+dy)
                    if(0<=n1[1]<h):n.add(n1)
                    if(0<=n2[1]<h):n.add(n2)
                elif(y1==y2):
                    dx=x2-x1
                    n1=(x1-dx,y1)
                    n2=(x2+dx,y1)
                    if(0<=n1[0]<w):n.add(n1)
                    if(0<=n2[0]<w):n.add(n2)
                else:
                    dx=x2-x1
                    dy=y2-y1
                    n1=(x1-dx,y1-dy)
                    n2=(x2+dx,y2+dy)
                    if(0<=n1[0]<w and 0<=n1[1]<h):n.add(n1)
                    if(0<=n2[0]<w and 0<=n2[1]<h):n.add(n2)
    return len(n)

def slv2(d):
    a,h,w=prs(d)
    n=set()
    
    for f in a:
        p=a[f]
        if(len(p)<2):
            continue
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                x1,y1=p[i]
                x2,y2=p[j]
                
                for y in range(h):
                    for x in range(w):
                        if((x,y)!=(x1,y1) and (x,y)!=(x2,y2) and col((x1,y1),(x2,y2),(x,y))):
                            n.add((x,y))
                n.add((x1,y1))
                n.add((x2,y2))
    return len(n)

if(__name__=="__main__"):
    inp=get_data(day=8,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(a1,part="a",day=8,year=2024)
    
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    submit(a2,part="b",day=8,year=2024)
