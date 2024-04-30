---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
title: Home
--- 

## A Data Story To Guide Citizens safely through NYC



### Intro to the datastory

Have you ever felt unsafe walking alone at night in New York City? Or perhaps you have been a victim of a crime and wish to know how to avoid the risks of it happening again? With the rise in crime rates in urban areas, it is more important than ever to be aware of the potential dangers and take steps to protect yourself. In this datastory we will explore the crime data in New York City and provide insights that can help you make informed decisions about your safety, whether you are a resident or a visitor to New York City. 

In this datastory we will use the NYPD Complaint Data Historic dataset to analyze crime patterns in New York City and identify high-risk areas and times. We will also explore the socio-economic factors that may contribute to crime rates in different neighborhoods. By understanding these patterns and trends, we can help you navigate the city safely and make informed decisions about your safety by providing you with a Safe Travel Planner (STP) that can help you avoid high-risk areas and optimize your travel routes. The NYPD Complaint Data Historic dataset [original dataset](https://data.cityofnewyork.us/d/qgea-i56i?category=Public-Safety&view_name=NYPD-Complaint-Data-Historic) from the [NYC Open Data](https://opendata.cityofnewyork.us/) website, contains all valid felony, misdemeanor, and violation crimes reported in New York City between the start of 2006 and April 2024. It covers a wide range of crimes types and severity, location, date, time, victim and suspect demographics, and more. 


### Data Visualizations: Focus Crimes
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur a bibendum arcu. Donec sodales lorem dui, vitae vehicula augue rhoncus vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus vel mollis diam, non pellentesque purus. Aliquam id dui consequat, posuere est ut, rutrum augue. Nullam sit amet ornare neque. Nunc urna felis, vestibulum eu varius sed, elementum vel turpis. Nunc ante magna, venenatis ultrices arcu sit amet, mollis auctor eros.


### Socio Economic Overlays
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur a bibendum arcu. Donec sodales lorem dui, vitae vehicula augue rhoncus vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus vel mollis diam, non pellentesque purus. Aliquam id dui consequat, posuere est ut, rutrum augue. Nullam sit amet ornare neque. Nunc urna felis, vestibulum eu varius sed, elementum vel turpis. Nunc ante magna, venenatis ultrices arcu sit amet, mollis auctor eros.

Donec rutrum ex vitae augue condimentum tristique. Pellentesque rutrum nec risus sed luctus. Quisque laoreet est in blandit ullamcorper. Aliquam erat volutpat. Nullam luctus sodales sapien fermentum posuere. Quisque dapibus massa a mi dignissim elementum. Fusce ultrices purus at dapibus lobortis. Vivamus accumsan est vitae varius iaculis. Ut eu blandit est, ut egestas enim. Etiam feugiat vitae ipsum sit amet consectetur. Proin ante lacus, aliquet at vestibulum eu, venenatis sed orci. Donec volutpat iaculis sapien, et maximus libero venenatis eget. Nulla ornare mauris vel porta feugiat. Proin sed lobortis ante. Fusce imperdiet quam non augue placerat cursus. Sed dapibus a nunc id pellentesque.

<iframe src="heatmap.html" width="100%" height="800px"></iframe>



### Explore Safely with STP - Your Safe Travel Planner for New York City

Introducing the STP model, a practical solution designed to enhance urban navigation for New York City residents. As a prototype poised for future development, the Safe Travel Planner offers a strategic approach to travel, combining safety with convenience. This tool is tailored to help users plan their journeys effectively, integrating historic data and machine learning to avoid hazards and optimize travel routes.

STP is still a prototype but could be built to scale in the future. Consider the following two scenarios, which illustrate just how versatile and necessary the STP can be for different individuals:


**Use Case 1:**  
You are a 20yr woman leaving a lavish bachelorette party at “X” bar in downtown Manhattan. Its 01:30 on a chilly Friday 13th May 2018. After a night of celebrating and spending all your cash on drinks, you find yourself unable to afford a taxi home to  “address”, Bronx. The thought of walking home alone, with the possibility of assault or harassment from “dark figures in the night” scares you. Getting home safely is your main concern. Luckily you have your travel card with you.
Suggest a travel route which avoids certain high-risk areas. 

The focus crimes are given by the user
User: particularly afraid of X crimes {rape, harrasment 1, etc}

Suggestions like 
    - Don't take the subway from this station, but instead {bus, walk}
    - Avoid this street and intersection
    - Walk on main streets (with good lighting?) instead of alleyways

(We have Suspect {AgeGroup, Race, Sex}, as well as Victim {AgeGroup, Race, Sex} for at least like 30%)


<iframe src="/heatmap2.html" style="width:100%; height:600px;" frameborder="0"></iframe>
<br/>



**Use Case 2:**
Your car was recently vandalized and you cant afford more vehicle repairs. You have to show up for work at McDonald’s to work a night shift during the weekend - it’s the 1st of april 2018 in the time period 22:00-6:00. You’re allowed to choose which McDonald's store you want to work at in Brooklyn. You suffer from bad arthritis and thus have trouble walking further than 1 mile. 
Your usual spot at the nearby paid parking lot is completely full, and the next closest paid porking lot is too far away. Separately from your car being vandalized or stolen, you are afraid of assault and burglary. Where should you park on the street?


What part of Bronx?
- Suggest parking area