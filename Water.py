#################################WATER#################################

import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.selector

ifc = ifcopenshell.open('/Users/eidursnaer/Desktop/dtu/BIM/LLYN - VVS.ifc')

pipes = ifc.by_type('IfcPipeSegment')

#pipe_types = set()

# Loop through all pipes and collect their types
#for pipe in pipes:  # Add the missing colon here
    # Fix extra comma in hasattr
    #if hasattr(pipe, 'PredefinedType') and pipe.PredefinedType:
        #pipe_types.add(pipe.PredefinedType)

# Convert the set to a list (if you need it as a list)
#pipe_types_list = list(pipe_types)


result = (f"Number of pipes: {len(pipes)}")
print(result)
#print("Different types of pipes in the model:", pipe_types_list)



############################VENTILATION##############################

#import ifcopenshell
#import ifcopenshell.util
#import ifcopenshell.util.selector
#ifcvent = ifcopenshell.open('/Users/eidursnaer/Desktop/dtu/BIM/LLYN - VENT.ifc')

#def checkRule = (ifcvent)
    #ventilation = ifcvent.by_file ('Ifc')