"""
start1 = int(input())
finish1 = int(input())
start2 = int(input())
finish2 = int(input())
isS1In2 = start2 <= start1 <= finish2
isF1In2 = start2 <= finish1 <= finish2
isS2In1 = start1 <= start2 <= finish1
isF2In1 = start1 <= finish2 <= finish1
answer = isF2In1 or isF1In2 or isS2In1 or isS1In2
print(answer)
"""
start1 = int(input())
finish1 = int(input())
start2 = int(input())
finish2 = int(input())
answer = start1 <= finish2 and start2 <= finish1
print(answer)
