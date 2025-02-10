import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from backend import get_data

# Add title,text input , slider , selectbox and subheader
st.title("Weather forcast for next Days")
place = st.text_input("Place: ")
days= st.slider("Forecast Days: ", 1, 5,help="Select the number of forcasted days.")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        # Get the temperature/sky
        filtered_data= get_data(place,days)

        # Create the plot
        if option=="Temperature":
            t= [dict["main"]["temp"]/10 for dict in filtered_data]
            d =[dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=d, y=t,labels={"x": "Date", "y": "Temperature"})        
            st.plotly_chart(figure)
        if option=="Sky":
            images = {"Clear":"app7_weather_forcast_data_app/images-3/clear.png","Clouds":"app7_weather_forcast_data_app/images-3/cloud.png",
                    "Rain":"app7_weather_forcast_data_app/images-3/rain.png","Snow":"app7_weather_forcast_data_app/images-3/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            images_path = [images[condition] for condition in sky_conditions]
            
            st.image(images_path,width=115)
            
    # Except block for the Location that does not exist.
    except KeyError:
        st.write("Place does not exist.")
        
     

    
