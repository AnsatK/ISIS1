def count_lines(text):
    try:
        with open(text, 'r') as file:
            count = 0
            for l in file:
                count+=1
        return f"The number of lines in '{text}' is: {count}"
    except FileNotFoundError:
        return f"Error: File '{text}' not found."

p= "sa.txt"
result = count_lines(p)
print(result)