from data_structure.linked_lists import DoublyLinkedList
from data_structure.ds import Vertex


class Graph:
    def __init__(self):
        self._vertices = []

    def add_nodes(self, nodes: list):
        for i, data in enumerate(set(nodes)):
            new_node = Vertex()
            new_node.data = data
            new_node.connections = DoublyLinkedList()

            self._vertices.append(new_node)

    def add_edges(self, edges: list):
        v_list = [v.data for v in self._vertices]
        for edge in edges:
            start, end = v_list.index(edge[0]), v_list.index(edge[1])
            self._vertices[start].connections.insert_data(end)

    def get_node_by_index(self, ind: int):
        return self._vertices[ind]

    def is_connected(self, index1: int, index2: int) -> bool:
        return self._vertices[index1].connections.exists(index2)

    def is_connected_by_data(self, node1_data: str, node2_data: str) -> bool:
        v_list = [v.data for v in self._vertices]
        ind1, ind2 = v_list.index(node1_data), v_list.index(node2_data)
        return self._vertices[ind1].connections.exists(ind2)

    def draw(self):
        for node in self._vertices:
            print(f'{node}\nconnected to {[self._vertices[i] for i in node.connections.as_list]}')
            print()

    @property
    def get_all_edges(self):
        temp = []
        for node in self._vertices:
            for each in node.connections.as_list:
                temp.append((node.data, self._vertices[each].data))
        return temp

    @property
    def get_all_nodes(self):
        return [v.data for v in self._vertices]
