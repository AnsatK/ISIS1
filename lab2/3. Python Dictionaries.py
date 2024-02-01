#1 get method
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))

#2 chainging value by keyword
car["year"] = 2020
print(car)

#3 adding new pair
car["color"] = "red"
print(car)

#4 pop method 
car.pop("model")
print(car)

#5 clear method
car.clear()
print(car)