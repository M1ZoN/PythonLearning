# in how many days can ********* reach the height h going a at day move back b at night
from math import ceil
h = float(input())
a = float(input())
b = float(input())
print(ceil((h-a)/(a-b)+1))
