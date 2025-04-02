from tkinter import *
import tkinter as tk
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""


model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


janela = tk.Tk()
janela.title("Chatbot")

texto_inicial = Label(janela, text="Bem-vindo ao chatbot")
texto_inicial.grid(column=0, row=0, padx=10, pady=10)

entrada_user = tk.Text(janela, height=3, width=50)
entrada_user.grid(column=0, row=1, padx=10, pady=10)


def pegar_texto():
    texto = entrada_user.get("1.0", tk.END)
    texto_bot["text"] = texto

    context = ""
    user_input = entrada_user.get("1.0", tk.END)
    # texto_bot["text"] = user_input


    result = chain.invoke({"context": context, "question": user_input})
    texto_bot["text"] = result
    # print("Bot: ", result)
    context += f"\nUser: {user_input}\n AI: {result}"


botao = Button(janela, text="executar", command= pegar_texto)
botao.grid(column=0, row=2, padx=10, pady=10)

botao_sair = Button(janela, text="sair", command= janela.quit)
botao_sair.grid(column=0, row=3, padx=10, pady=10)

texto_bot = Label(janela, text="insira aqui o texto do bot")
texto_bot.grid(column=0, row=4, padx=10, pady=10,)




janela.mainloop()