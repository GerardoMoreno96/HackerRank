#!/usr/bin/python
s = "abcdefghhgfedecba"
words_dictionary = {}
for char in s:
    if not char in words_dictionary:
        words_dictionary[char] = 1
    else:
        words_dictionary[char]+=1
#first case: all the values are the same or there is only one value
globalCount=s[0]
globalCount = words_dictionary[globalCount]
flag = True
false_count = 0
for char in set(s):
    if (globalCount != words_dictionary[char]):
        flag = False
        false_count +=1
if(flag):
    print("YES")
#second case: removing 1 element will return YES
elif false_count == 1:
    print("YES")
#third case: Too many irregularities
else:
    print("NO")
