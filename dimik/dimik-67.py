x = int(input()) - 1
fib1 = 1
fib2 = 1
for i in range(x):
    fib1, fib2 = fib2, fib1 + fib2
print(fib1)
