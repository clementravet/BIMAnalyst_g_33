# ASSIGNMENT 4
Group 33 - Clément, Eiður & Emma

## INTRODUCTION - Focus area and BIM use
With our focus area of "Materials", we have developed a tool, which can be used to ease the DGNB-certification process and determine a criteria of the DGNB lite certification. The DGNB criteria which the tool can be used to determine is: TEC4.4 Quality of the building envelope 
The tools main purpose is to find the U-value in the external walls of the building, which is coded in the IFC model, and then compare these with the calculated U-values by the MEP engineers. The tool will then calculate whether the correct DGNB-points have been given to the criteria. 

Summarized, the tool has 2 different uses: it can compare if the results from the BIM model and the report are the same or not, and then determine which DGNB criteria points is given.

Firstly, the turorial will explain how to get started with the tool and secondly, it will go through the code.


## ROLE IDENTIFICATION
Our tool can be used for different purposes with some modification. 
It is possible for the tool to be used by the role of "Modeller Level 1 and Level 2", as it can be used to check whether the model is modelled correct or that the mapping of the modelled properties is done correctly - here with the U-values as a reference, which can be usefull to check if the layers or materials of walls, slabs, roof etc. is correct.
But the tool is mostly relevant for the role of "Analyst Level 2" since its primary use to analyse the properties of a standard IFC file and extract the essential properties with Pyhton script.


## HOW TO GET STARTED
This section aims to explain how to set up the coding program we need in order to use the tool.

- The first step is to download a coding program for python language. The tool has been made on Visual Studio Code, but every equivalent program may be used to run it. Once this is done, you can launch it.
- To run the code, you need to install some packgages. You have to write in the console the folowing code lines:
  - pip install --upgrade pip
  - pip install ifcopenshell
  - pip install geometry
  - pip install tabulate


## RUN CODE
This section aims to explain how to take control of the code.

The only thing to do at this point is to change the path of the ifc file you want to study. It takes place in the 6th line: model = ifcopenshell.open(r"ifcpathfile.ifc"). At this point, you have to copy-paste the path of your ifc file in this line. When you did this, you can now run the code.


### Note:
Sometimes, some errors may pop up but they are not important and they do not disturb the result of the tool, you just need to ignore it.
