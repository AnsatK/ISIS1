
def upper_lower_counter(text):
    uc = sum(1 for c in text if c.isupper())
    lc = sum(1 for c in text if c.islower())
    return f"Uppercase: {uc}, Lowercase: {lc}"

input_text = input()
result = upper_lower_counter(input_text)
print(result)