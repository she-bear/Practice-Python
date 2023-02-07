def FibonacciR(f, n):
    if n == 1 or n == 2: 
        f[n-1] = 1
        return f[n-1]
    else:
        if f[n-1]:
            return  f[n-1]
        else:
            f[n-1] = FibonacciR(f, n-1) + FibonacciR(f, n-2)
            return f[n-1]


def FibonacciGood(n):   
    f = [0 for x in range(n)]
    FibonacciR(f, n)
    print(f)
    return FibonacciR(f, n)

n = 7
print(FibonacciGood(n))