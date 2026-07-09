from openai import OpenAI

client = OpenAI(api_key="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")

lista_mensagens = []

def enviar_mensagem(mensagem):
    lista_mensagens.append(
        {
            "role": "user",
            "content": mensagem
        }
    )

    resposta = client.responses.create(
        model="gpt-5",
        input=mensagem
    )

    return resposta.output_text


while True:
    texto = input("Quando desejar sair da conversa, digite 'sair': ")

    if texto.lower() == "sair":
        break

    resposta = enviar_mensagem(texto)
    print("Chatbot:", resposta)