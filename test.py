from random import randrange
nonb_odinate = randrange(0,500) 
eseye=1
nomb_itilizate=-1
print("odinate a jenere yon nomb aleyatwa ou men m w ap gen pou w devine ki nomb li ye")
print("Ann ale!!! antre on vale")
while nomb_itilizate!=nonb_odinate and eseye<6:
    nomb_itilizate = int(input("  "))
    eseye=eseye+1
    if nomb_itilizate>nonb_odinate:
        print("nomb lan pi piti antre on lot vale: ")
    elif nomb_itilizate<nonb_odinate:
        print("nomb lan pi gran antre on lot vale: ")
if nomb_itilizate == nonb_odinate:
    print("Bingo ou jwenn li")
else:
    print("ou eseye twop fwa")    
    