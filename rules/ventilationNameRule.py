import ifcopenshell

def checkRule(model):
    MechanicalVentilation = model.by_type("IfcBuildingElementProxy")
    MechanicalVentilation1 = MechanicalVentilation[0]
    MechanicalVentilation2 = MechanicalVentilation[1]

    # Number of elements for the mechanical ventilation
    result = f"The first mechanical ventilation is {len(MechanicalVentilation1.Name)} and the second one is {len(MechanicalVentilation2.Name)}"

    return result