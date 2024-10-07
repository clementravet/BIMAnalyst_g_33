# Introduction
Our group is composed of 3 students who are more or less familiar with coding in python.

” I am confident coding in python? ”:
- Emma: 1 Disagree
- Eidur: 2 Neutral
- Clément: 3 Agree

Our group’s focus is Materials. We are a group of analysts. We decided to work on a label that allows us to assess the environmental aspect of a building through the materials that compose it. That’s why we will focus on the DGNB Certification System.



# DGNB system
The DGNB Certification System is a comprehensive framework developed by the German Sustainable Building Council (Deutsche Gesellschaft für Nachhaltiges Bauen), to evaluate and certify the sustainability of buildings, neighborhoods, and urban districts. Established in 2007, DGNB has become one of the leading sustainability certification systemsworldwide, renowned for its holistic approach that integrates environmental, economic, sociocultural, and functional aspects of sustainability. The DGNB certification is a voluntary system designed to evaluate, collaborate on, and promote sustainability across the built environment. From building interiors to entire urban districts, DGNB supports decisions that improve conditions for the environment, people, and society. There are currently five types of certification, each based on various criteria that assess buildings, renovations, constructions, or urban areas according to social, environmental, and economic factors. DGNB addresses topics such as biodiversity, indoor climate, harmful chemicals, CO2 footprint, social conditions, and durability. The points in DGNBlite may not fully align with the official DGNB guidelines; for instance, certain criteria are given more weight based on their relevance to the learning objectives, and the entire SITE topic has been excluded to fit the course scope. However, the overall concept for achieving a certified level remains unchanged.
- Platinum: Scoring an overall 80% with each topic scoring at least 65%
- Gold: Scoring an overall 65% with each topic scoring at least 50%
- Silver: Scoring an overall 50% with each topic scoring at least 35%

The maximum possible point of DGNBlite is 2200, which gives 1760, 1430, 1100 and 770 the threshold points respectively for each level. As seen on figure 2.1 here below how many points are distributed for each category.



# Use case
## Identification of the claim
We decided to work on the report of the building 2406 from last year’s Advanced Building Design Course. We want to focus on the DGNB Certification System, we will focus on particular criteria of this label. Firstly, we will focus on the TEC4.4 DGNBlite indicator. This indicator correspond to the quality of the building envelope. To do so, we need the Uvalue of exterior walls. The criteria for the Uvalues is explained here below:

TEC4.4 – Quality of the building envelope (C) Points total: 50pts
- Lv1: Average Uvalue of exterior wall < min. Building Regulation requirement 20pts
- Lv2: Average Uvalue of exterior wall < 15% of min. Building Regulation requirement 30pts
- Lv3: Average Uvalue of exterior wall < 30% of min. Building Regulation requirement 50pts

We choosed to focus on this criteria because we think it can be a very useful tool for the future. It can enable to save a lot of time in preparing the report.


## Use case description
In order to check the claim, we have to get some data from the BIM model. We will focus on the Architectural BIM Model, but the Structural BIM Model and the MEP BIM Model may be still useful. We will collect data such as the U-value of the exterial-walls when it is possible. If it is not, we can get the thickness of the walls and the material it is made of to calculate the U-value. This claim needs to be checked before the writing of the report. The goal is to check if the project respects the chosen criteria from the DGNB Certification defined at the begining of the project. The BIM purpose is to analyse the data from the BIM model and determine the indicator from the DGNB Certification System.

The BIM model that is the closest to ours is the Sustainibility Analysis. Here is our BPMN diagram:
![Tool_diagram](https://github.com/user-attachments/assets/10904bb3-750a-4953-b893-ad6b3b4a364d)


## Tool Idea
What we want to execute from our tool is, first to identify the exterial-walls of our building. Secondly, we want to determine the U-value of each exterial wall for it selfs and if some information is missing, then find out what is missing and calculate the U-value for that particular wall. Third is gathering all the U-values of all the exterial walls in the building. The fourth and last step is to determine which indicator the project has from the DGNB Certification System.


## Information Requirements
We have two options when it comes to extract the information from the model, we can either extract it straight from the IFC from the external walls information or we can find out the thickness of the wall and the material composition of the wall to calculate the U-value our selfs. 
This information is in the model, either the U-value or the thickness and materials
Yes we know how to get in IfcOpenShell, the model type we will be using is " IfcCurtainWall ". For now we know how to get all the information by util.element.get_psets(wall).

## Software Licence



