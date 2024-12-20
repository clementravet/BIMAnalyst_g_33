import ifcopenshell
from tabulate import tabulate

from rules import Finalproject

model = ifcopenshell.open(r"ifcpathfile.ifc")



####################################################################################################################################
##########################################          SEARCHING FOR U_VALUES         #################################################
####################################################################################################################################
U_value_curtain_walls = Finalproject.U_value_curtain_walls(model)
print("The different U_values coming from the IfcCurtainWall are :", U_value_curtain_walls)
print(tabulate(U_value_curtain_walls, tablefmt="grid"))
print(" ")

U_value_walls = Finalproject.U_value_walls(model)
print("The different U_values coming from the IfcWall are :", U_value_walls)
print(tabulate(U_value_walls, tablefmt="grid"))
print(" ")

U_value_roofs = Finalproject.U_value_roofs(model)
print("The different U_values coming from the IfcRoof are :", U_value_roofs)
print(tabulate(U_value_roofs, tablefmt="grid"))
print(" ")

U_value_slabs = Finalproject.U_value_slabs(model)
print("The different U_values coming from the IfcSlab are :", U_value_slabs)
print(tabulate(U_value_slabs, tablefmt="grid"))
print(" ")



####################################################################################################################################
############################################          REPORT VS BIM MODEL         ##################################################
####################################################################################################################################
Finalproject.table_report_BIM(model)



####################################################################################################################################
###############################################          DGNB CRITERIA         #####################################################
####################################################################################################################################
Finalproject.Check_DGNB(model)
