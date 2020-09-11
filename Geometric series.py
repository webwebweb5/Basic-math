#Geometric series
import math

print('Geometric series')
print('use to find Sn')
print('Sn = a1*(1-r^n)/(1-r)')
a1 = float(input('a1(the initial term) : '))
r = float(input('r : '))
n = int(input('n : '))

def Sequences(n):
    return float(a1*(1-r**n)/(1-r))

print('Sn = ' + str(Sequences(n)))
