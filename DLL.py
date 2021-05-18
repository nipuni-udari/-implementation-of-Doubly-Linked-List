'''
AF/18/14804
AR/96770
Weeraman N.U.R.
implementation of Doubly Linked List:'''


class Node:                                  #create a class for the single node in the list
    def __init__(self, data):
        self.item = data                     # store data
        self.nref = None                     # store reference (next item)
        self.pref = None                     # store reference (previous item)



class DoublyLinkedList:                     #create the DoublyLinkedList class
    def __init__(self):
        self.start_node = None

    def insert_in_emptylist(self, data):    #Inserting Items in Empty List
        if self.start_node is None:         #checks whether the self.start_node variable is None
            new_node = Node(data)           #list is actually empty. Next, a new node is created and its value is initialized by the value passed as a parameter to the data parameter
            self.start_node = new_node      #variable is set to the new node
        else:
            print("list is not empty")      #if the list is not empty, a message is simply displayed to the user that the list is not empty

    # Inserting Items at the start
    def insert_at_start(self, data):
        if self.start_node is None:         #whether the list is empty or not.
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node     # the new node, the reference to the next node will be set
        self.start_node.pref = new_node     # the reference to the previous node will be set to the newly inserted node.
        self.start_node = new_node          # will become the newly inserted node.

    # Inserting Items at the End
    def insert_at_end(self, data):
        if self.start_node is None:         #check if the list is empty
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:           #If the list already contains some element,
            n = n.nref                      #we traverse through the list until the reference to the next node becomes None
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    #Inserting Items after an another item
    def insert_after_item(self, x, data):       #check whether or not the list is empty
        if self.start_node is None:             #f the list is actually empty,
            print("List is empty")              # we simply display the message that the "list is empty"
            return
        else:
            n = self.start_node                 #if the node after which we want to insert the new node is not found, we display the message to the user that the item is not found. Else if the node is found,
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n               #Set the previous reference of the newly inserted node to the selected node
                new_node.nref = n.nref          #Set the next reference of the newly inserted node to the next reference of the selected
                if n.nref is not None:          #If the selected node is not the last node,
                    n.nref.prev = new_node      #set the previous reference of the next node after the selected node to the newly added node.
                n.nref = new_node               #set the next reference of the selected node to the newly inserted node

    # Inserting Items before an another item
    def insert_before_item(self, x, data):
        if self.start_node is None:             # first check whether or not the list is empty
            print("List is empty")              #If the list is actually empty, we simply display the message that the "list is empty".
            return
        else:
            n = self.start_node                #if the node before which we want to insert the new node is not found, we display the message to the user that the item is not found.
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = n               #Set the next reference of the newly inserted node to the selected node.
                new_node.pref = n.pref          #Set the previous reference of the newly inserted node to the previous reference of the selected.
                if n.pref is not None:
                    n.pref.nref = new_node      #set the next reference of the node previous to the selected node, to the newly added node
                n.pref = new_node               #set the previous reference of the selected node to the newly inserted node.

    # Traversing forward
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.nref

    # deleting Items at the start
    def delete_at_start(self):
        if self.start_node is None:                 # set the value of the start node to the next node
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None                  # If the list contains elements then we can simply set the start node to None
            return
        self.start_node = self.start_node.nref      #set the value of the start node to the next node
        self.start_pref = None                      #then set the previous reference of the start node to None

    # deleting Items at the end
    def delete_at_end(self):
        if self.start_node is None:                 #if the list is empty or if the list contains a single element. If the list contains a single element
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:            #If the list contains a single element
            self.start_node = None                  #set the start node to None
            return
        n = self.start_node
        while n.nref is not None:                   #If the list has more than one element, iterate through the list until the last node is reached
            n = n.nref
        n.pref.nref = None                          #set the next reference of the node previous to the last node

    # deleting Items at given position
    def delete_element_by_value(self, x):           #we check if the list is empty or not.
        if self.start_node is None:
            print("The list has no element to delete")  #If the list is empty display the user that the list is empty.
            return
        if self.start_node.nref is None:            # If the only element is the one that we want to delete,set node to none
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found")             #If there is only one item and that is not the item that we want to delete, display this message
            return

        if self.start_node.item == x:               #deletes an element from the start in case of multiple items
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return

        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref                    #Set the value of the next reference of the previous node to the next reference of the node to be deleted.
            n.nref.pref = n.pref                    #Set the previous value of the next node to the previous reference of the node to be deleted.
        else:
            if n.item == x:
                n.pref.nref = None                  #the next reference of the node previous to the last node is set to None
            else:
                print("Element not found")


    # Reversing through the list
    def reverse_linked_list(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        p = self.start_node
        q = p.nref
        p.nref = None                                #The next reference of the start node should be set none
        p.pref = q
        while q is not None:
            q.pref = q.nref
            q.nref = p
            p = q
            q = q.pref
        self.start_node = p




linked_list = DoublyLinkedList()                    #create the object of the DoublyLinkedList class
linked_list.insert_in_emptylist(40)                 #add an element in the empty list

print("The first adding item of the list is:")
linked_list.traverse_list()

#Insert Function
linked_list.insert_at_start(30)
linked_list.insert_at_start(20)
linked_list.insert_at_start(10)

linked_list.insert_at_end(50)
linked_list.insert_at_end(80)
linked_list.insert_at_end(90)

linked_list.insert_before_item(80,60)
linked_list.insert_after_item(60,70)

print("Traversing forward via the linked list is :")
linked_list.traverse_list()

#Reverse Function
linked_list.reverse_linked_list()

print("Traversing backward via the linked list is :")
linked_list.traverse_list()

#Delete Function
linked_list.delete_at_start()
linked_list.delete_at_end()
linked_list.delete_element_by_value(50)

print("After deleting, the linked list is :")
linked_list.traverse_list()







