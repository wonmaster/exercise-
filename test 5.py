num= 0
tot = 0.0
while True :
    inp = input ("enter a number: ")
    if inp == "done" :
        break
    try :
        nu = float (inp)
    except :
        print("nikmok dir nimiro")
        continue
    print (nu)
    num = num + 1
    tot = tot + nu 
print ("all done")
print (tot,num, tot/num)