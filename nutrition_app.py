import streamlit as st #web app
import pandas as pd #data manipulation
import numpy as np
import plotly.express as px #visualizations
import plotly.graph_objects as go #visualizations


st.set_page_config(
     page_title="nutrition_app.py",
     layout="wide",
     initial_sidebar_state="expanded",
     )

BMI=pd.read_csv("BMI.csv")
BMI=BMI.drop(BMI.columns[[0]], axis=1)
#st.write(BMI)

Obesity=pd.read_csv("Obesity.csv")
Obesity=Obesity.drop(Obesity.columns[[0]], axis=1)
#st.write(Obesity)

Underweight=pd.read_csv("final_underweight.csv")
Underweight=Underweight.drop(Underweight.columns[[0]], axis=1)
#st.write(Underweight)



st.title("Body Mass Index (BMI) Dashboard")
from PIL import Image
image = Image.open('bmi6.jpg')
st.image(image)



st.sidebar.title("Visualization Selector")
#st.sidebar.markdown("Select the Charts accordingly:")
st.subheader("This interactive dashboard will visualize the world's nutritional status in terms of Body Mass Index, Obesity, and Underweight of adults across different regions at different periods of time")


st.markdown("## Key Facts related to the World's Adults in 2016")

metric1, metric2, metric3=st.columns(3)
metric1.metric(label="Overweight among adults", value="1.9B")
metric2.metric(label="Obesity among adults", value="650M")
metric3.metric(label="Underweight among adults", value="462M")

dataset_name=st.radio("Select Dataset", ("BMI", "Obesity", "Underweight"))
if not st.checkbox("Hide", True, key='3'):
	if dataset_name=="BMI":
		st.subheader("Average BMI (kg/m²) among Adults per Region over the Years")
		st.write("This dataset, collected from WHO website, shows the average BMI among adults per region from the year 1975 till the year 2016." )
		st.write(BMI)


	if dataset_name=="Obesity":
		st.subheader("Prevalence of Obesity (%) among Adults per Region in 2016")
		st.write("This dataset, collected from WHO website, shows the prevalence of obesity among adults per region in 2016.")
		st.write(Obesity)

	if dataset_name=="Underweight":
		st.subheader("Prevalence of Underweight (%) among Adults per Region in 2016")
		st.write("This dataset, collected from WHO website, shows the prevalence of underweight among adults per region in 2016.")
		st.write(Underweight)


select=st.sidebar.selectbox('Select Visualization Type',['Line Chart-BMI', 'Bar Chart-Obesity', 'Pie Chart-Underweight'], key= "1")
if not st.sidebar.checkbox("Hide", True, key='2'):
	if select=="Bar Chart-Obesity":
		st.subheader("Prevalence of Obesity (%) among Adults per Region for the Year 2016")
		fig= px.bar(Obesity, x=Obesity["Region"], y=Obesity["Percentage of Obesity (%)"], color=Obesity["Region"], range_y=[0,35], text="Percentage of Obesity (%)")
		st.plotly_chart(fig)
		st.write("The Western Pacific region ranks first in terms of the highest prevalence of obesity among its adult citizens followed by Eastern Mediterranean, Americas and Europe. South-East Asia and Africa witness the lowest percentages of Obesity among their adult citizens in 2016")
	
	if select == 'Line Chart-BMI':
		st.subheader("Pattern of Average BMI (kg/m²) across Different Regions over Time")
		fig=px.line(BMI, x=BMI["Year"], y=BMI["Average BMI (kg/m²)"], color=BMI["Region"])
		fig.update_layout(xaxis_title="Years", yaxis_title="Average BMI (kg/m²)")
		fig.update_xaxes(range=[1975, 2016])
		st.plotly_chart(fig)
		st.write("As we can see in the above line chart, there is an upward sloping trend in the Average BMI (kg/m²) for both sexes across all regions from the year 1975 till the year 2015. We can also see that in the most recent years, Western Pacific and Americas regions witness the highest average BMI for both sexes followed by Eastern Mediterranean and Europe. The regions with the lowest average BMI are Africa and Southeast Asia with an average BMI that does not exceed 24 (kg/m²). Compared to the average health range of adult BMI which is between 18.5 and 24.9  (kg/m²), we can say that the Western Pacific, Americas, Eastern Mediterranean and Europe are on the upper end of the healthy range (closer to overweight population) while Africa and SouthEast Asia are closer to the lower end of the healthy range (closer to underweight population")

	if select== "Pie Chart-Underweight":
		st.subheader("Prevalence of Underweight (%) per Region in 2016")
		fig= px.pie(Underweight, values='Percentage of Underweight (%)', names='Region',
             hover_data=['Percentage of Underweight (%)'], labels={'Percentage of Underweight (%)':'% of Underweight'})
		st.plotly_chart(fig)
		st.write("The South-East Asian region ranks first in terms of the highest prevalence of underweight among its adult citizens followed by Africa, Eastern Mediterranean and Western Pacific. Americas and Europe witness the lowest percentages of Underweight among their adults in 2016")
