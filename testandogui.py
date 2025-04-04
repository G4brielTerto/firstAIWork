from tkinter import *
import tkinter as tk
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


context = []

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
texto_inicial.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

entrada_user = tk.Text(janela, height=3, width=50)
entrada_user.grid(column=0, row=1, padx=10, pady=10, columnspan=2)



def pegar_texto():
    one_context = ""
    user_input = entrada_user.get("1.0", tk.END)


    result = chain.invoke({"context": context, "question": user_input})
    texto_bot["text"] = result

    one_context += f"\nUser: {user_input}\n AI: {result}"
    context.append(one_context)



botao = Button(janela, text="executar", command= pegar_texto, width=20, height=2, bg="blue", fg="white", activebackground="yellow", activeforeground="black")
botao.grid(column=0, row=2, padx=10, pady=10,)

botao_sair = Button(janela, text="sair", command= janela.quit, width=20, height=2, bg="blue", fg="white", activebackground="yellow", activeforeground="black")
botao_sair.grid(column=1, row=2, padx=1, pady=10)

texto_bot = Label(janela, text="insira aqui o texto do bot wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww", wraplength=330, justify="left")
texto_bot.grid(column=0, row=3, padx=10, pady=10, columnspan=2)




janela.mainloop()