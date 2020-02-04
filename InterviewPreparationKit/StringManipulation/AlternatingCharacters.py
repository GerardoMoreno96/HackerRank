#!/usr/bin/python
string = "AAABBB"
firstChar = string[0]
secondChar = None
count=0
for i in range(1,len(string)):
    secondChar=string[i]
    if(firstChar == secondChar):
        firstChar == secondChar
        count+=1
    else:
        firstChar=secondChar
print(count)