#1 in operator
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")

#2 add method
fruits.add("orange")
print(fruits)

#3 update method
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

#4 remove method
fruits.remove("banana")
print(fruits)

#5 discard method
fruits.add("banana")
fruits.discard("banana")
print(fruits)