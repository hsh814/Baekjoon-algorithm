
# https://docs.python.org/ko/3/howto/sorting.html?highlight=sorting#key-functions
def cmp_to_key(mycmp):
  class K:
    def __init__(self, obj, *args):
      self.obj = obj

    def __lt__(self, other):
        return mycmp(self.obj, other.obj) < 0

    def __gt__(self, other):
      return mycmp(self.obj, other.obj) > 0

    def __eq__(self, other):
      return mycmp(self.obj, other.obj) == 0

    def __le__(self, other):
      return mycmp(self.obj, other.obj) <= 0

    def __ge__(self, other):
      return mycmp(self.obj, other.obj) >= 0

    def __ne__(self, other):
      return mycmp(self.obj, other.obj) != 0
  return K

def is_digit(c: str) -> bool:
  return zero <= ord(c) <= nine


def parser(s: str) -> list:
  result: list = []
  temp: list = []
  digit: bool = is_digit(s[0])
  for c in s:
    if digit != is_digit(c):
      #print("temp: ", temp)
      result.append("".join(temp))
      temp.clear()
    digit = is_digit(c)
    temp.append(c)
  result.append("".join(temp))
  return result

def compare_str(str1: str, str2: str) -> int:
  if str1 == str2:
    return 0
  d1 = is_digit(str1[0])
  d2 = is_digit(str2[0])
  if d1 and d2:
    i1 = int(str1)
    i2 = int(str2)
    if i1 == i2:
      if len(str1) < len(str2):
        return -1
      else:
        return 1
    elif i1 < i2:
      return -1
    else:
      return 1
  if not d1 and not d2:
    if str1 < str2:
      return -1
    else:
      return 1
  if d1:
    return -1
  else:
    return 1

def natural_compare(str1: str, str2: str) -> int:
  s1 = parser(str1)
  s2 = parser(str2)
  l1 = len(s1)
  l2 = len(s2)
  for i in range(min(l1, l2)):
    if compare_str(s1[i], s2[i]) != 0:
      return compare_str(s1[i], s2[i])
  if l1 < l2:
    return -1
  elif l1 == l2:
    return 0
  else:
    return 1


def natural_sort(files: list) -> list:
  return sorted(files, key=cmp_to_key(natural_compare))

def lab_result(lab: list, n: int, k: int) -> list:
  print(lab, n, k)
  return []

def main():
  temp = input()
  n = int(temp.split()[0])
  k = int(temp.split()[1])
  lab = list()
  for i in input().split():
    lab.append(int(i))
  result = lab_result(lab, n, k)
  if not result:
    print(-1)
  else:
    print(" ".join(result))


main()