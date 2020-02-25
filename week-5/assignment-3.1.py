h=input('Enter the hours:')
r=input('Enter the rate:')
hrs = float(h)
rte = float(r)
if hrs<=40:
    print(hrs*rte)
if hrs>40:
    print(40*rte+(hrs-40)*rte*1.5)

        
