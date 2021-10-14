x=[]
f=open('1.txt','r')
for line in f.readlines():
    x.append(line)
  
counter = 0
def partition(a, p, r):
    if p<r:
        #a[p],a[r]=a[r],a[p]
        """if (a[p]<a[(p+r)/2] and a[(p+r)/2]<a[r])or (a[p]>a[(p+r)/2] and a[(p+r)/2]>a[r])  :
            a[(p+r)/2],a[r]=a[r],a[(p+r)/2]
        elif (a[p]>a[(p+r)/2] and a[p]<a[r])or (a[p]<a[(p+r)/2] and a[p]>a[r]):
            a[p],a[r]=a[r],a[p]"""     
        global counter
        x=a[r]
        i=p-1
        for j in range(p,r):
            if a[j]<=x:
                i+=1
                a[i],a[j]=a[j],a[i]
        a[i+1],a[r]=a[r],a[i+1]
        partition(a,p,i)
        partition(a,i+2,r)
        counter+=r-p
partition (x, 0, len(x)-1)
print x
print counter
    
