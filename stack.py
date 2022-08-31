# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 21:35:28 2022

@author: J SRI THRISHNA
"""
#Implementation of stack

class stack():
    def __init__(self):
        self.a=[]
    def push(self,n):
        self.a.append(n)
        for i in self.a[::-1]:
            print(i)
            print("--")
        print("successfully pushed",n)
        
    def pop(self):
        popped_element=self.a.pop()
        for i in self.a[::-1]:
            print(i)
            print("--")
        print("successfully popped",popped_element)
    
s=stack()
m=int(input("enter the number of elements you need to push"))
for _ in range(m):
    n=eval(input("enter your elements"))
    s.push(n)
    
o=int(input("enter number of elements you need to pop"))
if o>len(s.a):
    print("invalid")
    o=int(input("enter the number of elements you need to pop"))
for _ in range(o):
    s.pop()
    
    
#stack using linked list

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class stack():
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.isempty():
            return None
        else:
            popped_node=self.head
            self.head=self.head.next
            popped_node.next=None
            return popped_node.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        internode=self.head
        if self.isempty():
            print("stack underflow")
        else:
            while(internode!=None):
                print(internode.data,"->",end=" ")
                internode=internode.next
            return
s=stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.display()
print("\nTop element in the stack",s.peek())
s.pop()
s.pop()
s.display()
print("\nTop element in the stack",s.peek())          
        
        





