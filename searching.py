# -*- coding: utf-8 -*-
"""Searching.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fJkgAaL8gUS7qUG-OFQ7wHtM9ALMm_hm
"""

# soal diberikan list x dimana x adalah nilai random dari (0-10) sebanyak 20 data
# ada y1 = jika y1 ada dalam list dan y1 adalah genap maka print indexnya

import random

random_numbers = [random.randint(1, 10) for _ in range(20)]

y = int(input("Masukkan angka yang ingin dicari: "))

print(random_numbers)

for x in range(len(random_numbers)):
    if random_numbers[x] == y and random_numbers[x] % 2 == 0:
        print("Angka", y, "ditemukan di index ke", x)

# for x in range(len(random_numbers)):

