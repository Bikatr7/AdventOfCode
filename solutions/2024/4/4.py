from aocd import get_data,submit

def slv(grd):
    r=len(grd)
    c=len(grd[0])
    ans=0
    
    for i in range(r):
        for j in range(c-3):
            if(grd[i][j:j+4]=="XMAS"):
                ans+=1
            if(grd[i][j:j+4]=="SAMX"):
                ans+=1
    
    for i in range(r-3):
        for j in range(c):
            forward = grd[i][j]+grd[i+1][j]+grd[i+2][j]+grd[i+3][j]
            backward = grd[i+3][j]+grd[i+2][j]+grd[i+1][j]+grd[i][j]
            if(forward == "XMAS"):
                ans+=1
            if(backward == "XMAS"):
                ans+=1
    
    for i in range(r-3):
        for j in range(c-3):
            d1 = grd[i][j]+grd[i+1][j+1]+grd[i+2][j+2]+grd[i+3][j+3]
            d1 = grd[i][j]+grd[i+1][j+1]+grd[i+2][j+2]+grd[i+3][j+3]
            d1_rev = grd[i+3][j+3]+grd[i+2][j+2]+grd[i+1][j+1]+grd[i][j]
            if(d1 == "XMAS"):
                ans+=1
            if(d1_rev == "XMAS"):
                ans+=1
            d2 = grd[i][j+3]+grd[i+1][j+2]+grd[i+2][j+1]+grd[i+3][j]
            d2_rev = grd[i+3][j]+grd[i+2][j+1]+grd[i+1][j+2]+grd[i][j+3]
            if(d2 == "XMAS"):
                ans+=1
            if(d2_rev == "XMAS"):
                ans+=1
    return ans

def slv2(grd):
    r=len(grd)
    c=len(grd[0])
    anser=0
    
    for i in range(1,r-1):
        for j in range(1,c-1):
            if(grd[i][j]=="A"):
                d1=grd[i-1][j-1]+grd[i+1][j+1]
                d2=grd[i-1][j+1]+grd[i+1][j-1]
                if((d1 in ["MS","SM"]) and (d2 in ["MS","SM"])):
                    anser+=1
    return anser

if(__name__=="__main__"):
    inp=get_data(day=4,year=2024)
    g=inp.splitlines()
    
    a1=slv(g)
    print(f"Part 1: {a1}")
    submit(str(a1), part="a", day=4, year=2024)
    
    a2=slv2(g)
    print(f"Part 2: {a2}")
    submit(str(a2), part="b", day=4, year=2024)
