
def input_two_numbers():
   a,b=[int(x) for x in input("Enter two numbers: ").split()]
   return a,b

def add(a, b):
    return a+b

def output(a, b, sum):
    print("The sum of",a ,"and",b, "is",sum)

def main():
    a,b =input_two_numbers()
    sum = add(a, b)
    output(a, b, sum)
  
main()