def computepay(h,r):
    if h>40 :
        wtp = h*r
        wtb = (h-40)*(r*0.5)
        pay = wtp+wtb
    else :
        pay = h*r
    return pay

hrs = input("Enter Hours:")
rent=input("enter rent:")
try :
    h = float(hrs)
    r = float(rent)
except :
    print("Error,pleas enter a numeric input")
    quit()
p = computepay(h,r)
print("Pay",p)

