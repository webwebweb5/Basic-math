#Arithmetic progression
import math

print('Arithmetic progression')
print('use to find Sn')
print('Sn =(n/2*(2*a1+(n-1)*d)')
a1 = float(input('a1(the initial term) : '))
n = int(input('n : '))
d = float(input('d(the common difference) : '))

def Sequences(n):
    return float(n/2*(2*a1+(n-1)*d))

print('Sn = ' + str(Sequences(n)))
