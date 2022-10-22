def decToRoman(num):
    num = int(num)
    roman = ""
    dec = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    sym = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    i = 0
    while num > 0:
        div = num // dec[i]
        num = num % dec[i]
        while div > 0:
            roman += sym[i]
            div -= 1
        i += 1
    print (roman)
    return roman

def romanToDec(roman):
    roman = str(roman)
    sym = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
    num = 0
    i = 0
    while i < len(roman):
        if i+1<len(roman) and roman[i:i+2] in sym:
            num += sym.get(roman[i:i+2])
            i += 2
            continue
        else:
            num += sym.get(roman[i])
            i += 1
    print (num)
    return num

inp = input("Enter your number : ")
# romanToDec(decToRoman(inp))
romanToDec(inp)