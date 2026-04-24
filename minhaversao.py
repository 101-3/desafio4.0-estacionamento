print("="*45)
print("               MENU PRINCIPAL")
print("="*45)
print(""" 
      1- Registrar um novo veículo
      2- Listar os veículos registrados
      3- Listar os veículos de professores 
      4- Listar os veículos de colaboradores
      5- Listar os veículos de alunos
      6- Registrar entrada de um veículo
      7- Registrar saída de um veículo
      8- Consultas      9- Mostrar vagas 
      """)
op = 0
va = 0
vp = 0
vc = 0
veiculos = []
alunoestacionamento = []
professorestacionamento = []
colaboradorestacionamento = []
autorizado = False
while True:
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
      

  elif op == 2:
     for i in range(len(veiculos)):
       print(f"Veículo {i+1}:")
       print(f"Placa: {veiculos[i]['placa']}")
       print(f"Modelo: {veiculos[i]['modelo']}")
       print(f"Perfil: {veiculos[i]['perfil']}")
       print(f"Cor: {veiculos[i]['cor']}\n")
  
  elif op == 3:
     for i in range(len(professorestacionamento)):
       print(f"Veículo {i+1}:")
       print(f"Placa: {professorestacionamento[i]['placa']}")
       print(f"Modelo: {professorestacionamento[i]['modelo']}")
       print(f"Perfil: {professorestacionamento[i]['perfil']}")
       print(f"Cor: {professorestacionamento[i]['cor']}\n")
       if i == len(professorestacionamento):
          break
  

  elif op == 4:
     for i in range(len(colaboradorestacionamento)):
       print(f"Veículo {i+1}:")
       print(f"Placa: {colaboradorestacionamento[i]['placa']}")
       print(f"Modelo: {colaboradorestacionamento[i]['modelo']}")
       print(f"Perfil: {colaboradorestacionamento[i]['perfil']}")
       print(f"Cor: {colaboradorestacionamento[i]['cor']}\n")
       if i == len(colaboradorestacionamento):
          break
  

  elif op == 5:
      for i in range(len(alunoestacionamento)):
        print(f"Veículo {i+1}:")
        print(f"Placa: {alunoestacionamento[i]['placa']}")
        print(f"Modelo: {alunoestacionamento[i]['modelo']}")
        print(f"Perfil: {alunoestacionamento[i]['perfil']}")
        print(f"Cor: {alunoestacionamento[i]['cor']}\n")
        if i == len(alunoestacionamento):
          break
  
  
  elif op == 6:
      placa = input("Digite a placa do veículo: ")
      for veiculo in veiculos:
        cont = 0
        cont += 1
        if veiculo['placa'] == placa:
          autorizado = True
          print("Entrada registrada com sucesso!\n")
          va += 1
          break
        else: 
         print('', end="")
        if cont == len(veiculos) and autorizado == False:
          print("Veículo não registrado. Por favor, registre o veículo antes de registrar a entrada")
          break
    


      