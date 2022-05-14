# Conditional Execution

hrs = input("Enter hours? ")
rt = float(input("Rate :"))
h = float(hrs)
if h<=40:
   print(h*rt)
else :
   hr=h-40
   print((40*rt)+(hr*1.5*rt))