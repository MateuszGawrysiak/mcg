#quick sort
import random

def div(tab,l,r):
    tilt=l+(r-l)//2
    w=tab[tilt]

    temp=tab[tilt]
    tab[tilt]=tab[r]
    tab[r]=temp

    p=l
    for x in range(l,r-l):
        if tab[x]<w:
            temp=tab[x]
            tab[x]=tab[p]
            tab[p]=temp
            p+=1

    temp=tab[p]
    tab[p]=tab[r]
    tab[r]=temp

    return p


def quicksort(tab,l,r):
    if l<r:
        t=div(tab,l,r)
        quicksort(tab,l,t-1)
        quicksort(tab,t+1,r)


tablica=[]
n=5


for x in range(n):
    tablica.append(int(input()))

"""a=tablica[random.randrange(n)]
b=tablica[random.randrange(n)]
c=tablica[random.randrange(n)]

if(a>=b>=c) or (c>=b>=a): tilt=b
elif(a>=c>=b) or (b>=c>=a): tilt=c
else: tilt=a

print(a,b,c,tilt)"""

quicksort(tablica,0,n-1)

print(tablica)