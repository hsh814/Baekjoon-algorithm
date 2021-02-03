n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

result = 0
gas = 0
for i in range(n - 1):
    if gas < dist[i]:
        gas += dist[i]
        result += cost[i] * dist[i]
        index = i + 1
        while index < n-1:
            if cost[i] <= cost[index]:
                result += cost[i] * dist[index]
                gas += dist[index]
            else:
                break
            index += 1
    gas -= dist[i]
print(result)
