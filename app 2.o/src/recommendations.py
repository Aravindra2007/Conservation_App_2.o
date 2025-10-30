import streamlit as st

def get_recommendations():
    st.title("💡 Energy & Water Saving Recommendations")

    recommendations = [
        "Use LED bulbs instead of incandescent ones.",
        "Turn off fans and lights when not in use.",
        "Schedule washing machines for non-peak hours.",
        "Fix leaky taps to prevent water wastage.",
        "Use smart plugs to automate power control.",
        "Install low-flow showerheads and faucets.",
        "Monitor water pump run-time regularly.",
        "Use solar-powered heaters if possible.",
        "Unplug chargers and devices not in use.",
        "Use rainwater harvesting for gardening."
    ]

    for rec in recommendations:
        st.write(f"✅ {rec}")
