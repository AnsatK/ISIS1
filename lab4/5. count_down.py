def count_down(n):
    for i in range(n+1):
        yield n-i
for i in count_down(7):
    print(i)