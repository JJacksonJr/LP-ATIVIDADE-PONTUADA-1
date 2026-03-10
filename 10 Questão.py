import os 

os.system("cls")

Quantidade_de_litros=int(input(" Digite A Quantidade de litros "))

tipo_de_combustivel=str(input(" Digite Qual combustivel Àlcool ou Gasolina")).strip()

if tipo_de_combustivel == "Álcool":
    
    if Quantidade_de_litros <=25 :
        
        valor_total_pagar= Quantidade_de_litros * 3.79
        
        valor_total_com_desconto= valor_total_pagar - (valor_total_pagar * 0.02)
        
        print(" O valor Total A pagar é de ",valor_total_com_desconto)
        
    if Quantidade_de_litros > 25 :
        
        valor_total_pagar= Quantidade_de_litros * 3.79
        
        valor_total_com_desconto= valor_total_pagar - (valor_total_pagar * 0.04)
        
        print("  O valor total a pagar é de ",valor_total_com_desconto)
        
if tipo_de_combustivel == "Gasolina":
    if Quantidade_de_litros <=25 :
        
        valor_total_pagar= Quantidade_de_litros * 6.59
        
        valor_total_com_desconto= valor_total_pagar - (valor_total_pagar * 0.03)
        
        print(" O valor total A pagar é de ",valor_total_com_desconto)
        
    if Quantidade_de_litros > 25 :
        
        valor_total_pagar= Quantidade_de_litros * 6.59
        
        valor_total_com_desconto= valor_total_pagar - (valor_total_pagar * 0.05)
        
        print(" O valor total a pagar é de ",valor_total_com_desconto)