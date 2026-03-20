import streamlit as st
import folium
from streamlit_folium import st_folium

def show_map():

    st.header("🗺 GIET Campus Map")

    m = folium.Map(location=[17.064486, 81.866150], zoom_start=15)

    folium.Marker(
        [17.064486, 81.866150],
        popup="GIET Campus, Rajahmundry"
    ).add_to(m)

    st_folium(m,width=700)