def checkVowel(char):
  sym = ["a","e","i","o","u","A","E","I","O","U"]
  strt = ""
  for i in char:
    if i in sym:
      pass
    else:
      strt += i
  return strt

char = str(input())
print(checkVowel(char))
