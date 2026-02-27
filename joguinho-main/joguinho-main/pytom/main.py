import random as rd

print("----------")
print("Bm vindo ao jogo")
print("----------")

# definicao das variaveis
n_secreto = rd.randrange(1, 100)
print(n_secreto)
n_tentativas = 5
rodada = 1
pontos = 1000

print("Níveis de dificuldade")
print("\n(1) facil (2) médio (3) difícil (4) aleatório\n")

nivel = int(input("escolha a dificuldade: "))

if(nivel == 1):
    n_tentativas = 12
elif(nivel == 2):
    n_tentativas = 5
elif(nivel == 3):
    n_tentativas = 3
else:
    n_tentativas = rd.randrange(1,50)        

for rodada in range (1,n_tentativas + 1):
    print(f"tentativa {rodada} de {n_tentativas}")
    entrada = int(input("Digite um número: "))
    acerto = entrada == n_secreto
    entrada_maior = entrada > n_secreto
    entrada_menor = entrada < n_secreto
    
    if(entrada > 100 or entrada <1):
        print("o valor digitado não é permitido")

    print(f"Você digitou o número: {entrada}")

    if(acerto):
        print("Você conseguiu")
        print(f"parabens (ou nao)! voce fez {pontos} pontos.J")
        break
    else:
        if(entrada_menor):
            print("o numero é menor que isso")
        if(entrada_maior):
            print("o numero e maior que isso")

    pontos_perdidos =  abs(n_secreto - n_tentativas) #(80 - 40) = -20
    pontos = pontos -  pontos_perdidos   
    rodada = rodada + 1

print("Fim de Jogo")
