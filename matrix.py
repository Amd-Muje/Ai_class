# -*- coding: utf-8 -*-
"""Matrix.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zYFOHf0E97GStaXvwDotTcnhtzDyiwTp
"""

import numpy as np

a = np.array([[2,0,-3],
             [1,4,5]])

b = np.array([[3,1],
             [-1, 0],
             [4, 2]])

c = np.array([[4,7],
             [2,1],
              [1,-1]])

ab = np.dot(a,b)

ac = np.dot(a,c)

# matrix ab + ac =

print(ab + ac)
