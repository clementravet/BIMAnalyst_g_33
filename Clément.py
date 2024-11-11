####################################################################################################################################
#############################################          IMPORT WINDOW          ######################################################
####################################################################################################################################
#import ifcopenshell
#import ifcopenshell.util
#import ifcopenshell.util.element
#import ifcopenshell.util.selector

#model1 = ifcopenshell.open(r"C:\Users\clemr\Desktop\DTU\-----COURSES-----\41934-AdvancedBIM\elec.ifc")


#lights = model.by_type('IfcLightFixtureType')
#print(f"Lights in model: {len(lights)}")

#LightFixture = model.by_type('IfcLightFixtureType')
#FirstLightFixture = LightFixture[0]


####################################################################################################################################
#############################################          PRINT WINDOW          ######################################################
####################################################################################################################################
#print(len(LightFixture))
#print(ifcopenshell.util.element.get_psets(FirstLightFixture))
#print(ifcopenshell.util.selector.filter_elements(model, "IfcLightFixtureType"))



####################################################################################################################################
#############################################          IMPORT WINDOW          ######################################################
####################################################################################################################################
#import ifcopenshell
#import ifcopenshell.util
#import ifcopenshell.util.element
#import ifcopenshell.util.selector

#model = ifcopenshell.open(r"C:\Users\clemr\Desktop\DTU\-----COURSES-----\41934-AdvancedBIM\Assignment 1\CES_BLD_24_06_ARC.ifc")

#MechanicalVentilation = model.by_type("IfcBuildingElementProxy")
#MechanicalVentilation1 = MechanicalVentilation[0]
#MechanicalVentilation2 = MechanicalVentilation[1]

#### Number of elements for the mechanical ventilation
#print(f"There are {len(MechanicalVentilation)} mechanical ventilation systems")
#print("     ")

#### Name of Mechanical ventilation
#print(f"The first mechanical ventilation is {MechanicalVentilation1.Name}")
#print(f"The second mechanical ventilation is {MechanicalVentilation2.Name}")
#print("     ")

#### 
#print(ifcopenshell.util.selector.filter_elements(model, "IfcBuildingElementProxy"))


#### Walls
#Wall = model.by_type("IfcCurtainWall")[1]

#print(ifcopenshell.util.element.get_psets(Wall))

####################################################################################################################################
##############################################          PRINT WINDOW          ######################################################
####################################################################################################################################
#print(ifcopenshell.util.element.get_psets(MechanicalVentilation))
#print(ifcopenshell.util.selector.filter_elements(model, "IfcLightFixtureType"))





























####################################################################################################################################
#############################################          IMPORT WINDOW          ######################################################
####################################################################################################################################
import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
import ifcopenshell.util.pset
import ifcopenshell.util.selector
from tabulate import tabulate

model = ifcopenshell.open(r"C:\Users\clemr\Desktop\DTU\-----COURSES-----\41934-AdvancedBIM\Assignment 1\CES_BLD_24_06_ARC.ifc")

Walls = model.by_type("IfcCurtainWall")
Wall_100 = Walls[100]
Roofs = model.by_type("IfcRoof")
Roof_1 = Roofs[0]
#Slabs = model.by_type("IfcSlab")
#Slab_1 = Slabs[0]


####################################################################################################################################
############################################          EXPERIMENTATION         ######################################################
####################################################################################################################################
#print(Wall.Name)
#print(ifcopenshell.util.selector.get_element_value(Wall, "type.Name"))
#print(ifcopenshell.util.selector.get_element_value(Wall, "material.Name"))   --> None
#print(pset_qto.get_applicable_names("IfcCurtainWall"))

#Wall_materials = selector.get_element_value(Wall, "Pset_WallCommon.IsExternal")

#print(ifcopenshell.util.element.get_pset(Wall, 'Dimensions'))

#print(ifcopenshell.util.element.get_pset(Wall, 'Analytical Properties'))

#Properties = ifcopenshell.util.element.get_pset(Wall, 'Analytical Properties')
#print(Properties.get('Heat Transfer Coefficient (U)'))



####################################################################################################################################
#######################################          SHOW EVERY ELEMENT (PSETS)         ################################################
####################################################################################################################################
#print(ifcopenshell.util.element.get_psets(Wall_100))
#print(len(Walls))
#print(ifcopenshell.util.element.get_psets(Roof_1))
#print(len(Roofs))



####################################################################################################################################
##################################          CODE FOR U_VALUE OF THE CURTAIN WALLS         ##########################################
####################################################################################################################################
#for external_wall in model.by_type("IfcCurtainWall"):
#    print("The wall name is", external_wall.Name)
#    properties = ifcopenshell.util.element.get_pset(external_wall, 'Analytical Properties')
#    if properties==None:
#        print("This wall does not have an U value")
#    else:
#        U_value = properties.get('Heat Transfer Coefficient (U)')
#        print("The U value of the wall is", U_value)

def find_U_value_element(x):
    L = []
    for element in x:
        properties = ifcopenshell.util.element.get_pset(element, 'Analytical Properties')
        if properties != None:
            U_value = properties.get('Heat Transfer Coefficient (U)')
            if U_value not in L and U_value != None:
                L.append(U_value)
    return L

def find_U_value_element2(x):
    L = []
    L1 = []
    L2 = []
    L1.append("Name")
    L2.append("U_value")
    n = 0
    for element in x:
        properties = ifcopenshell.util.element.get_pset(element, 'Analytical Properties')
        if properties != None:
            U_value = properties.get('Heat Transfer Coefficient (U)')
            if U_value not in L2 and U_value != None:
                L1.append(element.Name)
                L2.append(U_value)
                n = n+1
    L.append(L1)
    L.append(L2)
    return L

U_value_curtain_walls = find_U_value_element2(model.by_type("IfcCurtainWall"))
print("The different U_values coming from the IfcCurtainWall are :", U_value_curtain_walls)

table_curtain_wall = U_value_curtain_walls
print(tabulate(table_curtain_wall, tablefmt="grid"))
print(" ")



####################################################################################################################################
######################################          CODE FOR U_VALUE OF THE WALLS         ##############################################
####################################################################################################################################
U_value_walls = find_U_value_element2(model.by_type("IfcWall"))
print("The different U_values coming from the IfcWall are :", U_value_walls)

table_wall = U_value_walls
print(tabulate(table_wall, tablefmt="grid"))
print(" ")



####################################################################################################################################
#######################################          CODE FOR U_VALUE OF THE ROOF         ##############################################
####################################################################################################################################
#for roof in model.by_type("IfcRoof"):
#    print("The roof name is", roof.Name)
#    properties = ifcopenshell.util.element.get_pset(roof, 'Analytical Properties')
#    if properties==None:
#        print("This roof does not have an U value")
#    else:
#        U_value = properties.get('Heat Transfer Coefficient (U)')
#        print("The U value of the roof is", U_value)

U_value_roofs = find_U_value_element2(model.by_type("IfcRoof"))
print("The different U_values coming from the IfcRoof are :", U_value_roofs)

table_roof = U_value_roofs
print(tabulate(table_roof, tablefmt="grid"))
print(" ")



####################################################################################################################################
#######################################          CODE FOR U_VALUE OF THE SLAB         ##############################################
####################################################################################################################################
#for slab in model.by_type("IfcSlab"):
#    print("The slab name is", slab.Name)
#    properties = ifcopenshell.util.element.get_pset(slab, 'Analytical Properties')
#    if properties==None:
#        print("This slab does not have an U value")
#    else:
#        U_value = properties.get('Heat Transfer Coefficient (U)')
#        print("The U value of the slab is", U_value)

U_value_slabs = find_U_value_element2(model.by_type("IfcSlab"))
print("The different U_values coming from the IfcSlab are :", U_value_slabs)

table_slab = U_value_slabs
print(tabulate(table_slab, tablefmt="grid"))
print(" ")



####################################################################################################################################
###############################          COMPARISON TABLE BETWEEN REPORT AND BIM MODEL         #####################################
####################################################################################################################################
## Datas of the report
U_value_roof_report = 0.14                 #0.085*1.7
U_value_external_walls_report = 0.21       #0.12*1.7
U_value_basement_walls_report = 0.18       #0.11*1.7
U_value_basement_slab_report = 0.21        #0.12*1.7

## Datas of the BIM Model
U_value_roof_BIM = U_value_roofs[1][1]*1.7
U_value_external_walls_BIM = U_value_curtain_walls[1][1]*1.7
U_value_basement_walls_BIM = 0
U_value_basement_slab_BIM = U_value_slabs[1][1]*1.7

table = [
    ["Roof",            U_value_roof_report,            U_value_roof_BIM], 
    ["External walls",  U_value_external_walls_report,  U_value_external_walls_BIM], 
    ["Basement walls",  U_value_basement_walls_report,  U_value_basement_walls_BIM], 
    ["Basement slab",   U_value_basement_slab_report,   U_value_basement_slab_BIM]
]

# create header
head = [" ", "Report" , "BIM Model"]

# display table
print(tabulate(table, tablefmt="grid"))



####################################################################################################################################
#####################                    DEVELOPMENT OF TOOL TO ANALYSE DGNB CRITERIA                    ###########################
#####################          TEC4.4 – Quality of the building envelope (C) Points total: 50pts         ###########################
####################################################################################################################################
min_U_value_requirement = 0.3  #Building Regulation Requirement : minimum requirements for U-value of exterior walls and basement walls towards ground: 0.30W/m²K
level1 = min_U_value_requirement
level2 = 0.85*min_U_value_requirement
level3 = 0.7*min_U_value_requirement

def DGNB_TEC4_4_score(x):
    score = 0
    if x < level3:
        score = 50
        return score
    elif x >= level3 and x < level2:
        score = 30
        return score
    elif x >= level2 and x < level1:
        score = 20
        return score
    else:
        return score

print(" ")
print("The DGNB score from the data of the report is", DGNB_TEC4_4_score(U_value_external_walls_report), "points, and the one from the data of the BIM model is", DGNB_TEC4_4_score(U_value_external_walls_BIM), "points")
print(" ")
if U_value_external_walls_report == U_value_external_walls_BIM:
    print("The data from the report and the BIM model can lead to the same result")
if U_value_external_walls_report != U_value_external_walls_BIM:
    print("The data from the report and the BIM model lead to a different result")
print("")
