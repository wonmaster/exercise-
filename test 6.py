largest = None
smallest = None
while True :
    inp = input ("enter a number: ")
    if inp == "done" :
        break
    try :
        inp = int (inp)
    except :
        print("Invalid input")
        continue
    for largnum in [inp] :
        if largnum > largest:
            largest = largnum
    for smallnum in [inp] :
        if smallest is None:
            smallest = smallnum
        elif smallnum < smallest:
            smallest=smallnum

print("Maximum is",largest)
print ("Minimum is",smallest)
