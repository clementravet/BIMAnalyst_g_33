import ifcopenshell

def checkRule(ifc):
    pipes = ifc.by_type('IfcPipeSegment')

    result = f"Number of pipes: {len(pipes)}"

    return result
