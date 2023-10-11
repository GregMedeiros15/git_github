# Desafio de codigo para determinar se um tweet tem 140 caracteres ou menos

tweet = input ("Digite seu tweet: ")  # Entrada de texto do tweet a ser publicado

numero_de_caracteres = len (tweet) # Contagem do numero de caracteres do tweet

if numero_de_caracteres <= 140:
    print ("TWEET")
else:
    print ("MUTE")