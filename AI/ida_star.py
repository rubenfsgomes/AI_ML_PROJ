from graph import Grafo
from vetor import VetorOrdenado
import math

TAMANHO = 15

PortoZona1 = []
PortoZona2 = []
SumZona1=0
SumZona2=0

grafo = Grafo()

grafo.ShipAction.adjacentes
grafo.ShipAction.adjacentes[0].vertice.rotulo, grafo.ShipAction.adjacentes[0].vertice.distancia_objetivo

grafo.ShipAction.adjacentes[0].distancia_aestrela, grafo.ShipAction.adjacentes[0].tempo

vetor = VetorOrdenado(20)
vetor.insere(grafo.ShipAction.adjacentes[0])
vetor.insere(grafo.ShipAction.adjacentes[1])
vetor.insere(grafo.ShipAction.adjacentes[2])

def heuristica(adjacente, somaTempo1, somaTempo2):
  if adjacente.tamanho >= TAMANHO:
    result = adjacente.horaChegada - (somaTempo1 + adjacente.tempo)
    return result * result
  else:
    result = adjacente.horaChegada - (somaTempo2 + adjacente.tempo)
    return result * result


class IDA:
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False
    self.zona1 = 0
    self.zona2 = 0

    
  def alg(self, atual):
    global SumZona1, SumZona2
    threshold = heuristica(atual, SumZona1, SumZona2)
    
    while 1:
      cost = self.Search(atual, 0, threshold)
      
      if cost == float("inf"):
        return -1
      elif cost < 0:
        print("Found it!")
        return -cost
      
      threshold = cost
      
  
  def Search(self, atual, distance, threshold):
    global SumZona1
    global SumZona2
    # print("Visiting Node " + str(atual.rotulo))
    if (atual.tamanho > TAMANHO):
      estimate = distance + heuristica(atual, SumZona1, SumZona2)
    else:
      estimate = distance + heuristica(atual, SumZona1, SumZona2)
    insert(atual, self.objetivo)
    atual.visitado = True
    
    if(SumZona1 >= self.objetivo and SumZona2 >= self.objetivo):
      return -estimate
    
    if estimate > threshold:
      return estimate
    
    min = float("inf")
    for adjacente in atual.adjacentes:
      if adjacente.vertice.visitado == False:
        adjacente.vertice.visitado = True
        t = self.Search(adjacente.vertice, distance + adjacente.tempo, threshold)
        if t < 0:       
          return t
        elif t < min:
          min = t
    return min

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


ida = IDA(24)
ida.alg(grafo.ShipAlabama)

PortoZona1.sort(key=lambda x: x.horaInicio, reverse=False)
PortoZona2.sort(key=lambda x: x.horaInicio, reverse=False)

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

print("Average waiting time: " + f"{calculate_average_waiting_time(PortoZona1, PortoZona2)}")
