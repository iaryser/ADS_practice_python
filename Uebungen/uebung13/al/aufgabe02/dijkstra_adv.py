
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung13/graphs
# Version: Sun Dec 12 10:10:09 CET 2021

import time
import socket

from uebung13.al.aufgabe02.dijkstra import Dijkstra
from uebung13.graphs.graph_adv import GraphADV
from uebung13.graphs.dict_adv import dict_ADV
from uebung13.graphs.adaptable_heap_priority_queue_adv import AdaptableHeapPriorityQueueADV

class DijkstraADV(Dijkstra):        
  
  _IP = "127.0.0.1"
  _PORT = 2*4711;

  def __init__(self):
    super(DijkstraADV, self).__init__()
    self._graph = None
    self._printing_maps = False
    
  def get_graph(self):
    self._graph = GraphADV(self)
    return self._graph
  
  def _get_adaptable_priority_queue(self):
    return AdaptableHeapPriorityQueueADV(self)
  
  def distances(self, graph, s):
    self._send_message("distances")
    Dijkstra.distances(self, graph, s)
    
  def _get_distance_map(self):
    return dict_ADV(self, "distanceMap")

  def _get_parents_map(self):
    return dict_ADV(self, "parentMap")
    
  def _send_message(self, message):
    with socket.create_connection((DijkstraADV._IP, DijkstraADV._PORT)) as my_socket:
      my_socket.sendall(message.encode())
      time.sleep(0.3)
      
  def printing_maps(self, printing):
    self._printing_maps = printing
