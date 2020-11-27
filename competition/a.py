from typing import List, Set, Dict, Tuple

alphabet = "abcdefghijklmnopqrstuvwxyz"
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a: int = chr('a')
z: int = chr('z')
A: int = chr('A')
Z: int = chr('Z')

zero: int = chr('0')
nine: int = chr('9')


def cmp_to_key(mycmp):
  'Convert a cmp= function into a key= function'
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


def natural_compare(str1: str, str2: str) -> int:



def natural_sort(files: List[str]) -> List[str]:
  return sort(files, key=com_to_key(natural_compare))

def main():
  n: int = int(input())
  files: List[str] = []
  for i in range(n):
    files.append(input())
  files = natural_sort(files)
  for file in files:
    print(file)

main()
