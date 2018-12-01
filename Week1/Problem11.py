# counting of how many it will cost in cents and dollars
a = int(input())
b = int(input())
n = int(input())
count = a*100 + b
print((count * n) // 100, (count * n) % 100)
