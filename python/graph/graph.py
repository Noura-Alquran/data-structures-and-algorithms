class Vertex():
  def __init__(self,key):
    self.key = key
  
  def __str__(self):
    return str(self.key)



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
  
  def print_graph(self):
    print(self._adjacency_list)



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
