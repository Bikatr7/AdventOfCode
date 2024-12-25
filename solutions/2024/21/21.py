from aocd import get_data,submit
from functools import cache

p=[
    ["7","8","9"],
    ["4","5","6"],
    ["1","2","3"],
    [None,"0","A"]
]
ap=[
    [None,"^","A"],
    ["<","v",">"]
]

def gp(a,c):
    for i,r in enumerate(a):
        if(c in r):
            return (i,r.index(c))
    return None

@cache
def sp1(s,e,l):
    if(s=="<" and e==">"): pass
    
    if(isinstance(s,str)):
        s=gp(ap,s)
    if(isinstance(e,str)):
        e=gp(ap,e)
    
    if(l==0): return 1
    elif(l<3):
        v=None
        h=None
        if(e[0]<s[0]): v="^"
        elif(e[0]>s[0]): v="v"
        if(e[1]<s[1]): h="<"
        elif(e[1]>s[1]): h=">"
        
        if(not h and not v):
            return sp1("A","A",l-1)
        elif(not h):
            return sp1("A",v,l-1)+(abs(e[0]-s[0])-1)*sp1(v,v,l-1)+sp1(v,"A",l-1)
        elif(not v):
            return sp1("A",h,l-1)+(abs(e[1]-s[1])-1)*sp1(h,h,l-1)+sp1(h,"A",l-1)
        else:
            if(s[1]==0):
                return sp1("A",h,l-1)+(abs(e[1]-s[1])-1)*sp1(h,h,l-1)+sp1(h,v,l-1)+(abs(e[0]-s[0])-1)*sp1(v,v,l-1)+sp1(v,"A",l-1)
            elif(e[1]==0):
                return sp1("A",v,l-1)+(abs(e[0]-s[0])-1)*sp1(v,v,l-1)+sp1(v,h,l-1)+(abs(e[1]-s[1])-1)*sp1(h,h,l-1)+sp1(h,"A",l-1)
            else:
                return min(
                    sp1("A",h,l-1)+(abs(e[1]-s[1])-1)*sp1(h,h,l-1)+sp1(h,v,l-1)+(abs(e[0]-s[0])-1)*sp1(v,v,l-1)+sp1(v,"A",l-1),
                    sp1("A",v,l-1)+(abs(e[0]-s[0])-1)*sp1(v,v,l-1)+sp1(v,h,l-1)+(abs(e[1]-s[1])-1)*sp1(h,h,l-1)+sp1(h,"A",l-1)
                )
    else:
        v=None
        h=None
        if(e[0]<s[0]): v="^"
        elif(e[0]>s[0]): v="v"
        if(e[1]<s[1]): h="<"
        elif(e[1]>s[1]): h=">"
        
        if(not h and not v):
            return sp1("A","A",l-1)
        elif(not h):
            return sp1("A",v,l-1)+(abs(e[0]-s[0])-1)*sp1(v,v,l-1)+sp1(v,"A",l-1)
        elif(not v):
            return sp1("A",h,l-1)+(abs(e[1]-s[1])-1)*sp1(h,h,l-1)+sp1(h,"A",l-1)
        else:
            if(s[1]==0 and e[0]==3):
                return sp1("A",h,l-1)+(abs(e[1]-s[1])-1)*sp1(h,h,l-1)+sp1(h,v,l-1)+(abs(e[0]-s[0])-1)*sp1(v,v,l-1)+sp1(v,"A",l-1)
            elif(e[1]==0 and s[0]==3):
                return sp1("A",v,l-1)+(abs(e[0]-s[0])-1)*sp1(v,v,l-1)+sp1(v,h,l-1)+(abs(e[1]-s[1])-1)*sp1(h,h,l-1)+sp1(h,"A",l-1)
            else:
                return min(
                    sp1("A",h,l-1)+(abs(e[1]-s[1])-1)*sp1(h,h,l-1)+sp1(h,v,l-1)+(abs(e[0]-s[0])-1)*sp1(v,v,l-1)+sp1(v,"A",l-1),
                    sp1("A",v,l-1)+(abs(e[0]-s[0])-1)*sp1(v,v,l-1)+sp1(v,h,l-1)+(abs(e[1]-s[1])-1)*sp1(h,h,l-1)+sp1(h,"A",l-1)
                )

@cache
def sp2(s,e,l):
    if(s=="<" and e==">"): pass
    
    if(isinstance(s,str)):
        s=gp(ap,s)
    if(isinstance(e,str)):
        e=gp(ap,e)
    
    if(l==0): return 1
    elif(l<26):
        v=None
        h=None
        if(e[0]<s[0]): v="^"
        elif(e[0]>s[0]): v="v"
        if(e[1]<s[1]): h="<"
        elif(e[1]>s[1]): h=">"
        
        if(not h and not v):
            return sp2("A","A",l-1)
        elif(not h):
            return sp2("A",v,l-1)+(abs(e[0]-s[0])-1)*sp2(v,v,l-1)+sp2(v,"A",l-1)
        elif(not v):
            return sp2("A",h,l-1)+(abs(e[1]-s[1])-1)*sp2(h,h,l-1)+sp2(h,"A",l-1)
        else:
            if(s[1]==0):
                return sp2("A",h,l-1)+(abs(e[1]-s[1])-1)*sp2(h,h,l-1)+sp2(h,v,l-1)+(abs(e[0]-s[0])-1)*sp2(v,v,l-1)+sp2(v,"A",l-1)
            elif(e[1]==0):
                return sp2("A",v,l-1)+(abs(e[0]-s[0])-1)*sp2(v,v,l-1)+sp2(v,h,l-1)+(abs(e[1]-s[1])-1)*sp2(h,h,l-1)+sp2(h,"A",l-1)
            else:
                return min(
                    sp2("A",h,l-1)+(abs(e[1]-s[1])-1)*sp2(h,h,l-1)+sp2(h,v,l-1)+(abs(e[0]-s[0])-1)*sp2(v,v,l-1)+sp2(v,"A",l-1),
                    sp2("A",v,l-1)+(abs(e[0]-s[0])-1)*sp2(v,v,l-1)+sp2(v,h,l-1)+(abs(e[1]-s[1])-1)*sp2(h,h,l-1)+sp2(h,"A",l-1)
                )
    else:
        v=None
        h=None
        if(e[0]<s[0]): v="^"
        elif(e[0]>s[0]): v="v"
        if(e[1]<s[1]): h="<"
        elif(e[1]>s[1]): h=">"
        
        if(not h and not v):
            return sp2("A","A",l-1)
        elif(not h):
            return sp2("A",v,l-1)+(abs(e[0]-s[0])-1)*sp2(v,v,l-1)+sp2(v,"A",l-1)
        elif(not v):
            return sp2("A",h,l-1)+(abs(e[1]-s[1])-1)*sp2(h,h,l-1)+sp2(h,"A",l-1)
        else:
            if(s[1]==0 and e[0]==3):
                return sp2("A",h,l-1)+(abs(e[1]-s[1])-1)*sp2(h,h,l-1)+sp2(h,v,l-1)+(abs(e[0]-s[0])-1)*sp2(v,v,l-1)+sp2(v,"A",l-1)
            elif(e[1]==0 and s[0]==3):
                return sp2("A",v,l-1)+(abs(e[0]-s[0])-1)*sp2(v,v,l-1)+sp2(v,h,l-1)+(abs(e[1]-s[1])-1)*sp2(h,h,l-1)+sp2(h,"A",l-1)
            else:
                return min(
                    sp2("A",h,l-1)+(abs(e[1]-s[1])-1)*sp2(h,h,l-1)+sp2(h,v,l-1)+(abs(e[0]-s[0])-1)*sp2(v,v,l-1)+sp2(v,"A",l-1),
                    sp2("A",v,l-1)+(abs(e[0]-s[0])-1)*sp2(v,v,l-1)+sp2(v,h,l-1)+(abs(e[1]-s[1])-1)*sp2(h,h,l-1)+sp2(h,"A",l-1)
                )

def slv1(d):
    t=0
    for l in d.splitlines():
        c=l.strip()
        iv=int(c[:-1])
        sl=0
        for sp,ep in zip('A'+c[:3],c):
            sl+=sp1(gp(p,sp),gp(p,ep),3)
        cx=iv*sl
        print(f"Code: {c}, Sequence length: {sl}, Numeric value: {iv}, Complexity: {cx}")
        t+=cx
    print(f"Part 1: {t}")
    return t

def slv2(d):
    t=0
    for l in d.splitlines():
        c=l.strip()
        iv=int(c[:-1])
        sl=0
        for sp,ep in zip('A'+c[:3],c):
            sl+=sp2(gp(p,sp),gp(p,ep),26)
        cx=iv*sl
        print(f"Code: {c}, Sequence length: {sl}, Numeric value: {iv}, Complexity: {cx}")
        t+=cx
    print(f"Part 2: {t}")
    return t

if(__name__=="__main__"):
    td="""029A
980A
179A
456A
379A"""
    
    print("Test result part 1:",slv1(td))
    assert slv1(td)==126384

    inp=get_data(day=21,year=2024)
    
    a1=slv1(inp)
    submit(str(a1),part="a",day=21,year=2024)
    
    for s in ["<","^",">","v","A"]:
        for e in ["<","^",">","v","A"]:
            print(s,e,sp2(s,e,1))
    
    a2=slv2(inp)
    submit(str(a2),part="b",day=21,year=2024) 