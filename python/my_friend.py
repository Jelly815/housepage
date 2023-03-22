# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 22:10:38 2019

@author: Jelly
"""
from collections import Counter
import matplotlib.pyplot as plt
import math
#my_friend = [100,100,1,2,3,30,40,1,2,3,1,2,3,50,60,100,100,1,2,3]
my_friend = [100,1,2,30,20,3,35]
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

#print(sorted(my_friend))
#abc1 = quantile(my_friend,0.33)
#abc2 = quantile(my_friend,0.66)

#print(abc1)
#print(abc2)


c = Counter("dengjingdong") 
#c = Counter({'n': 3, 'g': 3, 'd': 2, 'i': 1, 'o': 1, 'e': 1, 'j': 1}) 
print("原始數據：",c) 
print("最多的兩個元素：",c.most_common())#輸出數量最多的元素 
