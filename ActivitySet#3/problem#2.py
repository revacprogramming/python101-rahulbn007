from fractions import Fraction as f
n = int(input('enter the number of fractions:'))
fr=[]
for i in range(n):
  fr.append(int(input()))

a=0
for i in fr:  
   a+=f(f'1/{i}')

for i in fr:
  print(f"1/{i} + ", end="")
  
print(f"1/{i}",'=',a )