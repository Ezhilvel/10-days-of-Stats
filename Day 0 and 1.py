# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 15:32:50 2018

@author: ezhilvel
"""

# mean, median, mode
N = int(input())
stdin = list(map(int, input().rstrip().split()))


import numpy as np

arr = np.array(stdin)

mean = arr.sum()/N

n_1 = int(N/2-1)
n_2 = int(N/2)

if (N%2 == 0):
    median  = (arr[n_1]+arr[n_2])/2
else:
    median = arr[n_2]
count = 0
prev_count = 0
mode  = arr[0] 
temp_mode = arr[0]
for a in arr:
    if (a == temp_mode):
        count = count + 1
        if(count > prev_count):
            prev_count = count
            mode = a

    else:
        count = 1
        temp_mode = a
        

print(mean)
print(median)
print(mode) 

    
#weighted sum

N = int(input())
vales = list(map(int, input().rstrip().split()))
weights = list(map(int, input().rstrip().split()))

sumprod = 0
weightsum = 0
for  i in range(N):
    sumprod = sumprod + vales[i]*weights[i]
    weightsum = weightsum + weights[i]

mean = sumprod/weightsum
print(mean)



#standard deviation
N = int(input())
arr = list(map(int, input().rstrip().split()))

sum_arr = 0
for a in arr:
    sum_arr = sum_arr +a

mean = sum_arr/N

variance= 0
for a in arr:
    variance = variance + (a-mean)**2

std_dev = (variance/N)**(1/2)

print('{:.1f}'.format(std_dev))



# quartiles

N_1 = int(input())
arr_1 = list(map(int, input().rstrip().split()))

def median(arr):
    arr.sort()
    N = len(arr)
    n_1 = int(N/2-1)
    n_2 = int(N/2)

    if (N%2 == 0):
        median  = (arr[n_1]+arr[n_2])/2
    else:
        median = arr[n_2]
    return(median)

Q2 = median(arr_1)

if (N_1%2 == 0):
    L1 = arr_1[0:int(N_1/2)]
    L2 = arr_1[int(N_1/2):] 
else:
    L1 = arr_1[0:int(N_1/2)] 
    L2 = arr_1[int(N_1/2+1):]    


Q1 = median(L1)
Q3 = median(L2)

print(int(Q1))
print(int(Q2))
print(int(Q3))





# Enter your code here. Read input from STDIN. Print output to STDOUT

N_1 = int(input())
elem = list(map(int, input().rstrip().split()))
freq = list(map(int, input().rstrip().split()))

arr_1 =[]
for i in range(N_1):
    for j in range(freq[i]):
        arr_1.append(elem[i])

N_1 = len(arr_1)

def median(arr):
    arr.sort()
    N = len(arr)
    n_1 = int(N/2-1)
    n_2 = int(N/2)

    if (N%2 == 0):
        median  = (arr[n_1]+arr[n_2])/2
    else:
        median = arr[n_2]
    return(median)

Q2 = median(arr_1)

if (N_1%2 == 0):
    L1 = arr_1[0:int(N_1/2)]
    L2 = arr_1[int(N_1/2):] 
else:
    L1 = arr_1[0:int(N_1/2)] 
    L2 = arr_1[int(N_1/2+1):]    


Q1 = median(L1)
Q3 = median(L2)

IQR = Q3 -Q1
print(IQR)