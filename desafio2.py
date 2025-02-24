import textwrap

def menu():
    menu = """\n
    #########################################
            Bem vindo ao serviço de 
            autoatendimento do Banco
        
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo usuário
    [nc]\tNova conta
    [lc]\tLista de contas
    [lu]\tLista de usuários
    [q]\tSair

    #########################################
    Favor selecionar a operação que deseja:
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}    Saldo: R$ {saldo:.2f} \n"
        print(f"Depósito realizado com Sucesso!\n R$ {valor:.2f}")
    else:
        print("Falha na operação! Valor informado não é válido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = (valor > saldo)

    excedeu_limite = (valor > limite)

    excedeu_saques = (numero_saques >= limite_saques)

    if excedeu_saldo:
        print("Falha na operação! Saldo insuficiente.")

    elif excedeu_limite:
        print("Falha na operação! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Falha na operação! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}    Saldo: R$ {saldo:.2f}\n"
        numero_saques += 1
        print(f"Saque realizado com sucesso! Saldo:R$ {saldo:.2f}")

    else:
        print("Falha na operação! Valor informado não é válido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n################ EXTRATO ################\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo Atual: R$ {saldo:.2f}")
    print("\n#########################################")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
            print("CPF já cadastrado!")
            return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (Logradouro, no - bairro - cidade/Estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
    
def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f"Conta criada com sucesso!\nAgência: {AGENCIA}  Cc: {numero_conta}\nUsuário: {usuario['nome']}  CPF: {usuario['cpf']}")
        return {"agencia": AGENCIA, "numero_conta": numero_conta, 'usuario': usuario}
    
    print("Usuário não encontrado. Favor verificar o cpf ou cadastrar usuário.")

def listar_contas(contas):
    for conta in contas:
        linha_conta= f"""\
            Agência:\t{conta['agencia']}
            Cc:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha_conta))

def listar_usuarios(usuarios):
    for usuario in usuarios:
        linha_usuario= f"""
            Titular:\t{usuario['nome']}
            CPF:\t\t{usuario['cpf']}
            Endereço:\t{usuario['endereco']}
            Data de Nascimento:\t{'data_nascimento'}
        """
        print("=" * 100)
        print(textwrap.dedent(linha_usuario))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1
    

    while True: # loop infinito
    
        opção = menu()

        if opção == "d":
            valor = float(input("Informe o valor do depósito:"))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opção == "s":
            valor = float(input("Informe o valor do saque:"))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opção == "e":
            exibir_extrato(saldo, extrato= extrato)

        elif opção == "nu":
            criar_usuario(usuarios)

        elif opção == "nc":
            conta = criar_conta(AGENCIA, numero_conta, usuarios)      

            if conta:
                contas.append(conta)
                numero_conta += 1      

        elif opção == "lc":
            listar_contas(contas)

        elif opção == "lu":
            listar_usuarios(usuarios)

        elif opção =="q":
            print("Obrigado por utilizar nossos serviços!")
            break

        else:
            print("Operação inválida.  Por favor selecione novamente a operação desejada.")

main ()