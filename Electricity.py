#import ifcopenshell
#import ifcopenshell.util
#import ifcopenshell.util.element
#import ifcopenshell.util.selector

#ifc = ifcopenshell.open('C:\Users\clemr\Desktop\DTU\h-----COURSES-----h\41934-Advanced BIM\elec.ifc')
###selector = Selector()

#things = file.by_type('IfcLightFixtureType')
###things = ifcopenshell.util.selector.parse(ifc, '.IfcLightFixtureType')
###Elecapp = things[0]

###print(len(things))

#for thing in things:
#    print(thing.Name)

#print(ifcopenshell.util.element.get_psets(Elecapp))

#element = ifcopenshell.util.selector.parse(file, '.IfcLightFixtureType[IfcElectricVoltageMeasure = "220."]')
#print(element)

#Pset_ElectricalDeviceCommon
#IfcElectricVoltageMeasure





import ifcopenshell
model = ifcopenshell.open('C:\Users\clemr\Desktop\DTU\elec.ifc')

lights = model.by_type('IfcLightFixtureType')
print(f"Lights in model: {len(lights)}")