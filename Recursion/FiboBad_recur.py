def FibonacciBad(n):
    if n == 1 or n == 2: 
        return 1
    else: 
        return FibonacciBad(n-1) + FibonacciBad(n-2)
    

n = 6
print(FibonacciBad(n))    