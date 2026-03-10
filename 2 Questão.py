import os   

os.system("cls")

Nome=str(input(" Digite Seu Nome ")).strip()

Sexo=str(input(" Digite o Seu Gênero ")).strip()

Estado_civil=str(input(" Digite o seu estado civil")).strip()

if Sexo == "F" and Estado_civil == "CASADA":
    
    Tempo_de_casada=str(input(" Digite o tempo de casada")).strip()
    
print(" \nNome:",Nome," \nSexo: ",Sexo, "\nEstado_civil:",Estado_civil," \nTempo de Casada:",Tempo_de_casada," Anos")
    