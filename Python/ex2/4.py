plus = 0
minus = 0
have = False
while True:
  check = int(input())
  if check == 0: break
  elif check > 0: plus+=1
  else: minus+=1
  have = True
if have: print(f"There is {plus} positive number \nThere is {minus} negative number")
else: print("No Data")