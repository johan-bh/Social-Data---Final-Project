import pandas as pd
from bokeh.models import ColumnDataSource, RadioButtonGroup, Select, CustomJS
from bokeh.plotting import figure, save
from bokeh.layouts import column
from bokeh.io import output_file
from bokeh.resources import CDN
from bokeh.transform import dodge
from bokeh.palettes import Viridis5
from bokeh.models import FactorRange
import seaborn as sns
from bokeh.colors import RGB
import warnings

warnings.filterwarnings('ignore')

# flag to determine which use case to run
use_case_1 = False

# define path and load data
# path = '/Users/benjaminfazal/Desktop/Skole/Kandidat/Semester_1/Social_data/'
path = 'C:/Users/jbh/Desktop/'
data = pd.read_csv(path + 'NYPD_Complaint_Data_Cleaned.csv')

# extract the data for specific Victim Sex
if use_case_1:
    # victim sex == F and M
    data = data[data['Victim_Sex'] != 'D']
    data = data[data['Victim_Sex'] != 'L']
    data = data[data['Victim_Sex'] != 'E']
    data = data[data['Victim_Sex'] != 'L']
    # top 5 crime types for individuals
    crime_types = ['FELONY ASSAULT', 'HARRASSMENT 2', 'PETIT LARCENY', 'GRAND LARCENY', 'ASSAULT 3 & RELATED OFFENSES']
    title = 'individuals'
else:
    # victim is a business, == D
    data = data[data['Victim_Sex'] == 'D']
    # top 5 business crime types
    crime_types = ['BURGLARY', 'GRAND LARCENY', 'PETIT LARCENY', 'ROBBERY', 'CRIMINAL MISCHIEF & RELATED OF']
    title = 'businesses'


df_focus = data[data['Offense_Description'].isin(crime_types)]

# generate descriptive statistics
df_focus['hour'] = pd.to_datetime(df_focus['Complaint_From_Time'], format='%H:%M:%S').dt.hour
df_focus['day_of_week'] = pd.to_datetime(df_focus['Complaint_From_Date']).dt.day_name()
df_focus['month'] = pd.to_datetime(df_focus['Complaint_From_Date']).dt.month_name()

# aggregating data
crime_data_aggregated = df_focus.groupby(['hour', 'Offense_Description', 'day_of_week', 'month']).size().reset_index(name='count')

# initialize data sources for each crime type
sources = {}
full_sources = {}
for crime in crime_types:
    crime_data = crime_data_aggregated[crime_data_aggregated['Offense_Description'] == crime]
    sources[crime] = ColumnDataSource(crime_data)
    full_sources[crime] = ColumnDataSource(crime_data)

# create a figure
hours = [str(h) for h in sorted(df_focus['hour'].unique())]
p = figure(x_range=hours, title=f"Hourly Crime Distribution by Day (top 5 crimes commited towards {title})",
           toolbar_location=None, tools="", y_axis_label="Crime Count", width=1010,
           y_range=(0, max(crime_data_aggregated['count']) + 100)) 

p.title.text_font_size = '14pt'

# Set the x_range more flexibly to accommodate dodging
p.x_range = FactorRange(*hours)


colors = Viridis5  # adjust the number of colors based on the number of crime types
sns_colors = sns.color_palette("viridis", len(crime_types))  # this generates RGB tuples
colors = [RGB(*[int(255 * x) for x in rgb]).to_hex() for rgb in sns_colors]

for idx, crime_type in enumerate(crime_types):
    p.vbar(x=dodge('hour', -0.2 + 0.2 * idx, range=p.x_range), top='count', width=0.185, source=sources[crime_type],
           color=colors[idx], legend_label=crime_type)

# configure legend and widgets
p.legend.location = "top_left"
p.legend.orientation = "horizontal"
p.legend.click_policy = "mute"
# p.legend.margin =  50


day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
radio_button_group = RadioButtonGroup(labels=day_of_week, active=0)  # Default: Monday
month_list = ['All'] + sorted(df_focus['month'].unique().tolist())
select_month = Select(title="Month:", value="All", options=month_list)

# javaScript callback code for updating data based on widget selections
callback_code = """
    const selected_day = days[radio_button_group.active];
    const selected_month = select_month.value;

    for (let crime in sources) {
        const source = sources[crime];
        const full_source = full_sources[crime];
        const data = full_source.data;
        const new_data = {hour: [], count: [], Offense_Description: [], day_of_week: [], month: []};

        for (let i = 0; i < data.hour.length; i++) {
            if ((selected_day === 'All' || data.day_of_week[i] === selected_day) &&
                (selected_month === 'All' || data.month[i] === selected_month)) {
                new_data.hour.push(data.hour[i]);
                new_data.count.push(data.count[i]);
                new_data.Offense_Description.push(data.Offense_Description[i]);
                new_data.day_of_week.push(data.day_of_week[i]);
                new_data.month.push(data.month[i]);
            }
        }
        source.data = new_data;
        source.change.emit();
    }
"""

# attach JavaScript callbacks
radio_button_group.js_on_change('active', CustomJS(args=dict(sources=sources, full_sources=full_sources, radio_button_group=radio_button_group, select_month=select_month, days=day_of_week), code=callback_code))
select_month.js_on_change('value', CustomJS(args=dict(sources=sources, full_sources=full_sources, radio_button_group=radio_button_group, select_month=select_month, days=day_of_week), code=callback_code))

# layout configuration
layout = column(select_month, radio_button_group, p)

# output the plot
if use_case_1:
    output_file("html_templates\interactive_plot_bokeh_case1.html", title=f"Interactive Bokeh Plot for {title}")
    save(layout, resources=CDN)

else:
    output_file("html_templates\interactive_plot_bokeh_case2.html", title=f"Interactive Bokeh Plot for {title}")
    save(layout, resources=CDN)

