# Program to show list methods

cars = ["Skoda", "Toyota", "Ferrari", "BMW"]
print("list index ", cars.index("BMW"))
cars.append("Ford")
print(" after append = ", cars)
print(" after pop = ", cars.pop())
cars.remove("Skoda")
print(" after remove = ", cars)
cars.insert(2, "Fiat")
print(" after insert = ", cars)
cars.clear()
print(" after clear = ", cars)