from aocd import get_data,submit

def gd(x,y,g):
    dr=[(0,1),(1,0),(0,-1),(-1,0)]
    h=len(g)
    w=len(g[0])
    nb=[]
    for dx,dy in dr:
        nx,ny=x+dx,y+dy
        if(0<=nx<w and 0<=ny<h):
            nb.append((nx,ny))
    return nb

def slv1(d):
    g=[list(l) for l in d.splitlines()]
    h=len(g)
    w=len(g[0])
    
    ar=[]
    v=set()
    
    for y in range(h):
        for x in range(w):
            if(g[y][x]!="#" and (x,y) not in v):
                t=g[y][x]
                ar.append(set())
                td=[(x,y)]
                v.add((x,y))
                
                while(len(td)>0):
                    cx,cy=td.pop(0)
                    ar[-1].add((cx,cy))
                    for nx,ny in gd(cx,cy,g):
                        if((nx,ny) not in v and g[ny][nx]==t):
                            v.add((nx,ny))
                            td.append((nx,ny))
    
    r=0
    for a in ar:
        p=0
        for x,y in a:
            for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if((nx,ny) not in a):
                    p+=1
        r+=len(a)*p
    
    return r

def slv2(d):
    g=[list(l) for l in d.splitlines()]
    h=len(g)
    w=len(g[0])
    
    ar=[]
    
    for y in range(h):
        for x in range(w):
            if(g[y][x]!="#"):
                t=g[y][x]
                g[y][x]="#"
                ar.append(set([(x,y)]))
                td=[(x,y)]
                
                while(len(td)>0):
                    cx,cy=td.pop(0)
                    for nx,ny in gd(cx,cy,g):
                        if(g[ny][nx]==t):
                            g[ny][nx]="#"
                            td.append((nx,ny))
                            ar[-1].add((nx,ny))
    
    r=0
    for a in ar:
        sc=0
        for oxy in [(0,1),(0,-1),(1,0),(-1,0)]:
            s=set()
            for x,y in a:
                t=(x+oxy[0],y+oxy[1])
                if(t not in a):
                    s.add(t)
            
            tr=set()
            for x,y in s:
                t=(x+oxy[1],y+oxy[0])
                while(t in s):
                    tr.add(t)
                    t=(t[0]+oxy[1],t[1]+oxy[0])
            
            sc+=len(s)-len(tr)
        
        r+=len(a)*sc
    
    return r

if(__name__=="__main__"):
    inp=get_data(day=12,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(str(a1),part="a",day=12,year=2024)
    
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    submit(str(a2),part="b",day=12,year=2024) 