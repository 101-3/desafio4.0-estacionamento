print("="*45)
print("               MENU PRINCIPAL")
print("="*45)
print(""" 
      1- Registrar um novo veículo
      2- Registro Geral de veículos
      3- Veículos de professores 
      4- Veículos de colaboradores
      5- Veículos de alunos
      6- Registrar entrada de um veículo
      7- Registrar saída de um veículo
      8- Mostrar vagas 
      """)
op = 0
vg = vp = vc = 40
veiculos = []
alunoestacionamento = []
professorestacionamento = []
colaboradorestacionamento = []

while True:
  autorizado = False
  dados = {}
  op = int(input("Digite a opção desejada: "))
  if op == 1:
    placa = input("Digite a placa do veículo: ").upper()
    modelo = input("Digite o modelo do veículo: ").upper()
    perfil = input("Digite o perfil do dono do carro (aluno, colaborador, professor): ").upper()
    cor = input("Digite a cor do veículo: ").upper()
    print("Veículo registrado com sucesso!\n")
    
    dados["placa"] = placa
    dados["modelo"] = modelo
    dados["perfil"] = perfil
    dados["cor"] = cor
    veiculos.append(dados)

  if perfil == "PROFESSOR":
    professorestacionamento.append(dados)
  
  if perfil == "COLABORADOR":
    colaboradorestacionamento.append(dados)

  if perfil == "ALUNO":
    alunoestacionamento.append(dados)
      

  if op == 2:
     for i in range(len(veiculos)):
       print(f"Veículo {i+1}:")
       print(f"Placa: {veiculos[i]['placa']}")
       print(f"Modelo: {veiculos[i]['modelo']}")
       print(f"Perfil: {veiculos[i]['perfil']}")
       print(f"Cor: {veiculos[i]['cor']}\n")
       if i == len(veiculos):
            break
  if op == 3:
     for i in range(len(professorestacionamento)):
       print(f"Veículo {i+1}:")
       print(f"Placa: {professorestacionamento[i]['placa']}")
       print(f"Modelo: {professorestacionamento[i]['modelo']}")
       print(f"Perfil: {professorestacionamento[i]['perfil']}")
       print(f"Cor: {professorestacionamento[i]['cor']}\n")
       if i == len(professorestacionamento):
          break
  

  if op == 4:
     for i in range(len(colaboradorestacionamento)):
       print(f"Veículo {i+1}:")
       print(f"Placa: {colaboradorestacionamento[i]['placa']}")
       print(f"Modelo: {colaboradorestacionamento[i]['modelo']}")
       print(f"Perfil: {colaboradorestacionamento[i]['perfil']}")
       print(f"Cor: {colaboradorestacionamento[i]['cor']}\n")
       if i == len(colaboradorestacionamento):
          break
  

  if op == 5:
      for i in range(len(alunoestacionamento)):
        print(f"Veículo {i+1}:")
        print(f"Placa: {alunoestacionamento[i]['placa']}")
        print(f"Modelo: {alunoestacionamento[i]['modelo']}")
        print(f"Perfil: {alunoestacionamento[i]['perfil']}")
        print(f"Cor: {alunoestacionamento[i]['cor']}\n")
        if i == len(alunoestacionamento):
          break
  
  
  if op == 6:
      local = ""
      placa = input("Digite a placa do veículo: ").upper()
      local = input("Digite o local de estacionamento (professor, colaborador, geral): ").upper()
      for veiculo in veiculos:
        cont = 0
        cont += 1
        if local == "PROFESSOR":
            vp -= 1
            local = ""
        if local == "COLABORADOR":
            vc -= 1 
            local = ""
        if local == "GERAL":
            vg -= 1
            local = ""
        if veiculo['placa'] == placa:
          autorizado = True
          print("Entrada registrada com sucesso!\n")
          vg += 1
          break
        else: 
         print('', end="")
        if cont == len(veiculos) and autorizado == False:
          print("Veículo não registrado. Por favor, registre o veículo antes de registrar a entrada")
          break

        elif op == 7: 
          local = input("Digite o tipo de estacionamento (professor, colaborador, geral): ").upper()
          if local == "PROFESSOR":
                vp += 1
                print("Saída registrada com sucesso!\n")
                local = ""
          if local == "COLABORADOR":
                vc += 1 
                print("Saída registrada com sucesso!\n")
                local = ""
          if local == "GERAL":
                vg += 1
                print("Saída registrada com sucesso!\n")
                local = ""

    


      