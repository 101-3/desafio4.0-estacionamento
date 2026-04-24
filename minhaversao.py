print("="*45)
print("               MENU PRINCIPAL")
print("="*45)
print(""" 
      1- Registrar um novo veículo
      2- Listar os veículos registrados
      3- Registrar entrada de um veículo
      5- Consultas
      6- Mostrar vagas 
      """)
op = 0
veiculos = []
estacinamento = []
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


