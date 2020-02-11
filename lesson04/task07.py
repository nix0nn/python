def fibo_gen(n):
    y = 1
    for x in range(1, n+1):
        y *= x
        yield y


for x in fibo_gen(15):
    print(x)