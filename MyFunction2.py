def computepay(h,r):    
    if h <= 40:
        x = h*r
    elif h>40:
        x = (40*r+(h-40)*1.5*r)
        return x
hrs = input("h: ")
rate = input("r:")
h = float(hrs)
r = float(rate)    
    
p = computepay(h,r)
print("Pay",p)