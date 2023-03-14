# Este é um jogo de Adivinhação.
# O usuário deverá acertar qual é a informação secreta.
# O objetivo do jogo é encontrar a informação secreta no menor numero de tentativas

informacao_secreta = "51"


print ("***** Olá seja bem vindo ao Jogo de Adivinhação*****")
print ("***** Você tem duas tentativas para acertar a informação secreta*****")

tentativa = input ("A pista da informação secreta é: *Este número é uma boa ideia* : ")
resultado = str(tentativa)

if resultado == informacao_secreta:
        print ("Parabéns você acertou")

else:
        print (" Você errou tente outra vez")


sair = input ("Pressione (1) Sair (2) Jogar Novamente: ")
sair_game = int(sair)

if sair_game == 1:
        exit()

elif sair_game == 2:
    tentativa = input ("A pista da informação secreta é: *Este número é uma boa ideia* : ")
resultado = str(tentativa)

if resultado == informacao_secreta:
        print ("Parabéns você acertou")

else:
        print (" Você errou tente outra vez")

print ("A informação secreta era: ", informacao_secreta)    
        
print ("Obrigado por ter participado do Jogo")
print ("*****FIM DE JOGO*****")