import streamlit as st

def check_usage_alerts(power, water, power_limit=200, water_limit=500):
    alerts = []
    if power > power_limit:
        alerts.append(f"⚡ Power usage exceeded limit ({power}/{power_limit} kWh)")
    if water > water_limit:
        alerts.append(f"💧 Water usage exceeded limit ({water}/{water_limit} Liters)")

    if alerts:
        for a in alerts:
            st.warning(a)
    else:
        st.success("✅ All usage levels are within safe limits.")
