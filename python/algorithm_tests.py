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

def repeatedString(s, n):
    """using modulus""""
    len_s = len(s)
    counts_in_s = s.count("a")
    
    if n < len_s:
        return s[:n].count("a")
    elif n == len_s:
        return counts_in_s
    else:
        repeats = math.floor(n/len_s )
        modulus = n % len_s
        if modulus == 0:
            return counts_in_s * repeats
        else:
            return (counts_in_s * repeats) + s[:modulus].count("a")


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


def jumpingOnClouds(c):
    jump = 0
    while len(c) > 2:
        if c[2] != 1:
            c = c[2:]
        else:
            c = c[1:]
        jump += 1

    if len(c) == 2:
        jump += 1
        
    return jump


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
    toy_list = []
    toys = sorted(prices)
    
    for toy in toys:
        toy_list.append(toy)
        if sum(toy_list) > k:
            break
    return len(toy_list) - 1

            
# string manipulation
# https://www.hackerrank.com/challenges/alternating-characters/problem?isFullScreen=true

def alternatingCharacters(s):    
    duplicates = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            duplicates += 1
    return duplicates

# not as good in terms of time complexity
def alternatingCharacters(s):
    flag = True
    x = s
    
    while flag:
        len_before = len(x)
        x = x.replace("AA", "A").replace("BB","B")
        if len_before == len(x):
            flag = False

    return len(s) - len(x)


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

def pairs(k, arr):    
    pairs = 0
    for cnt, a in enumerate(arr):
        for b in arr[cnt+1:]:
            if abs(a-b) == k:
                pairs+=1
    return pairs



# dict & hasimaps
# https://www.hackerrank.com/challenges/two-strings/problem?isFullScreen=true
    
def twoStrings(s1, s2):
    for letter in s1:
        if letter in s2:
            return "YES"
    return "NO"



# MODULUS -------------------
# e.g. test if it is a full divisioin
10 % 5 # out: 0
# e.g. get remainder
11 % 5 # out: 1

x = divmod(5, 2) # out: (2, 1)


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


# BINARY TREE -------------------
# the most efficient algorithm through divide & conquer methods
def binary_search(list1, n):
    """https://www.javatpoint.com/binary-search-in-python
    list needs to be integer, unique, and sorted"""
    low = 0  
    high = len(list1) - 1  
    mid = 0  
  
    while low <= high:    
        mid = (high + low) // 2  
        if list1[mid] < n:  
            low = mid + 1  
        elif list1[mid] > n:  
            high = mid - 1  
        else:  
            return mid  
    return -1  


# CLASSES -------------------
# __init__ passes variables to all methods in class
# all methods in class requires self
# all shared methods requires self.<variable_name>

class captcha:
    
    def __init__(self, model_path="model.json"):
        """Initialize variables & model"""
        # pixel positional heights and widths to extract 5 chars in a captcha
        self.h_min, self.h_max = 11, 21
        self.w_start_list = [5, 14, 23, 32, 41]
        self.w = 8

        f = open(model_path)
        self.model = json.load(f)

    
    def clean_image(self, img, bg_threshold=0.2, char_threshold=0.5):
        """Remove texture & fix char color based on thresholds"""
        img[img >= char_threshold] = 1.0
        img[img <= bg_threshold] = 0.0
        return img
