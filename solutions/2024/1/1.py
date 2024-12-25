from aocd import get_data,submit

if(__name__ == "__main__"):
    dat = get_data(day=1, year=2024)
    
    l,r = [],[]
    for ln in dat.splitlines():
        a,b = map(int,ln.split())
        l.append(a)
        r.append(b)
    
    dist = sum(abs(x-y) for x,y in zip(sorted(l),sorted(r)))
    print(f"Part 1 - The total distance between the lists is: {dist}")
    submit(dist, part="a", day=1, year=2024)
    
    cnt = {}
    for x in r:
        cnt[x] = cnt.get(x,0) + 1
    
    scor = sum(x * cnt.get(x,0) for x in l)
    print(f"Part 2 - The similarity score is: {scor}")
    submit(scor, part="b", day=1, year=2024)
