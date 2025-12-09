from aocd import get_data,submit

def prs(d):
    return [tuple(map(int,ln.split(','))) for ln in d.strip().splitlines()]

def in_poly(x,y,pts):
    cnt=0
    for i in range(len(pts)):
        x1,y1,x2,y2=pts[i]+pts[(i+1)%len(pts)]
        if(y1<=y<y2 or y2<=y<y1):
            if(x<x1+(y-y1)*(x2-x1)/(y2-y1)):cnt+=1
    return cnt%2==1

def on_edge(x,y,pts):
    for i in range(len(pts)):
        x1,y1,x2,y2=pts[i]+pts[(i+1)%len(pts)]
        if(x1==x2==x and min(y1,y2)<=y<=max(y1,y2)):return True
        if(y1==y2==y and min(x1,x2)<=x<=max(x1,x2)):return True
    return False

def pt_in(x,y,pts):
    return in_poly(x,y,pts) or on_edge(x,y,pts)

def rect_ok(rx1,ry1,rx2,ry2,pts):
    mnx,mxx,mny,mxy=min(rx1,rx2),max(rx1,rx2),min(ry1,ry2),max(ry1,ry2)
    cx,cy={mnx,mxx},{mny,mxy}
    for i in range(len(pts)):
        x1,y1,x2,y2=pts[i]+pts[(i+1)%len(pts)]
        if(x1==x2 and mnx<=x1<=mxx):cx.add(x1)
        if(y1==y2 and mny<=y1<=mxy):cy.add(y1)
    for x in cx:
        if(not pt_in(x,mny,pts) or not pt_in(x,mxy,pts)):return False
    for y in cy:
        if(not pt_in(mnx,y,pts) or not pt_in(mxx,y,pts)):return False
    return True

def slv(d,p2=False):
    pts=prs(d)
    mx=0
    for i in range(len(pts)):
        for j in range(i+1,len(pts)):
            x1,y1,x2,y2=pts[i]+pts[j]
            if(not p2 or rect_ok(x1,y1,x2,y2,pts)):
                mx=max(mx,(abs(x2-x1)+1)*(abs(y2-y1)+1))
    return mx

if(__name__=="__main__"):
    tst="""7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
    
    tr=slv(tst)
    print(f"Test part 1: {tr}")
    assert tr==50
    
    dat=get_data(day=9,year=2025)
    
    a1=slv(dat)
    print(f"Part 1: {a1}")
    submit(a1,part="a",day=9,year=2025)
    
    tr2=slv(tst,True)
    print(f"Test part 2: {tr2}")
    assert tr2==24
    
    a2=slv(dat,True)
    print(f"Part 2: {a2}")
    submit(a2,part="b",day=9,year=2025)
