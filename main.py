from utils import somar, multiplicar, dividir
from ai_helper import sugerir_codigo

descricao = input("Descreva a operação que deseja fazer: ")

sugestao = sugerir_codigo(descricao)
print("IA sugere:", sugestao)

if "somar" in descricao:
    print("Resultado:", somar(10, 5))
elif "multiplicar" in descricao:
    print("Resultado:", multiplicar(10, 5))
elif "dividir" in descricao:
    print("Resultado:", dividir(10, 5))
else:
    print("Operação não executada.")
