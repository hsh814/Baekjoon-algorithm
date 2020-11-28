def count(s: str, c: str) -> int:
  n = 0
  for temp in s:
    if temp == c:
      n += 1
  return n

def thanos(s: str) -> str:
  zero = count(s, '0')
  one = count(s, '1')
  result = list()
  zn = 0
  on = 0
  for i in range(len(s)):
    if s[i] == '0':
      if zn < zero // 2:
        #print("zero", i)
        result.append(s[i])
      zn += 1
    else:
      if on >= one // 2:
        #print("one", i)
        result.append(s[i])
      on += 1
  return "".join(result)


def main():
  s: str = input()
  print(thanos(s))

main()
