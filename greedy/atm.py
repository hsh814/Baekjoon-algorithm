temp = input()
nums = list(map(lambda s: int(s), input().split()))
nums.sort()
result = 0
sum = 0
for num in nums:
    sum += num
    result += sum
print(result)
