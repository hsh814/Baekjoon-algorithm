M: list = [0, 1, 1, 1, 2, 2]
MAX = 100

def M_init():
  for i in range(MAX):
    M.append(-1)

def padoban(n: int) -> int:
  if n <= 0:
    return 0
  if n <= 3:
    return 1
  if M[n] != -1:
    return M[n]
  M[n] = padoban(n - 1) + padoban(n - 5)
  return M[n]

def main():
  n: int = int(input())
  cases: list = []
  M_init()
  for i in range(n):
    cases.append(int(input()))
  for case in cases:
    print(padoban(case))

main()
