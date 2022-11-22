import sort_palavra as s

class Jogo():
  def __init__(self):
    self.palavra =  ''
    self.quant_l =  ''
    self.vidas =  ''

  def getPalavra(self):
    return self.palavra

  def setPalavra(self, p):
    self.palavra = p

  def getQuant_L(self):
    return self.quant_l

  def setQuant_L(self, q):
    self.quant_l = q

  def getVidas(self):
    return self.vidas

  def setVidas(self, v):
    self.vidas = v

  def Sort(self):
    self.setPalavra(s.comp(s.lista))
    

