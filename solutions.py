'''
Question 1
Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and
t = "ad", then the function returns True. Your function definition should look like: question1(s, t) and return a
boolean True or False.
'''


def question1(s, t):
    index_array = []
    for t_letter in t:
        index_found = False
        for index, s_letter in enumerate(s):
            if s_letter == t_letter and index not in index_array:
                index_array.append(index)
                index_found = True
                break
        if index_found == False:
            return False
    if len(index_array) != len(t):
        return False
    else:
        return True


print(question1('udacity', 'da'))
# True

print(question1('supercalifragilisticexpialidocious', 'zoo'))
# False

print(question1('supercalifragilisticexpialidocious', 'capital'))
# True

print(question1('supercalifragilisticexpialidocious', 'slfxcu'))
# True

print(question1('supercalifragilisticexpialidocious', 'supercali_docious'))
# False

print(question1('computerscience', 'epic'))
# True


'''
Question 2
Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), 
and return a string.
'''


def question2(a):
    a = a.lower()
    for substg_size in range(len(a), 0, -1):
        for starting_index in range(0, len(a) - substg_size + 1):
            substring = a[starting_index:starting_index + substg_size]
            a_index = 0
            b_index = len(substring) - 1
            is_palendrome = False
            while a_index <= b_index:
                if substring[a_index] == substring[b_index]:
                    a_index = a_index + 1
                    b_index = b_index - 1
                    is_palendrome = True
                else:
                    is_palendrome = False
                    break
            if is_palendrome == True:
                return substring


print(question2('udacity'))
# u

print(question2('racecar'))
# racecar

print(question2('Annapolis'))
# anna

print(question2('1234567890123456_racecar_abcdefghijk'))
# _racecar_

'''
Question 3
Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a 
graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list 
structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
 
Vertices are represented as unique strings. The function definition should be question3(G)
'''

def question3(G):
    connections = []
    for node1, vertices in G.items():
        for vertex in vertices:
            node2 = vertex[0]
            weight = vertex[1]
            if (node2, node1, weight) not in connections:
                connections.append((node1,node2,weight))
    connections = sorted(connections, key=lambda x: x[2])
    stack = [connections[0][0], connections[0][1]]
    minimal_spanning_connections = [connections[0]]
    while len(minimal_spanning_connections) < len(G.keys())-1:
        connection_found = False
        counter = 1
        while connection_found is False:
            if not (connections[counter][0] in stack) == (connections[counter][1] in stack):
                minimal_spanning_connections.append(connections[counter])
                connection_found = True
                if connections[counter][0] not in stack:
                    stack.append(connections[counter][0])
                else:
                    stack.append(connections[counter][1])
            counter = counter + 1
    MST = {}
    for node in G.keys():
        MST[node] = []
    for connection in minimal_spanning_connections:
        MST[connection[0]].append((connection[1], connection[2]))
        MST[connection[1]].append((connection[0], connection[2]))
    for node in MST.keys():
        MST[node] = connections = sorted(MST[node], key=lambda x: x[0])
    return MST


G = {'A': [('B', 2), ('D', 1)],
     'B': [('A', 2), ('C', 5), ('D', 2)],
     'C': [('B', 5), ('E', 2)],
     'D': [('A', 1), ('B', 2)],
     'E': [('C', 2)]}
print(question3(G))
'''
{'A': [('B', 2), ('D', 1)], 
'B': [('A', 2), ('C', 5)], 
'C': [('B', 5), ('E', 2)], 
'D': [('A', 1)], 
'E': [('C', 2)]}
'''

H = {'A': [('B', 2), ('C', 4), ('D', 1), ('E', 3), ('F', 5)],
     'B': [('A', 2), ('C', 1), ('D', 2), ('E', 1), ('F', 3)],
     'C': [('A', 4), ('B', 1), ('D', 4), ('E', 1), ('G', 3)],
     'D': [('A', 1), ('B', 2), ('C', 4), ('E', 2), ('F', 3)],
     'E': [('A', 3), ('B', 1), ('C', 1), ('D', 2), ('F', 4)],
     'F': [('A', 5), ('B', 3), ('D', 3), ('E', 4), ('G', 2)],
     'G': [('F', 2)]}
print(question3(H))
'''
{'A': [('B', 2), ('D', 1)], 
'B': [('A', 2), ('C', 1), ('E', 1), ('F', 3)], 
'C': [('B', 1)], 
'D': [('A', 1)], 
'E': [('B', 1)], 
'F': [('B', 3), ('G', 2)], 
'G': [('F', 2)]}
'''

J = {'A': [('B', 2)],
    'B': [('A', 2), ('C', 5)],
    'C': [('B', 5)]}
print(question3(J))
'''
{'A': [('B', 2)],
'B': [('A', 2), ('C', 5)],
'C': [('B', 5)]}
'''

'''
Question 4
Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest node 
from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the tree, 
but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor. 
You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition should 
look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is equal to the integer 
stored in that node and a 1 represents a child node, r is a non-negative integer representing the root, and n1 and n2 are non-negative
 integers representing the two nodes in no particular order. For example, one test case might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.
'''

def question4(T, r, n1, n2):
    cur_node = T[r]
    node1 = min((n1, n2))
    node2 = max((n1, n2))
    cur_node_left = -1
    cur_node_right = len(cur_node)
    for index, child in enumerate(cur_node):
        if child == 1 and index < r:
            cur_node_left = index
        if child == 1 and index > r:
            cur_node_right = index
    if node1 < node2 < r:
        return question4(T, cur_node_left, node1, node2)
    elif r < node1 < node2:
        return question4(T, cur_node_right, node1, node2)
    else:
        return r



print(question4([[0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                3,
                1,
                4))
# 3


BST = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(question4(BST, 5, 1, 4))
# 3
print(question4(BST, 5, 0, 9))
# 5
print(question4(BST, 5, 6, 9))
# 7
print(question4(BST, 5, 8, 9))
# 8

'''
Question 5
Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements, 
the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll 
is the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use 
as a representation of a node in the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None    
'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def addNode(self, data):
        if self.next == None:
            self.next = Node(data)
        else:
            self.next.addNode(data)

    def printList(self):
        print(self.data)
        if self.next != None:
            self.next.printList()

def question5(node, reverse_index):
    list_size = 1
    cur_node = node
    while cur_node.next != None:
        list_size = list_size+1
        cur_node = cur_node.next
    index = list_size - reverse_index
    cur_node = node
    for i in range(0,index):
        cur_node = cur_node.next
    return cur_node.data

node =  Node(1)
node.addNode(2)
node.addNode(3)
node.addNode("A")
node.addNode("B")
node.addNode("C")
node.addNode(4)
node.addNode("D")
node.addNode(5)
node.addNode("LAST NODE")

print(question5(node,2))
# 5
print(question5(node,5))
# C
print(question5(node,1))
# LAST NODE
print(question5(node,100))
# 1