spd = int(input("Your input :"))
# inp = int(spd)
if 0 <= spd < 52:
    print("breeze")
elif spd < 56:
    print("Depression")
elif spd < 102:
    print("Tropical Strom")
elif spd < 209:
    print("typhoon")
elif spd >= 209:
    print("Super typhoon")
else:
    print("error")