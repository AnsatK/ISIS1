def if_divisible(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
for i in if_divisible(24):
    print(i)