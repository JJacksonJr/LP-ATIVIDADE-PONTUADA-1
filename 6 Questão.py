import os 

os.system("cls")

Nota_1=int(input(" Digite a sua primeira Nota"))

Nota_2=int(input(" Digite sua Segunda Nota"))

média=(Nota_1+Nota_2)/2

print(" média:",média)

if média >= 6.0 :

    print(" Parábens, Aprovado ")
    
if média >=4.0 and média < 6.0:
    
    print(" Está de Recuperação")

elif média < 4.0:
    print(" Está Reprovado")

    