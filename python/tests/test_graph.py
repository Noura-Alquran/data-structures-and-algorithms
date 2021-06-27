from graph.graph import Graph
import pytest

def test_add_node_successfully():
  gr = Graph()
  gr.add_node('A')
  expected = 1
  actual = gr.size()
  assert  actual == expected

def test_add_edge_successfully():
  gr = Graph()
  v1 = gr.add_node('A')
  v2  =gr.add_node('B')
  gr.add_edge(v1,v2,1)
  assert gr._adjacency_list[v1] == [(v2 , 1)]


def test_get_all_nodes_and_check_the_size():
  gr = Graph()
  v1= gr.add_node('A')
  v2 =gr.add_node('B')
  v3=gr.add_node('C')
  v4=gr.add_node('D')
  v5=gr.add_node('E')
  assert gr.size() == 5

def test_get_neighbor_and_with_weights():
  gr = Graph()
  v1= gr.add_node('A')
  v2 =gr.add_node('B')
  v3=gr.add_node('C')
  gr.add_edge(v1,v2,1)
  gr.add_edge(v1,v3,2)
  assert gr.neighbors(v1) == [('B', 1), ('C', 2)]


def test_graph_with_one_node_and_edge():
  gr=Graph()
  v1 = gr.add_node('A')
  with pytest.raises(KeyError):
    gr.add_edge(v1,None)

def test_empty_graph():
  gr = Graph()
  assert gr.print_graph()== None
  print('pass')


def test_BFS_graph():
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
  gr.add_edge(v2,v1,10)
  gr.add_edge(v3,v1,7)
  gr.add_edge(v4,v3,8)
  gr.add_edge(v5,v3,7)
  assert gr.breath_first_search(v1) == ['A','B','C','D','E']