#heap sort

def kop(tab,n,y):
    el=y

    if 2 * y + 1 < n and tab[2 * y + 1] > tab[el]:
        el = 2 * y + 1
    if 2 * y + 2 < n and tab[2 * y + 2] > tab[el]:
        el = 2 * y + 2

    if el!=y:
        temp = tab[y]
        tab[y] = tab[el]
        tab[el] = temp
        kop(tab,n,el)




def heapsort(tab,n):
    for x in range(n//2,-1,-1):
        kop(tab,n,x)

    for x in range(n-1,0,-1):
        temp = tab[x]
        tab[x] = tab[0]
        tab[0] = temp
        kop(tab, x, 0)


tablica=[]
n=5


for x in range(n):
    tablica.append(int(input()))

heapsort(tablica,n)

print(tablica)