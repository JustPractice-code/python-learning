#sum of digits of a number
# def sum_digit(num):
#     if num == 0:
#         return 0
#     return (num%10) + sum_digit(num // 10)
# print(sum_digit(12345))

#reverse a string recursively
# def rev_str(char):
#     if char == "":
#         return ""
#     return rev_str(char[1:]) + char[0]
# print(rev_str("Jash"))

#print 1 to N recursively 
# def one_N(num):
#     if num == 0:
#         return
#     one_N(num-1)
#     print(num,end=" ")
# one_N(10)

#find max in list recursively
# def max_list(arr):
#     if len(arr) == 1:
#         return arr[0]
#     return max(arr[0],max_list(arr[1:]))
# print(max_list([1,5,3,2,5,3,6,99,1,10]))

#sum of first n natural number
# def sum_N(num):
#     if num == 0:
#         return 0
#     return num + sum_N(num-1)
# print(sum_N(5))

#count digits in a number
# def count_digit(num):
#     if num == 0:
#         return 0
#     return 1 + count_digit(num//10)
# print(count_digit(1234))

#prime number 
# def is_prime(n, divisor=2):
#     if n <= 1:   
#         return False
#     if divisor * divisor > n:   
#         return True
#     if n % divisor == 0:   
#         return False
#     return is_prime(n, divisor + 1)
# print(is_prime(29)) 

#GCD of two number
# def gcd(a, b):
#     if b == 0:  
#         return a
#     return gcd(b, a % b) 
# print(gcd(48, 18))   