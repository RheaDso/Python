def findSum(n) :
    sum = 0
    x = 1
    while x <=n :
        sum += x
        x += 1
    return sum
n = 100
print (findSum(n))