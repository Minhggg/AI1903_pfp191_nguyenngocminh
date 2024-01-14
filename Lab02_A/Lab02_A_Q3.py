#3.1
def recur_fun (a,n=0,tong=0):
    if n<=a:
        tong=tong+n
        n+=1
        return recur_fun(a,n,tong)
    else:
        return tong
res=recur_fun(10)
print(res)



#3.2
def display_student(name, age):
    print(name, age)

display_student('Emma', 26)


    