print("*** Election ***")
n = int(input("Enter a number of voter(s) : "))

if n <= 20:
    inp = list(map(int,input("").split()))
    candidate = 0
    max = 0
    for i in inp:
        # print(inp.count(i))
        if inp.count(i) > max and i > 0:
            max = inp.count(i)
            candidate = i
    if candidate == 0:
        print("*** No Candidate Wins ***")
    else:
        print(candidate)
elif n >20:
    print("*** No Candidate Wins ***")
else:
    print("*** No Candidate Wins ***")