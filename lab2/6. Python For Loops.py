#1 For x in y
print("First")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
#2 continue
print("Second")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        print(x)
#3 range 
print("Third")
for x in range(6):
    print(x)
#4 break
print("Fourth")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)