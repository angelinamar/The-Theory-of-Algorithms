x=raw_input("first=")
y=raw_input("second=")
a=[]
b=[]
c=[]
f=open('input.txt','r')
for line in f.readlines():
    a=line.split(" ")
    if x==a[0]:
        b=a
    if y==a[0]:
        c=a
for i in range(len(b)):
    b[i]=int(b[i])
for i in range(len(c)):
    c[i]=int(c[i])
for index in range(1,len(b)):
    a[b[index]]=c[index]
del a[0]
print b,c,a
def count_inversion(s):   
    cnt = 0
    srtd = sorted(s)
    while s != srtd:
        for index, elem in enumerate(s):
            if elem > s [index+1]:
                s[index], s[index+1] = s[index+1], s[index]
                cnt += 1
                break
    return cnt
print count_inversion(a)
