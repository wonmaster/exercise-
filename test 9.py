fname = input("Enter file name: ")
fh = open(fname)
tot= 0
count= 0
for line in fh :
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    num = float(line.split(": ",1)[2])
    tot = tot + num
    count +=1
print ("Average spam confidence: ",tot/count)