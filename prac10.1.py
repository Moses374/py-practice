class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtTheBeginning(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    def printLinkedList(self):
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
        print()

    def insertAtTheEnd(self,new_data):
        new_node=Node(new_data)

        if self.head is None:
            self.head=new_node
            return None
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node

if __name__ =="__main__":
    llist=LinkedList()
    llist.insertAtTheBeginning("Fox")
    llist.insertAtTheBeginning("Brown")
    llist.insertAtTheBeginning("Quick")
    llist.insertAtTheBeginning("The")

    llist.printLinkedList()
    llist.insertAtTheEnd("Jumps")
    llist.printLinkedList()