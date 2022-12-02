#1 Rock = A/X
#2 Paper = B/Y
#3 Scissors = C/Z

# X = lose
# Y = draw
# Z = win

score=0
with open("day2") as input:
    strat = input.read().split("\n")
    strat = [x.split(" ") for x in strat]

plan={"X":0,"Y":3,"Z":6}
for x in strat[:-1]:
    if x[1]=="X":
        score+=1
        if x[0]=="A":
            score+=3
        if x[0]=="B":
            score+=1
        if x[0]=="C":
            score+=2
    if x[1]=="Y":
        score+=2
        if x[0]=="A":
            score+=1
        if x[0]=="B":
            score+=2
        if x[0]=="C":
            score+=3
    if x[1]=="Z":
        score+=3
        if x[0]=="A":
            score+=2
        if x[0]=="B":
            score+=3
        if x[0]=="C":
            score+=1
print(score)
score=0
for x in strat[:-1]:
    score+=plan[x[1]]
    if x[1]=="X":
        if x[0]=="A":
            score+=3
        if x[0]=="B":
            score+=1
        if x[0]=="C":
            score+=2
    if x[1]=="Y":
        if x[0]=="A":
            score+=1
        if x[0]=="B":
            score+=2
        if x[0]=="C":
            score+=3
    if x[1]=="Z":
        if x[0]=="A":
            score+=2
        if x[0]=="B":
            score+=3
        if x[0]=="C":
            score+=1
print(score)