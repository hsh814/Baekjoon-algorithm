M: list = []
MAX = 310

def M_init():
  for i in range(MAX):
    M.append(-1)

def ss(p_list: list) -> str:
  if p_list == ['(1)'] or p_list == ['0']:
    return p_list[0][1]
  if p_list == ['1', '1', '1', '1']:
    return "1"
  if p_list == ['0', '0', '0', '0']:
    return "0"
  result: str = "("
  for p in p_list:
    result += p
  return result + ")"

def zip(pic: list, n: int, x: int, y: int) -> str:
  if n == 1:
    return pic[x][y]
  result: list = list()
  half: int = n // 2
  result.append(zip(pic, half, x + 0, y + 0))
  result.append(zip(pic, half, x + 0, y + half))
  result.append(zip(pic, half, x + half, y + 0))
  result.append(zip(pic, half, x + half, y + half))
  return ss(result)

def main():
  n: int = int(input())
  picture: list = []
  for i in range(n):
    picture.append(input())
  #print("##########################")
  print(zip(picture, n, 0, 0))

main()
