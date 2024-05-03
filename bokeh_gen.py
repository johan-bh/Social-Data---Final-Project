import pandas as pd
from bokeh.models import ColumnDataSource, RadioButtonGroup, Select, CustomJS
from bokeh.plotting import figure, save
from bokeh.layouts import column
from bokeh.io import output_file
from bokeh.resources import CDN
from bokeh.transform import dodge
from bokeh.palettes import Viridis3
import seaborn as sns
from bokeh.colors import RGB
import warnings

warnings.filterwarnings('ignore')

# Define path and load data
path = '/Users/benjaminfazal/Desktop/Skole/Kandidat/Semester_1/Social_data/'
data = pd.read_csv(path + 'NYPD_Complaint_Data_Cleaned.csv')

# extract the data for specific Victim Sex
data = data[data['Victim_Sex'] == 'D']

# Focus crimes
crime_types = ['FRAUDS', 'CRIMINAL TRESPASS', 'BURGLARY']
# crime_types = ['FELONY ASSAULT', 'ROBBERY', 'RAPE']
df_focus = data[data['Offense_Description'].isin(crime_types)]

# Generate descriptive statistics
df_focus['hour'] = pd.to_datetime(df_focus['Complaint_From_Time'], format='%H:%M:%S').dt.hour
df_focus['day_of_week'] = pd.to_datetime(df_focus['Complaint_From_Date']).dt.day_name()
df_focus['month'] = pd.to_datetime(df_focus['Complaint_From_Date']).dt.month_name()

# Aggregating data
crime_data_aggregated = df_focus.groupby(['hour', 'Offense_Description', 'day_of_week', 'month']).size().reset_index(name='count')

# Initialize data sources for each crime type
sources = {}
full_sources = {}
for crime in crime_types:
    crime_data = crime_data_aggregated[crime_data_aggregated['Offense_Description'] == crime]
    sources[crime] = ColumnDataSource(crime_data)
    full_sources[crime] = ColumnDataSource(crime_data)

# Create a figure
hours = [str(h) for h in sorted(df_focus['hour'].unique())]
p = figure(x_range=hours, title="Hourly Crime Distribution by Day",
           toolbar_location=None, tools="", y_axis_label="Crime Count", width=800,
           y_range=(0, max(crime_data_aggregated['count']) + 5)) 

# Add bars for each crime type
colors = Viridis3  # Adjust if you have more than 3 crime types
sns_colors = sns.color_palette("hsv", 3)  # This generates RGB tuples
colors = [RGB(*[int(255 * x) for x in rgb]).to_hex() for rgb in sns_colors]

for idx, crime_type in enumerate(crime_types):
    p.vbar(x=dodge('hour', -0.25 + 0.25 * idx, range=p.x_range), top='count', width=0.2, source=sources[crime_type],
           color=colors[idx], legend_label=crime_type)

# Configure legend and widgets
p.legend.location = "top_left"
p.legend.orientation = "horizontal"
p.legend.click_policy = "mute"
day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
radio_button_group = RadioButtonGroup(labels=day_of_week, active=0)  # Default: Monday
month_list = ['All'] + sorted(df_focus['month'].unique().tolist())
select_month = Select(title="Month:", value="All", options=month_list)

# JavaScript callback code for updating data based on widget selections
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

# Attach JavaScript callbacks
radio_button_group.js_on_change('active', CustomJS(args=dict(sources=sources, full_sources=full_sources, radio_button_group=radio_button_group, select_month=select_month, days=day_of_week), code=callback_code))
select_month.js_on_change('value', CustomJS(args=dict(sources=sources, full_sources=full_sources, radio_button_group=radio_button_group, select_month=select_month, days=day_of_week), code=callback_code))

# Layout configuration
layout = column(select_month, radio_button_group, p)

# Output the plot
output_file("interactive_plot_bokeh_case2.html", title="Interactive Bokeh Plot")
save(layout, resources=CDN)
