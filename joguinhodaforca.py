import random

def aleatoria(listapalavras):
    return random.choice(listapalavras)

lista = ["esqueleto", "maçarico", "neymar","laranja", "melancia","refrigerante","anel","abobora"]

def verificar(palavra,letra):
  estado=''
  for letter in palavra:
    if letter in letra:
      estado+=letter + ' ' 
    else:
      estado+='_ ' 
  return estado.strip()
     
  



def jogo():

    tentativas=0

    maximatentativas=6 
  
    palavra= aleatoria(lista)

    letrasadivinhadas=set()
    
    
    
    
    
    while tentativas < maximatentativas:
      
      
      estado= verificar(palavra,letrasadivinhadas)
      print(estado)
      print(letrasadivinhadas)
      letra=input("digite uma letra")
      if letra in letrasadivinhadas:
         print ("essa vc ja tentou, tente outra")
         #tentativas +=1
      else:                       
          letrasadivinhadas.add(letra)

      if letra in palavra:
        print("acertou") 
        letrasadivinhadas.add(letra) 

      else: 
        print ("errou") 
        tentativas+=1

      if set(palavra) <= letrasadivinhadas:
        print("acertou a palavra")
        break


      if tentativas ==6: 
        print("perdeu")

jogo()



























