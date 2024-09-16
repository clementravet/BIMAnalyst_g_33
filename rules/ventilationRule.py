import ifcopenshell

def checkRule(model):
    MechanicalVentilation = model.by_type("IfcBuildingElementProxy")
    
    # Number of elements for the mechanical ventilation
    result = f"There are {len(MechanicalVentilation)} mechanical ventilation systems"

    return result

