def calculate_love_score(name1, name2):

    finalword=name1+name2

    tcount = 0
    for trueletter in finalword:
        if trueletter == "t":
            tcount += 1
        elif trueletter == "r":
            tcount += 1
        elif trueletter == "u":
            tcount += 1
        elif trueletter == "e":
            tcount += 1
    print(f"Total={tcount}")

    lcount=0
    for loveletter in finalword:
        if loveletter == "l":
            lcount += 1
        elif loveletter == "o":
            lcount += 1
        elif loveletter == "v":
            lcount += 1
        elif loveletter == "e":
            lcount += 1

    print(f"Total={lcount}")

    print(f"Love Score = {tcount}{lcount}")

calculate_love_score("Angela Yu", "Jack Bauer")