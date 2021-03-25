#insertion sort

tablica=[]

n=5


for x in range(n):
    tablica.append(int(input()))

print(tablica)


for x in range(1,n):
    temp=[]
    element=tablica[x]
    #print(element)
    y=x-1
    while element<tablica[y] and y>=0:
        #print(y)
        tablica[y+1]=tablica[y]
        y-=1
    tablica[y+1]=element









print(tablica)
