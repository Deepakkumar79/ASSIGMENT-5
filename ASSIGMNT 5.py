#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT 5
1. What does an empty dictionary's code look like?

ANSWER:-Empty dictionary is represented by a pair of curly braces '{}'. 2. What is the value of a dictionary value with the key 'foo' and the value 42?

ANSWER:-{'foo': 42}3. What is the most significant distinction between a dictionary and a list?

ANSWER:-The elements in a list are ordered, and the elements in a dictionary aren't.
Also, elements in a list must be accessed using numerical indices. Elements in a dictionary are indexed using keys, which can have different data types. 

 4.What happens if you try to access spam['foo'] if spam is {'bar': 100}?
 
 ANSWER:-You will get a KeyError error.5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

ANSWER:-There is no difference, the expression " 'cat' in spam " checks whether 'cat' is a key in spam.6.If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

ANSWER:-'cat' in spam checks whether'cat' exists as a key in spam. 'cat' in spam.values() checks whether 'cat' is a value in spam.
7.What is a shortcut for the following code?
if 'color' not in spam:
spam['color'] = 'black'

ANSWER:-spam.setdefault('color', 'black')
8.How do you "pretty print" dictionary values using which module and function?

ANSWER:-The module is pprint.
The functions are pprint.pprint() and pprint.pformat().