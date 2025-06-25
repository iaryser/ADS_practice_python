
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung11/graphs
# Version: Sun Nov 28 17:43:55 CET 2021

import time
import socket
from uebung11.graphs.graph import Graph
from uebung11.graphs.dict_adv import dict_ADV


class GraphADV(Graph):        
  
  _IP = "127.0.0.1"
  _PORT = 2*4711

  def __init__(self): 
    super(GraphADV, self).__init__()
    self._printing_maps = False
  
  def insert_vertex(self, element):
    v = Graph.insert_vertex(self, element)
    self._send_message("insertVertex," + str(v))
    return v
    
  def insert_edge(self, v, w):
    e = Graph.insert_edge(self, v, w)
    self._send_message("insertEdge," + str(v) + ","  + str(w))
    return e
  
  def get_dfs_vertex_map(self):
    return dict_ADV(self, "vertexMap")
  
  def get_dfs_edge_map(self):
    return dict_ADV(self, "edgeMap")
  
  def _send_message(self, message):
    with socket.create_connection((GraphADV._IP, GraphADV._PORT)) as my_socket:
      #print(my_socket)
      my_socket.sendall(message.encode())
      time.sleep(0.3)
      
  def printing_maps(self, printing):
    self._printing_maps = printing
      