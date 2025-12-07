import math

def helper(num, digit):
    if num % 10 == num:
        return num
    rem= num % 10
    return (rem * (10**digit)) + helper((num//10), digit-1)


def reverse(n):
    digit = int(math.log10(n))
    print(helper(n, digit))
    
reverse(2343)

