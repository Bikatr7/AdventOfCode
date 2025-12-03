from aocd import get_data,submit

def mx_jolt(bank,cnt=2):
    if(cnt==2):
        mx=0
        for i in range(len(bank)):
            for j in range(i+1,len(bank)):
                jlt=int(bank[i]+bank[j])
                mx=max(mx,jlt)
        return mx
    
    res=[]
    pos=0
    for step in range(cnt):
        remain=cnt-step
        mx_d='0'
        mx_i=-1
        for i in range(pos,len(bank)-remain+1):
            if(bank[i]>mx_d):
                mx_d=bank[i]
                mx_i=i
        res.append(mx_d)
        pos=mx_i+1
    return int(''.join(res))

def slv1(d):
    tot=0
    for ln in d.splitlines():
        if(ln.strip()):
            tot+=mx_jolt(ln.strip())
    return tot

def slv2(d):
    tot=0
    for ln in d.splitlines():
        if(ln.strip()):
            tot+=mx_jolt(ln.strip(),12)
    return tot

if(__name__=="__main__"):
    tst="""987654321111111
811111111111119
234234234234278
818181911112111"""
    
    tr=slv1(tst)
    print(f"Test result part 1: {tr}")
    assert tr==357
    
    dat=get_data(day=3,year=2025)
    
    a1=slv1(dat)
    print(f"Part 1: {a1}")
    submit(a1,part="a",day=3,year=2025)
    
    tr2=slv2(tst)
    print(f"Test result part 2: {tr2}")
    assert tr2==3121910778619
    
    a2=slv2(dat)
    print(f"Part 2: {a2}")
    submit(a2,part="b",day=3,year=2025)

