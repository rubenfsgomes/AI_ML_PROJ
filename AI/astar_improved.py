from graph import Grafo
from vetor import VetorOrdenado
import math
import os, psutil

TAMANHO = 15

PortoZona1 = []
PortoZona2 = []
SumZona1=0
SumZona2=0


process = psutil.Process(os.getpid())
# process.memory_info().rss

grafo = Grafo()

grafo.ShipAlacrity.adjacentes
grafo.ShipAlacrity.adjacentes[0].vertice.rotulo, grafo.ShipAlacrity.adjacentes[0].vertice.distancia_objetivo

grafo.ShipAlacrity.adjacentes[0].distancia_aestrela, grafo.ShipAlacrity.adjacentes[0].tempo

vetor = VetorOrdenado(20)
vetor.insere(grafo.ShipAlacrity.adjacentes[0])
vetor.insere(grafo.ShipAlacrity.adjacentes[1])
vetor.insere(grafo.ShipAlacrity.adjacentes[2])

class AEstrela:
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False
    self.zona1 = 0
    self.zona2 = 0
    self.visited = set()
    self.adjacent_nodes = {}

  def buscar(self, atual):
    self.visited.add(atual)

    if atual in self.adjacent_nodes:
      del self.adjacent_nodes[atual]

    insert(atual, self.objetivo)

    if self.zona2 >= self.objetivo and self.zona2 >= self.objetivo:
      self.encontrado = True
    else:
      
      for adjacente in atual.adjacentes:
        if adjacente.vertice not in self.visited:
          self.visited.add(adjacente.vertice)
          if adjacente.tamanho >= TAMANHO:
            adjacente.distancia_aestrela = adjacente.tempo + heuristica(adjacente, SumZona2)
            self.adjacent_nodes[adjacente] = adjacente.distancia_aestrela
          else:
            adjacente.distancia_aestrela = adjacente.tempo + heuristica(adjacente, SumZona1)
            self.adjacent_nodes[adjacente] = adjacente.distancia_aestrela

      if len(self.adjacent_nodes) > 0:
        self.adjacent_nodes = {k: v for k, v in sorted(self.adjacent_nodes.items(), key=lambda item: item[1])}
        self.buscar(list(self.adjacent_nodes.keys())[0].vertice)
        
def heuristica(adjacente, horaAtual):
  return math.sqrt(abs(adjacente.horaChegada**2 - horaAtual**2))
  
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
busca_aestrela.buscar(grafo.ShipAbdiel)

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

  return total_wait_time / total_ships

print(calculate_average_waiting_time(PortoZona1, PortoZona2))