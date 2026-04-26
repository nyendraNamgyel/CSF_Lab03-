class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, data):
        temp = self.head

        if temp and temp.data == data:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    def search(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return "Element found"
            temp = temp.next
        return "Element not found"

    def display(self):
        temp = self.head
        result = ""
        while temp:
            result += str(temp.data) + " -> "
            temp = temp.next
        result += "None"
        return result


# Demo
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

print("Linked List:", ll.display())

ll.insert_at_beginning(5)
print("After inserting 5 at beginning:", ll.display())

ll.delete_node(20)
print("After deleting 20:", ll.display())

print("Search 30:", ll.search(30))