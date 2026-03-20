import streamlit as st
import json

def show_branches():

    st.header("🎓 Branch Explorer")

    with open("giet_data.json") as f:
        data = json.load(f)

    branches = [i["branch"] for i in data]

    selected = st.selectbox("Select Branch",branches)

    for b in data:
        if b["branch"] == selected:
            st.subheader(b["branch"])
            st.write(b["description"])
            st.success(f"Fee: ₹{b['fee']}")