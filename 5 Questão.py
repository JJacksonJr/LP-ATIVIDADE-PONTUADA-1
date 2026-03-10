import os  

os.system("cls")

operações=str(input(" Escolha uma operação ")).strip()
A=int(input(" Digite o valor de A "))

B=int(input(" Digite o valor de B"))

match operações :
    case "+":
        Resultado=A+B
        
        print(" Resultado:",Resultado)
        
    case "-":
        Resultado=A-B
        
        print("Resultado:",Resultado)
        
    case "*":
        Resultado=A*B
        
        print(" Resultado:",Resultado)
        
    case "/":
        Resultado=A/B
        
        print(" Resultado:",Resultado)
        
    case _:
        print(" Digite Denovo")