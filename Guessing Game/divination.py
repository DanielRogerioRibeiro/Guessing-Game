# Este é um jogo de Adivinhação.
# O usuário deverá acertar qual é a informação secreta.
# O objetivo do jogo é encontrar a informação secreta no menor número de tentativas

import random

# Apresentação
print ("***** Olá seja bem vindo ao Jogo da Adivinhação*****")
print ("***** Você deverá acertar a informação secreta*****")


# Resposta da Informação Secreta
informacao_secreta = random.randrange(1,51)
#print ("Informação secreta é: ", informacao_secreta)

# Variáveis Globais
total_de_tentativas = 0
score               = 500

#Selecionando o nível
print("Qual o nível de dificuldade que você deseja tentar?")
print("(1) Fácil (2) Moderado (3) Difícil")
nivel = int(input("Defina o seu nível: "))

if(nivel == 1): 
    total_de_tentativas = 15
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

# Realizando Loop
for rodada in range (1, total_de_tentativas + 1):
    print ("Tentativa {} de {}".format(rodada, total_de_tentativas))
    tentativa = input("Digite seu palpite entre 1 e 50: ")
    resultado = int(tentativa)

    if (resultado < 1 or resultado > 50):
        print("Você deve digitar um valor entre 1 e 50")
        continue

# Variáveis
    acertou         = resultado == informacao_secreta
    chute_for_maior = resultado > informacao_secreta
    chute_for_menor = resultado < informacao_secreta
    
            
    if (acertou):
        print ("Parabéns você acertou")
        print ("Sua pontuação foi de {} pontos.".format(pontos))
        break

    else:
       if (chute_for_maior):
            print ("Você Errou. Seu palpite foi maior")
       elif (chute_for_menor):
            print ("Você Errou. Seu palpite foi menor")
       pontos_perdidos = abs(informacao_secreta - resultado)
       pontos          = score - pontos_perdidos
   
    print ("Não foi desta vez....")
        
     
print ("A informação secreta era: ", informacao_secreta)
print ("Obrigado por ter participado do Jogo")
print ("*****FIM DE JOGO*****")

