# ASSIGNMENT 4
Group 33 - Clément, Eiður & Emma

## INTRODUCTION
The tool is used to determine a criteria of the DGNB lite certification. Our tool is finding the U-value in the external walls of the building which is coded in the IFC model. After that it compares these values and checks if they are the same and if or if not they are by DGNB certification standards.

The tool has 2 different goals: it can compare if the results from the BIM model and the report are the same or not, and then determine the DGNB criteria we choosed.

Firstly, the turorial will explain how to get started with the tool and in a second time, it will go through the code.


## HOW TO GET STARTED
This section aims to explain how to set up the coding program we need in order to use the tool.

- The first step is to download a coding program for python language. The tool has been made on Visual Studio Code, but every equivalent program may be used to run it. Once this is done, you can launch it.
- To run the code, you need to install some packgages. You have to write in the console the foloowing code lines:
  - pip install --upgrade pip
  - pip install ifcopenshell
  - pip install geometry
  - pip install tabulate


## RUN CODE
This section aims to explain how to take control of the code.

The only thing to do at this point is to change the path of the ifc file you want to study. It takes place in the 6th line: model = ifcopenshell.open(r"ifcpathfile.ifc"). At this point, you have to copy-paste the path of your ifc file in this line. When you did this, you can now run the code.



### Note:
Sometimes, some errors may pop up but they are not important and they do not disturb the result of the tool, you just need to ignore it.


