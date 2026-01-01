class node:#class which reperesent the node in singliy linked list
     def __init__(self,data):
          self.data=data
          self.next=None 

class singlylinkedlist:#implement all the operation on singliy linked list 
     def __init__(self):
          self.head=None

     #this function adda the node at the begining 
     #this needs to handele to scenaries 
     #1)when list is empty 
     #2)list  has some elements 
     def insertatbegining(self,data):
          #create a  new node 
          newnode=node(data)
          #case 1 if the list is empty make the new node as head 
          if(self.head==None):
               self.head=newnode
               return

          # case 2 if the list is not empty make the newnode is as head and head to newnode 
          else:
               newnode.next=self.head
               self.head=newnode
               return 


list=singlylinkedlist()
list.insertatbegining(10)
list.insertatbegining(20)
list.insertatbegining(30)
print("list is created succefully ")
print("head node data id",list.head.data)
print("head node data id",list.head.data)
print("head node data id",list.head.next.next.data)
