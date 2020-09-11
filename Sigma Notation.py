#Sigma Notation ∑n
import math

print('Sigma Notation')
print('use to find ∑n')
print('∑n = n/2*(n+1)')

n = float(input('n : '))

def Sequences():
    return float(n/2*(n+1))

print('∑n = ' + str(Sequences()))
