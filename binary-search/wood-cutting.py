def cut_woods(woods, height):
    if True:
        left = 0
        right = len(woods)
        while True:
            if right - left <= 8:
                start = left
                break
            start = (left + right) // 2
            if woods[start] > height:
                right = start
            elif woods[start] < height:
                left = start
            else:
                break
    result = 0
    for i in range(start, len(woods)):
        if woods[i] > height:
            result += woods[i] - height
    return result

def wood_wood(woods, n, m):
    result = 0
    left = 0
    right = woods[n - 1]
    while left <= right:
        start = (left + right) // 2
        length = cut_woods(woods, start)
        if length > m:
            left = start + 1
        elif length < m:
            right = start - 1
        else:
            return start
    return right


n, m = map(int, input().split())
woods = list(map(int, input().split()))
woods.sort()
result = wood_wood(woods, n, m)
print(result)