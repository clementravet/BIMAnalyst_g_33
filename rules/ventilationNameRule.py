import ifcopenshell

def checkRule(model):
    MechanicalVentilation = model.by_type("IfcBuildingElementProxy")
    MechanicalVentilation1 = MechanicalVentilation[0]
    MechanicalVentilation2 = MechanicalVentilation[1]

    # Number of elements for the mechanical ventilation
    result = f"The first mechanical ventilation is {MechanicalVentilation1.Name} and the second one is {MechanicalVentilation2.Name}"

    return result