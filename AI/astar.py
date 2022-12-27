from graph import Grafo
# from vetor import VetorOrdenado
import math
import os, psutil

TAMANHO = 15

PortoZona1 = []
PortoZona2 = []
SumZona1=0
SumZona2=0

class VetorOrdenado:
    def __init__(self, size):
        self.items = []
        self.size = size

    def insere(self, item):
        self.items.append(item)
        self.items.sort(key=lambda x: x.distancia_aestrela, reverse=False)


grafo = Grafo()

grafo.ShipLisbon.adjacentes
grafo.ShipLisbon.adjacentes[0].vertice.rotulo, grafo.ShipLisbon.adjacentes[0].vertice.distancia_objetivo

grafo.ShipLisbon.adjacentes[0].distancia_aestrela, grafo.ShipLisbon.adjacentes[0].tempo

vetor = VetorOrdenado(20)
vetor.insere(grafo.ShipLisbon.adjacentes[0])
vetor.insere(grafo.ShipLisbon.adjacentes[1])
vetor.insere(grafo.ShipLisbon.adjacentes[2])

class AEstrela:
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False
    self.zona1 = 0
    self.zona2 = 0
    self.ListaVizinhos = []

  def buscar(self, atual):
    atual.visitado = True
    if len(self.ListaVizinhos) > 0:
      self.ListaVizinhos.pop(0)
    
    insert(atual, self.objetivo)
    if SumZona1 >= self.objetivo and SumZona2 >= self.objetivo:
      self.encontrado = True
    else:
      for adjacente in atual.adjacentes:
        if adjacente.vertice.visitado == False:
          adjacente.vertice.visitado = True
          adjacente.distancia_aestrela = adjacente.tempo + heuristica(adjacente, SumZona1, SumZona2)
          self.ListaVizinhos.append(adjacente)
          self.ListaVizinhos.sort(key=lambda x: x.distancia_aestrela, reverse=False)
          
      if len(self.ListaVizinhos) > 0:
        self.buscar(self.ListaVizinhos[0].vertice)
        
        

def heuristica(adjacente, somaTempo1, somaTempo2):
  if adjacente.tamanho >= TAMANHO:
    return math.sqrt(abs((adjacente.horaChegada - somaTempo1)**2)) 
  else:
    return math.sqrt(abs((adjacente.horaChegada - somaTempo2)**2)) 
'''
def heuristica(adjacente, somaTempo1, somaTempo2):
  if adjacente.tamanho >= TAMANHO:
    return adjacente.horaChegada - (somaTempo1 + adjacente.tempo)
  else:
    return adjacente.horaChegada - (somaTempo2 + adjacente.tempo)
'''
'''
def heuristica(adjacente, somaTempo1, somaTempo2):
  if adjacente.tamanho >= TAMANHO:
    # Calculate the waiting time for the ship in zone 1 based on the current sum of stay times in that zone
    waiting_time = adjacente.horaChegada - (somaTempo1 + adjacente.tempo)
    # Return the square of the waiting time to prioritize ships with lower waiting times
    return waiting_time * waiting_time
  else:
    # Calculate the waiting time for the ship in zone 2 based on the current sum of stay times in that zone
    waiting_time = adjacente.horaChegada - (somaTempo2 + adjacente.tempo)
    # Return the square of the waiting time to prioritize ships with lower waiting times
    return waiting_time * waiting_time
'''

def insert(atual, objetivo):
  if((atual.tamanho >= TAMANHO and SumZona2 + atual.tempo <= objetivo)):
    # print(f"{atual.rotulo} na zona 2 das {SumZona2}h até às {SumZona2 + atual.tempo}h")
    insertZona2(atual)
  elif (SumZona1 + atual.tempo <= objetivo):
    # print(f"{atual.rotulo} na zona 1 das {SumZona1}h até às {SumZona1 + atual.tempo}h")
    insertZona1(atual)

def insertZona1(navio):
  global SumZona1
  navio.horaInicio = SumZona1
  navio.horaFim = SumZona1 + navio.tempo
  PortoZona1.append(navio)
  SumZona1 += navio.tempo 

def insertZona2(navio):
  global SumZona2
  navio.horaInicio = SumZona2
  navio.horaFim = SumZona2 + navio.tempo
  PortoZona2.append(navio)
  SumZona2 +=navio.tempo
  

busca_aestrela = AEstrela(24)
busca_aestrela.buscar(grafo.ShipLisbon)

PortoZona1.sort(key=lambda x: x.horaInicio, reverse=False)

print ([n.rotulo + f" {n.horaInicio}h-" + f"{n.horaFim}h" for n in PortoZona1])
print ([n.rotulo + f" {n.horaInicio}h-" + f"{n.horaFim}h" for n in PortoZona2])

def calculate_average_waiting_time(PortoZona1, PortoZona2):
  total_wait_time = 0
  total_ships = len(PortoZona1) + len(PortoZona2)

  for ship in PortoZona1:
    total_wait_time += ship.horaInicio - ship.horaChegada

  for ship in PortoZona2:
    total_wait_time += ship.horaInicio - ship.horaChegada

  return abs(total_wait_time / total_ships)

print("Average waiting time: " + f"{calculate_average_waiting_time(PortoZona1, PortoZona2)} hours")