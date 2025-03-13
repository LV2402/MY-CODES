#reverse and palindrome

def fun(x):
    r=0
    while x>0:
        a=x%10
        r=r*10+a
        x=x//10
    return r

def isP(x):
    if x==fun(x):
        return True
    return False