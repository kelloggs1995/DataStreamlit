
import streamlit as st 
import streamlit.components.v1 as components
from IPython.core.display import display 
import matplotlib.pyplot as plt  
from streamlit.components.v1 import html
import pandas as pd



# Page Config
st.set_page_config(page_title="Above our heads",
                   page_icon=":rocket:",
                   layout="wide")
st.markdown(""" <style>
footer {visibility: hidden;}

</style> """, unsafe_allow_html=True)

# Header for site
st.header("Space DashBoard Data Viz ") 

# Adding dark theme 
plt.style.use("dark_background")



# Loading Data Frame
data = pd.read_csv("./vgsales.csv")


# # 1 Some Basic information about data like total number of entries
i0, i1, i2, i3= st.columns(4)# 4 containers in a row 

# Single digit stories 
i0.metric("How Many people in Space",(data['People'].sum()))
i1.metric("What country has sent the most people into space", "USA")
i2.metric("Longest time in space", max(data['Flight_Time']),"","normal","dddd/hh/mm")
i3.metric("Total people to reach space", len(data['Name'].unique()))

# # 2 Bar Race
components.iframe('https://public.flourish.studio/visualisation/12145846/',height=600)

# # 3 double Pie charts about satellites
# Satellites section 
    # creating containers for Piecharts  
left, right = st.columns(2)  
        #Left column 
left.subheader("Satellites by Country")
left._iframe('https://flo.uri.sh/visualisation/12164595/embed',height=550)
        #Right coloumn 
right.subheader("Satellites Function")
right._iframe('https://flo.uri.sh/visualisation/12165039/embed',height=550)

# # 4 Extra to break up the data and add somthing else to the site 
# Live video Feed 
    #creating containers for embeding
left, right = st.columns(2)
        #Left column 
left.subheader("ISS Earth Viewing")
left._iframe('https://www.ustream.tv/embed/17074538?html5ui=1&amp;autoplay=true&amp;volume=0&amp;muted=1" scrolling="no" allowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen" frameborder="0"',height=270)
        #Right column
right.subheader("ISS Stream")
right._iframe('https://www.ustream.tv/embed/9408562?html5ui=1&amp;autoplay=true&amp;volume=0&amp;muted=1&amp;wmode" scrolling="no" allowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen" frameborder="0"',height=270)

# # 5 Map for Launches by Country
st.subheader("Launches by Country")
components.iframe('https://flo.uri.sh/visualisation/12177845/embed', height=600)

# # 6 Filtered Line Graph 
st.subheader("Mission outcome by year")
components.iframe('https://flo.uri.sh/visualisation/12174068/embed', height=600 )
