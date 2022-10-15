# Program to show lambda functions

cube = lambda n: n**3
print("cube(3) = ", cube(3))
# using lambda and map
cubes = list(map(lambda n: n**3,[1, 2, 3, 4, 5]))
print("cubes =", cubes)
# using lambda and filter
filtered_list = list(filter(lambda n: n > 10,
                            [21, 1, 2, 32, 4, 23, 17]))
print("filtered list = ", filtered_list)


