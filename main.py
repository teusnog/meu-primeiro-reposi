
print("Raízes do Nordeste")
print("Sistema de gerenciamento de pedidos")
print("Projeto Back-end em Python")





nome_sistema= "Raizes do nordeste"

def mostrar_cardapio():
    print("Cardápio da Raízes do Nordeste")
        
    print("Cuscuz - R$ 15,00")
    print("Tapioca - R$ 12,00")
    print("Suco - R$ 8,00")

    

mostrar_cardapio()

nome_cliente = input("Qual é o nome do cliente? ")
print(f"Cliente: {nome_cliente}")



cardapio = ["cuscuz", "tapioca", "suco"]

produto = input("Qual produto você deseja? ").strip().lower()


if produto in cardapio:
    print("Produto disponível!")
else:
    print("Produto indisponível!")
    exit()

# Preço dos produtos
if produto == "cuscuz":
    preco = 15
elif produto == "tapioca":
    preco = 12
elif produto == "suco":
    preco = 8


quantidade = int(input("Quantas unidades deseja? "))
total_pedido = preco * quantidade

estoque = 10

if quantidade > 0 and quantidade <= estoque:
    print("----- RESUMO DO PEDIDO -----")
    print(f"Cliente: {nome_cliente}")
    print(f"Produto: {produto}")
    print(f"Quantidade: {quantidade}")
    print(f"Total: R$ {total_pedido:.2f}")

    print("Pedido autorizado!")
    estoque = estoque - quantidade
    print(f"Estoque restante: {estoque}")
else:
    print("Quantidade inválida ou estoque insuficiente!")

