play = {"bum":[1,1], "poo":[2,4]}
if "bum" in play:
    print("wee")

print(len(play))
play["wee"] = [5,len(play)+1]
print(play["wee"])

play["fart"] = [1, 2]
print(play["fart"])

for key in play:
    if play[key][1] == 2:
        print(key)