from aocd import get_data,submit

def prs(d):
    f=[]
    s=[]
    fl=True
    c=""
    for x in d:
        c+=x
        if(len(c)==1):
            if(fl):
                f.append(int(c))
            else:
                s.append(int(c))
            c=""
            fl=not fl
    return f,s

def cmp1(f,s):
    d=[]
    i=0
    for j in range(len(f)):
        for _ in range(f[j]):
            d.append(i)
        i+=1
        if(j<len(s)):
            for _ in range(s[j]):
                d.append(-1)
    
    p=0
    for i in range(len(d)-1,-1,-1):
        if(d[i]!=-1):
            while(p<i and d[p]!=-1):
                p+=1
            if(p<i and d[p]==-1):
                d[p]=d[i]
                d[i]=-1
                p+=1
    return d

def cmp2(f,s):
    d=[]
    i=0
    ps={}
    sz={}
    
    for j in range(len(f)):
        st=len(d)
        for _ in range(f[j]):
            d.append(i)
        ps[i]=(st,len(d))
        sz[i]=f[j]
        i+=1
        if(j<len(s)):
            for _ in range(s[j]):
                d.append(-1)
    
    for i in range(len(f)-1,-1,-1):
        st,e=ps[i]
        z=sz[i]
        
        fs=-1
        fs2=0
        
        for j in range(st):
            if(d[j]==-1):
                if(fs==-1):
                    fs=j
                fs2+=1
            else:
                fs=-1
                fs2=0
            
            if(fs2==z):
                for k in range(z):
                    d[fs+k]=i
                    d[st+k]=-1
                break
    
    return d

def chk(d):
    s=0
    for p,i in enumerate(d):
        if(i!=-1):
            s+=p*i
    return s

def slv1(d):
    f,s=prs(d)
    return chk(cmp1(f,s))

def slv2(d):
    f,s=prs(d)
    return chk(cmp2(f,s))

if(__name__=="__main__"):
    inp=get_data(day=9,year=2024)
    
    a1=slv1(inp)
    print(f"Part 1: {a1}")
    submit(a1,part="a",day=9,year=2024)
    
    a2=slv2(inp)
    print(f"Part 2: {a2}")
    submit(a2,part="b",day=9,year=2024)
