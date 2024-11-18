####################################################################################################################################
#############################################          IMPORT WINDOW          ######################################################
####################################################################################################################################
import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
import ifcopenshell.util.pset
import ifcopenshell.util.selector
from tabulate import tabulate


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



####################################################################################################################################
######################################          CODE FOR U_VALUE OF THE WALLS         ##############################################
####################################################################################################################################
def U_value_walls(ifc):
    result = find_U_value_element(ifc.by_type("IfcWall"))
    return result



####################################################################################################################################
#######################################          CODE FOR U_VALUE OF THE ROOF         ##############################################
####################################################################################################################################
def U_value_roofs(ifc):
    result = find_U_value_element(ifc.by_type("IfcRoof"))
    return result



####################################################################################################################################
#######################################          CODE FOR U_VALUE OF THE SLAB         ##############################################
####################################################################################################################################
def U_value_slabs(ifc):
    result = find_U_value_element(ifc.by_type("IfcSlab"))
    return result



####################################################################################################################################
###############################          COMPARISON TABLE BETWEEN REPORT AND BIM MODEL         #####################################
####################################################################################################################################
def table_report_BIM(ifc):
    U_value_roof_report = 0.14
    U_value_external_walls_report = 0.21
    U_value_basement_walls_report = 0.18
    U_value_basement_slab_report = 0.21
    U_value_roof_BIM = U_value_roofs(ifc)[1][1]*1.7
    U_value_external_walls_BIM = U_value_curtain_walls(ifc)[1][1]*1.7
    U_value_basement_walls_BIM = 0
    U_value_basement_slab_BIM = U_value_slabs(ifc)[1][1]*1.7
    table = [
    ["Roof",            U_value_roof_report,            U_value_roof_BIM], 
    ["External walls",  U_value_external_walls_report,  U_value_external_walls_BIM], 
    ["Basement walls",  U_value_basement_walls_report,  U_value_basement_walls_BIM], 
    ["Basement slab",   U_value_basement_slab_report,   U_value_basement_slab_BIM]
    ]
    head = [" ", "Report" , "BIM Model"]
    print(tabulate(table, headers=head, tablefmt="grid"))



####################################################################################################################################
#####################                    DEVELOPMENT OF TOOL TO ANALYSE DGNB CRITERIA                    ###########################
#####################          TEC4.4 – Quality of the building envelope (C) Points total: 50pts         ###########################
####################################################################################################################################
def DGNB_TEC4_4_score(x):
    min_U_value_requirement = 0.3  #Building Regulation Requirement : minimum requirements for U-value of exterior walls and basement walls towards ground: 0.30W/m²K
    level1 = min_U_value_requirement
    level2 = 0.85*min_U_value_requirement
    level3 = 0.7*min_U_value_requirement
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


def Check_DGNB(ifc):
    min_U_value_requirement = 0.3  #Building Regulation Requirement : minimum requirements for U-value of exterior walls and basement walls towards ground: 0.30W/m²K
    level1 = min_U_value_requirement
    level2 = 0.85*min_U_value_requirement
    level3 = 0.7*min_U_value_requirement
    U_value_external_walls_report = 0.21
    U_value_external_walls_BIM = U_value_curtain_walls(ifc)[1][1]*1.7
    print(" ")
    print("The DGNB score from the data of the report is", DGNB_TEC4_4_score(U_value_external_walls_report), "points, and the one from the data of the BIM model is", DGNB_TEC4_4_score(U_value_external_walls_BIM), "points")
    print(" ")
    if U_value_external_walls_report == U_value_external_walls_BIM:
        print("The data from the report and the BIM model can lead to the same result")
    if U_value_external_walls_report != U_value_external_walls_BIM:
        print("The data from the report and the BIM model lead to a different result")
    print("")