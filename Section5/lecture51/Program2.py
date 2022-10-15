# program to filter a list and create new list

list1 = ["David", "Sam",
         "Adam", "Don", "Fred", "Dante", "Paul"]
filtered_list = [s for s in list1 if s.startswith("D")]
print("Filtered list : ", filtered_list)