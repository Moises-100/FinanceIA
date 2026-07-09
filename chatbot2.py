from google import genai


client = genai.Client(api_key="AQ.Ab8RN6LjnmPRnzW5NO83n5Y4GWRYQUj6QX8uNsrRPka3g8bxGA")


chat = client.chats.create(model="gemini-2.5-flash")

print("--- Chatbot Gemini Iniciado ---")
print("Digite 'sair' a qualquer momento para encerrar a conversa.\n")

while True:
    texto = input("Você: ")

    if texto.lower() == "sair":
        print("Chatbot: Até logo!")
        break

    if not texto.strip():
        continue

    try:
       
        resposta = chat.send_message(texto)
        
        print(f"Chatbot: {resposta.text}\n")
        
    except Exception as e:
        print(f"\n[Erro] Não foi possível se comunicar com a API: {e}")
        print("Verifique se você colocou sua chave de API corretamente entre as aspas.\n")