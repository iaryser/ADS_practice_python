
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung13/graphs
# Version: Sun Dec 12 10:10:09 CET 2021


class dict_ADV(dict):        
 
  def __init__(self, dijkstra_adv, map_type):
    self._dijkstra_adv = dijkstra_adv
    self._map_type = map_type

  def __setitem__(self, key, value):
    operation = self._map_type + ".put"
    self._dijkstra_adv._send_message(operation + "," + str(key) + "," + str(value))
    return dict.__setitem__(self, key, value)
  
  def __getitem__(self, key):
    if self._map_type == "edgeMap" and not self._graph_adv._printing_maps:
      operation = self._map_type + ".get"
      self._dijkstra_adv._send_message(operation + "," + str(key))
    return dict.__getitem__(self, key)
  
  
