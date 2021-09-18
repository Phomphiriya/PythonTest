n = int(input('Enter Input : '))
# for i in range(n + 1, -1, -1):
#     print('.' * i + '#' * (n + 2 - i), end = '')
#     print('+' + ( '+' * n if i == n + 1 or i == 0 else '#' * n) + '+')
# for i in range(n + 2):
#     print('#' + ( '#' * n if i == n + 1 or i == 0 else '+' * n) + '#', end = '')
#     print('+' * (n + 2 - i) + '.' * i)

k = n+1
k2 = n+1
for l in range(1,n+3):
    print("."*k,end='')
    print("#"*l,end='')
    if l == 1 or l == n+2:
        print("+"*(n+2),end='')
    else:
        print("+" + "#"*n + "+",end='')
    k -= 1
    print(end='\n')

for l in range(1,n+3):
    if l == 1 or l == n+2:
        print("#"*(n+2),end='')
    else:
        print("#" + "+"*n + "#",end='')
    print("+"*(k2+1),end='')
    print("."*(l-1),end='')
    k2 -= 1
    print(end='\n')

# test case
# 5
# ......#  +++++++
# .....##  +#####+
# ....###  +#####+
# ...####  +#####+
# ..#####  +#####+
# .######  +#####+
# #######  +++++++


# #######  +++++++
# #+++++#  ++++++.
# #+++++#  +++++..
# #+++++#  ++++...
# #+++++#  +++....
# #+++++#  ++.....
# #######  +......