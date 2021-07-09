from .ds import LinkedListNode


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    @staticmethod
    def __get_node(data: int):
        new_node = LinkedListNode()
        new_node.data = data
        return new_node

    def insert_data(self, data: int):
        new_node = self.__get_node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next_node = new_node
            new_node.prv_node = self.tail
            self.tail = new_node

    def extend(self, data: list):
        for i in data:
            self.insert_data(i)

    @property
    def as_list(self):
        data_list = []
        temp = self.head
        while temp is not None:
            data_list.append(temp.data)
            temp = temp.next_node
        return data_list

    def exists(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next_node

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next_node


if __name__ == '__main__':
    l = DoublyLinkedList()
    l.insert_data(23)
    l.insert_data(24)
    l.insert_data(25)
    l.insert_data(26)

    l.display()
