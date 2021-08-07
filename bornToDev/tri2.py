inp = int(input())

for i in range(inp):
  print(" "*(inp-i-1),end='')
  print("*"*(i*2+1))