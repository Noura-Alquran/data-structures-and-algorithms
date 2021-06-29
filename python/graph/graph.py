from collections import deque

class EmptyStackException(Exception):
    pass
class Vertex():
  def __init__(self,key=None):
    self.key = key
  
  def __str__(self):
    return str(self.key)

class Queue():
  def __init__(self):
    self.dq =deque()
  
  def enqueue(self,value):
    self.dq.appendleft(value)

  def dequeue(self):
    return self.dq.pop()
  
  def __len__ (self):
    return len(self.dq)


class Stack():
  def __init__(self,top = None):
    self.top =top

  def push(self,value):
    new_Node=Vertex(value)
    new_Node.next=self.top
    self.top = new_Node
  
  def pop(self):
    if not self.isEmpty():
      temp = self.top
      self.top = self.top.next
      temp.next =None
      return temp.key
    raise EmptyStackException("stack is empty")
 
  
  def peek(self):
    if not self.isEmpty():
      return self.top.key
    raise EmptyStackException("stack is empty")


  def isEmpty(self):
    if self.top:
      return False
    return True

  def __str__(self):
    top = self.top
    items = []
    while top:
      items.append(str(top.value))
      top = top.next
    return " ".join(items)


class Graph():
  def __init__(self):
    self._adjacency_list = {}
    

  def add_node(self ,value):
    new_v = Vertex(value)
    new_v=str(new_v)
    self._adjacency_list[new_v] = []
    return new_v
    

  def add_edge(self , start_vertex ,end_vertex ,weight =0):
    if start_vertex not in self._adjacency_list:
      raise KeyError('Start vertex is not found in the graph')
    if end_vertex not in self._adjacency_list:
      raise KeyError('end vertex is not found in the graph') 
    self._adjacency_list[start_vertex].append((str(end_vertex),weight))  

  def get_nodes(self):
    return self._adjacency_list.keys()
    
  
  def neighbors(self , vertex):
    return self._adjacency_list[vertex]
  
  def size(self):
    return len(self._adjacency_list)
  
   
  def breath_first_search(self ,start_vertex):
    list=[]
    queue = Queue()
    visited = set()

    queue .enqueue(start_vertex)
    visited.add(start_vertex)
    
    while len(queue):
      current_vertex = queue.dequeue()
      list.append(current_vertex)
      for child in self._adjacency_list[current_vertex]:
        if child[0] not in visited:
          child=child[0]
          visited.add(child)
          queue.enqueue(child)
    return list


  def business_trip (self,cities:list):
    sum=0
    flag =False
    for i in range(len(cities)-1):
        neighbors=self._adjacency_list[cities[i]]
        print (neighbors)
        for neighbor in neighbors:
          if cities[i+1] == neighbor[0]:
            sum += neighbor[1]
            flag=True
            break
          else:
            sum+= 0
            flag=False
    if not flag :
      return False ,'$0'  
        
    return True,'$'+ str(sum)

    
  def print_graph(self):
    print(self._adjacency_list)

  def depth_first(self, start_vertex =None):
    vertexes = []
    visited =[]
    stack = Stack()

    if start_vertex not in self._adjacency_list:
      raise KeyError('Start vertex is not found in the graph')

    stack.push(start_vertex)

    while not stack.isEmpty():

      vertex = stack.pop()
      vertexes.append(vertex)
      vertex_neighbors = self.neighbors(vertex)

      for neighbor in vertex_neighbors:
        if neighbor[0] not in visited :
          stack.push(neighbor[0])
          visited.append(neighbor[0])

    return vertexes    


if __name__ == "__main__":
  gr = Graph()
  v1= gr.add_node('A')
  v2 =gr.add_node('B')
  v3=gr.add_node('C')
  v4=gr.add_node('D')
  v5=gr.add_node('E')
  gr.add_edge(v1,v2,1)
  gr.add_edge(v1,v3,2)
  gr.add_edge(v2,v4,4)
  gr.add_edge(v3,v4,8)
  gr.add_edge(v3,v5,3)
  gr.add_edge(v4,v5,5)
  assert gr.size() == 5
  print(gr.get_nodes())
  print(gr.neighbors(v1))
  print(gr.neighbors(v2))
  print(gr.neighbors(v3))
  print(gr.neighbors(v4))
  print(gr.neighbors(v5))
  gr.print_graph()
