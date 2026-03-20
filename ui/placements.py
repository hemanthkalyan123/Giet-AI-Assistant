import streamlit as st
import pandas as pd
import plotly.express as px

def show_placements():

    st.header("💼 Placement Analytics")

    data = pd.DataFrame({
        "Company":["TCS","Infosys","Wipro","Capgemini","Accenture"],
        "Students Placed":[120,90,70,60,55]
    })

    fig = px.pie(
        data,
        names="Company",
        values="Students Placed",
        title="Placements by Company"
    )

    st.plotly_chart(fig,use_container_width=True)