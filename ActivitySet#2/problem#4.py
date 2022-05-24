

def get_cs():
  s=str(input("Enter the string: "))
  return s

def cs_to_lot(cs):
   j=[]
   li=cs.split(";")
   for r in li:
     j.append(tuple(r.split("=")))
   return j

def lot_to_cs(lot):
    sr=" "
    sr= [''.join(i) for i in lot]
    print(+str(sr))
    #for a,b in lot:
    # str+=
    return sr


def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()
