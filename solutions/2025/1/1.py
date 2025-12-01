from aocd import get_data, submit

if(__name__ == "__main__"):
    dat = get_data(day=1, year=2025)
    
    tst = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
    
    pos = 50
    cnt = 0
    for ln in tst.splitlines():
        if(not ln.strip()): continue
        dirr = ln[0]
        dist = int(ln[1:])
        if(dirr == 'L'):
            pos = (pos - dist) % 100
        else:
            pos = (pos + dist) % 100
        if(pos == 0): cnt += 1
    
    print(f"Test part 1: {cnt}")
    assert cnt == 3
    
    pos = 50
    cnt = 0
    for ln in dat.splitlines():
        if(not ln.strip()): continue
        dirr = ln[0]
        dist = int(ln[1:])
        if(dirr == 'L'):
            pos = (pos - dist) % 100
        else:
            pos = (pos + dist) % 100
        if(pos == 0): cnt += 1
    
    print(f"Part 1: {cnt}")
    submit(cnt, part="a", day=1, year=2025)
    
    pos = 50
    cnt2 = 0
    for ln in tst.splitlines():
        if(not ln.strip()): continue
        dirr = ln[0]
        dist = int(ln[1:])
        
        if(dirr == 'L'):
            if(pos > 0 and dist >= pos):
                cnt2 += 1 + (dist - pos) // 100
            elif(pos == 0):
                cnt2 += dist // 100
            else:
                cnt2 += dist // 100
            pos = (pos - dist) % 100
        else:
            targ = (100 - pos) % 100
            if(targ == 0): targ = 100
            if(dist >= targ):
                cnt2 += 1 + (dist - targ) // 100
            pos = (pos + dist) % 100
    
    print(f"Test part 2: {cnt2}")
    assert cnt2 == 6
    
    pos = 50
    cnt2 = 0
    for ln in dat.splitlines():
        if(not ln.strip()): continue
        dirr = ln[0]
        dist = int(ln[1:])
        
        if(dirr == 'L'):
            if(pos > 0 and dist >= pos):
                cnt2 += 1 + (dist - pos) // 100
            elif(pos == 0):
                cnt2 += dist // 100
            else:
                cnt2 += dist // 100
            pos = (pos - dist) % 100
        else:
            targ = (100 - pos) % 100
            if(targ == 0): targ = 100
            if(dist >= targ):
                cnt2 += 1 + (dist - targ) // 100
            pos = (pos + dist) % 100
    
    print(f"Part 2: {cnt2}")
    submit(cnt2, part="b", day=1, year=2025)
