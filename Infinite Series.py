#Infinite Series
import math

print('Infinite Series')
print('use to find S∞')
print('S∞ = a1/(1/r)')

a1 = float(input('a1(the initial term) : '))
r = float(input('r : '))

def Sequences():
    return float(a1/(1-r))

print('S∞ = ' + str(Sequences()))
