import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def show_dashboard():
    # Background Image CSS
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('assets/giet_clg.png');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Background Image CSS
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('assets/giet_clg.png');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Header
    st.markdown(
        """
        <h1 style='text-align:center;color:#1976D2'>
        🎓 GIET Smart Campus Dashboard
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # Filters
    st.sidebar.header("Filters")
    years = ["2021", "2022", "2023", "2024"]
    selected_year = st.sidebar.selectbox("Select Year", years, index=len(years)-1)
    departments = [
        "CSE", "CSE AIML", "CSE DS", "Cyber Security", "IT", "ECE", "EEE", "Mechanical", "Civil"
    ]
    selected_dept = st.sidebar.multiselect("Select Departments", departments, default=departments)

    # Simulate dynamic data
    import numpy as np
    np.random.seed(42)
    dept_students = np.random.randint(300, 1300, size=len(departments))
    total_students = dept_students.sum()
    placement_rate = np.random.randint(75, 90)
    companies_visiting = np.random.randint(100, 140)

    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Departments", f"{len(departments)}")
    col2.metric("Students", f"{total_students}")
    col3.metric("Companies Visiting", f"{companies_visiting}")
    col4.metric("Placement Rate", f"{placement_rate}%")

    st.markdown("---")

    # Department Data
    data = pd.DataFrame({
        "Department": departments,
        "Students": dept_students
    })
    if selected_dept:
        data = data[data["Department"].isin(selected_dept)]

    col1, col2 = st.columns(2)

    # Action Buttons
    st.sidebar.markdown("---")
    if st.sidebar.button("Refresh Data"):
        st.experimental_rerun()
    download = st.sidebar.button("Download Report")
    toggle_view = st.sidebar.radio("Chart View", ["3D", "2D"], index=0)

    # Bar Chart
    with col1:
        fig = px.bar(
            data,
            x="Department",
            y="Students",
            color="Department",
            title="📊 Department Strength",
            template="plotly_dark"
        )
        fig.update_traces(marker_line_width=2, marker_line_color="white")
        st.plotly_chart(fig, width='stretch')

    # Pie Chart
    with col2:
        fig2 = px.pie(
            data,
            names="Department",
            values="Students",
            title="🎓 Student Distribution",
            template="plotly_dark"
        )
        fig2.update_traces(textinfo='percent+label')
        st.plotly_chart(fig2, width='stretch')

    # Extra Feature: Data Table
    st.markdown("### Department Data Table")
    st.dataframe(data, use_container_width=True)

    st.markdown("---")

    # Placement Data (simulate)
    companies = ["TCS", "Infosys", "Wipro", "Capgemini", "Accenture", "Cognizant", "IBM", "Tech Mahindra"]
    students_placed = np.random.randint(50, 180, size=len(companies))
    placement = pd.DataFrame({
        "Company": companies,
        "Students Placed": students_placed
    })

    col3, col4 = st.columns(2)

    # Placement Bar
    with col3:
        fig3 = px.bar(
            placement,
            x="Company",
            y="Students Placed",
            color="Company",
            title="💼 Top Recruiters",
            template="plotly_dark"
        )
        fig3.update_traces(marker_line_width=2, marker_line_color="white")
        st.plotly_chart(fig3, width='stretch')

    # Placement Trend (simulate)
    with col4:
        placement_trend = np.random.randint(60, 95, size=len(years))
        fig4 = go.Figure()
        fig4.add_trace(
            go.Scatter(
                x=years,
                y=placement_trend,
                mode="lines+markers",
                line=dict(color="cyan", width=4),
                marker=dict(size=8, color=placement_trend, colorscale="Cividis")
            )
        )
        fig4.update_layout(
            title="📈 Placement Growth Trend",
            template="plotly_dark",
            xaxis_title="Year",
            yaxis_title="Placement Rate"
        )
        st.plotly_chart(fig4, width='stretch')

    st.markdown("---")

    # Extra Feature: Info Popup
    if st.button("Show Dashboard Info"):
        st.info("This dashboard provides a 3D interactive view of campus data, placements, and department stats. Use sidebar filters and toggles for customization.")

    st.info(f"Showing data for year: {selected_year}")
    st.success("GIET Smart Campus AI Dashboard Active 🚀")