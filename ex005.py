n=int(input("DIGITE UM NÚMERO INTEIRO: "))
cont=1
par=0
imp=0
while cont<9:
    n=int(input("DIGITE UM NÚMERO INTEIRO: "))
    cont+=1
    if n%2==0:
        par=par+1
    else:
        imp=imp+1
print(f"PARES {par} E ÍMPARES {imp}")            