score = input("Enter Score: ")
try :
    x=float(score)
except:
    print ("Error,pleas enter a numeric input between 0.0 and 1.0")
    quit()
if x < 0.6 :
    print ("F")
elif x > 1 :
    print ("Error,pleas enter a numeric input between 0.0 and 1.0")
elif x >= 0.6 :
    print ("D")
elif x >=0.7 :
    print ("C")
elif x >= 0.8 :
    print("B")
elif x >= 0.9 :
    print ("A")

