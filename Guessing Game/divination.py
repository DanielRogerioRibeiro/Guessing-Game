# Este é um jogo de Adivinhação.
# O usuário deverá acertar qual é a informação secreta.
# O objetivo do jogo é encontrar a informação secreta no menor número de tentativas

# Resposta da Informação Secreta
informacao_secreta = 51

# Variáveis Globais
total_de_tentativas 	= 2

# Apresentação
print ("***** Olá seja bem vindo ao Jogo de Adivinhação*****")
print ("***** Você tem duas tentativas para acertar a informação secreta*****")

# Realizando Loop
for rodada in range (1, total_de_tentativas + 1):
    print ("Tentativa {} de {}".format(rodada, total_de_tentativas))
    tentativa = input ("A pista da informação secreta é: *Este número é uma boa ideia* : ")
    resultado = int(tentativa)

# Variáveis
    acertou                = resultado == informacao_secreta
    chute_for_maior  = resultado > informacao_secreta
    chute_for_menor = resultado < informacao_secreta

    if (acertou):
        print ("Parabéns você acertou")

    else:
        if (chute_for_maior):
            print ("Você Errou. Seu palpite foi maior")
        elif (chute_for_menor):
            print ("Você Errou. Seu palpite foi menor")

    


print ("A informação secreta era: ", informacao_secreta)    
        
print ("Obrigado por ter participado do Jogo")
print ("*****FIM DE JOGO*****")

