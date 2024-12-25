from aocd import get_data,submit
from collections import defaultdict

def sum_p(p1,p2):
    return (p1[0]+p2[0],p1[1]+p2[1])

def mk_g(d):
    g=defaultdict(lambda:'#')
    for r in range(len(d)):
        for c in range(len(d[r])):
            g[(r,c)]=d[r][c]
    return g

def psh(p,d,bx,g):
    s=set()
    if(g[p]=='['):
        s=set([p,sum_p(p,(0,1))])
    elif(g[p]==']'):
        s=set([p,sum_p(p,(0,-1))])

    n=set([sum_p(b,d) for b in s])-s
    
    if(any(g[p]=='#' for p in n)):
        return False
    
    r=all(g[p]=='.' or psh(p,d,bx,g) for p in n)
    if(r):
        bx.update(s)
    return r

def slv2(d):
    dm={'v':(1,0),'^':(-1,0),'<':(0,-1),'>':(0,1)}
    m=[dm[v] for v in ''.join(d[1].split('\n'))]
    
    s=[]
    for l in d[0].split('\n'):
        s.append(l.replace('O','[]').replace('.','..').replace('#','##').replace('@','@.'))

    g=mk_g(s)
    p=next(p for p in g if g[p]=='@')

    for m in m:
        n=sum_p(p,m)
        if(g[n]=='#'):
            continue
        elif(g[n] in '[]'):
            b=set()
            if(psh(n,m,b,g)):
                nb={}
                for b in b:
                    nb[sum_p(b,m)]=g[b]
                    g[b]='.'
                for b in nb:
                    g[b]=nb[b]
                g[n]='@'
                g[p]='.'
                p=n
        elif(g[n]=='.'):
            g[n]='@'
            g[p]='.'
            p=n

    return sum((100*r+c) for (r,c) in g if g[(r,c)]=='[')

def slv1(d):
    dm={'v':(1,0),'^':(-1,0),'<':(0,-1),'>':(0,1)}
    m=[dm[v] for v in ''.join(d[1].split('\n'))]
    
    g=mk_g(d[0].split('\n'))
    p=next(p for p in g if g[p]=='@')

    for m in m:
        n=sum_p(p,m)
        if(g[n]=='#'):
            continue
        elif(g[n]=='O'):
            e=n
            while(g[e]=='O'):
                e=sum_p(e,m)
            if(g[e]=='#'):
                continue
            g[e]='O'
            g[n]='@'
            g[p]='.'
            p=n
        elif(g[n]=='.'):
            g[n]='@'
            g[p]='.'
            p=n

    return sum((100*r+c) for (r,c) in g if g[(r,c)]=='O')

if(__name__=="__main__"):
    inp=get_data(day=15,year=2024).split('\n\n')
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(str(a1),part="a",day=15,year=2024)
    
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    submit(str(a2),part="b",day=15,year=2024) 