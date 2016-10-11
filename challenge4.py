import string
import io
import numpy as np

file = io.open("textChallenge4.txt",'r')
textIn = file.read()
textIn = textIn.replace('\n','')
text = textIn.encode('utf-8')
listText = list(text)
file.close()

lower = np.zeros(np.shape(listText),dtype='bool')
for ii in range(len(listText)):
    if listText[ii].islower():
        lower[ii]=1

guarded = {}
for ii in range(len(lower)):
    if np.allclose(lower[ii:ii+9],np.array([1,0,0,0,1,0,0,0,1],dtype=bool)):
        guarded.append=listText[ii+4]
        
# lowerDiff = np.diff(lowerInd,n=1)   # difference between

print ''.join(guarded)