# pip install pyautogui
import pandas  # Importar biblioteca pandas para trabalhar com base de dados
import pyautogui  # biblioteca para interagir com o mouse e tecladochrome
import time  # biblioteca para pausar o programa


pyautogui.PAUSE = 0.5  # Pausa por 0.5 segundo entre cada ação

# pyautogui.click -> Clicar na tela
# pyautogui.press -> Pressionar uma Tecla do teclado
# pyautogui.write -> Escrever um Texto
# pyautogui.hotkey -> Atalho de teclado (ctrl, C)
# pyautogui.moveTo -> Mover o mouse para uma posição


#                PASSO A PASSO DO PROGRAMA


# Passo 1: Entrar no sistema da empresa


# https://dlp.hashtagtreinamentos.com/python/intensivao/login


pyautogui.press("win")  # pressionar a tecla windows

pyautogui.write("chrome")  # escrever o nome do navegador

pyautogui.press("enter")  # pressionar a tecla enter

# escrever a url do site
pyautogui.write("https://gabrielb04.github.io/Site-Automacao-Py/")

pyautogui.press("enter")  # pressionar a tecla enter
time.sleep(2)  # pausar o programa por 2 segundos


# Passo 2: Fazer login


# usar (auxiliar.py) para puxar o posiçao do mouse para o campo email

pyautogui.click(x=518, y=436)  # clicar no campo email

pyautogui.write("Gabriel@gmail.com")  # escrever o email

pyautogui.press("tab")  # pressionar a tecla tab para ir para o campo senha

pyautogui.write("123456")  # escrever a senha

pyautogui.press("tab")  # pressionar a tecla tab para ir para o campo login

pyautogui.press("enter")  # pressionar a tecla enter para fazer login


# Passo 3: Importar a base de produtos pra cadastrar


# pip install pandas openpyxl


pandas.read_csv("produtos.csv")  # lendo a base de produtos do csv


# Criando uma Variavel Para Armazenar o Banco de Dados
Tabela = pandas.read_csv("produtos.csv")

print(Tabela)  # Imprimir a base de produtos


time.sleep(1)  # pausar o programa por 1 segundo


# Passo 4: Cadastrar um produto

# Logica for :
# for item in lista_itens: para cada "Item" na lista de itens, faça o seguinte:
# # item é cada item da lista / pode ser colocado como linha ou coluna


for linha in Tabela.index:  # Para Cada Linha Da Tabela Fazer as Seguintes Funções abaixo
    # Tabela.index -> Linhas do banco de dados
    # Tabela.columns -> Colunas do banco de dados
    # dar um "tab" para colocar as funções dentro do "for"
    pyautogui.click(x=468, y=397)  # clicar no botão cadastrar produto


# FORMULA
# Item = variavel que armazena o banco de dados.loc [linha, coluna] ->
    # Codigo
   # quando precisar selecionar algo de uma lista ou tabela coloca "[]" passa a linha e a coluna
    # a Linha nesse caso e dinamica por isso se repete indo de cima para baixo
    codigo = Tabela.loc[linha, "codigo"]  # Pegar os Codigos da Coluna Codigo
    pyautogui.write(codigo)
    pyautogui.press(str("tab"))
    # Marca
    marca = Tabela.loc[linha, "marca"]  # Pegar as Marcas da Coluna Marca
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    # Tipo
    tipo = Tabela.loc[linha, "tipo"]  # Pegar os Tipos da Coluna Tipo
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    # Categoria
    # Pegar as Categorias da Coluna Categoria
    categoria = Tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    # Preco_unitario
    # Pegar os Precos_Unitarios da Coluna Preco_Unitario
    preco_unitario = Tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    # Custo
    custo = Tabela.loc[linha, "custo"]  # Pegar os Custos da Coluna Custo
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    # obs
    obs = str(Tabela.loc[linha, "obs"])  # Pegar as Obs da Coluna Obs
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    # usa-se "STR" para converter para string - transformando em texto para que possa ser digitado no campo

    # pressionar a tecla enter para cadastrar o produto
    pyautogui.press("enter")

    pyautogui.scroll(1000)  # rolar a tela para cima ou para baixo
    # numero positivo = scroll para Cima
    # numero negativo = scroll para Baixo


# Passo 5: Repetir o processo de cadastro até o fim
