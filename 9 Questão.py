import os 
os.system("cls")

Renda_mensal_do_solicitante=float(input(" Digite a Renda mensal do solicitante "))

Valor_total_do_empréstimo=float(input(" Digite o Valor total do empréstimo"))

Número_de_prestações=int(input(" Digite o Número de prestações"))

valor_máximo_de_empréstimo_permitido= Renda_mensal_do_solicitante * 10 

valor_da_parcela= Valor_total_do_empréstimo * Número_de_prestações

Renda_mensal= Renda_mensal_do_solicitante * 0.30

if valor_da_parcela > Renda_mensal :
    print(" o valor não pode ser emprestado ")
    
else:
    print(" Ainda está dentro da regra ")