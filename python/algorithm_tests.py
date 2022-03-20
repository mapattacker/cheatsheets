# https://www.tutorialspoint.com/python_data_structure/index.htm


# easiest questions
# https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?isFullScreen=true

def repeatedString(s, n):
    cnt_s = len(s)
    cnt_a_s = s.count("a")
    
    # num a in full s
    multiply = math.floor(n / len(s))
    cnt_a_full_s = cnt_a_s * multiply
    
    # num a in remainder s
    cnt_full_s = multiply * cnt_s
    remainder_s = n - cnt_full_s
    s_slice = s[:remainder_s]
    cnt_a_sliced_s = s_slice.count("a")
    
    return cnt_a_full_s + cnt_a_sliced_s


def rotLeft(a, d):
    for i in range(d):
        first_char = a[0]
        a.pop(0)
        a.append(first_char)
    return a



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


# array
# https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true

def hourglassSum(arr):
    max = 0
    
    for A in range(0, 4):
        
        for r in range(0,4):
            
            top = sum(arr[A][r:r+3])
            mid = arr[A+1][r+1]
            bottom = sum(arr[A+2][r:r+3] )
            hr_sum = top+mid+bottom
            
            if hr_sum > max: max = hr_sum
        
    return max





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
