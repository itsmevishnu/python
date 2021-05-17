class LinkedList:
    def __init__(self):
        self.head = None # intially head is null

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

class Node:
    def __init__(self, data):
        self.data = data # the initial data
        self.next = None # intially the next data is null

#initialise a linkedlist
list = LinkedList()
#first node
first = Node(1)
second = Node(2)
third = Node(3)



list.head = first #assigning head to first node
# list.head.next = second
first.next = second
second.next = third
third.next = None # the last value to null

#print linkedlist
list.printList()