# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from uebung13.graphs.heap_priority_queue import HeapPriorityQueue
from uebung13.graphs.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue

class AdaptableHeapPriorityQueueADV(AdaptableHeapPriorityQueue):
  
  def __init__(self, dijkstra_adv):
    super(AdaptableHeapPriorityQueueADV, self).__init__()
    self._dijkstra_adv = dijkstra_adv
    self._locator_map = dict()
    self._locator_nr = 0
    
  def __len__(self):
    length = AdaptableHeapPriorityQueue.__len__(self)
    if length == 0:
      self._dijkstra_adv._send_message("APQ.isEmpty,");
    return length
    
  def insert(self, key, value):
    self._dijkstra_adv._send_message("APQ.insert," + str(key) + "," + str(value) + "," + str(self._locator_nr))
    locator =  AdaptableHeapPriorityQueue.insert(self, key, value)
    self._locator_map[locator] = self._locator_nr
    self._locator_nr += 1
    return locator
  
  def replace_key(self, loc, newkey):
    self._dijkstra_adv._send_message("APQ.replaceKey," + str(self._locator_map.get(loc)) + "," + str(newkey))
    return AdaptableHeapPriorityQueue.replace_key(self, loc, newkey)

  def remove_min(self):
    self._dijkstra_adv._send_message("APQ.removeMin")
    return AdaptableHeapPriorityQueue.remove_min(self)
  
  
  
  
