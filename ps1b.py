from math import *
x=100000
ct=3.0
sumOfLogs = log(2)
while ct <= x:
    i = 2
    isPrime=True
    while i*i <= ct :
        if(ct % i == 0):
            isPrime=False
            break
        i=i+1
    if(isPrime):
        sumOfLogs+=log(ct)
    ct=ct+1
print(sumOfLogs/ct)
            
        
   
