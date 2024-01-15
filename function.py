# Funções em Python.
"""
Funções são trechos de códigos utilizados para replicar determinadas ações ao longo do código. 

def - diz ao python que você está criando uma função;
nome - é um bom costume colocar o que a função faz
() - parametros/argumentos, são dados que sua função precisa para poder funcionar da maneira correta.
"""
# Observação: Uma boa pratica de programação é que o nome da função deve ser criado com letras minúculas.

def somar_dois_valores(x,y):
    calculo = x + y
    return calculo
#print(somar_dois_valores(5,6))

#print(somar_dois_valores(5,))
"""
Quando você cria uma função que precisa de parâmetros, quando isso não for atendido o python retorna-rá um erro. 
No caso da função somar_dois_valores(), o tipo de erro retornado foi:

TypeError: somar_dois_valores() missing 1 required positional argument: 'y'
"""
print("="*20)
print("CRIAR NOME COMPLETO")
print("="*20)

nome = input("Nome:")
sobre_nome = input("Sobrenome:")

def nome_completo(nome, sobre_nome):
    nome_completo = f'{nome} {sobre_nome}.'

    return nome_completo

print("="*20)
print(f"Seu nome completo será: ", nome_completo(nome, sobre_nome))
print("="*20)