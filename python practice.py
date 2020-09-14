#!/usr/bin/env python
# coding: utf-8

# In[1]:


p = int(input("\n Enter the principal Amount:"))
t = int(input("\n Enter the time period:"))
r = float(input("\n Enter the rate of interest:"))
si = p*t*r/100
print("\n Simple Interest:",si)


# In[2]:


print('''This sentence is output to the screen''')
a=5
print("The value of a is:",a)
print('x:',1,2,3,4)
x = 5 ; y = 10
print('The value of x is {} and y is {}'.format(x,y))
print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))


# In[3]:


print('Hello {name}, {greeting}'.format(greeting = 'Good Morning!!',                                        name = 'John'))


# In[4]:


x = 10.3456789
print('The value of x is %3.2f' %x)
print('The value of x is %3.4f' %x)


# In[5]:


for x in range(1, 19):
     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


# In[7]:



table = {'Raj': 9480123526, 'Rai': 9480123527, 'dinesh': 9480123528}
for name, phone in table.items():
     print('{0:10} ==> {1:10d}'.format(name, phone))
        


# In[8]:


x = input('Enter a string: ')
print("The entered string is :{0}".format(x))
y = int(input('Enter a integer: '))
print("The entered integer is :",y)
z = float(input('Enter a floating point number:'))
print("The entered real number  is :",z)


# In[9]:


x = ('1' + '2' +
     '3' + '4')
# Example of explicit line continuation
y = '1' + '2' + '11' + '12'
weekdays = ['Monday', 'Tuesday', 'Wednesday',
'Thursday', 'Friday']
weekday = {'one':
           'Monday'}
print ('x has a value of', x)
print ('y has a value of', y)
print(weekdays)
print(weekday)


# In[10]:


import os; x = 'Hello'; print(x)


# In[11]:


var = -1
if var < 0:
    print(var)
    print("the value of var is negative")
# If there is only a single clause then it may go on the same line as the
# header statement
if ( var == -1 ) : 
    print("the value of var is negative")


# In[12]:


var = 1
if var < 0:
    print("the value of var is negative")
    print(var)
else:
    print("the value of var is positive")
    print(var)


# In[13]:


score = 95
if score >= 99:
    print('A')
elif score >=75:
    print('B')
elif score >= 60:
    print('C')
elif score >= 35:
    print('D')
else:
    print('F')
3.0


# In[14]:


print("First Example")
for item in [1,2,3,4,5]:
    print('item :', item)
print("Second Example")
letters = ['A', 'B', 'C']
for index in range(len(letters)):
    print('First loop letter :', letters[index])


# In[15]:


# Create lists
list_1 = ['Statistics', 'Programming', 2016, 2017, 2018]
list_2 = ['a', 'b', 1, 2, 3, 4, 5, 6, 7 ]
# Accessing values in lists
print("list_1[0]: ", list_1[0])
print("list2_[1:5]: ", list_2[1:5])


# In[16]:


print("Values of list_1: ", list_1)
# Updating existing value of list
print("Index 2 value : ", list_1[2])
list_1[2] = 2015;
print("Index 2's new value : ", list_1[2])


# In[17]:


import string
import operator
#Example code for basic operations on lists

print("Length: ", len(list_1))

print("Concatenation: ", [1,2,3] + [4, 5, 6])

print("Repetition :", ['Hello'] * 4)

print("Membership :", 3 in [1,2,3])

print("Iteration :")
for x in [1,2,3]: print(x)

# Negative sign will count from the right
print("slicing :", list_1[-2])

# If you dont specify the end explicitly, all elements from the specified
#start index will be printed
print("slicing range: ", list_1[1:])

print("Max of list: ", max([1,2,3,4,5]))

print("Min of list: ", min([1,2,3,4,5]))

print("Count number of 1 in list: ", [1,1,2,3,4,5,].count(1))

list_1.extend(list_2)

print("Extended :", list_1)

print("Index for Programming:",list_1.index('Programming'))
print (list_1)
print("pop last item in list: ", list_1.pop())
print("pop the item with index 2: ", list_1.pop(2))
list_1.remove('b')
print("removed b from list: ", list_1)
list_1.reverse()
print("Reverse: ", list_1)
list_1 = ['a','c','b']
list_1.sort()
print("Sort ascending: ", list_1)
list_1.sort(reverse = True)
print("Sort descending: ", list_1)


# In[18]:


Tuple = ()
print("Empty Tuple: ", Tuple)
Tuple = (1,)
print("Tuple with single item: ", Tuple)
Tuple = ('a','b','c','d',1,2,3)
print("Sample Tuple :", Tuple)


# In[19]:


Tuple = ('a', 'b', 'c', 'd', 1, 2, 3)
print("3rd item of Tuple:", Tuple[2])
print("First 3 items of Tuple", Tuple[0:2])


# In[20]:


Tuple = ('a','b','c','d',1,2,3)
print("Length of Tuple: ", len(Tuple))
Tuple_Concat = Tuple + (7,8,9)
print("Concatinated Tuple: ", Tuple_Concat)

print("Repetition: ", (1,'a',2, 'b') * 3)
print("Membership check: ", 3 in (1,2,3))
# Iteration
for x in (1, 2, 3): print(x)
print("Negative sign will retrieve item from right: ", Tuple_Concat[-2])
print("Sliced Tuple [2:] ", Tuple_Concat[2:])
# Find max
print("Max of the Tuple (1,2,3,4,5,6,7,8,9,10): ",
max((1,2,3,4,5,6,7,8,9,10)))
print("Min of the Tuple (1,2,3,4,5,6,7,8,9,10): ",
min((1,2,3,4,5,6,7,8,9,10)))
print("List [1,2,3,4] converted to tuple: ", type(tuple([1,2,3,4])))


# In[21]:


dict = {'Name': 'Jivin', 'Age': 6, 'Class': 'First'}
print("Sample dictionary: ", dict)


# In[22]:


print("Value of key Name, from sample dictionary:", dict['Name'])


# In[23]:


dict0 = {'Name': 'Jivin', 'Age': 6, 'Class': 'First'}
print("Sample dictionary: ", dict0)
k=1
for i in dict0:
    print(k,i,dict0[i])
    k=k+1
del (dict0['Name']) # Delete specific item

print("Sample dictionary post deletion of item Name:", dict0)

dict0 = {'Name': 'Jivin', 'Age': 6, 'Class': 'First'}
dict0.clear() # Clear all the contents of dictionary
print("dict post dict.clear():", dict0)

dict = {'Name': 'Jivin', 'Age': 6, 'Class': 'First'}
del (dict0) # Delete the dictionary
#print(dict0)


# In[24]:


# Basic operations
dict = {'Name': 'Jivin', 'Age': 6, 'Class': 'First'}
print("Length of dict: ", len(dict))

# Copy the dict
dict1 = dict.copy()
print("Copy:\n",dict1)

# Retrieve value for a given key
print("Value for Age: ", dict.get('Age'))

# Return items of dictionary
print("dict items: ", dict.items())

# Return items of keys
print("dict keys: ", dict.keys())

# return values of dict
print("Value of dict: ", dict.values())

# Concatenate dicts
dict1 = {'Name': 'Jivin', 'Age': 6}
dict2 = {'Sex': 'male' }
dict1.update(dict2)
print("dict1.update(dict2) = ", dict1)


# In[25]:


def add(x, y): 
    return x + y
print("FUNCTION ADD:\n",add(3,2))

add = lambda x, y : x + y 
print("LAMBDA ADD :\n",add(3,2))


# In[26]:


def sample_function(**args):
    for a in args:
        print(a, args[a])
# Call the function
sample_function(name='John', age=27)


# In[27]:


# Global variable
x = 10
# Simple function to add two numbers
def sum_two_numbers(y):
    return x + y
# Call the function and print result
print(sum_two_numbers(10))


# In[ ]:




