#merge sort

def merge(tablica,p,q,r):
    #print(tablica,p,q,r)
    lewa=tablica[p:q+1]
    prawa=tablica[q+1:r+1]
    #print(lewa,prawa)

    x=0
    y=0
    k=p

    while x<len(lewa) and y<len(prawa):
        if lewa[x]<prawa[y]:
            tablica[k]=lewa[x]
            x+=1
        else:
            tablica[k]=prawa[y]
            y+=1
        k+=1

    while x<len(lewa):
        tablica[k]=lewa[x]
        x+=1
        k+=1

    while y<len(prawa):
        tablica[k]=prawa[y]
        y+=1
        k+=1

    #print(tablica, p, q, r,"..",lewa,prawa)

def divide(tablica,p,r):
    #print(p,r)
    if p<r:
        q=(p+(r-1))//2
        #print(p, q, r)
        divide(tablica,p,q)
        divide(tablica,q+1,r)
        merge(tablica,p,q,r)

tablica=[]
n=5


for x in range(n):
    tablica.append(int(input()))

divide(tablica,0,n-1)







print(tablica)