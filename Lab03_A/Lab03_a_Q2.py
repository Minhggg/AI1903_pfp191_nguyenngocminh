#2.1A

def print_number(numbers):
    for num in numbers:
        if num % 5 == 0:
            if num > 150 and num <= 500:
                continue
            elif num > 500:
                break
            print(num)
                
# test
numbers = [11,33,67,75,150,145,151,505,15]
print_number(numbers)


#2.2A


def count_digist_of_number (number):
    return len(str(number))

number = 123445
total_digist  = count_digist_of_number (number)
print("total digist of number : ",total_digist)


#2.3A 

my_list = [1, 2, 3, 4, 5]
reversed_list = []
for item in my_list:
    reversed_list.insert(0, item)
print(reversed_list)
