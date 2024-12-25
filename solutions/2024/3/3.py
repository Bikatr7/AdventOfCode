from aocd import get_data,submit
import re

def find_valid_multiplications(data):
    patrn=r"mul\((\d{1,3}),(\d{1,3})\)"
    tot=0
    
    for ln in data.splitlines():
        matchs=re.finditer(patrn,ln)
        for m in matchs:
            n1,n2=map(int,m.groups())
            tot+=n1*n2
    
    return tot

def find_enabld(dat):
    mp = r"mul\((\d{1,3}),(\d{1,3})\)"
    dp = r"do\(\)"
    dnp = r"don't\(\)"
    
    t = 0
    en = True
    
    for l in dat.splitlines():
        p = 0
        while(p < len(l)):
            mm = re.match(mp, l[p:])
            dm = re.match(dp, l[p:])
            dnm = re.match(dnp, l[p:])
            
            if(mm):
                if(en):
                    n1,n2 = map(int,mm.groups())
                    t += n1*n2
                p += mm.end()
            elif(dm):
                en = True
                p += dm.end()
            elif(dnm):
                en = False
                p += dnm.end()
            else:
                p += 1
    
    return t

if(__name__ == "__main__"):
    dat = get_data(day=3, year=2024)
    
    p1 = find_valid_multiplications(dat)
    print(f"Part 1 - Sum of multiplicatios: {p1}")
    submit(p1, part="a", day=3, year=2024)
    
    p2 = find_enabld(dat)
    print(f"Part 2 - Sum of enabled multiplications: {p2}")
    submit(p2, part="b", day=3, year=2024) 