text = "X-DSPAM-Confidence:    0.8475"
spacnum=text.find (':')
lastnum = text.find ('5')
numnotlast = text [19:29]
num= numnotlast.lstrip()
numlast= float (num)
print (numlast)