from aocd import get_data,submit

def is_saf(lvl):
    for i in range(len(lvl)-1):
        if(lvl[i] == lvl[i+1]):
            return False
    
    dif = [lvl[i+1]-lvl[i] for i in range(len(lvl)-1)]
    inc = all(d > 0 for d in dif)
    dec = all(d < 0 for d in dif)
    
    if(not (inc or dec)):
        return False
    
    return all(1 <= abs(d) <= 3 for d in dif)

def chk_damp(lvl):
    if(is_saf(lvl)):
        return True
    
    for i in range(len(lvl)):
        tmp = lvl[:i] + lvl[i+1:]
        if(is_saf(tmp)):
            return True
    return False

if(__name__ == "__main__"): 
    dat = get_data(day=2, year=2024)
    
    reps = [list(map(int,ln.split())) for ln in dat.splitlines()]
    
    p1 = sum(1 for r in reps if is_saf(r))
    print(f"Part 1 - Number of safe reports: {p1}")
    submit(p1, part="a", day=2, year=2024)
    
    p2 = sum(1 for r in reps if chk_damp(r))
    print(f"Part 2 - Number of safe reports with Problem Dampener {p2}")
    submit(p2, part="b", day=2, year=2024)
