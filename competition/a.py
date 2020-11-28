"""
def even_list(arr:list) -> list:
  result: list = list()
  for i in range(len(arr)):
    if i % 2 != 0:
      result.append(arr[i])
  return result

def odd_list(arr:list) -> list:
  result: list = list()
  for i in range(len(arr)):
    if i % 2 == 0:
      result.append(arr[i])
"""
"""
def triple_sort(arr: list, n: int) -> bool:
  even_list = list()
  odd_list = list()
  for i in range(n):
    if i % 2 == 0:
      odd_list.append(arr[i])
    else:
      even_list.append((arr[i]))
  even = sorted(even_list)
  odd = sorted(odd_list)
  r: list = list()
  for i in range(n // 2):
    r.append(odd[i])
    r.append(even[i])
  if n % 2 == 1:
    r.append(odd[-1])
  for j in range(n - 1):
    if r[j] > r[j + 1]:
      return False
  return True
"""

def triple_sort(arr: list, n: int) -> bool:
  for i in range(n):
    if i % 2 == 0:
      if arr[i] % 2 == 0:
        return False
    else:
      if arr[i] % 2 != 0:
        return False
  return True

def main():
  n: int = int(input())
  arr: list = input().split(' ')
  na = list()
  for a in arr:
    na.append(int(a))
  if triple_sort(na, n):
    print("YES")
  else:
    print("NO")

main()
