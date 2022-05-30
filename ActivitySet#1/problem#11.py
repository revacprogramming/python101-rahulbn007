# Tuples
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d={}
t=()
for l in handle:
    if l.startswith('From:'): continue
    if not l.startswith('From'): continue
    index=l.find(':')
    s=l[index-2:index]
    if s not in d:
        d[s]=1
    else:
        d[s]+=1

t = tuple(d.items())
result=sorted(t)
for a,b in result:
    print(a,b)
