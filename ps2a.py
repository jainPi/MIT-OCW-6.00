def arePossibleMcnuggets(n):
    pack1=6
    pack2=9
    pack3=20
    npack1=0
    npack2=0
    npack3=0
    maxPack1=n/pack1
    maxPack2=n/pack2
    maxPack3=n/pack3
    while npack1<=maxPack1:
        npack2=0
        while npack2<=maxPack2:
            npack3=0
            while npack3<=maxPack3:
                if (6*npack1 + 9*npack2 + 20 *npack3)==n:
                    print('Mcnuggets : ', n, ' require pack of 6: ' ,npack1,' pack of 9: ',npack2,' pack of 20 :  ',npack3)
                    return True
                npack3=npack3+1
            npack2=npack2+1
        npack1=npack1+1
    return False
  
consecutiveSols=0
n=1
nonSol=0
while consecutiveSols<6:
    if arePossibleMcnuggets(n):
        consecutiveSols=consecutiveSols+1
    else:
        consecutiveSols = 0
        nonSol=n
    n=n+1
print(nonSol)
