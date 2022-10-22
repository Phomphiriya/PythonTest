inp1,inp2 = map(list,input("Enter your String : ").split())
inp1_copy = inp1.copy()
inp2_copy = inp2.copy()

inp1_copy = inp1_copy[-2:] + inp1_copy[:len(inp1)-2]
inp2_copy = inp2_copy[3:] + inp2_copy[:3]
round = 1
print(f'{round} {"".join(inp1_copy)} {"".join(inp2_copy)}')

while (inp1_copy != inp1 or inp2_copy != inp2):
    inp1_copy = inp1_copy[-2:] + inp1_copy[:len(inp1)-2]
    inp2_copy = inp2_copy[3:] + inp2_copy[:3]
    round += 1
    if round < 6 or (inp1_copy == inp1 and inp2_copy == inp2):
        print(f'{round} {"".join(inp1_copy)} {"".join(inp2_copy)}')
    elif round == 6:
        print(". . . . . .")

