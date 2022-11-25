import sort_palavra as s
import estagios as e

import estagios
def bonequinho(v):
  if v == 5:
    print(e.d1)
  elif v == 4:
    print(e.d2)
  elif v == 3:
    print(e.d3)
  elif v == 2:
    print(e.d4)
  elif v == 1:
    print(e.d5)



class Jogo():
  def __init__(self):
    self.palavra = ''
    self.n_palavra = ''
    self.quant_l = ''
    self.vidas = ''

# ===================================================================================
  def getPalavra(self):
    return self.palavra
  def setPalavra(self, p):
    self.palavra = p

  def getN_Palavra(self):
    return self.n_palavra
  def setN_Palavra(self,np):
    self.n_palavra = np

  def getQuant_L(self):
    return self.quant_l
  def setQuant_L(self, q):
    self.quant_l = q

  def getVidas(self):
    return int(self.vidas)
  def setVidas(self, v):
    self.vidas = v
  def dano(self, vPerdida):
    self.vidas = self.getVidas() - vPerdida
    bonequinho(self.getVidas())
# ===================================================================================

  def start(self):
    p = s.comp(s.lista)
    self.setPalavra(p)
    
    tamanho = len(p)
    self.setQuant_L(tamanho)

    self.setVidas(6)

  def pega_letra(self, txt):
    letra = input(txt).upper().strip()
    return letra
  
  def confere(self, letra):
    if letra not in self.getPalavra():
      self.dano(1)
    else: 
      self.setPalavra(self.getPalavra().replace(letra, ''))
      


