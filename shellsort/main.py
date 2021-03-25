#shell sort
import math

tablica=[]
shell=[]
n=12
x=1
while (3**x-1)//2<=math.ceil(n/3):
    shell.append((3**x-1)//2)
    x+=1
shell=shell[::-1]
#print(shell)

for x in range(n):
    tablica.append(int(input()))

#print(tablica)

indeks=0
for z in range(len(shell)):
    for x in range(shell[z],n):
        #print(x)
        temp = []
        element = tablica[x]
        # print(element)
        y = x
        while element < tablica[y-z] and y >= z:
            #print(y)
            tablica[y] = tablica[y-z]
            y -= z
        tablica[y] = element
    #print(shell[z],tablica)



print(tablica)
