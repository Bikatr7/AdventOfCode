from aocd import get_data,submit

def prs(d,rtl):
    lns=d.splitlines()
    w=max(len(ln) for ln in lns)
    lns=[ln.ljust(w) for ln in lns]
    h,prbs,c=len(lns),[],0
    
    while(c<w):
        if(all(lns[r][c]==' ' for r in range(h))):
            c+=1
            continue
        
        st=c
        while(c<w and any(lns[r][c]!=' ' for r in range(h))):
            c+=1
        
        nums,op=[],None
        if(rtl):
            for col in range(c-1,st-1,-1):
                digs=[]
                for r in range(h):
                    ch=lns[r][col]
                    if(ch!=' '):
                        if(ch in ['+','*']):
                            op=ch
                        else:
                            digs.append(ch)
                if(digs):
                    nums.append(int(''.join(digs)))
        else:
            for r in range(h):
                tok=lns[r][st:c].strip()
                if(tok):
                    if(tok in ['+','*']):
                        op=tok
                    else:
                        nums.append(int(tok))
        
        if(nums and op):
            prbs.append((nums,op))
    
    return prbs

def slv(d,rtl):
    tot=0
    for nums,op in prs(d,rtl):
        tot+=sum(nums) if op=='+' else eval('*'.join(map(str,nums)))
    return tot

if(__name__=="__main__"):
    tst="""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
    
    tr=slv(tst,False)
    print(f"Test part 1: {tr}")
    assert tr==4277556
    
    dat=get_data(day=6,year=2025)
    
    a1=slv(dat,False)
    print(f"Part 1: {a1}")
    submit(a1,part="a",day=6,year=2025)
    
    tr2=slv(tst,True)
    print(f"Test part 2: {tr2}")
    assert tr2==3263827
    
    a2=slv(dat,True)
    print(f"Part 2: {a2}")
    submit(a2,part="b",day=6,year=2025)
