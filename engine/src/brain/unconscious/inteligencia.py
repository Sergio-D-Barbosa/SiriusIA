input1 = 1
input2 = 0
valorEsperado = 1

def neuron(x1, x2):

    def somatorio(peso1, peso2, bias):
        b = bias
        w1 = peso1
        w2 = peso2
        m1 = round((x1*w1)*100)/100
        m2 = round((x2*w2)*100)/100
        soma = round((m1+m2+b)*100)/100
        return [w1, w2, soma, b]

    def activationFunction(soma):
        if soma > 0:
            return 1
        else:
            return 0

    def propagation(peso1x, peso2x, saidax, bias):
        taxaAprendizado = 0.1
        erro = valorEsperado-saidax
        variancaoDoPeso1 = round((erro*taxaAprendizado*x1)*100, 2)/100
        variancaoDoPeso2 = round((erro*taxaAprendizado*x2)*100, 2)/100
        variacaoDoB = round((erro*taxaAprendizado)*100, 2)/100
        novoW1 = round((peso1x+variancaoDoPeso1)*100, 2)/100
        novoW2 = round((peso2x+variancaoDoPeso2)*100, 2)/100
        novoB = round((bias+variacaoDoB)*100, 2)/100

        print(f"erro: {erro}")
        print(f"variação1: {variancaoDoPeso1}")
        print(f"erro: {erro}")
        print(f"variação1: {variancaoDoPeso1}")
        print(f"variação2: {variancaoDoPeso2}")
        print(f"variaçãob: {variacaoDoB}")
        print(f"novow1: {novoW1}")
        print(f"novow2: {novoW2}")
        print(f"novoN: {novoB}")
        
        return [novoW1, novoW2, novoB]

    def execucaoRevisao(w1, w2, b):
        print(f"w1: {w1}\nw2: {w2}\nb: {b}")
        listDados = somatorio(w1, w2, b)
        saida = activationFunction(listDados[2])
        print(f"somatório: {listDados[2]}")
        print(f"saida: {saida}")
        supervisao(listDados[0], listDados[1], saida, listDados[3])

    def execucaoInit():
        print(f"INIT w1: 1\nw2: 1\nb: 1")
        listDados = somatorio(0.7,0.5,-0.8)
        saida = activationFunction(listDados[2])
        print(f"somatório: {listDados[2]}")
        print(f"INIT saida: {saida}")
        supervisao(listDados[0], listDados[1], saida, listDados[3])

    def reaprender(peso1, peso2, saida, bias):
        novosDados = propagation(peso1, peso2, saida, bias)

        execucaoRevisao(novosDados[0], novosDados[1], novosDados[2])

    def supervisao(peso1, peso2, saida, b):
        resposta = input("Deseja treinar o modelo? ")

        if resposta == "s":
            reaprender(peso1, peso2, saida, b)
        else:
            print("Treinamento finalizaddo!")
    
    execucaoInit()

neuron(input1, input2)

