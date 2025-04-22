
from DataStructures.List import single_linked_list as sll

def new_map():
    red_black_tree = {"root": None,
                      "type": "RBT"}

    return red_black_tree

def insert_node (root, key,value):
    
   def insert_node(root, key, value):
    """
    Inserta (key, value) en el RBT con raíz `root`. 
    Si ya existe la clave, sólo actualiza el valor.
    Devuelve la nueva raíz del subárbol.
    """
    # 1) Inserción BST básica
    if root is None:
        return {
            "key": key,
            "value": value,
            "left": None,
            "right": None,
            "color": "RED",    # nuevo nodo siempre rojo
            "size": 1          # tamaño inicial
        }
    if key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    elif key > root["key"]:
        root["right"] = insert_node(root["right"], key, value)
    else:
        # reemplazo de valor en caso de clave duplicada
        root["value"] = value

    # 2) Reparaciones LLRB (reglas 2.1, 2.2, 2.3)
    # 2.1 Si hay enlace rojo a la derecha: rotar izquierda
    if is_red(root["right"]) and not is_red(root["left"]):
        root = rotate_left(root)
    # 2.2 Si hay doble enlace rojo por la izquierda: rotar derecha
    if is_red(root["left"]) and is_red(root["left"]["left"]):
        root = rotate_right(root)
    # 2.3 Si ambos hijos son rojos: flip de colores
    if is_red(root["left"]) and is_red(root["right"]):
        flip_colors(root)

    # 3) Actualizar tamaño del subárbol
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

    
    
def put (my_rbt, key, value):
    my_rbt["root"] = insert_node(my_rbt["root"], key, value)
    my_rbt["root"]["color"] = "BLACK"
     
    return my_rbt


def get_node (root, key):
    
    if root is None:
        return None
    if key == root["key"]:
        return root["value"]
    elif key < root['key']:
        return get_node(root["left"], key)
    elif key > root["key"]:
        return get_node(root["right"],key)
        
     
    
def get (my_rbt, key):
    
    return get_node(my_rbt["root"], key)


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


def remove (my_rbt, key):
    
    my_rbt["root"] = remove_node(my_rbt["root"], key)
    if my_rbt["root"] is not None:
        my_rbt["root"]["color"] = "BLACK" # le cambia el color al root a negro que siempre debe ser negro
    return my_rbt


def contains (my_rbt,key):
    
    if get(my_rbt,key) is not None:
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
        
        
def get_min_node (root):
    
    if root is None:
        return None
    else:
        return get_min_node(root["left"])  # busca recursivamente el menor de los hijos izquierdos

def get_min (my_rbt):
    
    return get_min_node(my_rbt["root"]) # se llama a la funcion que busca el menor de los hijos izquierdos


def get_max_node (root):
    
    if root is None:
        return None
    else:
        return get_max_node(root["right"])
    

def get_max (my_rbt):
    return get_max_node(my_rbt["root"]) # se llama a la funcion que busca el mayor de los hijos derechos

def delete_min_node (root):
    
    if root is None:
        return None
   
    if root["left"] is None:  # si ya el left no tiene hijos significa que es el menor 
        return root["right"]  # En la llamada recursiva de arriba, ese valor se asignará al puntero izquierdo de su padre, “saltándonos” a root y dejando intactos todos los nodos mayores.
    
    root["left"] = delete_min_node(root["left"]) # si tiene hijo izquierdo se llama a la funcion recursivamente
    
    return root         

def delete_min (my_rbt):
    
    my_rbt["root"] = delete_min_node(my_rbt["root"]) # se llama a la funcion que elimina el menor de los hijos izquierdos
    if my_rbt["root"] is not None:
        my_rbt["root"]["color"] = "BLACK" # se cambia el color del root 
        

def delete_max_node (root):
    if root is None:
        return None
    
    if root["right"] is None:
        return root["left"]
    
    root["right"] = delete_max_node(root["right"])
    
    return root 

def delete_max (my_rbt):
    
    my_rbt["root"] = delete_max_node(my_rbt["root"]) 
    if my_rbt["root"] is not None:
        my_rbt["root"]["color"] = "BLACK" 
    
            
def floor_key (root, key):
    
    if root is None:
        return None
    if key == root["key"]: # si la llave ya esta retorna la llave
        return root["key"]
    if key < root["key"]:
        return floor_key(root["left"], key) # si la llave es menor el candidato debe estar a la izquierda
    
    candidate = floor_key(root["right"], key) # si la llave es mayor el candidato debe estar a la derecha
    if candidate is not None:  
        return candidate    # si el candidato no es none significa que hay algo a la derecha y se retorna la llave del candidato
    else:
        return root["key"] # si el candidato es none significa que no hay nada a la derecha y se retorna la llave del padre
         
        
def floor (my_rbt, key):
    
    x = floor_key(my_rbt["root"], key) # se llama a la funcion que busca el menor de los hijos izquierdos
    
    return x 

def ceiling_key (root, key):
    
    if root is None:
        return None
    if key == root["key"]:
        return root["key"]
    
    if key > root["key"]:
        return ceiling_key(root["right"], key)
    
    
    candidate = ceiling_key(root["left"], key) # aqui es key < root["key"] por lo que ya estaria a la izquierda
    
    if candidate is not None:
        return candidate 
    else:
        return root["key"]
    

def ceiling (my_rbt, key):
    
    x = ceiling_key(my_rbt["root"], key) 
    return x
    

def select_key (root, key):
    
    if root is None:
        return None

    left_count = size_tree(root["left"])

    if key < left_count:
     
        return select_key(root["left"], key)
    elif key == left_count:
        # es la clave de la raíz
        return root["key"]
    else:
        # está en la derecha, ajustamos pos
        return select_key(root["right"], key - left_count - 1)

    
def select (my_rbt, pos):
    
    return select_key(my_rbt, pos)
    
def rank_keys (root, key):
    
    if root is None:
        return 0
    if key <= root["key"]:
        return rank_keys(root["left"], key)
    else:
        menores = size_tree(root["left"]) 
        
        return 1 + menores + rank_keys(root["right"], key)
    
    
def rank (my_rbt, key):
    
    x = rank_keys(my_rbt["root"], key) 
    return 
      
      
def height_tree (root):
    
    if root is None:
        return 0 
    else:
        x = height_tree(root["left"]) # hace recusrivamente el conteo de izquierda
        y = height_tree(root["right"]) # y derecha 
        
        if x >= y:
            return x + 1 # se le suma 1 al mayor de los dos (1 porque es el root)
        elif y > x:
            return y +1
       

def height (my_rbt):
    return height_tree(my_rbt["root"])

def values_range(root, key_initial, key_final, value_list):
    
    if root is None:
        return value_list
    if key_initial < root["key"]: # si la llave inicial es menor que la del root se tiene que ir a la izquierda
        values_range(root["left"], key_initial, key_final, value_list)
    if key_initial <= root["key"] <= key_final:  # si esta en el rango entra a la lista
        sll.add_last(value_list, root["value"])
    if key_final > root["key"]: # si la llave final es mayor que la del root se tiene que ir a la derecha 
        values_range(root["right"], key_initial, key_final, value_list)
    
    return value_list
    
def values (my_rbt, key_initial, key_final):
    
    value_list = sll.new_list()
    if my_rbt is not None:
        value_list = values_range(my_rbt["root"], key_initial, key_final, value_list) 
    return value_list

        
    
     
def keys_range(root, key_initial, key_final, key_list):
    if root is None:
        return key_list

    if key_initial < root["key"]:
        keys_range(root["left"], key_initial, key_final, key_list)

    if key_initial <= root["key"] <= key_final:
        sll.add_last(key_list, root["key"])

    if root["key"] < key_final:
        keys_range(root["right"], key_initial, key_final, key_list)

    return key_list

        

def keys (my_rbt, key_initial, key_final):
    
    key_list = sll.new_list()
    if my_rbt is not None:
        key_list = values_range(my_rbt["root"], key_initial, key_final, key_list) 
    return key_list


def rotate_left (node_rbt):
    
    x= node_rbt["right"]            # se guarda el hijo derecho
    node_rbt["right"] = x["left"]   # se cambia el hijo derecho por el hijo izquierdo del hijo derecho
    x["left"] = node_rbt            # se cambia el hijo izquierdo del hijo derecho por el nodo padre
    x["color"] = x["left"]["color"] # se cambia el color del nodo hijo por el del padre
    x["left"]["color"] = "RED"      # se cambia el color del padre por rojo
    x["size"] = node_rbt["size"]
    node_rbt ["size"] = 1 + size_tree(node_rbt["left"]) + size_tree(node_rbt["right"]) # se cambia el tamaño del padre
    
    return x


def rotate_right (node_rbt):
    
    x= node_rbt["left"] # se guarda el hijo izquierdo
    node_rbt["left"] = x["right"] # se cambia el hijo izquierdo por el hijo derecho del hijo izquierdo
    x["right"] = node_rbt # se cambia el hijo derecho del hijo izquierdo por el nodo padre
    x["color"] = x["right"]["color"]
    x["right"]["color"] = "RED"  
    x["size"] = node_rbt["size"]
    node_rbt ["size"] = 1 + size_tree(node_rbt["left"]) + size_tree(node_rbt["right"]) \
        
    return x 

def flip_node_color (node_rbt):
    
    if node_rbt is not None:
        
        if node_rbt["color"] == "RED":
            node_rbt["color"] = "BLACK"
        else:
            node_rbt["color"] = "RED"
            

def flip_colors (node_rbt):
    
    if node_rbt is not None:
        flip_node_color(node_rbt["left"])
        flip_node_color(node_rbt["right"])
        flip_node_color(node_rbt)
    
    
def is_red (node_rbt):
    
    if node_rbt is not None:
        return node_rbt["color"] == "RED"
    else:
        return False
    