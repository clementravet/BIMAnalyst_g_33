# Assignment 3
Group 33 - Clément, Eiður & Emma
## The Tool
As analysts we are looking into the DGNB lite certification.
In our main.py, this is the defined variable pointing to the model on our local machine:

import ifcopenshell
from .rules import pipeRule
from .rules import ventilationNameRule
from .rules import ventilationRule
model = ifcopenshell.open("path/to/ifcfile.ifc")

## About the Tool
### State the problem / claim that your tool is solving.
Seeing if the model is following the DGNB lite certification standards for U-values in external walls.

### State where you found that problem.
U-values where coded in IFCCurtainWall and addition to that we calculated the U-value by knowing the thickness of the external walls.

### Description of the tool
Our tool is finding the U-value in the external walls of the building which is coded in the IFC model. After that it compares these values and checks if they are the same and if or if not they are by DGNB certification standards.

### Instructions to run the tool.
The managers have to change the path to the IFC file

## Advanced Building Design
### What Advanced Building Design Stage (A,B,C or D) would your tool be usefuL?
In our professional opinion it could the used in B,C and D.

### Which subjects might use it?
In our professional opinion the architect's and the MEP's would want to use our tool

### What information is required in the model for your tool to work?
If the U-value is not coded already in the IFC Model, then whats needed is the thickness of the external walls, average temperature outside and inside. As well the level you want as certification in the DGNB lite standards.

## An IDS
There is inconsistancy in the materials of the elements, fx. walls, slabs, roof.
Not really clear to know which wall we are "working" on, it gives us a number but we dont know where that wall is.
The description of the elemets that compoose every wall is missing, it is considered as only one element, whereas it has to include different layers surch as the insulation for instance.
