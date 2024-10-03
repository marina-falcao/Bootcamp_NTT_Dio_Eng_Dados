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
[nu] novo usuário
[nc] nova conta
[q] sair

"""

def cadastrar_usuario():
    usuarios = []
    nome = input("Nome do usuário: ")
    data_nascimento = input("Data de nascimento do usuário: ")
    cpf = input("CPF do usuário: ")
    endereco = input("Endereço do usuário (r./av., no, bairro, cidade, estado): ")

    cpf_numeros = []
    for digito in cpf:
        if digito.isdigit():
            cpf_numeros.append(int(digito))
    
    for usuario in usuarios:
        if usuario.get('cpf') == cpf_numeros:
            print("CPF já cadastrado.")
            return

    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf_numeros,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")
    return usuarios  

def cadastrar_conta(usuarios): 
    contas = []
    numero_conta = 1
    cpf = input("Digite o CPF do usuário: ")
    

    cpf_numeros = []
    for digito in cpf:
        if digito.isdigit():
            cpf_numeros.append(int(digito))

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario['cpf'] == cpf_numeros:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("Usuário não encontrado.")
        return

    conta = {
        'agencia': '0001',
        'numero': numero_conta,
        'usuario': usuario_encontrado
    }
    contas.append(conta)
    numero_conta += 1
    print("Conta cadastrada com sucesso.")

def depositar(valor, /):
    global saldo, extrato

    if valor >= 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito efetuado. Seu novo saldo é de: R$ {saldo:.2f}")
    else:
        print("Valor inválido. Tente novamente.")

def sacar(*, valor):
    global saldo, extrato, numero_saques

    if numero_saques >= limite_saques:
        print("Limite de saques diários atingido.")
        return

    if valor <= 0:
        print("Valor inválido. Tente novamente.")
    elif valor > limite:
        print("Valor excede o limite diário de R$ 500. Tente novamente.")
    elif valor > saldo:
        print("Não há saldo suficiente na conta corrente para efetuar a operação.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        print(f"Saque efetuado. Seu novo saldo é de: R$ {saldo:.2f}")
        numero_saques += 1  

def mostrar_extrato(saldo, /, *, extrato):
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print("\n------- Extrato -------")
        for transacao in extrato:
            print(transacao)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("------------------------")

usuarios = [] 

while True: 

    try:
        opcao = input(menu)
    except ValueError:
        print("Erro de entrada. O programa será encerrado.")
        break

    if opcao == 'q':
        break  

    if opcao == "d":
        try:
            valor_deposito = float(input("Digite o valor do depósito: "))
            depositar(valor_deposito)
        except ValueError:
            print("Valor inválido. Use apenas números.")
    elif opcao == "s":
        try:
            valor_saque = float(input("Digite o valor do saque: "))
            sacar(valor=valor_saque)
        except ValueError:
            print("Valor inválido. Use apenas números.")
    elif opcao == "e":
        mostrar_extrato(saldo, extrato=extrato)
    elif opcao == "nu":
        usuarios = cadastrar_usuario()  
    elif opcao == "nc":
        if usuarios: 
            cadastrar_conta(usuarios)
        else:
            print("Cadastre um usuário primeiro.")
    else:
        print("Opção inválida.")
        print(menu)

print("O Banco Mari agradece sua visita.")