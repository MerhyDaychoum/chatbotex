from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('TW Chat Bot')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo',
            'Você gosta de programar?', 'Sim, eu programo em Python', 'Quantos anos voce tem?',
            '24', 'Qual seu nome?', 'Meu nome é Paula Dentro']

conversa02 = ['Ola', 'WHATSUUUUUP BRO?', 'Voce tem nome?', 'Sim, eu me chamo Paula Dentro', 'Qual sua idade?', '22']

conversa03 = ['Ola meu anjo', 'Oi sumido, rs', 'Vem sempre aqui?', 'Somente quando você vem! rs']

bot.set_trainer(ListTrainer)
bot.train(conversa)
bot.train(conversa02)
bot.train(conversa03)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('TW Bot: ', resposta)
    else:
        print('TW Bot: Ainda não sei responder esta pergunta')