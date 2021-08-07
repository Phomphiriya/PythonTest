print("*** Election ***")
n = int(input("Enter a number of voter(s) : "))

if n <= 20:
    inp = list(map(int,input("Enter number : ").split()))
    candidate = 0
    max = 0
    for i in inp:
        if inp.count(i) > max and i > 0:
            max = inp.count(i)
            candidate = i

    if candidate == 0:
        print("Fail candidate")
    else:
        print(candidate)
else:
    print("Error")