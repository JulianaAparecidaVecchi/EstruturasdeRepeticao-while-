total=0
soma=0
num=float(input("DIGITE UM NÚMERO: "))
while True:
    if num!= -1:
        soma=soma+num
        total=total+1
        media=soma/total
        num=float(input("DIGITE UM NÚMERO: "))
    else:
        break
print(f"A MÉDIA É {media:.2f}")    