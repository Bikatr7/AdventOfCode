from aocd import get_data,submit

def prs(d):
    e=[]
    for l in d.split("\n"):
        if(not l):continue
        t,n=l.split(": ")
        t=int(t)
        n=[int(x) for x in n.split()]
        e.append((t,n))
    return e

def evl(n,o):
    r=n[0]
    for i,p in enumerate(o):
        if(p==0):
            r+=n[i+1]
        elif(p==1):
            r*=n[i+1]
        else:
            r=r*(10**len(str(n[i+1])))+n[i+1]
    return r

def chk(t,n,c=False):
    if(len(n)==1):
        return n[0]==t
    
    l=len(n)-1
    mx=max(n)
    mn=min(n)
    
    if(t<mn or (t>mx*mx and l==1)):
        return False
        
    if(c):
        ts=str(t)
        td=sum(len(str(x)) for x in n)
        if(len(ts)>td):
            return False
    
    o=[0]*l
    m=2 if c else 1
    while(True):
        try:
            if(evl(n,o)==t):
                return True
        except:
            pass
            
        i=0
        while(i<l and o[i]==m):
            o[i]=0
            i+=1
        if(i==l):
            break
        o[i]+=1
    
    return False

def slv1(d):
    e=prs(d)
    s=0
    for t,n in e:
        if(chk(t,n,False)):
            s+=t
    return s

def slv2(d):
    e=prs(d)
    s=0
    for t,n in e:
        if(chk(t,n,True)):
            s+=t
    return s

if(__name__=="__main__"):
    inp=get_data(day=7,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(a1,part="a",day=7,year=2024)
    
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    submit(a2,part="b",day=7,year=2024)
