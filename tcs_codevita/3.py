def ev(c, m):
    o=["==","!=", "<", ">"]
    for op in o:
        if op in c:
            l,r=c.split(op)
            l=l.strip(); r=r.strip()
            lv=m[l] if l in m else int(l)
            rv=m[r] if r in m else int(r)
            if op=="==": return lv==rv
            if op=="!=": return lv!=rv
            if op=="<": return lv<rv
            if op==">": return lv>rv
    return False

def blk(a,i,stop):
    b=[]; d=0
    while i<len(a):
        s=a[i].strip()
        if s.startswith("for") or s.startswith("if"): d+=1
        elif s=="end":
            if d==0 and "end" in stop: break
            d-=1
        elif s in stop and d==0: break
        b.append(a[i]); i+=1
    return b,i

def run(a,m):
    o=[]; i=0
    while i<len(a):
        s=a[i].strip()
        if not s: i+=1; continue
        p=s.split(); c=p[0]
        if c=="print":
            v=p[1]
            o.append(str(m[v] if v in m else v) + "\n")
            i+=1
        elif c=="if":
            cond=" ".join(p[1:])
            tv=ev(cond,m); i+=1
            y,i=blk(a,i,("No","end")); n=[]
            if i<len(a) and a[i].strip()=="No": n,i=blk(a,i+1,("end",))
            if i<len(a) and a[i].strip()=="end": i+=1
            o+=run(y,m.copy()) if tv else run(n,m.copy())
        elif c=="for":
            v,st,en=p[1],p[2],p[3]
            sv=m[st] if st in m else int(st)
            evl=m[en] if en in m else int(en)
            b,i=blk(a,i+1,("end",))
            if i<len(a) and a[i].strip()=="end": i+=1
            for val in range(sv,evl+1):
                mm=m.copy(); mm[v]=val
                o+=run(b,mm)
        else: i+=1
    return o

def main():
    import sys
    ln=[x.rstrip("\n") for x in sys.stdin if x.strip()]
    v=ln[-2].split()
    vv=list(map(int,ln[-1].split()))
    mp=dict(zip(v,vv))
    code=ln[:-2]
    r=run(code,mp)
    sys.stdout.write("".join(r))

main()
