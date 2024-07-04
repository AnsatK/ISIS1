def generate_even_numbers(n):
    for i in range(n+1):
        if i%2==0:
            yield i
n = int(input("Enter a number:"))

print(*[i for i in generate_even_numbers(n)], sep = ', ')