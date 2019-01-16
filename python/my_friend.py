# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 22:10:38 2019

@author: Jelly
"""
from collections import Counter
import matplotlib.pyplot as plt

my_friend = [1,2,3,1,2,3,1,2,3,1,2,3,100,100,100,100]
friend_counts = Counter(my_friend)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs,ys)
plt.axis([0,101,0,25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

def quantile(x,p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]

abc = quantile(my_friend,0.90)

print(abc)