import chat as bot

nome_maquina= "joia"
bot.greetings(nome_maquina)
while True:
    texto = bot.recebetexto()
    resposta = bot.search_answer(nome_maquina, texto)
    # if bot.show_answer(resposta, nome_maquina) == "fim":
    #     break













