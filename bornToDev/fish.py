inp = []
i = 0

while True:
    a = input()
    if a == '0':
        break
    inp.append(a)
if input().lower() == "max":

    print(' '.join(sorted(inp,reverse=True)))
else:

    print(' '.join(sorted(inp)))