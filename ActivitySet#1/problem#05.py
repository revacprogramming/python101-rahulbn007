def computepay(h, r):
    p=0.0
    if h<=40 :
        p = h*r

    else :
        hr=h-40
        p=40*r+(hr*r*1.5)
        
    return p

hrs = float(input("Enter Hours:"))
rt = float(input("Enter rate: "))
p = computepay(hrs, rt)
print("Pay ", p)