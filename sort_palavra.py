from random import randint

with open('palavras.txt', 'r', encoding='utf-8') as arquivo:
  lista_bruta = arquivo.readlines()
  # print(lista_bruta)
  lista = list()

  # tirar os '\n'
  for p in lista_bruta:
    lista.append(p.replace('\n', ''))
  # print(lista)
  # 


comp = lambda l: l[randint(0, len(l)-1)]


