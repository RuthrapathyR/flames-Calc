u1=input("please enter the name1:")
p=input("please enter the name")
p1=list(p)
u=list(u1)
for i in p:
    if i in u:
        u.remove(i)
        p1.remove(i)
q=len(p1)+len(u)
l=['F','L','A','M','E','S']
l1=[]
while True:
    l1.clear()
    if len(l)<q:
        if q%len(l)==0:
            l1=l[:len(l)-1]
        else:
            l1=l[q%len(l):]+l[:(q%len(l))-1]
    elif len(l)>=q:
        l1=l[q:]+l[:q-1]
    l=list(l1)
    if len(l1)==1:
        break
if l1[0] == 'S':
    print("SOULMATE")
elif l1[0] == 'E':
    print("ENEMY")
elif l1[0] == 'M':
    print("MARRIAGE")
elif l1[0] == 'A':
    print("AFFECTION")
elif l1[0] == 'L':
    print("LOVE")
elif l1[0] == 'F':
    print("FRIENDS")
