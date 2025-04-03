class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None
        self.length=0

    def isEmpty(self):
        return self.head==None
    
    def addNode(self,node):
        if self.isEmpty():
            self.head=Node
        elif self.head.next is None:
            self.head.next=node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
                current.next=node
        self.length+=1
    
    def addNodeAfter(self,node,x):
        if self.isEmpty():
            self.head=Node
        else:
            current=self.head
            while current.next is not None:
                if current.data==x:
                    node.next=current.next
                    current.next=node
                    self.length+=1
                    return
                current=current.next
            print("Node not found")
    
    def reverse(self):
        if self.isEmpty():
            return "Linked List is empty"
        elif self.head.next is None:
            return self.head
        else:
            current=self.head
            prev= None
            while current is not None:
                next =current.next#stores next node
                current.next=prev #reverse the links
                prev=current#sets the current node as previous node
                current=next #sets the next node as current node
            self.head=prev
            return self.head
        
    def deleteNode(self,x):
        if self.isEmpty():
            return "Linked List is empty"
        elif self.head.data==x:
            self.head=self.head.next
        else:
            current=self.head
            while current.next is not None:
                if current.next.data==x:
                    current.next=current.next.next
                    self.length-=1
                    return "Node deleted"
                current=current.next
            return "Node not found"
        
    def printList(self):
        if self.isEmpty():
            print("Linked List is empty")
        else:
            current=self.head
            while current is not None:
                print(current.data,end=" ")
                current=current.next
    
    def search(self,x):
        if self.isEmpty():
            return "Linked List is empty"
        else:
            current=self.head
            while current is not None:
                if current.data==x:
                    return current.data
                current=current.next
            return "Node not found"
        
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None

    def isEmpty(self):
        return self.head==None and self.tail==None
    
    def enqueue(self,node):
        if self.isEmpty():
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        elif self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next

    def printQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            current=self.head
            while current is not None:
                print(current.data,end=" ")
                current=current.next

class Stack:
    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head==None
    
    def push(self,node):
        if self.isEmpty():
            self.head=node
        else:
            node.next=self.head
            self.head=node

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            self.head=self.head.next