def forFloat(*args):
    count = len(args)
    if count == 2: #มี parameter 2 ตัว
        start = args[0]
        stop = args[1]
        while start < stop:
            print(round(start,2))
            start += 1            
    elif count == 3: #มี parameter 3 ตัว
        start = args[0]
        stop = args[1]
        step = args[2]
        while start < stop:
            print(round(start,2))
            start += step
    else: #มี parameter 1 ตัว
        stop = args[0]
        for i in range(stop):
            print(i)

inp = input("Enter : ").split(',')
if len(inp) == 1:
    stop = int(inp[0])
    forFloat(stop)
elif len(inp) == 2:
    start = float(inp[0])
    stop = float(inp[1])
    forFloat(start,stop)
else:
    start = float(inp[0])
    stop = float(inp[1])
    step = float(inp[2])
    forFloat(start,stop,step)