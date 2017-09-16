
def fibonacci_sequence(end, start=1):
    n = start
    fib_arr = []
    a = 0
    b = 1

    while n < end:
        fib_arr.append(n)
        n = a + b
        a = b
        b = n



    return fib_arr


print(fibonacci_sequence(30))