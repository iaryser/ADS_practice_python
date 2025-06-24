from uebung07.adv.ad_visualizer import ADV

class BinaryTreeModule:

  def __init__(self, session_name, binary_tree):
    self._session_name = session_name
    self._binary_tree = binary_tree
    self._max_left_height = -1
    self._max_right_height = -1
    self._tree_elements = None  # list
    self._relations = None  # list
    
  def snapshot(self):
    self._tree_elements = []
    self._relations = []
    self._traverse_preorder(1, self._binary_tree._root)
    
  def _traverse_preorder(self, vector_index, node):
    content = str(node.get_key()) + " / " + str(node.get_value())
    self._tree_elements.append(ADV.Element(vector_index, content))
    #print(",".join(map(str, self._tree_elements)))
    
    if vector_index > 1: # this is a child, so there is a new relation
      self._relations.append(ADV.Relation(vector_index // 2, vector_index))
      #print(",".join(map(str, self._relations)))
      
    if self._has_left_child(node):
      self._traverse_preorder(2 * vector_index, node.get_left())
    if self._has_right_child(node):
      self._traverse_preorder(2 * vector_index + 1, node.get_right())
  
  def _has_left_child(self, node):   
    if node.get_left().is_external():
      return False
    else :
      return True
    
  def _has_right_child(self, node):   
    if node.get_right().is_external():
      return False
    else :
      return True

  def get_tree_elements(self):
    return self._tree_elements
  
  def get_relations(self):
    return self._relations
  
  def set_fixed_tree_height(self, max_left_height, max_right_height):
    self._max_left_height = max_left_height
    self._max_right_height = max_right_height
    