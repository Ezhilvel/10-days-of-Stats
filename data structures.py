# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#counting valley

s = 'DDUUDDUDUUUD'

k = 0
valley = 0
for i in range(len(s)):
    if (s[i] == 'U'):
        k = k + 1
        g = 1
    if (s[i] == 'D'):
        k = k -1 
        g = 0 
    print(k,g)
    if ( (k == 0) & (g == 1)): 
        valley = valley + 1           
valley            



s= 'au'

longest_char = []
for i in range(len(s)-1):
    current_char = list(s[i])
    print(i)
    print(current_char)
    for j in range(i+1,len(s)):
        if (s[j] in current_char):
            if (len(current_char) > len(longest_char)):
                longest_char = current_char
            break            
        if (s[j] not in current_char):
            current_char.append(s[j])
            print(j,current_char)
        if (j == len(s)-1):
            if (len(current_char) > len(longest_char)):
                longest_char = current_char
            break
                        

longest_char

arr_count = int(input())
arr = list(map(int, input().rstrip().split()))



reverse = a*1
n =len(a)
for i in range(len(a)):
    print(a)
    reverse[n-i-1] = a[i]
    print(i)
    print(a)
    print(reverse)

print(reverse)