# Lists
lt=[]
fname = input("Enter file name: ")
f= open(fname)
for line in f:
    for i in line.split():
        if i not in lt:
            lt.append(i)

print(sorted(lt))
