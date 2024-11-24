import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

api_key = 'api_key_langchain_groq'
os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')

def resposta_bot(mensagem):
    mensagem_modelo = [('system', 'Assitente de Inteligencia Artifical!')]
    mensagem_modelo += mensagem
    template = ChatPromptTemplate.from_messages(mensagem_modelo)
    chain = template | chat
    return chain.invoke({}).content

print('Bem Vindo ao Chatbot\n')

mensagem = []
while True:
    pergunta = input('usuario:\n')
    if pergunta.lower() == 's':
        break
    mensagem.append(('user', pergunta))
    resposta = resposta_bot(mensagem)
    mensagem.append(('assistant', pergunta))
    print(f'bot: {resposta}')
    
print('muito obrigado por usar o chatbot\n')
print(mensagem)