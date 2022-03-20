# https://www.tutorialspoint.com/python_data_structure/index.htm

# warmup questions
# https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true
    


def countingValleys(steps, path):
    """count no. steps climbing up to sea level"""
    seaLevel = valley = 0

    for step in path:
        if step == 'U':
            seaLevel += 1
        else:
            seaLevel -= 1
        
        if step == 'U' and seaLevel == 0:
            valley += 1
    return valley


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
