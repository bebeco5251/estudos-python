import random

def aleatoria(listapalavras):
    return random.choice(listapalavras)


lista = ["esqueleto", "maçarico", "neymar","laranja", "melancia","refrigerante","anel","abobora"]
palavraaleatoria = aleatoria(lista)
print(palavraaleatoria)

def verificar(palavra,letra):
 
 for letra in palavra:
  if letra in palavra:
    print("existe",letra) 
  else:
    print("não existe") 


verificar(palavraaleatoria,"a")

#joia