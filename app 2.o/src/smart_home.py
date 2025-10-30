import streamlit as st
import pandas as pd
import random
from twilio.rest import Client

# ------------------- Twilio Setup -------------------
ACCOUNT_SID = "AC6c7690f9d0b31b8d1873288a5968f28a"
AUTH_TOKEN = "153d3f795a940e42e15f3bc671a49da8"
TWILIO_PHONE = "+19788833751"
USER_PHONE = "+918919146448"  # Replace with your number

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_sms_alert(message):
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE,
        to=USER_PHONE
    )

def smart_home_page():
    st.title("🏠 EcoSense Smart Home - Energy & Water Control")

    appliances = {
        "Light": {"status": False, "usage": 0},
        "Fan": {"status": False, "usage": 0},
        "Washing Machine": {"status": False, "usage": 0},
        "Heater": {"status": False, "usage": 0},
        "Water Pump": {"status": False, "usage": 0}
    }

    if "data" not in st.session_state:
        st.session_state.data = appliances.copy()

    col1, col2 = st.columns(2)
    with col1:
        power_limit = st.number_input("⚡ Power Cutoff Limit (kWh)", 0, 1000, 200)
        water_limit = st.number_input("💧 Water Cutoff Limit (Liters)", 0, 1000, 500)
    with col2:
        st.markdown("### Appliance Controls")

    # Toggle appliances
    for appliance, info in st.session_state.data.items():
        c1, c2 = st.columns([3, 1])
        c1.write(f"**{appliance}**")
        toggle = c2.toggle("Active", value=info["status"], key=appliance)
        st.session_state.data[appliance]["status"] = toggle

    # Simulate usage
    total_power = 0
    total_water = 0
    for appliance, info in st.session_state.data.items():
        if info["status"]:
            power_usage = random.randint(5, 20)
            water_usage = random.randint(1, 10) if "Water" in appliance else 0
            info["usage"] += power_usage + water_usage
        total_power += info["usage"]
        total_water += info["usage"] if "Water" in appliance else 0

    st.markdown("### 📊 Current Usage Summary")
    df = pd.DataFrame(
        [(a, "ON" if d["status"] else "OFF", d["usage"]) for a, d in st.session_state.data.items()],
        columns=["Appliance", "Status", "Usage (units)"]
    )
    st.dataframe(df)

    # ------------------- Alerts -------------------
    alert_message = ""
    if total_power > power_limit:
        alert_message += f"⚡ Power usage crossed limit ({total_power} > {power_limit})\n"
    if total_water > water_limit:
        alert_message += f"💧 Water usage crossed limit ({total_water} > {water_limit})\n"

    if alert_message:
        st.warning(alert_message)
        try:
            send_sms_alert(f"🚨 EcoSense Alert:\n{alert_message}")
            st.success("📱 SMS Notification Sent via Twilio!")
        except Exception as e:
            st.error(f"Twilio Error: {e}")
