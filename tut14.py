# A math function to check the number is prime.
import math
def prime(n):
    for j in range(2, int(math.sqrt(n))+1):
        if n%j ==0:
            break
        else:
            return True

n = int(input("Enter the Number: "))
print(prime(n))
