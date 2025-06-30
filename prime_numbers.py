
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

print(is_prime(10))


def primes(num):
    num=10
    for i in range(2,num + 1):
        if is_prime(i):
            print(i, end=' ')

primes(20)               

