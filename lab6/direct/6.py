import string
alphabet = list(string.ascii_uppercase)
for i in alphabet:
        
        i = i + '.txt'
for i in alphabet:
        with open(i, 'w') as file:
            file.write('')
        