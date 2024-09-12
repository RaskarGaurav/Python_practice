#!/usr/bin/python3
import sys

x=0
print(sys.getsizeof(x))

x=1
print(sys.getsizeof(x))

x= 2**20
print(sys.getsizeof(x))

x= 2**32
print(sys.getsizeof(x))

x=2**60
print(sys.getsizeof(x))

