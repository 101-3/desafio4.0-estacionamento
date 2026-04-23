from datetime import datetime

estacionamentos = {
    "interno administrativo": {
        "vagas_total": 5,
        "vagas": {},
        "perfis_permitidos": ["coordenador", "diretor"]
    },
    "externo dos servidores": {
        "vagas_total": 8,
        "vagas": {},
        "perfis_permitidos": ["professor", "funcionario"]
    },
    "entrada principal": {
        "vagas_total": 10,
        "vagas": {},
        "perfis_permitidos": ["aluno", "professor", "funcionario", "coordenador", "diretor", "visitante"]
    }
}

veiculos = {}
movimentacoes = []
indice_cor = {}
indice_perfil = {}

for nome_estacionamento in estacionamentos:
    numero_vaga = 1
    while numero_vaga <= estacionamentos[nome_estacionamento]["vagas_total"]:
        estacionamentos[nome_estacionamento]["vagas"][numero_vaga] = None
        numero_vaga += 1

print("\nSISTEMA DE ESTACIONAMENTO DA UNIVERSIDADE")

while True:
    print("\nMENU PRINCIPAL")
    print("1 - Registrar veiculo")
    print("2 - Registrar entrada")
    print("3 - Registrar saida")
    print("4 - Consultas")
    print("5 - Relatorio geral")
    print("6 - Mostrar vagas")
    print("0 - Encerrar")

    opcao = input("Escolha uma opcao: ").strip()

    if opcao == "1":
        placa = input("Placa: ").strip().upper()

        if placa in veiculos:
            print("Esse veiculo ja esta cadastrado.")
        else:
            cor = input("Cor: ").strip().lower()
            tipo = input("Tipo do veiculo: ").strip().lower()
            dono = input("Nome do dono: ").strip()
            perfil = input("Perfil do dono (aluno, professor, funcionario, coordenador, diretor, visitante): ").strip().lower()

            veiculos[placa] = {
                "placa": placa,
                "cor": cor,
                "tipo": tipo,
                "dono": dono,
                "perfil": perfil,
                "estacionamento": None,
                "vaga": None,
                "entrada": None
            }

            if cor not in indice_cor:
                indice_cor[cor] = []
            indice_cor[cor].append(placa)

            if perfil not in indice_perfil:
                indice_perfil[perfil] = []
            indice_perfil[perfil].append(placa)

            print("Veiculo cadastrado com sucesso.")

    elif opcao == "2":
        placa = input("Digite a placa do veiculo: ").strip().upper()

        if placa not in veiculos:
            print("Veiculo nao cadastrado.")
        elif veiculos[placa]["estacionamento"] is not None:
            print("Esse veiculo ja esta estacionado.")
        else:
            print("\nEstacionamentos disponiveis:")
            print("1 - Interno Administrativo")
            print("2 - Externo dos Servidores")
            print("3 - Entrada Principal")
            escolha = input("Escolha o estacionamento: ").strip()

            if escolha == "1":
                nome_estacionamento = "interno administrativo"
            elif escolha == "2":
                nome_estacionamento = "externo dos servidores"
            elif escolha == "3":
                nome_estacionamento = "entrada principal"
            else:
                nome_estacionamento = ""

            if nome_estacionamento == "":
                print("Opcao invalida.")
            else:
                perfil = veiculos[placa]["perfil"]

                if perfil not in estacionamentos[nome_estacionamento]["perfis_permitidos"]:
                    print("Entrada negada. Esse perfil nao pode usar esse estacionamento.")
                else:
                    vaga_encontrada = None
                    numero_vaga = 1

                    while numero_vaga <= estacionamentos[nome_estacionamento]["vagas_total"]:
                        if estacionamentos[nome_estacionamento]["vagas"][numero_vaga] is None:
                            vaga_encontrada = numero_vaga
                            break
                        numero_vaga += 1

                    if vaga_encontrada is None:
                        print("Nao ha vagas disponiveis nesse estacionamento.")
                    else:
                        horario_entrada = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                        estacionamentos[nome_estacionamento]["vagas"][vaga_encontrada] = placa
                        veiculos[placa]["estacionamento"] = nome_estacionamento
                        veiculos[placa]["vaga"] = vaga_encontrada
                        veiculos[placa]["entrada"] = horario_entrada

                        movimentacoes.append({
                            "placa": placa,
                            "tipo": "entrada",
                            "estacionamento": nome_estacionamento,
                            "vaga": vaga_encontrada,
                            "horario": horario_entrada
                        })

                        print("Entrada registrada com sucesso.")
                        print("Estacionamento:", nome_estacionamento.title())
                        print("Vaga:", vaga_encontrada)
                        print("Horario:", horario_entrada)

    elif opcao == "3":
        placa = input("Digite a placa do veiculo: ").strip().upper()

        if placa not in veiculos:
            print("Veiculo nao cadastrado.")
        elif veiculos[placa]["estacionamento"] is None:
            print("Esse veiculo nao esta estacionado.")
        else:
            nome_estacionamento = veiculos[placa]["estacionamento"]
            vaga = veiculos[placa]["vaga"]
            horario_saida = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            estacionamentos[nome_estacionamento]["vagas"][vaga] = None

            movimentacoes.append({
                "placa": placa,
                "tipo": "saida",
                "estacionamento": nome_estacionamento,
                "vaga": vaga,
                "horario": horario_saida
            })

            veiculos[placa]["estacionamento"] = None
            veiculos[placa]["vaga"] = None
            veiculos[placa]["entrada"] = None

            print("Saida registrada com sucesso.")
            print("Horario:", horario_saida)

    elif opcao == "4":
        while True:
            print("\nCONSULTAS")
            print("1 - Onde esta um carro pela placa")
            print("2 - Quantos carros existem por cor")
            print("3 - Quantos veiculos estacionados existem por perfil")
            print("4 - Verificar se ha aluno em area proibida")
            print("5 - Ver qual estacionamento esta mais cheio")
            print("6 - Listar veiculos estacionados")
            print("7 - Mostrar historico de movimentacoes")
            print("0 - Voltar")

            consulta = input("Escolha uma consulta: ").strip()

            if consulta == "1":
                placa = input("Digite a placa: ").strip().upper()

                if placa not in veiculos:
                    print("Veiculo nao encontrado.")
                elif veiculos[placa]["estacionamento"] is None:
                    print("O veiculo esta cadastrado, mas nao esta estacionado.")
                else:
                    print("Placa:", placa)
                    print("Dono:", veiculos[placa]["dono"])
                    print("Perfil:", veiculos[placa]["perfil"])
                    print("Estacionamento:", veiculos[placa]["estacionamento"].title())
                    print("Vaga:", veiculos[placa]["vaga"])
                    print("Entrada:", veiculos[placa]["entrada"])

            elif consulta == "2":
                cor = input("Digite a cor: ").strip().lower()
                total_cor = 0

                if cor in indice_cor:
                    total_cor = len(indice_cor[cor])

                print("Quantidade de veiculos cadastrados com essa cor:", total_cor)

            elif consulta == "3":
                perfil = input("Digite o perfil: ").strip().lower()
                total_perfil_estacionado = 0

                for placa in veiculos:
                    if veiculos[placa]["perfil"] == perfil and veiculos[placa]["estacionamento"] is not None:
                        total_perfil_estacionado += 1

                print("Quantidade de veiculos estacionados desse perfil:", total_perfil_estacionado)

            elif consulta == "4":
                encontrou_irregularidade = False

                for placa in veiculos:
                    if veiculos[placa]["estacionamento"] is not None:
                        perfil = veiculos[placa]["perfil"]
                        nome_estacionamento = veiculos[placa]["estacionamento"]

                        if perfil not in estacionamentos[nome_estacionamento]["perfis_permitidos"]:
                            encontrou_irregularidade = True
                            print("Irregularidade encontrada:")
                            print("Placa:", placa)
                            print("Perfil:", perfil)
                            print("Estacionamento:", nome_estacionamento.title())

                if encontrou_irregularidade is False:
                    print("Nao ha alunos ou outros perfis em area proibida.")

            elif consulta == "5":
                nome_mais_cheio = ""
                percentual_mais_cheio = -1

                for nome_estacionamento in estacionamentos:
                    ocupadas = 0
                    total = estacionamentos[nome_estacionamento]["vagas_total"]

                    for vaga in estacionamentos[nome_estacionamento]["vagas"]:
                        if estacionamentos[nome_estacionamento]["vagas"][vaga] is not None:
                            ocupadas += 1

                    percentual = ocupadas / total

                    if percentual > percentual_mais_cheio:
                        percentual_mais_cheio = percentual
                        nome_mais_cheio = nome_estacionamento

                if nome_mais_cheio != "":
                    print("Estacionamento mais cheio:", nome_mais_cheio.title())
                    print("Taxa de ocupacao:", round(percentual_mais_cheio * 100, 2), "%")

            elif consulta == "6":
                existe_estacionado = False

                for placa in veiculos:
                    if veiculos[placa]["estacionamento"] is not None:
                        existe_estacionado = True
                        print("\nPlaca:", placa)
                        print("Cor:", veiculos[placa]["cor"])
                        print("Tipo:", veiculos[placa]["tipo"])
                        print("Dono:", veiculos[placa]["dono"])
                        print("Perfil:", veiculos[placa]["perfil"])
                        print("Estacionamento:", veiculos[placa]["estacionamento"].title())
                        print("Vaga:", veiculos[placa]["vaga"])
                        print("Entrada:", veiculos[placa]["entrada"])

                if existe_estacionado is False:
                    print("Nao ha veiculos estacionados no momento.")

            elif consulta == "7":
                if len(movimentacoes) == 0:
                    print("Ainda nao existem movimentacoes registradas.")
                else:
                    for item in movimentacoes:
                        print("\nTipo:", item["tipo"])
                        print("Placa:", item["placa"])
                        print("Estacionamento:", item["estacionamento"].title())
                        print("Vaga:", item["vaga"])
                        print("Horario:", item["horario"])

            elif consulta == "0":
                break

            else:
                print("Opcao invalida.")

    elif opcao == "5":
        total_cadastrados = len(veiculos)
        total_estacionados = 0

        print("\nRELATORIO GERAL")
        print("Total de veiculos cadastrados:", total_cadastrados)

        for placa in veiculos:
            if veiculos[placa]["estacionamento"] is not None:
                total_estacionados += 1

        print("Total de veiculos estacionados agora:", total_estacionados)

        for nome_estacionamento in estacionamentos:
            ocupadas = 0
            total = estacionamentos[nome_estacionamento]["vagas_total"]

            for vaga in estacionamentos[nome_estacionamento]["vagas"]:
                if estacionamentos[nome_estacionamento]["vagas"][vaga] is not None:
                    ocupadas += 1

            livres = total - ocupadas

            print("\nEstacionamento:", nome_estacionamento.title())
            print("Vagas totais:", total)
            print("Vagas ocupadas:", ocupadas)
            print("Vagas livres:", livres)

    elif opcao == "6":
        for nome_estacionamento in estacionamentos:
            print("\n", nome_estacionamento.title())
            print("Vagas:")

            for vaga in estacionamentos[nome_estacionamento]["vagas"]:
                if estacionamentos[nome_estacionamento]["vagas"][vaga] is None:
                    print("Vaga", vaga, "- livre")
                else:
                    print("Vaga", vaga, "- ocupada por", estacionamentos[nome_estacionamento]["vagas"][vaga])

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opcao invalida.")