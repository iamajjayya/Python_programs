def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(10))  

def primes():
    start  =  int(input("Enter a starting a value"))
    end = int(input("Enter a Ending value"))
    for i in range(start, end + 1):
        if is_prime(i):
            print(i,  end=" ")


primes()
