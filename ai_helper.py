def sugerir_codigo(descricao):
    descricao = descricao.lower()

    if "somar" in descricao:
        return "Use a função somar(a, b)"
    elif "multiplicar" in descricao:
        return "Use a função multiplicar(a, b)"
    elif "dividir" in descricao:
        return "Use a função dividir(a, b)"
    else:
        return "Funcionalidade não reconhecida pela IA"
