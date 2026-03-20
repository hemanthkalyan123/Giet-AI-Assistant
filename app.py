import streamlit as st

from ui.dashboard import show_dashboard
from ui.branches import show_branches
from ui.facilities import show_facilities
from ui.placements import show_placements
from ui.map import show_map
from rag_agent import ask_giet_ai

st.set_page_config(
    page_title="GIET Smart Campus AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 GIET Smart Campus AI Assistant")

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "AI Assistant",
        "Voice Assistant",
        "Branch Explorer",
        "Facilities",
        "Placements",
        "Campus Map",
        "About GIET"
    ]
)

if menu == "Dashboard":
    show_dashboard()

elif menu == "AI Assistant":
    st.header("🤖 GIET AI Chatbot")

    question = st.text_input("Ask anything about GIET")

    if question:
        response = ask_giet_ai(question)
        st.success(response)

elif menu == "Voice Assistant":
    show_voice_ai()

elif menu == "Branch Explorer":
    show_branches()

elif menu == "Facilities":
    show_facilities()

elif menu == "Placements":
    show_placements()

elif menu == "Campus Map":
    show_map()

elif menu == "About GIET":
    st.image("assets/campus.jpg")
    st.write("""
    Godavari Institute of Engineering and Technology (GIET)
    is located in Rajahmundry and is affiliated with JNTU Kakinada.

    The campus offers modern labs, hostels, sports facilities,
    placement training and technical events.
    """)


    st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
color:white;
}

[data-testid="metric-container"]{
background-color:#1e1e1e;
border-radius:10px;
padding:15px;
box-shadow:0px 0px 10px rgba(0,0,0,0.5);
}

</style>
""", unsafe_allow_html=True)