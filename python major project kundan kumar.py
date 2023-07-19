#!/usr/bin/env python
# coding: utf-8

# In[113]:


#Q1. Find the datatype of these two declaration :
x = 5
y = "john"

print(x)
print(y)
 
    


# In[115]:


#Q2. Check whether the following syntax is valid or invalid for naminga variable.




abc = 100;


# In[14]:


3a = 10;


# In[15]:


@abc = 10;


# In[16]:


a100 = 100;


# In[18]:


_a984_ = 100;


# In[20]:


a9967$ = 100;


# In[24]:


xyz-2 = 100;


# In[108]:


#Q3Check if element exists in list in Python :
#Check if 3 exist or not.
list= test_list = [1,6,3,5,3,4]
print(test_list),
for i in list:
    print(list)
    print(list.count(3))
    
    #. Check if 9 exists or not.
    print(test_list.count(9))


# In[110]:


#Q4.Take the user input to print the current date.

import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
date = now.strftime("%Y-%m-%d")


# In[111]:


#Q5.what is the output of the following code :

#a. print 9//2

x, y = 9 , 2
print(x // y)

#b. print 9%2

print(x % y)


# In[112]:


#Q6.Print First 10 natural numbers using a while loop

i=1
while i<=10:
    print(i)
    i+=1
        
       
    


# In[12]:


#7. Write a program to accept a number from a user and calculate


x=1,2,3,4,5,6,7,8,9,10
print(sum(x))

n = int(input("Enter a number:"))
s = 0
for i in range(n+1):
    s+=i
    print("sum of all number from 1 to given number:",s)



# In[13]:


#Q8 Write a Python program which iterates the integers from 1 to 50.
#For multiples of three print "Fizz" instead of the number and for
#the multiples of five print "Buzz". For numbers which are
#multiples of both three and five print "FizzBuzz.


for i in range(1,51):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    
    elif(i%3 == 0):
        print("Fizz")
    
    
    elif(i%5 ==0):
        print("Buzz")
    
    else:
        print(i)
    
 
    



# In[ ]:




