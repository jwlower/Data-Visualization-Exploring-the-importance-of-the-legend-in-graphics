import csv
import pandas as pd
import os
import numpy as np
#bokeh stuff
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel

"""
NOTES
https://www.ovg.ox.ac.uk/news/herd-immunity-how-does-it-work

90-95% needed to have successful herd immunity for meesels
80%-85% needed for polio
"""


# Prepare the data
geoData = pd.read_csv('geoData.csv')
studentData = pd.read_csv('studentData.csv',encoding = "ISO-8859-1")
studat = studentData.sort_values(by=['school_code','year'])
#nPBE = permenant belief exceptions
#nPME = permenant medical exceptions
no_vacc = studat[['n','nMMR','nDTP','nPolio','nPBE','nPME','year']]
no_vacc = (no_vacc.sort_values(by=(['year'])))
years = np.arange(2000,2016)
print(years)
total = []
total_MMR_vulnerable = []
total_DTP_vulnerable = []
total_Polio_vulnerable = []
percent_MMR_vulnerable = []
percent_DTP_vulnerable = []
percent_Polio_vulnerable = []

for year in years:
    print(year)
    total.append(no_vacc[no_vacc['year']==year]['n'].sum())

    total_MMR_vulnerable.append(no_vacc[no_vacc['year']==year]['n'].sum() - no_vacc[no_vacc['year']==year]['nMMR'].sum())
    total_DTP_vulnerable.append(no_vacc[no_vacc['year']==year]['n'].sum() - no_vacc[no_vacc['year']==year]['nDTP'].sum())
    total_Polio_vulnerable.append(no_vacc[no_vacc['year']==year]['n'].sum() - no_vacc[no_vacc['year']==year]['nPolio'].sum())
    """
    percent_MMR_vulnerable.append(no_vacc[no_vacc['year']==year]['n'].sum()/no_vacc[no_vacc['year']==year]['nMMR'].sum())
    percent_DTP_vulnerable.append(no_vacc[no_vacc['year']==year]['n'].sum()/no_vacc[no_vacc['year']==year]['nDTP'].sum())
    percent_Polio_vulnerable.append(no_vacc[no_vacc['year']==year]['n'].sum()/no_vacc[no_vacc['year']==year]['nPolio'].sum())
    """
#Total of each value with index 0,1,...,15 coresponds to years 2000,2001,...,2015
print(total)
print(total_DTP_vulnerable)
print(total_MMR_vulnerable)
print(total_Polio_vulnerable)
perc_MMR_vacc = (np.array(total_MMR_vulnerable)/np.array(total))*100
perc_DTP_vacc = (np.array(total_DTP_vulnerable)/np.array(total))*100
perc_Polio_vacc = (np.array(total_Polio_vulnerable)/np.array(total))*100
print(perc_DTP_vacc)
print(perc_MMR_vacc)
print(perc_Polio_vacc)


Measels_upper = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]

Measels_lower = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

########TESTING##############

output_file("test.html")



plot = figure(title="MMR Polio 2000-2001 to 2015-2016 School Year",x_axis_label = 'years',y_axis_label = 'Percentage of Cases')

plot.line(years,Measels_upper,line_width=1,line_color="green",line_dash=[1,5])
plot.line(years,Measels_lower,line_width=1,line_color="green",line_dash=[1,5])

plot.line(years,perc_Polio_vacc,legend="Polio Unvaccinated",line_width=2,line_color="red")
plot.line(years,perc_MMR_vacc,legend="MMR Vulnerable Children",line_width=2,line_color="blue")

plot.legend.location = "top_left"
plot.legend.click_policy = "mute"

show(plot)




"""
nv00 = no_vacc[no_vacc['year']==2000]
nv01 = no_vacc[no_vacc['year']==2001]
nv02 = no_vacc[no_vacc['year']==2002]
nv03 = no_vacc[no_vacc['year']==2003]
nv04 = no_vacc[no_vacc['year']==2004]
nv05 = no_vacc[no_vacc['year']==2005]
nv06 = no_vacc[no_vacc['year']==2006]
nv07 = no_vacc[no_vacc['year']==2007]
nv08 = no_vacc[no_vacc['year']==2008]
nv09 = no_vacc[no_vacc['year']==2009]
nv10 = no_vacc[no_vacc['year']==2010]
nv11 = no_vacc[no_vacc['year']==2011]
nv12 = no_vacc[no_vacc['year']==2012]
nv13 = no_vacc[no_vacc['year']==2013]
nv14 = no_vacc[no_vacc['year']==2014]
nv15 = no_vacc[no_vacc['year']==2015]

#Total Count Vulnerable Cases, lack of MMR, DTP, or Polio Vaccene

#totals
total00, nMMR00, nDTP00, nPolio00 = nv00['n'].sum(),nv00['n'].sum()-nv00['nMMR'].sum(),nv00['n'].sum()-nv00['nDTP'].sum(),nv00['n'].sum()-nv00['nPolio'].sum()
total00, nMMR00, nDTP00, nPolio00 = nv01['n'].sum(),nv00['n'].sum()-nv01['nMMR'].sum(),nv01['n'].sum()-nv01['nDTP'].sum(),nv01['n'].sum()-nv01['nPolio'].sum()
total00, nMMR00, nDTP00, nPolio00 = nv02['n'].sum(),nv00['n'].sum()-nv02['nMMR'].sum(),nv02['n'].sum()-nv02['nDTP'].sum(),nv02['n'].sum()-nv02['nPolio'].sum()
total00, nMMR00, nDTP00, nPolio00 = nv03['n'].sum(),nv00['n'].sum()-nv03['nMMR'].sum(),nv03['n'].sum()-nv03['nDTP'].sum(),nv03['n'].sum()-nv03['nPolio'].sum()
total00, nMMR00, nDTP00, nPolio00 = nv04['n'].sum(),nv00['n'].sum()-nv04['nMMR'].sum(),nv04['n'].sum()-nv04['nDTP'].sum(),nv04['n'].sum()-nv04['nPolio'].sum()
total00, nMMR00, nDTP00, nPolio00 = nv05['n'].sum(),nv00['n'].sum()-nv05['nMMR'].sum(),nv05['n'].sum()-nv05['nDTP'].sum(),nv05['n'].sum()-nv05['nPolio'].sum()
total00, nMMR00, nDTP00, nPolio00 = nv06['n'].sum(),nv00['n'].sum()-nv06['nMMR'].sum(),nv06['n'].sum()-nv06['nDTP'].sum(),nv06['n'].sum()-nv06['nPolio'].sum()
total00, nMMR00, nDTP00, nPolio00 = nv07['n'].sum(),nv00['n'].sum()-nv07['nMMR'].sum(),nv07['n'].sum()-nv07['nDTP'].sum(),nv07['n'].sum()-nv07['nPolio'].sum()
total00, nMMR00, nDTP00, nPolio00 = nv08['n'].sum(),nv00['n'].sum()-nv08['nMMR'].sum(),nv08['n'].sum()-nv08['nDTP'].sum(),nv08['n'].sum()-nv08['nPolio'].sum()
total00, nMMR00, nDTP00, nPolio00 = nv09['n'].sum(),nv00['n'].sum()-nv09['nMMR'].sum(),nv09['n'].sum()-nv09['nDTP'].sum(),nv09['n'].sum()-nv09['nPolio'].sum()
total00, nMMR00, nDTP00, nPolio00 = nv10['n'].sum(),nv00['n'].sum()-nv10['nMMR'].sum(),nv10['n'].sum()-nv10['nDTP'].sum(),nv10['n'].sum()-nv10['nPolio'].sum()
nv15['n'].sum(),nv15['n'].sum()-nv15['nMMR'].sum(),nv15['n'].sum()-nv15['nDTP'].sum(),nv15['n'].sum()-nv15['nPolio'].sum()


#percentage
print(nv00['n'].sum(),nv00['nMMR'].sum()/nv00['n'].sum(),nv00['nDTP'].sum()/nv00['n'].sum(),nv00['nPolio'].sum()/nv00['n'].sum())
print(nv15['n'].sum(),nv15['nMMR'].sum()/nv15['n'].sum(),nv15['nDTP'].sum()/nv15['n'].sum(),nv15['nPolio'].sum()/nv15['n'].sum())
"""

#studentData.sort_values(by=['school_code','year']).to_csv(index=False)

# Determine where the visualization will be rendered
#output_file('filename.html',title="empty bokeh feature")  # Render to static HTML, or
  # Render inline in a Jupyter Notebook

# Set up the figure(s)
"""
fig = figure(background_fill_color='gray',
             background_fill_alpha=0.5,
             border_fill_color='blue',
             border_fill_alpha=0.25,
             plot_height=300,
             plot_width=500,
             h_symmetry=True,
             x_axis_label='X Label',
             x_axis_type='datetime',
             x_axis_location='above',
             x_range=('2018-01-01', '2018-06-30'),
             y_axis_label='Y Label',
             y_axis_type='linear',
             y_axis_location='left',
             y_range=(0, 100),
             title='Example Figure',
             title_location='right',
             toolbar_location='below',
             tools='save')  # Instantiate a figure() object
"""
# Connect to and draw the data

# Organize the layout

# Preview and save
#show(fig)  # See what I made, and save if I like it
