import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
import ifcopenshell.util.pset
import ifcopenshell.util.selector
from tabulate import tabulate
import numpy as np

A = np.zeros((2,100))
A[0,0] = 'name'
print(A)