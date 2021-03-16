#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import matplotlib.pyplot as plt
import numpy as np # maybe not needed


# In[29]:


def random_walk(nsteps):
    if nsteps <= 0: # if our user wants to troll and gives a number less or equal to zero
    # we will tell them gives a positive number like 69
        print("Enter a positive number. For example, the number 69")
    else:
        # print("Your random walk is starting")
        i_step = 0 # step i, i < n
        # the walk starts at 0
        step = 0
        walk = [step]
        while i_step < nsteps:
            # at each i_step a coin will be flipped 
            coinflip = random.random() # we will get a random number from 0 to 1 (excluded)
            # if coinflip greater than 0.5  
            if coinflip > 0.5:
                step += 1 # we add 1 to our walk
            else: # else 
                step -= 1 # we subtract 1
            walk.append(step)
            i_step += 1
            
        return walk


# In[30]:


my_walk = random_walk(100)


# In[31]:


def plot_walk(walk): # this is to try and be cute
    plt.plot(walk)
    plt.show()
    
plot_walk(my_walk)


# In[35]:


# more than one random walk

def multi_random_walks(number, nsteps):
    # to avoid ugly errors we will prevent one or lesser numbers
    if number < 0:
        print("You can't take negative random walks. what is that even?")
    elif number == 0:
        print("You can take zero random walks by standing still")
    elif number == 1:
        print("There's already a function for that")
    else:
        if nsteps <= 0: # if our user wants to troll and gives a number less or equal to zero
    # we will tell them gives a positive number like 69
            print("Enter a positive number. For example, the number 69")
        else:
            walks = []
            for i in range(number): # run number times the function random_walk
                walks.append(random_walk(nsteps)) # append it to a list
        return walks


# In[36]:


print(multi_random_walks(4, 30))


# In[37]:


walks = multi_random_walks(25, 100)
plot_walk(walks)


# In[39]:


# two dimensional random walk

X = random_walk(150)
Y = random_walk(150)

plt.plot(X, Y)
plt.show()


# In[ ]:




