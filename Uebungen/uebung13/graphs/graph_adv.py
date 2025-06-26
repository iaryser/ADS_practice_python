
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung13/graphs
# Version: Sun Dec 12 10:10:09 CET 2021

from uebung13.graphs.graph import Graph
from uebung13.graphs.dict_adv import dict_ADV


class GraphADV(Graph):        
  
  def __init__(self, dijkstra): 
    super(GraphADV, self).__init__()
    self._dijkstra = dijkstra
    self._printing_maps = False
  
  def insert_vertex(self, element):
    v = Graph.insert_vertex(self, element)
    self._send_message("insertVertex," + str(v))
    return v
    
  def insert_edge(self, v, w, e):
    e = Graph.insert_edge(self, v, w, e)
    self._send_message("insertEdge," + str(v) + ","  + str(w) + "," + str(e.element()) + "," + str(e))
    return e
  
  def opposite(self, v, e):
    w = Graph.opposite(self, v, e)
    self._send_message("opposite," + str(v) + ","+ str(e))
    return w
  
  def get_vertex_map(self):
    return dict_ADV(self, "vertexMap")
  
  def get_edge_map(self):
    return dict_ADV(self, "edgeMap")
  
  def _send_message(self, message):
    self._dijkstra._send_message(message)
      
  def printing_maps(self, printing):
    self._printing_maps = printing
      
