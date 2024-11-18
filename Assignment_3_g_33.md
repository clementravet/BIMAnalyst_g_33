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
The managers have to change the path to the IFC file in the main.py. It is the only thing to do.

### How it works
The file main.py imports the functions in the file Finalproject.py which is located in the folder "rules". Then, the main.py calls the functions and runs them with the model that the user has chosen. 

In the file Finalproject.py, there are different functions:
- find_U_value _element: it creates a list with . There are as many elements in the list as there are different U_values in the ifc type that has been chosen. The function takes as input an element of type ifc type. The list will contain the name of the element and their U_value.
- U_value_XXX: it uses the function find_U_value_element for every ifc type we want to study.
- table_report_BIM: this function takes as input an element of type model. It creates a table with the U_values of roof, external walls, basement walls and basement slabs from the report and the BIM model. The goal is to compare the values from the 2 sources so as to see if it is consistent.
- DGNB_TEC4_4_score: this function takes as input an element of type string. It calculates the score of the DGNB criteria based on the U_value of the external walls.
- Check_DGNB: this function takes as input an element of type model. It prints the score of the DGNB criteria and says if the result from the report and the one from the BIM model are the same or not.

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
