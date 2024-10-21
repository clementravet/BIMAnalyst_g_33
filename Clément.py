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

model = ifcopenshell.open(r"C:\Users\clemr\Desktop\DTU\-----COURSES-----\41934-AdvancedBIM\Assignment 1\CES_BLD_24_06_ARC.ifc")

Wall_all = model.by_type("IfcCurtainWall")
Wall = model.by_type("IfcCurtainWall")[100]

#print(ifcopenshell.util.element.get_psets(Wall))
#print(Wall.Name)
#print(ifcopenshell.util.selector.get_element_value(Wall, "type.Name"))
#print(ifcopenshell.util.selector.get_element_value(Wall, "material.Name"))   --> None
#print(pset_qto.get_applicable_names("IfcCurtainWall"))

#Wall_materials = selector.get_element_value(Wall, "Pset_WallCommon.IsExternal")

#print(ifcopenshell.util.element.get_pset(Wall, 'Dimensions'))

#print(ifcopenshell.util.element.get_pset(Wall, 'Analytical Properties'))





#Properties = ifcopenshell.util.element.get_pset(Wall, 'Analytical Properties')
#print(Properties.get('Heat Transfer Coefficient (U)'))

for external_wall in model.by_type("IfcCurtainWall"):
    print("The wall name is", external_wall.Name)
    properties = ifcopenshell.util.element.get_pset(external_wall, 'Analytical Properties')
    if properties==None:
        print("This wall does not have an U value")
    else:
        U_value = properties.get('Heat Transfer Coefficient (U)')
        print("The U value of the wall is", U_value)