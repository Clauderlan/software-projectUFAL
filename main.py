escolha = 0
voos = [
    {
        "Codigo": "LA3156",
        "Origem": "SP/Congonhas",
        "Partida": "12:23",
        "Destino": "AL/Maceió",
        "Chegada": "14:40",
        "Status": "DECOLOU",
        "Assentos": ["A1", "A2", "B1", "B2"],
        "Bagagem": "2x 23kg",
        "Pontos_Fidelidade": 1000,
        "Solicitacoes_Especiais": []
    },
    {
        "Codigo": "SE3123",
        "Origem": "SP/Congonhas",
        "Partida": "12:43",
        "Destino": "AC/Rio Branco",
        "Chegada": "15:20",
        "Status": "Partindo",
        "Assentos": ["A3", "A4", "B3", "B4"],
        "Bagagem": "1x 23kg",
        "Pontos_Fidelidade": 500,
        "Solicitacoes_Especiais": []
    }
]

reservas = {}

while escolha != 10:
    print("\nMenu")
    print("1 - Flight Status Updates")
    print("2 - Flight Search")
    print("3 - Book a Flight")
    print("4 - Cancel a Booking")
    print("5 - Online Check-in")
    print("6 - Seat Selection")
    print("7 - Baggage Information")
    print("8 - Loyalty Program Management")
    print("9 - Special Requests")
    print("10 - Exit")
    
    escolha = int(input("Digite sua escolha: "))

    if escolha == 1:
        for x in voos:
            print(x)

    elif escolha == 2:
        codVoo = input("Digite o código do voo: ")
        encontrado = False
        for x in voos:
            if codVoo == x["Codigo"]:
                print(x)
                encontrado = True
        if not encontrado:
            print("Voo não encontrado.")

    elif escolha == 3:
        codVoo = input("Digite o código do voo para reserva: ")
        nome = input("Digite seu nome: ")
        if codVoo in reservas:
            print("Voo já reservado.")
        else:
            reservas[codVoo] = nome
            print("Reserva efetuada com sucesso!")

    elif escolha == 4:
        codVoo = input("Digite o código do voo para cancelar reserva: ")
        if codVoo in reservas:
            del reservas[codVoo]
            print("Reserva cancelada com sucesso!")
        else:
            print("Reserva não encontrada.")

    elif escolha == 5:
        codVoo = input("Digite o código do voo para check-in: ")
        if codVoo in reservas:
            print("Check-in realizado com sucesso!")
        else:
            print("Nenhuma reserva encontrada para este voo.")

    elif escolha == 6:
        codVoo = input("Digite o código do voo para selecionar assento: ")
        for x in voos:
            if codVoo == x["Codigo"]:
                print(f"Assentos disponíveis: {x['Assentos']}")
                assento = input("Escolha seu assento: ")
                if assento in x['Assentos']:
                    x['Assentos'].remove(assento)
                    print("Assento selecionado com sucesso!")
                else:
                    print("Assento inválido.")

    elif escolha == 7:
        codVoo = input("Digite o código do voo para ver informações de bagagem: ")
        for x in voos:
            if codVoo == x["Codigo"]:
                print(f"Bagagem permitida: {x['Bagagem']}")

    elif escolha == 8:
        codVoo = input("Digite o código do voo para verificar pontos de fidelidade: ")
        for x in voos:
            if codVoo == x["Codigo"]:
                print(f"Pontos de fidelidade disponíveis: {x['Pontos_Fidelidade']}")

    elif escolha == 9:
        codVoo = input("Digite o código do voo para solicitar um pedido especial: ")
        pedido = input("Digite seu pedido especial (ex: refeição vegetariana): ")
        for x in voos:
            if codVoo == x["Codigo"]:
                x["Solicitacoes_Especiais"].append(pedido)
                print("Pedido especial adicionado com sucesso!")

    elif escolha == 10:
        print("Saindo do sistema...")
