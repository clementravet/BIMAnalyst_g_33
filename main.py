import ifcopenshell

from .rules import pipeRule
from .rules import doorRule

model = ifcopenshell.open("path/to/ifcfile.ifc")

pipeResult = pipeRule.checkRule(ifc)
doorResult = doorRule.checkRule(model)

print("Pipe result:", pipeResult)
print("Door result:", doorResult)
