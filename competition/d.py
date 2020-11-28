import sys

div: int = (10 ** 9 + 7)

def bench_sum(benchs: list, n: int, history: list) -> list:
  num: int = 0
  if len(benchs) == n:
    return [history, history[0] * benchs[n - 1]]
  for i in range(len(benchs) - n):
    history[i] = history[i] * benchs[n + i]
    num += history[i]
  return [history, num]

def bench_num(benchs: list, n: int) -> int:
  num = 0
  history: list = benchs.copy()
  for i in range(1, n):
    result: list = bench_sum(benchs, i, history)
    num += result[1]
    history = result[0]
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
