#1 i iterator
print("First")
i = 1
while i < 6:
    print(i)
    i += 1

#2 break
print("Second")
i = 1
while i < 6:
    if i == 3:
        break
    i += 1

#3 continue
print("Third")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
#4 else 
print("Fourth")
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")