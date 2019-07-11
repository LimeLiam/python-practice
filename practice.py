import string
#(0°C × 9/5) + 32 = 32°F
def CToF():
    c = -40
    f = c * (9 / 5) + 32
    return f

def FToC():
    f = -40
    c = (f - 32) * 5 / 9
    return c

def addFunction(x, y, z):
    return x + y + z

def counter(n):
    while n > 1:
        return n
        n -=1

def maxNums(a, b ,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif c > b:
        return c
    else:
        return b

def tri(side1, side2, side3):
    if side1 == side2 == side3:
        return "That's an equilateral triangle!"
    elif side1 == side2 or side2 == side3 or side1 == side3:
        return "That's an isosceles triangle!"
    else:
        return "That's a scalene triangle!"

def median(a, b, c):
    if a > b > c or c > b > a:
        return b;
    elif b > a > c or c > a > b:
        return a;
    elif a > c > b or b > c > a:
        return c;

def sumFunction(x):
    total = 0
    for a in x:
        total += a
    return total

def avgFunction(x):
    total = 0
    for a in x:
        total += a
    y = len(x)
    total /= y
    return total

def nSquares(n):
    ls = []
    x = 1
    for i in range(n):
        ls += [x**2]
        x += 1
    return ls

def isIn(x, y): # x is the character being looked for, y is the list
    for i in y:
        if i == x:
            return True
    else:
        return False

def charCount(x):
    letters = 0
    numbers = 0
    for char in x: #seperates each character
        if isIn(char, string.ascii_letters) == True:
            letters += 1
        elif isIn(char, string.digits) == True:
            numbers += 1
        else:
            continue
    return (letters, numbers)

def oddNums(x):
    oddNumbers = 0 #The number of odd numbers
    for i in x: #For each item in the list x
        if i % 2 != 0: #Check if the remainder of the item divided by 2 is 0, if not, add 1 to oddNumbers variable
            oddNumbers += 1
    return oddNumbers

def password(password):
    upper = 0 #At least one
    lower = 0 #At least one
    nums = 0 #At least one
    #Should be 8-32 characters
    if 8 <= len(password) <= 32:
        charLength = True
    else:
        charLength = False
    for char in password:
        if isIn(char, string.ascii_lowercase):
            lower += 1
        if isIn(char, string.ascii_uppercase):
            upper += 1
        if isIn(char, string.digits):
            nums += 1
    if lower >= 1 and upper >= 1 and nums >= 1 and charLength == True:
        return "Valid password entered."
    else:
        return "Invalid password! Your password must have at least 1 uppercase, 1 lowercase, 1 number, and must be between 8 and 32 characters."


def revTerm(x):
    y = -1
    revStr = "" #creates empty string to later append to
    for i in x:
        revStr += x[y]
        y-=1
    return revStr

def tacocat(palindrome):
    if revTerm(palindrome) == palindrome:
        return True
    else:
        return False

def lazyDog(pangram):# subscribe to Pew Die Pie
    pg = pangram.lower()#turns everything lowercase
    for i in string.ascii_lowercase:
        if isIn(i, pg):
            return True   
        else:
            return False
#17
def unique(ls):
    return_list = [] #Creates a return list to later return
    for i in ls:
        a = ls.count(i) #sets a variable to check how many time i is in ls
        if a <2: #if it is included less than twice, simply record it in return_list
            return_list += i
        elif a >= 2: #otherwise, check if it is in the return list before inputting it
            if return_list.count(i) == 1:
                continue
            else:
                return_list += i 
    return return_list
#18
def isPrime(n):
    for i in range(2, n-1):
        if n%i !=0:
            return True
        else:
            return False 

"""99 reports of bugs in the code, 99 reports of bugs!
Take one down fix it around, 144 bugs in the code!
144 bugs in the code, 144 bugs!
Take one down, fix it around, 34,000 bugs in the code!"""






