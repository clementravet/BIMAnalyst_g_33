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

####################################################################################################################################
##################################          CODE FOR U_VALUE OF THE CURTAIN WALLS         ##########################################
####################################################################################################################################
def find_U_value_element(x):
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

def U_value_curtain_walls(ifc):
    result = find_U_value_element(ifc.by_type("IfcCurtainWall"))
    return result
print("The different U_values coming from the IfcCurtainWall are :", U_value_curtain_walls(model))

table_curtain_wall = U_value_curtain_walls(model)
print(tabulate(table_curtain_wall, tablefmt="grid"))
print(" ")



####################################################################################################################################
######################################          CODE FOR U_VALUE OF THE WALLS         ##############################################
####################################################################################################################################
def U_value_walls(ifc):
    result = find_U_value_element(ifc.by_type("IfcWall"))
    return result
print("The different U_values coming from the IfcWall are :", U_value_walls(model))

table_wall = U_value_walls(model)
print(tabulate(table_wall, tablefmt="grid"))
print(" ")



####################################################################################################################################
#######################################          CODE FOR U_VALUE OF THE ROOF         ##############################################
####################################################################################################################################
def U_value_roofs(ifc):
    result = find_U_value_element(ifc.by_type("IfcRoof"))
    return result
print("The different U_values coming from the IfcRoof are :", U_value_roofs(model))

table_roof = U_value_roofs(model)
print(tabulate(table_roof, tablefmt="grid"))
print(" ")



####################################################################################################################################
#######################################          CODE FOR U_VALUE OF THE SLAB         ##############################################
####################################################################################################################################
def U_value_slabs(ifc):
    result = find_U_value_element(ifc.by_type("IfcSlab"))
    return result
print("The different U_values coming from the IfcSlab are :", U_value_slabs(model))

table_slab = U_value_slabs(model)
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

