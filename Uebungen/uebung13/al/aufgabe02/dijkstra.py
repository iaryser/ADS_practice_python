
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung13/al/aufgabe02
# Version: Mon May 19 19:00:45 CEST 2025

import sys

from uebung13.graphs.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from uebung13.graphs.graph import Graph


class Dijkstra:

  def __init__(self):
    self._graph = None
    self._distances = self._get_distance_map()
    self._locators = self._get_locators_map()
    self._parents = self._get_parents_map()
    
  def distances(self, graph, s):
    self._graph = graph
    self._apq = self._get_adaptable_priority_queue()

    # TODO Implement here ...
    
          
  def get_graph(self):    
    return Graph()
  
  def _get_adaptable_priority_queue(self):    
    return AdaptableHeapPriorityQueue()
    
  def _get_distance_map(self):    
    return dict()

  def _get_locators_map(self):    
    return dict()

  def _get_parents_map(self):    
    return dict()
  
  def print_distances(self):
    print("\nDistances:")
    for v in self._graph.vertices():
      print(str(v) + ": " + str(self._distances.get(v)))
      
