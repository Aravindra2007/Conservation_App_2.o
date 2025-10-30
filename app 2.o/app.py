import streamlit as st
from src.analyze_usage import analyze_usage
from src.recommendations import get_recommendations
from src.alerts import check_usage_alerts
from src.smart_home import smart_home_page

st.set_page_config(page_title="EcoSenseAI Dashboard", layout="wide")

st.sidebar.title("🌿 EcoSenseAI Navigation")
page = st.sidebar.radio("Select Page", [
    "Dashboard",
    "Usage Analysis",
    "Smart Home Control"
])

if page == "Dashboard":
    st.title("🌿 EcoSenseAI: AI for Energy & Water Conservation")
    st.write("""
        Welcome to EcoSenseAI — your intelligent system for conserving 
        **water** and **electrical energy** through smart monitoring and automation.
    """)
    st.info("Use the sidebar navigate to Pages.")

elif page == "Usage Analysis":
    analyze_usage()

elif page == "Smart Home Control":
    smart_home_page()
