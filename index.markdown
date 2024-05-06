---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
title: Home
--- 


## Crime in New York City: A Data-Driven Approach to Safety and Navigation

### Are you safe in the city that never sleeps?

Have you ever felt unsafe walking alone at night? Or ever been worried if your business is in a high-crime area? Or perhaps you have been a victim of a crime and wish to know how to avoid the risks of it happening again? With the rise in crime rates in urban areas, it is more important than ever to be aware of the potential dangers and to take steps to protect yourself. Whether you're a long-time resident, a visitor, or a business owner, it's essential to understand the crime patterns in order to make informed decisions. 

In this datastory we will uncover the trends of crime data in New York City using the NYPD Complaint Data Historic dataset. We will explore the most common crimes related to travel and business, the times and locations they occur, and the socio-economic factors that may contribute to crime rates in different neighborhoods. We will provide you with a tool called UrbanShield NYC that can help you avoid high-risk areas and optimize your travel routes to keep yourself and your business safe. The NYPD Complaint Data Historic dataset [original dataset](https://data.cityofnewyork.us/d/qgea-i56i?category=Public-Safety&view_name=NYPD-Complaint-Data-Historic) from the [NYC Open Data](https://opendata.cityofnewyork.us/) website, contains all valid felony, misdemeanor, and violation crimes reported in New York City between the start of 2006 and April 2024. It covers a wide range of crimes types and severity, location, date, time, victim and suspect demographics, and more. We have thoroughly cleaned this dataset to ensure that the data is accurate and as fair as possible for our analysis, notably by only focusing on years 2006 to 2022 due to inconsistent data.

### Which crimes should you look out for?
In New York City, certain crimes are more prominent and can pose a greater risk to your safety while travelling or your business operations. It is crucial to be aware of these crimes and take precautions to avoid them. To give an overview, see the bar chart below which shows the daily average count of 8 of the most common travel-related crimes towards people (left) and 8 business-related crimes (right). 
<img src="figures/daily_average_crime_comparison.png" width="100%">
For travel-related crimes, we see that less severe crimes such as petit larceny and harassment are more common in comparison to severe crimes such as sex crimes and rape. For most companies, the main daily concern is petty theft due to shoplifting, whereas more damaging crimes like Burglary and Robbery happen less often. 

There are many precautions one can take to avoid the risk of specific crimes such as reducing petit larceny in retail by installing more visible [security cameras](https://www.bttcomms.com/combating-retail-theft-how-to-use-advanced-security-cameras-to-prevent-shoplifting/) in the store or [hiring security guards](https://www.dailymail.co.uk/news/article-10498885/Owner-NYC-grocery-store-chain-Gristedes-hires-security-guards-crack-shoplifting.html), which is one measure NYC Mayor Eric Adams has [proposed](https://www.nyc.gov/office-of-the-mayor/news/340-23/mayor-adams-plan-combat-retail-theft-new-york-city#/0) in his neighbourhood retail watch to combat the rise in retail theft.

Temporal changes are also important to consider, as certain crimes are more prevalent on specific hours of the day. 
Adding caption saying 'Figure 3: Line plot showing the hourly distribution of travel-related crimes in NYC.'
<div style="display: flex; justify-content: center; align-items: center;">
    <img src="figures/hourly_crime_counts.png" style="height: 350px; width: auto; margin: 0;">
    <img src="figures/hourly_polar_plot.png" style="height: 350px; width: auto; margin: 0;">
</div>
Looking at crimes towards people on the line plot, we can observe that travelling at night can be more dangerous than during the day for crimes such as rape and sex crimes which are more likely to occur at midnight. However, harassment is far more likely to occur during the day between 8am and 8pm, as supported by the polar plot. 

<br/>
### UrbanShield NYC - Your Essential Navigation Partner for Safety in New York City

Introducing **UrbanShield NYC**, a pioneering navigation solution tailored for New York City dwellers and business owners. This tool enhances urban mobility by integrating historical crime data with data analysis and advanced navigation tools to provide optimized and safe travel routes and locations. Whether you need to navigate the city late at night or are looking to relocate your business, UrbanShield NYC is designed to assist in planning safer journeys and making informed location decisions.

UrbanShield NYC is still in the prototype phase but shows promising potential for future development and scalability. Explore how UrbanShield NYC addresses two distinct needs through the following use cases:


#### Use Case 1: Getting home safe in the night
You are a man/woman leaving a lavish party at bar in downtown Manhattan. Its 02:00 on a chilly Friday. After a night of celebrating and spending all your cash on drinks, you find yourself unable to afford a taxi home to the Bronx. The thought of walking home alone, with the possibility of assault or harassment from dark figures in the night scares you. Getting home safely is your main concern. Luckily, group 17 of the Social Viz course has developed a tool that enables users to find a safe route home. In the interactive map below you can enter the time of day, day of week, your sex assigned at birth as well as navigational inputs which yields a suggested route drawn on a heatmap. This heatmap is based which crimes you are especially interested in avoiding. The available crimes are ones we envision most individuals want to steer clear of on their way home from a part. This suggested route can be adjusted by the user to avoid crime hotspots. Furthermore, we have added markers at the locations of the 77 NYPD precincts which might be useful to a citizen navigating a dangerous city.

**How to use the UrbanShield Navigator:** 
- Adjust time accordingly
- Select your sex
- Select the crimes that you most want to avoid
- Enter start (e.g. "Lower East Side, NYC") and destination address (e.g "Upper East Side, NYC") - specific addresses works just fine too
- Click draw route
- Drag route to avoid hotspots or change start/end location
- Toggle the NYDP precints to see their locations

<iframe src="/html_templates/usecase1.html" style="width:100%; height:600px;" frameborder="0"></iframe>
<br/>


In an urban landscape as complex and dynamic as New York City, navigating the streets at night can be daunting, particularly after social events where personal safety becomes a paramount concern. Our **UrbanShield NYC** navigator specifically addresses this issue by providing a user-friendly tool that dynamically suggests safer travel routes based on historical crime data. By inputting a start and destination address along with the time and day of travel, users can visually assess and modify their route to avoid areas frequently associated with crimes such as robbery, felony assault, and other violent offenses.

This tool is particularly beneficial for individuals who may find themselves in unfamiliar parts of the city or those who are vulnerable late at night, offering peace of mind through tailored navigational advice that prioritizes safety.

**Illumination on Urban Safety Issues:**
Use Case 1 shines a light on the broader issues of urban safety and the uneven geographical distribution of crime within the city. By mapping crime hotspots against user-directed routes, it not only aids in immediate personal safety but also raises awareness about the areas with heightened risks. This can foster a greater understanding among city dwellers and visitors about the dynamics of urban crime, potentially influencing habits and decisions regarding nightlife and travel.

#### Limitations and Considerations:
While **UrbanShield NYC** provides an innovative approach to enhancing nighttime safety, there are inherent limitations to consider:

1. **Accuracy of Crime Data**: The geolocation of certain crimes in the NYPD dataset is not always exact, as locations are often reported at the nearest police precinct to maintain victim anonymity. I.e the footnotes of the NYDP complaint dataset states that rape incidents are geolocated at the nearest NYDP precint. This can lead to a slight distortion in crime mapping, potentially affecting the accuracy of the suggested safe routes. If you select rape as the crime of interest (and female since there's more female victims) and toggle on the NYDP markers you'll see that there all hotspots are next to a NYPD precinct. Thus, while you'd intuitively steer clear of the red spots but in specific instance you might actually be safer going through them.

2. **Changing Criminal Patterns**: Criminals may adapt their strategies in response to shifts in public behavior influenced by tools like ours or through the use of predictive policing strategies. This could lead to changes in crime patterns over time, which means continuous updates and model recalibrations are necessary to maintain the tool's effectiveness.

3. **Data and Privacy Concerns**: Utilizing crime data to navigate the city also raises questions about privacy and the ethical use of data. It is vital to ensure that the application respects user privacy and data security, particularly in how location and navigational data are handled.

4. **Over-reliance on Technology**: There is a risk of over-reliance on technological solutions for safety. Users should remain aware and vigilant, using the tool as a supplement to, rather than a replacement for, personal judgment and situational awareness.

**UrbanShield NYC's** navigator for getting home safe at night represents a significant step forward in leveraging data for public safety. However, it is crucial that users understand both its strengths and its limitations. As we continue to refine the tool, feedback and ongoing analysis will be key in enhancing its precision and reliability, ensuring that it remains a valuable resource for navigating New York City safely.
While the crime "hotspots" cannot fully avoided when navigating the city the map shines a light general areas to avoid at certain times of the day.
According to an article written by ['Building Security Services (BSS)'](https://www.buildingsecurity.com/blog/the-most-dangerous-neighborhoods-in-nyc/) the two most dangerous streets of Manhattan are 125th Street and Lexington Ave. If you were to select the top 5 crimes in the dropdown menu, set the time to nighttime and zoom out you would see a clear hotspots where there's dysproportionately many incidents in these exact areas. Heatmaps are great for showcasing a lot of information in a digestible manner but sometimes it can be beneficial to see a more quantitative visualization. To do so, please use the following interactive bar plot to get an overview of a handful of crimes which we deemed of especially high interest for your specific case. 

<iframe src="/html_templates/interactive_plot_bokeh_case1.html" style="width:100%; height:720px;" frameborder="0"></iframe>

### Write some comments here (Benja)

#### Use Case 2: Finding a good business location

A business owner, having experienced repeated vandalism at their current location, is exploring new locations for their business in New York City. Their priority is to find an area with lower crime rates to ensure the safety and security of the business. This decision-making process involves scouting various neighborhoods across NYC, comparing historical crime statistics, and considering factors like accessibility and visibility to minimize future risks of vandalism or theft. The goal is to identify a location that not only promises a thriving business environment but also ensures a safe space for their operations. We can help business owners avoid hotspots for crimes commited towards businesses. Furthermore, we have added a vast number of socioeconomic features on a Borough-level which might be of interest.

**How to use the UrbanShield Business Locator:**
- Adjust the year accordingly on the slider in the top left corner
- Select crimes of interest in the multi-select button in the top left corner
- Drag the potential business markers to locations of interest
- Zoom and interact with the map to investigate further
- Conduct further investigations by selecting various miscellaneous socioeconomic features in the top right corner (lighter color indicates higher value)

<iframe src="/html_templates/usecase2.html" style="width:100%; height:600px;" frameborder="0"></iframe>

The interative bar plot below gives a more detailed overview of some crimes you are most interested in avoiding.
Navigating the business landscape in New York City requires not only a keen sense of market dynamics but also an awareness of safety and security issues. **UrbanShield NYC** assists business owners in identifying optimal locations for their enterprises by analyzing historical crime data alongside socioeconomic factors. By using this tool, entrepreneurs can compare different neighborhoods for crime rates and other relevant data, enabling them to make informed decisions about where to establish or relocate their businesses to minimize risk.

This proactive approach to site selection is especially useful for business owners who have experienced issues such as vandalism or theft, or for new entrepreneurs who wish to avoid such challenges from the outset.

#### Illumination on Business Safety and Security:
Use Case 2 casts light on the critical need for businesses to consider safety and security as part of their location strategy. It emphasizes the importance of understanding the local crime landscape and how it intersects with business operations. The tool not only provides data on common crimes affecting businesses, such as theft and vandalism, but it also integrates socioeconomic indicators that may influence crime rates, such as poverty levels and educational attainment.

#### Limitations and Considerations:
Despite the advantages of **UrbanShield NYC**, there are several limitations that users should be aware of:

1. **Data Accuracy and Timeliness**: The tool relies on historical crime data, which may not fully capture current trends or emerging patterns. Business owners should consider this tool as one part of a comprehensive due diligence process.

2. **Dynamic Crime Patterns**: As with residential safety, business-related crime patterns can shift over time. Factors such as new police strategies, changes in neighborhood demographics, or even other businesses moving into or out of an area can affect local crime rates. Continuous monitoring and adaptation are required to respond to these changes effectively.

3. **Socioeconomic Data Integration**: While socioeconomic data provides valuable context, these indicators can be complex and require nuanced interpretation. Users should consider additional sources and expert analysis to fully understand the implications of this data on business safety.

4. **Potential for Displacement and Gentrification**: Utilizing crime data to choose business locations can inadvertently contribute to gentrification, potentially displacing existing communities. Business owners should consider the broader social impacts of their location choices.


**UrbanShield NYC** is designed to empower business owners with data-driven insights for selecting safe and prosperous business locations in New York City. While the tool offers a robust basis for decision-making, it is vital for users to maintain an informed perspective by considering additional current and localized information. As the landscape of New York City continues to evolve, so too should the strategies for choosing the safest and most viable locations for business operations. The socioeconomic features are only a small subset of data points that might be of interest to a business owner. We encourage users to investigate the usefulness of the features and what conclusions you can draw from them.

#### can we find a link on business vandalism or problems with shoplifting etc, i know they changed the laws in the USA such that stealing under a certain amount isnt a severe felony

<iframe src="/html_templates/interactive_plot_bokeh_case2.html" style="width:100%; height:720px;" frameborder="0"></iframe>

### Write some comments here
<br/>

### Socio Economic Overlays
On a more general note, we wish to emphasize that this should not be viewed solely as a critique of the individuals who commit such crimes. A significant body of research has demonstrated that increases in criminal activity are strongly linked to socio-economic factors. For example, a [paper](https://www.researchgate.net/publication/341956879_Dynamic_linkages_between_poverty_inequality_crime_and_social_expenditures_in_a_panel_of_16_countries_two-step_GMM_estimates) published in the Journal of Economic Structures in 2020, titled "Dynamic Linkages between Poverty, Inequality, Crime, and Social Expenditures in a Panel of 16 Countries: Two-Step GMM Estimates,"  establishes a causal relationship between poverty and crime. Similarly, a [paper](https://scholarworks.utrgv.edu/cgi/viewcontent.cgi?article=1064&context=cj_fac) by a Ph.D. student at the University of Texas Rio Grande Valley, titled "Education and Crime,"  underscores the link between lower educational levels and increased criminal activity.

As a collective, we have used [data](https://data.cityofnewyork.us/Education/2013-2018-Demographic-Snapshot-Borough/v9z6-t6nq/about_data) on poverty and total enrollment counts from various boroughs in NYC between 2013 and 2018 to highlight social issues that may be contributing to the crime rate we are observing. Initially, we explored the relationship between early total enrollment in educational institutions and the number of individuals living in poverty by fitting a linear regression model, with poverty as the dependent variable. Furthermore, the correlation coefficient between these two variables was calculated to be 0.9827. These calculations were conducted in hopes of illustrating a connection between two social issues that, as described in the referenced papers, are seen as catalysts for higher criminal activity.

The linear fit, with an R^2 value of 0.92, shows a strong linear relationship between the variables, as shown in figure 1. Moreover, the occurrence and probability of poverty can be visualized by figure 2 and 3:

The first bar plot depicts the proportion of individuals living below the poverty line in the various boroughs, and the normalized plot is created for comparative purposes. Apart from the Bronx and Brooklyn having the two highest probabilities of an individual being under the poverty line, a general trend regarding poverty in NYC's boroughs becomes quite clear. None of the boroughs hold a poverty percentage below 50%, which is predominantly higher when compared to the average European country — see [source](https://www.euro.centre.org/downloads/detail/1302) for reference.

Naturally, this should be compared against the number of reported crimes per citizen in each borough.

<img src="figures/multiple_plots.png" width="100%">

Here, we see that the Bronx and Brooklyn have the first and third highest crimes per individual in their respective boroughs, as visualized in figure 4. This trend largely follows the earlier referenced papers when compared to the highlighted social data analysis for poverty and total enrollment.

This segment hereby highlights potential socially-themed societal problems that may underlie the crime-specific issues this page addresses. We hope this will broaden the users' understanding and potentially reduce prejudice regarding the issue which we call crime.

### Summary

As shown in this data story, crime in New York City is a complex issue which has some overall identifiable trends such as specific crimes are more common during certain hours of the day, or in certain neighborhoods. However, the underlying causes of crimes can be deceptively difficult to pinpoint. By incorporating socio-economic data, we can see that there is a strong correlation between poverty and crime rates, indicating that crime is a multifaceted issue. This is why NYC Mayor Eric Adams has recently proposed a [holistic approach](https://www.cbsnews.com/newyork/news/watch-live-mayor-eric-adams-to-hold-public-safety-briefing-with-gov-kathy-hochul-attorney-general-letitia-james/) to combat the some of root causes of crime, especially in specific boroughs in the Bronx and Brooklyn.

As products similar to our UrbanShield NYC tool are popularised and integrated into society through safer travel planning apps or business location scouting tools, we hope to see a reduction in crime rates and an increase in safety and security for all New Yorkers. However, since this tool is accessible to all citizens, including criminals, this may instead just shift the locations of crimes and introduce new biases into the future crime data.


<br/><br/><br/>