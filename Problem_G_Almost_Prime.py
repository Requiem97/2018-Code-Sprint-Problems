from math import ceil

def is_prime(num):
    n = ceil(num/2)
    if num != 2 and num % 2 == 0: return False
    for i in range(3, n):
        if num % i == 0:
            return False
    return True
def get_factors(num):
    factors = []
    for i in range(2, num + 1):
        if num % i == 0: factors.append(i)
    return factors
def almost_prime(num_list):
    count = 0
    if len(num_list) == 1:
        return 0
    for i in num_list:
        if is_prime(i): count += 1
    if count == 2: return 1
    else: return 0

try:
    inp = int(input())
    factors = []
    num_perfect_prime = 0
    for i in range(2, inp + 1):
        factors.append(get_factors(i))
    for i in factors:
        num_perfect_prime += almost_prime(i)
    print(num_perfect_prime)
except ValueError:
    print("Invalid Input")