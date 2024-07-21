from fractions import Fraction

def black_probability(n1, n2, n3, n4):
    x = ['w'] * n1 + ['b'] * n2
    y = ['w'] * n3 + ['b'] * n4
    
    total_outcomes = len(x) * (len(y) + 1)
    
    favorable_outcomes = (x.count('w') * y.count('b') + 
                          x.count('b') * (y.count('b') + 1))
   
    probability = Fraction(favorable_outcomes, total_outcomes)
    
    return probability

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

print(black_probability(n1, n2, n3, n4))
