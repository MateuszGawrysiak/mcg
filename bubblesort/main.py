#bubble sort

tablica=[]
n=5

for x in range(n):
    tablica.append(int(input()));

print(tablica)

p=1

while p==1:
    p=0
    for x in range(n-1):
        if tablica[x]>tablica[x+1]:
            temp=tablica[x]
            tablica[x]=tablica[x+1]
            tablica[x+1]=temp
            p=1

print(tablica)