import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True

def sum_of_primes(start, end):
    prime_sum = sum(num for num in range(start, end + 1) if is_prime(num))
    return prime_sum

# Example usage
start, end = 10, 50
print(f"Sum of prime numbers between {start} and {end}: {sum_of_primes(start, end)}")
