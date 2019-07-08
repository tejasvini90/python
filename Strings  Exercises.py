# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 01:06:05 2019

@author: SHAIL
"""


#exercises =================================================================

s = "Hey there! what should this string be?"
# find length of the above string
print(len(s))

# First occurrence of "s"
print(s.index('s'))

# Number of a's should be ?
print(s.count('s'))

# Slicing the string into bits


#1 - The first five characters are 
s1=(s[0:4])
print(s1)
#2 - The next five characters are 
s2=(s[4:9])
print(s2)
#3 - The thirteenth character is 
s3=(s[12])
print(s3)

#4 - length of total string

n=(s1 + s2 + s3)
print(n)

#5 -  Convert everything to uppercase
print(n.upper())


# Convert everything to lowercase
print(n.lower())


# Split the string into separate strings,
# each containing only a word


print(s.split(' '))


