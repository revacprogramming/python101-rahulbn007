# Lists
list=[]
fname = input("Enter file name: ")
f= open(fname)
for line in f:
    for i in line.split():
        if i not in list:
            list.append(i)

print(sorted(list))
