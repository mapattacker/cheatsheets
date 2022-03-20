# https://www.tutorialspoint.com/python_data_structure/index.htm

# warmup questions
# https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true




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


def jumpingOnClouds(c):
    """use while loop or recursive"""
    jumps = 0
    # "000" = 2
    # "010" = 2
    # "00" = 1
    c = "".join(str(i) for i in c)
    while len(c) > 1:
        if c[:3] == "000":
            c = c.replace("000", "00", 1)
        if c[:2] == "00":
            c = c.replace("00", "0", 1)
            jumps += 1
        if c[:3] == "010":
            c = c.replace("010", "0", 1)
            jumps += 1
            
    return jumps




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
