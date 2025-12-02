from aocd import get_data,submit

def chk(n,p2=False):
    s=str(n)
    l=len(s)
    if(p2):
        for pl in range(1,l):
            if(l%pl==0 and l//pl>=2 and s[:pl]*(l//pl)==s):
                return True
        return False
    return l%2==0 and s[:l//2]==s[l//2:]

def slv(d,p2=False):
    tot=0
    for rng in d.strip().split(','):
        if(rng.strip()):
            st,en=map(int,rng.split('-'))
            tot+=sum(i for i in range(st,en+1) if chk(i,p2))
    return tot

if(__name__=="__main__"):
    tst="11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    
    tr=slv(tst)
    print(f"Test part 1: {tr}")
    assert tr==1227775554
    
    dat=get_data(day=2,year=2025)
    
    a1=slv(dat)
    print(f"Part 1: {a1}")
    submit(a1,part="a",day=2,year=2025)
    
    tr2=slv(tst,True)
    print(f"Test part 2: {tr2}")
    assert tr2==4174379265
    
    a2=slv(dat,True)
    print(f"Part 2: {a2}")
    submit(a2,part="b",day=2,year=2025)
