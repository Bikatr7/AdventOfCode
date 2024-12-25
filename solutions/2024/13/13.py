from aocd import get_data,submit

def prs(d):
    m=[]
    c=[]
    for l in d.splitlines():
        if(not l):continue
        if(l.startswith("Button A:")):
            p=l.split(", ")
            ax=int(p[0].split("+")[1])
            ay=int(p[1].split("+")[1])
            c=[(ax,ay)]
        elif(l.startswith("Button B:")):
            p=l.split(", ")
            bx=int(p[0].split("+")[1])
            by=int(p[1].split("+")[1])
            c.append((bx,by))
        else:
            p=l.split(", ")
            px=int(p[0].split("=")[1])
            py=int(p[1].split("=")[1])
            c.append((px,py))
            m.append(tuple(c))
    return m

def fnd(ax,ay,bx,by,px,py):
    d=ax*by-ay*bx
    if(d==0):
        return None
    
    a=(px*by-py*bx)/d
    b=(py*ax-px*ay)/d
    
    if(a<0 or b<0 or a!=int(a) or b!=int(b)):
        return None
    
    return (int(a),int(b))

def slv1(d):
    m=prs(d)
    s=0
    
    for c in m:
        a,b,p=c
        r=fnd(a[0],a[1],b[0],b[1],p[0],p[1])
        if(r):
            ap,bp=r
            s+=ap*3+bp
    
    return s

def slv2(d):
    m=prs(d)
    s=0
    o=10000000000000
    
    for c in m:
        a,b,p=c
        r=fnd(a[0],a[1],b[0],b[1],p[0]+o,p[1]+o)
        if(r):
            ap,bp=r
            s+=ap*3+bp
    
    return s

if(__name__=="__main__"):
    inp=get_data(day=13,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(a1,part="a",day=13,year=2024)
    
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    submit(a2,part="b",day=13,year=2024) 