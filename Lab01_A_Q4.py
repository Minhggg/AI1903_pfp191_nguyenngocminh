n=-1
while (n<=0):
    n=int(input("enter decimal number :"))
result=""
while ((n/8)>0):
    result=str(n%8)+result
    n=n//8
print("to octal value",result)
      