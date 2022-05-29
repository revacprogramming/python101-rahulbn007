# Tuples
name = input("Enter file:")
if len(name) < 1:
     name = "mbox-short.txt"
h = open(name)
d={}
t=[]
for l in h:
    if l.startswith('From:'): continue
    if not l.startswith('From'): continue
    index=l.find(':')
    s=l[index-2:index]
    if s not in d:
        d[s]=1
    else:
        d[s]+=1

t = list(d.items())
t.sort()
for a,b in t:
    print(a,b)