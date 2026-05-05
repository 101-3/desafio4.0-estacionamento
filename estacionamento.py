print("=" * 45)
print("               MENU PRINCIPAL")
print("=" * 45)
print("""
      1- Registrar um novo veículo
      2- Registro Geral de veículos
      3- Veículos de professores
      4- Veículos de colaboradores
      5- Veículos de alunos
      6- Registrar entrada de um veículo
      7- Registrar saída de um veículo
      8- Mostrar vagas
      9- Buscar veículo por placa
      10- Buscar veículos por cor
      11- Mostrar veículos por estacionamento
      12- Verificar veículos em local errado
      13- Mostrar ocupação geral
      14- Histórico de entrada e saída
      15- Sair
      """)

op = 0

vg = 40
vp = 40
vc = 40

historico = []

veiculos = [
    {"placa": "ABC123", "modelo": "ONIX", "perfil": "ALUNO", "cor": "PRATA", "estacionado": "NAO", "local": ""},
    {"placa": "DEF456", "modelo": "HB20", "perfil": "ALUNO", "cor": "BRANCO", "estacionado": "NAO", "local": ""},
    {"placa": "GHI789", "modelo": "ARGO", "perfil": "ALUNO", "cor": "PRETO", "estacionado": "NAO", "local": ""},
    {"placa": "JKL012", "modelo": "GOL", "perfil": "ALUNO", "cor": "VERMELHO", "estacionado": "NAO", "local": ""},
    {"placa": "MNO345", "modelo": "COROLLA", "perfil": "COLABORADOR", "cor": "CINZA", "estacionado": "NAO", "local": ""},
    {"placa": "PQR678", "modelo": "CIVIC", "perfil": "COLABORADOR", "cor": "AZUL", "estacionado": "NAO", "local": ""},
    {"placa": "STU901", "modelo": "CRONOS", "perfil": "COLABORADOR", "cor": "BRANCO", "estacionado": "NAO", "local": ""},
    {"placa": "VWX234", "modelo": "TRACKER", "perfil": "COLABORADOR", "cor": "PRETO", "estacionado": "NAO", "local": ""},
    {"placa": "YZA567", "modelo": "COMPASS", "perfil": "PROFESSOR", "cor": "PRATA", "estacionado": "NAO", "local": ""},
    {"placa": "BCD890", "modelo": "T-CROSS", "perfil": "PROFESSOR", "cor": "CINZA", "estacionado": "NAO", "local": ""},
    {"placa": "EFG135", "modelo": "HR-V", "perfil": "PROFESSOR", "cor": "BRANCO", "estacionado": "NAO", "local": ""},
    {"placa": "HIJ246", "modelo": "CRETA", "perfil": "PROFESSOR", "cor": "AZUL", "estacionado": "NAO", "local": ""},
]

alunoestacionamento = [
    veiculo for veiculo in veiculos if veiculo["perfil"] == "ALUNO"
]
professorestacionamento = [
    veiculo for veiculo in veiculos if veiculo["perfil"] == "PROFESSOR"
]
colaboradorestacionamento = [
    veiculo for veiculo in veiculos if veiculo["perfil"] == "COLABORADOR"
]

while True:
    autorizado = False
    encontrado = False
    dados = {}

    print("=" * 24)
    op = int(input("Digite a opção desejada: "))
    print("=" * 24)

    if op == 1:
        placa = input("Digite a placa do veículo: ").upper()
        modelo = input("Digite o modelo do veículo: ").upper()
        perfil = input("Digite o perfil do dono do carro (aluno, colaborador, professor, coordenador, diretor): ").upper()
        cor = input("Digite a cor do veículo: ").upper()

        repetido = False

        for veiculo in veiculos:
            if veiculo["placa"] == placa:
                repetido = True

        if repetido == True:
            print("Essa placa já foi cadastrada.\n")
        else:
            if perfil == "FUNCIONARIO":
                perfil = "COLABORADOR"

            if perfil == "ALUNO" or perfil == "COLABORADOR" or perfil == "PROFESSOR" or perfil == "COORDENADOR" or perfil == "DIRETOR":
                print("Veículo registrado com sucesso!\n")

                dados["placa"] = placa
                dados["modelo"] = modelo
                dados["perfil"] = perfil
                dados["cor"] = cor
                dados["estacionado"] = "NAO"
                dados["local"] = ""
                veiculos.append(dados)

                if perfil == "PROFESSOR":
                    professorestacionamento.append(dados)

                if perfil == "COLABORADOR":
                    colaboradorestacionamento.append(dados)

                if perfil == "ALUNO":
                    alunoestacionamento.append(dados)
            else:
                print("Perfil inválido.\n")

    if op == 2:
        for i in range(len(veiculos)):
            print(f"Veículo {i + 1}:")
            print(f"Placa: {veiculos[i]['placa']}")
            print(f"Modelo: {veiculos[i]['modelo']}")
            print(f"Perfil: {veiculos[i]['perfil']}")
            print(f"Cor: {veiculos[i]['cor']}")
            print(f"Estacionado: {veiculos[i]['estacionado']}")
            print(f"Local: {veiculos[i]['local']}\n")

    if op == 3:
        for i in range(len(professorestacionamento)):
            print(f"Veículo {i + 1}:")
            print(f"Placa: {professorestacionamento[i]['placa']}")
            print(f"Modelo: {professorestacionamento[i]['modelo']}")
            print(f"Perfil: {professorestacionamento[i]['perfil']}")
            print(f"Cor: {professorestacionamento[i]['cor']}\n")

    if op == 4:
        for i in range(len(colaboradorestacionamento)):
            print(f"Veículo {i + 1}:")
            print(f"Placa: {colaboradorestacionamento[i]['placa']}")
            print(f"Modelo: {colaboradorestacionamento[i]['modelo']}")
            print(f"Perfil: {colaboradorestacionamento[i]['perfil']}")
            print(f"Cor: {colaboradorestacionamento[i]['cor']}\n")

    if op == 5:
        for i in range(len(alunoestacionamento)):
            print(f"Veículo {i + 1}:")
            print(f"Placa: {alunoestacionamento[i]['placa']}")
            print(f"Modelo: {alunoestacionamento[i]['modelo']}")
            print(f"Perfil: {alunoestacionamento[i]['perfil']}")
            print(f"Cor: {alunoestacionamento[i]['cor']}\n")

    if op == 6:
        placa = input("Digite a placa do veículo: ").upper()
        local = input("Digite o local de estacionamento (administrativo, servidores, geral): ").upper()

        if local == "PROFESSOR":
            local = "ADMINISTRATIVO"

        if local == "COLABORADOR":
            local = "SERVIDORES"

        if local == "ADMINISTRATIVO" or local == "SERVIDORES" or local == "GERAL":
            for veiculo in veiculos:
                if veiculo["placa"] == placa:
                    encontrado = True

                    if veiculo["estacionado"] == "SIM":
                        print("Esse veículo já está estacionado.\n")
                    else:
                        if local == "ADMINISTRATIVO":
                            if veiculo["perfil"] == "COORDENADOR" or veiculo["perfil"] == "DIRETOR":
                                autorizado = True
                            else:
                                print("Acesso negado. Esse estacionamento é apenas para coordenadores e diretores.\n")

                            if autorizado == True:
                                if vp > 0:
                                    vp -= 1
                                    veiculo["estacionado"] = "SIM"
                                    veiculo["local"] = local
                                    historico.append({"placa": placa, "acao": "ENTRADA", "local": local})
                                    print("Entrada registrada com sucesso!\n")
                                else:
                                    print("Não existem vagas disponíveis nesse estacionamento.\n")

                        if local == "SERVIDORES":
                            if veiculo["perfil"] == "PROFESSOR" or veiculo["perfil"] == "COLABORADOR":
                                autorizado = True
                            else:
                                print("Acesso negado. Esse estacionamento é apenas para professores e colaboradores.\n")

                            if autorizado == True:
                                if vc > 0:
                                    vc -= 1
                                    veiculo["estacionado"] = "SIM"
                                    veiculo["local"] = local
                                    historico.append({"placa": placa, "acao": "ENTRADA", "local": local})
                                    print("Entrada registrada com sucesso!\n")
                                else:
                                    print("Não existem vagas disponíveis nesse estacionamento.\n")

                        if local == "GERAL":
                            autorizado = True

                            if vg > 0:
                                vg -= 1
                                veiculo["estacionado"] = "SIM"
                                veiculo["local"] = local
                                historico.append({"placa": placa, "acao": "ENTRADA", "local": local})
                                print("Entrada registrada com sucesso!\n")
                            else:
                                print("Não existem vagas disponíveis nesse estacionamento.\n")

            if encontrado == False:
                print("Veículo não registrado. Por favor, registre o veículo antes de registrar a entrada.\n")
        else:
            print("Local de estacionamento inválido.\n")

    if op == 7:
        placa = input("Digite a placa do veículo: ").upper()

        for veiculo in veiculos:
            if veiculo["placa"] == placa:
                encontrado = True

                if veiculo["estacionado"] == "NAO":
                    print("Esse veículo não está estacionado.\n")
                else:
                    local = veiculo["local"]

                    if local == "ADMINISTRATIVO":
                        vp += 1

                    if local == "SERVIDORES":
                        vc += 1

                    if local == "GERAL":
                        vg += 1

                    veiculo["estacionado"] = "NAO"
                    veiculo["local"] = ""
                    historico.append({"placa": placa, "acao": "SAIDA", "local": local})
                    print("Saída registrada com sucesso!\n")

        if encontrado == False:
            print("Veículo não encontrado.\n")

    if op == 8:
        print(f"Vagas no estacionamento administrativo: {vp}")
        print(f"Vagas no estacionamento dos servidores: {vc}")
        print(f"Vagas no estacionamento geral: {vg}\n")

    if op == 9:
        placa = input("Digite a placa do veículo: ").upper()

        for veiculo in veiculos:
            if veiculo["placa"] == placa:
                encontrado = True
                print(f"Placa: {veiculo['placa']}")
                print(f"Modelo: {veiculo['modelo']}")
                print(f"Perfil: {veiculo['perfil']}")
                print(f"Cor: {veiculo['cor']}")
                print(f"Estacionado: {veiculo['estacionado']}")
                print(f"Local: {veiculo['local']}\n")

        if encontrado == False:
            print("Veículo não encontrado.\n")

    if op == 10:
        cor = input("Digite a cor do veículo: ").upper()
        quantidade = 0

        for veiculo in veiculos:
            if veiculo["cor"] == cor and veiculo["estacionado"] == "SIM":
                quantidade += 1
                print(f"Placa: {veiculo['placa']}")
                print(f"Modelo: {veiculo['modelo']}")
                print(f"Perfil: {veiculo['perfil']}")
                print(f"Local: {veiculo['local']}\n")

        print(f"Quantidade de veículos dessa cor estacionados: {quantidade}\n")

    if op == 11:
        local = input("Digite o local de estacionamento (administrativo, servidores, geral): ").upper()

        if local == "PROFESSOR":
            local = "ADMINISTRATIVO"

        if local == "COLABORADOR":
            local = "SERVIDORES"

        quantidade = 0

        for veiculo in veiculos:
            if veiculo["local"] == local and veiculo["estacionado"] == "SIM":
                quantidade += 1
                print(f"Placa: {veiculo['placa']}")
                print(f"Modelo: {veiculo['modelo']}")
                print(f"Perfil: {veiculo['perfil']}")
                print(f"Cor: {veiculo['cor']}\n")

        print(f"Quantidade de veículos nesse estacionamento: {quantidade}\n")

    if op == 12:
        irregular = False

        for veiculo in veiculos:
            if veiculo["estacionado"] == "SIM":
                if veiculo["local"] == "ADMINISTRATIVO":
                    if veiculo["perfil"] != "COORDENADOR" and veiculo["perfil"] != "DIRETOR":
                        irregular = True
                        print(f"Veículo em local errado: {veiculo['placa']}")

                if veiculo["local"] == "SERVIDORES":
                    if veiculo["perfil"] != "PROFESSOR" and veiculo["perfil"] != "COLABORADOR":
                        irregular = True
                        print(f"Veículo em local errado: {veiculo['placa']}")

        if irregular == False:
            print("Não existem veículos em locais errados.\n")
        else:
            print()

    if op == 13:
        print("Ocupação dos estacionamentos:")
        print(f"Administrativo: {40 - vp} ocupadas e {vp} livres")
        print(f"Servidores: {40 - vc} ocupadas e {vc} livres")
        print(f"Geral: {40 - vg} ocupadas e {vg} livres")
        print(f"Total de vagas ocupadas: {(40 - vp) + (40 - vc) + (40 - vg)}")
        print(f"Total de vagas livres: {vp + vc + vg}\n")

    if op == 14:
        if len(historico) == 0:
            print("Ainda não existe histórico.\n")
        else:
            for i in range(len(historico)):
                print(f"Registro {i + 1}:")
                print(f"Placa: {historico[i]['placa']}")
                print(f"Ação: {historico[i]['acao']}")
                print(f"Local: {historico[i]['local']}\n")

    if op == 15:
        print("Sistema encerrado.")
        break

    if op < 1 or op > 15:
        print("Opção inválida.\n")
