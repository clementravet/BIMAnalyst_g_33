####### THIS IS A TEST ####### remove# to run the script
#import ifcopenshell

#model = ifcopenshell.open(r"C:\Users\Emma\OneDrive\DTU\41639 Advanced Open BIM\Models\CES_BLD_24_06_MEP.ifc")

#Claim Check: There is mechanical ventilation
#aggregat = model.by_type('IfcBuildingElementProxy')

#Result >0 there is mechanical
#print(len(aggregat))





############################################ TEST AT DEN KAN HENTE FIL - VIRKER #########################################
import ifcopenshell

ifc = ifcopenshell.open(r"C:\Users\Emma\OneDrive - Danmarks Tekniske Universitet\Efterår 24\41639 Advanced Open BIM\Models\CES_BLD_24_06_ARC.ifc")

print(ifc.schema)

print(ifc.by_id(1))

walls = ifc.by_type('IfcWall')
print(len(walls))

wall = ifc.by_type('IfcWall')[0]
print(wall.is_a()) # Returns 'IfcWall'


################################################ CHATGPT Script ###########################################################

import ifcopenshell
import ifcopenshell.util.pset

# Indlæs IFC-filen
ifc_file = ifcopenshell.open(r"C:\Users\Emma\OneDrive - Danmarks Tekniske Universitet\Efterår 24\41639 Advanced Open BIM\Models\CES_BLD_24_06_ARC.ifc")

# Find vægge (IfcCurtainWall eller IfcWall)
walls = ifc_file.by_type("IfcWall")  # Ændret til IfcWall for at sikre, at vi får almindelige vægge
Wall1 = walls[0]  # Tager den første væg

# Få egenskabssæt (psets) fra væggen
psets = ifcopenshell.util.pset.get_psets(Wall1)
print(psets)



##################################################Clement code#########################################################################
import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
import ifcopenshell.util.pset
import ifcopenshell.util.selector

model = ifcopenshell.open(r"C:\Users\Emma\OneDrive - Danmarks Tekniske Universitet\Efterår 24\41639 Advanced Open BIM\Models\CES_BLD_24_06_ARC.ifc")

Wall_all = model.by_type("IfcCurtainWall")
Wall = model.by_type("IfcCurtainWall")[100]

for external_wall in model.by_type("IfcCurtainWall"):
    print("The wall name is", external_wall.Name)
    properties = ifcopenshell.util.element.get_pset(external_wall, 'Analytical Properties')
    if properties==None:
        print("This wall does not have an U value")
    else:
        U_value = properties.get('Heat Transfer Coefficient (U)')
        print("The U value of the wall is", U_value)
