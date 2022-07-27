#!/usr/bin/env python
# coding: utf-8

# # Data Analysis on Lynchings From 1882-1968

# In[90]:


# source of data: http://archive.tuskegee.edu/repository/wp-content/uploads/2020/11/Lynchings-Stats-Year-Dates-Causes.pdf

# This dataset comes from Tuskegee University


# In[91]:


# Import libraries

import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import folium


# In[92]:


# Import datasets

# Lynching broken down by Crime
lynch_cause_df = pd.read_excel ('Causes Of Lynchings.xlsx')

# Lynching broken down by state and race
lynch_state_race_df = pd.read_excel ('Lynchings By State and Race 1882-1968.xlsx')

# Lynching broken down by year and race
lynch_year_race_df = pd.read_excel ('Lynchings By Year and Race.xlsx')


# In[93]:


# How many years was the data collected?

years_data_collection = 1968-1882


# In[94]:


# Observe the sum

print('Lynching data spans', years_data_collection,'years.')


# # Analysis on Causes of Lynchings

# In[95]:


# Look at dataframe and sort for matplotlib bar chart

lynch_cause_df = lynch_cause_df.sort_values('Count', ascending=False)

# Look at head

lynch_cause_df.head()


# In[96]:


# Total amount of lynching within dataset

lynch_cause_df['Count'].sum()


# In[97]:


#  Bar chart of Lynching by Crime

# Parameters of figure size
plt.rcParams["figure.figsize"] = (14,10)


# Add figure
fig, ax = plt.subplots()

# Add title
fontsize = 20
ax.set_title('Bar Chart ', fontsize=fontsize)

# Add labels
ax.set_xlabel('Crime')
ax.set_ylabel('Count')

# Add variables to visualize
g = ax.bar(lynch_cause_df['Crimes'],lynch_cause_df['Count'])
ax.bar_label(g)

# Display plot
plt.show()


# In[98]:


# Define seaborn colors palette to use
colors = sns.color_palette('pastel')

# Add title
plt.title('Pie Chart of Causes of Lynchings by Crime', pad=76)

# Create Pie Chart
plt.pie(lynch_cause_df['Count'], labels = lynch_cause_df['Crimes'], colors = colors, autopct='%.0f%%')
plt.show()


# # Analysis on Causes of Lynchings By State and Race 

# In[99]:


# Look at dataframe

lynch_state_race_df.head()


# In[100]:


# Change variable name from Total to Lynch Total

lynch_state_race_df.rename(columns = {'Total':'Lynching Total'}, inplace = True)


# In[101]:


# Look at how many states had lynching

lynch_state_race_df_state_count = lynch_state_race_df.State.count()

print('Lynching occurred in', lynch_state_race_df_state_count,'states.')


# In[102]:


# Create a map for Lynch Total


fig = px.choropleth(lynch_state_race_df,
                    locations='State', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='Lynching Total',
                    color_continuous_scale="Viridis_r",
                    )
fig.update_layout(
    title_text = 'Lynching Count by State Total', title_x=0.5,
    geo_scope='usa',
    legend_title="Legend Title"

)

fig.show()


# In[103]:


# Create a map for Whites 

fig_white = px.choropleth(lynch_state_race_df,
                    locations='State', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='White',
                    color_continuous_scale="Viridis_r",
                    )
fig_white.update_layout(
    title_text = 'Lynching Count of Whites Per State', title_x=0.5,
    geo_scope='usa',
    legend_title="Legend Title"

)


fig_black = px.choropleth(lynch_state_race_df,
                    locations='State', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='Black',
                    color_continuous_scale="Viridis_r",
                    )
fig_black.update_layout(
    title_text = 'Lynching Count by Blacks Total', title_x=0.5,
    geo_scope='usa',
    legend_title="Legend Title"

)

fig_white.show()
fig_black.show()


# # Analysis on Lynchings by Year and Race

# In[104]:


# Look at dataframe

lynch_year_race_df.head()


# In[105]:


# Look at the data types

lynch_year_race_df.info()


# In[106]:


# Look at the column names

print(lynch_year_race_df.columns.tolist())


# In[115]:


#  Create time series graph of lynching from 1882-1968

fig = px.line(lynch_year_race_df, x='Year', y=['Whites', 'Blacks'])
  

fig.update_layout(plot_bgcolor = "white", 
                  title_text='Lynchings From 1882-1968 by Race', title_x=0.5,
                  legend_title="Race of Victims",
                  yaxis_title="Count of Lynchings")
fig.show()


# In[ ]:




