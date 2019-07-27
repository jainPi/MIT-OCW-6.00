def arePossibleMcnuggets(n,tuple):
    pack1=tuple[0]
    pack2=tuple[1]
    pack3=tuple[2]
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
                if (tuple[0]*npack1  + tuple[1]*npack2 + tuple[2] *npack3)==n:
                    return True
                npack3=npack3+1
            npack2=npack2+1
        npack1=npack1+1
    return False

tuple=[1,2,3]  
n=1
nonSol=0
while n<=200:
    if not(arePossibleMcnuggets(n,tuple)):
        nonSol=n
    n=n+1
print('given packages of size ',tuple[0],' ',tuple[1],' ',tuple[2],' the largest number of nuggets that cannot be bought in exact quantity ', nonSol)
