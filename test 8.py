fname = input("Enter file name: ")
fh = open(fname)
for line in fh :
    ly = line.strip()
    lx = ly.upper()
    print (lx)