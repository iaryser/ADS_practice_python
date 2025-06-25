
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung11/al/aufgabe02
# Version: Sun May  4 17:01:35 CEST 2025

from uebung11.graphs.graph import Graph
from uebung11.graphs.graph_adv import GraphADV
from uebung11.al.aufgabe02.depth_first_search import DepthFirstSearch


if __name__ == '__main__':
  
  graph = Graph() # without ADV
  #graph = GraphADV() # with ADV
  
  v_a = graph.insert_vertex('A')
  v_b = graph.insert_vertex('B')
  v_c = graph.insert_vertex('C')  
  v_d = graph.insert_vertex('D') 
  v_e = graph.insert_vertex('E')   
  
  graph.insert_edge(v_a, v_b)
  graph.insert_edge(v_a, v_c)
  graph.insert_edge(v_a, v_d)
  graph.insert_edge(v_a, v_e)
  graph.insert_edge(v_b, v_c)
  graph.insert_edge(v_c, v_d)
  graph.insert_edge(v_c, v_e)
  
  dfs = DepthFirstSearch()
  dfs.search(graph)
  
  dfs.print_maps()


""" Session-Log:

DepthFirstSearch._search(): v = A
  e = A-B
    w = B
DepthFirstSearch._search(): v = B
  e = A-B
  e = B-C
    w = C
DepthFirstSearch._search(): v = C
  e = A-C
    w = A
  e = B-C
  e = C-D
    w = D
DepthFirstSearch._search(): v = D
  e = A-D
    w = A
  e = C-D
  e = C-E
    w = E
DepthFirstSearch._search(): v = E
  e = A-E
    w = A
  e = C-E
  e = A-C
  e = A-D
  e = A-E

DepthFirstSearch.print_maps():
Vertex-Map : {A=VISITED, B=VISITED, C=VISITED, D=VISITED, E=VISITED}
Edge-Map   : {A-B=DISCOVERY, A-C=BACK, A-D=BACK, A-E=BACK, B-C=DISCOVERY, C-D=DISCOVERY, C-E=DISCOVERY}

"""
  
