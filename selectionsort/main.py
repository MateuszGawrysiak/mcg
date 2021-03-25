#selection sort

tablica=[]
n=5

for x in range(n):
    tablica.append(int(input()));

print(tablica)

indeks=0
for x in range(n):
    mini = tablica[x]
    indeks=x
    for y in range(x+1,n):
        if tablica[y]<mini:
            mini=tablica[y]
            indeks=y
    tablica[indeks]=tablica[x]
    tablica[x]=mini
    print(tablica)



print(tablica)