def torWord(inp):
    ls = []
    temp = ""
    for i in inp:
        word = i.split()
        if word[0] == "P":
            if ls == []:
                temp = word[1]
                ls.append(temp)
            else:
                old = temp[-1:-2]
                new = word[1][0:2]
                old = old.lower()
                new = new.lower()
                if old == new:
                    ls.append(word[1])
                    temp = word[1]
                else:
                    return "Game Over"
        elif word[0] == "R":
            ls = []
            return "Game Restarted"
        elif word[0] == "X":
            return ls
        else:
            return "Invaild Input"

inp = list(map(str,input("Enter your word : ").split(',')))
print(torWord(inp))