saldo = 0
limite = 500
extrato = []
numero_saques = 0
limite_saques = 3

menu = """
Escolha a opção desejada:

[d] depositar
[s] sacar
[e] extrato
[q] sair

"""


def depositar():
    global saldo, extrato

    deposito = input("Digite o valor do depósito: ")
    valor_deposito = int(deposito)

    if valor_deposito >= 0:
        saldo += valor_deposito
        extrato.append(f"Depósito: R$ {valor_deposito:.2f}")
        print(f"Depósito efetuado. Seu novo saldo é de: R$ {saldo:.2f}")
        #print(saldo)
        #print(extrato)
    else:
        print("Valor inválido. Tente novamente.")

def sacar():
    global saldo, extrato, numero_saques

    if numero_saques >= limite_saques:
        print("Limite de saques diários atingido.")
        return

    saque = input("Digite o valor do saque: ")
    valor_saque = int(saque)

    if valor_saque <= 0:
        print("Valor inválido. Tente novamente.")
    elif valor_saque > limite:
        print("Valor excede o limite diário de R$ 500. Tente novamente.")
    elif valor_saque > saldo:
        print("Não há saldo suficiente na conta corrente para efetuar a operação.")
    else:
        saldo -= valor_saque
        extrato.append(f"Saque: R$ {valor_saque:.2f}")
        print(f"Saque efetuado. Seu novo saldo é de: R$ {saldo:.2f}")
        #print(saldo)
        #print(extrato)
        numero_saques += 1  

def mostrar_extrato():
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print("\n------- Extrato -------")
        for transacao in extrato:
            print(transacao)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("------------------------")

while True: 

    try:
        opcao = input(menu)
    except ValueError:
        print("Erro de entrada. O programa será encerrado.")
        break

    if opcao == 'q':
        break  

    if opcao == "d":
        depositar()
    elif opcao == "s":
        sacar()
    elif opcao == "e":
        mostrar_extrato()
    else:
        print("Opção inválida.")
        print(menu)

print("O Banco Mari agradece sua visita.")