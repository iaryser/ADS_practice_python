from uebung07.adv.binary_tree_module import BinaryTreeModule
from uebung07.adv.ad_visualizer import ADV
from uebung07.al.aufgabe01.binary_search_tree import BinarySearchTree

class BinarySearchTreeADV(BinarySearchTree):

  def __init__(self, session_name, max_left_height = -1, max_right_height = -1):
    super().__init__()
    self._adv_message = ""
    self._adv_tree = BinaryTreeModule(session_name, self)
    if max_left_height != -1 and max_right_height != -1:
      self._adv_tree.set_fixed_tree_height(max_left_height, max_right_height)
      
  def insert(self, key, value):
    self._adv_message = "insert(" + str(key) + "," + str(value) + ")"
    super().insert(key, value)
    self._display_on_adv()
      
  def remove(self, key):
    self._adv_message = "remove(" + str(key) + ")"
    value = super().remove(key)
    self._display_on_adv()
    return value
    
  def _display_on_adv(self):
    ADV.snapshot(self._adv_tree, "\n" + self._adv_message)
    