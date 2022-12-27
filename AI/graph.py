
class Vertice:

  def __init__(self, rotulo, horaChegada, tempo, tamanho):
    self.rotulo = rotulo
    self.visitado = False
    self.printed = False
    self.horaChegada = horaChegada
    self.tempo = tempo
    self.tamanho = tamanho
    self.distancia_objetivo = self.tempo + self.tamanho
    self.horaInicio = 0
    self.horaFim = 0
    self.adjacentes = []
    
  

  def adiciona_adjacente(self, adjacente):
    self.adjacentes.append(adjacente)

  def mostra_adjacentes(self):
    for i in self.adjacentes:
      print(i.vertice.rotulo, i.custo)
  

class Adjacente:
  def __init__(self, vertice, horaChegada, tempo, tamanho):
    self.vertice = vertice
    self.horaChegada = horaChegada
    self.tempo = tempo
    self.tamanho = tamanho
    self.distancia_aestrela = 0


class Grafo:
  
  
  ShipAlacrity = Vertice('ShipAlacrity', 23, 5, 4)
  ShipAlaska = Vertice('ShipAlaska', 16, 4, 18)
  ShipAlbatross = Vertice('ShipAlbatross', 8, 2, 10)
  ShipAaronWard  = Vertice('ShipAaronWard ', 13, 3, 9)
  ShipAbdiel  = Vertice('ShipAbdiel ', 1, 6, 30)
  ShipAbercrombie = Vertice('ShipAbercrombie', 14, 5, 7)
  ShipAbukuma = Vertice('ShipAbukuma', 19, 3, 32)
  ShipAcasta = Vertice('ShipAcasta', 23, 8, 25)
  ShipAcavus = Vertice('ShipAcavus', 18, 6, 14)
  ShipAchilles = Vertice('ShipAchilles', 6, 4, 7)
  ShipAconit = Vertice('ShipAconit', 9, 5, 20)
  ShipAcree = Vertice('ShipAcree', 0, 2, 10)
  ShipAction = Vertice('ShipAction', 20, 4, 25)
  ShipAlabama = Vertice('ShipAlabama', 10, 4, 13)
  ShipActive = Vertice('ShipActive', 21, 6, 15)
  ShipLisbon = Vertice('ShipLisbon', 8, 4, 24)
  ShipPorto = Vertice('ShipPorto', 15, 3, 20)
  ShipAzores = Vertice('ShipAzores', 11, 5, 13)
  

  ShipAlacrity.adiciona_adjacente(Adjacente(ShipAlaska, 16, 4, 18))
  ShipAlacrity.adiciona_adjacente(Adjacente(ShipAaronWard , 13, 3, 9))
  ShipAlacrity.adiciona_adjacente(Adjacente(ShipAbdiel , 1, 6, 30))
  ShipAlacrity.adiciona_adjacente(Adjacente(ShipActive, 21, 10, 25))

  ShipActive.adiciona_adjacente(Adjacente(ShipAlacrity, 23, 5, 4))

  ShipAlaska.adiciona_adjacente(Adjacente(ShipAlacrity, 23, 5, 4))
  ShipAlaska.adiciona_adjacente(Adjacente(ShipAlbatross, 8, 7, 10))
  ShipAlaska.adiciona_adjacente(Adjacente(ShipLisbon, 8, 4, 24))

  ShipAlbatross.adiciona_adjacente(Adjacente(ShipAlaska, 16, 4, 18))
  ShipAlbatross.adiciona_adjacente(Adjacente(ShipAaronWard , 13, 3, 9))

  ShipAaronWard .adiciona_adjacente(Adjacente(ShipAlbatross, 8, 7, 10))
  ShipAaronWard .adiciona_adjacente(Adjacente(ShipAlacrity, 23, 5, 4))
  ShipAaronWard .adiciona_adjacente(Adjacente(ShipAchilles, 6, 4, 7))
  ShipAaronWard .adiciona_adjacente(Adjacente(ShipAlabama, 10, 4, 13))

  ShipAbdiel .adiciona_adjacente(Adjacente(ShipAlacrity, 23, 5, 4))
  ShipAbdiel .adiciona_adjacente(Adjacente(ShipAbercrombie, 14, 5, 7))

  ShipAbercrombie.adiciona_adjacente(Adjacente(ShipAbdiel , 1, 6, 30))
  ShipAbercrombie.adiciona_adjacente(Adjacente(ShipAbukuma, 19, 3, 32))
  ShipAbercrombie.adiciona_adjacente(Adjacente(ShipAlabama, 10, 4, 13))
  ShipAbercrombie.adiciona_adjacente(Adjacente(ShipLisbon, 8, 4, 24))

  ShipLisbon.adiciona_adjacente(Adjacente(ShipAbercrombie, 14, 5, 7))
  ShipLisbon.adiciona_adjacente(Adjacente(ShipAzores, 11, 5, 13))
  ShipLisbon.adiciona_adjacente(Adjacente(ShipAlaska, 16, 4, 18))

  ShipAzores.adiciona_adjacente(Adjacente(ShipLisbon, 8, 4, 24))
  ShipAzores.adiciona_adjacente(Adjacente(ShipPorto, 15, 3, 20))
  ShipAzores.adiciona_adjacente(Adjacente(ShipAcree, 0, 2, 10))

  ShipPorto.adiciona_adjacente(Adjacente(ShipAzores, 11, 5, 13))
  ShipPorto.adiciona_adjacente(Adjacente(ShipAconit, 9, 5, 20))

  ShipAbukuma.adiciona_adjacente(Adjacente(ShipAbercrombie, 14, 5, 7))
  ShipAbukuma.adiciona_adjacente(Adjacente(ShipAcasta, 23, 8, 25))
  ShipAbukuma.adiciona_adjacente(Adjacente(ShipAlabama, 10, 4, 13))

  ShipAcasta.adiciona_adjacente(Adjacente(ShipAbukuma, 19, 3, 32))
  ShipAcasta.adiciona_adjacente(Adjacente(ShipAcavus, 18, 6, 14))
  ShipAcasta.adiciona_adjacente(Adjacente(ShipAction, 20, 4, 25))

  ShipAcavus.adiciona_adjacente(Adjacente(ShipAcasta, 23, 8, 25))
  ShipAcavus.adiciona_adjacente(Adjacente(ShipAcree, 0, 2,10))
  ShipAcavus.adiciona_adjacente(Adjacente(ShipAchilles, 6, 4, 7))

  ShipAchilles.adiciona_adjacente(Adjacente(ShipAcavus, 18, 6, 14))
  ShipAchilles.adiciona_adjacente(Adjacente(ShipAaronWard , 13, 3, 9))
  ShipAchilles.adiciona_adjacente(Adjacente(ShipAcree, 0, 2,10))

  ShipAconit.adiciona_adjacente(Adjacente(ShipAction, 20, 4,25))
  ShipAconit.adiciona_adjacente(Adjacente(ShipPorto, 15, 3, 20))
  
  ShipAcree.adiciona_adjacente(Adjacente(ShipAcavus, 18, 6, 14))
  ShipAcree.adiciona_adjacente(Adjacente(ShipAchilles, 6, 4, 7))
  ShipAcree.adiciona_adjacente(Adjacente(ShipAzores, 11, 5, 13))

  ShipAction.adiciona_adjacente(Adjacente(ShipAconit, 9, 5,20))
  ShipAction.adiciona_adjacente(Adjacente(ShipAlabama, 10, 4,13))
  ShipAction.adiciona_adjacente(Adjacente(ShipAcasta, 23, 8, 25))

  ShipAlabama.adiciona_adjacente(Adjacente(ShipAbukuma, 19, 3, 32))
  ShipAlabama.adiciona_adjacente(Adjacente(ShipAbercrombie, 14, 5, 7))
  ShipAlabama.adiciona_adjacente(Adjacente(ShipAaronWard, 13, 3, 9))

