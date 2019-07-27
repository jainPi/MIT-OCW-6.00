# run arePossibleMcnuggets with parameters 50,51,52,53,54,55.This will give answer to 1st question .
# given answer to this , it is easy to prove that 56-65 Mcnuggets could also be bought in exact quantity 
# as you can clearly see that 56 is 6 more than 50 . And 50 is already a solution . So it just needs a 6 Mcnugget pack similarly 57 = 51(Solution already known) + 6 
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
  