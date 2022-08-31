# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 22:10:22 2022

@author: J SRI THRISHNA
"""
#implementation of queue

class queue:
    def __init__(self):
        self.a=[]
    def enqueue(self,n):
        self.a.append(n)
        for i in self.a:
            print(i)
            print("--")
        print("successfully inserted",n)
    def dequeue(self):
        popele=self.a.pop(0)
        for i in self.a:
            print(i)
            print("--")
        print("successfully popped",popele)
q=queue()
m=int(input("enter number of element you need to push"))
for _ in range(m):
    n=eval(input("enter your element"))
    q.enqueue(n)
o=int(input("enter number of element you need to pop"))
if (o>len(q.a)):
    print("invalid")
    o=int(input("enter number of element you need to pop"))
for _ in range(o):
    print(q.dequeue())
    
#queue using linked list
class Node():
    def __init__(self,data):
        self.data=data
        self.head=None
class queue():
    def __init__(self):
        self.front=self.rare=None
    def isempty(self):
        return self.front==None
    def enqueue(self,item):
        temp=Node(item)
        if self.rare==None:
            self.front=self.rare=temp
            return
        self.rare.next=temp
        self.rare=temp
    def dequeue(self):
        if self.isempty():
            return
        temp=self.front
        self.front=temp.next
        if(self.front==None):
            self.rare=None
q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()
q.dequeue()
print(str(q.front.data))
print(str(q.rare.data))