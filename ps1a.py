x=5
ct=3
primesFound=1
while primesFound < x:
    i = 2
    isPrime=True
    while i*i <= ct :
        if(ct % i == 0):
            isPrime=False
            break
        i=i+1
    if(isPrime):
        primesFound=primesFound+1
    ct=ct+1
print('The '+str(x)+'th Prime number is '+ str(ct-1))
            
        
   
