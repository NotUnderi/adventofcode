summa=[]
with open('day1',mode="r") as input:
    lista = input.read()
    lista = lista.split("\n\n")
    for x in range(len(lista)):
        lista[x]=lista[x].split("\n")
    for x in range(len(lista)):
        temp=0
        for x in lista[x]:
            try:temp+=int(x)
            except:pass
        summa.append(temp)
    print(max(summa))
    for x in range(len(summa)):
        if type(summa[x]) == None:
            print("Hep")
    summa.sort()
    temp=0
    for x in summa[-3:]:
        temp+=x
    print(temp)
XDXD