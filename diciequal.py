def diciequal(a,b):
    if len(a)!=len(b):
        return False
    for i in a:
        if i not in b or a[i]!=b[i]:
            return False
    return True

a={1:2,3:4}
b={1:2,3:4}

ans = diciequal(a,b)

print(ans)