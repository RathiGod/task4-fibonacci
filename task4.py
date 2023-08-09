n = int(input("Enter the number of fibonacci terms you want : "))
if (n>0):
    a = 0
    b = 1
    while n>0:
        print(a, end=' ')
        c = a+b
        a = b
        b = c
        n-=1


