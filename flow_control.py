#Write a function that uses while, if and continue statements to 
# print all the even numbers between 0 and 50. 

def even_numbers():
    num=0
    while num<50:
        if num%2==0:
           print(num)
        num+=1   
        continue

# Write a function that takes an integer argument and prints "Prime" 
# if the number is prime, and "Not prime" if the number is not prime.

def get_prime_numbers(num):
    if num>=1:
        for i in range(2,num):
            if num%2==0:
                print(f"{num} is not Prime")
                break
        else:
            print(f"{num} is Prime")

# Write a function that takes a list of integers as input and prints
#  the sum of all the even numbers in the list.

def sum_of_even(numbers):
    sum=0
    for i in numbers:
        if i%2==0:
            sum+=i
    print(sum)

# Write a function that takes any two integers as input, and prints the sum of 
# all the numbers between the two integers (inclusive) that are divisible by 3.

def  sum_of_all_numbers(x,y):
    empty=[]
    for i in range(x,y):
        if i%3==0:
            empty.append(i)
    print(empty)
    

        
    

