import sys
import time

def contador(i : float):
    print(i)
    contador(i+1)
    return i

def aumenta():
    sys.setrecursionlimit(200000000)

aumenta()
contador(1)