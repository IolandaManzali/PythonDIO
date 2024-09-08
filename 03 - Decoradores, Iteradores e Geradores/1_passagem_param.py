def executar(qualquer_funcao, nome,idade):
    return qualquer_funcao(nome,idade)

def funcao1(nome,idade):
    return f"Oi {nome}!"

def funcao2(nome,idade):
    return f"Olá tudo bem com você {nome}?"

def funcao3(nome,idade):
    return f"{nome} tem {idade} anos."
    
print(executar(funcao3, "Joao",21))
