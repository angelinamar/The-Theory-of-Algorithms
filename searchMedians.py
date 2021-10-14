x=[]
f=open('1.txt','r')
for line in f.readlines():
    x.append(line)
for i in range(len(x)):
    x[i]=int(x[i])
del x[0]
def maxheapify(a,i):
    l=i*2+1
    r=i*2+2
    if l<=len(a)-1 and a[l]>a[i]:
        largest=l
    else:
        largest=i
    if r<=len(a)-1 and a[r]>a[largest]:
        largest=r
    if largest!=i:
        a[i],a[largest]=a[largest],a[i]
        maxheapify(a,largest)
def minheapify(a,i):
    l=i*2+1
    r=i*2+2
    if l<=len(a)-1 and a[l]<a[i]:
        largest=l
    else:
        largest=i
    if r<=len(a)-1 and a[r]<a[largest]:
        largest=r
    if largest!=i:
        a[i],a[largest]=a[largest],a[i]
        minheapify(a,largest)
def heaps(a):
    hight=[]
    low=[]
    low.append(a[0])
    for i in range(1,len(a)):
        if low[0]<a[i]:
            hight.append(a[i])
            maxsort(hight, len(hight)-1)
        else:
            low.append(a[i])
            minsort(low, len(low)-1)
        if len(low)-len(hight)>1:
            hight.append(low[0])
            low[0]=low[len(low)-1]
            del low[len(low)-1]
            maxsort(hight, len(hight)-1)
            maxheapify(low, 0)
        if len(hight)-len(low)>1:
            low.append(hight[0])
            hight[0]=hight[len(hight)-1]
            del hight[len(hight)-1]
            minsort(low, len(low)-1)
            minheapify(hight,0)
        if i==9876-1:
	  #if i==2015-1:
            if len(low)==len(hight):
                print low[0],hight[0]
            else:
                if len(low)>len(hight):
                    print low[0]
                else:
                    print hight[0]
            print hight[0:5]
            print low[0:5]
def maxsort(a,i):
    p=int((i-1)/2)
    pp=int((p-1)/2)
    if a[p]>a[i]:
        a[p],a[i]=a[i],a[p]
    if pp!=-1:
        maxsort(a,p)
def minsort(a,i):
    p=int((i-1)/2)
    pp=int((p-1)/2)
    if a[p]<a[i]:
        a[p],a[i]=a[i],a[p]
    if pp!=-1:
        minsort(a,p)
heaps(x)        
