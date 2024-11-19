palavras = ["feio", "bobo","boboca","pateta"]
def greetings(name):
    import random 
    frases = ["ola meu nome é " + name +"como vai você", "eae"]
    return frases [random.randint(0,2)]


#-----função que verifica se uma palavra existe dentro de uma lista


def prohibited_words(text):
    for p in palavras: 
        if p != text:  
            pass
        else:
            return True
    return False
        
print(prohibited_words("bobo"))




def recebetexto():

        texto = "cliente" + input ("cliente: ")

        palavras = prohibited_words(texto)

        if palavras == False:
            return texto 
        else:   
            return recebetexto()




















def search_answer(name,text):  
 with open("base.txt", "a+") as knwo:
        knwo.seek(0)
        while True:
            see = knwo.readline()
            #print(see)
            if see !="":
                if text.replace("Cliente: "," ") == "TEM NADA AQUI ADEUS":
                    print(name+ ": volte sempre!")
                    return "fim"
                elif see.strip() == text.strip():
                    nextline = knwo.readline()
                    if "chatbo:" in nextline:
                        return nextline
            else:
                print("Me desculpe, não tenho esse conhecimento ainda mestre")
                knwo.write("\n" + text)   
                respota_user = input("O que esperava?\n")
                isproibo = prohibited_words(respota_user)

                if isproibo == False:
                    knwo.write("\n" + "chatbo: " + respota_user)
                    return "Hummmmmmmmmmmmm"    
                return "Não pode"    

print(search_answer("joia","beleza"))














def show_answer(answer, name):
    print(answer.replace("chatbot", name))
    if answer == "fim":
            return "fim"
    return "continua"





























