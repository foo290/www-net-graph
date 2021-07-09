class Vertex:
    def __init__(self):
        self.data = None
        self.title = None
        self.connections = None

    def __str__(self):
        return f"Node : {self.data}"

    def __repr__(self):
        return f"Node : {self.data}"

    def __eq__(self, other):
        return self.data == other.data


class LinkedListNode:
    def __init__(self):
        self.data = None
        self.weight = None
        self.next_node = None
        self.prv_node = None


if __name__ == '__main__':
    n1 = Vertex()
    n1.data = 'hhh'

    n2 = Vertex()
    n2.data = 'hhh'

    print(n1 == n2)
    print(n1)
