import streamlit as st

def show_facilities():

    st.header("🏫 Campus Facilities")

    facilities = [
        "Central Library",
        "Modern Computer Labs",
        "Hostels",
        "Sports Grounds",
        "Canteens",
        "NCC",
        "Transport"
    ]

    for f in facilities:
        st.success(f)