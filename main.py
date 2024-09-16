import ifcopenshell

from .rules import pipeRule
from .rules import ventilationNameRule
from .rules import ventilationRule

model = ifcopenshell.open("path/to/ifcfile.ifc")

pipeResult = pipeRule.checkRule(model)
ventilationNameResult = ventilationNameRule.checkRule(model)
ventilationResult = ventilationRule.checkRule(model)

print("Pipe result:", pipeResult)
print("Ventilation Name result:", ventilationNameResult)
print("Ventilation result:", ventilationResult)
