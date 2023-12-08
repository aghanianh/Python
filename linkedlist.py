class Node:
    def __init__(self, data, prev=None, nxt=None):
        self._data = data
        self._next = nxt
        self._prev = prev


class LinkedList:
    def __init__(self):
        self._tail = None
        self._head = None

    def is_empty(self) -> bool:
        return self._head is None

    def prepend(self, data) -> None:
        if self.is_empty():
            self._head = self._tail = Node(data)
            return
        tmp = Node(data)
        tmp._next = self._head
        self._head._prev = tmp
        self._head = tmp

    def append(self, data) -> None:
        if self.is_empty():
            self._head = self._tail = Node(data)
            return

        tmp = Node(data)
        tmp._prev = self._tail
        self._tail._next = tmp
        self._tail = tmp

    def insert_after(self, target_data, data) -> None:
        if self.is_empty():
            raise TypeError("Empty List")
        curr = self._head
        while curr._next is not None and curr._next._data != target_data:
            curr = curr._next
        if curr._next is None:
            raise TypeError("No such element in List")

        added_node = Node(data)
        added_node._prev = curr
        added_node._next = curr._next if curr._next else None
        curr._next = added_node

    def insert_before(self, target_data, data):
        if self.is_empty():
            raise TypeError("Empty List")
        curr = self._head
        eflag = False

        while curr is not None:
            if curr._data == target_data:
                eflag = True
                break
            curr = curr._next
        if not eflag:
            raise TypeError("No such element")
        tmp = Node(data)
        tmp._next = curr
        tmp._prev = curr._prev
        if curr._prev:
            curr._prev._next = tmp

        if curr == self._head:
            self._head = tmp

    def delete(self, data):
        if self.is_empty():
            raise TypeError("Empty List")

        curr = self._head
        while curr._next is not None and curr._next._data != data:
            curr = curr._next

        if curr._next is None:
            raise TypeError("No such element for deleting")

        tmp = curr._next
        curr._next = tmp._next

        if tmp._next:
            tmp._next._prev = curr

        del tmp

    def display(self):
        tmp = self._head
        print("None <-", end = " ")
        while tmp is not None:
            print(f"{tmp._data} <->", end=" ")
            tmp = tmp._next
        print("None")


if __name__ == "__main__":
    ls = LinkedList()
    ls.prepend(5)
    ls.display()
    ls.prepend(6)
    ls.display()
    ls.append('Aghanyan')
    ls.display()
    ls.append('Varuzhan')
    ls.display()
    ls.insert_after('Varuzhan', 'EEE')
    ls.display()
    ls.insert_before('Aghanyan', 'FFF')
    ls.display()
    ls.delete(5)
    ls.display()

