# -*- coding: utf-8 -*-
"""
Created on Mon May 11 02:37:09 2020

@author: DELL
"""

from plotly.offline import plot
import plotly.graph_objects as go
import pandas as pd

df=pd.read_csv('F:\Dropbox\Conferences\Proposal\Data\Emission index_highway.csv')
df.head()

# color scale
#scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
#            [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]

scl = [(0,"white"), (0.5,"yellow"), (1,"red")] 

fig = go.Figure(data=go.Choropleth(
    locations=df['State'], # Spatial coordinates
    z = df['EI_EV'], # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
#    text=df['State'],  #hover text
    autocolorscale=False,
    colorscale = scl,
#    colorscale = 'reds',
    reversescale=False,
#    marker_line_color='darkgray', 
    marker_line_color='black',  # line markers between states
    marker_line_width=0.5,
    #colorbar properties
    colorbar=dict(thickness=20,
                  ticklen=3, tickcolor='black',
                  ticks = 'outside',
                  len = 0.8,  # colorbar length
                  x = 0.8,  # move the colorbar w.r.t x axis; value between or equal to -2 and 3
                  xpad = 0,  # Sets the amount of padding (in px) along the x direction.
                  ypad = 0,
                  tickfont=dict(size=14, color='black'),
                  title = "Emission Index",  # colorbar title
                  titlefont=dict(size=16, color='blue')  # colorbar title properties
                  ),
))



fig.update_layout(
#    title_text = 'CO2 emission index of the US states',
    geo = dict(
    scope='usa', # limite map scope to USA
    showlakes=False, # lakes

    lakecolor='white'),       
)


plot(fig)

##save figure
#fig.write_image("fig1.jpeg")


#%%
from plotly.offline import plot
import pandas as pd

df=pd.read_csv('F:\Dropbox\Conferences\Proposal\Data\Emission index_highway.csv')
df.head()

# color scale
scl = [(0,'rgb(35, 122, 17)'), (0.5,'yellow'), (1,'red')]
#scl = [(0,'rgb(35, 122, 17)'), (0.5,'yellow'), (1,'rgb(241, 135, 15)')]  

data = [ dict(
        type = 'choropleth',
        locations=df['State'], # Spatial coordinates
        z = df['EI_PHEV'], # Data to be color-coded
        locationmode = 'USA-states', # set of locations match entries in `locations`
        text = df['State'],
        autocolorscale=False,
        colorscale = scl,
    #    colorscale = 'reds',
        reversescale=False,
    #    marker_line_color='darkgray', 
        marker_line_color='black',  # line markers between states
        marker_line_width=0.5,
        #colorbar properties
        colorbar=dict(thickness=20,
                      ticklen=3, tickcolor='black',
                      ticks = 'outside',
                      len = 0.8,  # colorbar length
                      x = 0.1,  # move the colorbar w.r.t x axis; value between or equal to -2 and 3
                      xpad = 0,  # Sets the amount of padding (in px) along the x direction.
                      ypad = 0,
                      tickfont=dict(size=14, color='black'),
                      title = "Emission Index <br> Color Scale",  # colorbar title
                      titlefont=dict(size=16, color='blue')  # colorbar title properties
                      ),
      ),
        ## create a scatter plot to show the state names
        dict(type = 'scattergeo',
             locations = df['State'],
             locationmode = 'USA-states',
             text = df['State'],
             mode = 'text'),
        
        ]



layout = dict(
        title = "<b>CO2 emission index of the US states (PHEV)<b>",  # <b> is a html tag to make the text bold
        titlefont=dict(size =25, color='black', family='Arial, sans-serif'),
        geo = dict(
        scope='usa', # limite map scope to USA
        showframe = False,
        showcoastlines = False,
        showlocations=False,
        showland=False,
        landcolor='#f0f0f0',
        showlakes=False,
        lakecolor='white'
        ),       

    )


fig = dict(data=data, layout=layout)
plot(fig, validate=False, filename='emission index plot')



