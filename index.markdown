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
In New York City, certain crimes are more prominent and can pose a greater risk to your safety while travelling or your business operations. It is crucial to be aware of these crimes and take precautions to avoid them. To give an overview, see the bar chart below which shows the daily average count of 8 travel-related crimes towards people (left) and 8 business-related crimes (right). We see that less severe crimes such as petit larceny and harassment are more common in comparison to severe crimes such as sex crimes and rape.
<img src="daily_average_crime_comparison.png" width="100%">

Certain crimes are more prevalent on specific hours of the day. These temporal changes are significant, as travelling at night can be more dangerous than during the day. 
<img src="hourly_crime_counts.png" width="80%">
Severe crimes such as rape and sex crimes are more likely to occur at midnight. Which could suggest to avoid travelling alone or with strangers at night if possible. 


### UrbanShield NYC - Your Essential Navigation Partner for Safety in New York City

Introducing **UrbanShield NYC**, a pioneering navigation solution tailored for New York City dwellers and business owners. This tool enhances urban mobility by integrating historical crime data with data analysis and advanced navigation tools to provide optimized and safe travel routes and locations. Whether you need to navigate the city late at night or are looking to relocate your business, UrbanShield NYC is designed to assist in planning safer journeys and making informed location decisions.

UrbanShield NYC is still in the prototype phase but shows promising potential for future development and scalability. Explore how UrbanShield NYC addresses two distinct needs through the following use cases:


#### Use Case 1: Getting home safe in the night
You are a man/woman leaving a lavish party at “X” bar in downtown Manhattan. Its 01:30 on a chilly Friday 13th. After a night of celebrating and spending all your cash on drinks, you find yourself unable to afford a taxi home to  “address”, Bronx. The thought of walking home alone, with the possibility of assault or harassment from “dark figures in the night” scares you. Getting home safely is your main concern. Luckily, group 17 of the Social Viz course has developed an safe travel planner that enables users to find a safe route home. In the interactive map below the user can enter the time of day, day of week as well as navigational inputs which yields a route suggestion drawn on a heatmap of Robbery, Felony Assaul, and Rape - crimes we envision most individuals want to steer clear of on their way home from a part.

**How to use the UrbanShield Navigator:** 
- Adjust time accordingly
- Enter start (e.g. "Lower East Side, NYC") and destination address (e.g "Upper East Side, NYC) - specific addresses works just fine too
- Click draw route
- Drag route to avoid hotspots or change start/end location

<iframe src="/heatmap2.html" style="width:100%; height:600px;" frameborder="0"></iframe>
<br/>

For a more quantative visualization, please use the following interactive plot to get an overview of varying crimes which we deemed of high interest for your specific case. 

<iframe src="/interactive_plot_bokeh_case1.html" style="width:100%; height:720px;" frameborder="0"></iframe>

#### Use Case 2: Finding a good business location

A business owner, having experienced repeated vandalism at their current location, is exploring new locations for their business in New York City. Their priority is to find an area with lower crime rates to ensure the safety and security of the business. This decision-making process involves scouting various neighborhoods across NYC, comparing historical crime statistics, and considering factors like accessibility and visibility to minimize future risks of vandalism or theft. The goal is to identify a location that not only promises a thriving business environment but also ensures a safe space for their operations. We can help business owners avoid hotspots for crimes commited towards businesses. Furthermore, we have added a vast number of socioeconomic features on a Borough-level which might be of interest.

**How to use the UrbanShield Business Locator:**
- Adjust the year accordingly on the slider in the top left corner
- Select crimes of interest in the multiselect button in the top left corner
- Drag the potential business markers to locations of interest
- Zoom and interact with the map to investigate further
- Conduct further investigations by selecting various miscellaneous socioeconomic features in the top right corner

<iframe src="/usecase2.html" style="width:100%; height:600px;" frameborder="0"></iframe>

For a more quantative visualization, please use the following interactive plot to get an overview of varying crimes which we deemed of high interest for your specific case. 

<iframe src="/interactive_plot_bokeh_case2.html" style="width:100%; height:720px;" frameborder="0"></iframe>

<br/><br/><br/>

### Socio Economic Overlays
On a more general note, we wish to emphasize that this should not be viewed solely as a critique of the individuals who commit such crimes. A significant body of research has demonstrated that increases in criminal activity are strongly linked to socio-economic factors. For example, a paper published in the Journal of Economic Structures in 2020, titled "Dynamic Linkages between Poverty, Inequality, Crime, and Social Expenditures in a Panel of 16 Countries: Two-Step GMM Estimates," establishes a causal relationship between poverty and crime. Similarly, a paper by a Ph.D. student at the University of Texas Rio Grande Valley, titled "Education and Crime," underscores the link between lower educational levels and increased criminal activity.

As a collective, we have used data on poverty and total enrollment counts from various boroughs in NYC between 2013 and 2018 to highlight social issues that may be contributing to the crime rate we are observing. Initially, we explored the relationship between early total enrollment in educational institutions and the number of individuals living in poverty by fitting a linear regression model, with poverty as the dependent variable. Furthermore, the correlation coefficient between these two variables was calculated to be 0.9827. These calculations were conducted in hopes of illustrating a connection between two social issues that, as described in the referenced papers, are seen as catalysts for higher criminal activity.

<!-- Replace the iframe with this img tag -->
<img src="Linear_fit_EP.png" alt="Linear Fit Plot" style="width:100%; height:auto;">


The linear fit, with an R^2 value of 0.92, shows a strong linear relationship between the variables. Moreover, the occurrence and probability of poverty can be visualized by the following bar plots:

<img src="P_poverty.png" width="100%">

<br/><br/>

<img src="P_poverty_norm.png" width="100%">
The first bar plot depicts the proportion of individuals living below the poverty line in the various boroughs, and the normalized plot is created for comparative purposes. Apart from the Bronx and Brooklyn having the two highest probabilities of an individual being under the poverty line, a general trend regarding poverty in NYC's boroughs becomes quite clear. None of the boroughs hold a poverty percentage below 50%, which is predominantly higher when compared to the average European country — see (https://www.euro.centre.org/downloads/detail/1302) for reference.

Naturally, this should be compared against the number of reported crimes per citizen in each borough.

<img src="Crimes_per_ind.png" width="100%">

Here, we see that the Bronx and Brooklyn have the first and third highest crimes per individual in their respective boroughs. This trend largely follows the earlier referenced papers when compared to the highlighted social data analysis for poverty and total enrollment.

This segment hereby highlights potential socially-themed societal problems that may underlie the crime-specific issues this page addresses. We hope this will broaden the users' understanding and potentially reduce prejudice regarding the issue which we call crime.

<!-- <iframe src="heatmap.html" width="100%" height="800px"></iframe> -->

<br/><br/><br/>