def atualizar_extrato(valor, extrato, operacao):
    extrato += f"{operacao}: R$ {valor:.2f}\n"
    return extrato

def depositar(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato = atualizar_extrato(valor, extrato, 'Depósito')
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato
    
def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato = atualizar_extrato(valor, extrato, 'Saque')
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, numero_saques, extrato

def visualizar_extrato(saldo, /, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(usuarios):
    print("\nPreencha as informações do usuário\n")

    cpf = input("Informe o CPF (somente os números): ")
    
    for usuario in usuarios:
        if (usuario["cpf"] == cpf):
            print("O CPF informado já está castrado.")
            return usuarios
    
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento no formato: DD/MM/AAAA: ")

    print("\nPreencha as informações do endereço do usuário\n")
    logradouro = input("Informe o logradouro: ")
    numero = input("Informe o número: ")
    bairro = input("Informe o bairro: ")
    cidade = input("Informe a cidade: ")
    sigla_estado = input("Informe a sigla do estado (exemplo: 'PR' para Paraná): ")
    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{sigla_estado}"

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
    }

    print("Usuário castrado com sucesso!")
    usuarios.append(usuario)
    return usuarios

def cadastrar_conta_corrente(usuarios, contas_correntes):
    cpf = input("Informe o CPF do usuário: ")

    usuario_cadastrado = False
    
    i = 0
    print(len(usuarios))
    while i < len(usuarios):
        if (usuarios[i]["cpf"] == cpf):
            usuario_cadastrado = True
        i += 1

    if not usuario_cadastrado:
        print("Usuário não encontrado! Cadastre o usuário primeiro.")
        return contas_correntes

    agencia = "0001"
    numero_conta = len(contas_correntes) + 1

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario_cpf": cpf
    }

    contas_correntes.append(conta)

    print(f"Conta corrente criada com sucesso! Agência: {agencia} Conta: {numero_conta}")
    return contas_correntes

def iniciar():
    menu = """
[u] Cadastrar usuário
[lu] Listar usuários
[c] Cadastrar conta corrente
[lc] Listar contas correntes
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas_correntes = []
    LIMITE_SAQUES = 3

    while True:
        opcao = input(menu)

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, numero_saques, extrato = sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
        elif opcao == "e":
            visualizar_extrato(saldo, extrato=extrato)
        elif opcao == "u":
            usuarios = cadastrar_usuario(usuarios)
        elif opcao == "lu":
            print(usuarios)
        elif opcao == "c":
            contas_correntes = cadastrar_conta_corrente(usuarios, contas_correntes)
        elif opcao == "lc":
            print(contas_correntes)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

iniciar()