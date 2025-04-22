from DataStructures.Tree import bst_node as bst_node
from DataStructures.List import single_linked_list as sll

def new_map():
    bst = {'root': None}
    return bst

def put(my_bst,key,value):
    my_bst['root'] = insert_node(my_bst['root'],key,value)
    return my_bst

def insert_node(root,key,value):
    if root is None: 
        root = bst_node.new_node(key,value)
    elif root['key'] == key:
        root['value'] = value
    elif key < root['key']:
        root['left'] = insert_node(root['left'],key,value)
    elif key > root['key']:
        root['right'] = insert_node(root['right'],key,value)
    
    left_size = root['left']['size'] if root['left'] else 0
    right_size = root['right']['size'] if root['right'] else 0
    root['size'] = 1 + left_size + right_size
    return root
    
    
def get(my_bst,key):
    value = get_node(my_bst['root'],key)
    return value
    
def get_node(root,key):
    if root == None:
        return None
    elif root["key"] == key:
        return root['value']
    elif key > root['key']:
        return get_node(root["right"],key)
    elif key < root['key']:
        return get_node(root['left'],key)


def delete_min(my_bst):
    my_bst['root'] = delete_min_tree(my_bst['root'])
    return my_bst

def delete_min_tree(root):
    if root is None:
        return root
    elif root['left'] is None:
        return root['right']
    else:
        delete_min_tree(root['left'])
        root['size'] -= 1


def delete_max(my_bst):
    my_bst['root'] = delete_max_tree(my_bst["root"])
    return my_bst
    
def delete_max_tree(root):
    if root is None:
        return root 
    elif root['right'] is None:
        return root["left"]
    else:
        delete_max_tree(root['right'])
        root["size"] -= 1
    
def remove(my_bst,key):
    my_bst['root'] = remove_node(my_bst["root"],key)
    return my_bst


def min_node(root):
    if root["left"] is None:
        return root
    else:
        return min_node(root["left"])


def remove_node(root,key):
    if root is None:
        return root
    
    if root["key"] < key:
        root['left'] = remove_node(root["left"],key)
    elif root["key"] > key:
        root['right'] = remove_node(root['right'],key)
        
    else:
        if root["left"] is None and root['right'] is None:
            root = None
        elif root['left'] is None:
            return root['right']
        elif root['right'] is None:
            return root["left"]
        
        else: 
            sucesor = min_node(root['right'])
            root['key'] = sucesor['key']
            root['value'] = sucesor["value"]
            root['right'] = remove_node(root['right',sucesor['key']])


    return root 

def contains(my_bst,key):
    if get(my_bst,key) is None:
        return False
    else:
        return True

def size(my_bst):
    return size_tree(my_bst['root'])

def size_tree(root):
    if root == None:
        return 0
    else:
        return root['size']

def is_empty(my_bst):
    if my_bst["root"] is None:
        return True
    else:
        return False

    
def key_set(my_bst):
    return postorder_key(my_bst)

def postorder_key(my_order_map):
    node_list = sll.new_list()
    if my_order_map is not None:
        node_list = postorder_tree_key(my_order_map['root'],node_list)
    return node_list

def postorder_tree_key(root,node_list):
    if root == None:
        return node_list
    else:
        postorder_tree_key(root['left'], node_list)
        postorder_tree_key(root['right'], node_list)
        sll.add_last(node_list, root['key'])
    
    return node_list

def value_set(my_bst):
    return postorder_value(my_bst)

def postorder_value(my_order_map):
    node_list = sll.new_list()
    if my_order_map is not None:
        node_list = postorder_tree_value(my_order_map['root'],node_list)
    return node_list

def postorder_tree_value(root,node_list):
    if root == None:
        return node_list
    else:
        postorder_tree_value(root['left'], node_list)
        postorder_tree_value(root['right'], node_list)
        sll.add_last(node_list, root['value'])
    
    return node_list

def get_min(my_bst):
    min = min_key_node(my_bst['root'])
    return min 

def min_key_node(root):
    if root is None:
        return None
    elif root['left'] is None:
        return root['key']
    else:
        return min_key_node(root['left'])

def get_max(my_bst):
    max = max_key_node(my_bst['root'])
    return max

def max_key_node(root):
    if root is None:
        return None
    elif root['right'] is None:
        return root['key']
    else:
        return max_key_node(root['right'])
    
def height(my_bst):
    altura = height_tree(my_bst['root'])
    return altura

def height_tree(root):
    if root is None:
        return 0
    left_height = height_tree(root['left'])
    right_height = height_tree(root['right'])
    return 1 + max(left_height, right_height)

def keys(my_bst, key_inicial, key_final):
    final = sll.new_list()
    keys = keys_range(my_bst['root'],key_inicial,key_final,final)
    return keys

def keys_range(root, key_inicial, key_final, list_key):
    if root == None:
        return list_key
    
    if root['key'] > key_inicial:
        keys_range(root['left'],key_inicial, key_final, list_key)
    
    if key_inicial <= root['key'] <= key_final:
        sll.add_last(list_key, root['key'])
    
    if root['key'] < key_final:
        keys_range(root['right'], key_inicial, key_final, list_key)
    
    return list_key
    

def values(my_bst, key_inicial, key_final):
    final = sll.new_list()
    values = values_range(my_bst['root'], key_inicial, key_final, final)
    return values

def values_range(root,key_inicial, key_final, lista):
    if root == None:
        return lista
    if root["key"] > key_inicial:
        values_range(root['left'], key_inicial, key_final, lista)
    
    if key_inicial <= root['key'] <= key_final:
        sll.add_last(lista, root['value'])
    
    if root['key'] < key_final:
        values_range(root['right'], key_inicial, key_final, lista)
        
    return lista
    




    




    
    
