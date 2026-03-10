import os  

os.system("cls")

Nome_do_produto=str(input(" Digite o nome do produto")).strip()

Quantidade_de_produto=int(input(" Digite a quantidade de produtos que voce pegou "))

preço_do_produto=float(input(" Digite o valor do Produto"))

Total_pagar=Quantidade_de_produto * preço_do_produto

print(" total A pagar ",Total_pagar)

if Quantidade_de_produto <= 5 :
    
    Valor_com_Desconto= Total_pagar - (Total_pagar * 0.02)
    
    print(" O valor final com desconto ",Valor_com_Desconto)
    
if Quantidade_de_produto > 5  and Quantidade_de_produto <= 10 :
    
    Valor_com_Desconto= Total_pagar - (Total_pagar * 0.03)
    
    print(" Valor com desconto final é de ",Valor_com_Desconto)
    
elif Quantidade_de_produto > 10 :
    
    Valor_com_Desconto= Total_pagar - (Total_pagar * 0.05)
    
    print(" Valor final com desconto é de: ",Valor_com_Desconto)