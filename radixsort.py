import re
x=[]
f=open('3.txt','r')
for line in f.readlines():
    x.append(line)
v=0
bukva=0
mass="".join(x)
for i in range(ord('a'), ord('z')+1):
    v1=mass.count(chr(i))
    if v<v1:
        v=v1
        bukva=i
for i in range(len(x)):
    x[i] = re.sub('\n', '', x[i])
def radixsort(a,d):
    for i in range(d):
        a=counting(a,d-i-1)
        print a[0]
    return a
def counting(c, h):
    w=[0]*26
    n=[0]*len(c)
    for i in range(len(c)):
        w[ord(c[i][h]) - ord('a')]+=1
    for i in range(1, len(w)):
        w[i]+=w[i-1]
    for i in range (len(c)):
        j=len(c)-i-1
        n[w[ord(c[j][h]) - ord('a')]-1]=c[j]
        w[ord(c[j][h]) - ord('a')]-=1
    return n
answer = radixsort(x, 3)
print radixsort(x,3)
print answer[0]+chr(bukva)+answer[len(x)-1]
