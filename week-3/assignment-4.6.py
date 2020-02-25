hrs=input('Enter hours:')
rte=input('Enter rate:')
h=float(hrs)
r=float(rte)
def computepay(hrs,rte):
    if h<=40:
        p=h*r
    elif h>40:
        p=(40*r+(h-40)*r*1.5)
        return p
p=computepay(hrs,rte)
print('Pay',p)
