

def get_cs():
    s=str(input("Enter the string: "))
    return s

def cs_to_lot(cs):
   j=[]
   li=cs.split(";")
   for r in li:
     j.append(tuple(r.split("=")))
   return j

def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)
  
main()
