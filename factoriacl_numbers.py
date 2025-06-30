# def factorial(num):
#     result = 1
#     for i in range(2,num+1):
#         result *= i
#     return result    




# n= 5
# print("Fcatorial of",n, "is", factorial(n))



# def factorail(n):
#     if n==0 or n==1:
#         return 1
#     return n * factorail(n-1)

# print(factorail(5))      


# Ternery operator


def factorial(n):

    return 1 if (n==1 or n==0) else n * factorial(n-1)

print(factorial(5))


