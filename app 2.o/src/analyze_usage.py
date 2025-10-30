import streamlit as st
import pandas as pd
import random

def analyze_usage():
    st.title("📈 Energy & Water Usage Analysis")

    # Simulated weekly data
    data = {
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Power (kWh)": [random.randint(100, 300) for _ in range(7)],
        "Water (Liters)": [random.randint(200, 600) for _ in range(7)]
    }
    df = pd.DataFrame(data)

    st.line_chart(df.set_index("Day"))
    st.dataframe(df)

    total_power = df["Power (kWh)"].sum()
    total_water = df["Water (Liters)"].sum()

    st.success(f"✅ Total Power Usage: {total_power} kWh")
    st.success(f"✅ Total Water Usage: {total_water} Liters")
