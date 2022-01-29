class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append_it(self, data):
        new = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new

    def print_it(self):
        if self.head.next == None:
            print('This list is empty.')
            return
        stringy = ''
        cur = self.head
        while cur.next != None:
            cur = cur.next
            stringy += str(cur.data) + '-->'
        print(stringy)
        return

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            cur = cur.next
            total +=1
        return total

    def get_it(self, index):
        if index >= self.length():
            print('This index is out of range.')
            return
        cur = self.head
        cur_idx = 0
        while cur.next != None:
            cur = cur.next
            cur_idx += 1
            if cur_idx == index:
                print(cur.data)
                return
        
    def remove_it(self, index):
        if index >= self.length():
            print('This index is out of range.')
            return
        cur = self.head
        cur_idx = 0
        while cur.next != None:
            previous = cur
            cur = cur.next
            cur_idx += 1
            if cur_idx == index:
                previous.next = cur.next
        return

                


ll = LinkedList()
ll.append_it(7)
ll.append_it(8)
ll.append_it(9)
ll.append_it(10)
ll.append_it(11)
ll.print_it()
ll.remove_it(3)
ll.print_it()
        


