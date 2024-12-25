from aocd import get_data,submit

def prs(d):
    r={'a':0,'b':0,'c':0}
    p=[]
    
    for l in d.splitlines():
        if("Register" in l):
            rg=l[9].lower()
            r[rg]=int(l.split(": ")[1])
        elif("Program:" in l):
            p=[int(x) for x in l.split(": ")[1].split(",")]
    
    return r['a'],r['b'],r['c'],p

def val(a,b,c,v):
    vs={4:a,5:b,6:c}
    return vs.get(v,v) if v<7 else None

def run(a,b,c,i,p):
    o,g=p[i],p[i+1]
    v=val(a,b,c,g)
    
    ops={
        0:lambda:(None,a//(1<<v),b,c),
        1:lambda:(None,a,b^g,c),
        2:lambda:(None,a,v&7,c),
        3:lambda:(None,a,b,c,g) if a else (None,a,b,c,i+2),
        4:lambda:(None,a,b^c,c),
        5:lambda:(v&7,a,b,c),
        6:lambda:(None,a,a//(1<<v),c),
        7:lambda:(None,a,b,a//(1<<v))
    }
    
    r=ops[o]()
    return r if len(r)==5 else (*r,i+2)

def sim(a,b,c,p):
    i,o=0,[]
    while(i<len(p)-1):
        r,a,b,c,i=run(a,b,c,i,p)
        if(r is not None):
            o.append(r)
    return o

def fnd(p,ps,v):
    for n in range(8):
        t=v*8+n
        if(sim(t,0,0,p)==p[ps:]):
            if(ps==0):
                return t
            r=fnd(p,ps-1,t)
            if(r is not None):
                return r
    return None

def slv1(d):
    a,b,c,p=prs(d)
    return ",".join(str(x) for x in sim(a,b,c,p))

def slv2(d):
    _,_,_,p=prs(d)
    return fnd(p,len(p)-1,0)

if(__name__=="__main__"):
    t="""Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
    
    assert slv1(t)=="4,6,3,5,6,3,5,2,1,0"
        
    inp=get_data(day=17,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(str(a1),part="a",day=17,year=2024)
    
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    if(a2 is not None):
        submit(str(a2),part="b",day=17,year=2024) 