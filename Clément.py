####################################################################################################################################
#############################################          IMPORT WINDOW          ######################################################
####################################################################################################################################
#import ifcopenshell
#import ifcopenshell.util
#import ifcopenshell.util.element
#import ifcopenshell.util.selector

#model = ifcopenshell.open(r"C:\Users\clemr\Desktop\DTU\-----COURSES-----\41934-AdvancedBIM\elec.ifc")


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
import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
import ifcopenshell.util.selector

#model = ifcopenshell.open(r"C:\Users\clemr\Desktop\DTU\-----COURSES-----\41934-AdvancedBIM\Assignment 1\CES_BLD_24_06_MEP.ifc")
model2 = ifcopenshell.open(r"C:\Users\clemr\Desktop\DTU\-----COURSES-----\41934-AdvancedBIM\Assignment 1\CES_BLD_24_06_ARC.ifc")

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
Wall = model2.by_type("IfcCurtainWall")
Wall1 = Wall[15]

print(ifcopenshell.util.element.get_psets(Wall1))

####################################################################################################################################
##############################################          PRINT WINDOW          ######################################################
####################################################################################################################################
#print(ifcopenshell.util.element.get_psets(MechanicalVentilation))
#print(ifcopenshell.util.selector.filter_elements(model, "IfcLightFixtureType"))


