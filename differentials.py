import matplotlib.pyplot as plt
import numpy as np
from value import Value
from graph import draw_dot

a=3
b=-2
c=5


# 3+(-2) * (-2) = -2 + 2 => 0
def f(a,b,c):
    return a*b + c

a = Value(data=2.0, label='a')
b = Value(data=-3.0, label='b')
c = Value(data=10.0, label='c')
d = a * b; d.label='d'
e = d + c; e.label='e'
e.label = 'e'

f = Value(data=-2.0, label='f')

L = e * f; L.label='L'

# dot = draw_dot(L)
# dot.render('output_graph')  # Saves the graph as 'output_graph.svg'
# dot.view()  # Opens the rendered graph in the default viewer


def derviative():
    a = Value(data=2.0, label='a')
    b = Value(data=-3.0, label='b')
    c = Value(data=10.0, label='c')
    d = a * b; d.label='d'
    e = d + c; e.label='e'
    e.label = 'e'

    f = Value(data=-2.0, label='f')

    L = e * f; L.label='L'

   
    h = 0.9
    a = Value(data=2.0 + h, label='a')
    b = Value(data=-3.0, label='b')
    c = Value(data=10.0, label='c')
    d = a * b; d.label='d'
    e = d + c; e.label='e'
    e.label = 'e'

    f = Value(data=-2.0, label='f')

    L1 = e * f; L1.label='L'


    der = (L1.data - L.data) / h

    print(der)


derviative()





