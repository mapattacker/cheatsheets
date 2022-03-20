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


# sorting
# https://www.hackerrank.com/challenges/mark-and-toys/problem?isFullScreen=true

def maximumToys(prices, k):

    prices = sorted(prices)
    total = 0
    
    for cnt, price in enumerate(prices, 1):
        if total + price > k:
            return cnt - 1
        else:
            total += price         

            
# string manipulation
# https://www.hackerrank.com/challenges/alternating-characters/problem?isFullScreen=true

def alternatingCharacters(s):    
    duplicates = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            duplicates += 1
    return duplicates

def alternatingCharacters(s):
    """time complexity fail, but worthy solution"""
    deletion = 0
    while "AA" in s or "BB" in s:
        if "AA" in s:
            s = s.replace("AA", "A", 1)
            deletion += 1
        if "BB" in s:
            s = s.replace("BB", "B", 1)
            deletion += 1
    return deletion


# search
# https://www.hackerrank.com/challenges/pairs/problem?isFullScreen=true

from itertools import combinations
def pairs(k, arr):
    """use itertools but not the most efficient"""
    cnts = 0
    
    combi = list(combinations(arr, 2))
    for com in combi:
        diff = abs(com[0] - com[1])
        if diff == k:
            cnts += 1
    return cnts

def pairs(k, arr):
    """use plain nested iteration""""
    cnts = 0

    for i in range(len(arr)-1):
        for a in range(i+1, len(arr)):
            diff = abs(arr[i] - arr[a])
            if diff == k:
                cnts += 1
    return cnts



# LIST -------------------
a = [23,21,50,1,5]
# updating a value by index
a[0] = a[0] + 1
# removing a value
a.remove(23)
# get index from value
a.index(50)
# remove based on index
a.pop(0)


# WHILE LOOPS -------------------
# loop complete when len(a) == 0
while a:
    for i in a:
        a.remove(i)


# SORTING -------------------
# where possible, use python sorted function
# it uses Timsort, an efficient sorting method
sorted(a, reverse=True)

# ITERATION -------------------
# when we need to iterate but need to grab +1 or +x index after use this
for i in range(len(arr)-1):
    # do something

# if need to iterate nested, but need exclude those iterated in first nest
for i in range(len(arr)-1):
    for a in range(i+1, len(arr)):
        # do something
    
