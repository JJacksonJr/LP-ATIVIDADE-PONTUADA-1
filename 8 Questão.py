import os  

os.system("cls")

CD_cor=str(input(" Digite As cores do CD Verde, Azul,Amarelo,Vermelho")).strip()

match CD_cor :
    
    case "Verde":
        
        print(" O valor do CD verde  é de  10,00$$ ")
        
    case "Azul":
        
        print(" O Valor do CD Azul é de 20,00$$ ")
        
    case "Amarelo":
        
        print(" O valor do CD Amarelo é de 30,00$$ ")
        
    case "Vermelho":
        
        print(" O valor Do CD vermelho é de 40,00$$ ")
        
    case _:
        print(" Digite as cores Novamente")
        
    