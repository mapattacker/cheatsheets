# https://www.tutorialspoint.com/python_data_structure/index.htm


# LIST -------------------
a = [23,21,50,1,5]
# updating a value by index
a[0] = a[0] + 1
# removing a value
a.remove(23)
# get index from value
a.index(50)


# WHILE LOOPS -------------------
# loop complete when len(a) == 0
while a:
    for i in a:
        a.remove(i)



# SORTING -------------------
# where possible, use python sorted function
# it uses Timsort, an efficient sorting method
sorted(a, reverse=True)