def square(n):
    for i in range(n+1):
        yield i*i
for j in square_n(5):
    print(j)