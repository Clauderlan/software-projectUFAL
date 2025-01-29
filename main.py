escolha = 0
voos = [
    {
        "Codigo" : "LA3156",
        "Origem" : "SP/Congonhas",
        "Partida" : "12:23",
        "Destino" : "AL/Maceió",
        "Chegada" : "14:40",
        "Status" : "DECOLOU"
    },{
        "Codigo" : "SE3123",
        "Origem" : "SP/Congonhas",
        "Partida" : "12:43",
        "Destino" : "AC/Rio Branco",
        "Chegada" : "15:20",
        "Status" : "Partindo"
    }       
]

while(escolha != 3):
    
    print("Menu\n\n1 - Flight Status Updates\n2 - Flight Search:\n3 - Exit")
    print("\n")
    escolha = int(input("Digite sua escolha:"))

    if(escolha == 1):
        for x in voos:
            print(x)                
    elif(escolha == 2):
        print("Digite o código do voo:")
        codVoo = str(input(""))
        var = 1
        for x in voos:
            if(codVoo == x["Codigo"]):
                print(x)
                var = 0
        if(var):
            print("Voo não encontrado.")
        