def fun(i,n):
    if i>n:
        return
    fun(i+1,n)
    print(i,end=" ")

n=int(input("Enter a number: "))
fun(1,4)