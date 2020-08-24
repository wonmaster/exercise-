text = "X-DSPAM-Confidence:    0.8475"
spacnum=text.find (':')
print (spacnum)
lastnum = text.find ('5')
print (lastnum)
numnotlast = text [19:29]
print (numnotlast)
num= numnotlast.lstrip()
numlast= float (num)
print (numlast)