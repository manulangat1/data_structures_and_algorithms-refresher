def fibonnaci(n):
    # if n < 0:
    #     return 0
    assert n >= 0 and int(n) == n, "fib num cannot be negative or non integer"
    if n in [0, 1]:
        return n

    return fibonnaci(n-1) + fibonnaci(n-2)


print(fibonnaci(100))
