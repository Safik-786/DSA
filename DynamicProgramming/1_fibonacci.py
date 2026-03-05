def fibonacci(n, memo={}):
    if n< 1 :
        return n;
    if memo.get(n, 0):
        return  memo[n]
    memo[n]= fibonacci(n-1, memo)+ fibonacci(n-2, memo)
    return memo[n]


print(fibonacci(2))