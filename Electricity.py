####################################################################################################################################
#############################################          IMPORT WINDOW          ######################################################
####################################################################################################################################
import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
import ifcopenshell.util.selector

model = ifcopenshell.open(r"C:\Users\clemr\Desktop\DTU\-----COURSES-----\41934-AdvancedBIM\elec.ifc")


#lights = model.by_type('IfcLightFixtureType')
#print(f"Lights in model: {len(lights)}")

LightFixture = model.by_type('IfcLightFixtureType')
FirstLightFixture = LightFixture[0]


####################################################################################################################################
#############################################          PRINT WINDOW          ######################################################
####################################################################################################################################
print(len(LightFixture))
print(ifcopenshell.util.element.get_psets(FirstLightFixture))
#print(ifcopenshell.util.selector.filter_elements(model, "IfcLightFixtureType"))




