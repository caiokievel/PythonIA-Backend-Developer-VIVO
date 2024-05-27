def countdown(n):
    while n > 0:
        yield n
        n -= 1


x = list(countdown(3))
print(x)
