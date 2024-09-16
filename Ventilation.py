import ifcopenshell
from bonsai.bim.ifc import IfcStore
file = IfcStore.get_file()

things = file.by_type('IfcDuctSegment')

print("Num of things",len(things))

duct = file.by_type('IfcDuctSegment')[0]
print(duct.is_a()) # Returns 'IfcDuct'

print(duct.id())
print(duct.GlobalId)
print(duct.Name)

#Information on elemenet. This script gives us all info at once
print(duct.get_info()) # Gives us a dictionary of attributes, such as {'id': 8, 'type': 'IfcWall', 'GlobalId': '2_qMTAIHrEYu0vYcqK8cBX', ... }

import ifcopenshell.util
import ifcopenshell.util.element
print(ifcopenshell.util.element.get_psets(duct))
