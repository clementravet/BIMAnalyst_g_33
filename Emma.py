import ifcopenshell

model = ifcopenshell.open(r"C:\Users\Emma\OneDrive\DTU\41639 Advanced Open BIM\Models\CES_BLD_24_06_MEP.ifc")

#Claim Check: There is mechanical ventilation
aggregat = model.by_type('IfcBuildingElementProxy')

#Result >0 there is mechanical
print(len(aggregat))