from aocd import get_data,submit
from collections import defaultdict
from itertools import combinations

def prs(d):
    g=defaultdict(set)
    for l in d.splitlines():
        a,b=l.split('-')
        g[a].add(b)
        g[b].add(a)
    return g

def ftr(g):
    tr=set()
    for n in g:
        nb=g[n]
        for n1,n2 in combinations(nb,2):
            if(n2 in g[n1]):
                tr.add(tuple(sorted([n,n1,n2])))
    return tr

def fmc(g):
    nd=sorted(g.keys(),key=lambda x:len(g[x]),reverse=True)
    bc=[]
    
    def ec(c,cd):
        nonlocal bc
        if(len(c)>len(bc)):
            bc=c[:]
        for n in cd:
            if(all(n in g[x] for x in c)):
                nc=[c for c in cd if c>n and c in g[n]]
                ec(c+[n],nc)
    
    ec([],nd)
    return sorted(bc)

def slv1(d):
    g=prs(d)
    tr=ftr(g)
    
    tt=set()
    for t in tr:
        if(any(c.startswith('t') for c in t)):
            tt.add(t)
            print(f"Found triplet: {t}")
    
    return len(tt)

def slv2(d):
    g=prs(d)
    mc=fmc(g)
    return ','.join(mc)

if(__name__=="__main__"):
    td="""kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""
    
    tr=slv1(td)
    print(f"Test result: {tr}")
    assert tr==7,f"Test failed: expected 7, got {tr}"
    
    tr2=slv2(td)
    print(f"Test result part 2: {tr2}")
    assert tr2=="co,de,ka,ta",f"Test failed part 2: expected co,de,ka,ta, got {tr2}"

    inp=get_data(day=23,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(str(a1),part="a",day=23,year=2024)
    
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    submit(str(a2),part="b",day=23,year=2024) 