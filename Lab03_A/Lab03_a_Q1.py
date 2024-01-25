#1.1A

n=int(input("enter n : "))
for n in range (0,6):
    for m in range (1,n+1,1):
        print (m,end=" ")
    print ()
    
    
    
#1.2A

def calculate_sum(n):
    result = 0
    for j in range(1, n + 1):
        result = result + j
    return result

n = int(input("Enter n: "))
print(calculate_sum(n))
        
