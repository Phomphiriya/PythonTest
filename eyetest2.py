while True:
    inp = int(input("Enter your input : "))
    if inp != "e" or inp != 'E':
        for i in range(13):
            print(f'{inp} x {i} = {inp*i}')
    else:
        break