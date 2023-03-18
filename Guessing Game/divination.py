# Este é um jogo de Adivinhação.
# O usuário deverá acertar qual é a informação secreta.
# O objetivo do jogo é encontrar a informação secreta no menor número de tentativas

import random

# Apresentação
print ("***** Olá seja bem vindo ao Jogo de Adivinhação*****")
print ("***** Você tem duas tentativas para acertar a informação secreta*****")

# Resposta da Informação Secreta
informacao_secreta = random.randrange(1,101)

# Variáveis Globais
total_de_tentativas = 0
score               = 500

#Selecionando o nível
print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if(nivel == 1): 
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

# Realizando Loop
for rodada in range (1, total_de_tentativas + 1):
    print ("Tentativa {} de {}".format(rodada, total_de_tentativas))
    tentativa = input ("A pista da informação secreta é: *Este número é uma boa ideia* : ")
    resultado = int(tentativa)

    if (resultado < 1 or resultado > 100):
        print("Você deve digitar um valor entre 1 e 100")
        continue

# Variáveis
    acertou                = resultado == informacao_secreta
    chute_for_maior  = resultado > informacao_secreta
    chute_for_menor = resultado < informacao_secreta
    falhou          = informacao_secreta


    if (acertou):
        print ("Parabéns você acertou")
        print ("Sua pontuação foi de {} pontos.".format(score))
        break

    else:
       if (chute_for_maior):
            print ("Você Errou. Seu palpite foi maior")
       elif (chute_for_menor):
            print ("Você Errou. Seu palpite foi menor")
        
       
print ("A informação secreta era: ", informacao_secreta)    
print ("Obrigado por ter participado do Jogo")
print ("*****FIM DE JOGO*****")

