
from DataStructures.List import single_linked_list as sll

def new_map():
    red_black_tree = {"root": None,
                      "type": "RBT"}

    return red_black_tree

def insert_node (root, key,value):
    
    if root is None:
        return 
    
    
def put (my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    my_bst["root"]["color"] = "BLACK"
     
    return my_bst



def get_node (root, key):
    
    if root is None:
        return None
    if key == root["key"]:
        return root["value"]
    elif key < root['key']:
        return get_node(root["left"], key)
    elif key > root["key"]:
        return get_node(root["right"],key)
        
     
    
def get (my_bst, key):
    
    return get_node(my_bst["root"], key)


def remove_node(root, key):
    
    if root is None:
        return None
    elif key < root['key']:
        return remove_node(root["left"], key)
    elif key > root["key"]:
        return remove_node(root["right"],key)
    else:
        if root["left"] is None:  # si es una hoja o tiene un solo hijo 
            return root["right"]  #  si es hoja ambos right y left son none 
        elif root["right"] is None:  # si tiene un solo hijo se sube el lado que no este vacio 
            return root["left"]
        
        successor = root ["right"]  # si tiene dos hijos se busca al sucesor
        while successor["left"] is not None: # se busca al menor de los hijos de la derecha 
            successor = successor["left"]   # ya que solo se necesitaria cambiar este para mantener el orden 
      
        root['key'] = successor["key"]  # se cambia la llave del nodo a eliminar por la del sucesor
        if "value" in successor:        # se cambia el valor del nodo a eliminar por el del sucesor
            root["value"] = successor["value"] 
            
        root['right'] = remove_node(root["right"], successor['key']) # se elimuna el succesor ya que esta repetido 
            
    return root


def remove (my_bst, key):
    
    my_bst["root"] = remove_node(my_bst["root"], key)
    if my_bst["root"] is not None:
        my_bst["root"]["color"] = "BLACK" # le cambia el color al root a negro que siempre debe ser negro
    return my_bst


def contains (my_bst,key):
    
    if get(my_bst,key) is not None:
        return True
    else:
        return False
    
def size_tree (root):
    
    if root is None:
        return 0 
    else:                                                               # no hay variable local que lleve el conteo
        return 1 + size_tree(root["left"]) + size_tree(root["right"])  # es la propia pila ejecucion que se encarga de hacer el conteo 
    

def size (my_rbt):
    return size_tree(my_rbt)

def is_empty (my_rbt):

    if my_rbt is None:
        return True 
    else:
        return False
    
    
def key_set_tree (root, key_list):
    
    if root is None:
        return key_list
    else:
        key_set_tree (root["left"], key_list) #va recursivamente hacia el elemento mas a la derecha
        sll.add_last(key_list, root["key"])   # lo anade a la lista
        key_set_tree (root["right"], key_list)  # RECORRIDO IN ORDER REVISAR PAPEL 
        

def key_set (my_rbt):
    
    key_list = sll.new_list()
    if my_rbt is not None:
        key_list = key_set_tree(my_rbt["root"], key_list) #simplemente aplica el inorder 
    return key_list



def value_set_tree (root, value_list):
    
    if root is None:
        return value_list
    else:
        key_set_tree (root["left"], value_list) 
        sll.add_last(value_list, root["key"])   
        key_set_tree (root["right"], value_list)  

def value_set (my_rbt):
    
    value_list = sll.new_list()
    if my_rbt is not None:
        value_list = key_set_tree(my_rbt["root"], value_list) 
    return value_list
        
