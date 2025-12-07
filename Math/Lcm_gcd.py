def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# in this problem first think about the  what u have to in b section( a%b ot b%a)
def gcdRecursion(a, b):
    if a==0:
        return b;
    gcdRecursion(b%a, a)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_three(a, b, c):
    return lcm(lcm(a, b), c)

print("LCM of 2, 4, 9:", lcm_three(2, 4, 9))