import sys

div: int = (10 ** 9 + 7)

def bench_sum(benchs: list, n: int, start: int) -> list:
  num: int = 0
  multiple: int = start * benchs[n - 1]
  save = multiple
  if len(benchs) == n:
    return [save, multiple]
  for i in range(len(benchs) - n):
    num += multiple
    multiple //= benchs[i]
    multiple *= benchs[n + i]
  num += multiple
  return [save, num % div]

def bench_num(benchs: list, n: int) -> int:
  num = 0
  save = 1
  for i in range(1, n):
    result: list = bench_sum(benchs, i, save)
    num += result[1]
    save = result[0]
  return num

def main():
  n: int = int(input())
  a = sys.stdin.readline().rstrip()
  temp: list = a.split(' ')
  benchs = list()
  for t in temp:
    benchs.append(int(t))
  print(bench_num(benchs, n) % (div))


main()
