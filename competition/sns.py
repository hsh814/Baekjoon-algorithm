M: list = []
MAX = 310

def M_init():
  for i in range(MAX):
    M.append(-1)

def step(st: list, n: int) -> int:
  if n < 1:
    return 0
  if n == 1:
    M[n] = st[n]
    return M[n]
  if n == 2:
    M[n] = max(st[1] + st[2], st[2])
    return M[n]
  if n == 3:
    M[n] = max(st[1] + st[3], st[2] + st[3])
    return M[n]
  M[1] = st[1]
  M[2] = max(st[1] + st[2], st[2])
  M[3] = max(st[1] + st[3], st[2] + st[3])
  for i in range(4, n + 1):
    M[i] = max(M[i - 2] + st[i], st[i] + M[i - 3] + st[i - 1])
  return M[n]

def main():
  n: int = int(input())
  cases: list = []
  M_init()
  cases.append(n)
  for i in range(n):
    cases.append(int(input()))
  #print("##########################")
  print(step(cases, n))

main()
