# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 22:52:47 2022

@author: J SRI THRISHNA
"""
#swapping two numbers

class swapping():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def swap(self):
        self.a,self.b = self.b,self.a
        print(self.a)
        print(self.b)
s1=swapping(53,45)
s1.swap()


#circle and circumference
class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        areas=3.14*self.radius*self.radius
        print(areas)
    def circumference(self):
        cir=2*3.14*self.radius
        print(cir)
s1=circle(3)
s1.area()
s1.circumference()

#employee

class Employee:
    def getInfo(self,sala,hours):
        self.sala=sala
        self.hours=hours
    def addSal(self):
        if self.sala<500:
            self.sala+=100
            return self.sala
    def addWorkSal(self):
        if self.hours>6:
           self.hours+=5
           return self.hours
       
hours=int(input())
s1=Employee()
s1.getInfo(100,hours)
print(s1.addSal())
print(s1.addWorkSal())

#pouch -kangaroo
class kangaroo():
    def __init__(self):
        self.pouch_contents=[]
    def put_in_pouch(self,thing):
        self.pouch_contents.append(thing)
    def __str__(self):
        return " I have {} in my pouch".format(self.pouch_contents)
    def __reo__(self):
        return 'kangaroo <{}>'.format(self.pouch.contents)
kanga=kangaroo()
roo=kangaroo()
kanga.put_in_pouch(5)   
kanga.put_in_pouch(8)   
kanga.put_in_pouch(9)   

roo.put_in_pouch("kkk")
print(kanga)
print(roo)

#elements,row in matrix

class Matrix():
    def __init__(self):
        self.r=[]
        self.c=[]
        self.mat=[]
    def num_r(self,r):
        self.r.append(r)
        self.row=str(self.r)[1:-1]
        self.row=int(self.row)
        print("Number of rows",self.row)
    def num_c(self,c):
        self.c.append(c)
        self.col=str(self.c)[1:-1]
        self.col=int(self.col)
        print("Number of columns",self.col)
    def matrix(self):
        print("enter the enteries")
        for i in range(self.row):
            a=[]
            for j in range(self.col):
                a.append(int(input()))
            self.mat.append(a)
    def show(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.mat[i][j],end=" ")
            print()
            
r=int(input("Enter the rows "))
c=int(input("Enter number of columns"))
s1=Matrix()
s1.num_r(r)
s1.num_c(c)
s1.matrix()
s1.show()          

#engine number
          
class numberplate():
    def __init__(self,x):
        self.x=x
    def Number(self):
        
        y=list(self.x)
        z=sorted(y)
        k=[]
        for i in z:
            try:
                k.append(int(i))
            except:
                pass
        return k
s1=numberplate("PY 02 1234")
print("Engine Number",sum(s1.Number()))

#worker bee

class WorkerBee():
    def __init__(self,container):
        self.container=container
    def report(self):
       return {k:v for k,v in sorted(self.container.items(),key=lambda item:item[1])}
   
container=eval(input("Enter the container:"))
a1=WorkerBee(container)
print(a1.report())

#valid parenthesis

class valid_parenthesis():
    def is_valid(self,string):
        for i in range(0,len(string),2):
            if len(string)%2 !=0:
                return False
            if string[i]=="(" and string[i+1]!=")":
                return False
            if string[i]=="[" and string[i+1]!="]":
                return False
            if string[i]=="{" and string[i+1]!="}":
                return False
        return True
    
string=eval(input())
s1=valid_parenthesis()
print(s1.is_valid(string))

#unique elements in diction

class unique:
    def display(self,lis):
        uni=[]
        for i in range(len(lis)):
            for j in lis[i].values():
                if j not in uni:
                    uni.append(j)
        print(uni)

s=unique()
s.display([{"sanjay":23},{"thrishna":10}])

#bubble sort
a=eval(input())
n=len(a)
for i in range(n):
    for j in range(n-1-i):
        if a[j]>a[j+1]:
            n1=a[j]
            n2=a[j+1]
            a[j+1]=n1
            a[j]=n2
        print(a)

#selection sort

a=eval(input())
sort=[]
for i in range(len(a)):
    min=a[0]
    for j in range(len(a)):
        if a[j]<min:
            min=a[j]
    a.pop(a.index(min))
    sort.append(min)
    print(sort)            
            
#insertion sort

a=eval(input())
sort=[]
sort.append(a[0])
for i in range(1,len(a)):
    sort.append(a[i])
    for j in range(len(sort)-1,0,-1):
        if sort[j]<sort[j-1]:
            n1=sort[j]
            n2=sort[j-1]
            sort[j]=n2
            sort[j-1]=n1
print(sort)


#quick sort

a=eval(input())
print(a)
def partition(arr,low,high):
    i=-1
    pivot=arr[high]
    for j in range(len(a)):
        if (arr[j]<pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        if (arr[j]==pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    return i

def quicksort(arr,low,high):
    if low<high:
        m=partition(arr,low,high)
        quicksort(arr,low,m-1)
        quicksort(arr,m+1,high)
    return arr

low=0
high=len(a)-1

print(quicksort(a,low,high))


#merge sort

def merge(arr,l,m,r):
    n1=m-l+1
    n2=r-m
    
    L=[0]*(n1)
    R=[0]*(n2)
    
    for i in range(0,n1):
        L[i]=arr[l+i]
    for j in range(0,n2):
        R[j]=arr[m+1+j]

    i=0
    j=0
    k=l
    
    while i<n1 and j<n2:
        if L[i]<=R[i]:
            arr[k]=L[i]
            i+=1
        else:
            arr[k]=R[j]
            j+=1
        k+=1
        
    while i<n1:
        arr[k]=L[i]
        i+=1
        k+=1
    while j < n2:
        
        arr[k] = R[j]
        j+=1
        k+=1
        
def merger(arr,l,r):
    if l < r:
        m=(l+(r-1))//2
        merger(arr,l,m)
        merger(arr,m+1,r)
        merge(arr,l,m,r)
            
arr=[23,12,32,33,44,46]
n=len(arr)
print("Given array is")
for i in range(n):
    print("%d" % arr[i],end=" ")
print("\n\nSorted array is")   
merger(arr,0,n-1)

for i in range(n):
    print("%d" % arr[i],end=" ")   
















            
                