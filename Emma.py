####### THIS IS A TEST ####### remove# to run the script
#import ifcopenshell

#model = ifcopenshell.open(r"C:\Users\Emma\OneDrive\DTU\41639 Advanced Open BIM\Models\CES_BLD_24_06_MEP.ifc")

#Claim Check: There is mechanical ventilation
#aggregat = model.by_type('IfcBuildingElementProxy')

#Result >0 there is mechanical
#print(len(aggregat))





############################################ U-VALUE FOR EXTERIOR WALL #########################################
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
import ifcopenshell.util
import ifcopenshell.util.element
import ifcopenshell.util.selector

# Indlæs IFC-filen
ifc_file = ifcopenshell.open(r"C:\Users\Emma\OneDrive - Danmarks Tekniske Universitet\Efterår 24\41639 Advanced Open BIM\Models\CES_BLD_24_06_ARC.ifc")

# Find vægge
walls = ifc_file.by_type("IfcCurtainWall")
Wall1 = walls[15]

# Få egenskabssæt (psets) fra væggen
psets = ifcopenshell.util.pset.get_psets(Wall1)
print(psets)


# Gå gennem alle vægge og tjek U-værdi
for wall in walls:
    # Hent egenskaberne for væggen
    for definition in wall.IsDefinedBy:
        if definition.is_a("IfcRelDefinesByProperties"):
            property_set = definition.RelatingPropertyDefinition
            if property_set.is_a("IfcPropertySet"):
                # Gennemgå alle egenskaber i property set
                for property in property_set.HasProperties:
                    if property.is_a("IfcPropertySingleValue"):
                        # Tjek om egenskaben hedder "U-værdi" eller noget lignende
                        if property.Name == "U-Value" or property.Name == "Uværdi" or property.Name == "U_value":
                            u_value = property.NominalValue.wrappedValue
                            print(f"U-værdi for væg {wall.GlobalId}: {u_value}")
                            break
                else:
                    print(f"Væg {wall.GlobalId} har ingen U-værdi angivet.")