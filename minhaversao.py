print("="*45)
print("               MENU PRINCIPAL")
print("="*45)
print(""" 
      1- Registrar um novo veículo
      2- Listar os veículos registrados
      3- Registrar entrada de um veículo
      4- Registrar saída de um veículo
      5- Consultas
      6- Mostrar vagas 
      """)
op = 0
va = 0
vp = 0
vc = 0
veiculos = []
estacinamento = []
alunoestacionamento = {}
professorestacionamento = {}
colaboradorestacionamento = {}
autorizado = False
while True:
  dados = {}
  op = int(input("Digite a opção desejada: "))
  if op == 1:
    placa = input("Digite a placa do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    perfil = input("Digite o perfil do dono do carro (aluno, colaborador, professor): ")
    cor = input("Digite a cor do veículo: ")
    print("Veículo registrado com sucesso!\n")
    
    dados["placa"] = placa
    dados["modelo"] = modelo
    dados["perfil"] = perfil
    dados["cor"] = cor
    veiculos.append(dados)

  elif op == 2:
     for i in range(len(veiculos)):
       print(f"Veículo {i+1}:")
       print(f"Placa: {veiculos[i]['placa']}")
       print(f"Modelo: {veiculos[i]['modelo']}")
       print(f"Perfil: {veiculos[i]['perfil']}")
       print(f"Cor: {veiculos[i]['cor']}\n")
  
  elif op == 3:
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
  


      