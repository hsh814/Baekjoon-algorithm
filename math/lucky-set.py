import sys
L = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
n = int(sys.stdin.readline().rstrip())

nums.sort()
index = -1
for i in range(L):
    if nums[i] >= n:
        index = i
        break

if index == 0:
    result = (nums[index] - n) * n - 1
    if result < 0:
        print(0)
    else:
        print(result)
elif nums[i] == n:
    print(0)
else:
    left = nums[i - 1]
    right = nums[i]
    result = (right - n) * (n - left) - 1
    print(result)