import os 

os.system("cls")
Fruteira=str(input(" Voce quer comprar Morango ou Maça")).strip()



if Fruteira == "Morango":
    
    Quantidades_KG_Morango=int(input("Digite a Quantidade de Kg Morango:"))
    
    if Quantidades_KG_Morango <=5 :
    
        valor_total_Morango_pagar = Quantidades_KG_Morango * 2.50
    
        print(" O valor total para pagar é de ",valor_total_Morango_pagar)
    
    if Quantidades_KG_Morango > 5:
    
        valor_total_Morango_pagar = Quantidades_KG_Morango * 2.20
    
    if Quantidades_KG_Morango >10 or valor_total_Morango_pagar > 15: 
            
        Valor_com_desconto =valor_total_Morango_pagar - (valor_total_Morango_pagar * 0.1)
        
        print(" O Valor Total a ser pago  com desconto é de ",Valor_com_desconto)
        
    else:
        print(" O Valor total é de ",valor_total_Morango_pagar)
        
elif Fruteira== "Maça":
    
    Quantidades_KG_maça=int(input(" Digite a Quantidade de Kg Maça:"))
        
    if Quantidades_KG_maça <= 5:
        
        Valor_total_maça_pagar= Quantidades_KG_maça * 1.80
    
        print(" O Valor Total para pagar é de ",Valor_total_maça_pagar)
    
    if Quantidades_KG_maça > 5 :
    
        Valor_total_maça_pagar = Quantidades_KG_maça *1.50
    
    if Quantidades_KG_maça > 10 or Valor_total_maça_pagar >15 :
        
        Valor_com_desconto=Valor_total_maça_pagar - (Valor_total_maça_pagar * 0.1)
        
        print(" O valor total a ser pago com desconto é de ",Valor_com_desconto)
        
    else :
        print(" O Valor total é de ",Valor_total_maça_pagar)
    