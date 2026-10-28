# Daniela Silva Rocha

# Inicializando variáveis
opcao = -1 
total_descontos = 0.0
valor_bruto = 0.0
valor_total = 0.0
lista_compras = []

# Looping para realizar as compras
while (opcao != 0):
    print("\n---------PONTO DE VENDA (PDV)------------\n")
    print("1 - Realizar uma compra\n")
    print("0- Finalizar compras\n")
    opcao = (input("Selecione a opcao: "))
    while not opcao.isdigit():
        print("\nDigite apenas números!")
        opcao = input("\nSelecione a opcao: ")
    opcao = int(opcao)
    match opcao:
        case 1:
            desconto_compra = 0
            print("\n====== Realize a compra =======")
            valor_compra = float(input("Digite o valor: "))
            while valor_compra <= 0:
                print("O valor do produto não pode ser menor ou igual a 0, tente novamente !!")
                valor_compra = float(input("\nDigite o valor: "))
            idade = int(input("Digite a idade: "))
            while idade <= 0 or idade > 120:
                print("A idade não pode ser menor ou igual a 0, tente novamente !!")
                idade = int(input("\nDigite a idade: "))
            print("\n================================") 
            valor_bruto = valor_bruto + valor_compra
            if(idade >= 65):
                desconto = valor_compra * (20/100)
                valor_compra = valor_compra - desconto
                desconto_compra = desconto_compra + desconto
                print("Desconto de 20% aplicado")
            if(valor_compra>100):
                desconto = valor_compra * (10/100)
                valor_compra = valor_compra - desconto
                desconto_compra = desconto_compra + desconto
                print("Desconto de 10% aplicado")
            total_descontos = total_descontos + desconto_compra
            lista_compras.append(valor_compra)
            print(f"Compra Realizada com sucesso!!\n- Valor R$ {valor_compra:.2f}")
        case 0:
            break
        case _:
            print("Opção invalida, tente novamente!")
            
# Exibição dos resultados das compras realizadas    
print("------ HISTORICO DE COMPRAS ------\n")
if len(lista_compras) != 0:
    for i in range(len(lista_compras)):
        print(f"Valor do item [{i+1}]: R$ {lista_compras[i]:.2f}")
        valor_total = valor_total + lista_compras[i]
    print("\n- Quantidade de compras: ", len(lista_compras)) 
    print(f"- Total bruto R$: {valor_bruto:.2f}")   
    print(f"- Total de descontos: R$ {total_descontos:.2f}")
    print(f"- Valor final da compra R$: {valor_total:.2f}")
    
# Gerando o arquivo txt do histórico de vendas
    arquivo = open("historico.txt", "w")
    arquivo.write("------ HISTORICO DE COMPRAS ------\n")
    for i in range(len(lista_compras)):
        arquivo.write(f"Valor do item [{i+1}]: R$ {lista_compras[i]:.2f}\n")
    arquivo.write(f"\n- Quantidade de compras: {len(lista_compras)}\n")
    arquivo.write(f"- Total bruto: R$ {valor_bruto:.2f}\n")
    arquivo.write(f"- Total de descontos: R$ {total_descontos:.2f}\n")
    arquivo.write(f"- Valor final: R$ {valor_total:.2f}\n")

    arquivo.close()

    print("\nHistórico salvo em historico.txt!")
    
else:
    print("A lista está vazia!")
    