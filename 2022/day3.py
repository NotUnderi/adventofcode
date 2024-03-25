import os
import string
os.chdir(os.path.dirname(os.path.abspath(__file__)))
bag1=[]
bag2=[]
flag=0

with open("day3") as input:
    rucksack = input.read().split("\n")    
    for x in rucksack:
        bag1.append(x[:len(x)//2])
        bag2.append(x[len(x)//2:])

def round1():
    tprio=0
    prio = dict()
    for i, x in enumerate(string.ascii_letters):
        prio[x] = i+1
    for i1,x in enumerate(bag1):
        flag=0
        for i2,l in enumerate(x):
            if flag==1:break
            if bag1[i1].find(bag2[i1][i2]) != -1:
                flag=1
                tprio += prio[bag2[i1][i2]]
    print(tprio)

def round2():
    tprio=0
    c=0
    index=0
    prio = dict()
    groups = [[] for _ in range(75)]
    for i, x in enumerate(string.ascii_letters):
        prio[x] = i+1

        #slightly plagiarized solution from elsewhere but with better priority counting :D
    while len(rucksack) > 0:
        first = set(rucksack.pop()) 
        second = set(rucksack.pop())
        third = set(rucksack.pop())
        com = ((first.intersection(second)).intersection(third)).pop()
        tprio += prio[com]
    print(tprio)






#round1()
round2()